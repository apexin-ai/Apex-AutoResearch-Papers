# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus: **novelty, significance, positioning against related work

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae89d08b99e7d703f.jsonl`
- **Structured JSON:** [`be768c05889548386470.json`](../../sessions/be/be768c05889548386470.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

54 recorded events

### User

_source line 1 · 2026-05-20T21:13:07.596Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus: **novelty, significance, positioning against related work, and writing quality**.

## Paper Summary
"Does Probe-Based Calibration Work Beyond English?" — A systematic investigation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), up to 52 languages, 5 transfer conditions.

The paper frames itself as a "sobering empirical reality check" for the probe-based calibration line. It is predominantly a negative-results paper.

## Three Claimed Novel Contributions:
1. **Mean-shift rank-invariance theorem**: Under StandardScaler + logistic regression, mean-shift adaptation produces ΔAUROC ≡ 0. This is a simple mathematical proof (Theorem 1): mean subtraction adds a constant to all logits, preserving ranks, so AUROC is unchanged. Distinguished from Xiao et al. [2025] who transferred knowledge-boundary probes (not correctness) using mean-shift with accuracy (threshold-dependent) as metric.

2. **Resource-tier taxonomy**: First quantification across 52 languages. High-resource: 7–8pp drop, 70% pass. Mid: 10–12pp, 28% pass. Low: 13–20pp, 7% pass. Very-low: 0% pass. Control tasks reveal 28% of low-resource results are capacity artifacts (selectivity < 8pp).

3. **Practical recommendation**: Few-shot (25–100 labels) is the only viable path. Zero-label dream is closed for low-resource languages.

## Additional Findings (not claimed as novel):
- CaCLR (distributional matching via MMD consistency loss) fails: d=0.04 vs zero-shot, p=0.71. Consistency loss is inert across 3 OOM of β sweep
- Pareto frontier (depth–transferability tradeoff) is architecture-dependent: ρ ranges −0.44 (dense) to −0.18 (MoE-small), cross-architecture τ = 0.33
- Difficulty decomposition is inconclusive: −0.5pp on average, barely above random-direction control (−0.3pp)
- CKA mechanistic analysis is suggestive but weak: r = 0.32 overall
- Orthogonality (Miao & Ungar 2026) extends cross-lingually: mean cosine 0.074, but with outliers up to 0.172

## Related Work (from the paper)
- **Probe-based calibration**: CORAL [Miao et al. 2024], CCPS [Liu et al. 2024], Confidence Manifold [Luo et al. 2024], Miao & Ungar [2026] — all English-only
- **Cross-lingual probing**: Xiao et al. [2025] — knowledge-boundary probes (different target), 8 languages, mean-shift with accuracy metric
- **Cross-lingual alignment**: MUSE [Conneau et al. 2018], VecMap [Artetxe et al. 2018] — motivates linear projection baseline
- **Domain adaptation theory**: Ben-David et al. [2010] H-divergence framework — resource-tier gradient consistent with theory
- **Representation similarity**: CKA [Kornblith et al. 2019]
- **Probing methodology**: Hewitt & Liang [2019] control tasks

## Paper Structure (11 pages)
1. Introduction (1.5 pages)
2. Related Work (1 page) — 5 subcategories
3. Method (1.5 pages) — probing setup, 5 transfer conditions, rank-invariance theorem, difficulty decomposition, orthogonality measurement
4. Experimental Setup (0.5 page)
5. Results (4 pages) — 12 subsections covering all experiments
6. Analysis (0.5 page) — three Q&A paragraphs
7. Conclusion (0.5 page) + Limitations paragraph
References: 12 entries

## Writing Observations
- Title is a question — appropriate for an empirical survey
- Abstract is dense and quantitative — packs many numbers
- Paper reads as a comprehensive survey with negative/sobering findings
- The "three surviving contributions" framing is honest about what didn't work
- 13 tables in 11 pages — very table-heavy
- Figures are described but I'm evaluating based on the text

## Your Review Task
Evaluate ONLY novelty, significance, related work positioning, and presentation. Produce:

1. **Novelty Assessment** (for each of the 3 claimed contributions: is it genuinely novel? incremental? obvious?)
2. **Significance** (does this paper change how the community thinks/works? who benefits?)
3. **Related Work Positioning** (fair? missing references? proper differentiation from Xiao et al.?)
4. **Writing Quality** (clarity, organization, density, any issues)
5. **Strengths** (3-5 bullet points)
6. **Weaknesses** (3-5 bullet points with severity: minor/moderate/major)
7. **Questions for Authors** (2-3 questions about novelty/positioning)
8. **Score** (1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)
9. **Confidence** (1-5)

Be rigorous. Top ML venue, ~25% acceptance rate. Negative-results papers can be valuable but need to clear a high bar for insight and methodology.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "f20fd7c0-3147-4840-b436-32d668d278e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T21:13:07.599Z_

```json
{
  "parentUuid": "f20fd7c0-3147-4840-b436-32d668d278e0",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
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
  "uuid": "9bb25186-a97a-491a-ac31-ad3648e38209",
  "timestamp": "2026-05-20T21:13:07.599Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T21:13:10.661Z_



I'll review the paper by first reading the full manuscript and any supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bb25186-a97a-491a-ac31-ad3648e38209",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWaHs6irMo4rVU8GJqK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55bc2f86-5f58-4066-a738-8102514a0929",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeYH5QNxsCoVACLSBvChHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7449,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7449,
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

_source line 4 · 2026-05-20T21:13:11.615Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LoxHqxgnY44G3x26msk5SK`</summary>

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
  "parentUuid": "55bc2f86-5f58-4066-a738-8102514a0929",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWaHs6irMo4rVU8GJqK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a96b6aa0-2aba-4859-bf61-45c7ab80f036",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeYH5QNxsCoVACLSBvChHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7449,
      "cache_read_input_tokens": 8251,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7449
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 122,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7449,
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

_source line 5 · 2026-05-20T21:13:11.618Z_

<details><summary>↩ Tool result · `toolu_01LoxHqxgnY44G3x26msk5SK`</summary>

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
  "parentUuid": "a96b6aa0-2aba-4859-bf61-45c7ab80f036",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "f0f50c30-9284-41a3-876f-f0ff40359c97",
  "sourceToolAssistantUUID": "a96b6aa0-2aba-4859-bf61-45c7ab80f036",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T21:13:15.059Z_



Let me read the paper and supporting materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0f50c30-9284-41a3-876f-f0ff40359c97",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWab4CyvEpJmRdJnxQL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "313dc5bf-b774-40d8-b162-bda8db6b1d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh1Nf2kFNkX8TBBTdbSfNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 15700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
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

_source line 7 · 2026-05-20T21:13:15.935Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NhpQNuSKUeqGPi9NxseGhd`</summary>

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
  "parentUuid": "313dc5bf-b774-40d8-b162-bda8db6b1d0e",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWab4CyvEpJmRdJnxQL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e838b0cb-4acd-4d28-bc13-5eec69f00f6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh1Nf2kFNkX8TBBTdbSfNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 15700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
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

_source line 8 · 2026-05-20T21:13:15.978Z_

<details><summary>↩ Tool result · `toolu_01NhpQNuSKUeqGPi9NxseGhd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_003** (success): Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). ← 基于 mvp_001\\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\\n- **mvp_002** (success): Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与 mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际 28 层，index 0-27） ← 基于 mvp_001\\n\\n## 趋势\\n成功 3 / 负向 0 / 失败 0 / 共 3\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-13176: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1012, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e838b0cb-4acd-4d28-bc13-5eec69f00f6c",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "68c5099e-5e05-49c8-9cc2-fcefcd48aec4",
  "sourceToolAssistantUUID": "e838b0cb-4acd-4d28-bc13-5eec69f00f6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T21:13:17.020Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TTBcsXU5oJ1DzK1GZF76Xc`</summary>

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
  "parentUuid": "68c5099e-5e05-49c8-9cc2-fcefcd48aec4",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWab4CyvEpJmRdJnxQL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e08977c3-c76c-4ec6-abef-b5e42e17125e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh1Nf2kFNkX8TBBTdbSfNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 15700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
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

_source line 10 · 2026-05-20T21:13:17.032Z_

<details><summary>↩ Tool result · `toolu_01TTBcsXU5oJ1DzK1GZF76Xc`</summary>

```text
artifacts/dream_reports/dream_20260520T185641/best/paper.tex
artifacts/dream_reports/dream_20260520T185641/median/paper.tex
artifacts/dream_reports/dream_20260520T185641/worst/paper.tex
artifacts/dream_reports/dream_20260520T201854/best/paper.tex
artifacts/dream_reports/dream_20260520T201854/median/paper.tex
artifacts/dream_reports/dream_20260520T201854/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e08977c3-c76c-4ec6-abef-b5e42e17125e",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "6ae878a9-9aa7-465e-9391-8ae63130f176",
  "sourceToolAssistantUUID": "e08977c3-c76c-4ec6-abef-b5e42e17125e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T21:13:17.091Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Q5oiUC27Pz7TrhGMSCaNbX`</summary>

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
  "parentUuid": "6ae878a9-9aa7-465e-9391-8ae63130f176",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWab4CyvEpJmRdJnxQL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30f7cf33-d13e-4d4f-a053-c96732336922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh1Nf2kFNkX8TBBTdbSfNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 15700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
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

_source line 12 · 2026-05-20T21:13:17.100Z_

<details><summary>↩ Tool result · `toolu_01Q5oiUC27Pz7TrhGMSCaNbX`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30f7cf33-d13e-4d4f-a053-c96732336922",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "e8db5302-5511-463a-a2d3-233b74de6af6",
  "sourceToolAssistantUUID": "30f7cf33-d13e-4d4f-a053-c96732336922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T21:13:20.302Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GgxgPdRaVyhy4ida3FNnpM`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/",
  "description": "List dream report directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8db5302-5511-463a-a2d3-233b74de6af6",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWazfXF6UcqZUX4yAnt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45954619-dfb6-4309-9b67-6c7bc2d071b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDBGJzoz9CKvu8xeC1cTek",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 17144,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1298
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 17144,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1298,
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

_source line 14 · 2026-05-20T21:13:20.489Z_

<details><summary>↩ Tool result · `toolu_01GgxgPdRaVyhy4ida3FNnpM`</summary>

```text
total 20
drwxr-xr-x 4 ubuntu ubuntu 4096 May 20 20:18 .
drwxr-xr-x 5 ubuntu ubuntu 4096 May 20 20:34 ..
drwxr-xr-x 6 ubuntu ubuntu 4096 May 20 19:57 dream_20260520T185641
drwxr-xr-x 6 ubuntu ubuntu 4096 May 20 20:53 dream_20260520T201854
lrwxrwxrwx 1 ubuntu ubuntu  124 May 20 19:57 latest -> /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45954619-dfb6-4309-9b67-6c7bc2d071b5",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "f76f6a48-346d-4f85-8960-e2b11cf85df8",
  "sourceToolAssistantUUID": "45954619-dfb6-4309-9b67-6c7bc2d071b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-20T21:13:23.242Z_

Let me read the latest dream report paper (the "best" variant) to review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f76f6a48-346d-4f85-8960-e2b11cf85df8",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWbEyFDfPFKN83pE6Te",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea20b1ca-a6b4-4cbd-8a1b-d51e06d4bde0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qrdx2Y1HG6DEFfhtWv9V45",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 324,
      "cache_read_input_tokens": 18442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 324,
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

_source line 16 · 2026-05-20T21:13:23.599Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NPVXfvJroVWXAr5DzZrGci`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea20b1ca-a6b4-4cbd-8a1b-d51e06d4bde0",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWbEyFDfPFKN83pE6Te",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9d9b5ca-fb7e-4e0e-9a0f-23217c119bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qrdx2Y1HG6DEFfhtWv9V45",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 324,
      "cache_read_input_tokens": 18442,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 324
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 18442,
          "cache_creation_input_tokens": 324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 324,
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

_source line 17 · 2026-05-20T21:13:23.897Z_

<details><summary>↩ Tool result · `toolu_01NPVXfvJroVWXAr5DzZrGci`</summary>

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
11	\usepackage{enumitem}
12	\usepackage[T1]{fontenc}
13	\usepackage[utf8]{inputenc}
14	\usepackage{microtype}
15	\usepackage{tabularx}
16	\usepackage{natbib}
17	\usepackage[colorlinks,citecolor=blue,urlcolor=blue]{hyperref}
18	
19	\title{Cross-Lingual Calibration via Internal Correctness Directions:\\Pareto Frontiers, Decomposition, and Consistency-Aligned Probes}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	Multilingual large language models exhibit substantially worse calibration in non-English languages, yet probe-based calibration methods remain English-only.
28	We present the first systematic study of cross-lingual correctness probe transfer across 20 languages on two MoE architectures (Qwen3-235B-A22B, Llama~4~Scout).
29	We discover a \emph{depth--transferability Pareto frontier}: deeper layers yield higher English probe AUROC but degrade in zero-shot cross-lingual transfer (Spearman $\rho=-0.78$/$-0.73$).
30	The frontier shape is architecture-dependent, with the optimal transfer depth at 60\% for Qwen3 versus 50\% for Scout.
31	We decompose correctness transfer into difficulty-shared and capability-specific components, showing that removing the difficulty direction improves transfer by 3.1~pp (median), with low-resource languages benefiting most (+4.1~pp).
32	We propose CaCLR, a probe training objective combining binary cross-entropy, sample-binned ECE, and an MMD-based cross-lingual consistency loss on parallel activations.
33	CaCLR-trained probes reduce non-English ECE by 3.5\% over temperature scaling with zero target-language labels, matching few-shot (100-label) supervised performance.
34	CKA analysis reveals that cross-lingual representation similarity monotonically decreases with depth ($r=0.82$ with transfer AUROC), mechanistically explaining the Pareto frontier.
35	Finally, we confirm that correctness--confidence orthogonality (cosine $<0.062$) persists universally across all 20 languages, bounding output-based calibration regardless of language.
36	\end{abstract}
37	
38	%---------------------------------------------------------------
39	\section{Introduction}
40	\label{sec:intro}
41	%---------------------------------------------------------------
42	
43	Calibration---the alignment between a model's expressed confidence and its actual accuracy---is critical for deploying language models in high-stakes settings.
44	Recent work has shown that multilingual LLMs suffer from substantially worse calibration in non-English languages, with expected calibration error (ECE) up to 5$\times$ higher than English \cite{}.
45	Output-based calibration methods such as temperature scaling \cite{guo2017calibration} and verbalized confidence extraction \cite{} offer post-hoc corrections but face a structural limitation:
46	\citet{} demonstrated that the internal \emph{correctness direction} (encoding whether the model will answer correctly) is nearly orthogonal to the \emph{confidence direction} (encoding verbalized confidence), with cosine similarity below 0.04 in English.
47	This orthogonality means output-based signals are fundamentally uninformative about actual correctness.
48	
49	Probe-based calibration methods---training linear classifiers on internal representations to predict correctness---offer a principled alternative by directly accessing the correctness direction \cite{}.
50	However, all existing probe-based methods (CORAL, CCPS, Confidence Manifold, correctness steering) operate exclusively in English.
51	The question of whether correctness probes transfer cross-lingually---enabling calibration in languages without correctness labels---remains open.
52	
53	We present the first systematic study of cross-lingual correctness probe transfer.
54	Our contributions form a causal chain:
55	
56	\paragraph{(1) Pareto Frontier Discovery.}
57	We reveal a depth--transferability Pareto frontier: deeper layers produce better English probes (AUROC up to 0.838) but degrade in zero-shot cross-lingual transfer.
58	The frontier shape is architecture-dependent---optimal transfer depth is 60\% for Qwen3-235B versus 50\% for Llama~4~Scout---with MoE expert routing accelerating deep-layer language specialization.
59	
60	\paragraph{(2) Difficulty--Capability Decomposition.}
61	We decompose the correctness signal into a difficulty-shared component (language-agnostic, transferable) and a capability-specific component (language-dependent, driving deep-layer degradation).
62	Removing the difficulty direction improves cross-lingual transfer by 3.1~pp median, with low-resource languages benefiting most (+4.1~pp).
63	
64	\paragraph{(3) CaCLR: Calibration-Consistent Cross-Lingual Regularization.}
65	We propose CaCLR, a probe training objective that jointly optimizes correctness prediction ($\mathcal{L}_\text{BCE}$), calibration ($\alpha \cdot \mathcal{L}_\text{SB-ECE}$), and cross-lingual distributional alignment ($\beta \cdot \mathcal{L}_\text{MMD}$) using parallel activations from translated items.
66	CaCLR requires zero target-language correctness labels and reduces non-English ECE by 3.5\% over temperature scaling across 20 languages.
67	
68	\paragraph{(4) Cross-Lingual Orthogonality.}
69	We confirm that correctness--confidence orthogonality persists across all 20 languages and both architectures (max cosine = 0.062), establishing that output-based calibration is structurally limited regardless of language.
70	
71	CKA representation similarity analysis provides the mechanistic glue: cross-lingual CKA monotonically decreases with depth ($r=0.82$ with transfer AUROC), explaining why deeper layers degrade and why CaCLR's distributional matching is most effective at mid-depth layers where misalignment is distributional rather than geometric.
72	
73	
74	%---------------------------------------------------------------
75	\section{Related Work}
76	\label{sec:related}
77	%---------------------------------------------------------------
78	
79	\paragraph{LLM Calibration.}
80	Temperature scaling \cite{guo2017calibration} remains the dominant post-hoc calibration method.
81	Recent work reveals that multilingual LLMs are substantially worse-calibrated in non-English languages.
82	LACE proposes per-language layer ensembles but requires target-language labels.
83	MKA uses multi-agent knowledge aggregation at 5$\times$ inference cost.
84	
85	\paragraph{Probe-Based Calibration.}
86	CORAL trains cross-task English correctness probes and identifies distribution-shift challenges.
87	CCPS uses clustering on correctness probe activations.
88	Miao \& Ungar discover correctness--confidence orthogonality and propose steering-based calibration, but only for English on 7--8B models.
89	All probe-based methods remain monolingual.
90	
91	\paragraph{Cross-Lingual Probe Transfer.}
92	Xiao et al.\ transfer \emph{knowledge boundary} probes (input-level answerability) across 8 languages.
93	Knowledge boundary is fundamentally different from correctness: answerability is an input property (does the model have relevant knowledge?) while correctness is output-dependent (will the model produce the right answer for this input?).
94	Their success with mean-shift alignment is not expected to transfer to correctness probes, and we formally prove why (Section~\ref{sec:method:transfer}).
95	Civelli et al.\ study cross-lingual \emph{difficulty} probes, which we use as a control in our decomposition analysis.
96	
97	\paragraph{Domain Adaptation Theory.}
98	Ben-David et al.'s $\mathcal{H}$-divergence framework predicts that cross-domain transfer degrades with increasing domain divergence.
99	We derive predictions from this framework and test them: the resource-tier gradient follows theory, but the architecture-dependent Pareto shape and difficulty--capability entanglement are novel findings.
100	
101	\paragraph{Representation Similarity.}
102	CKA \cite{kornblith2019similarity} measures representational similarity between network layers.
103	We use CKA to mechanistically explain the Pareto frontier by quantifying cross-lingual representation divergence at each depth.
104	
105	\paragraph{Cross-Lingual Alignment.}
106	Linear cross-lingual alignment methods (MUSE, VecMap) learn rotation matrices between embedding spaces.
107	Our linear projection baseline is conceptually similar; CaCLR's distributional matching via MMD represents the alternative alignment paradigm.
108	
109	\paragraph{Conformal Prediction.}
110	Distribution-free conformal prediction provides coverage guarantees but requires calibration data per language.
111	Our approach targets zero-label transfer, making the two complementary.
112	
113	
114	%---------------------------------------------------------------
115	\section{Method}
116	\label{sec:method}
117	%---------------------------------------------------------------
118	
119	\subsection{Correctness Probes}
120	\label{sec:method:probes}
121	
122	Given a multilingual LLM with $L$ layers, we extract the hidden representation $\mathbf{h}_\ell \in \mathbb{R}^d$ at layer $\ell$ for each input.
123	A correctness probe $f_\ell: \mathbb{R}^d \to [0,1]$ is a logistic regression classifier trained on English data to predict whether the model's generated answer is correct:
124	\begin{equation}
125	    f_\ell(\mathbf{h}) = \sigma(\mathbf{w}_\ell^\top \mathbf{h} + b_\ell)
126	\end{equation}
127	where $\mathbf{w}_\ell \in \mathbb{R}^d$ defines the \emph{correctness direction} at layer $\ell$.
128	We evaluate probes via AUROC (discrimination) and ECE (calibration).
129	
130	\subsection{Cross-Lingual Transfer}
131	\label{sec:method:transfer}
132	
133	We apply English-trained probes directly to target-language representations (zero-shot transfer).
134	We also evaluate several alignment strategies:
135	
136	\paragraph{Mean-Shift.}
137	Subtract the English mean and add the target-language mean of representations.
138	Under StandardScaler preprocessing + logistic regression, mean-shift adds a constant offset to all logits.
139	Since AUROC is rank-invariant, $\Delta\text{AUROC} \equiv 0$ mathematically---mean-shift cannot improve discrimination under this pipeline.
140	
141	\paragraph{Linear Projection.}
142	Learn a linear map $\mathbf{A} \in \mathbb{R}^{d \times d}$ from parallel English--target representation pairs to align the target-language representations to the English correctness subspace.
143	
144	\paragraph{Few-Shot.}
145	Fine-tune probes with 25 or 100 labeled target-language examples.
146	
147	\subsection{CaCLR: Calibration-Consistent Cross-Lingual Regularization}
148	\label{sec:method:caclr}
149	
150	CaCLR trains correctness probes with a composite loss:
151	\begin{equation}
152	    \mathcal{L}_\text{CaCLR} = \mathcal{L}_\text{BCE} + \alpha \cdot \mathcal{L}_\text{SB-ECE} + \beta \cdot \mathcal{L}_\text{MMD}
153	\end{equation}
154	
155	\noindent where:
156	\begin{itemize}[nosep,leftmargin=*]
157	    \item $\mathcal{L}_\text{BCE}$: binary cross-entropy on English correctness labels.
158	    \item $\mathcal{L}_\text{SB-ECE}$: sample-binned ECE, a differentiable calibration loss.
159	    \item $\mathcal{L}_\text{MMD}$: maximum mean discrepancy between English and target-language \emph{probe activations} on parallel inputs (GlobalMMLU train-split translations). This encourages the probe to produce similar output distributions for semantically equivalent inputs across languages.
160	\end{itemize}
161	
162	The MMD term aligns distributional properties (mean, covariance) of probe activations without requiring target-language correctness labels---only parallel inputs.
163	We set $\alpha=1.0$ and $\beta=0.1$ based on hyperparameter sweeps (Section~\ref{sec:exp:caclr}).
164	
165	\subsection{Difficulty--Capability Decomposition}
166	\label{sec:method:decomp}
167	
168	We hypothesize that the correctness signal mixes two components:
169	(1)~a \emph{difficulty-shared} component reflecting item difficulty (language-agnostic), and
170	(2)~a \emph{capability-specific} component reflecting the model's language-specific ability (drives deep-layer transfer degradation).
171	
172	We operationalize this via IRT difficulty probes: train a probe to predict item difficulty (from IRT parameters), extract the difficulty direction $\mathbf{d}_\ell$, project it out of representations, and retrain correctness probes on the residual.
173	Improved transfer on residual representations confirms that difficulty entanglement degrades cross-lingual transfer.
174	A random-direction control validates that the improvement is specific to difficulty removal, not arbitrary dimensionality reduction.
175	
176	%---------------------------------------------------------------
177	\section{Experimental Setup}
178	\label{sec:setup}
179	%---------------------------------------------------------------
180	
181	\paragraph{Models.}
182	Qwen3-235B-A22B (94 layers, MoE, INT8) and Llama~4~Scout (48 layers, MoE, INT8).
183	We probe every 4th layer: 24 layers for Qwen3, 12 for Scout.
184	
185	\paragraph{Languages.}
186	20 languages spanning three resource tiers: HIGH (en, zh, es, fr, de), MID (hi, ru, ko, tr, and 5 others), LOW (sw, bn, and 8 others).
187	
188	\paragraph{Benchmarks.}
189	Primary: GlobalMMLU (multilingual MCQA).
190	Generalization: Belebele (reading comprehension), MMLU-ProX (knowledge QA).
191	
192	\paragraph{Probes.}
193	Logistic regression with StandardScaler preprocessing.
194	We validate this choice against 2-layer MLPs (Section~\ref{sec:exp:probe}).
195	
196	\paragraph{Evaluation.}
197	AUROC for discrimination, ECE for calibration.
198	All comparisons include bootstrap CIs (1000 resamples) and paired permutation tests.
199	Effect sizes reported with Cohen's $d$.
200	
201	\paragraph{Transfer Conditions.}
202	Zero-shot, mean-shift, linear projection (50 parallel pairs), few-shot (25/100 labels), and CaCLR.
203	
204	%---------------------------------------------------------------
205	\section{Results}
206	\label{sec:results}
207	%---------------------------------------------------------------
208	
209	\subsection{Pareto Frontier Discovery}
210	\label{sec:exp:pareto}
211	
212	\begin{table}[t]
213	\centering
214	\small
215	\begin{tabular}{@{}lccccc@{}}
216	\toprule
217	\textbf{Layer} & \textbf{Depth} & \textbf{EN} & \textbf{ZS Med.} & \textbf{ZS Min} & \textbf{ZS Max} \\
218	\midrule
219	\multicolumn{6}{l}{\emph{Qwen3-235B-A22B (94 layers)}} \\
220	\midrule
221	16 & 17\% & .672 & .659 & .589 & .678 \\
222	32 & 34\% & .738 & .729 & .648 & .751 \\
223	48 & 51\% & .781 & .771 & .658 & .793 \\
224	\textbf{56} & \textbf{60\%} & \textbf{.798} & \textbf{.771} & \textbf{.641} & \textbf{.801} \\
225	64 & 68\% & .816 & .751 & .618 & .788 \\
226	76 & 81\% & .838 & .714 & .584 & .756 \\
227	88 & 94\% & .818 & .671 & .542 & .712 \\
228	\midrule
229	\multicolumn{6}{l}{\emph{Llama 4 Scout (48 layers)}} \\
230	\midrule
231	8  & 17\% & .674 & .661 & --- & --- \\
232	16 & 33\% & .741 & .738 & --- & --- \\
233	\textbf{24} & \textbf{50\%} & \textbf{.788} & \textbf{.756} & --- & --- \\
234	32 & 67\% & .811 & .726 & --- & --- \\
235	40 & 83\% & .821 & .698 & --- & --- \\
236	48 & 100\% & .798 & .654 & --- & --- \\
237	\bottomrule
238	\end{tabular}
239	\caption{Pareto frontier across depth for both architectures. Bold rows indicate the optimal zero-shot transfer layer. EN = English AUROC; ZS = zero-shot transfer AUROC (median across 20 languages). Beyond the optimal transfer layer, EN AUROC continues rising while cross-lingual transfer degrades.}
240	\label{tab:pareto}
241	\end{table}
242	
243	Table~\ref{tab:pareto} presents the depth--transferability Pareto frontier on both architectures.
244	On Qwen3-235B, English AUROC peaks at 0.838 (layer~76, 81\% depth), while the optimal zero-shot transfer layer is layer~56 (60\% depth) with median AUROC 0.771 across 20 languages.
245	Moving from the transfer-optimal layer~56 to the English-optimal layer~76, zero-shot transfer drops from 0.771 to 0.714 ($-5.7$~pp) while English AUROC gains only 4.0~pp.
246	The depth--transfer anticorrelation is robust: Spearman $\rho = -0.78$ (per-language median; IQR $[-0.84, -0.71]$).
247	
248	On Llama~4~Scout, the optimal transfer depth shifts to 50\% (layer~24), with a steeper frontier ($\rho = -0.73$).
249	Scout's shallower optimal depth is consistent with MoE expert routing driving faster language specialization in its 48-layer architecture.
250	17/20 languages achieve zero-shot AUROC $> 0.65$ on Qwen3 (16/20 on Scout).
251	
252	The resource tier strongly modulates transfer quality.
253	On Qwen3 at the optimal layer, high-resource languages (zh: 0.793, es: 0.801) substantially outperform low-resource languages (sw: 0.641, bn: 0.633), consistent with $\mathcal{H}$-divergence predictions from domain adaptation theory.
254	
255	\subsection{CaCLR Evaluation}
256	\label{sec:exp:caclr}
257	
258	\begin{table}[t]
259	\centering
260	\small
261	\begin{tabular}{@{}lccccc@{}}
262	\toprule
263	\textbf{Method} & \textbf{Labels} & \textbf{Q-56} & \textbf{Q-76} & \textbf{S-24} & \textbf{S-40} \\
264	\midrule
265	Zero-shot & 0 & .771 & .714 & .756 & .698 \\
266	Mean-shift & 0 & .771 & .714 & .756 & .698 \\
267	CaCLR$_{\alpha}$ & 0$^*$ & .798 & .762 & .784 & .745 \\
268	\textbf{CaCLR} & \textbf{0$^*$} & \textbf{.828} & \textbf{.788} & \textbf{.812} & \textbf{.771} \\
269	Lin.\ proj.\ (50) & 50 pairs & .812 & .779 & .798 & .758 \\
270	Few-shot 25 & 25 & .798 & .761 & .781 & .741 \\
271	Few-shot 100 & 100 & .821 & .792 & .808 & .778 \\
272	\bottomrule
273	\end{tabular}
274	\caption{Transfer method comparison (median AUROC across 20 languages). Q = Qwen3-235B; S = Llama~4~Scout. Numbers after model indicate layer. $^*$Requires parallel inputs but zero target-language correctness labels. CaCLR$_\alpha$ = $\beta=0$ (no consistency loss).}
275	\label{tab:transfer}
276	\end{table}
277	
278	Table~\ref{tab:transfer} compares all transfer methods.
279	CaCLR achieves median AUROC 0.828 at Qwen3 layer~56 and 0.812 at Scout layer~24---surpassing linear projection by +1.4~pp and nearly matching few-shot 100 ($-0.8$~pp), while requiring zero target-language labels.
280	Mean-shift yields exactly $\Delta\text{AUROC} = 0.000$, confirming our theoretical prediction (Section~\ref{sec:method:transfer}).
281	
282	The $\beta$ term (MMD consistency loss) provides a meaningful gain of +3.2~pp over the $\alpha$-only ablation (bootstrap CI: [0.019, 0.045]; paired permutation $p = 0.003$; Cohen's $d = 0.48$).
283	Table~\ref{tab:beta} shows the $\beta$ sensitivity sweep: $\beta = 0.1$ is optimal, with lower values providing insufficient distributional constraint and $\beta = 1.0$ over-regularizing.
284	
285	\begin{table}[t]
286	\centering
287	\small
288	\begin{tabular}{@{}lccc@{}}
289	\toprule
290	$\beta$ & $\Delta$AUROC & $\Delta$ECE & Note \\
291	\midrule
292	0.001 & +0.008 & $-$0.003 & Negligible \\
293	0.01  & +0.019 & $-$0.008 & Marginal \\
294	\textbf{0.1} & \textbf{+0.032} & $\mathbf{-}$\textbf{0.014} & \textbf{Optimal} \\
295	1.0   & +0.021 & $-$0.011 & Over-regularized \\
296	\bottomrule
297	\end{tabular}
298	\caption{$\beta$ sensitivity sweep (Qwen3-235B, layer~56, median across 20 languages). Deltas are relative to $\alpha$-only ($\beta=0$).}
299	\label{tab:beta}
300	\end{table}
301	
302	The $\beta$ gain is largest at mid-depth layers (+4.1~pp) and diminishes at deep layers (+2.4~pp) and shallow layers (+1.8~pp).
303	This pattern is explained by CKA analysis (Section~\ref{sec:exp:cka}): mid-depth layers have sufficient cross-lingual structure for MMD alignment to be effective, while deep-layer misalignment is geometric (directional rotation) rather than merely distributional.
304	
305	CaCLR reduces non-English ECE by a median of 3.5\% over temperature scaling (range: [1.2\%, 6.1\%]).
306	Temperature scaling achieves English ECE of 0.048 (Qwen3) and 0.053 (Scout) from raw ECE of 0.162 and 0.171 respectively, but cannot address cross-lingual representation misalignment.
307	CaCLR directly optimizes calibration during training via the SB-ECE term.
308	
309	\subsection{Difficulty--Capability Decomposition}
310	\label{sec:exp:decomp}
311	
312	\begin{table}[t]
313	\centering
314	\small
315	\begin{tabular}{@{}lcccc@{}}
316	\toprule
317	\textbf{Depth} & \textbf{HIGH} & \textbf{MID} & \textbf{LOW} & \textbf{Random} \\
318	\midrule
319	20\% & +.012 & +.014 & +.019 & +.001 \\
320	35\% & +.016 & +.022 & +.028 & +.002 \\
321	50\% & +.021 & +.031 & +.038 & +.002 \\
322	60\% & +.024 & +.036 & +.043 & +.003 \\
323	80\% & +.028 & +.041 & +.048 & +.003 \\
324	90\% & +.022 & +.034 & +.041 & +.002 \\
325	\bottomrule
326	\end{tabular}
327	\caption{$\Delta$AUROC after difficulty direction removal, by resource tier and depth. Random = random direction control. Difficulty removal consistently improves transfer, especially for low-resource languages at deep layers.}
328	\label{tab:decomp}
329	\end{table}
330	
331	Table~\ref{tab:decomp} shows the decomposition results.
332	Removing the difficulty direction from representations before training correctness probes improves cross-lingual transfer by a median of 3.1~pp (bootstrap CI: [1.8, 4.4]; $p = 0.006$; $d = 0.41$).
333	The difficulty direction has moderate cosine similarity with the correctness direction (0.34), confirming partial signal overlap without full redundancy.
334	The difficulty probe achieves $R^2 = 0.68$, validating that difficulty is linearly accessible in the representation space.
335	
336	Two patterns emerge.
337	First, a resource-tier gradient: low-resource languages benefit most from decomposition (+4.1~pp) versus high-resource (+2.2~pp), because low-resource languages have greater difficulty distribution mismatch with English.
338	Second, a depth gradient: deep-layer benefit (4.8~pp at 80\% depth) exceeds shallow-layer benefit (0.8~pp at 20\%), because deep layers encode more language-specific difficulty information.
339	The random-direction control yields only +0.2~pp, ruling out dimensionality reduction as a confound.
340	
341	\subsection{Cross-Lingual Orthogonality}
342	\label{sec:exp:ortho}
343	
344	\begin{table}[t]
345	\centering
346	\small
347	\begin{tabular}{@{}llccc@{}}
348	\toprule
349	\textbf{Lang} & \textbf{Tier} & \textbf{Qwen3} & \textbf{Scout} & \textbf{Mean} \\
350	\midrule
351	en & HIGH & .031 & .037 & .034 \\
352	zh & HIGH & .035 & .041 & .038 \\
353	es & HIGH & .033 & .039 & .036 \\
354	de & HIGH & .036 & .042 & .039 \\
355	hi & MID  & .039 & .045 & .042 \\
356	ru & MID  & .037 & .043 & .040 \\
357	ko & MID  & .041 & .047 & .044 \\
358	tr & MID  & .043 & .049 & .046 \\
359	sw & LOW  & .048 & .056 & .052 \\
360	bn & LOW  & .052 & .058 & .055 \\
361	\bottomrule
362	\end{tabular}
363	\caption{Correctness--confidence cosine similarity across languages and architectures. All values remain below 0.062, confirming universal near-orthogonality.}
364	\label{tab:ortho}
365	\end{table}
366	
367	Table~\ref{tab:ortho} reports correctness--confidence cosine similarity across languages.
368	All 20 languages on both architectures show cosine similarity below 0.062 (mean = 0.042; bootstrap CI for mean: [0.035, 0.049]).
369	This extends the English-only finding of Miao \& Ungar to a universal structural property: verbalized confidence is uninformative about correctness regardless of language or architecture.
370	
371	A mild resource-tier gradient exists: low-resource languages show slightly higher cosine (0.051 vs.\ 0.038 for high-resource), likely reflecting noisier confidence direction estimates from sparser training data rather than genuine reduction in orthogonality.
372	Qwen3 exhibits slightly stronger orthogonality than Scout (mean 0.039 vs.\ 0.046), possibly because its larger capacity encodes correctness and confidence in more separable subspaces.
373	
374	\subsection{CKA Representation Similarity Analysis}
375	\label{sec:exp:cka}
376	
377	\begin{table}[t]
378	\centering
379	\small
380	\begin{tabular}{@{}lcccc@{}}
381	\toprule
382	\textbf{Depth} & \textbf{HIGH} & \textbf{MID} & \textbf{LOW} & \textbf{ZS AUROC} \\
383	\midrule
384	10\% & .93 & .89 & .84 & .618 \\
385	25\% & .90 & .85 & .78 & .698 \\
386	40\% & .86 & .79 & .69 & .756 \\
387	50\% & .82 & .74 & .62 & .771 \\
388	60\% & .78 & .69 & .55 & .771 \\
389	70\% & .73 & .63 & .47 & .741 \\
390	80\% & .67 & .56 & .41 & .714 \\
391	90\% & .61 & .49 & .35 & .688 \\
392	\bottomrule
393	\end{tabular}
394	\caption{CKA similarity (EN vs.\ target, Qwen3-235B) by depth and resource tier, alongside zero-shot transfer AUROC. CKA monotonically decreases with depth and correlates strongly with transfer success.}
395	\label{tab:cka}
396	\end{table}
397	
398	Table~\ref{tab:cka} presents CKA similarity between English and target-language representations across depth.
399	CKA monotonically decreases with depth across all resource tiers, and correlates strongly with zero-shot transfer AUROC (Pearson $r = 0.82$; CI: [0.76, 0.87]; Spearman $\rho = 0.79$).
400	This provides a mechanistic explanation for the Pareto frontier: deeper layers have progressively less cross-lingual representational overlap, directly causing transfer degradation.
401	
402	The resource-tier gradient in CKA mirrors the transfer gradient: high-resource languages maintain CKA $\geq 0.61$ even at 90\% depth, while low-resource languages drop to 0.35.
403	This reflects pretraining data overlap---languages with more shared tokens develop more similar deep representations.
404	
405	Critically, the CKA analysis reveals why CaCLR's $\beta$ term has depth-dependent effectiveness.
406	At layers where CKA $< 0.55$, the $\beta$ term provides diminishing returns because misalignment becomes \emph{geometric} (the correctness direction rotates 15--35$^\circ$ across languages) rather than merely distributional (mean/covariance shift).
407	MMD corrects distributional shift but cannot learn rotations; this explains why linear projection---which explicitly learns a rotation matrix---remains effective at deep layers.
408	At mid-depth layers (CKA $\approx 0.62$--$0.78$), misalignment is primarily distributional, and CaCLR's MMD term effectively closes the gap.
409	
410	\subsection{Probe Complexity}
411	\label{sec:exp:probe}
412	
413	\begin{table}[t]
414	\centering
415	\small
416	\begin{tabular}{@{}lcccc@{}}
417	\toprule
418	\textbf{Layer} & \textbf{LR-EN} & \textbf{MLP-EN} & \textbf{LR-ZS} & \textbf{MLP-ZS} \\
419	\midrule
420	24 & .711 & .722 & .698 & .691 \\
421	40 & .762 & .778 & .756 & .741 \\
422	56 & .798 & .814 & .771 & .752 \\
423	76 & .838 & .852 & .714 & .686 \\
424	\bottomrule
425	\end{tabular}
426	\caption{Logistic regression (LR) vs.\ 2-layer MLP on Qwen3-235B. MLP achieves higher English AUROC but worse zero-shot transfer, with the gap widening at deeper layers.}
427	\label{tab:probe}
428	\end{table}
429	
430	Table~\ref{tab:probe} compares logistic regression and 2-layer MLP probes.
431	MLPs achieve +1.4~pp higher English AUROC but suffer 3.6~pp worse zero-shot transfer degradation (median), yielding a net transfer advantage of +2.2~pp for logistic regression.
432	The gap widens at deeper layers (LR advantage: +0.7~pp at layer~24 vs.\ +2.8~pp at layer~76), because deep-layer representations are more language-specific and MLP's extra capacity overfits to English-specific patterns.
433	Logistic regression's linear inductive bias matches the linear structure of correctness directions, supporting its use as the default probe.
434	
435	\subsection{Cross-Benchmark Generalization}
436	\label{sec:exp:benchmark}
437	
438	\begin{table}[t]
439	\centering
440	\small
441	\begin{tabular}{@{}lcccc@{}}
442	\toprule
443	\textbf{Benchmark} & \textbf{ZS} & \textbf{CaCLR} & $\rho$ & \textbf{$>$0.65} \\
444	\midrule
445	GlobalMMLU & .758 & .808 & $-$.78 & 17/20 \\
446	Belebele & .731 & .789 & $-$.71 & 15/20 \\
447	MMLU-ProX & .748 & .801 & $-$.75 & 16/20 \\
448	\bottomrule
449	\end{tabular}
450	\caption{Cross-benchmark generalization (Qwen3-235B, optimal transfer layer). ZS = zero-shot median AUROC; $\rho$ = Pareto Spearman correlation; $>$0.65 = languages above 0.65 AUROC.}
451	\label{tab:benchmark}
452	\end{table}
453	
454	Table~\ref{tab:benchmark} shows that all findings generalize across benchmarks.
455	The Pareto frontier persists on Belebele ($\rho = -0.71$) and MMLU-ProX ($\rho = -0.75$).
456	CaCLR provides consistent improvement on both (+5.8~pp on Belebele, +5.3~pp on MMLU-ProX).
457	Cross-benchmark per-language correlation is 0.92, indicating that transfer difficulty is language-inherent rather than benchmark-specific.
458	
459	\subsection{Linear Projection Data Efficiency}
460	\label{sec:exp:linproj}
461	
462	\begin{table}[t]
463	\centering
464	\small
465	\begin{tabular}{@{}lccccc@{}}
466	\toprule
467	\textbf{Pairs} & \textbf{Med.} & $\Delta$\textbf{ZS} & \textbf{\%200} & \textbf{HIGH} & \textbf{LOW} \\
468	\midrule
469	10  & .762 & +.027 & 88\% & .781 & .638 \\
470	20  & .778 & +.043 & 94\% & .798 & .651 \\
471	50  & .792 & +.057 & 98\% & .814 & .664 \\
472	100 & .796 & +.061 & 99\% & .818 & .668 \\
473	200 & .798 & +.063 & 100\% & .821 & .671 \\
474	\bottomrule
475	\end{tabular}
476	\caption{Linear projection data efficiency. Performance saturates at $\sim$35 pairs (95\% of 200-pair performance), with low-resource languages requiring slightly more pairs (48 vs.\ 22 for high-resource).}
477	\label{tab:linproj}
478	\end{table}
479	
480	Linear projection saturates rapidly: 50 parallel pairs achieve 98\% of 200-pair performance (Table~\ref{tab:linproj}).
481	This reflects the low intrinsic dimensionality of the correctness direction---a rotation/scaling matrix between low-dimensional subspaces needs few examples to estimate.
482	Low-resource languages saturate later (48 vs.\ 22 pairs), consistent with noisier correctness direction estimates.
483	CaCLR outperforms 50-pair linear projection by +1.4~pp while requiring no paired data beyond parallel inputs.
484	
485	
486	%---------------------------------------------------------------
487	\section{Discussion}
488	\label{sec:discussion}
489	%---------------------------------------------------------------
490	
491	\paragraph{Why architecture matters.}
492	The architecture-dependent Pareto shape is not predicted by domain adaptation theory alone.
493	MoE models exhibit sharper frontiers because expert routing creates discrete language specialization at depth: specific experts become ``responsible'' for specific languages, accelerating representational divergence.
494	Dense models (Gemma~4~31B; Appendix~\ref{app:gemma}) show smoother frontiers ($\rho = -0.69$, optimal transfer at 75\% depth), confirming that expert routing is the mechanism.
495	
496	\paragraph{When CaCLR works and when it does not.}
497	CaCLR is most effective at mid-depth layers where cross-lingual misalignment is distributional.
498	At deep layers (CKA $< 0.55$), geometric misalignment dominates and linear projection is preferable.
499	This provides a practical guideline: use CKA to predict which layer--language combinations will benefit from CaCLR versus requiring geometric alignment.
500	
501	\paragraph{The role of resource tier.}
502	Low-resource languages consistently show (1)~lower zero-shot transfer, (2)~greater benefit from difficulty decomposition, (3)~greater benefit from CaCLR, and (4)~slightly weaker orthogonality.
503	All patterns are consistent with sparser pretraining representation creating larger distributional gaps that alignment methods can partially close.
504	
505	\paragraph{Limitations.}
506	Our evaluation uses MCQA benchmarks, which enable clean correctness labeling but may not reflect open-ended generation.
507	CaCLR requires parallel inputs (translated items), which are readily available for MCQA but less natural for other tasks.
508	INT8 quantization introduces small but nonzero perturbations (max $\Delta$AUROC = 0.6~pp; Appendix~\ref{app:int8}).
509	
510	%---------------------------------------------------------------
511	\section{Conclusion}
512	\label{sec:conclusion}
513	%---------------------------------------------------------------
514	
515	We presented the first systematic study of cross-lingual correctness probe transfer.
516	Our findings form a coherent causal chain: (1)~a depth--transferability Pareto frontier exists with architecture-dependent shape; (2)~difficulty--capability decomposition explains the frontier and identifies where alignment is needed; (3)~CaCLR shifts the frontier via distributional alignment, reducing non-English ECE by 3.5\% over temperature scaling with zero target-language labels across 20 languages; (4)~correctness--confidence orthogonality universally bounds output-based calibration.
517	CKA analysis provides the mechanistic glue, linking representation geometry to transfer success and explaining CaCLR's depth-dependent effectiveness.
518	These results establish probe-based calibration as viable for multilingual settings and provide actionable guidelines for practitioners: select layers based on the architecture-specific Pareto frontier, apply CaCLR at mid-depth layers, and use linear projection when geometric misalignment dominates.
519	
520	%---------------------------------------------------------------
521	
522	\appendix
523	
524	\section{INT8 Validation}
525	\label{app:int8}
526	
527	\begin{table}[h]
528	\centering
529	\small
530	\begin{tabular}{@{}lcccc@{}}
531	\toprule
532	\textbf{Layer} & \textbf{INT8} & \textbf{FP16} & $\Delta$ & \textbf{Cos.} \\
533	\midrule
534	8  & .674 & .678 & $-$.004 & .991 \\
535	16 & .741 & .745 & $-$.004 & .989 \\
536	24 & .788 & .791 & $-$.003 & .992 \\
537	32 & .811 & .814 & $-$.003 & .990 \\
538	40 & .821 & .827 & $-$.006 & .987 \\
539	\bottomrule
540	\end{tabular}
541	\caption{INT8 vs.\ FP16 on Llama~4~Scout. Cos.\ = cosine similarity between extracted correctness directions. All differences are within bootstrap noise.}
542	\label{tab:int8}
543	\end{table}
544	
545	INT8 quantization has negligible impact on correctness probes (Table~\ref{tab:int8}).
546	Maximum AUROC difference is 0.6~pp (layer~40), and correctness direction cosine similarity exceeds 0.987 at all layers.
547	ECE differences are similarly small (max 0.8~pp).
548	
549	\section{Probing Control Tasks}
550	\label{app:control}
551	
552	\begin{table}[h]
553	\centering
554	\small
555	\begin{tabular}{@{}lcccc@{}}
556	\toprule
557	\textbf{Layer} & \textbf{EN Sel.} & \textbf{ZH Sel.} & \textbf{SW Sel.} & \textbf{Ctrl.} \\
558	\midrule
559	16 & .248 & .231 & .192 & .512 \\
560	32 & .281 & .268 & .218 & .519 \\
561	48 & .309 & .292 & .241 & .524 \\
562	56 & .318 & .301 & .248 & .521 \\
563	76 & .341 & .324 & .262 & .538 \\
564	\bottomrule
565	\end{tabular}
566	\caption{Selectivity (probe AUROC $-$ control AUROC) on Qwen3-235B. Ctrl.\ = control task AUROC (random labels). Minimum selectivity is 0.192, well above the 0.15 threshold.}
567	\label{tab:control}
568	\end{table}
569	
570	Following Hewitt \& Liang (2019), we validate probe selectivity with random-label control tasks (Table~\ref{tab:control}).
571	Control AUROC ranges from 0.502 to 0.538 (near chance).
572	Selectivity (probe AUROC minus control AUROC) has a median of 0.284 and minimum of 0.192, well above the 0.15 threshold.
573	This confirms that probes extract genuine correctness signals rather than exploiting high-dimensional capacity.
574	
575	\section{Three-Architecture Comparison}
576	\label{app:gemma}
577	
578	\begin{table}[h]
579	\centering
580	\small
581	\begin{tabular}{@{}llccccc@{}}
582	\toprule
583	\textbf{Model} & \textbf{Type} & \textbf{EN} & \textbf{ZS} & \textbf{Opt.\%} & $\rho$ \\
584	\midrule
585	Qwen3-235B & MoE & .838 & .758 & 60\% & $-$.78 \\
586	Llama 4 Scout & MoE & .821 & .742 & 50\% & $-$.73 \\
587	Gemma 4 31B & Dense & .809 & .738 & 75\% & $-$.69 \\
588	\bottomrule
589	\end{tabular}
590	\caption{Three-architecture comparison. Dense architecture (Gemma~4) shows a smoother frontier with deeper optimal transfer, consistent with expert routing driving sharper language specialization in MoE models.}
591	\label{tab:arch}
592	\end{table}
593	
594	Adding Gemma~4~31B Dense as a camera-ready extension confirms that MoE architectures produce sharper Pareto frontiers than dense models (Table~\ref{tab:arch}).
595	Gemma's optimal transfer depth is 75\% (vs.\ 60\% and 50\% for the MoE models), and its Pareto $\rho = -0.69$ indicates a smoother frontier with no sharp elbow, consistent with gradual rather than discrete language specialization.
596	
597	\section{Extended Language Coverage}
598	\label{app:extended}
599	
600	\begin{table}[h]
601	\centering
602	\small
603	\begin{tabular}{@{}lcccc@{}}
604	\toprule
605	\textbf{Tier} & $n$ & \textbf{ZS} & \textbf{CaCLR} & $\Delta$ \\
606	\midrule
607	HIGH & 12 & .786 & .828 & +.042 \\
608	MID & 18 & .741 & .798 & +.057 \\
609	LOW & 22 & .648 & .721 & +.073 \\
610	\bottomrule
611	\end{tabular}
612	\caption{Extended coverage (52 languages). CaCLR benefit increases with decreasing resource tier.}
613	\label{tab:extended}
614	\end{table}
615	
616	Expanding to 52 languages confirms all findings at scale (Table~\ref{tab:extended}).
617	CaCLR generalizes across the full language set, with low-resource languages benefiting most (+7.3~pp vs.\ +4.2~pp for high-resource).
618	38/52 languages (73\%) achieve zero-shot AUROC above 0.65; the Pareto frontier and CaCLR improvements remain robust.
619	
620	\bibliographystyle{plainnat}
621	\bibliography{references}
622	
623	\end{document}
624	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9d9b5ca-fb7e-4e0e-9a0f-23217c119bc2",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "153d6cf4-37ae-4629-b33f-aff24e4028ef",
  "sourceToolAssistantUUID": "d9d9b5ca-fb7e-4e0e-9a0f-23217c119bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T21:13:27.002Z_

Now let me read the other paper versions and supporting materials for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "153d6cf4-37ae-4629-b33f-aff24e4028ef",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWbVYLozXS44UbFkkKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72eb2b90-8d10-4f3a-9ac0-4347ab934c66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmS73Qo3biWrR8aQkZoo8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12852,
      "cache_read_input_tokens": 18766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12852,
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

_source line 19 · 2026-05-20T21:13:28.942Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PHD6pcAS76yWAPvsfGMf9D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72eb2b90-8d10-4f3a-9ac0-4347ab934c66",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWbVYLozXS44UbFkkKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "969c5462-6ba7-4774-9d23-8be84c9265db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmS73Qo3biWrR8aQkZoo8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12852,
      "cache_read_input_tokens": 18766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12852,
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

_source line 20 · 2026-05-20T21:13:29.262Z_

<details><summary>↩ Tool result · `toolu_01PHD6pcAS76yWAPvsfGMf9D`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{colortbl}
12	\usepackage{array}
13	\usepackage{tabularx}
14	\usepackage{enumitem}
15	\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}
16	\usepackage{natbib}
17	\bibliographystyle{plainnat}
18	
19	\definecolor{improved}{rgb}{0.85,0.95,0.85}
20	\definecolor{degraded}{rgb}{0.95,0.85,0.85}
21	
22	\title{Cross-Lingual Correctness Probes Reveal a Depth--Transferability\\Pareto Frontier: Distributional Matching Fails\\Where Linear Projection Succeeds}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	Probe-based calibration methods extract internal correctness signals from LLM representations, achieving strong results in English. Whether these signals transfer cross-lingually remains untested. We present the first systematic evaluation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B), 20+ languages, and 5 transfer methods. We discover a \emph{depth--transferability Pareto frontier}: deeper layers yield higher English calibration quality (AUROC up to 0.81) but degrade in cross-lingual zero-shot transfer (median Spearman $\rho = -0.52$ between English AUROC and transfer AUROC). CKA analysis reveals the mechanism---geometric misalignment between language subspaces increases with depth ($r = 0.58$ between CKA similarity and transfer AUROC, explaining 34\% of variance). We test CaCLR, a probe training objective augmenting BCE loss with MMD-based cross-lingual consistency, and show that the consistency term is \emph{inert} across three orders of magnitude ($\beta$ sweep: Cohen's $d = 0.08$, $p = 0.42$)---predicted by the geometric explanation, since MMD cannot correct representational rotations. In contrast, linear projection with as few as 50--100 parallel pairs achieves +3.5\,pp AUROC over zero-shot transfer, precisely because it learns the rotation that distributional matching cannot. Correctness--confidence orthogonality (cosine $< 0.10$) persists across all 20 languages, confirming that output-based calibration is structurally limited regardless of language. Our results establish that probe-based cross-lingual calibration is viable for the majority of languages at mid-depth layers, close the distributional-matching path with both empirical evidence and mechanistic explanation, and identify linear projection as the practical solution.
31	\end{abstract}
32	
33	%====================================================================
34	\section{Introduction}
35	\label{sec:intro}
36	
37	Large language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) degrading up to 5$\times$ compared to English \cite{ahuja2024globalmmlu,lai2024llmsurvey}. Recent work has shown that probe-based calibration---extracting internal correctness signals via linear probes on model representations---outperforms output-based methods in English \cite{miao2026coral,burns2023discovering}. A key finding by \citet{miao2026orthogonality} is that correctness and verbalized confidence directions are nearly orthogonal (cosine $< 0.04$) in English, establishing a structural limitation of output-based approaches. However, all existing probe-based calibration methods operate exclusively in English, leaving a fundamental question unanswered: \emph{do these internal correctness signals transfer across languages?}
38	
39	The answer is not obvious. Cross-lingual representation transfer has been studied extensively for tasks like NER and classification \cite{pires2019multilingual,conneau2020unsupervised}, but correctness probes target a fundamentally different signal---output-dependent accuracy rather than input-level features. \citet{xiao2025knowledgeboundary} transferred \emph{knowledge boundary} probes (input-level answerability) across 8 languages, but answerability and correctness are distinct signals with potentially different cross-lingual alignment properties.
40	
41	We present the first systematic evaluation of cross-lingual correctness probe transfer, contributing four findings organized as a causal chain:
42	
43	\paragraph{(1) Pareto Frontier.} We discover a depth--transferability tradeoff: deeper layers produce better English probes but transfer worse cross-lingually. The frontier shape is architecture-dependent (Spearman $\rho$ ranging from $-0.51$ to $-0.58$ across three architectures).
44	
45	\paragraph{(2) Mechanistic Explanation.} CKA analysis reveals that cross-lingual geometric similarity decreases with depth. The CKA--transfer correlation ($r = 0.58$) explains 34\% of transfer variance, substantially outpredicting distributional measures like MMD (6\%).
46	
47	\paragraph{(3) Principled Negative Result.} CaCLR, a probe training objective with MMD-based cross-lingual consistency loss, fails to shift the Pareto frontier ($d = 0.08$). This is \emph{predicted} by the geometric explanation: MMD matches marginal distributions but cannot correct the rotation of the correctness direction across language subspaces.
48	
49	\paragraph{(4) Constructive Alternative.} Linear projection with $\sim$50--100 parallel pairs achieves +3.5\,pp over zero-shot, succeeding precisely because it learns the rotation that MMD cannot. The correctness--confidence orthogonality persists across all 20 languages, confirming the structural necessity of probe-based approaches.
50	
51	We evaluate on GlobalMMLU \cite{ahuja2024globalmmlu}, Belebele \cite{bandarkar2023belebele}, and MMLU-ProX across 20 languages and 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense), with camera-ready extensions to 52 languages.
52	
53	%====================================================================
54	\section{Related Work}
55	\label{sec:related}
56	
57	\paragraph{Probe-Based Calibration.}
58	\citet{burns2023discovering} and \citet{li2024inference} demonstrated that linear probes on internal representations can identify model knowledge states. CORAL \cite{miao2026coral} extended this to cross-task English calibration. \citet{miao2026orthogonality} showed correctness--confidence orthogonality and used steering to improve calibration. All are English-only.
59	
60	\paragraph{Cross-Lingual Probe Transfer.}
61	\citet{xiao2025knowledgeboundary} transferred knowledge boundary probes across 8 languages, finding partial success. However, knowledge boundary (binary answerability) is an input-level property, while correctness depends on the model's actual output. \citet{civelli2024difficulty} transferred difficulty probes cross-lingually---difficulty is a shared confound we explicitly control for. LACE \cite{zhou2024lace} ensembles per-language probes but requires target-language labels.
62	
63	\paragraph{Cross-Lingual Alignment.}
64	MUSE \cite{conneau2018muse} and VecMap \cite{artetxe2018vecmap} achieve bilingual alignment with $\sim$50--100 dictionary entries via linear mappings. Our linear projection's sample efficiency is consistent with this literature. The novel finding is that distributional matching (MMD, the natural choice from domain adaptation theory \cite{bendavid2010theory}) fails for this specific alignment task.
65	
66	\paragraph{Representation Similarity.}
67	CKA \cite{kornblith2019similarity} measures geometric similarity between representations. We use CKA to explain \emph{why} transfer fails at depth---complementing prior work using CKA for layer-level analysis \cite{nguyen2021wide}.
68	
69	\paragraph{Conformal Prediction.}
70	Conformal methods \cite{angelopoulos2023conformal} provide distribution-free coverage guarantees but require calibration data per language. Our approach targets zero-label transfer; the two are complementary.
71	
72	%====================================================================
73	\section{Method}
74	\label{sec:method}
75	
76	\subsection{Correctness Probes}
77	\label{sec:probes}
78	
79	Given a multilingual MCQA dataset, we extract hidden representations $\mathbf{h}_\ell \in \mathbb{R}^d$ at layer $\ell$ for each question, taking the last-token representation before answer generation. We train a logistic regression probe $f_\ell(\mathbf{h}) = \sigma(\mathbf{w}_\ell^\top \mathbf{h} + b_\ell)$ on English data to predict binary correctness (whether the model's selected answer matches the gold label). We evaluate via AUROC and ECE.
80	
81	\paragraph{Cross-Lingual Transfer.}
82	We evaluate the English-trained probe on target-language representations without any adaptation (zero-shot transfer). We compare five transfer conditions:
83	
84	\begin{enumerate}[itemsep=1pt,parsep=0pt]
85	    \item \textbf{Zero-shot}: Direct application of the English probe.
86	    \item \textbf{Mean-shift}: Center target representations to match English mean.
87	    \item \textbf{Linear projection}: Learn an affine mapping $\mathbf{h}_{\text{tgt}} \mapsto \mathbf{W}\mathbf{h}_{\text{tgt}} + \mathbf{b}$ from parallel pairs.
88	    \item \textbf{Few-shot} (25/100): Train on small target-language labeled sets.
89	    \item \textbf{CaCLR}: Our proposed training objective (\S\ref{sec:caclr}).
90	\end{enumerate}
91	
92	\paragraph{Mean-Shift Rank Invariance.}
93	Under StandardScaler preprocessing and logistic regression, mean-shift adds a constant offset to all logits: $\mathbf{w}^\top (\mathbf{h} + \boldsymbol{\delta}) + b = \mathbf{w}^\top \mathbf{h} + (b + \mathbf{w}^\top \boldsymbol{\delta})$. Since AUROC depends only on ranking, $\Delta\text{AUROC} \equiv 0$ mathematically. Our experiments confirm this ($\Delta\text{AUROC} = 0.000$ across all conditions).
94	
95	\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}
96	\label{sec:caclr}
97	
98	CaCLR augments the standard probe training objective with two regularization terms:
99	\begin{equation}
100	\mathcal{L} = \mathcal{L}_{\text{BCE}} + \alpha \cdot \mathcal{L}_{\text{SB-ECE}} + \beta \cdot \mathcal{L}_{\text{consistency}}
101	\end{equation}
102	where $\mathcal{L}_{\text{SB-ECE}}$ is a differentiable smooth-binned ECE loss and $\mathcal{L}_{\text{consistency}}$ is an MMD-based term:
103	\begin{equation}
104	\mathcal{L}_{\text{consistency}} = \text{MMD}^2\big(\{f(\mathbf{h}_i^{\text{en}})\}, \{f(\mathbf{h}_i^{\text{tgt}})\}\big)
105	\end{equation}
106	computed over parallel activations from GlobalMMLU train-split translations. This requires parallel \emph{inputs} but zero target-language \emph{labels}.
107	
108	\subsection{Difficulty-Controlled Decomposition}
109	\label{sec:decomp}
110	
111	Following IRT-based difficulty estimation, we train a difficulty probe $g(\mathbf{h}) = \mathbf{v}^\top \mathbf{h} + c$ predicting item difficulty. We project out the difficulty direction: $\mathbf{h}^{\perp} = \mathbf{h} - (\mathbf{h}^\top \hat{\mathbf{v}})\hat{\mathbf{v}}$, then retrain correctness probes on residuals. Improvement after difficulty removal indicates the capability-specific component drives transfer degradation.
112	
113	\subsection{CKA Analysis}
114	\label{sec:cka}
115	
116	We compute linear CKA \cite{kornblith2019similarity} between English and target-language representations at each probed layer:
117	\begin{equation}
118	\text{CKA}(\mathbf{X}_{\text{en}}, \mathbf{X}_{\text{tgt}}) = \frac{\|\mathbf{X}_{\text{en}}^\top \mathbf{X}_{\text{tgt}}\|_F^2}{\|\mathbf{X}_{\text{en}}^\top \mathbf{X}_{\text{en}}\|_F \cdot \|\mathbf{X}_{\text{tgt}}^\top \mathbf{X}_{\text{tgt}}\|_F}
119	\end{equation}
120	CKA captures geometric similarity (rotation, scaling), while MMD captures distributional distance. We correlate both with transfer AUROC to determine which type of misalignment drives transfer failure.
121	
122	%====================================================================
123	\section{Experimental Setup}
124	\label{sec:setup}
125	
126	\paragraph{Models.}
127	We evaluate three architectures: Qwen3-235B-A22B (94 layers, MoE, INT8), Llama~4 Scout (48 layers, MoE, INT8), and Gemma~4 31B (60 layers, dense, FP16). INT8 quantization is validated against FP16 (Appendix~\ref{app:int8}).
128	
129	\paragraph{Languages.}
130	Core evaluation: 20 languages spanning 4 resource tiers and 8 language families (zh, es, fr, de, ar, hi, ru, ko, ja, pt, vi, tr, id, th, pl, uk, he, el, sw, bn). Camera-ready extension: 52 languages.
131	
132	\paragraph{Datasets.}
133	Primary: GlobalMMLU \cite{ahuja2024globalmmlu}. Generalization: Belebele \cite{bandarkar2023belebele} and MMLU-ProX. Train/test splits follow standard protocols; CaCLR parallel activations use train split only.
134	
135	\paragraph{Probing Layers.}
136	We probe 24 layers for Qwen3-235B (evenly spaced across 94 layers), 12 for Llama~4 Scout, and 15 for Gemma~4 31B.
137	
138	\paragraph{Evaluation Metrics.}
139	AUROC (primary, rank-based), ECE (secondary, calibration quality), paired permutation tests ($p < 0.05$), bootstrap 95\% CIs (1000 resamples), Cohen's $d$ for effect sizes.
140	
141	%====================================================================
142	\section{Results}
143	\label{sec:results}
144	
145	\subsection{Depth--Transferability Pareto Frontier}
146	\label{sec:pareto}
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Pareto frontier summary across three architectures. EN\textsubscript{best}: English optimal AUROC and layer. ZS\textsubscript{med}: median zero-shot transfer AUROC at the best transfer layer. $\rho$\textsubscript{med}: median per-language Spearman correlation between English AUROC and transfer AUROC. $\sigma_\rho$: standard deviation of per-language $\rho$.}
152	\label{tab:pareto_summary}
153	\begin{tabular}{lcccccc}
154	\toprule
155	\textbf{Architecture} & \textbf{EN\textsubscript{best}} & \textbf{Layer} & \textbf{ZS\textsubscript{med}} & \textbf{Xfer Layer} & \textbf{$\rho$\textsubscript{med}} & \textbf{$\sigma_\rho$} \\
156	\midrule
157	Qwen3-235B (MoE) & 0.81 & 72 & 0.70 & 48 & $-$0.51 & 0.16 \\
158	Llama 4 Scout (MoE) & 0.79 & 36 & 0.68 & 24 & $-$0.54 & 0.15 \\
159	Gemma 4 31B (Dense) & 0.80 & 45 & 0.69 & 33 & $-$0.58 & 0.12 \\
160	\bottomrule
161	\end{tabular}
162	\end{table}
163	
164	Table~\ref{tab:pareto_summary} presents the Pareto frontier across all three architectures. The key pattern is consistent: the English-optimal layer (72--76\% depth) is \emph{not} the transfer-optimal layer ($\sim$50\% depth) for most languages. The Spearman correlation between English AUROC and cross-lingual transfer AUROC is moderately negative across architectures ($\rho$ median $-0.51$ to $-0.58$), confirming the depth--transferability tradeoff.
165	
166	The architecture-dependent shape is visible in two contrasts. First, MoE models (Qwen3, Llama~4) show higher per-language $\rho$ variance ($\sigma_\rho = 0.15$--$0.16$) than the dense model (Gemma~4, $\sigma_\rho = 0.12$), reflecting MoE routing's heterogeneous effect on cross-lingual alignment. Second, the per-language $\rho$ range spans $[-0.82, -0.21]$ across models, with low-resource languages (sw: $\rho \approx -0.78$) showing stronger negative correlations than high-resource languages (zh: $\rho \approx -0.21$), indicating that representation divergence from English scales with both depth and pretraining exposure.
167	
168	\begin{table}[t]
169	\centering
170	\small
171	\caption{Zero-shot transfer AUROC at the best transfer layer for 20 languages on Qwen3-235B-A22B. Languages grouped by resource tier.}
172	\label{tab:zs_by_lang}
173	\begin{tabular}{llc|llc}
174	\toprule
175	\textbf{Lang} & \textbf{Tier} & \textbf{AUROC} & \textbf{Lang} & \textbf{Tier} & \textbf{AUROC} \\
176	\midrule
177	zh & High & 0.74 & vi & Mid & 0.68 \\
178	es & High & 0.73 & tr & Mid & 0.67 \\
179	fr & High & 0.73 & id & Mid & 0.68 \\
180	de & High & 0.72 & th & Mid & 0.66 \\
181	pt & High & 0.72 & pl & Mid & 0.69 \\
182	\midrule
183	ar & Mid & 0.70 & uk & Mid & 0.68 \\
184	ru & Mid & 0.71 & he & Mid & 0.66 \\
185	hi & Mid & 0.69 & el & Mid & 0.65 \\
186	ko & Mid & 0.69 & sw & Low & 0.58 \\
187	ja & Mid & 0.70 & bn & Low & 0.57 \\
188	\bottomrule
189	\end{tabular}
190	\end{table}
191	
192	Table~\ref{tab:zs_by_lang} shows per-language zero-shot transfer AUROC at the best transfer layer for Qwen3-235B. Of 20 languages, 13 exceed the 0.65 AUROC threshold for usable calibration (11 for Llama~4 Scout). The resource-tier gradient is clear: high-resource languages cluster at 0.72--0.74, mid-resource at 0.65--0.71, and low-resource sw/bn fall below 0.60.
193	
194	\subsection{CKA Reveals Geometric Misalignment}
195	\label{sec:cka_results}
196	
197	\begin{table}[t]
198	\centering
199	\small
200	\caption{CKA similarity between English and target languages at shallow (12) vs.\ deep (72) layers on Qwen3-235B, grouped by resource tier. Pearson $r$ between CKA and transfer AUROC shown at bottom.}
201	\label{tab:cka}
202	\begin{tabular}{lcc}
203	\toprule
204	\textbf{Resource Tier} & \textbf{CKA\textsubscript{shallow}} & \textbf{CKA\textsubscript{deep}} \\
205	\midrule
206	High (zh, es, fr, de, pt) & 0.88 & 0.60 \\
207	Mid (ar, ru, hi, ko, ja, ...) & 0.84 & 0.48 \\
208	Low (sw, bn) & 0.78 & 0.36 \\
209	\midrule
210	All languages (median) & 0.84 & 0.52 \\
211	\bottomrule
212	\end{tabular}
213	\vspace{4pt}
214	
215	\begin{tabular}{lcc}
216	\toprule
217	\textbf{Predictor} & \textbf{Pearson $r$} & \textbf{Variance Explained} \\
218	\midrule
219	CKA (linear) & 0.58 & 34\% \\
220	MMD & 0.25 & 6\% \\
221	\bottomrule
222	\end{tabular}
223	\end{table}
224	
225	CKA similarity between English and target-language representations decreases significantly with depth ($p < 10^{-5}$; Table~\ref{tab:cka}). The decline is steepest for low-resource languages (0.78 $\to$ 0.36) and most gradual for high-resource languages (0.88 $\to$ 0.60), mirroring the transfer AUROC gradient.
226	
227	The CKA--transfer correlation ($r = 0.58$ pooled across both MoE models, $p < 10^{-5}$) explains 34\% of transfer variance, substantially outpredicting MMD ($r = 0.25$, 6\% variance explained). This asymmetry is the mechanistic key: if cross-lingual misalignment were distributional (mean/covariance shift), MMD would predict transfer comparably to CKA. The 5.7$\times$ ratio in explained variance demonstrates that misalignment is geometric---the correctness direction \emph{rotates} across language subspaces rather than merely shifting.
228	
229	The dense model (Gemma~4 31B) shows steeper CKA decline with depth than both MoE models, consistent with MoE routing providing a modest buffer against geometric misalignment (different experts can maintain cross-lingual features at deeper layers).
230	
231	\subsection{CaCLR: A Principled Negative Result}
232	\label{sec:caclr_results}
233	
234	\begin{table}[t]
235	\centering
236	\small
237	\caption{CaCLR $\beta$ sensitivity sweep: $\Delta$AUROC over the $\alpha$-only baseline ($\beta = 0$, $\alpha = 0.5$). Median across 20 languages on both architectures. No $\beta$ value achieves statistical significance.}
238	\label{tab:beta_sweep}
239	\begin{tabular}{lccccc}
240	\toprule
241	$\beta$ & \textbf{Med $\Delta$AUROC} & \textbf{Std} & \textbf{$p$} & \textbf{$d$} & \textbf{\#Improved} \\
242	\midrule
243	0 (baseline) & --- & --- & --- & --- & --- \\
244	0.001 & +0.002 & 0.015 & 0.61 & 0.05 & 12/20 \\
245	0.01 & +0.001 & 0.014 & 0.53 & 0.03 & 11/20 \\
246	0.1 & $-$0.001 & 0.016 & 0.48 & 0.04 & 9/20 \\
247	1.0 & $-$0.003 & 0.018 & 0.35 & 0.10 & 7/20 \\
248	\midrule
249	\multicolumn{2}{l}{Overall $\beta$ effect:} & & \textbf{0.42} & \textbf{0.08} & \\
250	\bottomrule
251	\end{tabular}
252	\end{table}
253	
254	The $\beta$ (consistency loss) term in CaCLR is inert across three orders of magnitude (Table~\ref{tab:beta_sweep}). The overall effect size is negligible (Cohen's $d = 0.08$, $p = 0.42$). This inertness is consistent across resource tiers: high-resource languages see $\Delta = +0.004$, mid-resource $\Delta = 0.000$, low-resource $\Delta = -0.002$---none significant. The $\alpha$-only variant (SB-ECE regularization) provides a small calibration improvement (ECE reduction of 0.7\,pp) without AUROC degradation.
255	
256	\begin{table}[t]
257	\centering
258	\small
259	\caption{Transfer method comparison: median $\Delta$AUROC over zero-shot across 20 languages. All methods at per-language oracle layer. Paired permutation test against zero-shot baseline.}
260	\label{tab:method_comparison}
261	\begin{tabular}{lcccc}
262	\toprule
263	\textbf{Method} & \textbf{Qwen3} & \textbf{Llama4} & \textbf{$p$} & \textbf{$d$} \\
264	\midrule
265	Mean-shift & 0.000 & 0.000 & --- & --- \\
266	CaCLR ($\alpha$-only) & +0.005 & +0.005 & 0.18 & 0.12 \\
267	CaCLR (full) & +0.012 & +0.010 & 0.08 & 0.15 \\
268	Linear projection & \textbf{+0.035} & \textbf{+0.032} & \textbf{0.001} & \textbf{0.55} \\
269	Few-shot (25) & +0.025 & +0.022 & 0.005 & 0.40 \\
270	Few-shot (100) & +0.045 & +0.040 & $<$0.001 & 0.68 \\
271	\bottomrule
272	\end{tabular}
273	\end{table}
274	
275	Table~\ref{tab:method_comparison} shows the full method ranking, consistent across both architectures: few-shot-100 $>$ linear-projection $>$ few-shot-25 $>$ CaCLR $>$ zero-shot $>$ mean-shift. Linear projection achieves +3.5\,pp (Qwen3) and +3.2\,pp (Llama~4) with strong statistical significance ($p = 0.001$, $d = 0.55$), while CaCLR's full improvement (+1.2\,pp) comes entirely from $\alpha$-term calibration regularization, not from cross-lingual consistency.
276	
277	The CKA analysis (\S\ref{sec:cka_results}) provides the explanation: MMD optimizes distributional matching, but the misalignment is geometric (rotation/scaling). Linear projection succeeds because it directly estimates and corrects this rotation via a learned affine transformation on parallel pairs.
278	
279	\subsection{Linear Projection Sample Efficiency}
280	\label{sec:linproj}
281	
282	\begin{table}[t]
283	\centering
284	\small
285	\caption{Linear projection $\Delta$AUROC over zero-shot as a function of parallel pair count. Median across 20 languages, both models. Saturation knee at $\sim$70 pairs.}
286	\label{tab:linproj_pairs}
287	\begin{tabular}{lccc}
288	\toprule
289	\textbf{Pairs} & \textbf{Med $\Delta$AUROC} & \textbf{Std} & \textbf{\% of Max} \\
290	\midrule
291	10 & +0.012 & 0.025 & 33\% \\
292	20 & +0.022 & 0.018 & 61\% \\
293	50 & +0.030 & 0.012 & 83\% \\
294	100 & +0.035 & 0.008 & 97\% \\
295	200 & +0.036 & 0.007 & 100\% \\
296	\bottomrule
297	\end{tabular}
298	\end{table}
299	
300	Linear projection shows rapid saturation (Table~\ref{tab:linproj_pairs}), reaching 90\% of maximum improvement at $\sim$55 pairs and 95\% at $\sim$85 pairs. The knee point is $\sim$70 pairs, consistent with the cross-lingual alignment literature where 50--100 bilingual dictionary entries suffice for word-level alignment \cite{conneau2018muse,artetxe2018vecmap}. The saturation pattern is consistent across architectures (Qwen3 knee: 65 pairs; Llama~4: 75 pairs).
301	
302	The practical implication is that $\sim$50--100 parallel pairs (trivially obtainable from GlobalMMLU's train split or any parallel MCQA corpus) are sufficient to match or exceed CaCLR's entire training pipeline, while requiring no distributional matching, no hyperparameter tuning of $\alpha$/$\beta$, and providing a transparent geometric interpretation.
303	
304	\subsection{Difficulty-Controlled Decomposition}
305	\label{sec:decomp_results}
306	
307	\begin{table}[t]
308	\centering
309	\small
310	\caption{Decomposition results: percentage of language--layer combinations improved by difficulty removal, grouped by layer depth and resource tier. Random-direction control shown for comparison.}
311	\label{tab:decomp}
312	\begin{tabular}{lcc}
313	\toprule
314	\textbf{Condition} & \textbf{\% Improved} & \textbf{Med $\Delta$AUROC} \\
315	\midrule
316	\multicolumn{3}{l}{\emph{By depth}} \\
317	\quad Shallow layers & 50\% & +0.005 \\
318	\quad Deep layers & 78\% & +0.020 \\
319	\midrule
320	\multicolumn{3}{l}{\emph{By resource tier}} \\
321	\quad High-resource & 72\% & +0.018 \\
322	\quad Mid-resource & 65\% & +0.012 \\
323	\quad Low-resource & 53\% & +0.006 \\
324	\midrule
325	Overall & 65\% & +0.012 \\
326	Random direction & 50\% & +0.003 (n.s.) \\
327	\bottomrule
328	\end{tabular}
329	\end{table}
330	
331	Removing the difficulty direction improves transfer in 65\% of language--layer combinations (Table~\ref{tab:decomp}; $p = 0.03$, $d = 0.28$). The improvement concentrates at deep layers (78\% vs.\ 50\% at shallow layers), consistent with the CKA finding: at depth, the capability-specific component---which is geometrically misaligned across languages---drives transfer failure. Removing the shared difficulty signal isolates this effect.
332	
333	The random-direction control (50\% improved, $\Delta = +0.003$, not significant) confirms that the improvement is specific to difficulty removal, not an artifact of dimensionality reduction. The difficulty and correctness directions have moderate cosine similarity (median 0.18, range [0.08, 0.30]), indicating partial but not full entanglement.
334	
335	\subsection{Cross-Lingual Orthogonality}
336	\label{sec:orthogonality}
337	
338	\begin{table}[t]
339	\centering
340	\small
341	\caption{Cosine similarity between correctness and verbalized confidence directions across languages and resource tiers. All values below the 0.12 orthogonality threshold.}
342	\label{tab:orthogonality}
343	\begin{tabular}{lcc}
344	\toprule
345	\textbf{Condition} & \textbf{Cosine (Qwen3)} & \textbf{Cosine (Llama4)} \\
346	\midrule
347	English & 0.035 & 0.038 \\
348	\midrule
349	High-resource (med) & 0.040 & 0.042 \\
350	Mid-resource (med) & 0.060 & 0.063 \\
351	Low-resource (med) & 0.085 & 0.088 \\
352	\midrule
353	All languages (med) & 0.055 & 0.060 \\
354	Max (sw) & 0.100 & 0.098 \\
355	\bottomrule
356	\end{tabular}
357	\end{table}
358	
359	The correctness--confidence orthogonality discovered by \citet{miao2026orthogonality} in English (cosine $< 0.04$) extends to all 20 languages (Table~\ref{tab:orthogonality}), with all cosine similarities below 0.10. However, a resource-tier gradient emerges: high-resource languages maintain tighter orthogonality (median 0.04) than low-resource languages (median 0.085), with a significant correlation between cosine and resource level (Spearman $\rho = 0.52$, $p = 0.018$).
360	
361	Even the maximum cosine (0.10 for Swahili) is far below the $\sim$0.5+ threshold that would indicate meaningful alignment between correctness and confidence signals. This confirms that output-based calibration is structurally limited across all languages---probe-based approaches are the appropriate paradigm regardless of language, though the cross-lingual \emph{transfer} of these probes remains the bottleneck.
362	
363	\subsection{Three-Architecture Comparison}
364	\label{sec:arch}
365	
366	The Gemma~4 31B Dense results (Table~\ref{tab:pareto_summary}) provide the critical dense-vs-MoE contrast. Dense models show smoother Pareto frontiers ($\sigma_\rho = 0.12$ vs.\ 0.15--0.16 for MoE) because every token passes through every layer, creating more uniform layer-to-layer transformations. The dense model's $\rho$ is slightly more negative ($-0.58$) and CKA declines more steeply with depth, confirming that MoE routing provides a modest buffer against geometric misalignment. All three architectures agree on the key finding: mid-depth layers ($\sim$50\% depth) are the right operating point for cross-lingual transfer.
367	
368	\subsection{Extended Language Coverage}
369	\label{sec:extended}
370	
371	Extending to 52 languages, 28 (54\%) exceed 0.65 AUROC in zero-shot transfer. The median drops to 0.66 (vs.\ 0.70 for the curated 20), reflecting the disproportionately low-resource nature of additional languages. Five extremely low-resource languages (Amharic, Myanmar, Zulu, Shona, Kinyarwanda) fall below 0.55, approaching chance. The Pareto $\rho$ weakens slightly ($-0.49$) due to noisier correlations in low-resource languages. Linear projection improvement remains consistent (+3.1\,pp), confirming the geometric correction generalizes. With linear projection, viability extends to $\sim$35/52 languages (67\%).
372	
373	%====================================================================
374	\section{Discussion}
375	\label{sec:discussion}
376	
377	\paragraph{Why Does Distributional Matching Fail?}
378	CaCLR's $\beta$ inertness is not a hyperparameter failure---it is a fundamental limitation of distributional matching for this alignment task. MMD penalizes differences in mean embeddings and kernel-space moments, aligning \emph{marginal distributions} without correcting the \emph{rotation of the correctness direction} across language subspaces. At low $\beta$, the MMD signal is too weak; at medium $\beta$, the gradient pushes distributional alignment without targeting the correctness-relevant subspace; at high $\beta$, the MMD term dominates and distorts the probe. CKA's superiority as a transfer predictor (34\% vs.\ 6\% variance explained) confirms the geometric nature of misalignment.
379	
380	\paragraph{The Linear Projection Connection.}
381	Linear projection succeeds because it directly estimates the rotation matrix mapping source to target representational spaces. The sample complexity is low ($\sim$50--100 pairs) because the correctness-relevant subspace is much lower-dimensional than the full representation space. This is consistent with VecMap/MUSE results for word embeddings, extended here to sentence-level correctness representations.
382	
383	\paragraph{Limitations.}
384	Our evaluation is limited to MCQA tasks, which enable clean correctness labeling. Extension to open-ended generation requires different correctness definitions. Low-resource languages (sw, bn) show marginal probe selectivity (control task selectivity $\sim$10\,pp), warranting cautious interpretation. The Pareto frontier characterization assumes layer-wise probing with fixed representations; methods that modify representations (fine-tuning, adapters) may reshape the frontier.
385	
386	%====================================================================
387	\section{Conclusion}
388	\label{sec:conclusion}
389	
390	We present the first systematic evaluation of cross-lingual correctness probe transfer, revealing a depth--transferability Pareto frontier across three architectures and 20+ languages. CKA analysis identifies geometric misalignment as the mechanism, explaining why distributional matching (CaCLR) fails while linear projection succeeds with as few as 50 parallel pairs. The correctness--confidence orthogonality persists across all tested languages, confirming the structural necessity of probe-based calibration. For practitioners, the prescription is: probe at $\sim$50\% model depth and, if parallel data is available, apply linear projection rather than distributional matching.
391	
392	%====================================================================
393	
394	\bibliography{custom}
395	
396	\begin{thebibliography}{30}
397	
398	\bibitem[Ahuja et~al.(2024)]{ahuja2024globalmmlu}
399	Kabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Akshay Nambi, Tanuja Ganu, Sameer Bansal, Tanvi Bansal, et~al. 2024.
400	\newblock Global{MMLU}: Understanding and addressing cultural and linguistic limitations in multilingual evaluation of large language models.
401	\newblock \emph{arXiv preprint arXiv:2412.03304}.
402	
403	\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}
404	Anastasios~N. Angelopoulos and Stephen Bates. 2023.
405	\newblock Conformal prediction: A gentle introduction.
406	\newblock \emph{Foundations and Trends in Machine Learning}, 16(4):494--591.
407	
408	\bibitem[Artetxe et~al.(2018)]{artetxe2018vecmap}
409	Mikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.
410	\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.
411	\newblock In \emph{Proceedings of ACL}, pages 789--798.
412	
413	\bibitem[Bandarkar et~al.(2023)]{bandarkar2023belebele}
414	Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya~Narayan Shukla, Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. 2023.
415	\newblock The {B}elebele benchmark: A parallel reading comprehension dataset in 122 language variants.
416	\newblock \emph{arXiv preprint arXiv:2308.16884}.
417	
418	\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}
419	Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.
420	\newblock A theory of learning from different domains.
421	\newblock \emph{Machine Learning}, 79(1):151--175.
422	
423	\bibitem[Burns et~al.(2023)]{burns2023discovering}
424	Collin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023.
425	\newblock Discovering latent knowledge in language models without supervision.
426	\newblock In \emph{Proceedings of ICLR}.
427	
428	\bibitem[Civelli et~al.(2024)]{civelli2024difficulty}
429	Andrea Civelli, Brennan Lake, John Keston, and Tobias Roth. 2024.
430	\newblock Cross-lingual transfer of difficulty representations in multilingual language models.
431	\newblock In \emph{Proceedings of EMNLP}, pages 4521--4535.
432	
433	\bibitem[Conneau et~al.(2018)]{conneau2018muse}
434	Alexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\'e} J{\'e}gou. 2018.
435	\newblock Word translation without parallel data.
436	\newblock In \emph{Proceedings of ICLR}.
437	
438	\bibitem[Conneau et~al.(2020)]{conneau2020unsupervised}
439	Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzm{\'a}n, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020.
440	\newblock Unsupervised cross-lingual representation learning at scale.
441	\newblock In \emph{Proceedings of ACL}, pages 8440--8451.
442	
443	\bibitem[Hewitt and Liang(2019)]{hewitt2019control}
444	John Hewitt and Percy Liang. 2019.
445	\newblock Designing and interpreting probes with control tasks.
446	\newblock In \emph{Proceedings of EMNLP}, pages 2733--2743.
447	
448	\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}
449	Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.
450	\newblock Similarity of neural network representations revisited.
451	\newblock In \emph{Proceedings of ICML}, pages 3519--3529.
452	
453	\bibitem[Lai et~al.(2024)]{lai2024llmsurvey}
454	Yuxuan Lai, Xingchen Li, and Yansong Feng. 2024.
455	\newblock LLM calibration and alignment: A survey and its connection to RLHF.
456	\newblock \emph{arXiv preprint arXiv:2404.01076}.
457	
458	\bibitem[Li et~al.(2024)]{li2024inference}
459	Kenneth Li, Oam Patel, Fernanda Vi{\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.
460	\newblock Inference-time intervention: Eliciting truthful answers from a language model.
461	\newblock In \emph{Proceedings of NeurIPS}.
462	
463	\bibitem[Miao et~al.(2026)]{miao2026coral}
464	Qinyu Miao, Alex Wang, and Mark Johnson. 2026.
465	\newblock {CORAL}: Cross-task correctness probes for robust LLM calibration.
466	\newblock In \emph{Proceedings of ACL}, pages 1823--1840.
467	
468	\bibitem[Miao and Ungar(2026)]{miao2026orthogonality}
469	Qinyu Miao and Lyle Ungar. 2026.
470	\newblock Orthogonal correctness and confidence directions in language models: Implications for calibration.
471	\newblock In \emph{Proceedings of NAACL}, pages 2941--2958.
472	
473	\bibitem[Nguyen et~al.(2021)]{nguyen2021wide}
474	Thao Nguyen, Maithra Raghu, and Simon Kornblith. 2021.
475	\newblock Do wide neural networks learn the same things? {C}onvergence over the training trajectory.
476	\newblock In \emph{Proceedings of ICLR}.
477	
478	\bibitem[Pires et~al.(2019)]{pires2019multilingual}
479	Telmo Pires, Eva Schlinger, and Dan Garrette. 2019.
480	\newblock How multilingual is multilingual {BERT}?
481	\newblock In \emph{Proceedings of ACL}, pages 4996--5001.
482	
483	\bibitem[Raghu et~al.(2017)]{raghu2017svcca}
484	Maithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.
485	\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.
486	\newblock In \emph{Proceedings of NeurIPS}, pages 6076--6085.
487	
488	\bibitem[Voita and Titov(2020)]{voita2020mdl}
489	Elena Voita and Ivan Titov. 2020.
490	\newblock Information-theoretic probing with minimum description length.
491	\newblock In \emph{Proceedings of EMNLP}, pages 183--196.
492	
493	\bibitem[Xiao et~al.(2025)]{xiao2025knowledgeboundary}
494	Shiyuan Xiao, Jiaxin Zhang, and Yun Chen. 2025.
495	\newblock Cross-lingual transfer of knowledge boundary probes in multilingual language models.
496	\newblock In \emph{Proceedings of ACL}, pages 5312--5328.
497	
498	\bibitem[Zhou et~al.(2024)]{zhou2024lace}
499	Wenxuan Zhou, Sheng Zhang, Hoifung Poon, and Muhao Chen. 2024.
500	\newblock {LACE}: Layer-wise adaptive calibration ensembles for multilingual LLMs.
501	\newblock In \emph{Proceedings of EMNLP}, pages 7823--7838.
502	
503	\end{thebibliography}
504	
505	%====================================================================
506	\appendix
507	
508	\section{INT8 Validation}
509	\label{app:int8}
510	
511	We validate INT8 quantization against FP16 on Llama~4 Scout at 5 representative layers using a 5\% data subset. The maximum AUROC difference is 0.8\,pp, mean difference 0.3\,pp, with Pearson $r = 0.997$ between INT8 and FP16 probe scores. Rank agreement is 98\%. All differences fall within bootstrap confidence intervals, confirming INT8 does not distort correctness signals.
512	
513	\section{Probe Complexity}
514	\label{app:probe_complexity}
515	
516	MLP probes (2-layer) achieve 2.5\,pp higher English AUROC than logistic regression (0.835 vs.\ 0.81 on Qwen3) but suffer 6\,pp larger transfer gaps (0.17 vs.\ 0.11). The MLP exploits English-specific nonlinearities that do not generalize cross-lingually. 80\% of languages achieve better transfer with logistic regression, justifying our linear probe choice and reinforcing the geometric framing.
517	
518	\section{Cross-Benchmark Generalization}
519	\label{app:benchmarks}
520	
521	Results replicate on Belebele (EN AUROC: 0.78, ZS median: 0.68, $\rho$: $-0.48$) and MMLU-ProX (EN AUROC: 0.82, ZS median: 0.69, $\rho$: $-0.50$). Per-language AUROC rank correlations with GlobalMMLU are 0.82 (Belebele) and 0.88 (MMLU-ProX). Method rankings are consistent across all three benchmarks, confirming CaCLR's $\beta$ inertness is benchmark-independent.
522	
523	\section{Control Task Selectivity}
524	\label{app:control}
525	
526	Following \citet{hewitt2019control}, we train probes on randomly permuted labels. Control AUROC is 0.54--0.55 (near chance). Selectivity (probe AUROC minus control AUROC) is positive across all language--layer combinations: English median 26.5\,pp, high-resource 20\,pp, mid-resource 16\,pp, low-resource 10\,pp. 88\% of combinations exceed 10\,pp selectivity (95\% for high-resource, 70\% for low-resource). The weaker selectivity for low-resource languages is a genuine limitation: conclusions about sw/bn transfer should be interpreted with this caveat.
527	
528	\end{document}
529	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "969c5462-6ba7-4774-9d23-8be84c9265db",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "ed812003-64ea-4d95-96df-29f357cffa83",
  "sourceToolAssistantUUID": "969c5462-6ba7-4774-9d23-8be84c9265db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T21:13:29.897Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D6Dgr7ajhUDjj7qw2KDjC5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed812003-64ea-4d95-96df-29f357cffa83",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWbVYLozXS44UbFkkKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "292926f9-db3d-4661-a8fb-5c0c5a895a1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmS73Qo3biWrR8aQkZoo8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12852,
      "cache_read_input_tokens": 18766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12852,
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

_source line 22 · 2026-05-20T21:13:30.215Z_

<details><summary>↩ Tool result · `toolu_01D6Dgr7ajhUDjj7qw2KDjC5`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{amsthm}
9	\usepackage{booktabs}
10	\usepackage{multirow}
11	\usepackage{xcolor}
12	\usepackage{microtype}
13	\usepackage{hyperref}
14	\usepackage{url}
15	\usepackage{natbib}
16	\newtheorem{theorem}{Theorem}
17	
18	\newcommand{\auroc}{\textsc{auroc}}
19	\newcommand{\ece}{\textsc{ece}}
20	
21	\title{Does Probe-Based Calibration Work Beyond English?\\A Systematic Investigation Across 3 Architectures and 52 Languages}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	Probe-based calibration---training linear classifiers on internal representations to predict answer correctness---has emerged as a promising alternative to output-based calibration in LLMs, but existing work is English-only. We present the first systematic cross-lingual evaluation of correctness probe transfer across 3 architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B), up to 52 languages, and 5 transfer conditions. Our findings are sobering. First, we prove that mean-shift adaptation produces exactly zero \auroc{} change under standard probing pipelines (rank-invariance theorem), distinguishing our setup from prior work. Second, we establish a resource-tier taxonomy of probe transferability: high-resource languages transfer with 7--8pp \auroc{} drop, mid-resource at 10--12pp, and low-resource at 13--20pp, with control tasks revealing that 28\% of low-resource results are capacity artifacts (selectivity $<$8pp). Third, the natural distributional-matching approach (CaCLR) fails---its consistency loss is inert across three orders of magnitude of hyperparameter sweep ($p = 0.71$ vs.\ zero-shot, Cohen's $d = 0.04$). The depth--transferability Pareto frontier is architecture-dependent ($\rho = -0.44$ dense, $-0.38$ MoE-large, $-0.18$ MoE-small; cross-architecture $\tau = 0.33$), precluding universal layer selection. Few-shot adaptation with 25--100 target-language labels is the only viable path, closing the zero-label dream for low-resource languages.
30	\end{abstract}
31	
32	%% ============================================================
33	\section{Introduction}
34	\label{sec:intro}
35	
36	Non-English languages suffer substantially worse calibration in multilingual LLMs, with expected calibration error (\ece{}) up to 5$\times$ higher than English \cite{kadeethum2024calibration}. Output-based calibration methods face a structural ceiling: the correctness direction in internal representations is approximately orthogonal to verbalized confidence \cite{miao2026orthogonality}, meaning no amount of prompt engineering or temperature scaling can fully close the gap.
37	
38	A promising alternative is \emph{probe-based calibration}, which trains lightweight classifiers on internal activations to predict whether the model's answer is correct \cite{miao2024coral,burns2023discovering}. This approach has shown strong results in English, with recent work demonstrating cross-task transfer \cite{miao2024coral}, confidence manifold structure \cite{luo2024confidence}, and the potential for representation-level steering \cite{miao2026orthogonality}. However, all of this work is English-only.
39	
40	The natural question---\emph{do English correctness probes transfer to other languages?}---has not been systematically investigated. Xiao et al.\ \cite{xiao2025knowledge} transferred \emph{knowledge-boundary} probes (input-level answerability) across 8 languages, but knowledge boundaries are fundamentally different from correctness signals: the former encodes whether the model has seen relevant training data, while the latter depends on the model's output for a specific question. Their partial success does not predict ours.
41	
42	We present a systematic investigation across 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense), up to 52 languages spanning 15 language families, and 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot, CaCLR). Our study yields three surviving contributions:
43	
44	\paragraph{(1) Mean-shift rank-invariance.} We prove that under StandardScaler normalization and logistic regression---the standard probing pipeline---mean-shift adaptation produces \emph{exactly} $\Delta\auroc{} = 0$ because mean subtraction adds a constant to all logits, preserving ranks. This distinguishes our setup from Xiao et al., where mean-shift succeeds under different metrics.
45	
46	\paragraph{(2) Resource-tier taxonomy.} We provide the first quantification of cross-lingual probe transferability across 52 languages, establishing that high-resource languages transfer (7--8pp drop), mid-resource is marginal (10--12pp), and low-resource fails (13--20pp). Control tasks reveal capacity artifacts that further weaken low-resource results.
47	
48	\paragraph{(3) Practical recommendation.} Zero-label transfer fails for the majority of the world's languages. Few-shot adaptation with 25--100 target-language labels is the only viable path, closing the zero-label dream for low-resource languages.
49	
50	Along the way, we report that the depth--transferability Pareto frontier is architecture-dependent, that the natural distributional-matching method (CaCLR) produces negligible improvement, that difficulty--capability decomposition is inconclusive, and that CKA-based mechanistic analysis is suggestive but not convincing. The paper serves as a sobering empirical reality check for the probe-based calibration research line.
51	
52	%% ============================================================
53	\section{Related Work}
54	\label{sec:related}
55	
56	\paragraph{Probe-based calibration.}
57	CORAL \cite{miao2024coral} demonstrated cross-task correctness probe transfer in English; CCPS \cite{liu2024confidence} and the Confidence Manifold \cite{luo2024confidence} explored structural properties of correctness representations. Miao \& Ungar \cite{miao2026orthogonality} discovered that correctness and verbalized confidence directions are orthogonal in English, motivating representation-level intervention. All are English-only.
58	
59	\paragraph{Cross-lingual probing.}
60	Xiao et al.\ \cite{xiao2025knowledge} transferred knowledge-boundary probes across 8 languages using mean-shift adaptation, reporting partial success. Their target---input-level answerability---differs fundamentally from output-dependent correctness. We analyze this difference and explain why their mean-shift succeeds under accuracy metrics but produces $\Delta\auroc{} \equiv 0$ in our pipeline (\S\ref{sec:mean_shift}). Civelli et al.\ transferred difficulty probes cross-lingually; we use their methodology as a control in our decomposition analysis.
61	
62	\paragraph{Cross-lingual alignment.}
63	MUSE \cite{conneau2018muse} and VecMap \cite{artetxe2018vecmap} demonstrated that cross-lingual word embedding spaces are approximately related by linear transformations. Our linear projection baseline is motivated by this literature; CaCLR's failure despite distributional matching is the novel finding.
64	
65	\paragraph{Domain adaptation theory.}
66	Ben-David et al.\ \cite{bendavid2010theory} provide the $\mathcal{H}$-divergence framework predicting that transfer degrades with distributional distance. Our resource-tier gradient is consistent with this theory; the novel findings are that the Pareto frontier shape is architecture-dependent (not predicted by theory) and that distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
67	
68	\paragraph{Representation similarity.}
69	CKA \cite{kornblith2019similarity} measures representational similarity between neural network layers. We use CKA to provide mechanistic context for cross-lingual transfer patterns, though the correlation with transfer success is weaker than anticipated.
70	
71	\paragraph{Probing methodology.}
72	Hewitt \& Liang \cite{hewitt2019control} proposed control tasks to measure probe selectivity---the gap between real and random-label probe performance. We adopt their methodology and find that low-resource selectivity is dangerously low, qualifying our results.
73	
74	%% ============================================================
75	\section{Method}
76	\label{sec:method}
77	
78	\subsection{Correctness Probing}
79	
80	Given a multilingual LLM $f$ and a multiple-choice question $q$ in language $\ell$, we extract the hidden state $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$ after the final token. A correctness probe $g_l: \mathbb{R}^d \to [0,1]$ is trained on English data to predict $y \in \{0,1\}$ (whether the model's greedy answer is correct).
81	
82	We use two probe architectures: logistic regression (default) and 2-layer MLP (512 hidden units, ReLU). All activations are StandardScaler-normalized per layer using English training statistics.
83	
84	\subsection{Transfer Conditions}
85	
86	We evaluate five transfer strategies for applying an English-trained probe to language $\ell$:
87	
88	\paragraph{Zero-shot.} Apply the English probe directly to $\ell$-language activations after English-fitted StandardScaler normalization.
89	
90	\paragraph{Mean-shift.} Subtract the mean activation difference: $\tilde{\mathbf{h}}^{(\ell)} = \mathbf{h}^{(\ell)} - (\boldsymbol{\mu}_\ell - \boldsymbol{\mu}_{\text{en}})$. We prove this is equivalent to zero-shot for \auroc{} (\S\ref{sec:mean_shift}).
91	
92	\paragraph{Linear projection.} Learn an affine map $\mathbf{W}\mathbf{h}^{(\ell)} + \mathbf{b}$ from $n$ parallel activation pairs. We study $n \in \{10, 20, 50, 100, 200\}$.
93	
94	\paragraph{Few-shot.} Retrain the probe on $k$ target-language labeled examples ($k \in \{25, 100\}$), initializing from the English probe.
95	
96	\paragraph{CaCLR.} Train with a composite objective $\mathcal{L} = \mathcal{L}_{\text{BCE}} + \alpha \cdot \mathcal{L}_{\text{SB-ECE}} + \beta \cdot \mathcal{L}_{\text{consistency}}$, where $\mathcal{L}_{\text{consistency}}$ minimizes MMD between English and target-language activation distributions using parallel inputs from the GlobalMMLU train split. This requires parallel inputs but zero target-language labels.
97	
98	\subsection{Mean-Shift Rank-Invariance}
99	\label{sec:mean_shift}
100	
101	\begin{theorem}[Mean-Shift Rank-Invariance]
102	Let $g(\mathbf{h}) = \sigma(\mathbf{w}^\top \mathbf{h} + b)$ be a logistic regression probe trained on StandardScaler-normalized English activations. For any target language $\ell$ with mean activation $\boldsymbol{\mu}_\ell$ vs.\ English mean $\boldsymbol{\mu}_{\text{en}}$, the mean-shifted logit is:
103	\begin{align}
104	\mathbf{w}^\top \tilde{\mathbf{h}}^{(\ell)} + b &= \mathbf{w}^\top \mathbf{h}^{(\ell)} + b - \underbrace{\mathbf{w}^\top(\boldsymbol{\mu}_\ell - \boldsymbol{\mu}_{\text{en}})}_{\text{constant } c_\ell}
105	\end{align}
106	Since $c_\ell$ is constant across all samples in language $\ell$, the ranking of logits is preserved. \auroc{} depends only on rankings, so $\Delta\auroc{} \equiv 0$.
107	\end{theorem}
108	
109	We validate this empirically: across 2 models $\times$ all probed layers $\times$ 19 languages, the observed $\Delta\auroc{}$ is exactly 0.000. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities (range: $[-1.2, +6.8]$pp).
110	
111	This distinguishes our setup from Xiao et al., where mean-shift improves \emph{accuracy} (a threshold-dependent metric). Under our rank-based evaluation, mean-shift is provably inert.
112	
113	\subsection{Difficulty Decomposition}
114	
115	Following Civelli et al., we train IRT difficulty probes (Ridge regression on human difficulty scores) and project out the difficulty direction from activations:
116	\begin{equation}
117	\mathbf{h}_{\text{residual}} = \mathbf{h} - \frac{\mathbf{h}^\top \mathbf{d}}{\|\mathbf{d}\|^2} \mathbf{d}
118	\end{equation}
119	where $\mathbf{d}$ is the difficulty probe weight vector. We retrain correctness probes on $\mathbf{h}_{\text{residual}}$ and compare transfer. A random-direction control replaces $\mathbf{d}$ with a random unit vector.
120	
121	\subsection{Orthogonality Measurement}
122	
123	We prompt each model for verbalized confidence scores, fit a confidence probe on the resulting activations, and measure the cosine similarity between confidence and correctness probe weight vectors across all languages and architectures.
124	
125	%% ============================================================
126	\section{Experimental Setup}
127	\label{sec:setup}
128	
129	\paragraph{Models.} Qwen3-235B-A22B (94 layers, MoE, INT8), Llama~4 Scout (48 layers, MoE, INT8), Gemma~4 31B (60 layers, Dense, FP16). INT8 quantization is validated against FP16 (\S\ref{sec:int8}).
130	
131	\paragraph{Benchmarks.} GlobalMMLU (primary), Belebele (reading comprehension), MMLU-ProX (translated MMLU). Train/test split following GlobalMMLU protocol.
132	
133	\paragraph{Languages.} Core set: 20 languages spanning 12 families and 3 resource tiers. Extended set: 52 languages, 15 families, 4 resource tiers.
134	
135	\paragraph{Layers probed.} Every 4th layer for Qwen3 (24 points over 94 layers), every 4th for Llama~4 (12 points over 48), every 4th for Gemma~4 (15 points over 60).
136	
137	\paragraph{Statistical rigor.} Bootstrap CIs (1000 resamples) on all \auroc{}/\ece{}; paired permutation tests for method comparisons; Cohen's $d$ for effect sizes.
138	
139	%% ============================================================
140	\section{Results}
141	\label{sec:results}
142	
143	\subsection{English Probe Performance}
144	
145	Table~\ref{tab:en_probe} shows English correctness probe \auroc{} across layers for all three architectures. Probe quality increases with depth up to approximately 75--80\% of total layers, then declines in the final layers. The best English \auroc{} is 0.776 (Qwen3, layer 72), 0.749 (Llama~4, layer 36), and 0.761 (Gemma~4, layer 45). MLP probes provide a modest advantage ($+1.0$pp mean) over logistic regression in English but transfer marginally worse ($-0.3$pp; Cohen's $d = 0.15$, $p = 0.34$), confirming logistic regression as the default choice.
146	
147	\begin{table}[t]
148	\centering
149	\small
150	\begin{tabular}{@{}lcccc@{}}
151	\toprule
152	\textbf{Layer} & \textbf{Depth} & \textbf{LogReg} & \textbf{MLP} & \textbf{ECE\textsubscript{TC}} \\
153	\midrule
154	\multicolumn{5}{c}{\emph{Qwen3-235B-A22B (94 layers)}} \\
155	\midrule
156	4 & 4\% & .612 & .618 & .192 \\
157	28 & 30\% & .694 & .708 & .121 \\
158	52 & 55\% & .742 & .755 & .082 \\
159	72 & 77\% & \textbf{.776} & \textbf{.783} & \textbf{.069} \\
160	88 & 94\% & .753 & .762 & .079 \\
161	\midrule
162	\multicolumn{5}{c}{\emph{Llama 4 Scout (48 layers)}} \\
163	\midrule
164	8 & 17\% & .631 & .641 & .168 \\
165	20 & 42\% & .712 & .722 & .098 \\
166	36 & 75\% & \textbf{.749} & \textbf{.755} & \textbf{.074} \\
167	44 & 92\% & .731 & .738 & .084 \\
168	\midrule
169	\multicolumn{5}{c}{\emph{Gemma 4 31B Dense (60 layers)}} \\
170	\midrule
171	45 & 75\% & \multicolumn{2}{c}{\textbf{.761}} & — \\
172	\bottomrule
173	\end{tabular}
174	\caption{English correctness probe \auroc{} (LogReg and MLP) and temperature-calibrated \ece{} at selected layers. Best layer per model in bold.}
175	\label{tab:en_probe}
176	\end{table}
177	
178	\subsection{Cross-Lingual Transfer and the Resource-Tier Taxonomy}
179	\label{sec:transfer}
180	
181	Table~\ref{tab:transfer_tier} presents the central finding: zero-shot probe transfer follows a clear resource-tier gradient. On Qwen3, high-resource languages (zh, fr, de, es, ja, ko, ru) transfer at a mean \auroc{} of 0.663 (7--8pp below English). Mid-resource languages (ar, hi, vi, id, th, pl, uk) average 0.615 (10--12pp drop). Low-resource languages (bn, te, ta, sw, yo) average 0.548 (13--20pp drop), with Yoruba reaching 19.9pp below English.
182	
183	\begin{table}[t]
184	\centering
185	\small
186	\begin{tabular}{@{}lcccc@{}}
187	\toprule
188	\textbf{Tier} & \textbf{$n$} & \textbf{Qwen3} & \textbf{Llama4} & \textbf{Gemma4} \\
189	\midrule
190	High & 7 & .663 & .648 & — \\
191	Mid & 7 & .615 & .582 & — \\
192	Low & 5 & .548 & .522 & — \\
193	\midrule
194	All 19 & 19 & .618 & .588 & .605 \\
195	\bottomrule
196	\end{tabular}
197	\caption{Zero-shot transfer \auroc{} (mean) by resource tier. Qwen3 and Llama~4 broken down by tier on the 19-language core set.}
198	\label{tab:transfer_tier}
199	\end{table}
200	
201	Extended to 52 languages (Table~\ref{tab:extended}), the picture worsens. The overall mean drops to 0.581, with a 24\% pass rate (languages exceeding 0.65 \auroc{}). Very-low-resource languages ($n=10$, including Amharic, Lao, Mongolian) average 0.518 with 0\% pass rate. Amharic is the worst at 0.488---below chance when accounting for control task selectivity.
202	
203	\begin{table}[t]
204	\centering
205	\small
206	\begin{tabular}{@{}lcccc@{}}
207	\toprule
208	\textbf{Tier} & \textbf{$n$} & \textbf{\auroc{}} & \textbf{Std} & \textbf{Pass} \\
209	\midrule
210	High & 10 & .651 & .017 & 70\% \\
211	Mid & 18 & .598 & .023 & 28\% \\
212	Low & 14 & .553 & .028 & 7\% \\
213	Very low & 10 & .518 & .021 & 0\% \\
214	\midrule
215	All & 52 & .581 & — & 24\% \\
216	\bottomrule
217	\end{tabular}
218	\caption{Zero-shot transfer \auroc{} across 52 languages (Qwen3). Pass rate = fraction exceeding 0.65 \auroc{}.}
219	\label{tab:extended}
220	\end{table}
221	
222	Table~\ref{tab:per_lang} provides per-language zero-shot transfer \auroc{} on Qwen3 for the 19-language core set. The best transfer layer shifts shallower with decreasing resource level: layer 52 for zh/fr/de, layer 48 for es/ja/ko, down to layer 24 for Yoruba. This depth gradient motivates the Pareto frontier analysis.
223	
224	\begin{table}[t]
225	\centering
226	\small
227	\setlength{\tabcolsep}{3pt}
228	\begin{tabular}{@{}llccccc@{}}
229	\toprule
230	\textbf{Lang} & \textbf{Tier} & \textbf{Layer} & \textbf{\auroc{}} & \textbf{Drop} & \textbf{$\rho$} & \textbf{$p$} \\
231	\midrule
232	zh & high & 52 & .668 & 7.4 & $-$.55 & .006 \\
233	fr & high & 52 & .672 & 7.0 & $-$.51 & .011 \\
234	de & high & 52 & .671 & 7.1 & $-$.48 & .017 \\
235	es & high & 48 & .661 & 7.4 & $-$.42 & .041 \\
236	ja & high & 48 & .658 & 7.7 & $-$.37 & .075 \\
237	ko & high & 48 & .656 & 7.9 & $-$.33 & .115 \\
238	ru & high & 44 & .652 & 7.6 & $-$.25 & .239 \\
239	\midrule
240	pl & mid & 44 & .628 & 10.0 & $-$.14 & .513 \\
241	ar & mid & 40 & .625 & 9.6 & $-$.18 & .399 \\
242	id & mid & 40 & .621 & 10.0 & $-$.02 & .926 \\
243	hi & mid & 40 & .618 & 10.3 & $-$.11 & .609 \\
244	uk & mid & 40 & .614 & 10.7 & $-$.06 & .782 \\
245	vi & mid & 40 & .607 & 11.4 & .04 & .854 \\
246	th & mid & 36 & .594 & 11.8 & .09 & .674 \\
247	\midrule
248	bn & low & 28 & .553 & 14.1 & .14 & .514 \\
249	te & low & 28 & .571 & 12.3 & .18 & .400 \\
250	ta & low & 28 & .568 & 12.6 & .22 & .303 \\
251	sw & low & 28 & .537 & 15.7 & .27 & .202 \\
252	yo & low & 24 & .512 & 19.9 & .31 & .141 \\
253	\bottomrule
254	\end{tabular}
255	\caption{Per-language zero-shot transfer on Qwen3. Layer = best transfer layer; Drop = pp below English at same layer; $\rho$ = Spearman correlation between depth and transfer \auroc{}; $p$ = associated $p$-value.}
256	\label{tab:per_lang}
257	\end{table}
258	
259	\subsection{Architecture-Dependent Pareto Frontier}
260	\label{sec:pareto}
261	
262	The depth--transferability tradeoff is real but architecture-dependent. Table~\ref{tab:arch_compare} summarizes across three architectures. The dense model (Gemma~4) shows the strongest frontier ($\rho = -0.44$, sign consistency 0.68), followed by the large MoE (Qwen3: $\rho = -0.38$, 0.63) and the smaller MoE (Llama~4: $\rho = -0.18$, 0.53).
263	
264	\begin{table}[t]
265	\centering
266	\small
267	\begin{tabular}{@{}llcccc@{}}
268	\toprule
269	\textbf{Model} & \textbf{Type} & \textbf{EN} & \textbf{ZS} & \textbf{$\rho$} & \textbf{Sign} \\
270	\midrule
271	Qwen3 & MoE & .776 & .618 & $-$.38 & .63 \\
272	Llama4 & MoE & .749 & .588 & $-$.18 & .53 \\
273	Gemma4 & Dense & .761 & .605 & $-$.44 & .68 \\
274	\bottomrule
275	\end{tabular}
276	\caption{Three-architecture comparison. EN = best English \auroc{}; ZS = 19-lang mean zero-shot transfer; $\rho$ = global Spearman; Sign = sign consistency of per-language $\rho$.}
277	\label{tab:arch_compare}
278	\end{table}
279	
280	Cross-architecture agreement is low: Kendall's $\tau = 0.33$ between Qwen3 and Llama~4 for optimal layer rankings, and 0.42 between Qwen3 and Gemma~4. Practitioners cannot transfer layer selection findings from one model to another.
281	
282	On Llama~4 Scout, the per-language Spearman $\rho$ median is only $-0.12$ (range: $[-0.41, +0.48]$), with sign consistency at 0.53---essentially a coin flip. Non-monotonic jumps at layers 20--28 reflect MoE expert routing shifts. The Pareto frontier that exists on Qwen3 and Gemma~4 largely vanishes on Llama~4.
283	
284	\subsection{Transfer Method Comparison}
285	\label{sec:methods}
286	
287	Table~\ref{tab:methods} compares all transfer conditions across both primary models. Mean-shift produces exactly $\Delta\auroc{} = 0$ (as proven in \S\ref{sec:mean_shift}). CaCLR provides negligible improvement ($+0.5$pp on Qwen3, $+0.6$pp on Llama~4; Cohen's $d = 0.04$; permutation test $p = 0.71$). Linear projection offers modest gains ($+1.8$pp on Qwen3 with 50 parallel pairs). Few-shot with 100 labels is the strongest method ($+4.4$pp on Qwen3; $d = 0.58$).
288	
289	\begin{table}[t]
290	\centering
291	\small
292	\setlength{\tabcolsep}{3pt}
293	\begin{tabular}{@{}lccccl@{}}
294	\toprule
295	\textbf{Method} & \textbf{Q3} & \textbf{L4} & \textbf{$d$} & \textbf{Labels} \\
296	\midrule
297	Zero-shot & .618 & .588 & — & 0 \\
298	Mean-shift & .618 & .588 & 0.00 & 0 \\
299	CaCLR & .623 & .594 & 0.04 & 0 + parallel \\
300	LinProj (50) & .636 & .608 & 0.24 & $\sim$50 parallel \\
301	Few-shot 25 & .644 & .617 & 0.35 & 25 target \\
302	Few-shot 100 & .662 & .641 & 0.58 & 100 target \\
303	\bottomrule
304	\end{tabular}
305	\caption{Transfer method comparison (19-language mean \auroc{}). Q3 = Qwen3; L4 = Llama~4; $d$ = Cohen's $d$ vs.\ zero-shot.}
306	\label{tab:methods}
307	\end{table}
308	
309	\subsection{CaCLR: A Principled Negative Result}
310	\label{sec:caclr}
311	
312	CaCLR's consistency loss ($\beta \cdot \mathcal{L}_{\text{consistency}}$) is inert. Table~\ref{tab:caclr_ablation} shows the ablation: adding consistency to BCE+SB-ECE \emph{reduces} \auroc{} by 0.6pp. The $\beta$ sweep over three orders of magnitude (0.001--1.0) produces $<$0.4pp variation (Table~\ref{tab:beta_sweep}), ruling out a tuning failure.
313	
314	\begin{table}[t]
315	\centering
316	\small
317	\begin{tabular}{@{}lcc@{}}
318	\toprule
319	\textbf{Variant} & \textbf{\auroc{}} & \textbf{$\Delta$pp} \\
320	\midrule
321	Full CaCLR & .621 & 0.0 \\
322	BCE + SB-ECE & .627 & $+$0.6 \\
323	BCE + Consistency & .611 & $-$1.0 \\
324	BCE only ($\approx$ zero-shot) & .618 & $-$0.3 \\
325	Linear projection (ref.) & .636 & $+$1.5 \\
326	\bottomrule
327	\end{tabular}
328	\caption{CaCLR ablation (Qwen3, 19-language mean). Removing consistency \emph{improves} performance.}
329	\label{tab:caclr_ablation}
330	\end{table}
331	
332	\begin{table}[t]
333	\centering
334	\small
335	\begin{tabular}{@{}lcclcc@{}}
336	\toprule
337	$\beta$ & \textbf{\auroc{}} & $\Delta$pp & $\beta$ & \textbf{\auroc{}} & $\Delta$pp \\
338	\midrule
339	0.0 & .627 & 0.0 & 0.05 & .623 & $-$0.4 \\
340	0.001 & .626 & $-$0.1 & 0.1 & .621 & $-$0.6 \\
341	0.01 & .625 & $-$0.2 & 0.5 & .618 & $-$0.9 \\
342	\bottomrule
343	\end{tabular}
344	\caption{CaCLR $\beta$ sensitivity (Qwen3, $\alpha = 0.3$ fixed, 19-lang mean). Increasing $\beta$ monotonically hurts.}
345	\label{tab:beta_sweep}
346	\end{table}
347	
348	The mechanistic explanation: CKA analysis (\S\ref{sec:cka}) shows that cross-lingual misalignment at deeper layers is \emph{geometric} (the correctness direction rotates across language subspaces), not merely distributional. MMD-based alignment cannot correct rotation, which is why linear projection (which learns the rotation) succeeds where CaCLR (which matches distributions) fails.
349	
350	CaCLR also fails on Gemma~4 Dense (mean \auroc{} 0.609, $-0.9$pp vs.\ linear projection), ruling out the hypothesis that MoE routing specifically caused the failure. On Belebele and MMLU-ProX, CaCLR underperforms linear projection by $-0.8$pp and $-1.1$pp respectively, confirming the negative result generalizes across benchmarks.
351	
352	\subsection{Difficulty Decomposition: Inconclusive}
353	\label{sec:decomposition}
354	
355	The IRT difficulty probe achieves $R^2 = 0.52$ in English (Qwen3) but transfers with degraded quality (9-language mean $R^2 = 0.38$). Projecting out the difficulty direction changes transfer \auroc{} by $-0.5$pp on average---barely above the random-direction control ($-0.3$pp).
356	
357	\begin{table}[t]
358	\centering
359	\small
360	\begin{tabular}{@{}lcccc@{}}
361	\toprule
362	\textbf{Condition} & \textbf{Q3} & \textbf{$\Delta$} & \textbf{L4} & \textbf{$\Delta$} \\
363	\midrule
364	Full activations & .618 & 0.0 & .588 & 0.0 \\
365	Residual (diff.\ out) & .613 & $-$0.5 & .583 & $-$0.5 \\
366	Difficulty only & .569 & $-$4.9 & .548 & $-$4.0 \\
367	Random dir.\ control & .615 & $-$0.3 & .585 & $-$0.3 \\
368	\bottomrule
369	\end{tabular}
370	\caption{Decomposition ablation (9-language mean \auroc{}). Difficulty removal marginally hurts, barely above random control.}
371	\label{tab:decomp}
372	\end{table}
373	
374	Per-language analysis shows no systematic pattern: 3/10 languages improve slightly ($+0.4$ to $+1.3$pp), 5/10 worsen ($-0.3$ to $-2.1$pp), 2/10 unchanged. The difficulty-shared component carries useful cross-lingual signal (questions hard in English tend to be hard everywhere); removing it strips away a genuine invariance. The cosine between difficulty and correctness directions ($0.36 \pm 0.11$) confirms moderate entanglement, preventing clean separation.
375	
376	\subsection{Cross-Lingual Orthogonality}
377	\label{sec:orthogonality}
378	
379	The correctness--confidence orthogonality reported by Miao \& Ungar \cite{miao2026orthogonality} for English persists cross-lingually (overall mean cosine $= 0.074 \pm 0.036$; 73\% of languages below 0.10). However, a resource-tier gradient emerges: high-resource mean 0.052, mid-resource 0.073, low-resource 0.108 (Spearman $\rho = -0.61$ with resource level). Yoruba on Llama~4 reaches 0.172, an outlier weakening the universality claim.
380	
381	\begin{table}[t]
382	\centering
383	\small
384	\begin{tabular}{@{}lcccc@{}}
385	\toprule
386	\textbf{Tier} & \textbf{$n$} & \textbf{Qwen3} & \textbf{Llama4} & \textbf{Mean} \\
387	\midrule
388	High & 8 & .048 & .056 & .052 \\
389	Mid & 7 & .066 & .075 & .073 \\
390	Low & 5 & .100 & .122 & .108 \\
391	All & 20 & .069 & .079 & .074 \\
392	\bottomrule
393	\end{tabular}
394	\caption{Correctness--confidence cosine similarity by resource tier. Lower = more orthogonal. Orthogonality persists but weakens for low-resource languages.}
395	\label{tab:orthogonality}
396	\end{table}
397	
398	This confirms that output-based calibration faces a structural ceiling regardless of language, but this ceiling is noisier for low-resource languages where the model has less capacity to maintain the confidence--correctness dissociation.
399	
400	\subsection{CKA Mechanistic Analysis}
401	\label{sec:cka}
402	
403	CKA between English and target-language activations declines with depth (shallow mean 0.89, deep mean 0.54), confirming that deeper layers are less cross-lingually aligned. However, the correlation between CKA and transfer \auroc{} is weak: Pearson $r = 0.38$ on Qwen3, $r = 0.24$ on Llama~4, $r = 0.32$ combined.
404	
405	\begin{table}[t]
406	\centering
407	\small
408	\begin{tabular}{@{}lcccc@{}}
409	\toprule
410	\textbf{Model} & \textbf{$r$} & \textbf{$p$} & \textbf{Sig.} & \textbf{Total} \\
411	\midrule
412	Qwen3 & .38 & .002 & 5/19 & 19 \\
413	Llama4 & .24 & .041 & 2/19 & 19 \\
414	Combined & .32 & .001 & 7/38 & 38 \\
415	\bottomrule
416	\end{tabular}
417	\caption{CKA vs.\ transfer \auroc{} correlation. Sig.\ = languages with individually significant correlation.}
418	\label{tab:cka}
419	\end{table}
420	
421	A threshold analysis at CKA $= 0.35$ partially replicates: below this threshold, 61\% of language-layer pairs show transfer collapse (\auroc{} $< 0.55$), vs.\ 22\% above. But 39\% of below-threshold pairs do not collapse, and the threshold is architecture-dependent. CKA provides a suggestive but not convincing mechanistic account.
422	
423	The key qualitative insight survives: cross-lingual misalignment is geometric (correctness direction rotates), explaining why MMD-based CaCLR fails while linear projection succeeds. But the quantitative relationship is too noisy for reliable prediction.
424	
425	\subsection{Linear Projection Data Requirements}
426	\label{sec:linproj}
427	
428	Linear projection improves with more parallel pairs but saturates around 100 (Table~\ref{tab:linproj_pairs}). Critically, it fails for low-resource languages even at 200 pairs: Bengali +0.8pp, Swahili +0.6pp, Yoruba +0.6pp---within noise.
429	
430	\begin{table}[t]
431	\centering
432	\small
433	\begin{tabular}{@{}rccc@{}}
434	\toprule
435	\textbf{$n$} & \textbf{\auroc{}} & \textbf{$\Delta$pp} & \textbf{\%~Improved} \\
436	\midrule
437	10 & .608 & $-$1.0 & 26\% \\
438	20 & .621 & $+$0.3 & 42\% \\
439	50 & .636 & $+$1.8 & 55\% \\
440	100 & .643 & $+$2.5 & 63\% \\
441	200 & .647 & $+$2.9 & 68\% \\
442	\bottomrule
443	\end{tabular}
444	\caption{Linear projection \auroc{} by number of parallel pairs (19-language mean). Saturates at $\sim$100 pairs.}
445	\label{tab:linproj_pairs}
446	\end{table}
447	
448	High-resource languages benefit from as few as 20 pairs ($+3.1$pp at 50 pairs), while low-resource languages show minimal improvement regardless of parallel data quantity. The fundamental bottleneck is not the number of parallel pairs but the quality of cross-lingual activation alignment.
449	
450	\subsection{Control Tasks: Capacity Artifacts}
451	\label{sec:control}
452	
453	Control tasks (probes trained on randomly permuted labels) reveal that probe \auroc{} partially reflects capacity rather than genuine correctness signal. Table~\ref{tab:control} shows selectivity by resource tier.
454	
455	\begin{table}[t]
456	\centering
457	\small
458	\begin{tabular}{@{}lccccc@{}}
459	\toprule
460	\textbf{Tier} & \textbf{$n$} & \textbf{Probe} & \textbf{Ctrl} & \textbf{Sel.} & \textbf{Min} \\
461	\midrule
462	High & 7 & .660 & .548 & 17.2 & 10.4 \\
463	Mid & 7 & .614 & .546 & 13.8 & 8.2 \\
464	Low & 5 & .548 & .544 & 8.4 & 4.8 \\
465	All & 19 & .618 & .546 & 13.8 & 4.8 \\
466	\bottomrule
467	\end{tabular}
468	\caption{Control task selectivity (pp) by resource tier. Probe = real-label \auroc{}; Ctrl = random-label \auroc{}; Sel.\ = selectivity (Probe $-$ Ctrl); Min = minimum selectivity in tier.}
469	\label{tab:control}
470	\end{table}
471	
472	For low-resource languages, 28\% of language-layer pairs have selectivity below 8pp. At the English-optimal layer, Swahili scores 0.508 (selectivity $-4.4$pp, \emph{below} the random-label control) and Yoruba scores 0.487 ($-6.4$pp below control). These results are indistinguishable from probe memorization of random structure in high-dimensional activation spaces.
473	
474	The selectivity depth gradient is positive (deeper layers have higher selectivity: 3.3pp at 0--25\% depth, 9.5pp at 50--75\%), reflecting that the correctness signal strengthens with depth while control \auroc{} remains constant ($\sim$0.55). This means shallow-layer transfer results for low-resource languages should be interpreted with particular caution.
475	
476	\subsection{INT8 Quantization Validation}
477	\label{sec:int8}
478	
479	INT8 quantization introduces minimal distortion: mean $\Delta\auroc{} = -0.3$pp (max $-0.7$pp at layer 40), activation cosine similarity $= 0.994$, layer ranking correlation $= 0.98$. Quantization is not a confound.
480	
481	\subsection{Cross-Benchmark Generalization}
482	
483	Findings partially generalize across benchmarks. On Belebele (natively multilingual reading comprehension), zero-shot transfer drops an additional 2.4pp vs.\ GlobalMMLU, with language rankings largely preserved ($\rho = 0.83$). On MMLU-ProX (machine-translated MMLU), the drop is 3.9pp with lower ranking stability ($\rho = 0.69$), reflecting translation quality variation. CaCLR underperforms linear projection on both benchmarks ($-0.8$pp and $-1.1$pp respectively).
484	
485	%% ============================================================
486	\section{Analysis}
487	\label{sec:analysis}
488	
489	\paragraph{Why does transfer fail for low-resource languages?}
490	Three factors compound: (1) the model's internal representations for these languages are less structured, reducing the quality of the correctness signal at any depth; (2) the cross-lingual activation alignment (measured by CKA) degrades more steeply with depth for low-resource languages (CKA at 75\% depth: sw $= 0.33$, yo $= 0.28$ vs.\ fr $= 0.71$, zh $= 0.68$); (3) control tasks show that even the \auroc{} metric itself is unreliable in these settings (selectivity $< 8$pp).
491	
492	\paragraph{Why does CaCLR fail?}
493	CaCLR's MMD-based consistency loss attempts to align activation \emph{distributions} across languages. But the cross-lingual misalignment that matters for correctness probes is \emph{geometric}: the correctness direction rotates across language subspaces at deeper layers. Distribution matching cannot correct rotation---it collapses both signal and noise. Linear projection directly estimates the rotation and therefore succeeds where CaCLR fails.
494	
495	\paragraph{Practical guidance.}
496	For high-resource languages (en, zh, fr, de, es, ja, ko, ru): zero-shot transfer is viable with 7--8pp performance loss. Linear projection with $\sim$50 parallel pairs recovers an additional 1--3pp. For mid-resource languages: few-shot with 25 target-language labels provides the best cost-performance tradeoff. For low-resource languages: the zero-label dream is closed. Few-shot with 100 labels is the minimum viable approach, and even then, results should be validated against control tasks to ensure genuine correctness signal.
497	
498	%% ============================================================
499	\section{Conclusion}
500	\label{sec:conclusion}
501	
502	We present the first systematic evaluation of cross-lingual correctness probe transfer, finding that the probe-based calibration research line does not generalize beyond a small set of high-resource languages without fundamental methodological advances. Mean-shift is provably inert under standard pipelines. The depth--transferability Pareto frontier is architecture-dependent, precluding universal layer selection. CaCLR---the natural distributional-matching approach---fails because cross-lingual misalignment is geometric, not distributional. Few-shot adaptation with 25--100 labels is the only viable path for the majority of the world's languages.
503	
504	\paragraph{Limitations.}
505	Our study is restricted to MCQA benchmarks. Open-ended generation may exhibit different calibration patterns. INT8 quantization, while validated, may interact differently with other probe architectures. The resource-tier taxonomy is coarse---individual language pairs may deviate based on typological proximity rather than resource level alone.
506	
507	\bibliographystyle{plainnat}
508	\bibliography{references}
509	
510	\end{document}
511	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "292926f9-db3d-4661-a8fb-5c0c5a895a1c",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "5886fb3e-5453-4702-bfe8-2b4c428d5035",
  "sourceToolAssistantUUID": "292926f9-db3d-4661-a8fb-5c0c5a895a1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T21:13:30.471Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HSoW1rmMEr8TTCu6ECVgse`</summary>

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
  "parentUuid": "5886fb3e-5453-4702-bfe8-2b4c428d5035",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWbVYLozXS44UbFkkKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14a575d9-2f1a-4bda-b937-c8d50d0ee436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmS73Qo3biWrR8aQkZoo8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12852,
      "cache_read_input_tokens": 18766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12852,
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

_source line 24 · 2026-05-20T21:13:30.480Z_

<details><summary>↩ Tool result · `toolu_01HSoW1rmMEr8TTCu6ECVgse`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\", \"content\": \"# xling_calib_direction — Research Dashboard\\n\\n> 最后更新: 2026-05-20 20:18 UTC | 更新原因: Reviewer feedback integrated: D12 grid justification, D16 mean-shift formalization, CaCLR Path B geometric theory, per-language rho, CKA pilot\\n\\n## 核心方向\\nCross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier (depth vs transferability). CaCLR tests distributional matching; CKA provides mechanistic explanation. Mean-shift rank-invariance proof as formal theoretical contribution. 详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research phase** — MVP 通过 (D004)，Dream 审稿处理完成 (D005)，Reviewer 反馈已整合。等待 re-dream 验证后批准 P0。\\n\\n## Dream 审稿处理总结\\n- 初审评分: best=4/6, median=3/6, worst=3/6 (weak reject)\\n- 13+2 条确认行动项已执行（Reviewer 补充 D12 grid 理由 + D16 mean-shift 形式化）\\n- CaCLR framing 改为 conditional narrative（Path A method / Path B negative result with geometric explanation）\\n- 新增 3 P1 实验: plan_011 (CKA), plan_012 (linproj sensitivity), plan_013 (probing controls)\\n- 全局统计检验要求 + per-language Pareto rho + threshold sensitivity\\n- 5 条观察项待真实实验\\n\\n## 紧急事项\\n- ⚠️ Temperature scaling T=6.21 数据划分未确认 — Agent 正在检查（data integrity 风险）\\n- Agent 同时跑 CKA pilot（MVP activations，验证 plan_011 pipeline）\\n\\n## 近期任务\\n- [ ] Agent 确认 temp scaling 数据划分 + CKA pilot 结果\\n- [ ] 确认 mvp_003 (Llama-3.1-8B) 结果\\n- [ ] Re-dream 验证 framing/plan 改动（目标: best ≥ weak accept, median ≥ borderline）\\n- [ ] Re-dream 达标后批准 plan_001 + plan_002（P0，可 4 GPU 并行）\\n- [ ] [Dream 观察] O1: plan_002 Llama4 Pareto rho\\n- [ ] [Dream 观察] O3: plan_003 CaCLR consistency loss\\n- [ ] [Dream 观察] O4: plan_005 orthogonality 贡献度\\n\\n## GPU 预算\\n- 分配: 4× RTX 6000 PRO 96GB (westd-13176)\\n- P0: ~155 GPU-hrs | P1: ~39 GPU-hrs (含 Dream 新增 9h) | P2: ~80 GPU-hrs\\n- MVP 已用: ~7 GPU-hrs\\n\\n## 实验计划\\n详见 experiment_plan.yaml。P0: 4 (plan_001-004)。P1: 7 (plan_005-013)。P2: 2 (plan_008-009)。\\nCross-cutting: bootstrap CI + paired test + Cohen's d + AUROC threshold sensitivity + per-language rho。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D008 | 2026-05-20 | Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4 | mvp_003, mvp_001 |\\n| D007 | 2026-05-20 | mvp_003 (Llama-3.1-8B) cross-architecture validati | mvp_003, mvp_001 |\\n| D006 | 2026-05-20 | MVP gate re-evaluation after P1 leakage fix: 2/4 P | mvp_001, plan_003 |\\n| D005 | 2026-05-20 | Dream review (3/6 weak reject) processed: 13 confi | plan_003, plan_011, plan_012, plan_013 |\\n| D004 | 2026-05-20 | MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段 | mvp_001 |\\n| D003 | 2026-05-20 | P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/ | mvp_001 |\\n| D002 | 2026-05-20 | MVP 模型固定为 Qwen2.5-7B-Instruct | — |\\n| D001 | 2026-05-20 | MVP 用 7-8B 模型验证核心假设，不直接上 235B | — |\\n\\n\", \"total_chars\": 2633, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14a575d9-2f1a-4bda-b937-c8d50d0ee436",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "f189fccd-cac3-4f4f-a177-d17885e91d06",
  "sourceToolAssistantUUID": "14a575d9-2f1a-4bda-b937-c8d50d0ee436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T21:13:34.310Z_

Now let me check the first dream report and any other supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f189fccd-cac3-4f4f-a177-d17885e91d06",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWbz1cWhZmukk52TQ6s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8631e278-2ed9-456f-b5fb-9557dce4d715",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MoBGZscGzSgixHUAh6r8L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27950,
      "cache_read_input_tokens": 31618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27950,
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

_source line 26 · 2026-05-20T21:13:35.738Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ACznKDaTCMv1y7iBnWUBWH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8631e278-2ed9-456f-b5fb-9557dce4d715",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWbz1cWhZmukk52TQ6s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87425128-ed2f-47d1-b617-50436852b01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MoBGZscGzSgixHUAh6r8L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27950,
      "cache_read_input_tokens": 31618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27950,
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

_source line 27 · 2026-05-20T21:13:35.760Z_

<details><summary>↩ Tool result · `toolu_01ACznKDaTCMv1y7iBnWUBWH`</summary>

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
11	\usepackage{url}
12	\usepackage{hyperref}
13	\usepackage{microtype}
14	\usepackage{array}
15	\usepackage{natbib}
16	
17	\newcommand{\caclr}{\textsc{CaCLR}}
18	\newcommand{\ece}{\text{ECE}}
19	\newcommand{\auroc}{\text{AUROC}}
20	
21	\title{Shifting the Cross-Lingual Calibration Pareto Frontier:\\Probe-Based Calibration Transfer via CaCLR}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	Non-English languages suffer substantially worse calibration in multilingual LLMs, yet existing probe-based calibration methods operate exclusively in English.
30	We present the first systematic study of cross-lingual correctness probe transfer for calibration across 20 languages and three architectures (Qwen3-235B-A22B, Llama~4~Scout, Gemma~4~31B Dense).
31	We discover a \emph{depth-transferability Pareto frontier}: deeper layers yield better English calibration but degrade cross-lingual zero-shot transfer, with the optimal transfer depth converging to $\sim$58--60\% of model depth across architectures.
32	We decompose correctness probe signal into a \emph{difficulty-shared} component (68\% of variance, language-agnostic, transfers at all depths) and a \emph{capability-specific} component (32\%, language-dependent, drives 87\% of transfer degradation).
33	We propose \caclr{} (\textbf{Ca}libration-aware \textbf{C}ross-\textbf{L}ingual \textbf{R}egularization), a training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without target-language labels.
34	\caclr{} shifts the Pareto frontier outward: averaged across architectures, it improves non-English AUROC by 5.2pp over zero-shot transfer and reduces ECE by $\sim$40\% relative to temperature scaling, with zero target-language correctness labels.
35	We further show that correctness--confidence orthogonality (cosine $<0.1$) persists across all 20 languages in both architectures, establishing output-based calibration as structurally limited regardless of language.
36	Results generalize to 52 languages and two additional benchmarks (Belebele, MMLU-ProX).
37	\end{abstract}
38	
39	%------------------------------------------------------------------
40	\section{Introduction}
41	\label{sec:intro}
42	%------------------------------------------------------------------
43	
44	Calibration---the alignment between a model's expressed confidence and its actual accuracy---is critical for safe deployment of large language models (LLMs). While recent work has made substantial progress on English calibration through internal representation probing \cite{burns2023discovering,marks2024geometry,miao2026coral}, non-English languages remain poorly served: they suffer up to 5$\times$ worse expected calibration error (ECE) under standard output-based methods.
45	
46	This gap is not merely quantitative. Miao \& Ungar (2026) demonstrated that the correctness direction in LLM activation space is \emph{orthogonal} to the verbalized confidence direction, implying that output-based calibration methods are structurally limited. However, their analysis---and indeed all probe-based calibration work---is restricted to English. Whether this entire research line extends to multilingual settings is an open question with field-level implications.
47	
48	We address this question systematically. Our investigation reveals four findings that form an unbroken causal chain:
49	
50	\paragraph{Claim 1: Pareto Frontier (Discovery).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87425128-ed2f-47d1-b617-50436852b01b",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "0932c111-fc51-45f5-8d10-a43806b19275",
  "sourceToolAssistantUUID": "87425128-ed2f-47d1-b617-50436852b01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T21:13:36.666Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018PtbUCsNPchqHi9vhrW8HF`</summary>

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
  "parentUuid": "0932c111-fc51-45f5-8d10-a43806b19275",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWbz1cWhZmukk52TQ6s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e306030-d238-4a65-b8b8-3ff25f9c4fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MoBGZscGzSgixHUAh6r8L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27950,
      "cache_read_input_tokens": 31618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27950,
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

_source line 29 · 2026-05-20T21:13:36.678Z_

<details><summary>↩ Tool result · `toolu_018PtbUCsNPchqHi9vhrW8HF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 2 models × 20 languages × all contributions\\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff is architecture-dependent (strong on Qwen, weak on Llama), explained by architecture-specific CKA cliff steepness. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes reveal an architecture-dependent depth-transferability relationship: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong Pareto); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture-dependence of the Pareto shape is itself a core finding, not merely a qualifier.\\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method / Diagnostic)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.\\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA pilot reveals the mechanistic explanation: correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.\\n- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.\\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\\n- **Headline template (method success)**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n- **Headline template (negative result)**: \\\"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\\\"\\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\\n2. **\\\"Temperature scaling baseline\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\n3. **\\\"Mean-shift too weak / why does it fail?\\\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\\n4. **\\\"Difficulty confound\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\n5. **\\\"INT8 artifacts\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\n6. **\\\"Only MCQA\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\n7. **\\\"Predictable from domain adaptation theory\\\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\\n8. **\\\"No statistical tests\\\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\\n9. **\\\"Probing methodology concerns\\\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\\n10. **\\\"No mechanistic explanation\\\"** → CKA analysis provides two levels of insight: (a) between-language: languages with higher CKA (more aligned to English) show less transfer degradation — resource-tier gradient explained; (b) between-architecture: CKA cliff steepness at deepest layers differs (Qwen drops 50% in last 3 layers vs Llama 19%), explaining why Pareto is strong on Qwen but weak on Llama. Within-language depth effect requires 20-language full-scale analysis for statistical power (pilot n=9 per language insufficient). CKA pilot on 2 models × 5 languages validates the approach.\\n11. **\\\"Why not conformal prediction?\\\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\\n12. **\\\"CaCLR parallel activations = test leakage?\\\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\\n\\n## Additional Related Work Coverage (Dream-identified gaps)\\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.\\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.\\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA pilot reveals correctness direction is a robust low-dimensional subspace feature that persists despite global representation divergence. Not a simple \\\"low CKA → bad transfer\\\" relationship, but a threshold phenomenon: transfer collapses only when CKA drops below critical value (~0.35) at deepest layers.\\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.\\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\\n\\n## Differentiation from Closest Prior Work\\n| Paper | Their Focus | Our Difference |\\n|-------|-------------|----------------|\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\n\", \"total_chars\": 12237, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e306030-d238-4a65-b8b8-3ff25f9c4fe3",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "a393c528-1eb2-497b-bcf8-b51942080514",
  "sourceToolAssistantUUID": "0e306030-d238-4a65-b8b8-3ff25f9c4fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T21:13:37.060Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016HHpsPrkjQkmv6cqmpXgfy`</summary>

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
  "parentUuid": "a393c528-1eb2-497b-bcf8-b51942080514",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWbz1cWhZmukk52TQ6s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67dcc18f-f14b-440e-9092-24e55dd91d94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MoBGZscGzSgixHUAh6r8L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27950,
      "cache_read_input_tokens": 31618,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27950
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 321,
          "cache_read_input_tokens": 31618,
          "cache_creation_input_tokens": 27950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27950,
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

_source line 31 · 2026-05-20T21:13:37.069Z_

<details><summary>↩ Tool result · `toolu_016HHpsPrkjQkmv6cqmpXgfy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml\", \"content\": \"papers:\\n  miao2026closing:\\n    title: \\\"Closing the Confidence-Faithfulness Gap in Large Language Models\\\"\\n    authors: [\\\"Ruoxi Miao\\\", \\\"Lyle Ungar\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.25052\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Showed correctness direction and verbalized confidence direction are orthogonal (cosine < 0.04) in 7-8B models. Motivates probing internal representations. English-only — our cross-lingual extension is the natural next step.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  xiao2025knowledge:\\n    title: \\\"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\\\"\\n    authors: [\\\"Zheng Xiao\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2504.13816\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest prior work. Cross-lingual transfer of knowledge-boundary probes (answerable vs unanswerable). Key differences: they probe knowledge boundaries (input-level), we probe correctness (output-dependent); they measure probing accuracy, not ECE/Brier; they test 8 languages, we target 20+.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  civelli2026shared:\\n    title: \\\"A Shared Geometry of Difficulty in Multilingual Language Models\\\"\\n    authors: [\\\"Andrea Civelli\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2601.12731\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Cross-lingual difficulty probe transfer at intermediate layers. Architecture-dependent optimal depth (24-49%). Probes IRT difficulty (question property), not correctness (model property). Critical control for our difficulty ablation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  zhou2025lace:\\n    title: \\\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs\\\"\\n    authors: [\\\"Zhou\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03136\\\"\\n    category: \\\"multilingual_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"LACE: adaptive layer ensemble for multilingual calibration. Confirmed 5x ECE gap across 100+ languages. Requires per-language validation data. Our CaCLR needs no non-English correctness labels.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ravisankar2026dali:\\n    title: \\\"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs\\\"\\n    authors: [\\\"Ravisankar\\\"]\\n    year: 2026\\n    venue: \\\"EACL 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2504.09378\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"DALI: causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. Strongest causal support for our hypothesis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  miao2026coral:\\n    title: \\\"Correctness-Optimized Residual Activation Lens (CORAL)\\\"\\n    authors: [\\\"Ruoxi Miao\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.06022\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Transferable correctness probes via regularized MLP on residual activations, ~50% ECE improvement at 53-66% depth. English-only, cross-task. CaCLR positioned as solution to their identified distribution-shift transfer degradation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  joshi2025calibration:\\n    title: \\\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\\\"\\n    authors: [\\\"Joshi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Identified low-dimensional calibration direction in residual stream evolving across layers.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  confidence_manifold2026:\\n    title: \\\"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08159\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Correctness signals occupy 3-8 dimensions, linearly separable. 25 labeled examples achieve 89% of full-data accuracy. All English-only.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  karandikar2021sbece:\\n    title: \\\"Soft Calibration Objectives for Neural Networks\\\"\\n    authors: [\\\"Karandikar\\\"]\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"\\\"\\n    category: \\\"calibration_methods\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"SB-ECE: differentiable soft-binned ECE enabling gradient-based calibration optimization. Core component of our CaCLR objective.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  khanmohammadi2025ccps:\\n    title: \\\"Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)\\\"\\n    authors: [\\\"Khanmohammadi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.21772\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Calibration via probing perturbed representation stability at final layer. ~55% ECE reduction. English-only, single layer. No cross-lingual or multi-layer analysis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  liu2025middle:\\n    title: \\\"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\\\"\\n    authors: [\\\"Liu\\\", \\\"Niehues\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Middle layers form strongest language-agnostic shared space. Supports our hypothesis about intermediate-layer transfer.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ji2025calibrating:\\n    title: \\\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\\\"\\n    authors: [\\\"Ji\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Verbal uncertainty governed by single linear direction in representation space.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\ncategories:\\n  mechanistic_calibration: \\\"Probing/steering calibration signals in LLM internal representations\\\"\\n  cross_lingual_probing: \\\"Cross-lingual transfer of probes/directions in multilingual models\\\"\\n  cross_lingual_alignment: \\\"Language alignment and shared representations in multilingual LLMs\\\"\\n  multilingual_calibration: \\\"Calibration methods for multilingual LLMs\\\"\\n  calibration_methods: \\\"General calibration objectives and techniques\\\"\\n\\nmeta:\\n  created_at: \\\"2026-05-20\\\"\\n  last_updated: \\\"2026-05-20\\\"\\n  total_papers: 12\\n\", \"total_chars\": 6989, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67dcc18f-f14b-440e-9092-24e55dd91d94",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "25ccce12-5ce3-43eb-b90e-793e0b24c30c",
  "sourceToolAssistantUUID": "67dcc18f-f14b-440e-9092-24e55dd91d94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-20T21:13:40.077Z_

Now let me check the dream report review results to understand what the previous review round found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25ccce12-5ce3-43eb-b90e-793e0b24c30c",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWcU4pYdKMRcDtJteHU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95020239-2612-4568-8b1a-6d4fd4872dfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LZfb6bmruDyGfuHj4q91X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7605,
      "cache_read_input_tokens": 59568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7605,
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

_source line 33 · 2026-05-20T21:13:41.051Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015ovesfKveLJ8uBwuvgd7VU`</summary>

```json
{
  "pattern": "**/dream_*/**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95020239-2612-4568-8b1a-6d4fd4872dfa",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWcU4pYdKMRcDtJteHU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2918a36-0c7d-4403-807a-77332e779278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LZfb6bmruDyGfuHj4q91X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7605,
      "cache_read_input_tokens": 59568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7605,
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

_source line 34 · 2026-05-20T21:13:41.066Z_

<details><summary>↩ Tool result · `toolu_015ovesfKveLJ8uBwuvgd7VU`</summary>

```text
artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json
artifacts/dream_reports/dream_20260520T185641/median/experiment_data.json
artifacts/dream_reports/dream_20260520T185641/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T201854/best/experiment_data.json
artifacts/dream_reports/dream_20260520T201854/median/experiment_data.json
artifacts/dream_reports/dream_20260520T201854/worst/experiment_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2918a36-0c7d-4403-807a-77332e779278",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "5933c7d4-b20f-40b4-8bfc-e89fec68ec92",
  "sourceToolAssistantUUID": "f2918a36-0c7d-4403-807a-77332e779278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T21:13:41.721Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UJ8LTtjxPyGTwoivZgumMr`</summary>

```json
{
  "pattern": "**/dream_*/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5933c7d4-b20f-40b4-8bfc-e89fec68ec92",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWcU4pYdKMRcDtJteHU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a31f31c-59d0-4c14-a103-df668a0d5539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LZfb6bmruDyGfuHj4q91X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7605,
      "cache_read_input_tokens": 59568,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7605
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 59568,
          "cache_creation_input_tokens": 7605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7605,
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

_source line 36 · 2026-05-20T21:13:41.730Z_

<details><summary>↩ Tool result · `toolu_01UJ8LTtjxPyGTwoivZgumMr`</summary>

```text
artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml
artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml
artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T185641/meta.yaml
artifacts/dream_reports/dream_20260520T201854/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T201854/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T201854/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml
artifacts/dream_reports/dream_20260520T201854/median/review_context.yaml
artifacts/dream_reports/dream_20260520T201854/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a31f31c-59d0-4c14-a103-df668a0d5539",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "22194ad6-92ec-4d01-acda-5e31574a6e49",
  "sourceToolAssistantUUID": "1a31f31c-59d0-4c14-a103-df668a0d5539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T21:13:44.819Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Myso466kv8kfzzGBdvYTe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22194ad6-92ec-4d01-acda-5e31574a6e49",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWcp9JzrzDyigc1b63Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9be45035-f1c6-4af3-b7ae-2e91f039727d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgHb6zfwSd1iLvnhmof2Wo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 67173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 720,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 38 · 2026-05-20T21:13:45.097Z_

<details><summary>↩ Tool result · `toolu_017Myso466kv8kfzzGBdvYTe`</summary>

```text
1	narrative_guidance: 'Full method contribution paper (Path A). CaCLR consistency loss
2	  provides meaningful gain, confirming distributional matching via MMD helps align
3	  capability-specific signals at mid-depth layers. Causal chain complete: Pareto frontier
4	  discovered on both architectures with architecture-dependent shape → decomposition
5	  explains frontier via difficulty/capability separation → CaCLR shifts frontier by
6	  aligning capability-specific components → orthogonality bounds output-based approaches
7	  across all languages. CKA provides mechanistic glue linking representation geometry
8	  to transfer success. Headline: "CaCLR-trained correctness probes reduce non-English
9	  ECE by 3.5% over temperature scaling with zero target-language labels across 20
10	  languages on Qwen3-235B and Llama 4 Scout."
11	
12	  '
13	imagined_experiments:
14	- name: Full Pareto Frontier — Qwen3-235B-A22B
15	  plan_id: plan_001
16	  description: '94-layer MoE model, INT8, 24 probed layers (every 4th), 20 languages,
17	    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,
18	    CaCLR).
19	
20	    '
21	  expected_results:
22	    en_best_auroc: 0.838
23	    en_best_layer: 76
24	    en_best_ece_raw: 0.162
25	    en_best_ece_tempcal: 0.048
26	    temp_scaling_T: 4.83
27	    en_auroc_range:
28	    - 0.592
29	    - 0.838
30	    optimal_transfer_layer_median: 56
31	    zs_transfer_auroc_median_20lang: 0.758
32	    zs_transfer_auroc_at_en_optimal_layer76: 0.714
33	    zs_transfer_auroc_at_transfer_optimal_layer56: 0.771
34	    pareto_rho_global: -0.81
35	    pareto_rho_per_lang_median: -0.78
36	    pareto_rho_per_lang_iqr:
37	    - -0.84
38	    - -0.71
39	    zs_langs_above_0p65_out_of_20: 17
40	    best_zs_auroc_by_tier:
41	      HIGH_zh: 0.793
42	      HIGH_es: 0.801
43	      HIGH_fr: 0.798
44	      HIGH_de: 0.784
45	      MID_hi: 0.742
46	      MID_ru: 0.769
47	      MID_ko: 0.751
48	      MID_tr: 0.738
49	      LOW_sw: 0.641
50	      LOW_bn: 0.633
51	    mean_shift_delta_auroc_median: 0.0
52	    linear_proj_delta_auroc_over_zs_median: 0.048
53	    fewshot_25_delta_auroc_over_zs_median: 0.032
54	    fewshot_100_delta_auroc_over_zs_median: 0.055
55	  result_rationale: 'Qwen3-235B-A22B的94层深度和MoE架构产生了强correctness信号。235B参数量使EN AUROC达到0.838，
56	    远超7B MVP的0.754——更大模型的内部表征更丰富、correctness方向更可分离。 Pareto frontier清晰存在：layer 76（81%深度）是EN最优但跨语言transfer在此处下降约5.7pp
57	    （从layer 56的0.771降至0.714），因为深层表征越来越language-specific。 MoE架构中expert routing在深层更加language-dependent，强化了这一效应。
58	    Spearman rho中位数-0.78反映depth-transfer反相关在绝大多数语言中一致。 17/20语言ZS AUROC>0.65体现了235B模型强大的multilingual
59	    representation—— 仅sw/bn/my三个极低资源语言未达标，符合Ben-David H-divergence理论预测。 Mean-shift
60	    ΔAUROC=0.000由rank-invariance定理保证（StandardScaler + logistic regression下 mean-shift仅添加常数偏移，不改变rank
61	    order）。 Linear projection作为强baseline（+4.8pp）反映correctness方向在语言间存在可学习的线性映射关系。
62	
63	    '
64	  tables:
65	  - name: 'Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by
66	      Layer'
67	    columns:
68	    - layer
69	    - depth_pct
70	    - en_auroc
71	    - zs_median_auroc
72	    - zs_min_auroc
73	    - zs_max_auroc
74	    - rho_median
75	    rows:
76	    - - 0
77	      - 0
78	      - 0.592
79	      - 0.583
80	      - 0.521
81	      - 0.601
82	      - null
83	    - - 8
84	      - 9
85	      - 0.631
86	      - 0.618
87	      - 0.554
88	      - 0.639
89	      - null
90	    - - 16
91	      - 17
92	      - 0.672
93	      - 0.659
94	      - 0.589
95	      - 0.678
96	      - null
97	    - - 24
98	      - 26
99	      - 0.711
100	      - 0.698
101	      - 0.621
102	      - 0.719
103	      - null
104	    - - 32
105	      - 34
106	      - 0.738
107	      - 0.729
108	      - 0.648
109	      - 0.751
110	      - null
111	    - - 40
112	      - 43
113	      - 0.762
114	      - 0.756
115	      - 0.662
116	      - 0.778
117	      - null
118	    - - 48
119	      - 51
120	      - 0.781
121	      - 0.771
122	      - 0.658
123	      - 0.793
124	      - null
125	    - - 56
126	      - 60
127	      - 0.798
128	      - 0.771
129	      - 0.641
130	      - 0.801
131	      - null
132	    - - 60
133	      - 64
134	      - 0.808
135	      - 0.762
136	      - 0.632
137	      - 0.796
138	      - null
139	    - - 64
140	      - 68
141	      - 0.816
142	      - 0.751
143	      - 0.618
144	      - 0.788
145	      - null
146	    - - 68
147	      - 72
148	      - 0.824
149	      - 0.741
150	      - 0.607
151	      - 0.779
152	      - null
153	    - - 72
154	      - 77
155	      - 0.831
156	      - 0.728
157	      - 0.598
158	      - 0.768
159	      - null
160	    - - 76
161	      - 81
162	      - 0.838
163	      - 0.714
164	      - 0.584
165	      - 0.756
166	      - null
167	    - - 80
168	      - 85
169	      - 0.835
170	      - 0.702
171	      - 0.571
172	      - 0.742
173	      - null
174	    - - 84
175	      - 89
176	      - 0.829
177	      - 0.688
178	      - 0.558
179	      - 0.729
180	      - null
181	    - - 88
182	      - 94
183	      - 0.818
184	      - 0.671
185	      - 0.542
186	      - 0.712
187	      - null
188	    - - 92
189	      - 98
190	      - 0.801
191	      - 0.649
192	      - 0.523
193	      - 0.694
194	      - null
195	  - name: 'Table 2: Qwen3-235B Transfer Conditions at Fixed Layers (layer 56 + layer
196	      76)'
197	    columns:
198	    - condition
199	    - layer56_median_auroc
200	    - layer76_median_auroc
201	    - delta_vs_zs_l56
202	    - delta_vs_zs_l76
203	    rows:
204	    - - zero-shot
205	      - 0.771
206	      - 0.714
207	      - 0.0
208	      - 0.0
209	    - - mean-shift
210	      - 0.771
211	      - 0.714
212	      - 0.0
213	      - 0.0
214	    - - linear_proj_50pairs
215	      - 0.812
216	      - 0.779
217	      - 0.041
218	      - 0.065
219	    - - fewshot_25
220	      - 0.798
221	      - 0.761
222	      - 0.027
223	      - 0.047
224	    - - fewshot_100
225	      - 0.821
226	      - 0.792
227	      - 0.05
228	      - 0.078
229	    - - CaCLR_full
230	      - 0.828
231	      - 0.788
232	      - 0.057
233	      - 0.074
234	  figures_description:
235	  - 'Fig 1a: Pareto frontier scatter — x-axis EN AUROC, y-axis ZS transfer AUROC median.
236	    Each point is a layer. Clear concave frontier with elbow at ~60% depth. Color
237	    by resource tier shows HIGH langs cluster top-right, LOW langs bottom-left.'
238	  - 'Fig 1b: Heatmap 24 layers × 20 languages, cell color = ZS AUROC. Visible gradient:
239	    warm (high AUROC) at mid-depth for high-resource, shifting to shallower optimum
240	    for low-resource.'
241	  - 'Fig 1c: Per-language Spearman rho distribution (violin plot). Median -0.78, tight
242	    IQR, all languages negative. Annotate sw/bn as outliers with weaker rho.'
243	  analysis: 'Pareto frontier 在 Qwen3-235B 上形态清晰。拐点在 layer 56（60% depth）—— 此后EN AUROC继续上升但ZS
244	    transfer开始下降。MoE架构的expert routing在深层 更加language-specific是造成Pareto tradeoff的主要机制。High-resource语言
245	    （zh/es/fr/de）的frontier更靠右上方，因为这些语言在pretraining中获得更多 token coverage，deep-layer
246	    representation与EN的对齐更好。Low-resource（sw/bn） 即使在最优transfer层也仅达到0.64左右，符合H-divergence理论预测。
247	
248	    '
249	- name: Full Pareto Frontier — Llama 4 Scout
250	  plan_id: plan_002
251	  description: '48-layer MoE model, INT8, 12 probed layers (every 4th), 20 languages,
252	    5 transfer conditions.
253	
254	    '
255	  expected_results:
256	    en_best_auroc: 0.821
257	    en_best_layer: 40
258	    en_best_ece_raw: 0.171
259	    en_best_ece_tempcal: 0.053
260	    temp_scaling_T: 5.12
261	    en_auroc_range:
262	    - 0.604
263	    - 0.821
264	    optimal_transfer_layer_median: 24
265	    zs_transfer_auroc_median_20lang: 0.742
266	    zs_transfer_auroc_at_en_optimal_layer40: 0.698
267	    zs_transfer_auroc_at_transfer_optimal_layer24: 0.756
268	    pareto_rho_global: -0.76
269	    pareto_rho_per_lang_median: -0.73
270	    pareto_rho_per_lang_iqr:
271	    - -0.81
272	    - -0.66
273	    zs_langs_above_0p65_out_of_20: 16
274	    best_zs_auroc_by_tier:
275	      HIGH_zh: 0.778
276	      HIGH_es: 0.789
277	      HIGH_fr: 0.781
278	      HIGH_de: 0.772
279	      MID_hi: 0.728
280	      MID_ru: 0.756
281	      MID_ko: 0.739
282	      MID_tr: 0.721
283	      LOW_sw: 0.628
284	      LOW_bn: 0.618
285	    mean_shift_delta_auroc_median: 0.0
286	    linear_proj_delta_auroc_over_zs_median: 0.044
287	  result_rationale: 'Llama 4 Scout的48层架构使optimal transfer层在50%深度（layer 24）， 而Qwen3-235B在60%深度（layer
288	    56）——这就是architecture-dependent shape的关键证据。 Scout的层数不到Qwen的一半，deep层的language specialization发生得更快（按比例）。
289	    EN best AUROC=0.821略低于Qwen的0.838，反映Scout虽然是MoE但active参数更少。 ZS median 0.742 vs
290	    Qwen的0.758，差距16pp体现了Llama系列multilingual pretraining 数据在低资源语言上的相对弱势。Pareto rho中位数-0.73略弱于Qwen的-0.78，
291	    因为Scout只有12个probed层，frontier采样更粗糙。16/20语言>0.65（vs Qwen 17/20）， sw/bn/my/jv四个低资源语言未达标。Architecture-dependent差异是本文Claim
292	    1的核心发现。
293	
294	    '
295	  tables:
296	  - name: 'Table 3: Llama 4 Scout Pareto Frontier'
297	    columns:
298	    - layer
299	    - depth_pct
300	    - en_auroc
301	    - zs_median_auroc
302	    rows:
303	    - - 0
304	      - 0
305	      - 0.604
306	      - 0.592
307	    - - 4
308	      - 8
309	      - 0.638
310	      - 0.624
311	    - - 8
312	      - 17
313	      - 0.674
314	      - 0.661
315	    - - 12
316	      - 25
317	      - 0.712
318	      - 0.701
319	    - - 16
320	      - 33
321	      - 0.741
322	      - 0.738
323	    - - 20
324	      - 42
325	      - 0.768
326	      - 0.756
327	    - - 24
328	      - 50
329	      - 0.788
330	      - 0.756
331	    - - 28
332	      - 58
333	      - 0.801
334	      - 0.742
335	    - - 32
336	      - 67
337	      - 0.811
338	      - 0.726
339	    - - 36
340	      - 75
341	      - 0.818
342	      - 0.711
343	    - - 40
344	      - 83
345	      - 0.821
346	      - 0.698
347	    - - 44
348	      - 92
349	      - 0.814
350	      - 0.679
351	    - - 48
352	      - 100
353	      - 0.798
354	      - 0.654
355	  figures_description:
356	  - 'Fig 2a: Pareto frontiers overlaid — Qwen3-235B (blue) vs Llama 4 Scout (orange).
357	    Both concave but elbow position differs: Qwen at 60% depth, Scout at 50%. Demonstrates
358	    architecture-dependent shape.'
359	  - 'Fig 2b: Architecture comparison heatmap — difference in ZS AUROC (Qwen minus
360	    Scout) by language × normalized depth. Positive (Qwen better) at deep layers for
361	    high-resource; near zero at shallow layers.'
362	  analysis: '两个架构的Pareto frontier在归一化深度上呈现不同形状：Qwen3-235B的拐点在60%深度， Scout在50%深度。这一差异不能由模型大小alone解释（两者都是MoE），
363	    而是反映了训练数据分布、expert routing策略和层归一化实现的差异。 Scout在每层的language specialization更剧烈，导致frontier更陡峭、拐点更早。
364	    这是论文最核心的发现之一：optimal transfer depth不是universal的，必须per-architecture确定。
365	
366	    '
367	- name: CaCLR Implementation and Comparative Evaluation
368	  plan_id: plan_003
369	  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) 训练、超参数sweep、与所有baseline的全面比较。
370	    Path A: β term provides meaningful gain.
371	
372	    '
373	  expected_results:
374	    caclr_optimal_alpha: 1.0
375	    caclr_optimal_beta: 0.1
376	    caclr_beta_delta_auroc_over_alpha_only_median: 0.032
377	    caclr_beta_delta_auroc_over_alpha_only_range:
378	    - 0.018
379	    - 0.051
380	    caclr_full_delta_auroc_over_zeroshot_median: 0.062
381	    caclr_full_delta_auroc_over_zeroshot_range:
382	    - 0.031
383	    - 0.098
384	    caclr_vs_linear_proj_delta_median: 0.014
385	    caclr_vs_fewshot100_delta_median: -0.008
386	    ece_reduction_vs_temp_scaling_median: 0.035
387	    ece_reduction_vs_temp_scaling_range:
388	    - 0.012
389	    - 0.061
390	    beta_sweep_results:
391	      beta_0.001:
392	        delta_auroc_over_alpha_only: 0.008
393	        note: too weak
394	      beta_0.01:
395	        delta_auroc_over_alpha_only: 0.019
396	        note: marginal
397	      beta_0.1:
398	        delta_auroc_over_alpha_only: 0.032
399	        note: optimal
400	      beta_1.0:
401	        delta_auroc_over_alpha_only: 0.021
402	        note: overfitting to distributional match
403	    alpha_sweep_results:
404	      alpha_0.01:
405	        en_ece: 0.068
406	        transfer_auroc_median: 0.779
407	      alpha_0.1:
408	        en_ece: 0.055
409	        transfer_auroc_median: 0.793
410	      alpha_1.0:
411	        en_ece: 0.041
412	        transfer_auroc_median: 0.808
413	      alpha_10.0:
414	        en_ece: 0.038
415	        transfer_auroc_median: 0.791
416	    layer_interaction:
417	      mid_depth_beta_gain: 0.041
418	      deep_layer_beta_gain: 0.024
419	      shallow_layer_beta_gain: 0.018
420	    qwen_results:
421	      layer56_caclr_full_median: 0.828
422	      layer76_caclr_full_median: 0.788
423	    scout_results:
424	      layer24_caclr_full_median: 0.812
425	      layer40_caclr_full_median: 0.771
426	    bootstrap_ci_beta_effect:
427	    - 0.019
428	    - 0.045
429	    paired_permutation_p_beta: 0.003
430	    cohens_d_beta: 0.48
431	  result_rationale: 'CaCLR consistency loss (β term) 提供了有意义的增益（中位数+3.2pp over α-only），
432	    支持Path A叙事。β=0.1是最优点——更低（0.001-0.01）则MMD约束太弱无法对齐分布， 更高（1.0）则过度约束导致correctness
433	    prediction损失。 β增益在mid-depth层（40-60%）最大（+4.1pp），因为这些层的cross-lingual表征 仍有足够的共享结构让MMD可以有效对齐，但已经开始出现分化需要对齐。
434	    在deep层β增益下降到+2.4pp，因为表征的geometric misalignment（非仅distributional shift） 限制了MMD的有效性——但CaCLR仍然比zero-shot好得多。
435	    CaCLR vs linear projection：CaCLR赢1.4pp中位数，因为它同时优化calibration（α项） 和alignment（β项），而linear
436	    projection仅做alignment。但CaCLR略输于few-shot 100 （-0.8pp），因为100个标注样本提供了直接的target-language
437	    correctness信号。 关键：CaCLR不需要target-language labels，这是实际场景中的核心优势。 ECE reduction vs
438	    temp scaling中位数3.5pp，因为CaCLR在训练时直接优化SB-ECE， 而temp scaling仅做post-hoc rescaling无法修复表征层面的miscalibration。
439	    Bootstrap CI [0.019, 0.045]和p=0.003确认β效应统计显著；Cohen''s d=0.48为中等效应量。
440	
441	    '
442	  tables:
443	  - name: 'Table 4: Transfer Method Comparison (Median AUROC across 20 languages,
444	      both models)'
445	    columns:
446	    - method
447	    - labels_needed
448	    - qwen_layer56
449	    - qwen_layer76
450	    - scout_layer24
451	    - scout_layer40
452	    - median_all
453	    rows:
454	    - - zero-shot
455	      - 0
456	      - 0.771
457	      - 0.714
458	      - 0.756
459	      - 0.698
460	      - 0.735
461	    - - mean-shift
462	      - 0
463	      - 0.771
464	      - 0.714
465	      - 0.756
466	      - 0.698
467	      - 0.735
468	    - - CaCLR_alpha_only
469	      - 0 (parallel inputs)
470	      - 0.798
471	      - 0.762
472	      - 0.784
473	      - 0.745
474	      - 0.772
475	    - - CaCLR_full
476	      - 0 (parallel inputs)
477	      - 0.828
478	      - 0.788
479	      - 0.812
480	      - 0.771
481	      - 0.8
482	    - - linear_proj_50
483	      - 50 parallel pairs
484	      - 0.812
485	      - 0.779
486	      - 0.798
487	      - 0.758
488	      - 0.787
489	    - - fewshot_25
490	      - 25
491	      - 0.798
492	      - 0.761
493	      - 0.781
494	      - 0.741
495	      - 0.77
496	    - - fewshot_100
497	      - 100
498	      - 0.821
499	      - 0.792
500	      - 0.808
501	      - 0.778
502	      - 0.8
503	  - name: 'Table 5: β Sensitivity Sweep (Qwen3-235B, layer 56, median across 20 langs)'
504	    columns:
505	    - beta
506	    - delta_auroc_over_alpha_only
507	    - delta_ece_over_alpha_only
508	    - note
509	    rows:
510	    - - 0.001
511	      - 0.008
512	      - -0.003
513	      - negligible distributional constraint
514	    - - 0.01
515	      - 0.019
516	      - -0.008
517	      - marginal improvement
518	    - - 0.1
519	      - 0.032
520	      - -0.014
521	      - optimal — balances alignment and prediction
522	    - - 1.0
523	      - 0.021
524	      - -0.011
525	      - over-regularized — MMD dominates loss
526	  figures_description:
527	  - 'Fig 3a: Bar chart — 5 transfer methods × 2 models at optimal transfer layer.
528	    CaCLR_full highest, followed by fewshot_100, linear_proj, CaCLR_alpha_only, zero-shot.
529	    Error bars = bootstrap 95% CI.'
530	  - 'Fig 3b: β sweep curve — x-axis β (log scale), y-axis ΔAUROC over α-only. Inverted-U
531	    shape peaking at β=0.1. Three lines for shallow/mid/deep layers showing mid-depth
532	    benefits most.'
533	  - 'Fig 3c: Pareto frontier shift — original ZS frontier (dashed) vs CaCLR frontier
534	    (solid) for both architectures. CaCLR pushes frontier up and right, especially
535	    at mid-depth.'
536	  analysis: 'CaCLR的consistency loss在mid-depth层效果最好，这与CKA分析（plan_011）一致： mid-depth层的cross-lingual表征相似度足够高让MMD有效对齐，但已经有enough
537	    language-specific分化使得对齐产生实际收益。β=0.1的inverted-U曲线说明 distributional matching存在sweet
538	    spot——太弱无效，太强则牺牲correctness prediction。 CaCLR vs fewshot_100的near-parity（-0.8pp）是重要结果：CaCLR达到了接近
539	    100-label supervised的性能，但不需要任何target-language correctness labels。 统计显著性（p=0.003,
540	    d=0.48）确保β效应不是噪声。
541	
542	    '
543	- name: Difficulty-Controlled Decomposition Ablation
544	  plan_id: plan_004
545	  description: 'IRT difficulty probes → project out difficulty → retrain correctness
546	    probes → evaluate transfer. 10 languages × 8 layers × 2 models.
547	
548	    '
549	  expected_results:
550	    decomposition_transfer_delta_after_difficulty_removal_median: 0.031
551	    decomposition_transfer_delta_range:
552	    - 0.011
553	    - 0.052
554	    difficulty_probe_r2_median: 0.68
555	    difficulty_direction_cosine_with_correctness: 0.34
556	    capability_specific_transfer_degradation_per_depth:
557	      shallow_20pct: 0.008
558	      mid_50pct: 0.024
559	      deep_80pct: 0.048
560	    random_direction_control_delta: 0.002
561	    resource_tier_pattern:
562	      HIGH_delta: 0.022
563	      MID_delta: 0.033
564	      LOW_delta: 0.041
565	    bootstrap_ci_decomposition_delta:
566	    - 0.018
567	    - 0.044
568	    paired_permutation_p: 0.006
569	    cohens_d: 0.41
570	  result_rationale: 'Difficulty direction与correctness direction有中等cosine（0.34），说明两者共享
571	    部分信号但不完全重叠。Project out difficulty后，残差中的correctness信号更 "capability-pure"——这个信号在高资源语言间更容易transfer（+2.2pp），
572	    因为capability-specific failures在这些语言间更一致。低资源语言获益最大（+4.1pp）， 因为原始correctness方向中difficulty成分占比更高（低资源语言的difficulty分布
573	    与EN差异更大），去除difficulty后暴露出更可transfer的capability信号。 深层退化更明显（4.8pp）因为深层同时编码了更多language-specific的difficulty信息。
574	    Random-direction control仅+0.2pp，排除了dimensionality reduction artifact—— 是difficulty方向的specific
575	    removal而非arbitrary降维带来的改善。 这个分解是prescriptive的：它告诉我们哪些language-layer组合需要capability
576	    alignment （高delta = 高difficulty entanglement = 需要CaCLR/projection）。
577	
578	    '
579	  tables:
580	  - name: 'Table 6: Decomposition Effect by Resource Tier and Depth (ΔAUROC after
581	      difficulty removal)'
582	    columns:
583	    - depth_pct
584	    - HIGH_avg
585	    - MID_avg
586	    - LOW_avg
587	    - random_control
588	    rows:
589	    - - 20
590	      - 0.012
591	      - 0.014
592	      - 0.019
593	      - 0.001
594	    - - 35
595	      - 0.016
596	      - 0.022
597	      - 0.028
598	      - 0.002
599	    - - 50
600	      - 0.021
601	      - 0.031
602	      - 0.038
603	      - 0.002
604	    - - 60
605	      - 0.024
606	      - 0.036
607	      - 0.043
608	      - 0.003
609	    - - 70
610	      - 0.026
611	      - 0.039
612	      - 0.046
613	      - 0.002
614	    - - 80
615	      - 0.028
616	      - 0.041
617	      - 0.048
618	      - 0.003
619	    - - 85
620	      - 0.025
621	      - 0.038
622	      - 0.044
623	      - 0.002
624	    - - 90
625	      - 0.022
626	      - 0.034
627	      - 0.041
628	      - 0.002
629	  figures_description:
630	  - 'Fig 4a: Three-panel heatmap (HIGH/MID/LOW) — 8 layers × decomposition delta.
631	    Gradient intensifies with depth and decreases with resource level.'
632	  - 'Fig 4b: Scatter plot — difficulty-correctness cosine similarity vs decomposition
633	    delta. Each point = language × layer. Clear positive correlation (r=0.71).'
634	  - 'Fig 4c: Bar chart — decomposition delta vs random-direction control delta at
635	    each depth. Orders of magnitude difference confirms specificity.'
636	  analysis: 'Decomposition结果支持Claim 2：difficulty和capability在correctness方向中可分离， 且分离后capability-specific信号的cross-lingual
637	    transfer一致改善。 关键insight是resource tier gradient——低资源语言的difficulty entanglement最严重，
638	    也从decomposition中获益最多。这为CaCLR提供了theoretical motivation： CaCLR的consistency loss本质上在做distributional
639	    alignment of capability-specific signals。 Random-direction control（~0pp）是关键的methodological
640	    guard rail。
641	
642	    '
643	- name: Cross-Lingual Orthogonality Analysis
644	  plan_id: plan_005
645	  description: 'Correctness-confidence cosine similarity across 20 languages × 2 architectures,
646	    analyzed by resource tier and language family.
647	
648	    '
649	  expected_results:
650	    orthogonality_cosine_mean_across_langs: 0.042
651	    orthogonality_cosine_max_across_langs: 0.062
652	    orthogonality_cosine_min_across_langs: 0.018
653	    orthogonality_cosine_std: 0.013
654	    cosine_by_tier:
655	      HIGH_mean: 0.038
656	      MID_mean: 0.043
657	      LOW_mean: 0.051
658	    cosine_by_architecture:
659	      qwen_mean: 0.039
660	      scout_mean: 0.046
661	    cosine_range_qwen_20lang:
662	    - 0.018
663	    - 0.058
664	    cosine_range_scout_20lang:
665	    - 0.022
666	    - 0.062
667	    all_20_langs_below_0p08: true
668	    bootstrap_ci_mean_cosine:
669	    - 0.035
670	    - 0.049
671	  result_rationale: 'Orthogonality在所有20语言 × 2架构上持续存在（max cosine 0.062 < 0.08阈值）， 确认Miao
672	    & Ungar (2026)的English-only发现是universal structural property。 Low-resource语言cosine略高（0.051
673	    vs HIGH 0.038），因为这些语言的confidence probe quality更低（更少训练数据→confidence方向估计噪声更大→与correctness的
674	    apparent cosine被噪声inflate）。但即使是最高的0.062也远低于non-orthogonal阈值， 说明output-based calibration在结构上受限不依赖于语言。
675	    Qwen略比Scout更orthogonal（0.039 vs 0.046），可能反映Qwen更大的模型容量 使correctness和confidence能被编码在更分离的子空间中。
676	    这个发现bounds entire output-based calibration approach：无论语言或架构， verbalized confidence不包含correctness信息，motivating
677	    probe-based方法。
678	
679	    '
680	  tables:
681	  - name: 'Table 7: Correctness-Confidence Cosine Similarity by Language'
682	    columns:
683	    - language
684	    - tier
685	    - qwen_cosine
686	    - scout_cosine
687	    - mean
688	    rows:
689	    - - en
690	      - HIGH
691	      - 0.031
692	      - 0.037
693	      - 0.034
694	    - - zh
695	      - HIGH
696	      - 0.035
697	      - 0.041
698	      - 0.038
699	    - - es
700	      - HIGH
701	      - 0.033
702	      - 0.039
703	      - 0.036
704	    - - fr
705	      - HIGH
706	      - 0.034
707	      - 0.04
708	      - 0.037
709	    - - de
710	      - HIGH
711	      - 0.036
712	      - 0.042
713	      - 0.039
714	    - - hi
715	      - MID
716	      - 0.039
717	      - 0.045
718	      - 0.042
719	    - - ru
720	      - MID
721	      - 0.037
722	      - 0.043
723	      - 0.04
724	    - - ko
725	      - MID
726	      - 0.041
727	      - 0.047
728	      - 0.044
729	    - - tr
730	      - MID
731	      - 0.043
732	      - 0.049
733	      - 0.046
734	    - - sw
735	      - LOW
736	      - 0.048
737	      - 0.056
738	      - 0.052
739	    - - bn
740	      - LOW
741	      - 0.052
742	      - 0.058
743	      - 0.055
744	  figures_description:
745	  - 'Fig 5: Dot plot — cosine similarity per language, sorted by resource tier. Horizontal
746	    line at 0.08 threshold. All points below. Color by architecture (Qwen blue, Scout
747	    orange). Visible tier gradient.'
748	  analysis: 'Cross-lingual orthogonality的universal persistence是论文的bounding contribution。
749	    它回答了"为什么需要probe-based calibration"：因为output-based方法在结构上 无法获取correctness信息（cosine<0.08），无论语言。Resource
750	    tier gradient 是nuanced finding但不影响main conclusion。
751	
752	    '
753	- name: Probe Complexity Comparison
754	  plan_id: plan_006
755	  description: 'Logistic regression vs 2-layer MLP across all probed layers, both
756	    models. EN accuracy, cross-lingual transfer degradation, calibration comparison.
757	
758	    '
759	  expected_results:
760	    lr_en_best_auroc_qwen: 0.838
761	    mlp_en_best_auroc_qwen: 0.852
762	    lr_en_best_auroc_scout: 0.821
763	    mlp_en_best_auroc_scout: 0.834
764	    lr_zs_transfer_degradation_median: 0.068
765	    mlp_zs_transfer_degradation_median: 0.104
766	    lr_transfer_advantage_over_mlp_median: 0.022
767	    lr_ece_vs_mlp_ece:
768	    - -0.008
769	    - 0.003
770	    mlp_overfit_indicator_deep_layers: true
771	  result_rationale: 'Linear probes在EN AUROC上略输MLP（~1.4pp），但在cross-lingual transfer上
772	    显著更好（+2.2pp median）。MLP的额外容量捕获了EN-specific patterns导致更多 overfitting to source
773	    language——这些patterns在target语言中不泛化。 这与probe complexity literature一致（Hewitt & Liang
774	    2019）：更强的probe 在source domain表现更好但generalization更差。Linear probe的inductive bias
775	    （只能学习线性可分方向）恰好与correctness direction的线性结构匹配， 同时限制了对language-specific artifacts的拟合。
776	    在deep层这个差异更大（MLP overfitting更严重），因为deep层表征更language-specific。 这个结果support使用logistic
777	    regression作为primary probe的选择。
778	
779	    '
780	  tables:
781	  - name: 'Table 8: Probe Complexity — EN AUROC vs ZS Transfer (Qwen3-235B, selected
782	      layers)'
783	    columns:
784	    - layer
785	    - lr_en
786	    - mlp_en
787	    - lr_zs_median
788	    - mlp_zs_median
789	    - lr_transfer_advantage
790	    rows:
791	    - - 24
792	      - 0.711
793	      - 0.722
794	      - 0.698
795	      - 0.691
796	      - 0.007
797	    - - 40
798	      - 0.762
799	      - 0.778
800	      - 0.756
801	      - 0.741
802	      - 0.015
803	    - - 56
804	      - 0.798
805	      - 0.814
806	      - 0.771
807	      - 0.752
808	      - 0.019
809	    - - 76
810	      - 0.838
811	      - 0.852
812	      - 0.714
813	      - 0.686
814	      - 0.028
815	  figures_description:
816	  - 'Fig S1: Dual-axis plot — EN AUROC (solid) and ZS transfer AUROC (dashed) vs layer
817	    depth, separate lines for LR and MLP. MLP''s solid line higher but dashed line
818	    lower, scissors gap widens at deep layers.'
819	  analysis: 'Linear probe是正确的default choice。MLP的EN优势被transfer劣势完全抵消。 这个结果also间接支持correctness
820	    direction是线性的——linear probe已经捕获了 大部分信号，MLP额外捕获的主要是noise/language-specific artifact。
821	
822	    '
823	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
824	  plan_id: plan_007
825	  description: 'Best probes + CaCLR在Belebele和MMLU-ProX上的评估，验证beyond-GlobalMMLU泛化。
826	
827	    '
828	  expected_results:
829	    belebele_zs_auroc_median: 0.731
830	    belebele_caclr_auroc_median: 0.789
831	    mmlu_prox_zs_auroc_median: 0.748
832	    mmlu_prox_caclr_auroc_median: 0.801
833	    cross_benchmark_correlation: 0.92
834	    belebele_pareto_rho_median: -0.71
835	    mmlu_prox_pareto_rho_median: -0.75
836	  result_rationale: 'Belebele（reading comprehension）的ZS AUROC略低于GlobalMMLU（0.731 vs
837	    0.758）， 因为不同任务的correctness信号分布不完全一致——但Pareto frontier仍然存在 （rho=-0.71），说明depth-transfer
838	    tradeoff是task-general的。 MMLU-ProX与GlobalMMLU最相似（同为knowledge QA），所以结果最接近（0.748
839	    vs 0.758）。 CaCLR在两个benchmark上都提供了consistent improvement（+5.3-5.8pp）， 说明CaCLR学到的alignment不是GlobalMMLU-specific的。
840	    Cross-benchmark correlation 0.92表明per-language transfer difficulty在benchmarks间高度一致——
841	    sw/bn在所有benchmarks上都最难transfer，zh/es在所有benchmarks上都最容易。
842	
843	    '
844	  tables:
845	  - name: 'Table 9: Cross-Benchmark Generalization (Qwen3-235B, optimal transfer layer)'
846	    columns:
847	    - benchmark
848	    - zs_median
849	    - caclr_median
850	    - pareto_rho
851	    - langs_above_0p65
852	    rows:
853	    - - GlobalMMLU
854	      - 0.758
855	      - 0.808
856	      - -0.78
857	      - 17
858	    - - Belebele
859	      - 0.731
860	      - 0.789
861	      - -0.71
862	      - 15
863	    - - MMLU-ProX
864	      - 0.748
865	      - 0.801
866	      - -0.75
867	      - 16
868	  figures_description:
869	  - 'Fig S2: Scatter — per-language ZS AUROC on GlobalMMLU vs Belebele. High correlation
870	    (r=0.92). Each point labeled with language code.'
871	  analysis: 'Cross-benchmark泛化confirm findings are not benchmark-specific artifact。
872	    Pareto frontier在三个benchmark上一致存在但shape有细微差异—— Belebele更浅的optimal depth可能反映reading
873	    comprehension使用了更浅层的表征。
874	
875	    '
876	- name: INT8 Validation Ablation
877	  plan_id: plan_010
878	  description: 'INT8 vs FP16对比，Llama 4 Scout，5 representative layers，5% random subset。
879	
880	    '
881	  expected_results:
882	    int8_fp16_auroc_max_diff: 0.006
883	    int8_fp16_auroc_mean_diff: 0.003
884	    int8_fp16_ece_max_diff: 0.008
885	    int8_fp16_direction_cosine_min: 0.987
886	    all_diffs_within_noise: true
887	  result_rationale: 'INT8量化对correctness direction的影响极小（max AUROC差异0.6pp）， 因为correctness信号是高SNR的线性方向——量化噪声主要影响低幅度维度，
888	    而correctness direction在high-variance维度上有强projection。 Direction cosine>0.987说明INT8和FP16下提取的correctness方向几乎相同。
889	    ECE差异稍大（0.8pp）因为calibration对probability scale更敏感，但仍在噪声范围内。 这排除了"INT8 artifact"的reviewer
890	    concern。
891	
892	    '
893	  tables:
894	  - name: 'Table S1: INT8 vs FP16 Comparison (Llama 4 Scout)'
895	    columns:
896	    - layer
897	    - int8_auroc
898	    - fp16_auroc
899	    - diff
900	    - direction_cosine
901	    rows:
902	    - - 8
903	      - 0.674
904	      - 0.678
905	      - -0.004
906	      - 0.991
907	    - - 16
908	      - 0.741
909	      - 0.745
910	      - -0.004
911	      - 0.989
912	    - - 24
913	      - 0.788
914	      - 0.791
915	      - -0.003
916	      - 0.992
917	    - - 32
918	      - 0.811
919	      - 0.814
920	      - -0.003
921	      - 0.99
922	    - - 40
923	      - 0.821
924	      - 0.827
925	      - -0.006
926	      - 0.987
927	  figures_description:
928	  - 'Fig S3: Bland-Altman plot — mean of INT8/FP16 AUROC (x) vs difference (y). All
929	    points within ±0.01 band. No systematic bias.'
930	  analysis: 'INT8量化不distort correctness signals。所有差异在bootstrap noise范围内。 Deep层差异略大（layer
931	    40: 0.6pp）符合预期——深层表征更complex，量化误差累积更多。 但0.6pp远小于实验效应（CaCLR +6pp），不影响任何结论。
932	
933	    '
934	- name: CKA Cross-Lingual Representation Similarity
935	  plan_id: plan_011
936	  description: 'CKA (linear kernel) between EN and each target language at every probed
937	    layer, correlated with transfer AUROC. Mechanistic explanation for Pareto frontier.
938	
939	    '
940	  expected_results:
941	    cka_transfer_pearson_r: 0.82
942	    cka_transfer_pearson_r_ci:
943	    - 0.76
944	    - 0.87
945	    cka_transfer_spearman_rho: 0.79
946	    cka_en_zh_by_depth_trend: monotonically decreasing from 0.92 (shallow) to 0.61
947	      (deep)
948	    cka_en_sw_by_depth_trend: monotonically decreasing from 0.84 (shallow) to 0.38
949	      (deep)
950	    cka_resource_tier_gradient:
951	      HIGH_mean_cka_at_optimal_depth: 0.78
952	      MID_mean_cka_at_optimal_depth: 0.71
953	      LOW_mean_cka_at_optimal_depth: 0.58
954	    geometric_misalignment_evidence: 'CKA drop from mid to deep layers exceeds what
955	      mean/covariance shift alone predicts. Subspace angle analysis shows correctness
956	      direction rotates 15-35° across languages at deep layers vs 5-12° at shallow
957	      layers.
958	
959	      '
960	    cka_explains_caclr_beta_limit: 'At layers where CKA < 0.55, β term provides diminishing
961	      returns because geometric misalignment (rotation) dominates distributional shift.
962	
963	      '
964	  result_rationale: 'CKA与transfer AUROC的高相关（r=0.82）提供了Pareto frontier的mechanistic
965	    explanation： cross-lingual表征相似度随depth monotonically下降，直接导致deep层transfer degradation。
966	    这不是trivial的"深层更specific"——CKA量化了具体的相似度数值并与transfer成功率 建立了定量关系。High-resource语言在所有depth保持更高CKA（因为pretraining
967	    data overlap）， 解释了resource tier gradient。 关键insight：deep层的CKA下降不仅是distributional
968	    shift（可被MMD修正）， 还包含geometric misalignment（correctness方向在语言间旋转15-35°）。 这解释了CaCLR
969	    β term在deep层效果减弱——MMD对齐分布但不学习旋转， 而linear projection学习旋转所以在deep层更稳定。 Subspace angle
970	    analysis区分了distributional vs geometric misalignment， 为Path A narrative提供了theoretical
971	    depth：CaCLR works at mid-depth因为 那里的misalignment主要是distributional的。
972	
973	    '
974	  tables:
975	  - name: 'Table 10: CKA by Depth and Resource Tier (Qwen3-235B)'
976	    columns:
977	    - depth_pct
978	    - HIGH_cka
979	    - MID_cka
980	    - LOW_cka
981	    - zs_auroc_median
982	    rows:
983	    - - 10
984	      - 0.93
985	      - 0.89
986	      - 0.84
987	      - 0.618
988	    - - 25
989	      - 0.9
990	      - 0.85
991	      - 0.78
992	      - 0.698
993	    - - 40
994	      - 0.86
995	      - 0.79
996	      - 0.69
997	      - 0.756
998	    - - 50
999	      - 0.82
1000	      - 0.74
1001	      - 0.62
1002	      - 0.771
1003	    - - 60
1004	      - 0.78
1005	      - 0.69
1006	      - 0.55
1007	      - 0.771
1008	    - - 70
1009	      - 0.73
1010	      - 0.63
1011	      - 0.47
1012	      - 0.741
1013	    - - 80
1014	      - 0.67
1015	      - 0.56
1016	      - 0.41
1017	      - 0.714
1018	    - - 90
1019	      - 0.61
1020	      - 0.49
1021	      - 0.35
1022	      - 0.688
1023	  figures_description:
1024	  - 'Fig 6a: Dual-axis — CKA (left y-axis, lines by tier) and ZS AUROC median (right
1025	    y-axis, dashed) vs normalized depth. CKA decrease tracks AUROC decrease after
1026	    elbow.'
1027	  - 'Fig 6b: Scatter — CKA vs ZS transfer AUROC, each point = language × layer. Strong
1028	    linear relationship (r=0.82). Color by resource tier.'
1029	  - 'Fig 6c: Subspace angle between EN and target correctness directions vs depth.
1030	    Angles increase with depth; LOW languages diverge faster.'
1031	  analysis: 'CKA analysis是论文的mechanistic backbone。它将observation（Pareto frontier） 与explanation（representation
1032	    geometry变化）和method（CaCLR的作用机制与局限） 连接起来。CKA<0.55作为CaCLR β有效性的threshold是一个actionable
1033	    finding—— 实践者可以用CKA预测CaCLR在哪些layer-language组合上有效。 Geometric vs distributional
1034	    misalignment的区分是theoretical contribution： 它解释了为什么distributional matching（MMD/CaCLR）在mid-depth有效但在deep层递减，
1035	    而geometric alignment（linear projection）在deep层更稳定。
1036	
1037	    '
1038	- name: Linear Projection Sensitivity Analysis
1039	  plan_id: plan_012
1040	  description: 'Linear projection pair count sweep (10, 20, 50, 100, 200). Both models
1041	    × 5 layers × 20 languages.
1042	
1043	    '
1044	  expected_results:
1045	    linear_proj_min_pairs_for_saturation: 35
1046	    saturation_criterion: 95% of 200-pair performance
1047	    pairs_sweep:
1048	      10:
1049	        median_auroc: 0.762
1050	        pct_of_200: 0.88
1051	      20:
1052	        median_auroc: 0.778
1053	        pct_of_200: 0.94
1054	      50:
1055	        median_auroc: 0.792
1056	        pct_of_200: 0.98
1057	      100:
1058	        median_auroc: 0.796
1059	        pct_of_200: 0.99
1060	      200:
1061	        median_auroc: 0.798
1062	        pct_of_200: 1.0
1063	    low_resource_saturation_later: true
1064	    low_resource_min_pairs: 48
1065	    high_resource_min_pairs: 22
1066	  result_rationale: 'Linear projection在~35 pairs时达到饱和（95% of 200-pair performance），
1067	    因为correctness方向是低维线性结构——学习一个旋转/缩放矩阵不需要很多样本。 10 pairs已经达到88%性能，说明即使极少数据也能捕获主要的geometric
1068	    transformation。 50 pairs后几乎无改善（98%→100%），符合线性映射的low sample complexity理论。 Low-resource语言需要slightly
1069	    more pairs（48 vs 22），因为表征空间中 correctness方向的SNR更低，需要更多样本来robustly估计映射。 整体saturation在20-50范围内，support
1070	    "≤50 parallel pairs suffice"的claim。 这建立了linear projection作为practical baseline的地位——
1071	    50 pairs在任何语言都容易获得（e.g., 翻译50个MCQA items）。
1072	
1073	    '
1074	  tables:
1075	  - name: 'Table 11: Linear Projection Data Efficiency (median across 20 langs × 2
1076	      models)'
1077	    columns:
1078	    - n_pairs
1079	    - median_auroc
1080	    - delta_vs_zs
1081	    - pct_of_200pair
1082	    - HIGH_auroc
1083	    - LOW_auroc
1084	    rows:
1085	    - - 10
1086	      - 0.762
1087	      - 0.027
1088	      - 88
1089	      - 0.781
1090	      - 0.638
1091	    - - 20
1092	      - 0.778
1093	      - 0.043
1094	      - 94
1095	      - 0.798
1096	      - 0.651
1097	    - - 50
1098	      - 0.792
1099	      - 0.057
1100	      - 98
1101	      - 0.814
1102	      - 0.664
1103	    - - 100
1104	      - 0.796
1105	      - 0.061
1106	      - 99
1107	      - 0.818
1108	      - 0.668
1109	    - - 200
1110	      - 0.798
1111	      - 0.063
1112	      - 100
1113	      - 0.821
1114	      - 0.671
1115	  figures_description:
1116	  - 'Fig S4: Learning curve — n_pairs (x, log) vs median AUROC (y). Rapid rise, plateau
1117	    at ~50. Separate lines for HIGH/MID/LOW tiers — all plateau but at different levels.'
1118	  analysis: 'Linear projection的data efficiency confirms它作为practical baseline的价值。 50
1119	    pairs的saturation point意味着任何有minimal translation capacity的语言 都可以使用这个方法。这也为CaCLR设定了benchmark：CaCLR需要beat
1120	    50-pair projection 才能justify its additional complexity（in best tier, CaCLR beats
1121	    by +1.4pp median）。
1122	
1123	    '
1124	- name: Probing Control Tasks (Hewitt & Liang 2019)
1125	  plan_id: plan_013
1126	  description: 'Random-label control probes at each layer. Selectivity = probe AUROC
1127	    - control AUROC. Validates genuine correctness signal.
1128	
1129	    '
1130	  expected_results:
1131	    control_task_auroc_range:
1132	    - 0.502
1133	    - 0.538
1134	    selectivity_median: 0.284
1135	    selectivity_min: 0.192
1136	    selectivity_max: 0.341
1137	    control_task_selectivity_min_across_langs: 0.192
1138	    selectivity_by_depth:
1139	      shallow: 0.218
1140	      mid: 0.294
1141	      deep: 0.312
1142	    selectivity_by_tier:
1143	      HIGH: 0.301
1144	      MID: 0.278
1145	      LOW: 0.234
1146	  result_rationale: 'Control probe AUROC在0.50-0.54范围（near chance），selectivity中位数0.284
1147	    远超15pp minimum threshold（min=19.2pp）。这confirm probe AUROC反映 genuine correctness
1148	    direction而非memorized artifacts或probe capacity。 Selectivity随depth增加（0.218→0.312），因为深层表征包含更丰富的correctness
1149	    信号而control仍在chance附近——深层probe的高AUROC不是因为probe容量过大。 Low-resource语言selectivity最低（0.234）但仍远超threshold，
1150	    说明即使低资源语言的correctness信号也是genuine的（不是noise fitting）。 这直接回应Hewitt & Liang probing
1151	    methodology critique—— 我们的probes确实在提取linguistic property而非exploiting high-dimensional
1152	    capacity。
1153	
1154	    '
1155	  tables:
1156	  - name: 'Table S2: Control Task Selectivity (Qwen3-235B, selected layers × languages)'
1157	    columns:
1158	    - layer
1159	    - en_selectivity
1160	    - zh_selectivity
1161	    - sw_selectivity
1162	    - control_auroc
1163	    rows:
1164	    - - 16
1165	      - 0.248
1166	      - 0.231
1167	      - 0.192
1168	      - 0.512
1169	    - - 32
1170	      - 0.281
1171	      - 0.268
1172	      - 0.218
1173	      - 0.519
1174	    - - 48
1175	      - 0.309
1176	      - 0.292
1177	      - 0.241
1178	      - 0.524
1179	    - - 56
1180	      - 0.318
1181	      - 0.301
1182	      - 0.248
1183	      - 0.521
1184	    - - 76
1185	      - 0.341
1186	      - 0.324
1187	      - 0.262
1188	      - 0.538
1189	  figures_description:
1190	  - 'Fig S5: Paired bar chart — probe AUROC (dark) vs control AUROC (light) at each
1191	    layer. Gap (selectivity) clearly visible and widening with depth. Horizontal line
1192	    at 15pp threshold.'
1193	  analysis: 'Control task validation是methodological necessity。Selectivity最小值19.2pp
1194	    大幅超过15pp阈值，即使在最challenging的条件（low-resource × shallow layer） 也确认probe是在提取genuine
1195	    signal。这让reviewer对所有downstream结果 （Pareto frontier, CaCLR, decomposition）更有信心。
1196	
1197	    '
1198	- name: Gemma 4 31B Dense — Camera-Ready Extension
1199	  plan_id: plan_008
1200	  description: 'Third architecture (dense, FP16), full Pareto frontier. Dense vs MoE
1201	    contrast for camera-ready.
1202	
1203	    '
1204	  expected_results:
1205	    en_best_auroc: 0.809
1206	    en_best_layer: 48
1207	    optimal_transfer_layer: 36
1208	    zs_transfer_auroc_median: 0.738
1209	    pareto_rho_median: -0.69
1210	    pareto_shape: smoother frontier than MoE models — no sharp elbow
1211	    dense_vs_moe_key_finding: 'Dense architecture shows shallower Pareto slope — transfer
1212	      degrades more gradually with depth compared to MoE models. Consistent with hypothesis
1213	      that expert routing accelerates language specialization.
1214	
1215	      '
1216	  result_rationale: 'Gemma 4 31B Dense作为dense对照提供了architectural contrast。 EN AUROC
1217	    0.809低于两个MoE模型（0.838, 0.821），反映31B dense参数<235B MoE active参数。 关键发现：dense架构的Pareto
1218	    frontier更平滑（rho=-0.69 vs MoE -0.73/-0.78）， 没有MoE的sharp elbow。这是因为MoE的expert routing在深层创造了discrete
1219	    language specialization（某些experts "负责"特定语言），而dense模型的specialization是gradual的。
1220	    这是architecture-dependent Pareto shape claim的strongest evidence。 Optimal transfer在75%深度（layer
1221	    36/48），比Qwen3浅（60%）但比Scout深（50%）， 提供了第三个data point来characterize architecture-depth
1222	    relationship。
1223	
1224	    '
1225	  tables:
1226	  - name: 'Table S3: Three-Architecture Comparison Summary'
1227	    columns:
1228	    - model
1229	    - type
1230	    - params
1231	    - layers
1232	    - en_best_auroc
1233	    - zs_median
1234	    - optimal_transfer_pct
1235	    - pareto_rho
1236	    rows:
1237	    - - Qwen3-235B-A22B
1238	      - MoE
1239	      - 235B
1240	      - 94
1241	      - 0.838
1242	      - 0.758
1243	      - 60
1244	      - -0.78
1245	    - - Llama 4 Scout
1246	      - MoE
1247	      - 109B (17B active)
1248	      - 48
1249	      - 0.821
1250	      - 0.742
1251	      - 50
1252	      - -0.73
1253	    - - Gemma 4 31B Dense
1254	      - Dense
1255	      - 31B
1256	      - 60
1257	      - 0.809
1258	      - 0.738
1259	      - 75
1260	      - -0.69
1261	  figures_description:
1262	  - 'Fig S6: Three Pareto frontiers overlaid on normalized depth axis. MoE models
1263	    show sharper elbows; Dense model is smoother. Annotated with optimal transfer
1264	    depth for each.'
1265	  analysis: 'Three-architecture comparison is the crown jewel of Claim 1。 Dense vs
1266	    MoE对比provides causal insight into WHY frontiers differ—— expert routing is the
1267	    mechanism driving sharp language specialization at depth.
1268	
1269	    '
1270	- name: Extended Language Coverage — Camera-Ready
1271	  plan_id: plan_009
1272	  description: 'Expand from 20 to 50+ languages. Camera-ready extension using GlobalMMLU/Belebele
1273	    full sets.
1274	
1275	    '
1276	  expected_results:
1277	    total_languages: 52
1278	    zs_langs_above_0p65: 38
1279	    zs_auroc_median_52lang: 0.721
1280	    new_low_resource_findings: 'Several additional low-resource languages (e.g., Yoruba,
1281	      Hausa, Malagasy) show ZS AUROC 0.58-0.64, confirming resource-tier gradient
1282	      extends to tail.
1283	
1284	      '
1285	    pareto_frontier_robust: true
1286	    caclr_generalizes: true
1287	    caclr_delta_over_zs_52lang_median: 0.058
1288	  result_rationale: '52语言验证confirms所有findings at broader scale。ZS median从20 langs的0.758
1289	    降到52 langs的0.721，因为新增语言主要是低资源的——这是expected的composition effect。 38/52 > 0.65（73%）vs
1290	    17/20（85%），比例下降也反映低资源语言的加入。 Pareto frontier和CaCLR在所有语言上consistent，说明findings是language-general的。
1291	    Key new finding：Yoruba/Hausa等sub-Saharan African语言的ZS AUROC（0.58-0.62） 与sw/bn相当，但CaCLR对这些语言的improvement更大（+7-9pp），
1292	    可能因为GlobalMMLU translations provide parallel data that partially bridges the representation
1293	    gap for these extremely low-resource languages.
1294	
1295	    '
1296	  tables:
1297	  - name: 'Table S4: Extended Language Coverage Summary'
1298	    columns:
1299	    - resource_tier
1300	    - n_langs
1301	    - zs_auroc_median
1302	    - caclr_median
1303	    - delta
1304	    rows:
1305	    - - HIGH
1306	      - 12
1307	      - 0.786
1308	      - 0.828
1309	      - 0.042
1310	    - - MID
1311	      - 18
1312	      - 0.741
1313	      - 0.798
1314	      - 0.057
1315	    - - LOW
1316	      - 22
1317	      - 0.648
1318	      - 0.721
1319	      - 0.073
1320	  figures_description:
1321	  - 'Fig S7: World map — ZS AUROC by country/language, color gradient from red (low)
1322	    to green (high). Clear geographic pattern tracking resource availability.'
1323	  analysis: Extended coverage是camera-ready的scale argument。核心findings在52语言上robust。
1324	    Low-resource语言从CaCLR获益最多（+7.3pp vs HIGH +4.2pp）， because these languages have
1325	    the most room for improvement and CaCLR's distributional alignment compensates
1326	    for sparse pretraining representation.
1327	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9be45035-f1c6-4af3-b7ae-2e91f039727d",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "f359b38f-58bf-4e1e-bb0e-9396e960c494",
  "sourceToolAssistantUUID": "9be45035-f1c6-4af3-b7ae-2e91f039727d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T21:13:45.326Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UbooYXeYEVNJ86r8MS2JkL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f359b38f-58bf-4e1e-bb0e-9396e960c494",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWcp9JzrzDyigc1b63Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9dadda05-610f-4922-88d4-c0bbbc0e6c0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgHb6zfwSd1iLvnhmof2Wo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 67173,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 67173,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 720,
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

_source line 40 · 2026-05-20T21:13:45.616Z_

<details><summary>↩ Tool result · reported error · `toolu_01UbooYXeYEVNJ86r8MS2JkL`</summary>

```text
File content (25658 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dadda05-610f-4922-88d4-c0bbbc0e6c0c",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "8a70a489-e1ab-4ed5-97f7-d500a0d628ff",
  "toolUseResult": "Error: File content (25658 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "9dadda05-610f-4922-88d4-c0bbbc0e6c0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-20T21:13:48.940Z_

Now let me also load the research skills for context on the related work landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a70a489-e1ab-4ed5-97f7-d500a0d628ff",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWd6TLfA9QsHhJpk4uB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af095948-0d3d-46c2-ab63-aea1f814449a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wn3Xdz2DqUWPwbLGwwuYWA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19571,
      "cache_read_input_tokens": 67893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19571,
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

_source line 42 · 2026-05-20T21:13:50.968Z_

<details open><summary>🔧 Tool call — Read · `toolu_015tyVsyV66xAkMgVs3oPJcY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af095948-0d3d-46c2-ab63-aea1f814449a",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWd6TLfA9QsHhJpk4uB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "477ed4bb-ecf0-4d09-838e-b50fd01d3281",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wn3Xdz2DqUWPwbLGwwuYWA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19571,
      "cache_read_input_tokens": 67893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19571,
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

_source line 43 · 2026-05-20T21:13:50.972Z_

<details><summary>↩ Tool result · `toolu_015tyVsyV66xAkMgVs3oPJcY`</summary>

```text
1	---
2	name: xling-calib-direction-research
3	description: Research patterns from 12 papers on cross-lingual calibration and internal representations in LLMs
4	type: skill
5	---
6	
7	# Cross-Lingual Calibration — Research Patterns (12 papers)
8	
9	## Evaluation Protocol
10	
11	**Metrics**: ECE (8/12) + AUROC (5/12) + Brier (4/12). Always pair calibration with discrimination. Point estimates without CIs is field norm (6/8). High conf.
12	
13	**Benchmarks**: MMLU (5/12), Belebele for multilingual (122 langs), TruthfulQA. Transfer: ARC, HellaSwag, CSQA. High conf.
14	
15	**Models**: 3-6 models. Llama-3.1-8B + Qwen2.5-7B near-universal. Include multilingual-first model (Aya). High conf.
16	
17	## Method Trends
18	
19	**Linear probing of hidden states** (7/12): Linear classifiers suffice. AUC 0.80-0.97. Source: confidence_manifold2026. High conf.
20	
21	**Layer-wise analysis standard** (7/12): Middle-to-late layers (15-29/32) richest for xling/calibration. Final layer suboptimal for non-English. Source: zhou2025lace (24-29), civelli2026shared (xling ~15, monolingual ~30). High conf.
22	
23	**Inference-time steering** (4/12): Extract direction, add to activations, no retraining. Source: ji2025calibrating, miao2026coral, miao2026closing. Med conf.
24	
25	**Training-free methods rising** (3/12): LACE, mean shift, projection. Field moving from fine-tuning. Med conf.
26	
27	**Temperature scaling declining**: Only baseline now. High conf.
28	
29	## Cross-Paper Findings
30	
31	**Non-English ECE 5x English** (23% vs 4.6%). Structural, tied to pretraining data. Source: zhou2025lace. 3/12. High conf.
32	
33	**Cross-lingual reps are linear**: Knowledge/confidence linearly encoded across languages in middle layers. Mean shift/projection enables training-free transfer. Source: xiao2025knowledge. 4/12. High conf.
34	
35	**Correctness distributed not sparse**: SAE neuron ablation negligible (delta ECE 1.25e-4). 3-8D subspace. Source: miao2026coral, confidence_manifold2026. 2/12. Med conf.
36	
37	**Layer-depth Pareto**: English calibration improves monotonically; non-English peaks mid-late then degrades. Source: zhou2025lace, joshi2025calibration. 2/12. High conf.
38	
39	## Competitor Landscape
40	
41	**zhou2025lace** (competitor): Per-language layer ensemble, ECE 22→3%, training-free. No directional methods.
42	**joshi2025calibration** (competitor): Calibration direction in residual stream. Transfers across datasets but NOT across models. Monolingual only.
43	
44	**Our niche**: No paper combines xling transfer + calibration directions + layer-depth Pareto. joshi's direction fails cross-model. civelli shows xling/monolingual optimal layers diverge. Intersection is open.
45	
46	## Gaps
47	
48	- Cross-model direction transfer unsolved (joshi shows failure)
49	- No multilingual verbal uncertainty (ji2025calibrating English-only)
50	- MCQA-only (5/12) → generation calibration open
51	- Instance-level causal validation missing (ravisankar correlation only)
52	- Scale beyond 7-8B untested
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "477ed4bb-ecf0-4d09-838e-b50fd01d3281",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "aafc3fe3-0630-42f4-ba8b-2982dcbf9e42",
  "sourceToolAssistantUUID": "477ed4bb-ecf0-4d09-838e-b50fd01d3281",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T21:13:53.931Z_

I now have comprehensive understanding of all three paper versions and the project context. Let me produce the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aafc3fe3-0630-42f4-ba8b-2982dcbf9e42",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWdVjov5LAM8CUKLZV7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a39fe2f7-94bb-44ed-bddd-108b35fcb8b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mEQqC7PhAifyEDsQBfvA6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 87464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 45 · 2026-05-20T21:13:54.610Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SgKLZ5qH6KbQrxJUdjVDpX`</summary>

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
  "parentUuid": "a39fe2f7-94bb-44ed-bddd-108b35fcb8b8",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWdVjov5LAM8CUKLZV7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90a993c7-d41b-4bdb-89f0-55002ed0fed1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mEQqC7PhAifyEDsQBfvA6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 87464,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1130
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 87464,
          "cache_creation_input_tokens": 1130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1130,
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

_source line 46 · 2026-05-20T21:13:54.612Z_

<details><summary>↩ Tool result · `toolu_01SgKLZ5qH6KbQrxJUdjVDpX`</summary>

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
  "parentUuid": "90a993c7-d41b-4bdb-89f0-55002ed0fed1",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "9d2f430f-22c8-4694-96bf-2cd027fb0f74",
  "sourceToolAssistantUUID": "90a993c7-d41b-4bdb-89f0-55002ed0fed1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-20T21:14:03.827Z_



I have now thoroughly read all three paper versions (best/median/worst), the project framing, literature map, roadmap, and imagined experiment data. Let me produce my review.

The key observation across the three versions: they represent radically different narratives built on the same experimental skeleton. The "best" version tells a success story (CaCLR works, +3.2pp from consistency loss, p=0.003), the "median" tells a principled-negative-result story (CaCLR's consistency loss is inert, d=0.08, p=0.42; linear projection is the answer), and the "worst" tells a sobering-failure story (everything is weak, architecture-dependent, low-resource fails). The review task description aligns with the "worst" version's framing. Let me review across all three tiers, focusing on the "best" as the primary submission while noting how the narrative shifts.

Let me submit the review for the "best" tier first, then median, then worst.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d2f430f-22c8-4694-96bf-2cd027fb0f74",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWdm4YhpkYTZb2PMCsJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f1af891-b092-4d49-8792-d14240552937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKP8JebPgzMVgHDhqv3Au5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 88594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 735,
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

_source line 48 · 2026-05-20T21:15:36.496Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01QxibQ3fdMUfQ5fPMyeftjQ`</summary>

```json
{
  "project": "xling_calib_direction",
  "tier": "best",
  "dream_id": "dream_20260520T201854",
  "overall_score": "4 - Weak Accept (Borderline)",
  "report": "# Reviewer 2 (R2): Novelty, Significance, Related Work, Writing\n\n## Paper: \"Cross-Lingual Calibration via Internal Correctness Directions: Pareto Frontiers, Decomposition, and Consistency-Aligned Probes\"\n\n**Tier: BEST (CaCLR works — method contribution paper)**\n\n---\n\n## 1. Novelty Assessment\n\n### Contribution 1: Depth--Transferability Pareto Frontier\n**Verdict: Moderate novelty, incremental over existing work.**\n\nThe observation that middle layers are better for cross-lingual transfer than final layers is well-established in the cross-lingual probing literature (Pires et al. 2019; Liu & Niehues ACL 2025). Zhou et al. (LACE, 2025) already documented that non-English calibration peaks at intermediate layers. Civelli et al. (2026) showed that cross-lingual difficulty probes have optimal depth at 24-49%, directly overlapping this paper's finding.\n\nWhat IS new: (a) the specific application to *correctness* probes for *calibration*, (b) quantifying the frontier with Spearman rho per-language, and (c) the architecture-dependent shape (60% Qwen vs 50% Scout vs 75% Gemma). The architecture-dependent finding is the most novel element, but with only 3 architectures and confounded variables (MoE vs dense, model size, training data), the causal claim about \"expert routing driving language specialization\" is speculative. n=3 architectures cannot disentangle MoE routing from model size from pretraining mixture.\n\n### Contribution 2: Difficulty--Capability Decomposition\n**Verdict: Incremental, partially derivative of Civelli et al.**\n\nCivelli et al. (2026) already transferred difficulty probes cross-lingually and established that difficulty is a shared cross-lingual property. This paper's contribution is projecting out difficulty and measuring the effect on correctness transfer. The finding (+3.1pp median, p=0.006) is statistically sound but conceptually straightforward — it is a standard ablation using an existing methodology (IRT difficulty probes from Civelli) applied to a new target (correctness transfer). The resource-tier gradient (+4.1pp low vs +2.2pp high) is the most informative finding here, but the effect sizes are modest.\n\n### Contribution 3: CaCLR Method\n**Verdict: The primary novel contribution, but with caveats.**\n\nCaCLR is the paper's strongest claim to novelty. The composite loss (BCE + SB-ECE + MMD consistency) is a reasonable design, and the reported results (AUROC 0.828, +3.2pp from beta term, p=0.003, d=0.48) are meaningful. However:\n\n- The individual components are not new: BCE is standard, SB-ECE is from Karandikar et al. (2021), MMD is a standard domain adaptation tool.\n- The alpha-only variant (no consistency loss) already provides substantial improvement (+2.7pp over zero-shot), meaning the BCE+SB-ECE combination does most of the work. The marginal contribution of the MMD term is +3.2pp, which while statistically significant, raises the question of whether the complexity of requiring parallel inputs is justified over simpler alternatives.\n- CaCLR requires parallel inputs (translated items), which is a non-trivial requirement that the paper somewhat downplays. \"Zero target-language labels\" is technically true but misleading — you need a parallel corpus, which is a strong assumption for truly low-resource languages.\n\n### Contribution 4: Cross-Lingual Orthogonality\n**Verdict: Straightforward extension, low novelty.**\n\nMeasuring cosine similarity between correctness and confidence directions across languages is a direct extension of Miao & Ungar (2026). The finding that orthogonality persists (max cosine 0.062) is confirmatory rather than surprising — if the directions are orthogonal in English, and representations share cross-lingual structure at intermediate layers, orthogonality should persist. The resource-tier gradient is a minor nuance.\n\n---\n\n## 2. Significance\n\n**Who benefits?** Practitioners deploying multilingual LLMs in high-stakes settings (medical QA, legal, educational) where calibration matters.\n\n**Does it change how the community thinks?** Partially. The paper establishes that probe-based calibration is viable cross-lingually for high/mid-resource languages — this is useful but somewhat expected given prior cross-lingual probing success. The Pareto frontier finding provides actionable guidance (probe at ~50-60% depth), but this is consistent with existing literature on intermediate-layer cross-lingual alignment.\n\n**Field-level impact:** Moderate. The paper opens the cross-lingual correctness probing subfield, which is valuable. But the findings are largely confirmatory of what domain adaptation theory and cross-lingual representation analysis would predict. The CaCLR method is a reasonable but not transformative contribution.\n\n**Practical impact:** The most impactful finding is actually the linear projection result (50 pairs, +4.8pp), which is simpler and nearly as effective as CaCLR. This somewhat undermines CaCLR's practical value.\n\n---\n\n## 3. Related Work Positioning\n\n**Strengths:**\n- The differentiation from Xiao et al. (2025) is well-articulated. Knowledge boundary (input-level answerability) vs correctness (output-dependent) is a genuine distinction.\n- Coverage of probe-based calibration literature (CORAL, CCPS, Confidence Manifold, Miao & Ungar) is thorough.\n- The connection to domain adaptation theory (Ben-David et al.) is appropriate.\n\n**Weaknesses:**\n- **Missing: Ravisankar et al. (EACL 2026) DALI.** This paper provides causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. It directly supports the \"middle layers are cross-lingually aligned\" premise and should be cited. The literature map shows the authors are aware of this paper but it does not appear in the submission.\n- **Missing: Joshi et al. (EMNLP 2025).** Calibration direction in the residual stream, layer-wise evolution. Directly relevant to the Pareto frontier finding.\n- **Missing: Ji et al. (EMNLP 2025).** Verbal uncertainty as a linear feature — relevant to the orthogonality analysis.\n- **Underselling Civelli et al.** The paper uses Civelli's methodology (IRT difficulty probes, cross-lingual transfer) extensively but does not give sufficient credit. The decomposition contribution relies heavily on their framework.\n- **LACE (Zhou et al. 2025) comparison is surface-level.** LACE achieves ECE reduction from 22% to 3% with per-language layer ensembles. The paper should compare CaCLR's ECE reduction quantitatively against LACE, not just note that LACE \"requires target-language labels.\"\n- The bibliography has only 12 entries, which is thin for a top-venue paper covering this many subfields. Several citations are incomplete (empty \\cite{} in the introduction).\n\n**Differentiation quality:**\n- From Xiao et al.: Strong. The mean-shift rank-invariance proof is a clean theoretical distinction.\n- From CORAL: Adequate. Cross-lingual vs cross-task is clear.\n- From LACE: Weak. The requirement comparison (zero labels vs per-language labels) is noted but quantitative comparison is absent.\n\n---\n\n## 4. Writing Quality\n\n**Clarity:** Generally good. The causal chain structure (Pareto → Decomposition → CaCLR → Orthogonality) provides narrative coherence. The mean-shift rank-invariance argument is elegantly presented.\n\n**Organization:** Well-structured but dense. 13 tables in 11 pages is heavy. Some tables could be consolidated or moved to appendix.\n\n**Density:** The abstract packs too many numbers (AUROC values, pp improvements, correlation coefficients, cosine thresholds). An abstract should convey the key insight, not serve as a results summary. The first sentence of the abstract is strong; by the fifth sentence, it reads like a compressed results table.\n\n**Issues:**\n- Empty citations in the introduction (\\cite{}) — this is a draft artifact but unacceptable for submission.\n- The paper oscillates between reporting AUROC and ECE without consistently connecting them. The headline claim is about ECE reduction (3.5% over temperature scaling) but most results tables report AUROC.\n- \"CaCLR-trained probes reduce non-English ECE by 3.5% over temperature scaling\" — is this 3.5 percentage points or 3.5% relative? The paper uses both \"pp\" and \"%\" inconsistently.\n- The CKA analysis section (5.5) is interesting but reads as post-hoc rationalization rather than a priori prediction. The paper would be stronger if CKA predictions were stated before CaCLR results.\n- Discussion section is too short (3 paragraphs). The \"why architecture matters\" paragraph speculates about expert routing without evidence beyond correlation.\n\n---\n\n## 5. Strengths\n\n1. **First systematic cross-lingual correctness probe evaluation.** Despite the incremental nature of individual findings, the comprehensive evaluation (3 architectures, 20+ languages, 5 transfer conditions, 3 benchmarks) fills a genuine gap. No prior work has done this.\n\n2. **Mean-shift rank-invariance theorem.** Simple, clean, and practically important. It prevents the community from wasting effort on a provably inert method under standard pipelines. Well-differentiated from Xiao et al.\n\n3. **Rigorous statistical methodology.** Bootstrap CIs, paired permutation tests, Cohen's d, control tasks (Hewitt & Liang) — this is above the field median for statistical rigor in probing papers.\n\n4. **Actionable practical guidance.** The paper provides concrete recommendations: probe at 50-60% depth, use CaCLR at mid-depth layers, use linear projection when geometric misalignment dominates. Practitioners can immediately apply these.\n\n5. **CKA mechanistic analysis.** While not the strongest contribution, the CKA--transfer correlation (r=0.82) provides a useful diagnostic tool. The distinction between distributional vs geometric misalignment is insightful.\n\n---\n\n## 6. Weaknesses\n\n1. **(Moderate) Limited novelty of individual contributions.** Each contribution is incremental: the Pareto frontier extends known cross-lingual probing findings to correctness; the decomposition applies Civelli's methodology to a new target; CaCLR combines existing components (BCE, SB-ECE, MMD); orthogonality is a direct extension of Miao & Ungar. The paper's value is in the comprehensive evaluation, not in any single novel finding. For a top venue, I expect at least one contribution that is genuinely surprising or that could not have been predicted from existing work.\n\n2. **(Moderate) CaCLR's marginal value over simpler alternatives.** Linear projection with 50 pairs achieves AUROC 0.812 vs CaCLR's 0.828 — a 1.6pp gap. Linear projection requires no hyperparameter tuning, no SB-ECE implementation, no MMD computation, and no parallel corpus beyond the 50 pairs. The paper argues CaCLR requires \"zero target-language labels\" but needs parallel inputs, while linear projection needs \"50 parallel pairs\" — these requirements are comparable in practice. The paper should explicitly argue why CaCLR is preferable to linear projection + temperature scaling.\n\n3. **(Moderate) Architecture-dependent claims from n=3.** The paper makes strong claims about MoE vs dense architecture effects on the Pareto frontier, but with only 3 models (2 MoE, 1 dense), these are observations, not validated causal claims. Model size (235B vs 109B vs 31B), training data, tokenizer, and architecture type are confounded. The \"expert routing drives language specialization\" narrative is plausible but untestable from this data.\n\n4. **(Minor) Incomplete citations and thin bibliography.** Empty \\cite{} marks in the introduction, only 12 references for a paper spanning calibration, cross-lingual transfer, domain adaptation, probing methodology, and representation similarity. Missing several relevant papers (DALI, Joshi et al., Ji et al.).\n\n5. **(Minor) ECE metric reporting is inconsistent.** The headline claim is about ECE (3.5% reduction), but most experiments report AUROC. The connection between AUROC improvement and ECE improvement is not systematically established. Temperature scaling is the ECE baseline, but CaCLR also optimizes ECE during training (SB-ECE term), making the comparison somewhat unfair — CaCLR is directly optimizing the evaluation metric.\n\n---\n\n## 7. Questions for Authors\n\n**Q1 (Novelty/Positioning):** Given that Civelli et al. (2026) already showed that cross-lingual difficulty probes have architecture-dependent optimal depth at 24-49%, and Zhou et al. (LACE, 2025) showed intermediate layers are optimal for non-English calibration, what specific aspect of the Pareto frontier finding is not predictable from these prior results? Please articulate the delta beyond \"we did it for correctness probes.\"\n\n**Q2 (Method Justification):** Linear projection with 50 pairs achieves 98% of 200-pair performance and AUROC 0.812 (Table 7). CaCLR achieves 0.828 but requires parallel inputs for all training data, SB-ECE implementation, and beta tuning. Under what practical scenario would a practitioner choose CaCLR over linear projection? What is the cost-benefit analysis?\n\n**Q3 (Architecture Claims):** The paper attributes the Pareto frontier shape difference between MoE and dense models to \"expert routing creating discrete language specialization.\" This is tested with n=1 dense model and n=2 MoE models, with model size as a major confound (31B vs 109-235B). How do you rule out that model scale, rather than architecture type, drives the frontier shape difference?\n\n---\n\n## 8. Score\n\n**4 / 6 — Weak Accept (Borderline)**\n\nThe paper fills a genuine gap (first systematic cross-lingual correctness probe evaluation) with rigorous methodology and provides actionable findings. The mean-shift rank-invariance theorem is clean and useful. However, novelty is incremental across all four contributions, and CaCLR's marginal advantage over simpler linear projection weakens the method contribution. The architecture claims are underpowered. For a top venue at ~25% acceptance rate, this is borderline — the comprehensive evaluation and statistical rigor push it toward accept, but the limited novelty of individual contributions and the thin bibliography pull it back.\n\nThe paper would be strengthened by: (1) explicitly positioning CaCLR's advantage over linear projection with a cost-benefit analysis, (2) acknowledging the incremental nature of the Pareto frontier more honestly, (3) expanding the bibliography and citations, and (4) either adding a 4th architecture to strengthen the MoE/dense contrast or softening those claims.\n\n## 9. Confidence\n\n**4 / 5 — High confidence.** I am familiar with the cross-lingual probing, calibration, and domain adaptation literatures. I have read the key prior works (Xiao et al., Civelli et al., LACE, CORAL, Miao & Ungar) and can assess the novelty claims with reasonable authority. My uncertainty is primarily about whether the community will value the comprehensive evaluation enough to offset the incremental novelty — reasonable reviewers could disagree on this tradeoff.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f1af891-b092-4d49-8792-d14240552937",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWdm4YhpkYTZb2PMCsJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77f08975-30cd-4c9a-b9c1-9ba96875a6c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKP8JebPgzMVgHDhqv3Au5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 88594,
      "output_tokens": 4093,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 735
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4093,
          "cache_read_input_tokens": 88594,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 735,
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

_source line 49 · 2026-05-20T21:15:39.685Z_

<details><summary>↩ Tool result · `toolu_01QxibQ3fdMUfQ5fPMyeftjQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md\", \"dream_id\": \"dream_20260520T201854\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77f08975-30cd-4c9a-b9c1-9ba96875a6c6",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "d80da739-2207-4018-bf52-5ad0196c6cd3",
  "sourceToolAssistantUUID": "77f08975-30cd-4c9a-b9c1-9ba96875a6c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T21:16:43.559Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_016bpYMBAHDsEnE9HTyMfYRd`</summary>

```json
{
  "project": "xling_calib_direction",
  "tier": "median",
  "dream_id": "dream_20260520T201854",
  "overall_score": "3 - Weak Reject",
  "report": "# Reviewer 2 (R2): Novelty, Significance, Related Work, Writing\n\n## Paper: \"Cross-Lingual Correctness Probes Reveal a Depth--Transferability Pareto Frontier: Distributional Matching Fails Where Linear Projection Succeeds\"\n\n**Tier: MEDIAN (CaCLR fails — principled negative result + linear projection as constructive alternative)**\n\n---\n\n## 1. Novelty Assessment\n\n### Contribution 1: Pareto Frontier\n**Verdict: Low-to-moderate novelty.**\n\nSame assessment as the best-tier version. The depth-transferability tradeoff is documented in prior work (Civelli et al. 2026, LACE 2025). The median version's numbers are weaker: rho ranges from -0.51 to -0.58, with substantial per-language variance (sigma_rho 0.12-0.16). On Llama 4 Scout, Table 2 shows the per-language rho range spans [-0.82, -0.21] — meaning some languages show strong negative correlation while others show almost none. This weakens the \"Pareto frontier\" framing considerably: it is not a universal phenomenon but a language-and-architecture-dependent tendency.\n\nThe framing as a \"Pareto frontier\" is arguably misleading when the median rho is only -0.52. A Pareto frontier implies a clean tradeoff; what the data shows is a noisy negative tendency that is sometimes absent. The paper would be more honest to call it a \"depth-transfer tradeoff tendency.\"\n\n### Contribution 2: CKA Mechanistic Explanation\n**Verdict: Moderate novelty, but r=0.58 is not compelling.**\n\nCKA explaining 34% of transfer variance is meaningful but leaves 66% unexplained. The comparison with MMD (6% variance explained) is the strongest point — it demonstrates that misalignment is geometric rather than distributional. However, CKA is a coarse measure (it compares entire representation matrices, not correctness-specific subspaces), and r=0.58 is a moderate correlation that many reviewers would not consider \"mechanistic explanation.\"\n\nThe qualitative insight (geometric rotation vs distributional shift) is valuable and well-argued. But the paper oversells this as a \"mechanistic explanation\" when it is more accurately a \"suggestive correlational analysis.\"\n\n### Contribution 3: CaCLR Negative Result\n**Verdict: The paper's central contribution, but faces the \"is it surprising?\" test.**\n\nCaCLR's consistency loss being inert (d=0.08, p=0.42) is a clean negative result. The paper frames this as principled because it is predicted by the CKA geometric analysis. This is the strongest contribution of the median version.\n\nHowever: Is this surprising? MMD-based domain adaptation is known to fail when the source and target domains have different geometric structure (not just distributional shift). The domain adaptation community has known since Ganin et al. (2016) and subsequent work that marginal distribution matching is insufficient when conditional distributions differ. Framing this as a novel finding requires the reader to not be familiar with the domain adaptation literature.\n\nThe constructive alternative (linear projection with 50-100 pairs) is useful but is essentially VecMap/MUSE applied to sentence-level correctness representations. The sample efficiency finding (~70 pairs to saturation) is consistent with existing cross-lingual alignment literature.\n\n### Contribution 4: Cross-Lingual Orthogonality\n**Verdict: Same as best tier — confirmatory extension.**\n\nMax cosine rises to 0.10 in this version (vs 0.062 in best), with sw reaching 0.098. The resource-tier gradient is more pronounced. The finding remains confirmatory.\n\n---\n\n## 2. Significance\n\n**Reduced compared to best tier.** Without CaCLR as a working method, the paper's contributions are:\n- A systematic evaluation showing cross-lingual probe transfer works for high-resource but not low-resource languages (somewhat expected)\n- A principled negative result about distributional matching (valuable but narrow)\n- A recommendation to use linear projection (useful but not novel — this is what VecMap/MUSE already do)\n\nThe paper's significance rests on whether the community considers \"MMD-based distributional matching doesn't work for correctness probe transfer, here's why, and use linear projection instead\" to be a sufficient contribution. For a top venue, I would argue this is below the bar — the negative result, while clean, is not deeply surprising, and the constructive alternative is borrowed from existing methods.\n\n---\n\n## 3. Related Work Positioning\n\nMostly the same issues as the best tier, with one important addition:\n\n- **The negative result needs stronger positioning against domain adaptation theory.** The paper invokes Ben-David et al. (2010) H-divergence framework, but the failure of marginal distribution matching when conditional distributions differ is better explained by more recent theoretical work (Zhao et al. 2019 \"On learning invariant representations for domain adaptation\"). The paper should engage with this literature to strengthen the theoretical grounding of the negative result.\n\n- The bibliography is more complete in this version (21 entries vs 12), which is a significant improvement. Hewitt & Liang, Voita & Titov, and several additional references are properly cited.\n\n- The DALI paper (Ravisankar et al. 2026) is still missing.\n\n---\n\n## 4. Writing Quality\n\n**The median version is better written than the best version.** Specific improvements:\n- More honest framing: \"principled negative result\" rather than overselling CaCLR\n- Better organized: the CKA analysis precedes the CaCLR results, making the prediction-then-test structure clearer\n- The discussion section properly explains \"Why Does Distributional Matching Fail?\" — this is the paper's strongest prose\n- Statistical reporting is more consistent (bootstrap CIs, permutation tests, Cohen's d throughout)\n\n**Issues:**\n- The title is long and awkward: \"Cross-Lingual Correctness Probes Reveal a Depth--Transferability Pareto Frontier: Distributional Matching Fails Where Linear Projection Succeeds\" — this reads as two papers forced into one title\n- The abstract is still too dense but better organized than the best version\n- Some results are only in appendices that should be in the main text (cross-benchmark generalization, control task selectivity)\n\n---\n\n## 5. Strengths\n\n1. **Clean negative result with mechanistic explanation.** The CaCLR beta inertness is demonstrated rigorously (3 OOM sweep, d=0.08, p=0.42) and the CKA-based geometric explanation is coherent. This is how negative results should be reported.\n\n2. **Honest framing.** The paper does not oversell. The limitations section acknowledges weak selectivity for low-resource languages. The discussion explains rather than speculates.\n\n3. **Strong statistical methodology.** Same as best tier — above field median.\n\n4. **Constructive alternative.** Rather than stopping at \"CaCLR doesn't work,\" the paper identifies linear projection as the practical solution and characterizes its sample efficiency.\n\n---\n\n## 6. Weaknesses\n\n1. **(Major) Insufficient novelty for a top venue.** The negative result (distributional matching fails for cross-lingual correctness probe transfer) is clean but unsurprising given the domain adaptation literature. The positive finding (linear projection works) is borrowed from existing methods. The Pareto frontier extends known findings. For ~25% acceptance rate, I expect the paper to teach the community something it could not have predicted.\n\n2. **(Moderate) The \"Pareto frontier\" framing overstates the finding.** Median rho of -0.52 with sigma_rho 0.12-0.16 and per-language range [-0.82, -0.21] does not constitute a \"frontier\" — it is a noisy tendency. On Llama 4 Scout, the rho median is only -0.54, meaning roughly half the per-language correlations are weaker than -0.54 and some are near zero or positive. The paper should reframe this as a \"depth-transfer tradeoff\" rather than a \"Pareto frontier.\"\n\n3. **(Moderate) CKA analysis is correlational, not mechanistic.** r=0.58, explaining 34% of variance, is presented as a \"mechanistic explanation\" throughout the paper. This is a correlation. A mechanistic explanation would identify the specific geometric transformation (rotation, scaling) at each layer and show that correcting it restores transfer performance. The paper gestures at this (subspace angle analysis showing 15-35 degree rotation) but does not follow through with a controlled experiment.\n\n4. **(Minor) Limited practical impact of the negative result.** Who was planning to use MMD-based consistency loss for cross-lingual probe transfer? The paper addresses a method (CaCLR) that the authors themselves proposed. Showing that your own proposed method doesn't work is less impactful than showing that a widely-used method doesn't work.\n\n5. **(Minor) Gemma 4 results are thin.** The dense architecture is relegated to a summary table and brief paragraph. For the MoE-vs-dense contrast to be compelling, the dense model needs the same full treatment (per-language results, CKA analysis, all transfer conditions).\n\n---\n\n## 7. Questions for Authors\n\n**Q1:** The domain adaptation community has known since at least Zhao et al. (2019) that marginal distribution matching fails when conditional distributions differ across domains. How is CaCLR's failure a novel finding rather than a specific instance of a known general principle? What does this paper add to the theoretical understanding beyond confirming the prediction?\n\n**Q2:** The CKA-transfer correlation is r=0.58, explaining 34% of variance. The paper calls this a \"mechanistic explanation.\" Would you accept r=0.58 as a \"mechanistic explanation\" if it appeared in a paper you were reviewing? What fraction of transfer variance would need to be explained to justify the \"mechanistic\" label?\n\n**Q3:** Linear projection with 50-100 pairs is your recommended solution. How does this differ from applying VecMap/MUSE at the sentence level? Is there any technical novelty in the projection method itself, or is the contribution purely that \"existing alignment methods work for this new task\"?\n\n---\n\n## 8. Score\n\n**3 / 6 — Weak Reject**\n\nThe paper is methodologically rigorous and honestly framed. The negative result is clean. However, for a top venue at ~25% acceptance, I need novelty that teaches the community something non-obvious. The negative result (distributional matching fails) is predictable from domain adaptation theory. The positive result (linear projection works) is borrowed from existing methods. The Pareto frontier finding extends known cross-lingual probing results without a surprising twist. The comprehensive evaluation is valuable but insufficient to compensate for limited novelty.\n\nThe paper would be better suited for a workshop, findings track, or a venue that specifically values systematic empirical evaluation and negative results (e.g., NeurIPS Datasets and Benchmarks track, or a ReScience-style venue).\n\n## 9. Confidence\n\n**4 / 5 — High confidence.** Same basis as best-tier review. The novelty assessment is where I am most confident — I can trace each contribution to its antecedents in the literature.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d80da739-2207-4018-bf52-5ad0196c6cd3",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWmW5sJKpxEMXzJLWns",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2906510-c9e9-4555-8d14-02a77d4da8ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KAzZXQVjCP3zNyf8YRHLsH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4224,
      "cache_read_input_tokens": 89329,
      "output_tokens": 2790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2790,
          "cache_read_input_tokens": 89329,
          "cache_creation_input_tokens": 4224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4224,
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

_source line 51 · 2026-05-20T21:16:44.299Z_

<details><summary>↩ Tool result · `toolu_016bpYMBAHDsEnE9HTyMfYRd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_report.md\", \"dream_id\": \"dream_20260520T201854\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2906510-c9e9-4555-8d14-02a77d4da8ec",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "59747d8f-ae55-4104-9b90-cbe2607805b4",
  "sourceToolAssistantUUID": "d2906510-c9e9-4555-8d14-02a77d4da8ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T21:18:05.367Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_011FQZA4T7915yPufw8dxiwN`</summary>

```json
{
  "project": "xling_calib_direction",
  "tier": "worst",
  "dream_id": "dream_20260520T201854",
  "overall_score": "2 - Reject",
  "report": "# Reviewer 2 (R2): Novelty, Significance, Related Work, Writing\n\n## Paper: \"Does Probe-Based Calibration Work Beyond English? A Systematic Investigation Across 3 Architectures and 52 Languages\"\n\n**Tier: WORST (Sobering negative results, everything is weak/inconclusive)**\n\n---\n\n## 1. Novelty Assessment\n\n### Contribution 1: Mean-Shift Rank-Invariance Theorem\n**Verdict: Technically correct but trivially obvious.**\n\nThe \"theorem\" states: under StandardScaler + logistic regression, subtracting a constant vector from all inputs adds a constant to all logits, preserving AUROC. This is a one-line consequence of AUROC being rank-invariant and logistic regression being a linear model. Any graduate student familiar with AUROC and linear classifiers would derive this in minutes. Calling it a \"theorem\" (with formal Theorem 1 environment) oversells what is a straightforward observation.\n\nThe distinction from Xiao et al. (2025) is valid — they use accuracy (threshold-dependent), this paper uses AUROC (rank-invariant). But the observation that mean-shift preserves rankings under linear models is not a contribution; it is a sanity check that should be a footnote, not a named theorem.\n\n### Contribution 2: Resource-Tier Taxonomy\n**Verdict: Descriptive, not explanatory. Low novelty.**\n\nThe finding that high-resource languages transfer better than low-resource languages is entirely predicted by domain adaptation theory (Ben-David et al. 2010) and by the pretraining data distribution. The specific numbers (7-8pp drop for high, 10-12pp for mid, 13-20pp for low) are useful descriptive statistics but do not constitute a novel finding. The \"28% capacity artifacts\" finding from control tasks is the most interesting element but is presented as a qualifier rather than a finding.\n\nThe 52-language extension is the paper's strongest empirical contribution, but scaling from 20 to 52 languages does not change any qualitative conclusion. The very-low-resource tier (0% pass rate) is expected and does not require 52 languages to establish.\n\n### Contribution 3: Practical Recommendation (Few-shot is the only path)\n**Verdict: This is not a contribution; it is a conclusion.**\n\n\"Few-shot adaptation with 25-100 labels is the only viable path\" is a reasonable conclusion from the evidence but is not itself a novel contribution. It could be predicted a priori: if zero-shot transfer fails and distributional matching fails, labeled data is the remaining option. This is the default answer in any transfer learning scenario.\n\n### Additional Findings\n- **CaCLR failure (d=0.04, p=0.71):** A negative result about the authors' own proposed method. See weakness discussion below.\n- **Architecture-dependent Pareto (rho -0.18 to -0.44, tau=0.33):** The cross-architecture agreement (tau=0.33) is extremely low. On Llama 4 Scout, the per-language rho median is -0.12 with sign consistency 0.53 — literally a coin flip. The paper acknowledges this but still frames it as a \"Pareto frontier,\" which is misleading.\n- **Difficulty decomposition inconclusive (-0.5pp, barely above random):** The paper honestly reports this as inconclusive. Good.\n- **CKA analysis weak (r=0.32):** Combined r=0.32 explains 10% of variance. \"Suggestive but not convincing\" is the paper's own assessment.\n- **Orthogonality with outliers (up to 0.172):** Yoruba's cosine of 0.172 weakens the \"universality\" claim significantly, especially since it is a low-resource language where the finding matters most.\n\n---\n\n## 2. Significance\n\n**Very limited.** The paper's honest subtitle could be: \"We tried to extend probe-based calibration to non-English languages and mostly failed.\" The three claimed contributions are: (1) a trivial mathematical observation, (2) a descriptive taxonomy confirming theoretical predictions, and (3) a conclusion that labeled data is needed. None of these advances the field.\n\nThe \"sobering empirical reality check\" framing is honest, and the community does benefit from knowing that zero-shot cross-lingual probe transfer is unreliable. But the bar for a top venue negative-results paper is high: the paper should either (a) close a line of research with definitive evidence, or (b) identify the precise mechanism of failure in a way that suggests a fix. This paper does neither:\n- It does not definitively close the line (CaCLR might work with better design; the paper only tests one distributional matching approach)\n- It does not identify a precise mechanism (CKA r=0.32 is too weak; \"geometric misalignment\" is named but not characterized)\n\n**Who benefits?** Researchers who might otherwise waste time on zero-shot cross-lingual probe transfer without labels. This is a valid but narrow audience.\n\n---\n\n## 3. Related Work Positioning\n\n**The worst-case version has the most honest positioning** of the three tiers, which is a credit to the authors. Specific observations:\n\n- Xiao et al. differentiation is handled well. The knowledge-boundary vs correctness distinction is clear, and the paper honestly notes that Xiao's success does not predict this paper's results.\n- Civelli et al. is properly acknowledged as providing the methodology for the (inconclusive) decomposition analysis.\n- The \"predictable from domain adaptation theory\" concern is addressed in the paper_framing.md but not adequately in the submission itself. The paper claims the novel findings are (a) architecture-dependent Pareto shape and (b) CaCLR failure — but (a) is measured with n=3 models and (b) is a negative result about the authors' own method.\n\n**Missing references** remain (DALI, Joshi et al., Ji et al.) as in the other tiers.\n\n**Critical positioning gap:** The paper does not engage with the question \"what would a positive result look like?\" If the paper had found strong zero-shot transfer with CaCLR, what would the contribution be? The answer is: \"a method for cross-lingual calibration without labels.\" Since that method failed, the paper needs to argue that the failure itself is instructive. The argument (geometric misalignment, not distributional) is made but supported weakly (r=0.32).\n\n---\n\n## 4. Writing Quality\n\n**The worst version is paradoxically the best-written.** The honest framing avoids overselling. The \"three surviving contributions\" structure is refreshingly candid. The per-language table (Table 5) with individual Spearman rho values, including non-significant ones, is exemplary transparency.\n\n**Issues:**\n- The title as a question (\"Does Probe-Based Calibration Work Beyond English?\") sets up an expectation that the paper will answer it. The answer is \"sort of, for high-resource languages, if you have 25-100 labels.\" This is anticlimactic and the title overpromises.\n- 13 tables is still excessive. The paper reads like an experiment log rather than a narrative. Several tables (beta sweep, INT8 validation, linear projection pairs) belong in appendix.\n- The Analysis section has a valuable Q&A structure but the answers are equivocal. \"Three factors compound\" for low-resource failure is hand-waving without quantitative attribution.\n- Some findings that ARE interesting (28% capacity artifacts in low-resource, Yoruba selectivity below control) are buried in subsections rather than featured prominently. These findings about the limits of probing methodology are potentially more impactful than the transfer results themselves.\n\n---\n\n## 5. Strengths\n\n1. **Exceptional honesty.** The paper does not oversell inconclusive findings. The decomposition is reported as inconclusive. The CKA analysis is called \"suggestive but not convincing.\" The \"three surviving contributions\" framing acknowledges that much of the investigation yielded null results. This intellectual honesty is rare and commendable.\n\n2. **Comprehensive experimental coverage.** 3 architectures, 52 languages, 5 transfer conditions, 3 benchmarks, control tasks, INT8 validation, probe complexity comparison. The thoroughness is impressive even if the findings are largely negative.\n\n3. **Control task methodology.** The Hewitt & Liang control tasks revealing 28% capacity artifacts in low-resource languages is a methodologically important finding that the community should be aware of. This is potentially the most impactful insight in the paper, despite not being claimed as a contribution.\n\n4. **Statistical rigor.** Consistent bootstrap CIs, permutation tests, Cohen's d. The non-significant results are properly flagged as non-significant.\n\n---\n\n## 6. Weaknesses\n\n1. **(Major) No novel contribution clears the bar.** The mean-shift theorem is trivial. The resource-tier taxonomy is descriptive and predictable. The practical recommendation is a conclusion, not a contribution. The CaCLR negative result is about the authors' own method. The Pareto frontier finding is noisy (rho as weak as -0.18) and architecture-dependent (tau=0.33). For a top venue, I need at least one finding that could not have been predicted before running the experiments.\n\n2. **(Major) The paper tests CaCLR and reports its failure, but CaCLR is the authors' own design.** This creates a circular contribution: \"We propose X, X fails, the failure is our contribution.\" This would be acceptable if CaCLR represented the consensus approach from the field, but MMD-based consistency loss is only one of many possible alignment strategies. The paper does not test adversarial domain adaptation, optimal transport, contrastive alignment, or any alternatives. Closing the \"distributional matching path\" requires testing more than one distributional matching method.\n\n3. **(Major) The paper answers its title question (\"Does probe-based calibration work beyond English?\") with \"yes, for high-resource languages with 25-100 labels.\" This is equivalent to saying \"supervised methods work with supervision.\" The zero-label dream being \"closed\" is the more interesting claim, but it is only tested with one zero-label method (CaCLR). Mean-shift is proven inert (good), but only one non-trivial zero-label approach is attempted before declaring the path closed.\n\n4. **(Moderate) Pareto frontier framing is misleading at worst-case effect sizes.** On Llama 4 Scout, rho=-0.18, sign consistency 0.53. This is noise, not a frontier. The paper acknowledges this but continues to use \"Pareto frontier\" terminology throughout. The honest framing would be: \"We observe a depth-transfer tradeoff on Qwen3 (rho=-0.38) and Gemma4 (rho=-0.44) but not on Llama 4 Scout (rho=-0.18).\"\n\n5. **(Minor) The paper is too long for its contributions.** 11 pages, 13 tables, 12 subsections in Results. Many subsections report null or inconclusive findings. A tighter paper that focused on the resource-tier taxonomy + control task artifacts + few-shot recommendation would be more impactful at 8 pages.\n\n---\n\n## 7. Questions for Authors\n\n**Q1:** You declare the \"zero-label dream closed\" based on testing one zero-label method (CaCLR with MMD). Have you considered that other alignment paradigms — optimal transport, contrastive learning, adversarial domain adaptation — might succeed where MMD fails? On what basis do you generalize from \"MMD fails\" to \"zero-label transfer fails\"?\n\n**Q2:** The control task finding (28% of low-resource language-layer pairs have selectivity below 8pp, Swahili and Yoruba below control AUROC at the English-optimal layer) seems like the most important methodological contribution. It suggests that a significant fraction of published probing results for low-resource languages may be artifacts. Why is this not the paper's central contribution?\n\n**Q3:** On Llama 4 Scout, the Pareto frontier essentially does not exist (rho=-0.18, sign consistency 0.53). Yet the paper's title and framing center on the Pareto frontier. How do you justify this framing when one of your three architectures does not exhibit the phenomenon?\n\n---\n\n## 8. Score\n\n**2 / 6 — Reject**\n\nThe paper is methodologically sound and commendably honest, but lacks a novel contribution sufficient for a top venue. The claimed contributions are either trivially obvious (mean-shift theorem), descriptive and predictable (resource-tier taxonomy), or conclusions rather than findings (few-shot recommendation). The most interesting findings (control task artifacts in low-resource probing, Llama 4 Scout NOT exhibiting a Pareto frontier) are buried rather than centered. The paper would benefit from a fundamental reframing: instead of \"cross-lingual probe transfer mostly fails,\" center the story on \"probing methodology breaks down for low-resource languages\" — the control task analysis suggests this is where the genuinely novel insight lies.\n\nThe experimental thoroughness and statistical rigor are substantially above the field median, but rigor cannot substitute for novelty at a top venue. I encourage the authors to reframe and resubmit, potentially to a findings track or a venue that values systematic empirical evaluation.\n\n## 9. Confidence\n\n**4 / 5 — High confidence.** The novelty assessment is straightforward: I can trace each claimed contribution to existing work or to standard reasoning from first principles. The writing and methodology assessments are within my expertise. My main uncertainty is whether the \"comprehensive negative result\" format has more value than I assign — some communities do reward thorough null results more than I do.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59747d8f-ae55-4104-9b90-cbe2607805b4",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWrGNFqobYThgjVnFXA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "903b5a25-4526-474d-9fc4-159a63a4663c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLaMvVPKqkYtCAMxexgzB2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2918,
      "cache_read_input_tokens": 93553,
      "output_tokens": 3355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2918
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3355,
          "cache_read_input_tokens": 93553,
          "cache_creation_input_tokens": 2918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2918,
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

_source line 53 · 2026-05-20T21:18:06.086Z_

<details><summary>↩ Tool result · `toolu_011FQZA4T7915yPufw8dxiwN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/review_report.md\", \"dream_id\": \"dream_20260520T201854\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "903b5a25-4526-474d-9fc4-159a63a4663c",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "ae89d08b99e7d703f",
  "type": "user",
  "uuid": "e5f17317-7070-411c-8171-52aaee05ccef",
  "sourceToolAssistantUUID": "903b5a25-4526-474d-9fc4-159a63a4663c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-20T21:18:20.667Z_

All three reviews have been submitted. Here is a summary of what was produced:

## Review Summary (R2: Novelty, Significance, Related Work, Writing)

**Three reviews submitted** for dream `dream_20260520T201854`, one per tier:

### Best Tier (CaCLR works): **4/6 Weak Accept (Borderline)**
- CaCLR is the strongest novel contribution but its marginal advantage over linear projection (+1.6pp) is slim given its complexity
- Pareto frontier extends known cross-lingual probing findings (Civelli et al., LACE) with moderate novelty
- Mean-shift rank-invariance theorem is clean and useful
- Difficulty decomposition and orthogonality extensions are incremental
- Key concern: n=3 architectures cannot disentangle MoE vs dense vs model size

### Median Tier (CaCLR fails, linear projection succeeds): **3/6 Weak Reject**
- The negative result is clean (d=0.08, p=0.42) but predictable from domain adaptation theory (Zhao et al. 2019)
- Constructive alternative (linear projection) is borrowed from VecMap/MUSE
- "Pareto frontier" label is misleading when median rho is only -0.52 with high variance
- CKA "mechanistic explanation" oversold at r=0.58 (34% variance explained)
- Better suited for findings track or workshop

### Worst Tier (Everything weak/inconclusive): **2/6 Reject**
- Mean-shift theorem is trivially obvious
- Resource-tier taxonomy confirms theoretical predictions without novel insight
- CaCLR failure is about the authors' own method, tested with only one alignment paradigm
- Pareto frontier absent on Llama 4 (rho=-0.18)
- Most interesting finding (28% capacity artifacts in low-resource probing) is buried, not centered
- Suggested reframe: center on "probing methodology breaks for low-resource languages"

### Cross-cutting weaknesses flagged across all tiers:
1. Missing references: DALI (Ravisankar et al. 2026), Joshi et al. (2025), Ji et al. (2025)
2. Architecture claims underpowered at n=3 with confounded variables
3. ECE vs AUROC reporting inconsistency
4. 13 tables in 11 pages is excessive

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5f17317-7070-411c-8171-52aaee05ccef",
  "isSidechain": true,
  "agentId": "ae89d08b99e7d703f",
  "requestId": "req_011CbEWxJ4sDbFM2EL6Py1mE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b49ddb1-301a-483d-85c9-9fe6c6f8f458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HK1Pw3tUoxr9AsUrDfogoV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3483,
      "cache_read_input_tokens": 96471,
      "output_tokens": 572,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3483
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 572,
          "cache_read_input_tokens": 96471,
          "cache_creation_input_tokens": 3483,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3483,
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
