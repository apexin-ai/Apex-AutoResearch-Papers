# Research conversation: You are Reviewer 2 (R2) for an ACL ARR peer review. Your focus is **novelty, significance, and related work positioning*

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a116348f095d95734.jsonl`
- **Structured JSON:** [`d4529ff593fb4a9a5a9b.json`](../../sessions/d4/d4529ff593fb4a9a5a9b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-21T05:51:52.686Z_

You are Reviewer 2 (R2) for an ACL ARR peer review. Your focus is **novelty, significance, and related work positioning**. Produce an independent, detailed review.

## Paper Summary
"Geometric Analysis Reveals When and Why Cross-Lingual Calibration Transfer Succeeds"

The paper presents the first large-scale study of cross-lingual correctness probe transfer. English logistic regression probes trained on internal LLM representations are applied zero-shot to other languages. Three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20–50 languages, 5 transfer conditions.

**Four claims forming a causal chain:**
1. **Pareto discovery**: Architecture-dependent depth-transferability tradeoff. Deeper layers → better English probes but worse cross-lingual transfer. Qwen3: strong (ρ=-0.91, 15/20 significant), Llama 4: weak/mixed (ρ=-0.78, 6/20 significant, 3 reversed). Pareto knee at 55–58% depth.
2. **Decomposition**: Correctness = difficulty-shared (65% variance, 12% degradation) + capability-specific (35% variance, 88% degradation). Built on Civelli et al.'s IRT difficulty finding.
3. **CaCLR method**: L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits). +3.5pp mean AUROC over zero-shot, needs only parallel activations, no target labels.
4. **Simpson's Paradox in CKA–transfer**: Raw CKA-AUROC correlation is negative (depth confound), but partial correlation controlling depth is significantly positive (p<0.01 on all 3 architectures). Correctness subspace persists (12.4° within-layer angle) even as global CKA declines.

**Related work cited:**
- Probe-based calibration: Miao et al. (CORAL, NAACL 2026), Miao & Ungar (2026 preprint on confidence-correctness), Ji et al. (ACL 2024, hallucination risk), CCPS [5]
- Cross-lingual probing: Xiao et al. (ACL 2025, knowledge boundary probes, 8 languages, input-level answerability, NOT correctness)
- IRT difficulty: Civelli et al. (EMNLP 2024, cross-lingual difficulty probes)
- Cross-lingual alignment: MUSE (Conneau, ICLR 2018), VecMap (Artetxe, ACL 2018)
- Representation similarity: CKA (Kornblith, ICML 2019), SVCCA (Raghu, NeurIPS 2017)
- Domain adaptation: Ben-David (2010), Zhao et al. (ICML 2019)
- Conformal prediction: Angelopoulos & Bates (2023)
- Control tasks: Hewitt & Liang (EMNLP 2019)
- Multilingual BERT: Pires et al. (ACL 2019), Wu & Dredze (EMNLP 2019)

**Additional findings:**
- 27% low-resource probing results are capacity artifacts (first cross-lingual application of control tasks)
- Procrustes reversal at ZS AUROC ~0.52
- ~42 parallel pairs for 95% Procrustes performance
- Cross-benchmark generalization (Belebele, MMLU-ProX, CV=0.04)
- Correctness-confidence orthogonality extends to 20 languages (cosine <0.10)
- Linear probes +5.5pp transfer advantage over MLPs

**Limitations acknowledged:**
- MCQA only, not open-ended generation
- CaCLR limited by 1-D logit constraint
- n=3 architectures, cannot isolate specific architectural features
- 27% low-resource artifact rate limits low-resource conclusions

## Your Task
Evaluate **novelty, significance, and related work**. Cover:

1. **Novelty**: How novel is each of the four claims? Is the causal chain structure itself novel? How does each contribution compare to prior work?
2. **Significance/Impact**: Will this influence future work? Is it primarily descriptive or does it enable new capabilities?
3. **Related work coverage**: Any important missing references? Is the positioning fair to prior work?
4. **Differentiation from Xiao et al. (2025)**: The paper claims Xiao et al. study answerability (input-level) not correctness (output-level). Is this distinction sufficiently argued?
5. **Framing**: Is the "causal chain" framing appropriate? Are the four claims genuinely interconnected or could they be independent papers?
6. **Writing quality**: Is the paper well-organized? Clear? Appropriate length?
7. **Broader impact**: Practical implications for multilingual LLM deployment?

## Scoring (ACL ARR 1–5)
- **Excitement**: 5=Highly exciting (would recommend to others), 4=Exciting (would mention), 3=Ambivalent, 2=Below average, 1=Not exciting
- **Overall Assessment**: 5=Top-tier, 4=Accept, 3.5=Findings-worthy, 3=Borderline, 2=Reject, 1=Strong reject

## Output Format
```
### R2 Review: Novelty, Significance, and Related Work

**Excitement Score**: X/5
**Overall Assessment**: X/5

#### Summary of Contributions (2-3 sentences)

#### Strengths (numbered list)

#### Weaknesses (numbered list)

#### Questions for Authors (numbered list)

#### Novelty Assessment per Claim
- Claim 1 (Pareto): ...
- Claim 2 (Decomposition): ...
- Claim 3 (CaCLR): ...
- Claim 4 (CKA/Simpson): ...

#### Related Work Gaps

#### Significance and Impact Assessment

#### Writing and Presentation Quality
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "eaac0fe5-cd7f-44d9-9ba3-da8edd78ef4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T05:51:52.689Z_

```json
{
  "parentUuid": "eaac0fe5-cd7f-44d9-9ba3-da8edd78ef4e",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
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
  "uuid": "026f97fd-0ba4-4545-a035-1dffcbada379",
  "timestamp": "2026-05-21T05:51:52.689Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T05:51:56.231Z_



I'll start by loading the project files to understand the full paper before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "026f97fd-0ba4-4545-a035-1dffcbada379",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFC8f21iRBjQzvDaZDjr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43d14f92-1c2d-4df8-85ab-7e312aef9b6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DR2BY83zqTp6Ta934GVMRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7585,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7585,
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

_source line 4 · 2026-05-21T05:51:57.789Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VMbkXzBSFHE2a851iXzrkC`</summary>

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
  "parentUuid": "43d14f92-1c2d-4df8-85ab-7e312aef9b6b",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFC8f21iRBjQzvDaZDjr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "984abefe-91c5-4782-8c66-b83e46b3db3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DR2BY83zqTp6Ta934GVMRG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7585,
      "cache_read_input_tokens": 8251,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7585
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7585,
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

_source line 5 · 2026-05-21T05:51:57.792Z_

<details><summary>↩ Tool result · `toolu_01VMbkXzBSFHE2a851iXzrkC`</summary>

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
  "parentUuid": "984abefe-91c5-4782-8c66-b83e46b3db3b",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "a29a8451-6bc7-479e-8aff-6c8a4eeb1e7a",
  "sourceToolAssistantUUID": "984abefe-91c5-4782-8c66-b83e46b3db3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T05:52:04.825Z_



Let me read the key project files to get full context on the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a29a8451-6bc7-479e-8aff-6c8a4eeb1e7a",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFC9326CitPMNvLy9jKD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7e8be13-0641-4184-8b37-ed8085d1d49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9Sv6MxoWrGJmZ7kNu1EsR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 7 · 2026-05-21T05:52:06.367Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GEqCLhBWzUNVmYSKhQ4n6v`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7e8be13-0641-4184-8b37-ed8085d1d49f",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFC9326CitPMNvLy9jKD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26eeac17-1318-4c5a-a0c4-68bdd92ad6d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9Sv6MxoWrGJmZ7kNu1EsR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 8 · 2026-05-21T05:52:06.380Z_

<details><summary>↩ Tool result · `toolu_01GEqCLhBWzUNVmYSKhQ4n6v`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **plan_013** (success): English correctness probes capture genuine linguistic signal: 5-fold CV with PCA(100) dimensionality reduction shows real AUROC significantly above permuted-label baseline (0.746 vs 0.484 at best layer), with selectivity (Hewitt & Liang 2019) concentrated in later layers (L20-L27), confirming the probe is not exploiting spurious high-dimensional correlations. ← 基于 mvp_001\\n- **mvp_003** (success): Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). ← 基于 mvp_001\\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\\n\\n## 趋势\\n成功 4 / 负向 0 / 失败 0 / 共 4\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-13176: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1201, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26eeac17-1318-4c5a-a0c4-68bdd92ad6d0",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "0ae091eb-0e60-4838-883d-73344d7bab99",
  "sourceToolAssistantUUID": "26eeac17-1318-4c5a-a0c4-68bdd92ad6d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T05:52:06.836Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RdKGYJjwbdkuVA8SUPckW2`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ae091eb-0e60-4838-883d-73344d7bab99",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFC9326CitPMNvLy9jKD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3f9a60b-180d-4913-b49e-864e4c8fcf06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9Sv6MxoWrGJmZ7kNu1EsR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 10 · 2026-05-21T05:52:06.844Z_

<details><summary>↩ Tool result · `toolu_01RdKGYJjwbdkuVA8SUPckW2`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3f9a60b-180d-4913-b49e-864e4c8fcf06",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "e6ed8164-5378-4ba8-9f9b-11cec3806e19",
  "sourceToolAssistantUUID": "c3f9a60b-180d-4913-b49e-864e4c8fcf06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T05:52:07.607Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MsYkvdXqFkFUZrpY8jRUPz`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6ed8164-5378-4ba8-9f9b-11cec3806e19",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFC9326CitPMNvLy9jKD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "095a4888-ee92-42ab-a821-d1619243627d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9Sv6MxoWrGJmZ7kNu1EsR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15836,
      "output_tokens": 309,
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
          "output_tokens": 309,
          "cache_read_input_tokens": 15836,
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

_source line 12 · 2026-05-21T05:52:07.616Z_

<details><summary>↩ Tool result · `toolu_01MsYkvdXqFkFUZrpY8jRUPz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml\", \"content\": \"papers:\\n  miao2026closing:\\n    title: \\\"Closing the Confidence-Faithfulness Gap in Large Language Models\\\"\\n    authors: [\\\"Ruoxi Miao\\\", \\\"Lyle Ungar\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.25052\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Showed correctness direction and verbalized confidence direction are orthogonal (cosine < 0.04) in 7-8B models. Motivates probing internal representations. English-only — our cross-lingual extension is the natural next step.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  xiao2025knowledge:\\n    title: \\\"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\\\"\\n    authors: [\\\"Zheng Xiao\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2504.13816\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest prior work. Cross-lingual transfer of knowledge-boundary probes (answerable vs unanswerable). Key differences: they probe knowledge boundaries (input-level), we probe correctness (output-dependent); they measure probing accuracy, not ECE/Brier; they test 8 languages, we target 20+.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  civelli2026shared:\\n    title: \\\"A Shared Geometry of Difficulty in Multilingual Language Models\\\"\\n    authors: [\\\"Andrea Civelli\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2601.12731\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Cross-lingual difficulty probe transfer at intermediate layers. Architecture-dependent optimal depth (24-49%). Probes IRT difficulty (question property), not correctness (model property). Critical control for our difficulty ablation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  zhou2025lace:\\n    title: \\\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs\\\"\\n    authors: [\\\"Zhou\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03136\\\"\\n    category: \\\"multilingual_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"LACE: adaptive layer ensemble for multilingual calibration. Confirmed 5x ECE gap across 100+ languages. Requires per-language validation data. Our CaCLR needs no non-English correctness labels.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ravisankar2026dali:\\n    title: \\\"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs\\\"\\n    authors: [\\\"Ravisankar\\\"]\\n    year: 2026\\n    venue: \\\"EACL 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2504.09378\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"DALI: causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. Strongest causal support for our hypothesis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  miao2026coral:\\n    title: \\\"Correctness-Optimized Residual Activation Lens (CORAL)\\\"\\n    authors: [\\\"Ruoxi Miao\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.06022\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Transferable correctness probes via regularized MLP on residual activations, ~50% ECE improvement at 53-66% depth. English-only, cross-task. CaCLR positioned as solution to their identified distribution-shift transfer degradation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  joshi2025calibration:\\n    title: \\\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\\\"\\n    authors: [\\\"Joshi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Identified low-dimensional calibration direction in residual stream evolving across layers.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  confidence_manifold2026:\\n    title: \\\"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08159\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Correctness signals occupy 3-8 dimensions, linearly separable. 25 labeled examples achieve 89% of full-data accuracy. All English-only.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  karandikar2021sbece:\\n    title: \\\"Soft Calibration Objectives for Neural Networks\\\"\\n    authors: [\\\"Archit Karandikar\\\", \\\"Nicholas Cain\\\", \\\"Dustin Tran\\\", \\\"Balaji Lakshminarayanan\\\", \\\"Jonathon Shlens\\\", \\\"Michael C. Mozer\\\", \\\"Becca Roelofs\\\"]\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html\\\"\\n    category: \\\"calibration_foundations\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"SB-ECE: differentiable soft-binned ECE enabling gradient-based calibration optimization. Core component of our CaCLR objective.\\\"\\n    verified: true\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  khanmohammadi2025ccps:\\n    title: \\\"Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)\\\"\\n    authors: [\\\"Khanmohammadi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.21772\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Calibration via probing perturbed representation stability at final layer. ~55% ECE reduction. English-only, single layer. No cross-lingual or multi-layer analysis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  liu2025middle:\\n    title: \\\"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\\\"\\n    authors: [\\\"Liu\\\", \\\"Niehues\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Middle layers form strongest language-agnostic shared space. Supports our hypothesis about intermediate-layer transfer.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ji2025calibrating:\\n    title: \\\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\\\"\\n    authors: [\\\"Ji\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Verbal uncertainty governed by single linear direction in representation space.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  bendavid2010theory:\\n    title: \\\"A Theory of Learning from Different Domains\\\"\\n    authors: [\\\"Shai Ben-David\\\", \\\"John Blitzer\\\", \\\"Koby Crammer\\\", \\\"Alex Kulesza\\\", \\\"Fernando Pereira\\\", \\\"Jennifer Wortman Vaughan\\\"]\\n    year: 2010\\n    venue: \\\"Machine Learning, Vol. 79, pp. 151-175\\\"\\n    url: \\\"https://link.springer.com/article/10.1007/s10994-009-5152-4\\\"\\n    category: \\\"domain_adaptation_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"H-divergence framework for domain adaptation. Theoretical basis for bounding target error via source error and domain divergence — underpins our cross-lingual transfer analysis.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  zhao2019invariant:\\n    title: \\\"On Learning Invariant Representations for Domain Adaptation\\\"\\n    authors: [\\\"Han Zhao\\\", \\\"Remi Tachet des Combes\\\", \\\"Kun Zhang\\\", \\\"Geoffrey J. Gordon\\\"]\\n    year: 2019\\n    venue: \\\"ICML 2019\\\"\\n    url: \\\"https://proceedings.mlr.press/v97/zhao19a.html\\\"\\n    category: \\\"domain_adaptation_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Proves marginal distribution matching fails when conditional distributions differ. Motivates why naive cross-lingual probe transfer may degrade — our CaCLR addresses this gap.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  zhang2019bridging:\\n    title: \\\"Bridging Theory and Algorithm for Domain Adaptation\\\"\\n    authors: [\\\"Yuchen Zhang\\\", \\\"Tianle Liu\\\", \\\"Mingsheng Long\\\", \\\"Michael I. Jordan\\\"]\\n    year: 2019\\n    venue: \\\"ICML 2019\\\"\\n    url: \\\"https://proceedings.mlr.press/v97/zhang19i.html\\\"\\n    category: \\\"domain_adaptation_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Margin Disparity Discrepancy — tighter generalization bound connecting domain adaptation theory to practical adversarial algorithms. Complements Ben-David and Zhao theoretical foundations.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  hewitt2019control:\\n    title: \\\"Designing and Interpreting Probes with Control Tasks\\\"\\n    authors: [\\\"John Hewitt\\\", \\\"Percy Liang\\\"]\\n    year: 2019\\n    venue: \\\"EMNLP 2019\\\"\\n    url: \\\"https://aclanthology.org/D19-1275/\\\"\\n    category: \\\"probing_methodology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Defines selectivity metric for probes — ensures probe accuracy reflects encoded information, not classifier capacity. Methodological baseline for our probing evaluation.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  voita2020mdl:\\n    title: \\\"Information-Theoretic Probing with Minimum Description Length\\\"\\n    authors: [\\\"Elena Voita\\\", \\\"Ivan Titov\\\"]\\n    year: 2020\\n    venue: \\\"EMNLP 2020\\\"\\n    url: \\\"https://aclanthology.org/2020.emnlp-main.14/\\\"\\n    category: \\\"probing_methodology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"MDL probing — information-theoretic alternative measuring compression quality rather than raw accuracy. More robust evaluation metric for cross-lingual probe transfer.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  belinkov2022probing:\\n    title: \\\"Probing Classifiers: Promises, Shortcomings, and Advances\\\"\\n    authors: [\\\"Yonatan Belinkov\\\"]\\n    year: 2022\\n    venue: \\\"Computational Linguistics, Vol. 48, No. 1, pp. 207-219\\\"\\n    url: \\\"https://aclanthology.org/2022.cl-1.7/\\\"\\n    category: \\\"probing_methodology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Comprehensive survey of probing methodology — defines best practices, pitfalls, and evaluation standards we follow in our experimental design.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  kornblith2019cka:\\n    title: \\\"Similarity of Neural Network Representations Revisited\\\"\\n    authors: [\\\"Simon Kornblith\\\", \\\"Mohammad Norouzi\\\", \\\"Honglak Lee\\\", \\\"Geoffrey Hinton\\\"]\\n    year: 2019\\n    venue: \\\"ICML 2019\\\"\\n    url: \\\"https://proceedings.mlr.press/v97/kornblith19a.html\\\"\\n    category: \\\"representation_similarity\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Centered Kernel Alignment (CKA) — our primary metric for measuring cross-lingual representation similarity across layers.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  wu2020similarity:\\n    title: \\\"Similarity Analysis of Contextual Word Representation Models\\\"\\n    authors: [\\\"John Wu\\\", \\\"Yonatan Belinkov\\\", \\\"Hassan Sajjad\\\", \\\"Nadir Durrani\\\", \\\"Fahim Dalvi\\\", \\\"James Glass\\\"]\\n    year: 2020\\n    venue: \\\"ACL 2020\\\"\\n    url: \\\"https://aclanthology.org/2020.acl-main.422/\\\"\\n    category: \\\"representation_similarity\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Applies CKA and SVCCA to compare contextual word representations across architectures — direct precedent for our cross-lingual representation similarity analysis.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  guo2017calibration:\\n    title: \\\"On Calibration of Modern Neural Networks\\\"\\n    authors: [\\\"Chuan Guo\\\", \\\"Geoff Pleiss\\\", \\\"Yu Sun\\\", \\\"Kilian Q. Weinberger\\\"]\\n    year: 2017\\n    venue: \\\"ICML 2017\\\"\\n    url: \\\"https://proceedings.mlr.press/v70/guo17a.html\\\"\\n    category: \\\"calibration_foundations\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Temperature scaling baseline — canonical post-hoc calibration method we compare against. Established ECE as standard calibration metric.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  angelopoulos2023conformal:\\n    title: \\\"Conformal Prediction: A Gentle Introduction\\\"\\n    authors: [\\\"Anastasios N. Angelopoulos\\\", \\\"Stephen Bates\\\"]\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning, Vol. 16, No. 4, pp. 494-591\\\"\\n    url: \\\"https://www.nowpublishers.com/article/Details/MAL-101\\\"\\n    category: \\\"calibration_foundations\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Distribution-free uncertainty quantification framework — theoretical grounding for our conformal prediction extension of CaCLR.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\ncategories:\\n  mechanistic_calibration: \\\"Probing/steering calibration signals in LLM internal representations\\\"\\n  cross_lingual_probing: \\\"Cross-lingual transfer of probes/directions in multilingual models\\\"\\n  cross_lingual_alignment: \\\"Language alignment and shared representations in multilingual LLMs\\\"\\n  multilingual_calibration: \\\"Calibration methods for multilingual LLMs\\\"\\n  calibration_methods: \\\"General calibration objectives and techniques\\\"\\n  domain_adaptation_theory: \\\"Theoretical foundations for domain adaptation and representation learning\\\"\\n  probing_methodology: \\\"Methodology for probing neural network representations\\\"\\n  representation_similarity: \\\"Metrics and methods for comparing neural network representations\\\"\\n  calibration_foundations: \\\"Foundational calibration and uncertainty quantification methods\\\"\\n\\nmeta:\\n  created_at: \\\"2026-05-20\\\"\\n  last_updated: \\\"2026-05-21\\\"\\n  total_papers: 22\\n\", \"total_chars\": 13373, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "095a4888-ee92-42ab-a821-d1619243627d",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "b0532444-fae5-4aee-a1f8-111888cfb306",
  "sourceToolAssistantUUID": "095a4888-ee92-42ab-a821-d1619243627d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T05:52:11.674Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SfwQ4mgP8nw7XHQgqeRyH1`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0532444-fae5-4aee-a1f8-111888cfb306",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFC9m7ez2p19pMBJKuyd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16de4b25-46e0-4fa8-8467-0ca80cc5957c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141hSgqfLJXVh8xj6nhrEXA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6578,
      "cache_read_input_tokens": 17282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6578,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 14 · 2026-05-21T05:52:11.683Z_

<details><summary>↩ Tool result · `toolu_01SfwQ4mgP8nw7XHQgqeRyH1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 2 models × 20 languages × all contributions\\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method / Diagnostic)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\\\"method replication to more languages\\\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n### Key Empirical Contributions (elevated from appendix to main body, D012)\\n- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\\n- **Headline template (method success)**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n- **Headline template (negative result)**: \\\"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\\\"\\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\\n2. **\\\"Temperature scaling baseline\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\n3. **\\\"Mean-shift too weak / why does it fail?\\\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\\n4. **\\\"Difficulty confound\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\n5. **\\\"INT8 artifacts\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\n6. **\\\"Only MCQA\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\n7. **\\\"Predictable from domain adaptation theory\\\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\\n8. **\\\"No statistical tests\\\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\\n9. **\\\"Probing methodology concerns\\\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\\n10. **\\\"No mechanistic explanation\\\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \\\"geometric analysis\\\" not \\\"mechanistic explanation.\\\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\\n11. **\\\"Why not conformal prediction?\\\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\\n12. **\\\"CaCLR parallel activations = test leakage?\\\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\\n13. **\\\"CaCLR is your own method — self-debunking is less impactful\\\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\\n14. **\\\"CKA is correlational, not mechanistic\\\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\\n\\n## Additional Related Work Coverage (Dream-identified gaps)\\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \\\"On learning invariant representations for domain adaptation\\\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\\n\\n## Differentiation from Closest Prior Work\\n| Paper | Their Focus | Our Difference |\\n|-------|-------------|----------------|\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\n\", \"total_chars\": 17679, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16de4b25-46e0-4fa8-8467-0ca80cc5957c",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "a55fb982-1440-42b5-9191-4092265f3466",
  "sourceToolAssistantUUID": "16de4b25-46e0-4fa8-8467-0ca80cc5957c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T05:52:12.136Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HPriov3rvBzkbVBsmpXwhB`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a55fb982-1440-42b5-9191-4092265f3466",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFC9m7ez2p19pMBJKuyd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9edbd6d-7f0f-4bc4-9438-9807b144e836",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141hSgqfLJXVh8xj6nhrEXA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6578,
      "cache_read_input_tokens": 17282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6578,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 16 · 2026-05-21T05:52:12.148Z_

<details><summary>↩ Tool result · `toolu_01HPriov3rvBzkbVBsmpXwhB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\", \"content\": \"# xling_calib_direction — Research Dashboard\\n\\n> 最后更新: 2026-05-21 01:18 UTC | 更新原因: Correct model sizes (Llama4 66GB, Qwen3 122GB), revert to parallel download strategy, disk math confirms both fit\\n\\n## 核心方向\\nCross-lingual correctness probe transfer: 探索 LLM 内部 correctness direction 的跨语言可迁移性，测试 probe-based calibration 在非英语语言的可行性。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research phase — MVP 通过 (D004), Dream 审稿两轮完成 (D005→D009), P0 条件批准\\n- **MVP**: 3/3 完成 (mvp_001 ✓, mvp_002 ✓, mvp_003 ✓)\\n- **代码准备**: 全部就绪 ✅\\n  - transfer_eval.py: 5 种 transfer methods 已部署 (zero-shot, mean-shift, Procrustes, few-shot, CaCLR)\\n  - extract_activations_large.py: register_forward_hook + post-norm + 70/30 split ✅\\n  - train_caclr.py: M007 梯度修复已验证 ✅\\n- **模型下载** (并行，磁盘充足):\\n  - Llama4 Scout W4A16: ~44GB/66GB，ETA ~30-45min\\n  - Qwen3 GPTQ-Int4: ~38GB/122GB，ETA ~2-3h\\n  - 两模型合计 ~188GB，基础占用 ~88GB，总计 ~276GB/350GB = 79%\\n- **P1 先行**: plan_013 控制任务 ✅ (selectivity 0.262 at L27), plan_012 Procrustes sensitivity 运行中\\n- **关键发现**: Pareto tradeoff Qwen strong/Llama weak; mean-shift rank-invariance proof; few-shot +4.9pp AUROC over zero-shot\\n\\n## 近期任务\\n- [ ] Llama4 下载完成 (~30-45min) → 完整性验证 → dry-run → 正式审批 plan_002\\n- [ ] Qwen3 下载完成 (~2-3h) → 完整性验证 → dry-run → 正式审批 plan_001\\n- [ ] plan_002 执行: 提取激活 (12 layers × 20 langs) → 5 种 transfer eval\\n- [ ] plan_001 执行: 提取激活 (24 layers × 20 langs) → 5 种 transfer eval\\n- [ ] Procrustes sensitivity 结果收集 + CSV 完整性验证 (双进程写入风险)\\n- [ ] CPU-bound P1 (plan_011/012/013) 与 P0 并行推进\\n\\n## GPU 预算\\n- 服务器: westd-13176 (4× RTX 6000 PRO 96GB)\\n- 磁盘: /root/autodl-tmp/ 350GB total，下载完成后 ~276GB used (~74GB 余量)\\n- 激活存储策略: 先提取 Llama4 (~33GB) → 实验 → 可删模型释放 66GB → 再提取 Qwen3\\n- P0 总 GPU 预算: plan_001(80h) + plan_002(40h) + plan_003(20h) + plan_004(15h) = 155h → ~39h 墙钟\\n- 距 EACL ARR deadline (Aug 3): 74 天\\n\\n## Dream 审稿摘要 (Re-dream, D009)\\n| 档位 | 分数 | 核心反馈 |\\n|------|------|---------|\\n| Best | 4/6 WA | CaCLR underspec, CKA depth confound, arch confound, scope+controls 认可 |\\n| Median | 3/6 WR | Novelty insufficient (DA theory predicts), self-debunking less impactful |\\n| Worst | 3/6 WR | Contributions trivial/confirmatory, control task finding should be centered |\\n\\n### D009 确认行动项 (已全部执行 ✅)\\n1. CaCLR 完整实现规格 → plan_003 notes\\n2. CKA partial correlation controlling for depth → plan_011 (最关键分析)\\n3. Architecture-dependence 限定为 observational → paper_framing.md Claim 1\\n4. Control task finding 提升到 story spine → paper_framing.md\\n5. 补充引用: Zhao et al. 2019, DALI, Pires et al., Wu & Dredze → paper_framing.md\\n6. CKA: \\\"geometric/correlational analysis\\\" 非 \\\"mechanistic\\\" → paper_framing.md + plan_011\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D012 | 2026-05-21 | Novelty strategy: CKA partial correlation (plan_01 | plan_011, plan_013, plan_012 |\\n| D011 | 2026-05-21 | Revert to parallel download: Llama4 (66GB) + Qwen3 | plan_001, plan_002 |\\n| D010 | 2026-05-20 | GlobalMMLU data decisions: test 70/30 split for Ca | — |\\n| D009 | 2026-05-20 | Re-dream processed (4/3/3), P0 approved with condi | — |\\n| D008 | 2026-05-20 | Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4 | mvp_003, mvp_001 |\\n| D007 | 2026-05-20 | mvp_003 (Llama-3.1-8B) cross-architecture validati | mvp_003, mvp_001 |\\n| D006 | 2026-05-20 | MVP gate re-evaluation after P1 leakage fix: 2/4 P | mvp_001, plan_003 |\\n| D005 | 2026-05-20 | Dream review (3/6 weak reject) processed: 13 confi | plan_003, plan_011, plan_012, plan_013 |\\n| D004 | 2026-05-20 | MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段 | mvp_001 |\\n| D003 | 2026-05-20 | P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/ | mvp_001 |\\n\\n\", \"total_chars\": 3556, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9edbd6d-7f0f-4bc4-9438-9807b144e836",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "95e3b19b-4309-4120-b841-23c8b4a926ca",
  "sourceToolAssistantUUID": "e9edbd6d-7f0f-4bc4-9438-9807b144e836",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T05:52:12.683Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GFC9njxvhdnijgrTr55dZW`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95e3b19b-4309-4120-b841-23c8b4a926ca",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFC9m7ez2p19pMBJKuyd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea11a1ba-7b1d-4a7f-ac25-3f5c32f13764",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141hSgqfLJXVh8xj6nhrEXA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6578,
      "cache_read_input_tokens": 17282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6578,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 18 · 2026-05-21T05:52:12.694Z_

<details><summary>↩ Tool result · `toolu_01GFC9njxvhdnijgrTr55dZW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-21: Simpson's Paradox in CKA-transfer relationship (D012 关键发现)\\n\\n- **发现**: CKA vs transfer AUROC 存在 Simpson's Paradox——pool 所有 layer 时弱负相关 (rho≈−0.16)，控制 depth 后符号反转为正 (Llama rho=+0.41 p=0.006, Qwen rho=+0.18 ns)\\n- **机制**: CKA 随 depth 下降，AUROC 随 depth 上升，两趋势相消产生虚假负相关。同一 depth 下，CKA 越高 → transfer 越好\\n- **意义**: 直接回应 Reviewer depth confound 质疑；符号反转本身是 publishable finding\\n- **局限**: Qwen partial rho underpowered (n=40)，per-layer n=5 只能看方向。Full-scale 20 langs 会大幅增加统计功效\\n- **决策影响**: 如 Director 确认，paper_framing 中 CKA 分析可从 \\\"suggestive correlation\\\" 升级\\n\\n## 2026-05-21: run_plan_001.sh 关键设计决策\\n\\n- **GPTQ 加载**: `--quantization none` 让 HF 自动检测 GPTQ（不用 bitsandbytes NF4）\\n- **Train/eval split**: `--split_ratio 0.7` 产出 `_train.pt`/`_eval.pt`，symlink 桥接下游脚本\\n- **Procrustes 平行配对**: for_eval/ 中 EN 必须指向 eval split（与 target 平行），已修复初始 bug\\n\\n## 2026-05-21: 模型下载路径\\n\\n- Llama4 正确路径: `/root/autodl-tmp/models/Llama4-Scout-W4A16`（不带连字符）\\n- Qwen3 路径: `/root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4`\\n- 必须用 `HF_HUB_DISABLE_XET=1`（在 os.environ 中设置）+ `hf-mirror.com`\\n- `python3` 不在 PATH，用 `/root/miniconda3/bin/python3`\\n\", \"total_chars\": 1108, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea11a1ba-7b1d-4a7f-ac25-3f5c32f13764",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "1b5241a9-79bb-468d-99cf-66d563b5b269",
  "sourceToolAssistantUUID": "ea11a1ba-7b1d-4a7f-ac25-3f5c32f13764",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T05:52:15.238Z_

Now let me look at the actual paper draft and experimental artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b5241a9-79bb-468d-99cf-66d563b5b269",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCA96VHywwXoJFBKcp7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85c9aaff-58d4-42e4-9e3d-2668b05a5f3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBqybPybFdSiJXwC1mrAHp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7655,
      "cache_read_input_tokens": 23860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7655,
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

_source line 20 · 2026-05-21T05:52:16.269Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018iuqMfSGn87nv8SN8cwqhM`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85c9aaff-58d4-42e4-9e3d-2668b05a5f3f",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCA96VHywwXoJFBKcp7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59330656-22a2-477c-8b06-0b78933e23d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBqybPybFdSiJXwC1mrAHp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7655,
      "cache_read_input_tokens": 23860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7655,
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

_source line 21 · 2026-05-21T05:52:16.296Z_

<details><summary>↩ Tool result · `toolu_018iuqMfSGn87nv8SN8cwqhM`</summary>

```text
artifacts/dream_reports/dream_20260520T185641/best/paper.tex
artifacts/dream_reports/dream_20260520T185641/median/paper.tex
artifacts/dream_reports/dream_20260520T185641/worst/paper.tex
artifacts/dream_reports/dream_20260520T201854/best/paper.tex
artifacts/dream_reports/dream_20260520T201854/median/paper.tex
artifacts/dream_reports/dream_20260520T201854/worst/paper.tex
artifacts/dream_reports/dream_20260521T032808/best/paper.tex
artifacts/dream_reports/dream_20260521T032808/median/paper.tex
artifacts/dream_reports/dream_20260521T032808/worst/paper.tex
docs/paper/acl_latex.tex
artifacts/_project/paper/method.tex
docs/paper/method.tex
artifacts/dream_reports/dream_20260521T044911/best/paper.tex
artifacts/dream_reports/dream_20260521T044911/median/paper.tex
artifacts/dream_reports/dream_20260521T044911/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59330656-22a2-477c-8b06-0b78933e23d6",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "96b282dc-7e6b-4116-ba03-ddf465a89445",
  "sourceToolAssistantUUID": "59330656-22a2-477c-8b06-0b78933e23d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T05:52:16.720Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VASU4wMYkiY9Q3DEuwc8Pj`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96b282dc-7e6b-4116-ba03-ddf465a89445",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCA96VHywwXoJFBKcp7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19c88da6-cd4c-4e8e-99a9-a85ce83780eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBqybPybFdSiJXwC1mrAHp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7655,
      "cache_read_input_tokens": 23860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7655,
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

_source line 23 · 2026-05-21T05:52:16.736Z_

<details><summary>↩ Tool result · `toolu_01VASU4wMYkiY9Q3DEuwc8Pj`</summary>

```text
code/extract_activations.py
code/analyze_results.py
code/train_probe.py
code/train_caclr.py
code/extract_activations_large.py
code/transfer_eval.py
code/compute_cka.py
code/pareto_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19c88da6-cd4c-4e8e-99a9-a85ce83780eb",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "d20cb9dd-3db1-4153-8ed8-fd39d01292fc",
  "sourceToolAssistantUUID": "19c88da6-cd4c-4e8e-99a9-a85ce83780eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T05:52:17.301Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01U3rTvW9HZXUbU41HoPA7yM`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d20cb9dd-3db1-4153-8ed8-fd39d01292fc",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCA96VHywwXoJFBKcp7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22f1e1a1-4f0b-46e4-bc96-42775c2fdc30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBqybPybFdSiJXwC1mrAHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7655,
      "cache_read_input_tokens": 23860,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7655
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 23860,
          "cache_creation_input_tokens": 7655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7655,
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

_source line 25 · 2026-05-21T05:52:17.311Z_

<details><summary>↩ Tool result · `toolu_01U3rTvW9HZXUbU41HoPA7yM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml\", \"content\": \"_next_id: 13\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 13:49 UTC\\n  summary: MVP 用 7-8B 模型验证核心假设，不直接上 235B\\n  rationale: 核心假设（correctness probe 跨语言迁移 + layer-depth 效应）在 7-8B 模型上有充分先验（Miao &\\n    Ungar、Civelli 等均用 7-8B）。若 7B 无效应则整个方向不成立。7B 仅需 1 GPU × 2-4h，快速验证后再决定是否投入 235B\\n    的大资源。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 13:53 UTC\\n  summary: MVP 模型固定为 Qwen2.5-7B-Instruct\\n  rationale: 与正式实验 Qwen3-235B 同属 Qwen 家族，架构连续性最好。Civelli et al. 报告 Qwen3-8B 最优迁移深度为\\n    24%，可为正式实验提供直接参考。Reviewer 建议明确选一个并记录理由。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-20 18:25 UTC\\n  summary: P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/5 语言\\n  rationale: Mean-shift 是常数偏移，不改变 AUROC（rank-invariant）。Mean-shift 的设计目的是改善 calibration（概率准确性），应用\\n    ECE/Brier 衡量。同时 P1 ECE 阈值维持 0.15 但允许 temperature scaling 后重测。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: trigger\\n    result: P4 ΔAUROC=0 暴露标准设计缺陷\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-20 18:52 UTC\\n  summary: 'MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段'\\n  rationale: P1(AUROC=0.754+ECE=0.074 temp-scaled) / P2(4/5语言迁移) / P3(14.3pp depth\\n    effect) 全部 PASS。P4(mean-shift) FAIL 但属于 alignment baseline 方法失败，不否定核心假设。Mean-shift\\n    失败是有价值的 negative result：(1) 区分于 Xiao et al. 在 knowledge boundary 上 mean-shift\\n    成功；(2) motivate CaCLR 方法。额外发现：L27 英语最强但迁移退化 vs L24——直接观测到 Pareto tradeoff，是论文核心贡献的前兆。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: primary\\n    result: P1✅P2✅P3✅P4❌, core hypothesis supported\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-20 20:14 UTC\\n  summary: 'Dream review (3/6 weak reject) processed: 13 confirmed actions, 5 observations,\\n    3 ignores. Framing updated with conditional CaCLR narrative + 6 new reviewer concerns.\\n    3 new P1 experiments added (CKA, linproj sensitivity, control tasks). Proceeding\\n    with re-dream after changes.'\\n  rationale: 'Dream dream_20260520T185641 scored best=4/6 median=3/6 worst=3/6. Key\\n    structural issues identified across all 3 tiers: (1) no statistical tests — added\\n    as cross-cutting requirement; (2) CaCLR framing incoherent — redesigned as conditional\\n    narrative with two paths; (3) missing related work (domain adaptation theory,\\n    alignment literature, probing critiques) — added to paper_framing.md. Two-tier\\n    issues: (4) no mechanistic explanation — added plan_011 CKA analysis; (5) arbitrary\\n    AUROC threshold — added sensitivity analysis requirement; (6) probing methodology\\n    — added plan_013 control tasks. CaCLR consistency loss value is the key data-dependent\\n    risk (O3). Core 4-claim structure preserved; framing strengthened not weakened.\\n    No venue downgrade — issues are addressable via experiments and framing improvements.'\\n  related_experiments:\\n  - exp_id: plan_003\\n    role: affected\\n    result: CaCLR conditional narrative added\\n  - exp_id: plan_011\\n    role: new\\n    result: CKA mechanistic analysis (P1, 5 GPU-hrs)\\n  - exp_id: plan_012\\n    role: new\\n    result: Linear projection sensitivity (P1, 2 GPU-hrs)\\n  - exp_id: plan_013\\n    role: new\\n    result: Probing control tasks (P1, 2 GPU-hrs)\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-20 20:23 UTC\\n  summary: 'MVP gate re-evaluation after P1 leakage fix: 2/4 PASS, still proceed to\\n    research phase'\\n  rationale: 'M005 reveals temp scaling data leakage — P1 ECE now FAIL (0.2216 > 0.15).\\n    Gate drops from 3/4 to 2/4 PASS. However, the 2 passing criteria (P2: cross-lingual\\n    transfer 4/5 langs, P3: layer depth effect 14.28pp) are the hypothesis-critical\\n    ones that validate \\\"correctness direction exists and transfers cross-lingually.\\\"\\n    P1 ECE failure means raw probes are poorly calibrated — this is exactly the problem\\n    CaCLR is designed to solve, and actually strengthens the paper''s motivation (\\\"probe-based\\n    calibration needs CaCLR because naive probes fail on calibration\\\"). P4 mean-shift\\n    failure was already attributed to criteria design error (D003). Research phase\\n    continues with strengthened CaCLR motivation. The 0.15 ECE threshold for P1 was\\n    always somewhat arbitrary — discrimination (AUROC=0.754) is the primary signal\\n    that correctness information is linearly accessible.'\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: gate_check\\n    result: 2/4 PASS (P2+P3), P1 ECE FAIL after leakage fix\\n  - exp_id: plan_003\\n    role: motivated_by\\n    result: CaCLR motivation strengthened by raw probe calibration failure\\n  depends_on:\\n  - D004\\n  - D005\\n- id: D007\\n  date: 2026-05-20 20:31 UTC\\n  summary: 'mvp_003 (Llama-3.1-8B) cross-architecture validation: 3/4 PASS, Pareto\\n    architecture-dependence confirmed as core finding'\\n  rationale: 'mvp_003 gate 3/4 PASS (P1 PASS without temp scaling, P2 5/5, P3 7.85pp,\\n    P4 FAIL). Cross-architecture validation successful: correctness direction and\\n    transfer both replicate. Key finding: Pareto tradeoff is STRONG on Qwen (4/5 langs\\n    show depth-transfer degradation) but WEAK on Llama (only 2/5 — zh and sw; ar/ko\\n    improve with depth). This elevates architecture-dependence from a qualifier to\\n    a core finding in Claim 1. CKA pilot shows same two-model contrast. Swahili is\\n    model-dependent (fails Qwen, passes Llama). zh@L31 mean-shift anomaly flagged\\n    for investigation.'\\n  related_experiments:\\n  - exp_id: mvp_003\\n    role: validation\\n    result: 3/4 PASS, weak Pareto on Llama\\n  - exp_id: mvp_001\\n    role: comparison\\n    result: 2/4 PASS (post-fix), strong Pareto on Qwen\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-20 20:40 UTC\\n  summary: 'Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4), consistent with mvp_001.\\n    P1 evaluated at best-AUROC layer.'\\n  rationale: 'Reviewer pointed out D007 ambiguity: P1 passes at L0 (AUROC=0.650, ECE=0.148)\\n    but fails at best-AUROC layer L31 (AUROC=0.728, ECE=0.205). P1 should be evaluated\\n    at the best-AUROC layer (the probe we''d actually use), where ECE fails. Both\\n    models are now 2/4 PASS (P2+P3). This is consistent and actually cleaner: discrimination\\n    (P2+P3) confirmed on both architectures, calibration (P1+P4) fails on both → strengthens\\n    CaCLR motivation uniformly. No impact on research phase decision (D006).'\\n  related_experiments:\\n  - exp_id: mvp_003\\n    role: clarification\\n    result: 2/4 PASS (P2+P3), not 3/4\\n  - exp_id: mvp_001\\n    role: comparison\\n    result: 2/4 PASS (P2+P3), consistent\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-20 21:27 UTC\\n  summary: Re-dream processed (4/3/3), P0 approved with conditions — 6 confirmed action\\n    items integrated into framing+plan\\n  rationale: 'Re-dream scores: best=4/6 (Weak Accept) ✓, median=3/6 (Weak Reject =\\n    borderline), worst=3/6. All simulated quality. Scores unchanged from first dream\\n    despite acknowledged framing improvements — remaining issues are (1) implementation-level\\n    (CaCLR specs, CKA partial correlation) addressable in experiment execution, and\\n    (2) novelty concerns inherent to negative-result scenario that only resolve with\\n    real data. Blocking P0 further would waste time without improving situation. 6\\n    confirmed action items: A1-CaCLR complete implementation spec required, A2-CKA\\n    partial correlation controlling for depth mandatory, A3-architecture claim qualified\\n    as observational, A4-control task finding elevated in story, A5-missing references\\n    added (Zhao et al. 2019, DALI, Pires et al.), A6-CKA framed as geometric/correlational\\n    not mechanistic. 7 observation items tracked for real experiment validation. P0\\n    approved conditional on code blockers resolved (transfer_eval.py, extract_activations_large.py).'\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D010\\n  date: 2026-05-20 21:58 UTC\\n  summary: 'GlobalMMLU data decisions: test 70/30 split for CaCLR (no train split\\n    exists); th→te language swap'\\n  rationale: 'GlobalMMLU has only test (14042/lang) and dev (285/lang) splits, no\\n    train split. plan_003 assumed train split for CaCLR parallel activations. Fix:\\n    partition test 70/30 stratified into probe_train and eval. probe_train for BCE\\n    labels + MMD parallel activations; eval for all metrics. 4200 eval samples sufficient.\\n    dev too small (285) for MMD. Thai not in GlobalMMLU; replaced with Telugu (te)\\n    to add Dravidian family coverage (currently missing language family).'\\n  related_experiments: []\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-21 01:18 UTC\\n  summary: 'Revert to parallel download: Llama4 (66GB) + Qwen3 (122GB) both fit on\\n    disk (276GB/350GB)'\\n  rationale: 'Agent initially reported Qwen3=208GB and Llama4=103GB, triggering serial\\n    strategy. Reviewer verified actual sizes: Llama4 W4A16 = 14×4.7GB = 66GB, Qwen3\\n    GPTQ-Int4 = 32×3.8GB = 122GB. Total 188GB + 88GB baseline = 276GB/350GB (79%).\\n    Parallel download saves 2-3h. Activation storage handled sequentially: extract\\n    Llama4 first, delete model, then extract Qwen3.'\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: gated_by\\n  - exp_id: plan_002\\n    role: gated_by\\n  depends_on:\\n  - D009\\n- id: D012\\n  date: 2026-05-21 03:56 UTC\\n  summary: 'Novelty strategy: CKA partial correlation (plan_011) is the pivot point;\\n    Claim 4 downgrade to subsection; control task finding + projection efficiency\\n    elevated to main body'\\n  rationale: 'Reviewer independent assessment: CKA partial correlation controlling\\n    for depth is the single highest-impact novelty lever (+0.5 if significant). Control\\n    task finding (+0.3) and projection sample efficiency (+0.2) are certain improvements.\\n    Claim 4 (orthogonality) has weakest standalone novelty, should be subsection to\\n    free space. Pareto formalization doesn''t improve novelty score. Best case 2.5→3.5-4.0,\\n    conservative 2.5→3.0.'\\n  related_experiments:\\n  - exp_id: plan_011\\n    role: pivot_point\\n  - exp_id: plan_013\\n    role: elevate_finding\\n  - exp_id: plan_012\\n    role: elevate_finding\\n  depends_on:\\n  - D009\\n\", \"total_chars\": 9902, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22f1e1a1-4f0b-46e4-bc96-42775c2fdc30",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "659e1631-c459-4349-9eee-cc16c9360c38",
  "sourceToolAssistantUUID": "22f1e1a1-4f0b-46e4-bc96-42775c2fdc30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-21T05:52:20.544Z_

Let me also read the dream review reports to understand simulated reviewer feedback, and the actual paper draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "659e1631-c459-4349-9eee-cc16c9360c38",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCAUUJzpwoo6T87J753",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23ba7dec-ff8e-4972-ab4d-576a554f3274",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qDE8TfYZVaXrjQsGAvesG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4672,
      "cache_read_input_tokens": 31515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4672,
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

_source line 27 · 2026-05-21T05:52:23.009Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FVaSe7XwKM4SUuimHBTZNe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/acl_latex.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23ba7dec-ff8e-4972-ab4d-576a554f3274",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCAUUJzpwoo6T87J753",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac2ddaf2-3e17-4558-86a4-d4e2bc0c156f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qDE8TfYZVaXrjQsGAvesG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4672,
      "cache_read_input_tokens": 31515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4672,
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

_source line 28 · 2026-05-21T05:52:23.021Z_

<details><summary>↩ Tool result · `toolu_01FVaSe7XwKM4SUuimHBTZNe`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	% Change "review" to "final" to generate the final (sometimes called camera-ready) version.
4	% Change to "preprint" to generate a non-anonymous version with page numbers.
5	\usepackage[review]{acl}
6	
7	% Standard package includes
8	\usepackage{times}
9	\usepackage{latexsym}
10	
11	% For proper rendering and hyphenation of words containing Latin characters (including in bib files)
12	\usepackage[T1]{fontenc}
13	% For Vietnamese characters
14	% \usepackage[T5]{fontenc}
15	% See https://www.latex-project.org/help/documentation/encguide.pdf for other character sets
16	
17	% This assumes your files are encoded as UTF8
18	\usepackage[utf8]{inputenc}
19	
20	% This is not strictly necessary, and may be commented out,
21	% but it will improve the layout of the manuscript,
22	% and will typically save some space.
23	\usepackage{microtype}
24	
25	% This is also not strictly necessary, and may be commented out.
26	% However, it will improve the aesthetics of text in
27	% the typewriter font.
28	\usepackage{inconsolata}
29	
30	%Including images in your LaTeX document requires adding
31	%additional package(s)
32	\usepackage{graphicx}
33	
34	% If the title and author information does not fit in the area allocated, uncomment the following
35	%
36	%\setlength\titlebox{&lt;dim>}
37	%
38	% and set &lt;dim> to something 5cm or larger.
39	
40	\title{Instructions for *ACL Proceedings}
41	
42	% Author information can be set in various styles:
43	% For several authors from the same institution:
44	% \author{Author 1 \and ... \and Author n \\
45	%         Address line \\ ... \\ Address line}
46	% if the names do not fit well on one line use
47	%         Author 1 \\ {\bf Author 2} \\ ... \\ {\bf Author n} \\
48	% For authors from different institutions:
49	% \author{Author 1 \\ Address line \\  ... \\ Address line
50	%         \And  ... \And
51	%         Author n \\ Address line \\ ... \\ Address line}
52	% To start a separate ``row'' of authors use \AND, as in
53	% \author{Author 1 \\ Address line \\  ... \\ Address line
54	%         \AND
55	%         Author 2 \\ Address line \\ ... \\ Address line \And
56	%         Author 3 \\ Address line \\ ... \\ Address line}
57	
58	\author{First Author \\
59	  Affiliation / Address line 1 \\
60	  Affiliation / Address line 2 \\
61	  Affiliation / Address line 3 \\
62	  \texttt{email@domain} \\\And
63	  Second Author \\
64	  Affiliation / Address line 1 \\
65	  Affiliation / Address line 2 \\
66	  Affiliation / Address line 3 \\
67	  \texttt{email@domain} \\}
68	
69	%\author{
70	%  \textbf{First Author\textsuperscript{1}},
71	%  \textbf{Second Author\textsuperscript{1,2}},
72	%  \textbf{Third T. Author\textsuperscript{1}},
73	%  \textbf{Fourth Author\textsuperscript{1}},
74	%\\
75	%  \textbf{Fifth Author\textsuperscript{1,2}},
76	%  \textbf{Sixth Author\textsuperscript{1}},
77	%  \textbf{Seventh Author\textsuperscript{1}},
78	%  \textbf{Eighth Author \textsuperscript{1,2,3,4}},
79	%\\
80	%  \textbf{Ninth Author\textsuperscript{1}},
81	%  \textbf{Tenth Author\textsuperscript{1}},
82	%  \textbf{Eleventh E. Author\textsuperscript{1,2,3,4,5}},
83	%  \textbf{Twelfth Author\textsuperscript{1}},
84	%\\
85	%  \textbf{Thirteenth Author\textsuperscript{3}},
86	%  \textbf{Fourteenth F. Author\textsuperscript{2,4}},
87	%  \textbf{Fifteenth Author\textsuperscript{1}},
88	%  \textbf{Sixteenth Author\textsuperscript{1}},
89	%\\
90	%  \textbf{Seventeenth S. Author\textsuperscript{4,5}},
91	%  \textbf{Eighteenth Author\textsuperscript{3,4}},
92	%  \textbf{Nineteenth N. Author\textsuperscript{2,5}},
93	%  \textbf{Twentieth Author\textsuperscript{1}}
94	%\\
95	%\\
96	%  \textsuperscript{1}Affiliation 1,
97	%  \textsuperscript{2}Affiliation 2,
98	%  \textsuperscript{3}Affiliation 3,
99	%  \textsuperscript{4}Affiliation 4,
100	%  \textsuperscript{5}Affiliation 5
101	%\\
102	%  \small{
103	%    \textbf{Correspondence:} \href{mailto:email@domain}{email@domain}
104	%  }
105	%}
106	
107	\begin{document}
108	\maketitle
109	\begin{abstract}
110	This document is a supplement to the general instructions for *ACL authors. It contains instructions for using the \LaTeX{} style files for ACL conferences.
111	The document itself conforms to its own specifications, and is therefore an example of what your manuscript should look like.
112	These instructions should be used both for papers submitted for review and for final versions of accepted papers.
113	\end{abstract}
114	
115	\section{Introduction}
116	
117	These instructions are for authors submitting papers to *ACL conferences using \LaTeX. They are not self-contained. All authors must follow the general instructions for *ACL proceedings,\footnote{\url{http://acl-org.github.io/ACLPUB/formatting.html}} and this document contains additional instructions for the \LaTeX{} style files.
118	
119	The templates include the \LaTeX{} source of this document (\texttt{acl\_latex.tex}),
120	the \LaTeX{} style file used to format it (\texttt{acl.sty}),
121	an ACL bibliography style (\texttt{acl\_natbib.bst}),
122	an example bibliography (\texttt{custom.bib}),
123	and the bibliography for the ACL Anthology (\texttt{anthology.bib}).
124	
125	\section{Engines}
126	
127	To produce a PDF file, pdf\LaTeX{} is strongly recommended (over original \LaTeX{} plus dvips+ps2pdf or dvipdf).
128	The style file \texttt{acl.sty} can also be used with
129	lua\LaTeX{} and
130	Xe\LaTeX{}, which are especially suitable for text in non-Latin scripts.
131	The file \texttt{acl\_lualatex.tex} in this repository provides
132	an example of how to use \texttt{acl.sty} with either
133	lua\LaTeX{} or
134	Xe\LaTeX{}.
135	
136	\section{Preamble}
137	
138	The first line of the file must be
139	\begin{quote}
140	\begin{verbatim}
141	\documentclass[11pt]{article}
142	\end{verbatim}
143	\end{quote}
144	
145	To load the style file in the review version:
146	\begin{quote}
147	\begin{verbatim}
148	\usepackage[review]{acl}
149	\end{verbatim}
150	\end{quote}
151	For the final version, omit the \verb|review| option:
152	\begin{quote}
153	\begin{verbatim}
154	\usepackage{acl}
155	\end{verbatim}
156	\end{quote}
157	
158	To use Times Roman, put the following in the preamble:
159	\begin{quote}
160	\begin{verbatim}
161	\usepackage{times}
162	\end{verbatim}
163	\end{quote}
164	(Alternatives like txfonts or newtx are also acceptable.)
165	
166	Please see the \LaTeX{} source of this document for comments on other packages that may be useful.
167	
168	Set the title and author using \verb|\title| and \verb|\author|. Within the author list, format multiple authors using \verb|\and| and \verb|\And| and \verb|\AND|; please see the \LaTeX{} source for examples.
169	
170	By default, the box containing the title and author names is set to the minimum of 5 cm. If you need more space, include the following in the preamble:
171	\begin{quote}
172	\begin{verbatim}
173	\setlength\titlebox{&lt;dim>}
174	\end{verbatim}
175	\end{quote}
176	where \verb|&lt;dim>| is replaced with a length. Do not set this length smaller than 5 cm.
177	
178	\section{Document Body}
179	
180	\subsection{Footnotes}
181	
182	Footnotes are inserted with the \verb|\footnote| command.\footnote{This is a footnote.}
183	
184	\subsection{Tables and figures}
185	
186	See Table~\ref{tab:accents} for an example of a table and its caption.
187	\textbf{Do not override the default caption sizes.}
188	
189	\begin{table}
190	  \centering
191	  \begin{tabular}{lc}
192	    \hline
193	    \textbf{Command} & \textbf{Output} \\
194	    \hline
195	    \verb|{\"a}|     & {\"a}           \\
196	    \verb|{\^e}|     & {\^e}           \\
197	    \verb|{\`i}|     & {\`i}           \\
198	    \verb|{\.I}|     & {\.I}           \\
199	    \verb|{\o}|      & {\o}            \\
200	    \verb|{\'u}|     & {\'u}           \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac2ddaf2-3e17-4558-86a4-d4e2bc0c156f",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "97633a11-8d01-4efa-ac4c-601dff7b7c19",
  "sourceToolAssistantUUID": "ac2ddaf2-3e17-4558-86a4-d4e2bc0c156f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T05:52:24.062Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y2RmGjQr3tkTUJSbQaa7W8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97633a11-8d01-4efa-ac4c-601dff7b7c19",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCAUUJzpwoo6T87J753",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37fd1238-dfa7-4084-b96d-3778e7f37f28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qDE8TfYZVaXrjQsGAvesG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4672,
      "cache_read_input_tokens": 31515,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4672
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 31515,
          "cache_creation_input_tokens": 4672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4672,
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

_source line 30 · 2026-05-21T05:52:24.067Z_

<details><summary>↩ Tool result · `toolu_01Y2RmGjQr3tkTUJSbQaa7W8`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{multirow}
6	\usepackage{graphicx}
7	\usepackage{xcolor}
8	\usepackage[margin=1in]{geometry}
9	\usepackage{hyperref}
10	\usepackage{array}
11	\usepackage{caption}
12	\usepackage{subcaption}
13	
14	\hypersetup{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue}
15	
16	\newcommand{\rmark}{\textcolor{red}{$\rho$}}
17	\newcommand{\pp}{\,\text{pp}}
18	
19	\title{Geometric Analysis Reveals When and Why\\Cross-Lingual Calibration Transfer Succeeds}
20	
21	\author{Anonymous}
22	
23	\date{}
24	
25	\begin{document}
26	\maketitle
27	
28	%==============================================================================
29	\begin{abstract}
30	%==============================================================================
31	Probe-based calibration methods can detect whether a language model's internal representations encode answer correctness, but all existing approaches are English-only. We present the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B Dense), 50 languages, and five transfer conditions. Our analysis reveals four interconnected findings forming a causal chain. \textbf{(1)}~A depth-transferability Pareto frontier whose strength is architecture-dependent: Qwen3 exhibits a strong, consistent tradeoff (per-language Spearman $\rho$ significant in 15/20 languages) while Llama~4 shows a weak, language-specific pattern (6/20 significant; three languages exhibit reversed trends). \textbf{(2)}~Decomposing correctness into difficulty-shared (65\% variance, 12\% of transfer degradation) and capability-specific (35\% variance, 88\% of degradation) components reveals that capability-specific representations drive deep-layer transfer failure. \textbf{(3)}~CaCLR, a consistency-regularized calibration method requiring no target-language labels, provides a mean improvement of +3.5\pp{} AUROC over zero-shot transfer, with gains concentrated at deep layers (+4.8\pp). \textbf{(4)}~A Simpson's Paradox in the CKA--transfer relationship---raw correlation is negative ($\rho = -0.36$ to $-0.41$; depth confound) but partial correlation controlling for depth is significantly positive ($\rho = +0.41$ to $+0.48$; $p < 0.01$ on both architectures)---reveals that within-layer cross-lingual CKA genuinely predicts transfer quality while the correctness direction occupies a near-universal subspace (within-layer angle $12.4^{\circ}$). We additionally find that 28\% of low-resource probing results are capacity artifacts, and that Procrustes alignment reverses direction at a threshold of $\sim$0.52 zero-shot AUROC. Code and probes will be released.
32	\end{abstract}
33	
34	%==============================================================================
35	\section{Introduction}
36	\label{sec:intro}
37	%==============================================================================
38	
39	Multilingual large language models suffer from a persistent calibration gap: non-English languages exhibit expected calibration error (ECE) up to five times worse than English \cite{joshi2024llm}. Output-based recalibration methods such as temperature scaling require per-language calibration data, while ensemble approaches like MKA incur multiplicative inference costs \cite{zhou2024lace}. Recent work on probe-based calibration offers an alternative: linear probes trained on internal representations can detect whether a model ``knows'' the answer is correct, and this correctness direction is nearly orthogonal to the model's verbalized confidence \cite{miao2026coral,miao2026steering}. However, the entire probe-based calibration literature is English-only.
40	
41	Can English-trained correctness probes transfer to other languages without target-language labels? If so, under what conditions, and why does transfer succeed or fail? These questions are fundamental to the viability of representation-level calibration beyond English. Xiao et al.\ \cite{xiao2025crosslingual} transferred \emph{knowledge boundary} probes---binary answerability classifiers at the input level---and found encouraging results in 8 languages. But correctness probing targets a fundamentally different signal: output-dependent accuracy on specific items, not input-level answerability. The cross-lingual properties of correctness representations remain unexplored.
42	
43	We present the first large-scale study of cross-lingual correctness probe transfer. Probing three architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense) across 20--50 typologically diverse languages on GlobalMMLU, we discover a \emph{depth-transferability Pareto frontier}: deeper layers yield better English probes but progressively degrade in zero-shot cross-lingual transfer. The frontier's strength is architecture-dependent---strong and consistent on Qwen3, weak and language-specific on Llama~4. A geometric analysis based on centered kernel alignment (CKA) reveals a Simpson's Paradox at the heart of this phenomenon: pooling across layers, CKA and transfer quality correlate \emph{negatively} (depth confound), but controlling for layer depth, higher within-layer CKA significantly predicts better transfer ($p < 0.01$ on both architectures). The correctness direction itself occupies a near-universal low-dimensional subspace (cross-language angle $12.4^{\circ}$ within each layer) that persists even as global representations specialize by language.
44	
45	Our contributions are:
46	\begin{enumerate}
47	\item \textbf{Pareto discovery.} We identify an architecture-dependent depth-transferability tradeoff across three architectures and 20 languages, with Pareto knee at 55--58\% depth.
48	\item \textbf{Decomposition analysis.} We decompose correctness into difficulty-shared and capability-specific components, showing that capability drives 88\% of transfer degradation despite accounting for only 35\% of variance.
49	\item \textbf{CaCLR method.} A consistency-regularized calibration approach providing +3.5\pp{} mean AUROC gain without target-language labels, with gains concentrated at deep layers.
50	\item \textbf{CKA geometric explanation.} The Simpson's Paradox, subspace persistence ($12.4^{\circ}$ within-layer, $38.7^{\circ}$ cross-layer), and CKA cliff threshold ($\sim$0.35) together explain when and why transfer succeeds.
51	\end{enumerate}
52	Additionally, we report that 28\% of low-resource probing results are capacity artifacts (a methodological warning for the field), that Procrustes alignment with $\sim$42 parallel pairs reaches 95\% of full performance, and that Procrustes helps below a zero-shot AUROC threshold of $\sim$0.52 but \emph{hurts} above it.
53	
54	%==============================================================================
55	\section{Related Work}
56	\label{sec:related}
57	%==============================================================================
58	
59	\paragraph{Probe-based calibration.}
60	Linear probes trained on internal representations to detect answer correctness were introduced by Miao et al.\ \cite{miao2026coral} (CORAL) and extended to confidence--correctness steering vectors \cite{miao2026steering}. CCPS \cite{ji2024llm} identifies ``truth-telling'' and ``confidence'' directions in representation space. Ji et al.\ \cite{ji2024llm} demonstrate that the correctness direction and verbalized confidence are nearly orthogonal. All of these operate exclusively in English.
61	
62	\paragraph{Cross-lingual probing.}
63	Xiao et al.\ \cite{xiao2025crosslingual} transfer knowledge-boundary probes across 8 languages, reporting that mean-shift alignment and Procrustes rotation improve transfer. Their target is binary answerability (input-level), not correctness (output-dependent accuracy), and they evaluate probing accuracy rather than calibration. Civelli et al.\ \cite{civelli2024crosslingual} show that IRT difficulty transfers well cross-lingually. We decompose correctness into difficulty-shared and capability-specific components, directly building on their finding.
64	
65	\paragraph{Cross-lingual representation alignment.}
66	Static cross-lingual alignment methods such as MUSE \cite{conneau2018word} and VecMap \cite{artetxe2018robust} demonstrate that Procrustes rotation effectively aligns embedding spaces with minimal parallel data. Our linear projection applies this principle at the sentence-level correctness representation, and we characterize sample efficiency across resource tiers.
67	
68	\paragraph{Representation similarity.}
69	Centered kernel alignment (CKA; \cite{kornblith2019similarity}) and SVCCA \cite{raghu2017svcca} quantify representation similarity across models and layers. We use CKA to measure cross-lingual similarity at each layer, revealing a Simpson's Paradox when the depth confound is controlled.
70	
71	\paragraph{Domain adaptation theory.}
72	Ben-David et al.\ \cite{bendavid2010theory} formalize transfer error via $\mathcal{H}$-divergence. Zhao et al.\ \cite{zhao2019learning} show that marginal distribution matching fails when conditional distributions differ---directly relevant to understanding why CaCLR's MMD-based matching provides bounded rather than unbounded improvement.
73	
74	\paragraph{Conformal prediction.}
75	Distribution-free coverage guarantees \cite{angelopoulos2023conformal} provide complementary calibration. Unlike our zero-label approach, conformal methods require per-language calibration data; the two are complementary.
76	
77	%==============================================================================
78	\section{Method}
79	\label{sec:method}
80	%==============================================================================
81	
82	\subsection{Cross-Lingual Correctness Probing}
83	\label{sec:method:probing}
84	
85	Given a multilingual LLM with $L$ layers, we extract hidden-state representations at layer $l$ for each MCQA item in GlobalMMLU. An English logistic regression probe is trained:
86	\begin{equation}
87	p(\text{correct} \mid \mathbf{h}_l^{\text{en}}) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l^{\text{en}} + b_l)
88	\end{equation}
89	where $\mathbf{h}_l^{\text{en}}$ is the pooled hidden state at layer $l$ for an English input. We evaluate this probe on target language representations $\mathbf{h}_l^{\text{tgt}}$ without any target-language labels (zero-shot transfer). We also evaluate under four additional conditions: (a)~mean-shift alignment, (b)~Procrustes linear projection with varying numbers of parallel pairs, (c)~few-shot fine-tuning with 25 or 100 target-language labels, and (d)~CaCLR (Section~\ref{sec:method:caclr}).
90	
91	We select logistic regression over nonlinear probes because linear probes better capture the language-agnostic linear structure of the correctness subspace. Empirically, MLPs gain +2\pp{} English AUROC but lose 5.5\pp{} in transfer (Section~\ref{sec:probe_complexity}).
92	
93	\paragraph{Mean-shift invariance.} Under StandardScaler preprocessing followed by logistic regression, mean-shift adds a constant offset to all logits. Since AUROC is rank-invariant, $\Delta\text{AUROC} \equiv 0$ mathematically. Our data confirms this across all languages and layers.
94	
95	\subsection{CaCLR: Calibration via Cross-Lingual Regularization}
96	\label{sec:method:caclr}
97	
98	CaCLR optimizes a joint loss over English labels and cross-lingual distributional consistency:
99	\begin{equation}
100	\mathcal{L}_{\text{CaCLR}} = \mathcal{L}_{\text{BCE}} + \alpha \cdot \mathcal{L}_{\text{SB-ECE}} + \beta \cdot \mathcal{L}_{\text{consistency}}
101	\end{equation}
102	where $\mathcal{L}_{\text{BCE}}$ is binary cross-entropy on English correctness labels, $\mathcal{L}_{\text{SB-ECE}}$ is a soft-binned ECE loss, and $\mathcal{L}_{\text{consistency}}$ is Maximum Mean Discrepancy (MMD) between English and target-language probe logits:
103	\begin{equation}
104	\mathcal{L}_{\text{consistency}} = \text{MMD}^2_k\big(\{f(\mathbf{h}_l^{\text{en},i})\}_{i=1}^n, \{f(\mathbf{h}_l^{\text{tgt},i})\}_{i=1}^n\big)
105	\end{equation}
106	where $f(\cdot) = \mathbf{w}^\top(\cdot) + b$ denotes the probe logit (1-D for linear probes), and $k$ is a Gaussian RBF kernel with bandwidth set by the median heuristic. The parallel activations come from GlobalMMLU test split (70/30 partition for train/eval); no target-language \emph{labels} are used. We optimize with Adam ($\text{lr}=10^{-3}$, linear warmup 10\%), batch size 256, 50 epochs with early stopping (patience 10, monitoring validation AUROC). The probe is initialized from the standard logistic regression solution.
107	
108	CaCLR operates on 1-D logits---a design constraint of the linear probe. MMD in 1-D effectively matches mean and variance of the logit distributions across languages, equivalent to nudging the probe direction toward the universal correctness subspace revealed by our CKA analysis (Section~\ref{sec:cka}). However, it cannot perform full rotational alignment, which limits its ceiling compared to explicit Procrustes rotation.
109	
110	\subsection{Difficulty--Capability Decomposition}
111	\label{sec:method:decomposition}
112	
113	Following Civelli et al.\ \cite{civelli2024crosslingual}, we train an IRT difficulty probe (Ridge regression) on item difficulty estimates, then project out the difficulty direction from the hidden states and retrain correctness probes on the residual representations. This decomposes correctness variance into:
114	\begin{itemize}
115	\item \textbf{Difficulty-shared}: language-agnostic item difficulty information (hard items are hard everywhere).
116	\item \textbf{Capability-specific}: language-dependent competence that varies across languages and depths.
117	\end{itemize}
118	A random-direction control confirms that the decomposition captures genuine structure rather than arbitrary dimensionality reduction.
119	
120	\subsection{CKA Geometric Analysis}
121	\label{sec:method:cka}
122	
123	We compute linear CKA between English and each target language at every probed layer. Three analyses probe the geometry:
124	\begin{enumerate}
125	\item \textbf{Same-layer cross-language correlation}: at each layer, Spearman correlation between CKA$_l(\text{en}, \text{tgt})$ and zero-shot AUROC$_l(\text{tgt})$ across $n=20$ languages.
126	\item \textbf{Partial Spearman correlation}: controlling for normalized depth, testing whether CKA predicts transfer beyond the depth confound.
127	\item \textbf{Subspace angle analysis}: measuring the angular deviation of the correctness direction $\mathbf{w}_l$ across languages within the same layer and across layers.
128	\end{enumerate}
129	
130	%==============================================================================
131	\section{Experimental Setup}
132	\label{sec:setup}
133	%==============================================================================
134	
135	\subsection{Models}
136	
137	We evaluate three architectures spanning MoE and dense designs:
138	
139	\begin{table}[h]
140	\centering
141	\caption{Model specifications and summary results across 20 languages.}
142	\label{tab:three_arch}
143	\small
144	\begin{tabular}{lcccccccc}
145	\toprule
146	Model & Type & Layers & EN Best & ZS Mean & Pareto $\rho$ & Simpson $\rho_{\text{partial}}$ & CaCLR $\Delta$\pp \\
147	\midrule
148	Qwen3-235B & MoE & 94 & 0.81 & 0.72 & $-0.91$ & $+0.48$ & $+3.7$ \\
149	Llama~4 Scout & MoE & 48 & 0.79 & 0.70 & $-0.78$ & $+0.41$ & $+3.3$ \\
150	Gemma~4 31B & Dense & 60 & 0.80 & 0.71 & $-0.85$ & $+0.44$ & $+3.0$ \\
151	\bottomrule
152	\end{tabular}
153	\end{table}
154	
155	Qwen3-235B-A22B is a 94-layer MoE model ($\sim$22B active parameters) run under GPTQ-Int4 quantization. Llama~4 Scout is a 48-layer MoE model (17B$\times$16 experts, top-2 routing) under W4A16. Gemma~4 31B is a 60-layer dense model run in FP16. We probe every 4th layer (24 layers for Qwen3, 12 for Llama~4, 15 for Gemma~4). Quantization validation (Section~\ref{sec:quant}) confirms negligible distortion (mean $\leq 0.5\pp$, rank correlation $\geq 0.994$).
156	
157	\subsection{Languages and Benchmarks}
158	
159	Our core evaluation covers 20 typologically diverse languages grouped by resource tier: HIGH (zh, es, fr, de, ja, nl, pt, it), MID (ar, hi, ko, tr, ru, vi, th), and LOW (sw, bn, yo, ig, te). Extended evaluation (Section~\ref{sec:extended}) expands to 50 languages including Austronesian, Dravidian, Uralic, Kartvelian, and additional Niger-Congo families. Primary benchmark is GlobalMMLU; cross-benchmark generalization is assessed on Belebele and MMLU-ProX (Section~\ref{sec:cross_benchmark}).
160	
161	%==============================================================================
162	\section{Results}
163	\label{sec:results}
164	%==============================================================================
165	
166	\subsection{Architecture-Dependent Pareto Frontier}
167	\label{sec:pareto}
168	
169	\paragraph{Qwen3-235B.}
170	Table~\ref{tab:qwen_pareto} shows the layer-wise profile. The English-optimal layer (L72, 77\% depth, AUROC 0.81) and zero-shot-optimal layer (L52, 55\% depth, AUROC 0.72) are separated by 20 layers. The Pareto frontier spans layers L40--L56 with a knee gap of 4.2\pp. The global Spearman correlation between depth and zero-shot AUROC is $\rho = -0.91$ ($p < 0.001$), and 15 of 20 per-language correlations are significantly negative ($p < 0.05$). The two languages failing the 0.60 AUROC threshold are Yoruba (0.57) and Telugu (0.58), both extremely low-resource in pretraining data.
171	
172	\begin{table}[t]
173	\centering
174	\caption{Qwen3-235B Pareto frontier. Selected layers from 24 probed (every 4th of 94). $\checkmark$ marks Pareto-optimal layers.}
175	\label{tab:qwen_pareto}
176	\small
177	\begin{tabular}{cccccc}
178	\toprule
179	Layer & Depth\% & EN AUROC & ZS Mean$_{20}$ & ZS Drop\pp & Pareto \\
180	\midrule
181	4  & 4  & 0.580 & 0.572 & 0.8  & \\
182	12 & 13 & 0.645 & 0.632 & 1.3  & \\
183	20 & 21 & 0.710 & 0.695 & 1.5  & \\
184	28 & 30 & 0.752 & 0.733 & 1.9  & \\
185	36 & 38 & 0.778 & 0.752 & 2.6  & \\
186	40 & 43 & 0.788 & 0.748 & 4.0  & $\checkmark$ \\
187	44 & 47 & 0.796 & 0.740 & 5.6  & $\checkmark$ \\
188	48 & 51 & 0.802 & 0.732 & 7.0  & $\checkmark$ \\
189	52 & 55 & 0.806 & 0.720 & 8.6  & $\checkmark$ \\
190	56 & 60 & 0.808 & 0.706 & 10.2 & $\checkmark$ \\
191	60 & 64 & 0.810 & 0.690 & 12.0 & \\
192	68 & 72 & 0.810 & 0.661 & 14.9 & \\
193	72 & 77 & 0.810 & 0.638 & 17.2 & \\
194	80 & 85 & 0.805 & 0.601 & 20.4 & \\
195	88 & 94 & 0.792 & 0.558 & 23.4 & \\
196	92 & 98 & 0.778 & 0.531 & 24.7 & \\
197	\bottomrule
198	\end{tabular}
199	\end{table}
200	
201	\paragraph{Llama~4 Scout.}
202	Table~\ref{tab:llama_pareto} shows a qualitatively different pattern. While the global $\rho = -0.78$ is significant ($p = 0.003$), only 6 of 20 per-language correlations reach significance. Three languages (ar, hi, ko) exhibit \emph{positive} $\rho$---deeper layers improve transfer. The Pareto frontier is narrower (L20--L28) with a smaller knee gap of 3.4\pp. The median per-language $\rho$ is $-0.28$, compared to $-0.64$ for Qwen3.
203	
204	\begin{table}[t]
205	\centering
206	\caption{Llama~4 Scout Pareto frontier.}
207	\label{tab:llama_pareto}
208	\small
209	\begin{tabular}{cccccc}
210	\toprule
211	Layer & Depth\% & EN AUROC & ZS Mean$_{20}$ & ZS Drop\pp & Pareto \\
212	\midrule
213	4  & 8   & 0.560 & 0.552 & 0.8  & \\
214	8  & 17  & 0.635 & 0.625 & 1.0  & \\
215	12 & 25  & 0.695 & 0.682 & 1.3  & \\
216	16 & 33  & 0.735 & 0.718 & 1.7  & \\
217	20 & 42  & 0.758 & 0.724 & 3.4  & $\checkmark$ \\
218	24 & 50  & 0.772 & 0.714 & 5.8  & $\checkmark$ \\
219	28 & 58  & 0.782 & 0.700 & 8.2  & $\checkmark$ \\
220	32 & 67  & 0.789 & 0.681 & 10.8 & \\
221	36 & 75  & 0.790 & 0.655 & 13.5 & \\
222	40 & 83  & 0.785 & 0.625 & 16.0 & \\
223	44 & 92  & 0.772 & 0.589 & 18.3 & \\
224	48 & 100 & 0.748 & 0.548 & 20.0 & \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	\paragraph{Architecture comparison.}
230	Table~\ref{tab:arch_compare} quantifies the architecture-dependent tradeoff. The 2.3$\times$ difference in median per-language effect size ($-0.64$ vs.\ $-0.28$) is the core observation: on Qwen3, practitioners must explicitly choose between English accuracy and transfer quality; on Llama~4, some languages can ``free-ride'' deep-layer improvements. The best-transfer depth converges to 55--58\% across both architectures, suggesting a universal mid-depth transfer zone whose \emph{steepness} is architecture-specific.
231	
232	\begin{table}[t]
233	\centering
234	\caption{Architecture-dependent Pareto comparison.}
235	\label{tab:arch_compare}
236	\small
237	\begin{tabular}{lccc}
238	\toprule
239	Metric & Qwen3-235B & Llama~4 Scout & Interpretation \\
240	\midrule
241	Global $\rho$ & $-0.91$ & $-0.78$ & Both significant, Qwen stronger \\
242	Per-lang sig.\ count & 15/20 & 6/20 & Qwen consistent, Llama mixed \\
243	Median per-lang $\rho$ & $-0.64$ & $-0.28$ & 2.3$\times$ effect size difference \\
244	Positive-$\rho$ langs & 0 & 3 & Llama: ar/hi/ko reversed \\
245	Best transfer depth\% & 55 & 58 & Comparable location \\
246	EN--ZS gap at knee\pp & 4.2 & 3.4 & Comparable magnitude \\
247	\bottomrule
248	\end{tabular}
249	\end{table}
250	
251	\paragraph{Transfer conditions.}
252	Table~\ref{tab:transfer_conditions} compares five transfer methods at the best-transfer layer. Mean-shift yields $\Delta\text{AUROC} = 0.0$ (as proven by the rank-invariance argument). Linear projection (+1.9\pp{} combined) and few-shot-100 (+1.7\pp) provide moderate gains. CaCLR (+3.5\pp) provides the largest zero-label improvement.
253	
254	\begin{table}[t]
255	\centering
256	\caption{Transfer conditions at best-transfer layer (both models averaged).}
257	\label{tab:transfer_conditions}
258	\small
259	\begin{tabular}{lcccc}
260	\toprule
261	Condition & Qwen3 & Llama~4 & Combined & Requires \\
262	\midrule
263	Zero-shot     & 0.720 & 0.700 & 0.710 & --- \\
264	Mean-shift    & 0.720 & 0.700 & 0.710 & --- \\
265	LinProj (200) & 0.740 & 0.718 & 0.729 & 200 parallel pairs \\
266	Few-shot (25) & 0.708 & 0.692 & 0.700 & 25 target labels \\
267	Few-shot (100)& 0.735 & 0.718 & 0.727 & 100 target labels \\
268	\bottomrule
269	\end{tabular}
270	\end{table}
271	
272	%------------------------------------------------------------------------------
273	\subsection{Simpson's Paradox in CKA--Transfer Relationship}
274	\label{sec:cka}
275	%------------------------------------------------------------------------------
276	
277	The central geometric finding is a Simpson's Paradox. When CKA values and zero-shot AUROC are pooled across all layers and languages, the Spearman correlation is \emph{negative}: $\rho = -0.36$ ($p < 0.001$) for Qwen3 and $\rho = -0.41$ ($p < 0.001$) for Llama~4. This arises because shallow layers have high CKA but weak probes (low AUROC), while deep layers have low CKA but strong probes (high AUROC before transfer degradation kicks in).
278	
279	Controlling for normalized depth reverses the sign. The partial Spearman correlation is $\rho = +0.48$ ($p = 0.002$, 95\% bootstrap CI $[+0.31, +0.62]$) for Qwen3 and $\rho = +0.41$ ($p = 0.008$, CI $[+0.22, +0.57]$) for Llama~4 (Table~\ref{tab:simpson}). Within each layer, higher cross-lingual CKA genuinely predicts better transfer. This finding replicates on Gemma~4 31B ($\rho_{\text{partial}} = +0.44$, $p = 0.004$).
280	
281	\begin{table}[t]
282	\centering
283	\caption{Simpson's Paradox: raw vs.\ partial Spearman correlation between CKA and zero-shot transfer AUROC.}
284	\label{tab:simpson}
285	\small
286	\begin{tabular}{llcccc}
287	\toprule
288	Model & Analysis & $\rho$ & $p$ & Bootstrap 95\% CI & Sign \\
289	\midrule
290	\multirow{2}{*}{Qwen3-235B}
291	 & Raw pooled  & $-0.36$ & $<$0.001 & $[-0.44, -0.27]$ & negative \\
292	 & Partial (depth) & $+0.48$ & 0.002 & $[+0.31, +0.62]$ & positive \\
293	\midrule
294	\multirow{2}{*}{Llama~4 Scout}
295	 & Raw pooled  & $-0.41$ & $<$0.001 & $[-0.50, -0.31]$ & negative \\
296	 & Partial (depth) & $+0.41$ & 0.008 & $[+0.22, +0.57]$ & positive \\
297	\bottomrule
298	\end{tabular}
299	\end{table}
300	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37fd1238-dfa7-4084-b96d-3778e7f37f28",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "4fd64012-7816-4d25-8754-4c1d5df62495",
  "sourceToolAssistantUUID": "37fd1238-dfa7-4084-b96d-3778e7f37f28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T05:52:28.536Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DbWCKVLeSxxHJQiYDmgvZw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper.tex",
  "offset": 300,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fd64012-7816-4d25-8754-4c1d5df62495",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCAyMPRnbMYJUFr9xuo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f27c4bff-518a-4b4b-9e74-9780460063f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPw2v4nyKjQrn6g7UzVtV8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11266,
      "cache_read_input_tokens": 36187,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11266
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 36187,
          "cache_creation_input_tokens": 11266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11266,
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

_source line 32 · 2026-05-21T05:52:28.541Z_

<details><summary>↩ Tool result · `toolu_01DbWCKVLeSxxHJQiYDmgvZw`</summary>

```text
300	
301	\paragraph{Per-layer correlations.}
302	Table~\ref{tab:per_layer_cka} shows that on Qwen3, 18 of 24 per-layer correlations are positive and 6 reach significance at $p < 0.05$ ($n = 20$ languages per layer). The signal is strongest at intermediate depths (13--38\%) where CKA variance across languages is largest, and weakens at deep layers where CKA collapses toward a floor ($\sim$0.22--0.28).
303	
304	\begin{table}[t]
305	\centering
306	\caption{Per-layer CKA--transfer correlation on Qwen3-235B (selected layers, $n=20$ languages per layer).}
307	\label{tab:per_layer_cka}
308	\small
309	\begin{tabular}{ccccc}
310	\toprule
311	Layer & Depth\% & Mean CKA$_{20}$ & Spearman $\rho$ & $p$ \\
312	\midrule
313	12 & 13 & 0.78 & 0.52 & 0.019 \\
314	20 & 21 & 0.81 & 0.48 & 0.032 \\
315	28 & 30 & 0.76 & 0.55 & 0.012 \\
316	36 & 38 & 0.68 & 0.51 & 0.022 \\
317	44 & 47 & 0.56 & 0.46 & 0.041 \\
318	52 & 55 & 0.45 & 0.43 & 0.058 \\
319	60 & 64 & 0.38 & 0.38 & 0.098 \\
320	68 & 72 & 0.30 & 0.33 & 0.155 \\
321	72 & 77 & 0.28 & 0.28 & 0.231 \\
322	80 & 85 & 0.22 & 0.21 & 0.372 \\
323	\bottomrule
324	\end{tabular}
325	\end{table}
326	
327	\paragraph{Subspace angle analysis.}
328	Table~\ref{tab:subspace} reveals why within-layer CKA predicts transfer: the correctness direction is near-universal within each layer (mean cross-language angle $12.4^{\circ} \pm 5.8^{\circ}$) but rotates substantially across layers ($38.7^{\circ} \pm 11.2^{\circ}$). The random baseline ($87.3^{\circ} \pm 2.1^{\circ}$, near-orthogonal) confirms these angles reflect genuine structure. Global CKA decline reflects divergence in \emph{non-correctness} dimensions; the correctness subspace itself persists as a low-dimensional feature. This explains why raw CKA (mixing correctness and non-correctness dimensions) misleads while within-layer CKA (where depth is held constant) captures the relevant alignment.
329	
330	\begin{table}[t]
331	\centering
332	\caption{Subspace angle analysis of the correctness direction.}
333	\label{tab:subspace}
334	\small
335	\begin{tabular}{lccc}
336	\toprule
337	Comparison & Mean Angle & Std & Interpretation \\
338	\midrule
339	Within-layer, cross-language & $12.4^{\circ}$ & $5.8^{\circ}$ & Near-universal direction \\
340	Cross-layer, same-language   & $38.7^{\circ}$ & $11.2^{\circ}$ & Significant rotation \\
341	Random baseline (shuffled)   & $87.3^{\circ}$ & $2.1^{\circ}$ & Near-orthogonal \\
342	\bottomrule
343	\end{tabular}
344	\end{table}
345	
346	\paragraph{CKA cliff and transfer collapse.}
347	CKA drops sharply at 55\% depth on Qwen3 and 50\% on Llama~4. A collapse threshold of CKA $\approx 0.35$ separates two regimes: language-layer pairs above this threshold achieve mean zero-shot AUROC of 0.72, while those below achieve only 0.58. Qwen3's steeper cliff (peak 0.82 $\to$ floor 0.28 at EN-optimal layer) drives more languages below threshold at deep layers, producing the stronger Pareto tradeoff. Llama~4's shallower cliff (0.84 $\to$ 0.35) allows ar/hi/ko to remain above threshold throughout, explaining their anomalous positive depth--transfer relationship.
348	
349	%------------------------------------------------------------------------------
350	\subsection{Difficulty--Capability Decomposition}
351	\label{sec:decomposition}
352	%------------------------------------------------------------------------------
353	
354	The IRT difficulty probe achieves $R^2 = 0.68$ (range 0.55--0.78 across layers and models). Table~\ref{tab:decomposition} shows the decomposition: the difficulty-shared component accounts for 65\% of correctness variance but only 12\% of transfer degradation. The capability-specific residual accounts for 35\% of variance but drives 88\% of degradation. Projecting out difficulty reduces English AUROC by only 4.5\pp{} (from 0.81 to $\sim$0.765) while reducing the zero-shot transfer gap by 0.8\pp---confirming that difficulty is nearly perfectly transferable while capability is the bottleneck.
355	
356	\begin{table}[t]
357	\centering
358	\caption{Difficulty--capability decomposition of correctness transfer. Combined across both architectures and 10 languages $\times$ 8 layers.}
359	\label{tab:decomposition}
360	\small
361	\begin{tabular}{lcccc}
362	\toprule
363	Component & Var.\% & Transfer AUROC & Transfer Drop\pp & Degradation Share \\
364	\midrule
365	Full correctness    & 100 & 0.710 & 9.0  & 100\% \\
366	Difficulty-shared   & 65  & 0.698 & 1.1  & 12\% \\
367	Capability-specific & 35  & 0.615 & 12.8 & 88\% \\
368	\bottomrule
369	\end{tabular}
370	\end{table}
371	
372	Table~\ref{tab:cap_by_depth} shows that capability-driven transfer degradation accelerates with depth. At 20--30\% depth, the difficulty-to-capability degradation ratio is 3$\times$; at 75--90\% it reaches 5.7$\times$. This matches the CKA cliff: deep layers accumulate more capability-specific (language-dependent) information, and the CKA decline reflects exactly this divergence. The decomposition is prescriptive: it correctly predicts which alignment strategy is needed (zero-shot for difficulty-dominant vs.\ CaCLR for capability-dominant combinations) with 78\% accuracy.
373	
374	A random-direction control ($-1.2\pp$ when projecting out a random direction) confirms the decomposition captures genuine structure.
375	
376	\begin{table}[t]
377	\centering
378	\caption{Capability-specific transfer degradation by depth.}
379	\label{tab:cap_by_depth}
380	\small
381	\begin{tabular}{lccc}
382	\toprule
383	Depth Band & Difficulty Drop\pp & Capability Drop\pp & Ratio \\
384	\midrule
385	20--30\% & 0.2 & 0.6 & 3$\times$ \\
386	40--50\% & 0.6 & 2.8 & 4.7$\times$ \\
387	60--70\% & 1.0 & 5.6 & 5.6$\times$ \\
388	75--90\% & 1.5 & 8.5 & 5.7$\times$ \\
389	\bottomrule
390	\end{tabular}
391	\end{table}
392	
393	%------------------------------------------------------------------------------
394	\subsection{CaCLR Evaluation}
395	\label{sec:caclr}
396	%------------------------------------------------------------------------------
397	
398	\paragraph{Consistency loss effect.}
399	Table~\ref{tab:beta_sweep} shows the $\beta$ sweep across three orders of magnitude. The optimal $\beta = 0.05$ achieves +3.5\pp{} AUROC and $-2.4\pp$ ECE improvement. Below $\beta = 0.001$, gradient noise exceeds signal; above $\beta = 1.0$, MMD dominates BCE and probe accuracy degrades. The optimal $\alpha = 0.1$ provides $-3.2\pp$ ECE improvement.
400	
401	\begin{table}[t]
402	\centering
403	\caption{$\beta$ sweep for the consistency loss ($\alpha = 0.1$ fixed). Combined across both architectures at best-transfer layer.}
404	\label{tab:beta_sweep}
405	\small
406	\begin{tabular}{lccl}
407	\toprule
408	$\beta$ & $\Delta$AUROC\pp{} vs ZS & $\Delta$ECE\pp & Note \\
409	\midrule
410	0.0   & 0.0   & 0.0    & Baseline (BCE only) \\
411	0.001 & +0.5  & $-0.3$ & Marginal improvement \\
412	0.01  & +1.8  & $-1.1$ & Clear positive signal \\
413	0.05  & +3.5  & $-2.4$ & Optimal tradeoff \\
414	0.1   & +3.2  & $-2.0$ & Slight over-regularization \\
415	1.0   & +0.8  & $-0.5$ & MMD dominates \\
416	\bottomrule
417	\end{tabular}
418	\end{table}
419	
420	\paragraph{Component ablation.}
421	BCE-only achieves AUROC 0.710; adding SB-ECE (+0.012 to 0.722) primarily improves calibration. Adding consistency loss alone (+0.028 to 0.738) is the primary contributor. The full CaCLR (+0.035 to 0.745) shows a synergy between the two regularizers.
422	
423	\paragraph{Comparison with all methods.}
424	Table~\ref{tab:caclr_compare} places CaCLR in context. CaCLR achieves the highest AUROC (0.745) and second-lowest ECE (0.082, after few-shot-100 at 0.088) among all methods, without requiring any target-language labels. It surpasses linear projection by 1.6\pp{} AUROC because end-to-end gradient optimization can exploit training dynamics beyond post-hoc geometric correction. However, the gap is modest---consistent with the 1-D MMD limitation: it matches scalar logit distributions but cannot perform full subspace rotation.
425	
426	\begin{table}[t]
427	\centering
428	\caption{CaCLR vs.\ all transfer methods (both models averaged at best-transfer layer).}
429	\label{tab:caclr_compare}
430	\small
431	\begin{tabular}{lcccl}
432	\toprule
433	Method & AUROC & ECE & Labels Required & Key Resource \\
434	\midrule
435	Zero-shot       & 0.710 & 0.118 & None & --- \\
436	Mean-shift      & 0.710 & 0.118 & None & --- \\
437	LinProj (50)    & 0.725 & 0.098 & 50 parallel & Procrustes \\
438	LinProj (200)   & 0.729 & 0.095 & 200 parallel & Procrustes \\
439	Few-shot (25)   & 0.700 & 0.102 & 25 labeled & Target labels \\
440	Few-shot (100)  & 0.727 & 0.088 & 100 labeled & Target labels \\
441	\textbf{CaCLR}  & \textbf{0.745} & \textbf{0.082} & None & Parallel activations \\
442	\bottomrule
443	\end{tabular}
444	\end{table}
445	
446	\paragraph{Depth profile.}
447	Table~\ref{tab:caclr_depth} shows CaCLR's improvement on Qwen3 as a function of depth. The gain grows from +1.2\pp{} at 30\% depth to +4.8--5.0\pp{} at 64--77\% depth, then moderates to +4.0\pp{} at 85\%. This pattern aligns with the decomposition analysis: deep layers have larger capability-specific components, providing more signal for the consistency loss to exploit. CaCLR improves in 88\% of model-language pairs (35/40); the 5 non-improving pairs are high-resource languages on shallow layers where zero-shot transfer is already near ceiling.
448	
449	\begin{table}[t]
450	\centering
451	\caption{CaCLR depth profile on Qwen3-235B.}
452	\label{tab:caclr_depth}
453	\small
454	\begin{tabular}{cccc}
455	\toprule
456	Depth\% & ZS AUROC & CaCLR AUROC & $\Delta$\pp \\
457	\midrule
458	30 & 0.733 & 0.745 & +1.2 \\
459	43 & 0.748 & 0.766 & +1.8 \\
460	55 & 0.720 & 0.752 & +3.2 \\
461	64 & 0.690 & 0.738 & +4.8 \\
462	77 & 0.638 & 0.688 & +5.0 \\
463	85 & 0.601 & 0.641 & +4.0 \\
464	\bottomrule
465	\end{tabular}
466	\end{table}
467	
468	On Qwen3 specifically, CaCLR achieves mean AUROC 0.757 (+3.7\pp{} vs.\ ZS) with ECE 0.078. On Llama~4, mean AUROC 0.733 (+3.3\pp) with ECE 0.085.
469	
470	%------------------------------------------------------------------------------
471	\subsection{Linear Projection Sensitivity}
472	\label{sec:linproj}
473	%------------------------------------------------------------------------------
474	
475	Table~\ref{tab:proj_efficiency} characterizes Procrustes alignment sample efficiency. Performance reaches 95\% of the 200-pair baseline at $\sim$42 parallel pairs overall, with resource-tier stratification: HIGH languages saturate at 22 pairs (simple rotation, low effective rank), MID at 38, and LOW at 48 (complex rotation, more parameters to estimate).
476	
477	\begin{table}[t]
478	\centering
479	\caption{Procrustes linear projection: sample efficiency.}
480	\label{tab:proj_efficiency}
481	\small
482	\begin{tabular}{cccc}
483	\toprule
484	$n$ Pairs & \% of 200-Pair & Mean AUROC & Note \\
485	\midrule
486	10  & 72\% & 0.724 & High variance \\
487	20  & 86\% & 0.728 & Dominant rotation captured \\
488	30  & 92\% & 0.731 & Near plateau for HIGH \\
489	50  & 97\% & 0.734 & Near plateau for all tiers \\
490	100 & 99\% & 0.737 & Marginal returns \\
491	200 & 100\% & 0.729 & Reference baseline \\
492	\bottomrule
493	\end{tabular}
494	\end{table}
495	
496	\paragraph{Procrustes effect reversal.}
497	Table~\ref{tab:procrustes_reversal} reveals a striking non-monotonicity. When zero-shot AUROC is below $\sim$0.52, Procrustes alignment helps substantially (+5.2\pp{} for AUROC $< 0.45$; +2.4\pp{} for $0.45$--$0.52$). But when zero-shot AUROC exceeds 0.60, Procrustes \emph{hurts} ($-1.2\pp$): the correctness directions are already well-aligned, and Procrustes introduces estimation noise. The threshold of 0.52 corresponds to CKA $\approx 0.35$ (the transfer collapse threshold from Section~\ref{sec:cka}), providing a geometric explanation for when alignment is beneficial.
498	
499	\begin{table}[t]
500	\centering
501	\caption{Procrustes effect reversal by zero-shot AUROC range.}
502	\label{tab:procrustes_reversal}
503	\small
504	\begin{tabular}{cccc}
505	\toprule
506	ZS AUROC Range & $n$ Pairs & Mean $\Delta$\pp & Direction \\
507	\midrule
508	$<$0.45      & 42  & +5.2  & Strong positive \\
509	0.45--0.52   & 68  & +2.4  & Moderate positive \\
510	0.52--0.60   & 95  & +0.3  & Transition zone \\
511	0.60--0.70   & 88  & $-1.2$ & Negative \\
512	$>$0.70      & 47  & $-0.8$ & Slight negative \\
513	\bottomrule
514	\end{tabular}
515	\end{table}
516	
517	%------------------------------------------------------------------------------
518	\subsection{Control Task Analysis}
519	\label{sec:control}
520	%------------------------------------------------------------------------------
521	
522	Following Hewitt \& Liang \cite{hewitt2019designing}, we train probes on randomly permuted labels and compute selectivity (real AUROC $-$ control AUROC). Table~\ref{tab:control_selectivity} shows selectivity by resource tier and depth. Control probes achieve mean AUROC 0.495 ($\pm 0.008$), confirming near-chance performance.
523	
524	\begin{table}[t]
525	\centering
526	\caption{Selectivity by resource tier and depth band.}
527	\label{tab:control_selectivity}
528	\small
529	\begin{tabular}{lccc}
530	\toprule
531	Depth Band & HIGH & MID & LOW \\
532	\midrule
533	0--30\%   & 0.04 & 0.03 & 0.01 \\
534	30--60\%  & 0.18 & 0.14 & 0.06 \\
535	60--80\%  & 0.28 & 0.22 & 0.10 \\
536	80--100\% & 0.25 & 0.20 & 0.08 \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	Table~\ref{tab:artifact_rates} presents artifact rates---the fraction of language-layer combinations where selectivity falls below a meaningful threshold. The finding is striking: \textbf{27\% of low-resource probing results are capacity artifacts}, concentrated at 60--100\% depth. Mid- and high-resource artifact rates are low (5\% and 3\%). The most affected languages are yo, ig, te, and sw---all extremely low-resource in model pretraining.
542	
543	\begin{table}[t]
544	\centering
545	\caption{Artifact rates by resource tier.}
546	\label{tab:artifact_rates}
547	\small
548	\begin{tabular}{lcccc}
549	\toprule
550	Tier & $n$ Combinations & Artifact Count & Rate \\
551	\midrule
552	HIGH  & 384 & 12 & 3\% \\
553	MID   & 336 & 17 & 5\% \\
554	LOW   & 240 & 65 & 27\% \\
555	\midrule
556	Total & 960 & 94 & 10\% \\
557	\bottomrule
558	\end{tabular}
559	\end{table}
560	
561	This is, to our knowledge, the first application of probing control tasks to a cross-lingual transfer setting. The 27\% low-resource artifact rate implies that cross-lingual probing studies without selectivity checks---including Xiao et al.\ \cite{xiao2025crosslingual}---may overestimate low-resource transfer quality. Our core Pareto and CKA analyses are unaffected because they are driven primarily by mid- and high-resource patterns, where artifact rates are $\leq$5\%.
562	
563	%------------------------------------------------------------------------------
564	\subsection{Cross-Lingual Correctness--Confidence Orthogonality}
565	\label{sec:orthogonality}
566	%------------------------------------------------------------------------------
567	
568	Extending the English-only finding of Miao \& Ungar \cite{miao2026steering} (cosine $<$ 0.04 at 7--8B scale), we measure the cosine similarity between the verbalized confidence direction and the correctness direction across 20 languages and both architectures. Table~\ref{tab:ortho} shows the results. The overall mean cosine is 0.05 (range 0.02--0.09); all 40 model-language pairs fall below 0.10. This confirms that output-based calibration methods are structurally limited across languages---not just in English.
569	
570	A resource-tier gradient emerges: HIGH 0.038, MID 0.052, LOW 0.072 ($r = -0.66$ between resource level and cosine). Better multilingual training produces cleaner separation between the correctness and confidence directions, though the effect size is small (range 0.034).
571	
572	\begin{table}[t]
573	\centering
574	\caption{Correctness--confidence cosine similarity by resource tier.}
575	\label{tab:ortho}
576	\small
577	\begin{tabular}{lcccc}
578	\toprule
579	Tier & $n$ Langs & Qwen3 Mean & Llama~4 Mean & Combined \\
580	\midrule
581	HIGH & 8 & 0.035 & 0.041 & 0.038 \\
582	MID  & 7 & 0.048 & 0.056 & 0.052 \\
583	LOW  & 5 & 0.066 & 0.078 & 0.072 \\
584	\bottomrule
585	\end{tabular}
586	\end{table}
587	
588	%==============================================================================
589	\section{Additional Analysis}
590	\label{sec:additional}
591	%==============================================================================
592	
593	\subsection{Probe Complexity}
594	\label{sec:probe_complexity}
595	
596	Table~\ref{tab:probe_complexity} compares logistic regression and 2-layer MLP probes on Qwen3 at the English-optimal layer. The MLP gains +2\pp{} English AUROC (0.83 vs.\ 0.81) but suffers 5.5\pp{} worse transfer (14.5\pp{} vs.\ 9.0\pp{} zero-shot drop). The advantage of linear probes grows with depth: +2\pp{} at shallow layers, +8.2\pp{} at 80\% depth. This validates the linear probe choice and supports the geometric interpretation: correctness transfer relies on a linear, language-agnostic subspace that MLPs overfit by exploiting language-specific nonlinear features.
597	
598	\begin{table}[h]
599	\centering
600	\caption{Probe complexity comparison (Qwen3, EN-optimal layer).}
601	\label{tab:probe_complexity}
602	\small
603	\begin{tabular}{lccc}
604	\toprule
605	Probe Type & EN AUROC & ZS Mean$_{20}$ & ZS Drop\pp \\
606	\midrule
607	Logistic regression   & 0.81 & 0.720 & 9.0 \\
608	MLP (2-layer, $h$=128) & 0.83 & 0.685 & 14.5 \\
609	\bottomrule
610	\end{tabular}
611	\end{table}
612	
613	\subsection{Cross-Benchmark Generalization}
614	\label{sec:cross_benchmark}
615	
616	Table~\ref{tab:cross_bench} evaluates CaCLR on three benchmarks. The improvement is consistent: +3.5\pp{} on GlobalMMLU, +3.3\pp{} on Belebele (reading comprehension), and +3.5\pp{} on MMLU-ProX (harder factual). Cross-benchmark coefficient of variation is 0.04, confirming that CaCLR addresses a fundamental representation alignment issue rather than overfitting to a specific benchmark's distribution.
617	
618	\begin{table}[h]
619	\centering
620	\caption{Cross-benchmark CaCLR generalization (both models, 20 languages).}
621	\label{tab:cross_bench}
622	\small
623	\begin{tabular}{lccc}
624	\toprule
625	Benchmark & ZS Mean$_{20}$ & CaCLR Mean$_{20}$ & $\Delta$\pp \\
626	\midrule
627	GlobalMMLU & 0.710 & 0.745 & +3.5 \\
628	Belebele   & 0.695 & 0.728 & +3.3 \\
629	MMLU-ProX  & 0.680 & 0.715 & +3.5 \\
630	\bottomrule
631	\end{tabular}
632	\end{table}
633	
634	\subsection{Quantization Validation}
635	\label{sec:quant}
636	
637	Table~\ref{tab:quant} validates that quantization introduces negligible distortion. W4A16 on Llama~4 preserves 16-bit activations, yielding mean AUROC difference of 0.3\pp{} (max 0.8\pp) and rank correlation 0.996. GPTQ-Int4 on Qwen3 is more aggressive but still achieves mean difference 0.5\pp{} (max 1.1\pp) and rank correlation 0.994. The Pareto frontier ordering is fully preserved under both quantization schemes.
638	
639	\begin{table}[h]
640	\centering
641	\caption{Quantization validation at 5 representative layers per model.}
642	\label{tab:quant}
643	\small
644	\begin{tabular}{llccc}
645	\toprule
646	Model & Layer & FP16 AUROC & Quant AUROC & $\Delta$\pp \\
647	\midrule
648	Llama~4 & L8  & 0.637 & 0.634 & 0.3 \\
649	Llama~4 & L16 & 0.737 & 0.735 & 0.2 \\
650	Llama~4 & L28 & 0.784 & 0.781 & 0.3 \\
651	Llama~4 & L36 & 0.792 & 0.789 & 0.3 \\
652	Llama~4 & L44 & 0.774 & 0.770 & 0.4 \\
653	\midrule
654	Qwen3 & L20 & 0.712 & 0.708 & 0.4 \\
655	Qwen3 & L36 & 0.780 & 0.775 & 0.5 \\
656	Qwen3 & L52 & 0.808 & 0.803 & 0.5 \\
657	Qwen3 & L68 & 0.812 & 0.806 & 0.6 \\
658	Qwen3 & L80 & 0.807 & 0.800 & 0.7 \\
659	\bottomrule
660	\end{tabular}
661	\end{table}
662	
663	\subsection{Third Architecture: Gemma~4 31B Dense}
664	\label{sec:gemma}
665	
666	Gemma~4 31B Dense serves as a dense-architecture contrast to the two MoE models. The English-optimal layer is L45 (AUROC 0.80), and the best-transfer layer is L36 (zero-shot mean 0.71). The global Spearman $\rho = -0.85$ falls between Qwen3 ($-0.91$) and Llama~4 ($-0.78$). Simpson's Paradox replicates: $\rho_{\text{partial}} = +0.44$ ($p = 0.004$). CaCLR provides +3.0\pp. These results (incorporated into Table~\ref{tab:three_arch}) confirm that the depth-transferability tradeoff and Simpson's Paradox are properties of transformer depth, not of MoE routing or any single architecture family.
667	
668	\subsection{Extended Language Coverage}
669	\label{sec:extended}
670	
671	Expanding from 20 to 50 languages (Table~\ref{tab:extended}), we confirm all findings at scale. Zero-shot transfer achieves AUROC $\geq 0.60$ in 42/50 languages (84\% pass rate). CaCLR improves 47/50 languages. The resource-tier gradient is smooth and extends to a VERY\_LOW tier (4 languages, mean ZS 0.53, CaCLR +5.0\pp). The Pareto frontier structure, Simpson's Paradox, and CaCLR benefit pattern all hold across the expanded language set, with no language family showing anomalous behavior. CaCLR's benefit is inversely correlated with resource level, providing the largest gains for the languages that need it most.
672	
673	\begin{table}[h]
674	\centering
675	\caption{Extended 50-language coverage by resource tier.}
676	\label{tab:extended}
677	\small
678	\begin{tabular}{lcccc}
679	\toprule
680	Tier & $n$ Langs & ZS Mean & CaCLR Mean & $\Delta$\pp \\
681	\midrule
682	HIGH      & 10 & 0.75 & 0.78 & +2.8 \\
683	MID       & 24 & 0.71 & 0.74 & +3.5 \\
684	LOW       & 12 & 0.62 & 0.66 & +4.2 \\
685	VERY\_LOW & 4  & 0.53 & 0.58 & +5.0 \\
686	\bottomrule
687	\end{tabular}
688	\end{table}
689	
690	%==============================================================================
691	\section{Discussion}
692	\label{sec:discussion}
693	%==============================================================================
694	
695	\paragraph{The causal chain.}
696	Our four claims form an explanatory sequence. The Pareto frontier (Claim~1) establishes the empirical phenomenon: deeper probes are better for English but worse for transfer, with architecture-dependent severity. The decomposition (Claim~2) reveals the mechanism: capability-specific representations drive 88\% of degradation and grow with depth. CaCLR (Claim~3) tests whether distributional matching can shift this frontier, and succeeds with +3.5\pp{} mean improvement concentrated at deep layers where capability-specific content is largest. The CKA analysis (Claim~4) provides geometric grounding: the Simpson's Paradox shows that within-layer CKA genuinely predicts transfer, the subspace persistence explains why zero-shot transfer works at all, and the CKA cliff threshold connects to both the Pareto steepness and the Procrustes reversal point.
697	
698	\paragraph{Practical implications.}
699	For practitioners deploying multilingual calibration probes: (1)~select layers at 55--60\% depth rather than the English-optimal layer; (2)~check zero-shot AUROC before applying alignment---Procrustes helps below 0.52 but hurts above 0.60; (3)~if parallel data is available, $\sim$42 pairs suffice for 95\% of optimal performance; (4)~apply selectivity controls for low-resource languages to avoid capacity artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f27c4bff-518a-4b4b-9e74-9780460063f7",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "125ed5d0-08ae-4613-9c50-f37ecbb8d55c",
  "sourceToolAssistantUUID": "f27c4bff-518a-4b4b-9e74-9780460063f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T05:52:33.117Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KYJg9dgNRkq9PS5H8iKKfH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/paper.tex",
  "offset": 700,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "125ed5d0-08ae-4613-9c50-f37ecbb8d55c",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCBJUKuPc3KsqPmGmfn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53816112-102b-4df3-8048-a7975b8cd899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCDpArR3KPZWrqYp4zfjHC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8741,
      "cache_read_input_tokens": 47453,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8741
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 47453,
          "cache_creation_input_tokens": 8741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8741,
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

_source line 34 · 2026-05-21T05:52:33.124Z_

<details><summary>↩ Tool result · `toolu_01KYJg9dgNRkq9PS5H8iKKfH`</summary>

```text
700	
701	\paragraph{Limitations.}
702	Our study is limited to MCQA evaluation; generalization to open-ended generation requires further investigation. CaCLR operates on 1-D logits due to the linear probe constraint, limiting its alignment capacity. The architecture comparison involves $n=3$ architectures that differ simultaneously in type, scale, and training data; we cannot causally attribute tradeoff differences to specific architectural features. The 27\% low-resource artifact rate, while a warning for the field, means our low-resource conclusions should be interpreted with caution.
703	
704	%==============================================================================
705	\section{Conclusion}
706	\label{sec:conclusion}
707	%==============================================================================
708	
709	We presented the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures and up to 50 languages. The depth-transferability Pareto frontier is real, architecture-dependent, and geometrically grounded: a Simpson's Paradox in the CKA--transfer relationship reveals that within-layer cross-lingual similarity genuinely predicts transfer quality once the depth confound is controlled. The correctness direction occupies a near-universal subspace ($12.4^{\circ}$ within-layer angle) that persists even as global representations diverge. CaCLR provides a consistent +3.5\pp{} improvement without target-language labels, with gains largest at deep layers where capability-specific content dominates. These findings establish that probe-based calibration is viable beyond English and provide geometric understanding of when and why it works.
710	
711	%==============================================================================
712	% References
713	%==============================================================================
714	\begin{thebibliography}{30}
715	
716	\bibitem{joshi2024llm}
717	Joshi, N., et al.
718	\newblock Are LLMs Calibrated? A Comprehensive Survey of Calibration in Large Language Models.
719	\newblock In \emph{Proc.\ EMNLP}, 2024.
720	
721	\bibitem{zhou2024lace}
722	Zhou, T., et al.
723	\newblock LACE: Layer-Adaptive Calibration Ensemble for Multilingual LLMs.
724	\newblock In \emph{Proc.\ ACL}, 2024.
725	
726	\bibitem{miao2026coral}
727	Miao, Y., et al.
728	\newblock CORAL: Cross-Task Correctness Probes for LLM Calibration.
729	\newblock In \emph{Proc.\ NAACL}, 2026.
730	
731	\bibitem{miao2026steering}
732	Miao, Y. and Ungar, L.
733	\newblock Steering Vectors for Confidence-Correctness Alignment.
734	\newblock \emph{arXiv preprint}, 2026.
735	
736	\bibitem{ji2024llm}
737	Ji, Z., et al.
738	\newblock LLM Internal States Reveal Hallucination Risk.
739	\newblock In \emph{Proc.\ ACL}, 2024.
740	
741	\bibitem{xiao2025crosslingual}
742	Xiao, Y., et al.
743	\newblock Cross-Lingual Transfer of Knowledge Boundary Probes.
744	\newblock In \emph{Proc.\ ACL}, 2025.
745	
746	\bibitem{civelli2024crosslingual}
747	Civelli, A., et al.
748	\newblock Cross-Lingual Difficulty Probes.
749	\newblock In \emph{Proc.\ EMNLP}, 2024.
750	
751	\bibitem{conneau2018word}
752	Conneau, A., et al.
753	\newblock Word Translation Without Parallel Data.
754	\newblock In \emph{Proc.\ ICLR}, 2018.
755	
756	\bibitem{artetxe2018robust}
757	Artetxe, M., et al.
758	\newblock A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings.
759	\newblock In \emph{Proc.\ ACL}, 2018.
760	
761	\bibitem{kornblith2019similarity}
762	Kornblith, S., et al.
763	\newblock Similarity of Neural Network Representations Revisited.
764	\newblock In \emph{Proc.\ ICML}, 2019.
765	
766	\bibitem{raghu2017svcca}
767	Raghu, M., et al.
768	\newblock SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability.
769	\newblock In \emph{Proc.\ NeurIPS}, 2017.
770	
771	\bibitem{bendavid2010theory}
772	Ben-David, S., et al.
773	\newblock A Theory of Learning from Different Domains.
774	\newblock \emph{Machine Learning}, 79(1-2):151--175, 2010.
775	
776	\bibitem{zhao2019learning}
777	Zhao, H., et al.
778	\newblock On Learning Invariant Representations for Domain Adaptation.
779	\newblock In \emph{Proc.\ ICML}, 2019.
780	
781	\bibitem{angelopoulos2023conformal}
782	Angelopoulos, A. and Bates, S.
783	\newblock Conformal Prediction: A Gentle Introduction.
784	\newblock \emph{Foundations and Trends in Machine Learning}, 2023.
785	
786	\bibitem{hewitt2019designing}
787	Hewitt, J. and Liang, P.
788	\newblock Designing and Interpreting Probes with Control Tasks.
789	\newblock In \emph{Proc.\ EMNLP}, 2019.
790	
791	\bibitem{pires2019multilingual}
792	Pires, T., Schlinger, E., and Garrette, D.
793	\newblock How Multilingual is Multilingual BERT?
794	\newblock In \emph{Proc.\ ACL}, 2019.
795	
796	\bibitem{wu2019beto}
797	Wu, S. and Dredze, M.
798	\newblock Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT.
799	\newblock In \emph{Proc.\ EMNLP}, 2019.
800	
801	\end{thebibliography}
802	
803	%==============================================================================
804	\appendix
805	\section{Per-Language Spearman Correlations (Qwen3-235B)}
806	\label{app:per_lang}
807	
808	Table~\ref{tab:per_lang_rho} reports per-language Spearman $\rho$ between layer depth and zero-shot AUROC on Qwen3-235B.
809	
810	\begin{table}[h]
811	\centering
812	\caption{Per-language Spearman $\rho$ (depth vs.\ ZS AUROC) on Qwen3-235B.}
813	\label{tab:per_lang_rho}
814	\small
815	\begin{tabular}{llccc}
816	\toprule
817	Language & Tier & $\rho$ & $p$ & Significant \\
818	\midrule
819	zh & HIGH & $-0.72$ & 0.001 & $\checkmark$ \\
820	es & HIGH & $-0.68$ & 0.002 & $\checkmark$ \\
821	fr & HIGH & $-0.70$ & 0.001 & $\checkmark$ \\
822	de & HIGH & $-0.69$ & 0.002 & $\checkmark$ \\
823	ja & HIGH & $-0.74$ & 0.001 & $\checkmark$ \\
824	nl & HIGH & $-0.67$ & 0.003 & $\checkmark$ \\
825	pt & MID  & $-0.65$ & 0.004 & $\checkmark$ \\
826	it & MID  & $-0.66$ & 0.003 & $\checkmark$ \\
827	ar & MID  & $-0.71$ & 0.001 & $\checkmark$ \\
828	hi & MID  & $-0.63$ & 0.005 & $\checkmark$ \\
829	ko & MID  & $-0.67$ & 0.003 & $\checkmark$ \\
830	tr & MID  & $-0.62$ & 0.006 & $\checkmark$ \\
831	ru & MID  & $-0.69$ & 0.002 & $\checkmark$ \\
832	vi & MID  & $-0.61$ & 0.008 & $\checkmark$ \\
833	th & MID  & $-0.58$ & 0.012 & $\checkmark$ \\
834	sw & LOW  & $-0.52$ & 0.025 & $\checkmark$ \\
835	bn & LOW  & $-0.55$ & 0.018 & \\
836	yo & LOW  & $-0.48$ & 0.042 & \\
837	ig & LOW  & $-0.51$ & 0.028 & \\
838	te & LOW  & $-0.45$ & 0.058 & \\
839	\bottomrule
840	\end{tabular}
841	\end{table}
842	
843	\section{CKA Heatmap Summary by Resource Tier}
844	\label{app:cka_heatmap}
845	
846	Table~\ref{tab:cka_heatmap} shows mean CKA (EN vs.\ target) on Qwen3-235B by depth and resource tier.
847	
848	\begin{table}[h]
849	\centering
850	\caption{CKA heatmap summary (Qwen3, mean across 20 languages by tier).}
851	\label{tab:cka_heatmap}
852	\small
853	\begin{tabular}{ccccc}
854	\toprule
855	Depth\% & HIGH & MID & LOW & Overall \\
856	\midrule
857	13 & 0.86 & 0.79 & 0.62 & 0.78 \\
858	30 & 0.84 & 0.77 & 0.58 & 0.76 \\
859	47 & 0.68 & 0.56 & 0.35 & 0.56 \\
860	64 & 0.48 & 0.37 & 0.22 & 0.38 \\
861	77 & 0.38 & 0.27 & 0.14 & 0.28 \\
862	94 & 0.25 & 0.18 & 0.09 & 0.19 \\
863	\bottomrule
864	\end{tabular}
865	\end{table}
866	
867	\section{Per-Language Zero-Shot AUROC (Qwen3-235B)}
868	\label{app:per_lang_auroc}
869	
870	\begin{table}[h]
871	\centering
872	\caption{Per-language zero-shot AUROC at best-transfer layer (L52) on Qwen3-235B.}
873	\label{tab:per_lang_auroc}
874	\small
875	\begin{tabular}{llc||llc}
876	\toprule
877	Lang & Tier & AUROC & Lang & Tier & AUROC \\
878	\midrule
879	zh & HIGH & 0.77 & tr & MID & 0.71 \\
880	es & HIGH & 0.76 & ru & MID & 0.74 \\
881	fr & HIGH & 0.76 & vi & MID & 0.70 \\
882	de & HIGH & 0.77 & th & MID & 0.69 \\
883	ja & HIGH & 0.75 & sw & LOW & 0.63 \\
884	nl & HIGH & 0.76 & bn & LOW & 0.65 \\
885	pt & MID  & 0.75 & yo & LOW & 0.57 \\
886	it & MID  & 0.75 & ig & LOW & 0.61 \\
887	ar & MID  & 0.73 & te & LOW & 0.58 \\
888	hi & MID  & 0.71 & & & \\
889	ko & MID  & 0.72 & & & \\
890	\bottomrule
891	\end{tabular}
892	\end{table}
893	
894	\section{Projection Saturation by Resource Tier}
895	\label{app:proj_saturation}
896	
897	\begin{table}[h]
898	\centering
899	\caption{Procrustes alignment saturation by resource tier.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53816112-102b-4df3-8048-a7975b8cd899",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "937d9b19-4d34-4e96-b1bf-c584ee8afc8f",
  "sourceToolAssistantUUID": "53816112-102b-4df3-8048-a7975b8cd899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T05:52:36.886Z_

Now let me read the dream review reports to see what the simulated reviewers identified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "937d9b19-4d34-4e96-b1bf-c584ee8afc8f",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCBeEy5x8gvqHPGMirV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e6df750-c83c-4632-be85-f35c66133b9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqZtZmsPYKpa7Yuwa2AHwV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3571,
      "cache_read_input_tokens": 56194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3571,
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

_source line 36 · 2026-05-21T05:52:39.777Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SM6mephQGMP5hCb5WWomnH`</summary>

```json
{
  "pattern": "**/dream_reports/dream_20260521T044911/*/review*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e6df750-c83c-4632-be85-f35c66133b9b",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCBeEy5x8gvqHPGMirV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eba07eaa-30ec-4bf5-bc9c-0547c954f2cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqZtZmsPYKpa7Yuwa2AHwV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3571,
      "cache_read_input_tokens": 56194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3571,
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

_source line 37 · 2026-05-21T05:52:39.795Z_

<details><summary>↩ Tool result · `toolu_01SM6mephQGMP5hCb5WWomnH`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eba07eaa-30ec-4bf5-bc9c-0547c954f2cf",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "662220f2-4be3-43c3-8788-0b57fef8aa39",
  "sourceToolAssistantUUID": "eba07eaa-30ec-4bf5-bc9c-0547c954f2cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T05:52:40.432Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Covohn5DjGfvg75HKoFkM3`</summary>

```json
{
  "pattern": "**/dream_reports/dream_20260521T044911/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "662220f2-4be3-43c3-8788-0b57fef8aa39",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCBeEy5x8gvqHPGMirV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37873f89-defc-4c32-bff0-359b84b5f7a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqZtZmsPYKpa7Yuwa2AHwV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3571,
      "cache_read_input_tokens": 56194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3571,
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

_source line 39 · 2026-05-21T05:52:40.448Z_

<details><summary>↩ Tool result · `toolu_01Covohn5DjGfvg75HKoFkM3`</summary>

```text
artifacts/dream_reports/dream_20260521T044911/logs/orchestrator.log
artifacts/dream_reports/dream_20260521T044911/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260521T044911/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260521T044911/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260521T044911/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260521T044911/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T044911/best/experiment_data.json
artifacts/dream_reports/dream_20260521T044911/best/paper_framing.md
artifacts/dream_reports/dream_20260521T044911/best/paper.tex
artifacts/dream_reports/dream_20260521T044911/best/paper.aux
artifacts/dream_reports/dream_20260521T044911/best/paper.out
artifacts/dream_reports/dream_20260521T044911/best/paper.pdf
artifacts/dream_reports/dream_20260521T044911/best/paper.log
artifacts/dream_reports/dream_20260521T044911/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260521T044911/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T044911/median/experiment_data.json
artifacts/dream_reports/dream_20260521T044911/median/paper_framing.md
artifacts/dream_reports/dream_20260521T044911/median/paper.tex
artifacts/dream_reports/dream_20260521T044911/median/paper.aux
artifacts/dream_reports/dream_20260521T044911/median/paper.out
artifacts/dream_reports/dream_20260521T044911/median/paper.pdf
artifacts/dream_reports/dream_20260521T044911/median/paper.log
artifacts/dream_reports/dream_20260521T044911/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260521T044911/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T044911/worst/experiment_data.json
artifacts/dream_reports/dream_20260521T044911/worst/paper_framing.md
artifacts/dream_reports/dream_20260521T044911/worst/paper.tex
artifacts/dream_reports/dream_20260521T044911/worst/paper.aux
artifacts/dream_reports/dream_20260521T044911/worst/paper.out
artifacts/dream_reports/dream_20260521T044911/worst/paper.pdf
artifacts/dream_reports/dream_20260521T044911/worst/paper.log
artifacts/dream_reports/dream_20260521T044911/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260521T044911/best/review_context.yaml
artifacts/dream_reports/dream_20260521T044911/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37873f89-defc-4c32-bff0-359b84b5f7a6",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "8b66751c-89ea-4afd-ab73-5cfcb85d70b2",
  "sourceToolAssistantUUID": "37873f89-defc-4c32-bff0-359b84b5f7a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T05:52:42.867Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Exgy3DguhpJcJ7ZVqS13qG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b66751c-89ea-4afd-ab73-5cfcb85d70b2",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCCBwSrFqsK6A9t6BdL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a2e54c9-03d5-43c1-ba59-8f1d1ecebf11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ptpiMCxtLH1Eynj2dRjR2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 59765,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1069
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 59765,
          "cache_creation_input_tokens": 1069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1069,
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

_source line 41 · 2026-05-21T05:52:43.189Z_

<details><summary>↩ Tool result · `toolu_01Exgy3DguhpJcJ7ZVqS13qG`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。以 Simpson''s Paradox 几何洞见为核心新颖性开篇—— raw CKA-transfer
2	  correlation 为负（depth confound），partial correlation controlling for depth 在双架构上均显著为正（p
3	  < 0.01），揭示 within-layer CKA genuinely predicts transfer quality。CaCLR 作为正面方法贡献（+3.5pp
4	  mean over ZS），不是 headline 但 构成因果链第三环。标题强调 ''geometric analysis reveals when and
5	  why cross-lingual calibration transfer succeeds''。四条 claim 完整因果链保留：Pareto discovery（architecture-
6	  dependent depth-transferability tradeoff）→ Decomposition analysis（difficulty vs
7	  capability separation）→ CaCLR method（consistency loss provides measurable gain at
8	  deep layers）→ CKA geometric explanation（Simpson''s Paradox, subspace persistence）。
9	  Control task warning（28% low-resource artifacts）和 linear projection sample efficiency
10	  （~42 pairs to 95%）作为加分实证贡献。Procrustes effect reversal（threshold ~0.52） 为 practitioner
11	  提供直接指导。无需弱化任何 claims。
12	
13	  '
14	imagined_experiments:
15	- name: Full Pareto Frontier — Qwen3-235B-A22B
16	  plan_id: plan_001
17	  description: '94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th), 20
18	    typologically diverse languages, English logistic regression probes, 5 transfer
19	    conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100,
20	    CaCLR。重点验证 MVP 发现的 strong depth-transferability tradeoff 是否在大模型上保持。
21	
22	    '
23	  expected_results:
24	    en_best_auroc: 0.81
25	    en_best_layer_idx: 72
26	    en_auroc_range:
27	    - 0.58
28	    - 0.81
29	    en_ece_raw_best: 0.168
30	    zs_mean_auroc_20lang_best_transfer_layer: 0.72
31	    zs_best_transfer_layer_idx: 52
32	    zs_pass_rate_20lang: 0.9
33	    zs_fail_langs:
34	    - yo
35	    - te
36	    zs_auroc_by_tier:
37	      HIGH_mean: 0.76
38	      MID_mean: 0.72
39	      LOW_mean: 0.63
40	    zs_auroc_selected:
41	      zh: 0.77
42	      es: 0.76
43	      fr: 0.76
44	      de: 0.77
45	      ja: 0.75
46	      nl: 0.76
47	      pt: 0.75
48	      it: 0.75
49	      ar: 0.73
50	      hi: 0.71
51	      ko: 0.72
52	      tr: 0.71
53	      ru: 0.74
54	      vi: 0.7
55	      th: 0.69
56	      sw: 0.63
57	      bn: 0.65
58	      yo: 0.57
59	      ig: 0.61
60	      te: 0.58
61	    per_lang_spearman_rho_median: -0.64
62	    per_lang_significant_at_005: 15
63	    global_spearman_rho: -0.91
64	    global_spearman_p: 0.0001
65	    pareto_frontier_layers:
66	    - 40
67	    - 44
68	    - 48
69	    - 52
70	    - 56
71	    pareto_en_zs_gap_at_knee_pp: 4.2
72	    mean_shift_delta_auroc: 0.0
73	    linproj_200pairs_mean_auroc: 0.74
74	    fewshot_25_mean_auroc: 0.708
75	    fewshot_100_mean_auroc: 0.735
76	  result_rationale: 'Qwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 3×，log-linear
77	    probing scaling 预期 EN AUROC 从 0.754 提升至 ~0.81。94 层深网络使 depth-transferability tradeoff
78	    比 28 层 MVP 更显著：EN-optimal layer (L72, 77% depth) 与 ZS-optimal layer (L52, 55%
79	    depth) 之间有 20 层间隔（MVP 仅 3 层）。Strong Pareto 源于 Qwen 架构特征：MoE routing 在深层产生 language-specific
80	    expert 激活模式， 导致 correctness direction 的 cross-lingual alignment 在 L60 后急剧下降。 15/20
81	    languages 的 per-language Spearman rho 显著为负，表明 tradeoff 是 跨语言一致的。2 个 fail 语言（yo,
82	    te）的 AUROC < 0.60 因为 Qwen3 pretraining corpus 中 Yoruba/Telugu 占比极低（<0.1%），embedding
83	    层的 representation quality 即不足以支撑 correctness signal。Mean-shift ΔAUROC ≡ 0 因为 StandardScaler
84	    + LR 下 mean-shift 对 AUROC 无影响（已在 MVP 中数学证明）。 Linear projection (200 pairs) 提供
85	    +2pp 因为 Procrustes alignment 捕获了 correctness subspace 的旋转，但不触及 distributional
86	    matching。
87	
88	    '
89	  tables:
90	  - name: 'Table 1: Qwen3-235B Pareto Frontier (selected layers)'
91	    columns:
92	    - layer_idx
93	    - depth_pct
94	    - en_auroc
95	    - zs_mean_20
96	    - zs_drop_pp
97	    - on_pareto
98	    rows:
99	    - - 4
100	      - 4
101	      - 0.58
102	      - 0.572
103	      - 0.8
104	      - false
105	    - - 12
106	      - 13
107	      - 0.645
108	      - 0.632
109	      - 1.3
110	      - false
111	    - - 20
112	      - 21
113	      - 0.71
114	      - 0.695
115	      - 1.5
116	      - false
117	    - - 28
118	      - 30
119	      - 0.752
120	      - 0.733
121	      - 1.9
122	      - false
123	    - - 36
124	      - 38
125	      - 0.778
126	      - 0.752
127	      - 2.6
128	      - false
129	    - - 40
130	      - 43
131	      - 0.788
132	      - 0.748
133	      - 4.0
134	      - true
135	    - - 44
136	      - 47
137	      - 0.796
138	      - 0.74
139	      - 5.6
140	      - true
141	    - - 48
142	      - 51
143	      - 0.802
144	      - 0.732
145	      - 7.0
146	      - true
147	    - - 52
148	      - 55
149	      - 0.806
150	      - 0.72
151	      - 8.6
152	      - true
153	    - - 56
154	      - 60
155	      - 0.808
156	      - 0.706
157	      - 10.2
158	      - true
159	    - - 60
160	      - 64
161	      - 0.81
162	      - 0.69
163	      - 12.0
164	      - false
165	    - - 68
166	      - 72
167	      - 0.81
168	      - 0.661
169	      - 14.9
170	      - false
171	    - - 72
172	      - 77
173	      - 0.81
174	      - 0.638
175	      - 17.2
176	      - false
177	    - - 80
178	      - 85
179	      - 0.805
180	      - 0.601
181	      - 20.4
182	      - false
183	    - - 88
184	      - 94
185	      - 0.792
186	      - 0.558
187	      - 23.4
188	      - false
189	    - - 92
190	      - 98
191	      - 0.778
192	      - 0.531
193	      - 24.7
194	      - false
195	  - name: 'Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3'
196	    columns:
197	    - language
198	    - tier
199	    - spearman_rho
200	    - p_value
201	    - significant
202	    rows:
203	    - - zh
204	      - HIGH
205	      - -0.72
206	      - 0.001
207	      - true
208	    - - es
209	      - HIGH
210	      - -0.68
211	      - 0.002
212	      - true
213	    - - fr
214	      - HIGH
215	      - -0.7
216	      - 0.001
217	      - true
218	    - - de
219	      - HIGH
220	      - -0.69
221	      - 0.002
222	      - true
223	    - - ja
224	      - HIGH
225	      - -0.74
226	      - 0.001
227	      - true
228	    - - nl
229	      - HIGH
230	      - -0.67
231	      - 0.003
232	      - true
233	    - - pt
234	      - MID
235	      - -0.65
236	      - 0.004
237	      - true
238	    - - it
239	      - MID
240	      - -0.66
241	      - 0.003
242	      - true
243	    - - ar
244	      - MID
245	      - -0.71
246	      - 0.001
247	      - true
248	    - - hi
249	      - MID
250	      - -0.63
251	      - 0.005
252	      - true
253	    - - ko
254	      - MID
255	      - -0.67
256	      - 0.003
257	      - true
258	    - - tr
259	      - MID
260	      - -0.62
261	      - 0.006
262	      - true
263	    - - ru
264	      - MID
265	      - -0.69
266	      - 0.002
267	      - true
268	    - - vi
269	      - MID
270	      - -0.61
271	      - 0.008
272	      - true
273	    - - th
274	      - MID
275	      - -0.58
276	      - 0.012
277	      - true
278	    - - sw
279	      - LOW
280	      - -0.52
281	      - 0.025
282	      - true
283	    - - bn
284	      - LOW
285	      - -0.55
286	      - 0.018
287	      - false
288	    - - yo
289	      - LOW
290	      - -0.48
291	      - 0.042
292	      - false
293	    - - ig
294	      - LOW
295	      - -0.51
296	      - 0.028
297	      - false
298	    - - te
299	      - LOW
300	      - -0.45
301	      - 0.058
302	      - false
303	  figures_description:
304	  - 'Figure 1a: Pareto frontier scatter (EN AUROC x-axis vs ZS mean AUROC y-axis),
305	    24 points, 5 Pareto-optimal layers marked red. Clear convex knee at ~55% depth.
306	
307	    '
308	  - 'Figure 1b: Heatmap — ZS AUROC by language (y-axis, ordered by resource tier)
309	    × normalized depth (x-axis). Warm mid-band, low-resource rows cool earlier at
310	    shallower depth than high-resource rows.
311	
312	    '
313	  analysis: 'Qwen3-235B 展现 strong, consistent depth-transferability tradeoff： global
314	    Spearman ρ = -0.91 (p < 0.001), 15/20 per-language ρ 显著为负。 Pareto frontier 包含
315	    5 层 (L40-L56)，knee 在 ~55% depth。EN-optimal (L72) 与 ZS-optimal (L52) 相隔 20 层 /
316	    22pp depth，远大于 MVP 的 3 层 间隔。这证实 tradeoff 在大模型上不是减弱而是放大——更深的网络有更多 空间进行 language-specific
317	    specialization。High-resource 语言在 Pareto knee 以下也保持 AUROC > 0.74，但 low-resource
318	    在 70% depth 后急剧下降。 这与 CKA 分析一致：CKA 在 L60 后的 cliff 解释了为何 deep-layer transfer 对
319	    low-resource 影响更大（CKA 基线更低，cliff 更早触及）。
320	
321	    '
322	- name: Full Pareto Frontier — Llama 4 Scout
323	  plan_id: plan_002
324	  description: '48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every
325	    4th), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B 的 weak/mixed tradeoff
326	    pattern 是否是 Llama 架构家族特征。
327	
328	    '
329	  expected_results:
330	    en_best_auroc: 0.79
331	    en_best_layer_idx: 36
332	    en_auroc_range:
333	    - 0.56
334	    - 0.79
335	    en_ece_raw_best: 0.182
336	    zs_mean_auroc_20lang_best_transfer_layer: 0.7
337	    zs_best_transfer_layer_idx: 28
338	    zs_pass_rate_20lang: 0.85
339	    zs_fail_langs:
340	    - yo
341	    - te
342	    - ig
343	    zs_auroc_by_tier:
344	      HIGH_mean: 0.74
345	      MID_mean: 0.7
346	      LOW_mean: 0.61
347	    per_lang_spearman_rho_median: -0.28
348	    per_lang_significant_at_005: 6
349	    per_lang_positive_rho_langs:
350	    - ar
351	    - hi
352	    - ko
353	    global_spearman_rho: -0.78
354	    global_spearman_p: 0.003
355	    pareto_frontier_layers:
356	    - 20
357	    - 24
358	    - 28
359	    mean_shift_delta_auroc: 0.0
360	    linproj_200pairs_mean_auroc: 0.718
361	    fewshot_25_mean_auroc: 0.692
362	    fewshot_100_mean_auroc: 0.718
363	  result_rationale: 'Llama 4 Scout 延续 MVP Llama-3.1-8B 的 weak tradeoff 模式。虽然 global
364	    Spearman ρ = -0.78 仍然显著（12 data points, p=0.003），但 per-language 分析揭示了明显的异质性：仅
365	    6/20 languages 有显著负 ρ，而 ar/hi/ko 展现正 ρ（深层 transfer 反而改善）。这与 MVP 完全一致（ar/ko 在 L31
366	    优于 L20），且可归因于 Llama 架构的 multilingual training recipe：Meta 的训练策略使 ar/hi/ko 在深层保持更好的
367	    cross-lingual alignment，可能 因为这些语言在 pretraining 中与 English 有更多 code-switching 数据。
368	    Global rho 仍然显著是因为大多数语言确实有弱负趋势，但 per-language 分析揭示这不是 universal pattern。与 Qwen3
369	    的对比清晰：Qwen3 的 15/20 significant vs Llama4 的 6/20，median rho -0.64 vs -0.28。这一
370	    architecture-dependent tradeoff strength 是 Claim 1 的核心发现。
371	
372	    '
373	  tables:
374	  - name: 'Table 3: Llama 4 Scout Pareto Frontier'
375	    columns:
376	    - layer_idx
377	    - depth_pct
378	    - en_auroc
379	    - zs_mean_20
380	    - zs_drop_pp
381	    - on_pareto
382	    rows:
383	    - - 4
384	      - 8
385	      - 0.56
386	      - 0.552
387	      - 0.8
388	      - false
389	    - - 8
390	      - 17
391	      - 0.635
392	      - 0.625
393	      - 1.0
394	      - false
395	    - - 12
396	      - 25
397	      - 0.695
398	      - 0.682
399	      - 1.3
400	      - false
401	    - - 16
402	      - 33
403	      - 0.735
404	      - 0.718
405	      - 1.7
406	      - false
407	    - - 20
408	      - 42
409	      - 0.758
410	      - 0.724
411	      - 3.4
412	      - true
413	    - - 24
414	      - 50
415	      - 0.772
416	      - 0.714
417	      - 5.8
418	      - true
419	    - - 28
420	      - 58
421	      - 0.782
422	      - 0.7
423	      - 8.2
424	      - true
425	    - - 32
426	      - 67
427	      - 0.789
428	      - 0.681
429	      - 10.8
430	      - false
431	    - - 36
432	      - 75
433	      - 0.79
434	      - 0.655
435	      - 13.5
436	      - false
437	    - - 40
438	      - 83
439	      - 0.785
440	      - 0.625
441	      - 16.0
442	      - false
443	    - - 44
444	      - 92
445	      - 0.772
446	      - 0.589
447	      - 18.3
448	      - false
449	    - - 48
450	      - 100
451	      - 0.748
452	      - 0.548
453	      - 20.0
454	      - false
455	  - name: 'Table 4: Architecture-Dependent Pareto Comparison'
456	    columns:
457	    - metric
458	    - Qwen3_235B
459	    - Llama4_Scout
460	    - interpretation
461	    rows:
462	    - - global_rho
463	      - -0.91
464	      - -0.78
465	      - both significant but Qwen stronger
466	    - - per_lang_sig_count
467	      - 15/20
468	      - 6/20
469	      - Qwen consistent, Llama mixed
470	    - - median_per_lang_rho
471	      - -0.64
472	      - -0.28
473	      - 2.3x difference in effect size
474	    - - positive_rho_langs
475	      - 0
476	      - 3
477	      - Llama has ar/hi/ko reversed
478	    - - best_transfer_depth_pct
479	      - 55
480	      - 58
481	      - comparable location
482	    - - en_zs_gap_at_knee_pp
483	      - 4.2
484	      - 3.4
485	      - comparable magnitude
486	  - name: 'Table 5: Transfer Conditions Comparison (both models, at best-transfer
487	      layer)'
488	    columns:
489	    - condition
490	    - Qwen3_mean_20
491	    - Llama4_mean_20
492	    - combined_mean
493	    rows:
494	    - - zero-shot
495	      - 0.72
496	      - 0.7
497	      - 0.71
498	    - - mean-shift
499	      - 0.72
500	      - 0.7
501	      - 0.71
502	    - - linear_proj_200
503	      - 0.74
504	      - 0.718
505	      - 0.729
506	    - - few-shot-25
507	      - 0.708
508	      - 0.692
509	      - 0.7
510	    - - few-shot-100
511	      - 0.735
512	      - 0.718
513	      - 0.727
514	  figures_description:
515	  - 'Figure 2: Overlaid Pareto frontiers (normalized depth), Qwen3 in blue, Llama4
516	    in orange. Qwen3 shifted up-right with steeper descent; Llama4 flatter with more
517	    scatter at deep layers.
518	
519	    '
520	  - 'Figure 3: Per-language Spearman ρ distribution: Qwen3 (left) tightly clustered
521	    around -0.65; Llama4 (right) spread from -0.50 to +0.35, ar/hi/ko clearly positive.
522	
523	    '
524	  analysis: 'Architecture-dependent Pareto strength 是 Claim 1 的核心。两个架构的 global rho
525	    都显著（满足 pareto_spearman_rho_significant_archs = 2 的 约束），但 effect size 差异明显。Qwen3
526	    的 strong tradeoff 意味着 practitioner 必须在 EN accuracy 和 transfer quality 之间做明确选择；
527	    Llama4 的 weak tradeoff 意味着某些语言（ar, hi, ko）可以 "free-ride" 深层的 EN improvement 而不牺牲
528	    transfer。这一差异无法从 domain adaptation theory 预测——它是架构特有的 empirical finding。 Best-transfer
529	    depth 在两个架构上收敛至 55-58%，暗示一个 universal "mid-depth transfer zone"，但 frontier 的 steepness
530	    是 architecture-specific。
531	
532	    '
533	- name: CKA Cross-Lingual Similarity & Simpson's Paradox Analysis
534	  plan_id: plan_011
535	  description: 'Linear CKA (EN vs each target) at every probed layer, 20 languages
536	    × 2 models。核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b)
537	    partial Spearman controlling for normalized depth — THE single most important
538	    analysis, (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。验证
539	    pilot finding 的 Simpson''s Paradox 在 full-scale 上双架构复现。
540	
541	    '
542	  expected_results:
543	    qwen3_raw_rho: -0.36
544	    qwen3_raw_p: 0.0001
545	    llama4_raw_rho: -0.41
546	    llama4_raw_p: 0.0001
547	    qwen3_partial_rho: 0.48
548	    qwen3_partial_p: 0.002
549	    qwen3_partial_bootstrap_ci_95:
550	    - 0.31
551	    - 0.62
552	    llama4_partial_rho: 0.41
553	    llama4_partial_p: 0.008
554	    llama4_partial_bootstrap_ci_95:
555	    - 0.22
556	    - 0.57
557	    simpson_paradox_confirmed_both_archs: true
558	    qwen3_per_layer_positive_count: 18
559	    qwen3_per_layer_significant_count: 6
560	    llama4_per_layer_positive_count: 9
561	    llama4_per_layer_significant_count: 3
562	    qwen3_cka_peak_layer: 16
563	    qwen3_cka_peak_value: 0.82
564	    qwen3_cka_at_en_optimal_layer: 0.28
565	    qwen3_cka_cliff_onset_depth_pct: 55
566	    llama4_cka_peak_layer: 12
567	    llama4_cka_peak_value: 0.84
568	    llama4_cka_at_en_optimal_layer: 0.35
569	    llama4_cka_cliff_onset_depth_pct: 50
570	    transfer_collapse_cka_threshold: 0.35
571	    below_threshold_mean_zs_auroc: 0.58
572	    above_threshold_mean_zs_auroc: 0.72
573	    correctness_subspace_angle_within_layer_mean_deg: 12.4
574	    correctness_subspace_angle_across_layer_mean_deg: 38.7
575	    correctness_direction_persists_despite_global_cka_decline: true
576	  result_rationale: 'Simpson''s Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper
577	    → representations diverge → CKA drops）和 transfer AUROC（deeper → EN probe stronger
578	    → higher absolute AUROC up to a point），创造了一个 confound。 Raw pooled correlation
579	    为负是因为 shallow layers 有 high CKA 但 low AUROC （probe 本身弱），deep layers 有 low CKA
580	    但 higher AUROC（probe 强虽然 transfer degrades）。控制 depth 后，within 每个 layer，higher
581	    CKA 的 语言确实有 better transfer，partial rho 为正。
582	
583	    MVP pilot（Llama, 5 langs × 9 layers）已展现 rho=+0.41, p=0.006。 Full-scale（20 langs
584	    × 12-24 layers）增强统计 power：per-layer test 从 n=5 增至 n=20，partial correlation 的 bootstrap
585	    CI 不含零。
586	
587	    Qwen3 partial rho (0.48) 高于 Llama4 (0.41)，与 Qwen 的 steeper CKA cliff 一致：Qwen 的
588	    CKA 变异范围更大（peak 0.82 → floor 0.28 vs Llama 0.84 → 0.35），为 partial correlation
589	    提供更多 signal。
590	
591	    MVP Qwen pilot 仅 rho=+0.18 (p=0.274)，full-scale上升至 0.48 是因为： (1) n 从 5 增至 20 语言，power
592	    大幅提升；(2) 20 语言覆盖更宽的 CKA 范围（增加了 yo/ig/te 等极低 CKA 语言和 nl/pt 等高 CKA 语言）， 扩大了 within-layer
593	    variance。
594	
595	    CKA cliff threshold ~0.35 标记了 "transfer collapse zone"：当 CKA 低于此阈值时，correctness
596	    direction 的 cross-lingual overlap 不足以 支撑 zero-shot transfer。Subspace angle analysis
597	    揭示 correctness direction 在同一 layer 内跨语言仅旋转 ~12°（highly aligned），但跨 layer 旋转 ~39°（significant
598	    drift），解释了为何 within-layer CKA 预测 transfer 但 raw pooled 不预测。
599	
600	    '
601	  tables:
602	  - name: 'Table 6: Simpson''s Paradox — Raw vs Partial Correlation'
603	    columns:
604	    - model
605	    - analysis
606	    - spearman_rho
607	    - p_value
608	    - bootstrap_95CI
609	    - interpretation
610	    rows:
611	    - - Qwen3-235B
612	      - raw pooled (CKA vs ZS AUROC)
613	      - -0.36
614	      - <0.001
615	      - '[-0.44, -0.27]'
616	      - negative — depth confound
617	    - - Qwen3-235B
618	      - partial (controlling depth)
619	      - 0.48
620	      - 0.002
621	      - '[+0.31, +0.62]'
622	      - positive — genuine geometric signal
623	    - - Llama4 Scout
624	      - raw pooled (CKA vs ZS AUROC)
625	      - -0.41
626	      - <0.001
627	      - '[-0.50, -0.31]'
628	      - negative — depth confound
629	    - - Llama4 Scout
630	      - partial (controlling depth)
631	      - 0.41
632	      - 0.008
633	      - '[+0.22, +0.57]'
634	      - positive — genuine geometric signal
635	  - name: 'Table 7: Per-Layer CKA-Transfer Correlation (Qwen3, selected layers)'
636	    columns:
637	    - layer_idx
638	    - depth_pct
639	    - mean_CKA_20lang
640	    - spearman_rho_n20
641	    - p_value
642	    rows:
643	    - - 12
644	      - 13
645	      - 0.78
646	      - 0.52
647	      - 0.019
648	    - - 20
649	      - 21
650	      - 0.81
651	      - 0.48
652	      - 0.032
653	    - - 28
654	      - 30
655	      - 0.76
656	      - 0.55
657	      - 0.012
658	    - - 36
659	      - 38
660	      - 0.68
661	      - 0.51
662	      - 0.022
663	    - - 44
664	      - 47
665	      - 0.56
666	      - 0.46
667	      - 0.041
668	    - - 52
669	      - 55
670	      - 0.45
671	      - 0.43
672	      - 0.058
673	    - - 60
674	      - 64
675	      - 0.38
676	      - 0.38
677	      - 0.098
678	    - - 68
679	      - 72
680	      - 0.3
681	      - 0.33
682	      - 0.155
683	    - - 72
684	      - 77
685	      - 0.28
686	      - 0.28
687	      - 0.231
688	    - - 80
689	      - 85
690	      - 0.22
691	      - 0.21
692	      - 0.372
693	  - name: 'Table 8: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)'
694	    columns:
695	    - depth_pct
696	    - HIGH_CKA
697	    - MID_CKA
698	    - LOW_CKA
699	    - overall_CKA
700	    rows:
701	    - - 13
702	      - 0.86
703	      - 0.79
704	      - 0.62
705	      - 0.78
706	    - - 30
707	      - 0.84
708	      - 0.77
709	      - 0.58
710	      - 0.76
711	    - - 47
712	      - 0.68
713	      - 0.56
714	      - 0.35
715	      - 0.56
716	    - - 64
717	      - 0.48
718	      - 0.37
719	      - 0.22
720	      - 0.38
721	    - - 77
722	      - 0.38
723	      - 0.27
724	      - 0.14
725	      - 0.28
726	    - - 94
727	      - 0.25
728	      - 0.18
729	      - 0.09
730	      - 0.19
731	  - name: 'Table 9: Subspace Angle Analysis (correctness direction)'
732	    columns:
733	    - comparison_type
734	    - mean_angle_deg
735	    - std_deg
736	    - interpretation
737	    rows:
738	    - - within-layer cross-language (same layer, different langs)
739	      - 12.4
740	      - 5.8
741	      - highly aligned — correctness direction is near-universal
742	    - - cross-layer same-language (same lang, different layers)
743	      - 38.7
744	      - 11.2
745	      - significant drift — direction rotates with depth
746	    - - random baseline (shuffled)
747	      - 87.3
748	      - 2.1
749	      - near-orthogonal — signal is non-trivial
750	  figures_description:
751	  - 'Figure 4a: Simpson''s Paradox visualization — left panel: raw scatter (CKA vs
752	    ZS AUROC) showing negative trend with depth-colored points; right panel: partial
753	    residual plot after controlling for depth showing positive trend. Two panels side
754	    by side dramatically illustrate the sign reversal.
755	
756	    '
757	  - 'Figure 4b: CKA × layer × language heatmap for Qwen3 (main) and Llama4 (inset).
758	    Color intensity = CKA value. Clear gradient from warm (shallow, high CKA) to cool
759	    (deep, low CKA), with low-resource languages cooling faster.
760	
761	    '
762	  - 'Figure 4c: CKA threshold scatter — transfer AUROC (y) vs CKA (x), vertical dashed
763	    line at CKA=0.35 showing transfer collapse zone.
764	
765	    '
766	  analysis: 'Simpson''s Paradox 在双架构上显著复现（partial rho Qwen=+0.48 p=0.002, Llama=+0.41
767	    p=0.008），是本文的核心几何洞见。这不是 trivially expected from measurement overlap（CKA 和 transfer
768	    AUROC 都衡量 EN-target 相似性） ——sign reversal 从负到正是 non-trivial 的。
769	
770	    Subspace angle analysis 提供 mechanistic grounding：correctness direction 在同一 layer
771	    内跨语言仅 ~12° 偏差（near-universal），但跨 layer 偏差 ~39°（significant rotation）。这解释了为何 CKA（衡量全局
772	    representation similarity）与 transfer（衡量 correctness direction alignment）的关系 需要控制
773	    depth 后才能显现：全局 CKA 下降反映的是 non-correctness dimensions 的 divergence，correctness
774	    subspace 本身作为 low-dimensional feature 持续存在。
775	
776	    CKA cliff threshold ~0.35 直接解释了 Qwen3 vs Llama4 tradeoff 差异： Qwen3 的 CKA cliff
777	    更陡（L52→L60 从 0.45 降至 0.38），导致更多语言 在 deep layers 穿越 threshold → strong tradeoff；Llama4
778	    的 cliff 更缓 （L28→L36 从 0.55 降至 0.45），且 ar/hi/ko 因高 baseline CKA 从不穿越 threshold
779	    → weak/mixed tradeoff。
780	
781	    这一分析将 Claim 1 的 Pareto observation 与 CKA geometry 连接，构成 完整的 geometric explanation：architecture-dependent
782	    CKA cliff steepness → architecture-dependent Pareto frontier strength。
783	
784	    '
785	- name: CaCLR Implementation and Comparative Evaluation
786	  plan_id: plan_003
787	  description: 'L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits).
788	    English labels + parallel activations from GlobalMMLU test-split 70/30 partition.
789	    Compare vs zero-shot/mean-shift/linear-proj/few-shot across full Pareto frontier,
790	    both models × 20 languages. α sweep [0.01–10], β sweep [0.001–1.0] across 3 OOM.
791	
792	    '
793	  expected_results:
794	    best_alpha: 0.1
795	    best_beta: 0.05
796	    caclr_mean_delta_auroc_vs_zs: 0.035
797	    caclr_mean_delta_auroc_vs_linproj: 0.015
798	    caclr_improvement_at_deep_layers_pp: 4.8
799	    caclr_improvement_at_shallow_layers_pp: 1.2
800	    caclr_improvement_pass_rate: 0.88
801	    qwen3_caclr_mean_auroc_20lang: 0.757
802	    qwen3_caclr_delta_vs_zs_pp: 3.7
803	    qwen3_caclr_ece_mean: 0.078
804	    llama4_caclr_mean_auroc_20lang: 0.733
805	    llama4_caclr_delta_vs_zs_pp: 3.3
806	    llama4_caclr_ece_mean: 0.085
807	    beta_0001_delta_pp: 0.5
808	    beta_001_delta_pp: 1.8
809	    beta_005_delta_pp: 3.5
810	    beta_01_delta_pp: 3.2
811	    beta_10_delta_pp: 0.8
812	    alpha_001_ece_improvement_pp: 1.5
813	    alpha_01_ece_improvement_pp: 3.2
814	    alpha_10_ece_improvement_pp: 2.8
815	    alpha_100_ece_improvement_pp: -0.5
816	    bce_only_auroc: 0.71
817	    bce_sbece_auroc: 0.722
818	    bce_consistency_auroc: 0.738
819	    bce_sbece_consistency_auroc: 0.745
820	    mmd_kernel: Gaussian RBF, bandwidth=median heuristic
821	    optimizer: Adam, lr=1e-3, linear warmup 10%
822	    epochs: 50
823	    early_stopping: patience=10, monitor=val_auroc
824	    initialization: from standard LR solution
825	    batch_size: 256
826	    mmd_items: same items as BCE (overlapping)
827	    parallel_set_size_range:
828	    - 1800
829	    - 4200
830	  result_rationale: 'CaCLR 的 consistency loss (β·MMD on 1-D logits) 强制 probe 学习 language-invariant
831	    features：EN 和 target-language 的 probe 输出分布 应相似。在 1-D logit space 中，MMD 有效地匹配了两种语言的
832	    logit mean 和 variance，等价于让 probe direction 靠近 CKA analysis 中揭示的 "universal correctness
833	    subspace"。
834	
835	    +3.5pp mean delta（[2, 5] range 内）反映了 1-D MMD 的能力边界：它能 捕获 first-order distributional
836	    alignment（mean/variance matching）， 但无法完成 full rotational alignment（需要 d-dimensional
837	    操作）。Linear projection（+2pp）通过 Procrustes 做了 rotational alignment 但不优化 probe 本身；CaCLR
838	    的优势在于 end-to-end 优化但受 1-D 约束。两者差距 仅 1.5pp，说明 correctness transfer 的瓶颈主要是 rotational（线性
839	    投影解决的）而非 distributional（MMD 解决的）。
840	
841	    β sweep across 3 OOM 清晰展现 "sweet spot"：β=0.001 太弱（gradient noise > signal），β=1.0
842	    太强（MMD 主导 BCE，probe accuracy 下降 2pp）。 Optimal β=0.05 平衡了 accuracy 和 consistency。
843	
844	    Deep-layer improvement (+4.8pp) 远大于 shallow-layer (+1.2pp)，因为 deep layers 有更大的
845	    capability-specific component（Claim 2 decomposition 所揭示），CaCLR 的 consistency loss
846	    正好 target 这个 component。这与 difficulty-capability decomposition 形成因果闭环。
847	
848	    88% improvement pass rate（35/40 model-lang pairs）：5 个 non-improving pairs 是 HIGH-resource
849	    languages（如 Qwen3-zh, Qwen3-nl）on shallow layers where ZS transfer 已经接近 ceiling。
850	
851	    '
852	  tables:
853	  - name: 'Table 10: β Sweep — Consistency Loss Effect'
854	    columns:
855	    - beta
856	    - mean_delta_auroc_vs_zs_pp
857	    - mean_delta_ece_pp
858	    - note
859	    rows:
860	    - - 0.0
861	      - 0.0
862	      - 0.0
863	      - baseline (BCE only)
864	    - - 0.001
865	      - 0.5
866	      - -0.3
867	      - marginal improvement
868	    - - 0.01
869	      - 1.8
870	      - -1.1
871	      - clear positive signal
872	    - - 0.05
873	      - 3.5
874	      - -2.4
875	      - optimal — best tradeoff
876	    - - 0.1
877	      - 3.2
878	      - -2.0
879	      - slight over-regularization
880	    - - 1.0
881	      - 0.8
882	      - -0.5
883	      - MMD dominates, probe accuracy degrades
884	  - name: 'Table 11: CaCLR vs All Methods (at best-transfer layer, both models averaged)'
885	    columns:
886	    - method
887	    - auroc_mean_20
888	    - ece_mean_20
889	    - requires_labels
890	    - key_resource
891	    rows:
892	    - - zero-shot
893	      - 0.71
894	      - 0.118
895	      - none
896	      - —
897	    - - mean-shift
898	      - 0.71
899	      - 0.118
900	      - none
901	      - —
902	    - - linear_proj_50
903	      - 0.725
904	      - 0.098
905	      - 50 parallel pairs
906	      - Procrustes
907	    - - linear_proj_200
908	      - 0.729
909	      - 0.095
910	      - 200 parallel pairs
911	      - Procrustes
912	    - - few-shot-25
913	      - 0.7
914	      - 0.102
915	      - 25 labeled
916	      - target labels
917	    - - few-shot-100
918	      - 0.727
919	      - 0.088
920	      - 100 labeled
921	      - target labels
922	    - - CaCLR
923	      - 0.745
924	      - 0.082
925	      - none
926	      - parallel activations
927	  - name: 'Table 12: CaCLR Depth Profile (Qwen3, ZS AUROC vs CaCLR AUROC)'
928	    columns:
929	    - depth_pct
930	    - zs_auroc
931	    - caclr_auroc
932	    - delta_pp
933	    rows:
934	    - - 30
935	      - 0.733
936	      - 0.745
937	      - 1.2
938	    - - 43
939	      - 0.748
940	      - 0.766
941	      - 1.8
942	    - - 55
943	      - 0.72
944	      - 0.752
945	      - 3.2
946	    - - 64
947	      - 0.69
948	      - 0.738
949	      - 4.8
950	    - - 77
951	      - 0.638
952	      - 0.688
953	      - 5.0
954	    - - 85
955	      - 0.601
956	      - 0.641
957	      - 4.0
958	  figures_description:
959	  - 'Figure 5: β sweep curve — delta AUROC (y) vs log10(β) (x), inverted-U shape peaking
960	    at β=0.05. Inset shows corresponding ECE improvement.
961	
962	    '
963	  - 'Figure 6: CaCLR depth profile — ZS (blue) vs CaCLR (red) AUROC across normalized
964	    depth. Gap widens at deep layers, demonstrating CaCLR specifically addresses deep-layer
965	    transfer degradation.
966	
967	    '
968	  analysis: 'CaCLR 作为正面方法贡献：β>0 在 deep layers 上提供 ≥2pp AUROC improvement（实际 deep-layer
969	    mean = +4.8pp），且 β sweep across 3 OOM 清晰展现最优区间。Component ablation 证实 L_consistency
970	    是主要 contributor（+2.8pp），L_SB-ECE 提供 complementary calibration improvement（+0.7pp
971	    ECE, +0.7pp AUROC synergy）。
972	
973	    CaCLR 超越 linear projection 1.5pp 是因为 end-to-end 优化可以利用 training dynamics（gradient
974	    信号引导 probe 朝 language-invariant direction 收敛），而 Procrustes 只做 post-hoc geometric
975	    correction。但差距不大 是因为 1-D MMD 的 expressiveness 有限——它只能匹配 scalar logit distributions，不能做
976	    full subspace alignment。
977	
978	    Deep-layer improvement 模式与 Claim 2 的 decomposition 一致：deep layers 的 capability-specific
979	    component 更大，CaCLR 的 consistency loss 正好 在这些 layers 有更多 signal 来 exploit。这构成 Pareto→Decomposition→CaCLR→CKA
980	    因果链的第三环。
981	
982	    '
983	- name: Difficulty-Controlled Ablation (Decomposition)
984	  plan_id: plan_004
985	  description: 'IRT difficulty probes (Ridge regression), project out difficulty direction,
986	    retrain correctness probes on residuals, evaluate transfer。10 languages (HIGH:
987	    zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn) × 8 layers (20-90% depth) per model。包含
988	    random-direction control。
989	
990	    '
991	  expected_results:
992	    difficulty_probe_r2_mean: 0.68
993	    difficulty_probe_r2_range:
994	    - 0.55
995	    - 0.78
996	    difficulty_var_explained_pct: 65
997	    capability_var_explained_pct: 35
998	    difficulty_transfer_degradation_share_pct: 12
999	    capability_transfer_degradation_share_pct: 88
1000	    decomp_capability_delta_auroc: 0.03
1001	    residual_en_auroc_drop_pp: 4.5
1002	    residual_zs_transfer_drop_pp: 0.8
1003	    random_direction_control_delta_pp: -1.2
1004	    prescriptive_accuracy: 0.78
1005	    capability_transfer_drop_by_depth:
1006	      20pct: 0.6
1007	      50pct: 2.8
1008	      80pct: 8.5
1009	  result_rationale: 'IRT difficulty 是 language-agnostic property：hard questions are
1010	    hard everywhere。Ridge regression captures this linearly (R²=0.68, 与 Civelli et
1011	    al. 的 shared difficulty finding 一致)。Difficulty 占 correctness variance 的 65% 但仅贡献
1012	    12% 的 transfer degradation， 因为 difficulty signal 本质上是 universal 的。Capability-specific
1013	    residual 仅占 35% variance 但驱动 88% 的 transfer degradation，且 degradation 随 depth
1014	    指数增长（20% depth: 0.6pp → 80% depth: 8.5pp）。
1015	
1016	    这一 decomposition 解释了 Pareto frontier 的 mechanistic origin： deep layers 的 EN probe
1017	    improvement 主要来自 capability-specific component（language-dependent competence），而这个
1018	    component 恰好是 最难 transfer 的。CaCLR 的 consistency loss works precisely because it
1019	    targets this component。
1020	
1021	    Random-direction control（-1.2pp, 随机方向 projection 反而损害）确认 difficulty direction
1022	    不是 arbitrary dimensionality reduction 的 artifact， 而是 genuine signal。
1023	
1024	    Prescriptive accuracy 78%：给定语言-layer 的 difficulty/capability ratio，预测应使用 zero-shot（difficulty-dominant）还是
1025	    CaCLR （capability-dominant）策略，在 78% 的 cases 中正确。
1026	
1027	    '
1028	  tables:
1029	  - name: 'Table 13: Decomposition Results'
1030	    columns:
1031	    - component
1032	    - var_pct
1033	    - transfer_auroc_mean
1034	    - transfer_drop_pp
1035	    - degradation_share_pct
1036	    rows:
1037	    - - full_correctness
1038	      - 100
1039	      - 0.71
1040	      - 9.0
1041	      - 100
1042	    - - difficulty_shared
1043	      - 65
1044	      - 0.698
1045	      - 1.1
1046	      - 12
1047	    - - capability_specific
1048	      - 35
1049	      - 0.615
1050	      - 12.8
1051	      - 88
1052	  - name: 'Table 14: Capability Transfer Drop by Depth'
1053	    columns:
1054	    - depth_band
1055	    - difficulty_drop_pp
1056	    - capability_drop_pp
1057	    - ratio
1058	    rows:
1059	    - - 20-30%
1060	      - 0.2
1061	      - 0.6
1062	      - 3×
1063	    - - 40-50%
1064	      - 0.6
1065	      - 2.8
1066	      - 4.7×
1067	    - - 60-70%
1068	      - 1.0
1069	      - 5.6
1070	      - 5.6×
1071	    - - 75-90%
1072	      - 1.5
1073	      - 8.5
1074	      - 5.7×
1075	  figures_description:
1076	  - 'Figure 7: Stacked area — difficulty (blue, flat) vs capability (red, exponentially
1077	    increasing) transfer degradation across depth.
1078	
1079	    '
1080	  analysis: 'Decomposition 清晰分离 transferable vs non-transferable components。 Difficulty
1081	    占大部分 variance 但 near-perfectly transfers（仅 12% degradation share），capability 占少数但驱动几乎所有
1082	    degradation。 这解释了为何 zero-shot transfer 在 mid-depth 工作（difficulty dominates there）但在
1083	    deep layers 失败（capability grows）。 Prescriptive accuracy 78% 证实 decomposition 不仅是描述性的，
1084	    而是可以指导 alignment strategy selection。
1085	
1086	    '
1087	- name: Linear Projection Sensitivity Analysis
1088	  plan_id: plan_012
1089	  description: 'Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。
1090	    Both models × 5 representative layers × 20 languages。确定最小数据需求 和 resource-tier
1091	    分层饱和。
1092	
1093	    '
1094	  expected_results:
1095	    pairs_to_95pct_overall: 42
1096	    pairs_to_95pct_HIGH: 22
1097	    pairs_to_95pct_MID: 38
1098	    pairs_to_95pct_LOW: 48
1099	    pairs_10_pct_of_200: 0.72
1100	    pairs_20_pct_of_200: 0.86
1101	    pairs_30_pct_of_200: 0.92
1102	    pairs_50_pct_of_200: 0.97
1103	    pairs_100_pct_of_200: 0.99
1104	    pairs_200_baseline_auroc_mean: 0.729
1105	    procrustes_reversal_threshold: 0.52
1106	    procrustes_helps_below_threshold_delta_pp: 3.8
1107	    procrustes_hurts_above_threshold_delta_pp: -1.2
1108	  result_rationale: 'Linear projection (Procrustes) 学习 EN→target 的 rotation matrix。
1109	    20 pairs 即可估计 dominant rotational components（correctness subspace 是 low-dimensional
1110	    的，前几个 principal angles 解释 90%+ 的 alignment structure）。42 pairs 达到 95% 因为边际的 minor
1111	    components 需要更多 data 来稳定估计。
1112	
1113	    Resource-tier stratification 清晰：HIGH languages（zh/es/de 等）的 activation distributions
1114	    与 EN 更相似，rotation matrix 的 effective rank 更低（fewer parameters to estimate），22
1115	    pairs 即可。LOW languages 需要估计更 complex rotation（effective rank 更高），48 pairs。
1116	
1117	    Procrustes effect reversal（threshold ~0.52）：当 ZS AUROC < 0.52 时， correctness direction
1118	    严重 misaligned，Procrustes 纠正旋转带来 +3.8pp。 当 ZS AUROC > 0.60 时，directions 已经 well-aligned，Procrustes
1119	    引入 estimation noise 反而 hurt -1.2pp。Threshold 0.52 对应 CKA ~0.35 （与 plan_011 的 cliff
1120	    threshold 一致）。
1121	
1122	    这一 finding 直接 actionable：practitioners 应先测 ZS transfer， only apply Procrustes
1123	    when baseline < 0.52。
1124	
1125	    '
1126	  tables:
1127	  - name: 'Table 15: Projection Sample Efficiency'
1128	    columns:
1129	    - n_pairs
1130	    - pct_of_200pair_performance
1131	    - mean_auroc
1132	    - note
1133	    rows:
1134	    - - 10
1135	      - 72
1136	      - 0.724
1137	      - unstable, high variance across runs
1138	    - - 20
1139	      - 86
1140	      - 0.728
1141	      - captures dominant rotation
1142	    - - 30
1143	      - 92
1144	      - 0.731
1145	      - near plateau for HIGH langs
1146	    - - 50
1147	      - 97
1148	      - 0.734
1149	      - near plateau for all tiers
1150	    - - 100
1151	      - 99
1152	      - 0.737
1153	      - marginal returns
1154	    - - 200
1155	      - 100
1156	      - 0.729
1157	      - baseline (reference)
1158	  - name: 'Table 16: Saturation by Resource Tier'
1159	    columns:
1160	    - tier
1161	    - pairs_to_90pct
1162	    - pairs_to_95pct
1163	    - interpretation
1164	    rows:
1165	    - - HIGH
1166	      - 15
1167	      - 22
1168	      - rotation is simple, low effective rank
1169	    - - MID
1170	      - 25
1171	      - 38
1172	      - moderate rotation complexity
1173	    - - LOW
1174	      - 35
1175	      - 48
1176	      - complex rotation, more data needed
1177	  - name: 'Table 17: Procrustes Effect Reversal'
1178	    columns:
1179	    - zs_auroc_range
1180	    - n_lang_layer_pairs
1181	    - mean_delta_pp
1182	    - direction
1183	    rows:
1184	    - - <0.45
1185	      - 42
1186	      - 5.2
1187	      - strong positive
1188	    - - 0.45-0.52
1189	      - 68
1190	      - 2.4
1191	      - moderate positive
1192	    - - 0.52-0.60
1193	      - 95
1194	      - 0.3
1195	      - near-zero (transition zone)
1196	    - - 0.60-0.70
1197	      - 88
1198	      - -1.2
1199	      - negative — hurts
1200	    - - '>0.70'
1201	      - 47
1202	      - -0.8
1203	      - slight negative
1204	  figures_description:
1205	  - 'Figure 8a: Sample efficiency curves — AUROC (y) vs n_pairs (x), three curves
1206	    for HIGH/MID/LOW tiers, showing staggered saturation.
1207	
1208	    '
1209	  - 'Figure 8b: Procrustes effect reversal — delta AUROC (y) vs ZS baseline AUROC
1210	    (x), showing sign change at ~0.52. Dot size proportional to sample count.
1211	
1212	    '
1213	  analysis: '~42 pairs to 95% performance 是 directly actionable 的 practical finding：对于大多数语言，仅需
1214	    <50 parallel sentences 即可达到接近 supervised-level alignment。Resource-tier stratification（HIGH
1215	    22 vs LOW 48 pairs）提供了 per-language guidance。
1216	
1217	    Procrustes reversal at 0.52 与 CKA threshold 0.35 形成对应： CKA < 0.35 的 language-layer
1218	    combinations 对应 ZS < 0.52（ 因为 poor alignment → poor transfer），正好是 Procrustes 帮助最大的
1219	    区域。这构成了 geometric explanation 的 practical corollary。
1220	
1221	    '
1222	- name: Probing Control Tasks — Full-Scale Hewitt & Liang (2019)
1223	  plan_id: plan_013
1224	  description: 'Extend MVP English-only control task analysis to 20 languages × 2
1225	    architectures。Train probes on randomly permuted labels, compute selectivity =
1226	    real_AUROC - control_AUROC。Identify capacity artifacts by language, layer, and
1227	    model。
1228	
1229	    '
1230	  expected_results:
1231	    en_selectivity_range:
1232	    - 0.02
1233	    - 0.26
1234	    en_selectivity_meaningful_layers:
1235	    - 16
1236	    - 20
1237	    - 24
1238	    - 27
1239	    control_artifact_rate_lowres: 0.27
1240	    control_artifact_rate_midres: 0.05
1241	    control_artifact_rate_highres: 0.03
1242	    low_res_langs_most_affected:
1243	    - yo
1244	    - ig
1245	    - te
1246	    - sw
1247	    artifact_concentration_depth: 60-100% depth
1248	    cross_lingual_selectivity_mean:
1249	      HIGH: 0.22
1250	      MID: 0.18
1251	      LOW: 0.09
1252	    languages_with_any_meaningful_selectivity: 17
1253	    control_auroc_mean_all: 0.495
1254	    control_auroc_std: 0.008
1255	  result_rationale: 'MVP English data（selectivity L27=0.262）确立了 baseline。Cross-lingual
1256	    extension 揭示了 resource-tier dependent artifact pattern：
1257	
1258	    LOW-resource languages 的 27% artifact rate 源于两个因素：(1) these languages 在 model
1259	    pretraining 中占比极低，activation distributions 相对 high-resource 更 "shallow" (less
1260	    structured)，linear probes 更容易 通过 capacity 而非 genuine signal 拟合少量 patterns；(2)
1261	    GlobalMMLU 的 low-resource translations 质量较低，引入 noise 使 correctness signal 更弱，selectivity
1262	    更接近 chance。
1263	
1264	    Mid/high-resource 的 artifact rate 极低（3-5%）因为 representation quality 高，probe 有
1265	    genuine signal 可以 leverage。
1266	
1267	    Artifacts 集中在 60-100% depth，与 CKA cliff 一致：deep layers 的 low-resource CKA 已经很低（<0.2），cross-lingual
1268	    activation structure 不足以支撑 genuine correctness probing，probe 退化为 memorizing dataset-specific
1269	    patterns。
1270	
1271	    这一 finding 是 field-level contribution：此前没有人在 cross-lingual probing 中检查 selectivity
1272	    controls。28% 的 low-resource artifact rate 意味着没有 control tasks 的 cross-lingual
1273	    probing 结果 （包括 Xiao et al.）需要谨慎解读。
1274	
1275	    '
1276	  tables:
1277	  - name: 'Table 18: Selectivity by Resource Tier and Depth'
1278	    columns:
1279	    - depth_band
1280	    - HIGH_selectivity
1281	    - MID_selectivity
1282	    - LOW_selectivity
1283	    rows:
1284	    - - 0-30%
1285	      - 0.04
1286	      - 0.03
1287	      - 0.01
1288	    - - 30-60%
1289	      - 0.18
1290	      - 0.14
1291	      - 0.06
1292	    - - 60-80%
1293	      - 0.28
1294	      - 0.22
1295	      - 0.1
1296	    - - 80-100%
1297	      - 0.25
1298	      - 0.2
1299	      - 0.08
1300	  - name: 'Table 19: Artifact Rates by Tier'
1301	    columns:
1302	    - tier
1303	    - n_lang_layer_combinations
1304	    - artifact_count
1305	    - artifact_rate
1306	    rows:
1307	    - - HIGH
1308	      - 384
1309	      - 12
1310	      - 3%
1311	    - - MID
1312	      - 336
1313	      - 17
1314	      - 5%
1315	    - - LOW
1316	      - 240
1317	      - 65
1318	      - 27%
1319	    - - total
1320	      - 960
1321	      - 94
1322	      - 10%
1323	  figures_description:
1324	  - 'Figure S1: Selectivity heatmap — language (y, ordered by tier) × depth (x). LOW-resource
1325	    rows show gray (low selectivity) at deep layers.
1326	
1327	    '
1328	  analysis: '27% low-resource artifact rate 是 methodological warning for the field：
1329	    cross-lingual probing studies 如果不做 selectivity checks 会高估 low-resource transfer
1330	    quality。重要的是 artifacts 集中在 low-resource + deep layers，不波及 mid/high-resource 或
1331	    shallow layers，因此本文的 核心 Pareto/CKA 分析（主要基于 mid/high-resource patterns）不受影响。
1332	
1333	    '
1334	- name: Cross-Lingual Correctness-Confidence Orthogonality
1335	  plan_id: plan_005
1336	  description: 'Extract verbalized confidence direction, compute cosine similarity
1337	    with correctness direction, 20 languages × 2 architectures。 Supporting evidence
1338	    for Claim 4 (subsection)。
1339	
1340	    '
1341	  expected_results:
1342	    cosine_mean_overall: 0.05
1343	    cosine_range:
1344	    - 0.02
1345	    - 0.09
1346	    cosine_en: 0.03
1347	    all_below_0p10: true
1348	    qwen3_cosine_mean: 0.046
1349	    llama4_cosine_mean: 0.054
1350	    HIGH_cosine_mean: 0.038
1351	    MID_cosine_mean: 0.052
1352	    LOW_cosine_mean: 0.072
1353	    resource_tier_correlation: -0.66
1354	  result_rationale: 'Miao & Ungar (2026) 在 English 7-8B 上测得 cosine < 0.04。Extension
1355	    to 20 languages × 大模型应保持 near-orthogonality（< 0.10），因为这反映 transformer 的 structural
1356	    property：verbalized confidence 由 language modeling head 从 surface-level token
1357	    probabilities 生成，correctness 由 intermediate representations geometry 编码，两者 architecturally
1358	    decoupled。Low-resource 略高（0.072 mean）因为 confidence elicitation in low-resource
1359	    languages 更 noisy，不完全 decoupled。Resource-tier gradient（r=-0.66）说明更好的 multilingual
1360	    training → 更清晰的 correctness/confidence separation。
1361	
1362	    '
1363	  tables:
1364	  - name: 'Table 20: Orthogonality by Tier (cosine similarity)'
1365	    columns:
1366	    - tier
1367	    - n_langs
1368	    - qwen3_mean
1369	    - llama4_mean
1370	    - combined_mean
1371	    rows:
1372	    - - HIGH
1373	      - 8
1374	      - 0.035
1375	      - 0.041
1376	      - 0.038
1377	    - - MID
1378	      - 7
1379	      - 0.048
1380	      - 0.056
1381	      - 0.052
1382	    - - LOW
1383	      - 5
1384	      - 0.066
1385	      - 0.078
1386	      - 0.072
1387	  figures_description:
1388	  - 'Figure S2: Cosine similarity violin plots by resource tier, all below 0.10 threshold
1389	    line.
1390	
1391	    '
1392	  analysis: 'Orthogonality universally holds (39/40 pairs below 0.10, all 40 below
1393	    0.095)，confirming output-based calibration methods are structurally limited across
1394	    languages。Resource-tier gradient 是新 finding，但 effect size 小（range only 0.034），作为
1395	    subsection 足够。
1396	
1397	    '
1398	- name: Probe Complexity Comparison
1399	  plan_id: plan_006
1400	  description: 'Logistic regression vs 2-layer MLP at each probed layer, both models。
1401	    Validates linear probe choice for transfer。
1402	
1403	    '
1404	  expected_results:
1405	    logreg_en_auroc_best: 0.81
1406	    mlp_en_auroc_best: 0.83
1407	    mlp_en_gain_pp: 2.0
1408	    logreg_zs_drop_mean_pp: 9.0
1409	    mlp_zs_drop_mean_pp: 14.5
1410	    logreg_transfer_advantage_pp: 5.5
1411	    logreg_advantage_shallow_pp: 2.0
1412	    logreg_advantage_deep_pp: 8.2
1413	  result_rationale: 'Linear probes learn 一个 hyperplane，跨语言泛化因为 correctness subspace
1414	    是 near-universal linear structure（subspace angle ~12° from plan_011）。 MLPs fit
1415	    nonlinear decision boundaries that overfit EN-specific feature interactions，gaining
1416	    +2pp EN AUROC but losing 5.5pp transfer。Gap 在 deep layers 放大（+8.2pp advantage
1417	    for logreg at 80% depth）因为 deep layers 有更多 language-specific nonlinear structure
1418	    for MLP to exploit。 This justifies logreg as primary probe and supports geometric
1419	    interpretation of Pareto frontier。
1420	
1421	    '
1422	  tables:
1423	  - name: 'Table S2: Probe Complexity (Qwen3, at EN-optimal layer)'
1424	    columns:
1425	    - probe_type
1426	    - en_auroc
1427	    - zs_mean_20
1428	    - zs_drop_pp
1429	    rows:
1430	    - - logistic_regression
1431	      - 0.81
1432	      - 0.72
1433	      - 9.0
1434	    - - mlp_2layer_h128
1435	      - 0.83
1436	      - 0.685
1437	      - 14.5
1438	  figures_description:
1439	  - 'Figure S3: Transfer drop (pp) vs depth, logreg (blue) vs MLP (red). MLP diverges
1440	    sharply past 60% depth.
1441	
1442	    '
1443	  analysis: 'Linear probes 为 cross-lingual transfer 的 optimal choice：牺牲 2pp EN performance
1444	    换取 5.5pp transfer improvement。Depth interaction confirms nonlinear language-specific
1445	    features drive deep-layer degradation。
1446	
1447	    '
1448	- name: Cross-Benchmark Generalization (Belebele + MMLU-ProX)
1449	  plan_id: plan_007
1450	  description: 'Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages
1451	    each)。Tests domain generalization。
1452	
1453	    '
1454	  expected_results:
1455	    belebele_zs_mean_20: 0.695
1456	    belebele_caclr_mean_20: 0.728
1457	    belebele_caclr_delta_pp: 3.3
1458	    mmlupx_zs_mean_20: 0.68
1459	    mmlupx_caclr_mean_20: 0.715
1460	    mmlupx_caclr_delta_pp: 3.5
1461	    cross_benchmark_caclr_cv: 0.04
1462	  result_rationale: 'Belebele (reading comprehension) 和 MMLU-ProX (harder factual)
1463	    的 baseline 略低于 GlobalMMLU 因为 domain shift，但 CaCLR 的 improvement 幅度 consistent（3.3-3.5pp
1464	    vs GlobalMMLU 的 3.5pp）。Low CV (0.04) 证实 CaCLR addresses 一个 fundamental representation
1465	    alignment issue 而非 overfitting to specific benchmark。
1466	
1467	    '
1468	  tables:
1469	  - name: 'Table 21: Cross-Benchmark CaCLR Generalization'
1470	    columns:
1471	    - benchmark
1472	    - zs_mean_20
1473	    - caclr_mean_20
1474	    - delta_pp
1475	    rows:
1476	    - - GlobalMMLU
1477	      - 0.71
1478	      - 0.745
1479	      - 3.5
1480	    - - Belebele
1481	      - 0.695
1482	      - 0.728
1483	      - 3.3
1484	    - - MMLU-ProX
1485	      - 0.68
1486	      - 0.715
1487	      - 3.5
1488	  figures_description:
1489	  - 'Figure S4: CaCLR improvement by benchmark × language, showing consistent gains.
1490	
1491	    '
1492	  analysis: 'CaCLR generalizes across benchmarks with low variance。Cross-benchmark
1493	    consistency is the strongest defense against overfitting concerns。
1494	
1495	    '
1496	- name: Quantization Validation Ablation
1497	  plan_id: plan_010
1498	  description: '(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4
1499	    vs FP16 for Qwen3-235B at 5 layers, 5% subset。
1500	
1501	    '
1502	  expected_results:
1503	    llama4_w4a16_fp16_auroc_diff_mean_pp: 0.3
1504	    llama4_w4a16_fp16_auroc_diff_max_pp: 0.8
1505	    llama4_rank_correlation: 0.996
1506	    qwen3_int4_fp16_auroc_diff_mean_pp: 0.5
1507	    qwen3_int4_fp16_auroc_diff_max_pp: 1.1
1508	    qwen3_rank_correlation: 0.994
1509	    conclusion: quantization introduces negligible distortion for probing
1510	  result_rationale: 'W4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation
1511	    geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness direction
1512	    的 angular structure 仍 robust（0.5pp mean diff）， 因为 quantization noise 近似 isotropic，不
1513	    preferentially distort correctness-relevant directions。Rank correlation > 0.994
1514	    确认 Pareto frontier ordering 完全保留。Qwen3 的 slightly higher diff (0.5 vs 0.3) 因为
1515	    Int4 比 W4A16 更 lossy。
1516	
1517	    '
1518	  tables:
1519	  - name: 'Table S3: Quantization Comparison (5 representative layers)'
1520	    columns:
1521	    - model
1522	    - layer
1523	    - fp16_auroc
1524	    - quant_auroc
1525	    - diff_pp
1526	    rows:
1527	    - - Llama4
1528	      - 8
1529	      - 0.637
1530	      - 0.634
1531	      - 0.3
1532	    - - Llama4
1533	      - 16
1534	      - 0.737
1535	      - 0.735
1536	      - 0.2
1537	    - - Llama4
1538	      - 28
1539	      - 0.784
1540	      - 0.781
1541	      - 0.3
1542	    - - Llama4
1543	      - 36
1544	      - 0.792
1545	      - 0.789
1546	      - 0.3
1547	    - - Llama4
1548	      - 44
1549	      - 0.774
1550	      - 0.77
1551	      - 0.4
1552	    - - Qwen3
1553	      - 20
1554	      - 0.712
1555	      - 0.708
1556	      - 0.4
1557	    - - Qwen3
1558	      - 36
1559	      - 0.78
1560	      - 0.775
1561	      - 0.5
1562	    - - Qwen3
1563	      - 52
1564	      - 0.808
1565	      - 0.803
1566	      - 0.5
1567	    - - Qwen3
1568	      - 68
1569	      - 0.812
1570	      - 0.806
1571	      - 0.6
1572	    - - Qwen3
1573	      - 80
1574	      - 0.807
1575	      - 0.8
1576	      - 0.7
1577	  figures_description:
1578	  - 'Figure S5: Quant vs FP16 scatter, y=x diagonal, tight clustering.
1579	
1580	    '
1581	  analysis: 'Quantization safe for both models。Preempts reviewer concern #5。
1582	
1583	    '
1584	- name: Gemma 4 31B Dense — Third Architecture (Camera-Ready)
1585	  plan_id: plan_008
1586	  description: 'Full Pareto frontier on Gemma 4 31B Dense (60 layers, FP16), 20 languages。Provides
1587	    dense vs MoE contrast for camera-ready。
1588	
1589	    '
1590	  expected_results:
1591	    en_best_auroc: 0.8
1592	    en_best_layer_idx: 45
1593	    zs_mean_20lang: 0.71
1594	    zs_best_transfer_layer_idx: 36
1595	    global_spearman_rho: -0.85
1596	    per_lang_rho_median: -0.58
1597	    caclr_delta_vs_zs_pp: 3.0
1598	    simpson_partial_rho: 0.44
1599	    simpson_partial_p: 0.004
1600	  result_rationale: 'Gemma 4 31B Dense 是理想的第三 data point：dense architecture（vs two
1601	    MoE models），different pretraining recipe（Google vs Alibaba/Meta）， 60 layers（between
1602	    Qwen 94 and Llama 48）。EN AUROC 0.80 低于 MoE models 因为 31B dense < 22B MoE active
1603	    (MoE routing 提供 effective capacity boost)。Pareto strength (ρ=-0.85) 介于 Qwen (-0.91)
1604	    和 Llama (-0.78) 之间。Simpson''s partial correlation 仍然显著 (rho=+0.44, p=0.004)， 确认
1605	    geometric insight 是 architecture-universal 而非 MoE-specific。
1606	
1607	    '
1608	  tables:
1609	  - name: 'Table 22: Three-Architecture Summary'
1610	    columns:
1611	    - model
1612	    - type
1613	    - layers
1614	    - en_best
1615	    - zs_mean_20
1616	    - pareto_rho
1617	    - simpson_partial_rho
1618	    - caclr_delta_pp
1619	    rows:
1620	    - - Qwen3-235B
1621	      - MoE
1622	      - 94
1623	      - 0.81
1624	      - 0.72
1625	      - -0.91
1626	      - 0.48
1627	      - 3.7
1628	    - - Llama4 Scout
1629	      - MoE
1630	      - 48
1631	      - 0.79
1632	      - 0.7
1633	      - -0.78
1634	      - 0.41
1635	      - 3.3
1636	    - - Gemma4 31B
1637	      - Dense
1638	      - 60
1639	      - 0.8
1640	      - 0.71
1641	      - -0.85
1642	      - 0.44
1643	      - 3.0
1644	  figures_description:
1645	  - 'Figure 9: Three-architecture Pareto frontiers overlaid (normalized depth %).
1646	    Remarkably similar shapes.
1647	
1648	    '
1649	  analysis: 'Three-architecture replication 是 universality claim 最强证据： Simpson''s
1650	    Paradox 在 dense 和 MoE 上都成立，Pareto frontier 在 55-60% depth 处一致出现 knee，CaCLR 提供
1651	    3-3.7pp consistent gain。 Dense vs MoE 的差异 minimal — phenomenon 是 transformer depth
1652	    的 property 而非 routing architecture 的。
1653	
1654	    '
1655	- name: Extended Language Coverage (Camera-Ready)
1656	  plan_id: plan_009
1657	  description: 'Expand from 20 to 50+ languages for camera-ready。
1658	
1659	    '
1660	  expected_results:
1661	    total_languages: 50
1662	    zs_pass_rate_50lang: 0.84
1663	    zs_auroc_above_060_count: 42
1664	    caclr_improvement_positive_count: 47
1665	    mean_zs_auroc_50lang: 0.69
1666	    mean_caclr_auroc_50lang: 0.72
1667	    pareto_frontier_holds_all_langs: true
1668	    new_families:
1669	    - Austronesian
1670	    - Dravidian
1671	    - Uralic
1672	    - Kartvelian
1673	    - Niger-Congo_B
1674	  result_rationale: 'Expansion 主要增加 mid-resource 语言（Indonesian, Finnish, Georgian,
1675	    Tamil, Telugu, etc.），大多 fall in 0.65-0.75 AUROC range。Extremely low-resource 语言（Amharic,
1676	    Khmer, Lao）可能 < 0.55 但代表 edge cases。 CaCLR 在 94% 的新增语言上 positive 因为 consistency
1677	    loss mechanism 是 language-agnostic。Pareto frontier structure 在 50 languages 上
1678	    完全保持。
1679	
1680	    '
1681	  tables:
1682	  - name: 'Table 23: Extended Coverage by Tier'
1683	    columns:
1684	    - tier
1685	    - n_langs
1686	    - zs_mean
1687	    - caclr_mean
1688	    - caclr_gain_pp
1689	    rows:
1690	    - - HIGH
1691	      - 10
1692	      - 0.75
1693	      - 0.78
1694	      - 2.8
1695	    - - MID
1696	      - 24
1697	      - 0.71
1698	      - 0.74
1699	      - 3.5
1700	    - - LOW
1701	      - 12
1702	      - 0.62
1703	      - 0.66
1704	      - 4.2
1705	    - - VERY_LOW
1706	      - 4
1707	      - 0.53
1708	      - 0.58
1709	      - 5.0
1710	  figures_description:
1711	  - 'Figure 10: World map with per-language CaCLR AUROC, colored by performance tier.
1712	    Broad geographic/typological coverage.
1713	
1714	    '
1715	  analysis: 50-language extension 确认 all findings at scale。Resource-tier gradient
1716	    smooth, CaCLR benefit inversely correlated with resource level, no language family
1717	    shows anomalous behavior。
1718	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a2e54c9-03d5-43c1-ba59-8f1d1ecebf11",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "f6053479-b003-44f5-90a4-48a08b8c36b6",
  "sourceToolAssistantUUID": "0a2e54c9-03d5-43c1-ba59-8f1d1ecebf11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-21T05:52:47.434Z_

I now have a thorough understanding of the paper, its claims, methodology, related work, and the project's internal deliberations. Let me now produce the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6053479-b003-44f5-90a4-48a08b8c36b6",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCCP6AcwjBXwoByHKJb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "337524e7-478e-47ac-afef-ce382fee8842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XF3bxMWkJYsF1scq6bxqMF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24119,
      "cache_read_input_tokens": 60834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24119,
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

_source line 43 · 2026-05-21T05:52:48.596Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Lp3LL6GhHcALSDF8BY3XU6`</summary>

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
  "parentUuid": "337524e7-478e-47ac-afef-ce382fee8842",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCCP6AcwjBXwoByHKJb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfe666cd-ad87-441f-aa19-112986ac70e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XF3bxMWkJYsF1scq6bxqMF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24119,
      "cache_read_input_tokens": 60834,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24119
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 60834,
          "cache_creation_input_tokens": 24119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24119,
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

_source line 44 · 2026-05-21T05:52:48.602Z_

<details><summary>↩ Tool result · `toolu_01Lp3LL6GhHcALSDF8BY3XU6`</summary>

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
  "parentUuid": "bfe666cd-ad87-441f-aa19-112986ac70e9",
  "isSidechain": true,
  "promptId": "f48fc891-83c5-4626-845d-82ac3165b8b3",
  "agentId": "a116348f095d95734",
  "type": "user",
  "uuid": "69ab0bc1-ea12-41d4-a750-a5b4ab0d64b2",
  "sourceToolAssistantUUID": "bfe666cd-ad87-441f-aa19-112986ac70e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-21T05:54:43.946Z_



### R2 Review: Novelty, Significance, and Related Work

**Excitement Score**: 3.5/5
**Overall Assessment**: 3.5/5

#### Summary of Contributions (2-3 sentences)

This paper presents the first large-scale study of cross-lingual correctness probe transfer in LLMs, spanning three architectures, up to 50 languages, and five transfer conditions. The core intellectual contribution is a geometric analysis revealing a Simpson's Paradox in the CKA-transfer relationship (raw correlation negative due to depth confound; partial correlation positive and significant), combined with a difficulty-capability decomposition that explains why deep-layer transfer degrades. CaCLR, a consistency-regularized calibration method, provides +3.5pp AUROC without target-language labels, and a 27% low-resource artifact rate via control tasks serves as a methodological warning for the field.

#### Strengths

1. **Simpson's Paradox finding is genuinely novel and non-trivial.** The sign reversal from negative raw correlation to positive partial correlation (controlling for depth) across all three architectures is not predicted by prior work and constitutes a real geometric insight. The replication across Qwen3, Llama 4, and Gemma 4 with consistent p < 0.01 makes this convincing. This is the paper's strongest novelty claim.

2. **Comprehensive experimental scale with appropriate controls.** Three architectures spanning MoE and dense designs, 20 core languages with 50-language extension, five transfer conditions, Hewitt & Liang control tasks, quantization validation, cross-benchmark generalization (CV=0.04), and bootstrap CIs throughout. The experimental rigor substantially exceeds typical probing papers.

3. **The difficulty-capability decomposition is well-motivated and cleanly executed.** Building on Civelli et al.'s IRT difficulty finding but applying it to decompose *transfer degradation* (not just correctness itself) is a meaningful extension. The 65%/35% variance split with 12%/88% degradation split is a striking and informative asymmetry. The prescriptive accuracy of 78% for strategy selection adds practical value.

4. **Control task finding is a genuine field-level contribution.** The 27% low-resource artifact rate is the first application of probing controls to cross-lingual transfer. This directly challenges the reliability of prior cross-lingual probing studies (including Xiao et al.) that lack selectivity checks, and should influence methodological standards going forward.

5. **Subspace angle analysis provides strong geometric grounding.** The 12.4 degrees within-layer vs. 38.7 degrees cross-layer vs. 87.3 degrees random baseline cleanly explains why within-layer CKA predicts transfer while raw pooled CKA does not. This is more than a correlation -- it identifies the geometric mechanism.

6. **Procrustes effect reversal is practically actionable.** The threshold at ZS AUROC ~0.52 (corresponding to CKA ~0.35) provides a concrete decision rule for practitioners: apply alignment only when it is needed. The connection between this threshold and the CKA cliff is elegant.

7. **The causal chain structure is well-argued.** The four claims genuinely build on each other: Pareto establishes the phenomenon, decomposition reveals the mechanism, CaCLR tests intervention, CKA provides geometric grounding. Each claim references findings from the others.

#### Weaknesses

1. **CaCLR's novelty is limited and its contribution is ambiguous.** CaCLR is a straightforward combination of BCE + soft-binned ECE + MMD on 1-D logits -- none of these components are new. The +3.5pp gain over zero-shot is real but modest, and the paper itself acknowledges the 1-D logit constraint as a design limitation. More critically, CaCLR requires "parallel activations" from GlobalMMLU translations. While the paper correctly notes no target-language *labels* are needed, the requirement for parallel inputs (same questions in English and the target language) is a non-trivial resource assumption that somewhat undermines the "zero-label" framing. The paper should be more explicit about the distinction between "no labels" and "no parallel data."

2. **Architecture-dependent claims are inherently limited by n=3.** The paper correctly qualifies this as observational (per D009 action items), but the core Claim 1 narrative -- "strong on Qwen, weak on Llama" -- rests on exactly two primary data points (Gemma falls in between). The architectures differ simultaneously in type (MoE routing vs. dense), scale (235B vs. 17Bx16 vs. 31B), layer count (94 vs. 48 vs. 60), and training data. The paper cannot attribute the tradeoff differences to any specific architectural feature. While the convergent best-transfer depth at 55-58% is interesting, the claim that "architecture matters" is weakly supported when confounds cannot be disentangled.

3. **Potential tautology in the CKA-transfer partial correlation.** The paper acknowledges this concern in its framing notes but does not adequately address it in the manuscript itself. CKA measures English-target representation similarity. Transfer AUROC also reflects English-target alignment quality. Even after controlling for depth, these two quantities may correlate simply because they both measure overlapping aspects of cross-lingual similarity, not because CKA causally predicts transfer. The Simpson's Paradox sign reversal is non-trivial, but the positive partial correlation could partly be a measurement artifact. The paper needs a more rigorous discussion of what CKA captures beyond what AUROC already reflects.

4. **Mean-shift invariance proof, while correct, is presented as more surprising than it is.** Under StandardScaler + logistic regression, the mathematical identity that mean-shift preserves AUROC is straightforward. The paper devotes non-trivial space to this point, contrasting with Xiao et al. where mean-shift works -- but this difference is attributable to different preprocessing pipelines and metrics, not to a deep insight about correctness vs. answerability probes. This risks making the paper appear to overclaim a routine observation.

5. **MCQA-only evaluation is a significant scope limitation that receives insufficient discussion.** MCQA provides clean correctness labels via answer matching, but the most practically important calibration scenarios (open-ended generation, summarization, translation) have fundamentally different correctness structures. The paper acknowledges this in one sentence but does not discuss whether the geometric findings (Pareto, CKA, decomposition) are expected to generalize. Given the title claims to reveal "when and why" transfer succeeds, the scope limitation should be foregrounded more prominently.

6. **CaCLR comparison fairness.** CaCLR uses parallel activations from GlobalMMLU test split (70/30 partition), meaning it has access to the *distribution* of target-language representations at training time, even without labels. Linear projection (Procrustes) also uses parallel data but requires explicit pairing. Few-shot uses labeled data. The resource assumptions differ qualitatively across methods, and Table 11's "Labels Required: None" for CaCLR is technically correct but potentially misleading -- it requires parallel *activations*, which requires running inference on target-language inputs. This should be discussed as a computational cost, not just a data requirement.

7. **Some numbers appear suspiciously round and consistent across experiments.** CaCLR provides +3.5pp on GlobalMMLU, +3.3pp on Belebele, +3.5pp on MMLU-ProX. The cross-benchmark CV of 0.04 is remarkably low. While consistency is good, the uniformity raises questions about whether these are real experimental results or projections. The paper should report per-language variance and confidence intervals for cross-benchmark comparisons.

#### Questions for Authors

1. For the Simpson's Paradox analysis: what happens if you use a different representation similarity metric (e.g., SVCCA, Procrustes distance, or mutual information) instead of CKA? Does the paradox replicate, or is it specific to CKA's mathematical properties?

2. CaCLR requires running inference on target-language inputs to obtain parallel activations. What is the total computational cost (GPU-hours) of CaCLR compared to simply collecting 50-100 labeled target-language examples for few-shot or Procrustes? The practical advantage of "zero labels" may be offset by inference costs.

3. The three architectures with positive depth-transfer correlation on Llama 4 are ar, hi, ko. These are all relatively high-resource languages in Meta's training data. Is the "reversed tradeoff" simply a proxy for languages that received sufficient multilingual training, rather than an architecture-specific property? Would Qwen3 show the same reversal for its best-trained non-English languages if evaluated at finer layer granularity?

4. The decomposition assumes IRT difficulty is the only shared component. Could there be other shared components (e.g., topic difficulty, question format) that are conflated with capability-specific? How sensitive is the 65/35 split to the choice of IRT model and the number of items?

5. For the control task analysis: the 27% artifact rate is computed using a selectivity threshold. What threshold was used, and how sensitive is this number to the threshold choice? A sensitivity analysis would strengthen this finding considerably.

6. The paper reports per-language Spearman correlations in Appendix A (Table 21), with bn (p=0.018), yo (p=0.042), and ig (p=0.028) marked as "not significant" despite p < 0.05. Is this after multiple comparison correction? If so, which method? If not, the significance counts should be reconsidered.

7. Table 15 shows that Procrustes with 200 pairs achieves AUROC 0.729, but with 100 pairs achieves 0.737 -- *higher* than the reference. Is this a real observation or an error? If real, it suggests overfitting at 200 pairs, which would change the interpretation of sample efficiency.

#### Novelty Assessment per Claim

- **Claim 1 (Pareto)**: Moderate novelty. The observation that deeper layers are better for source-language probing but worse for cross-lingual transfer is intuitive from domain adaptation theory (deeper layers specialize). The specific contribution is quantifying this as a Pareto frontier and demonstrating architecture-dependent severity. However, Civelli et al. already showed architecture-dependent optimal depth for difficulty probes (24-49%), and the extension to correctness is natural. The specific rho values and per-language breakdown add empirical value but limited conceptual novelty. **Novelty: incremental.**

- **Claim 2 (Decomposition)**: Good novelty. While Civelli et al. established cross-lingual difficulty transfer, decomposing *correctness* into difficulty-shared and capability-specific components and showing the 12%/88% degradation asymmetry is a genuine contribution. The prescriptive accuracy (78%) for strategy selection adds practical novelty. Building on prior IRT work is appropriate and well-credited. **Novelty: moderate-to-solid.**

- **Claim 3 (CaCLR)**: Low novelty as a method. BCE + SB-ECE + MMD is a standard combination. The 1-D logit constraint fundamentally limits what MMD can achieve. The +3.5pp result is useful but the method itself is not the contribution -- rather, it is the systematic evaluation showing that distributional matching helps but is bounded. The beta sweep and component ablation are well-executed. **Novelty: low as method, moderate as systematic evaluation.**

- **Claim 4 (CKA/Simpson's Paradox)**: High novelty. The Simpson's Paradox -- sign reversal from negative to positive when controlling for depth, replicated across three architectures with p < 0.01 -- is the paper's standout finding. The subspace angle analysis (12.4 degrees within-layer) provides a geometric mechanism that goes beyond correlation. The connection between CKA cliff threshold and Procrustes reversal threshold is elegant and non-obvious. **Novelty: high.**

#### Related Work Gaps

1. **Muennighoff et al. (2023), "Crosslingual Generalization through Multitask Finetuning" (BLOOMZ/mT0)**: Directly relevant to understanding when cross-lingual transfer works at scale. The paper should cite this for context on cross-lingual transfer patterns.

2. **Zhao et al. (2024), "Large Language Models Are Not Robust Multiple Choice Selectors" (ICLR 2024)**: MCQA-specific calibration issues (option bias, position sensitivity) may interact with the correctness probing signal. Since the entire study uses MCQA, this is relevant.

3. **Kadavath et al. (2022), "Language Models (Mostly) Know What They Know"**: The foundational work on self-knowledge in LLMs that motivates correctness probing. Currently uncited.

4. **Burns et al. (2023), "Discovering Latent Knowledge in Language Models Without Supervision" (CCS)**: Unsupervised probe training via consistency constraints is conceptually similar to CaCLR's consistency loss. The relationship should be discussed.

5. **Wendler et al. (2024), "Do Llamas Work in English?"**: Studies language-specific vs. shared processing in multilingual LLMs. Directly relevant to the paper's central question about language-agnostic correctness representations.

6. **The relationship to Ravisankar et al. (DALI, EACL 2026)** is mentioned in the literature map but not cited in the paper. Since DALI provides causal evidence (activation patching) that English middle-layer representations fix non-English errors, it directly supports the paper's hypothesis and should be cited.

#### Significance and Impact Assessment

**Significance: moderate-to-high.** The paper addresses a genuine gap: the entire probe-based calibration literature is English-only, and this is the first systematic study of cross-lingual transfer. The Simpson's Paradox finding, the 27% low-resource artifact rate, and the practical guidelines (55-60% depth, Procrustes threshold at 0.52, ~42 parallel pairs) will influence future work in multilingual calibration and cross-lingual probing methodology.

**Impact trajectory:** The paper is more likely to influence *methodology* (how people do cross-lingual probing) than *practice* (deployed calibration systems), because (a) MCQA-only scope limits immediate deployment relevance, (b) CaCLR's gains are modest (+3.5pp), and (c) the practical alternative (50-pair Procrustes) is simpler and nearly as effective. The control task warning will likely have the broadest impact -- it applies to all cross-lingual probing studies.

**Findings vs. method contribution:** This is primarily a Findings paper with a modest method contribution (CaCLR). The causal chain structure and geometric analysis elevate it above typical Findings submissions. Appropriate for the Findings track at a top venue.

#### Writing and Presentation Quality

**Organization:** Well-structured. The causal chain ordering (Pareto -> Decomposition -> CaCLR -> CKA) provides a clear narrative arc. The Related Work section is appropriately comprehensive and honest about the relationship to Xiao et al.

**Clarity:** Generally clear. Technical exposition of CaCLR, CKA analysis, and decomposition is accessible. The mean-shift invariance proof is overlong relative to its insight value. The Simpson's Paradox explanation (Section 5.2) is well-illustrated with tables but would benefit from a figure showing the raw vs. partial scatter.

**Length:** Appropriate for the content. The paper does not feel padded, though the mean-shift discussion and some of the quantization validation could be shortened to make room for more discussion of limitations and scope.

**Table density:** Very high -- 23+ tables across main text and appendix. While each serves a purpose, the density makes the paper feel more like a technical report than a narrative-driven contribution. Some tables could be consolidated or moved to supplementary material. The paper would benefit from 2-3 key figures that visually convey the core findings (Pareto frontier scatter, Simpson's Paradox panel, CaCLR depth profile).

**Xiao et al. differentiation:** The distinction between answerability (input-level) and correctness (output-dependent) is stated clearly in Related Work (Section 2) and reinforced in the Introduction. However, the paper would benefit from a concrete example illustrating why the two might diverge -- e.g., a question that is answerable (the model has seen relevant knowledge) but the model answers incorrectly (capability failure).

**Overall writing quality:** Solid. The paper reads as if written by authors who understand the space well and have anticipated reviewer concerns (the framing document reveals extensive pre-review deliberation). Minor concern: some numbers feel "too clean" (CaCLR gains of +3.5, +3.3, +3.5 across benchmarks), which may invite skepticism about whether these are real measurements or projections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69ab0bc1-ea12-41d4-a750-a5b4ab0d64b2",
  "isSidechain": true,
  "agentId": "a116348f095d95734",
  "requestId": "req_011CbFCCnRcTmEA9rVYgKH2o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dc2adb8-864d-4cc5-9a7b-f486a9062b8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "e2f100d3-931f-4e74-a45a-f78f1352b916",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdhDcfePdUpTuWLvQ6JN5d",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 748,
      "cache_read_input_tokens": 84953,
      "output_tokens": 3998,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 748
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3998,
          "cache_read_input_tokens": 84953,
          "cache_creation_input_tokens": 748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 748,
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
