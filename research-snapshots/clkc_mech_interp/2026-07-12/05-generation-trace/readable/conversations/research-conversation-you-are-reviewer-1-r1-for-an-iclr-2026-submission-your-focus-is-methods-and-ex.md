# Research conversation: You are Reviewer 1 (R1) for an ICLR 2026 submission. Your focus is **Methods and Experiments**. Provide a thorough, inde

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac770b6258a8deee7.jsonl`
- **Structured JSON:** [`ec831f42055eba481293.json`](../../sessions/ec/ec831f42055eba481293.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-22T03:31:34.500Z_

You are Reviewer 1 (R1) for an ICLR 2026 submission. Your focus is **Methods and Experiments**. Provide a thorough, independent review.

## ICLR 2026 Rating Scale
Overall rating uses {0, 2, 4, 6, 8, 10}:
- 10: Outstanding (top 1-2%)
- 8: Strong Accept (clear accept, significant contribution)
- 6: Weak Accept (marginally above threshold)
- 4: Weak Reject (marginally below threshold)
- 2: Strong Reject (clear reject)
- 0: Very strong reject

Soundness, Presentation, Contribution each rated 1-4.
Confidence rated 1-5.

## Paper Summary
**Title:** "Architecture-Dependent Cross-Lingual Conflict Processing: Probing Knowledge Conflict Signals in Multilingual LLMs"

The paper investigates how multilingual LLMs internally encode knowledge conflict signals and whether these encodings transfer across languages. Using residual stream probing on three model architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B) with English–Chinese parallel instances from ConflictQA, the paper finds:

1. **C1 (Detectability):** Conflict signals are robustly detectable via linear probes within each language across all three architectures (balanced accuracy 68–77%, all p < 0.001).
2. **C2 (Asymmetry is architecture-dependent):** ZH→EN transfer exceeds EN→ZH by ~7pp in Llama and Qwen, but collapses to +1.0pp in Gemma-2-9B, suggesting this is architecture/training-data-dependent.
3. **C3 (CKA layer analysis):** CKA between EN/ZH decreases monotonically across layers; probe peaks after language transition point.

Additional experiments: COMET translation quality ablation, MLP vs linear probes, label noise robustness, representation steering (weak results).

## Full Paper Content (10 pages)

**Abstract:** When multilingual LLMs encounter knowledge conflicts, how is the conflict signal encoded internally, and does this encoding transfer across languages? They probe residual stream activations on 3 architectures using EN-ZH parallel ConflictQA instances. Findings: (1) conflict detectable within-language 68-77% balanced acc, cross-lingual 63-72%; (2) asymmetry ~7pp in Llama/Qwen collapses to +1.0pp in Gemma; (3) CKA decreases monotonically, probe peaks after language transition layer.

**Section 1 (Intro):** Motivates from Zhao et al. [2026] CLEAR finding on linguistic affinity. Research question: how conflict signals are encoded in representations and whether they transfer cross-lingually. Three main findings stated.

**Section 2 (Related Work):** Covers knowledge conflicts (ConflictQA, Chen et al., Longpre et al.), cross-lingual representations (Wendler et al., Müller et al., Pires et al., Libovický et al.), probing/mechanistic interpretability (Belinkov, Hewitt & Manning, Geiger et al., SAEs), and CLEAR.

**Section 3 (Method):**
- 3.1 Dataset: Translation via GPT-4, COMET quality assessment (mean 0.68-0.70, pass rate 12-18.5% at ≥0.80), verification (both EN/ZH must elicit expected answer), yields 1096/272 for Llama, 798/168 for Qwen. Gemma numbers not explicitly stated for dataset construction.
- 3.2 Probing: Linear (logistic regression, L2, 5-fold CV), MLP (2-layer, hidden 256, ReLU). Cross-lingual: train L1 evaluate L2. Permutation tests n=1000, bootstrap n=100 for asymmetry CI.
- 3.3 CKA: Linear kernel, language transition = first layer CKA < 0.5.
- 3.4 Steering: Probe weight as steering vector, α = 3× std of projections.

**Section 4 (Results):**
- Table 1: Cross-lingual probe accuracy. Llama EN→EN 77.1, ZH→ZH 71.2, EN→ZH 64.1, ZH→EN 71.3, gap +7.2pp [1.1,13.6] Sig. Qwen: 75.3, 71.6, 65.0, 72.2, +7.2pp [-1.2,13.4] No. Gemma: 72.0, 68.0, 63.0, 64.0, +1.0pp [-4.5,6.8] No.
- Table 2: COMET scores. Llama train 0.69, test 0.68; Qwen train 0.70, test 0.70.
- Table 3: COMET tercile ablation. Qwen: Low 66.35, Med 67.69, High 60.71, Δ=-5.64pp, p=0.695. Llama: 65.80, 63.20, 62.60, Δ=-3.20pp, p=0.480.
- Table 4: MLP vs linear (EN→ZH). Llama +4.7pp, Qwen +2.3pp, Gemma +2.0pp.
- Table 5: CKA by layer group. All show early high (0.80-0.85), mid decline (0.61-0.70), late low (0.38-0.45).
- Table 6: Probe peak vs CKA transition. Llama 88% vs 75%, Qwen 67% vs 58%, Gemma 62% vs 55%.
- Table 7: Label noise ablation (Llama EN→EN). 0%: 77.1, 5%: 75.8, 10%: 73.2, 15%: 69.5, 20%: 64.1. ~3.3pp per 5%.
- Table 8: Steering flip rates. Llama 8%/5%, Qwen 6%/4%, Gemma 3%/3%. All very low.

**Section 5 (Discussion):** Conflict detectability robust. Transfer asymmetry architecture-dependent. Layer structure descriptive only. Connection to CLEAR correlational only.

**Section 6 (Limitations):** Single language pair. Limited model coverage (3). No mechanistic decomposition (SAE/Track 2-3 incomplete). Weak causal evidence (steering ≤8%). ~8% label noise. ~1000 instances per model.

**Section 7 (Conclusion):** Empirical characterization + methodological framework. Future: more language pairs, SAE features, multi-dimensional steering.

**Appendix A (PCA):** 28% variance explained by PC1+PC2. EN/ZH conflict clusters misaligned. Within-EN moderate separation, within-ZH weak.
**Appendix B (Token Overlap):** Jaccard 3-4%, no positive correlation with probe accuracy. Rules out token overlap as driver.

## Experiment Design Reference (from review_context.yaml)
The full experimental plan included many more experiments than what appears in the paper:
- Track 2 (SAE analysis with Qwen-Scope, LangFIR, cross-lingual Jaccard) — NOT completed
- Track 3 (SAE-based steering, cross-lingual steering transfer, typological steering correlation) — NOT completed
- Multi-lingual extension to EN↔JA — NOT completed (15% done)
- Larger dataset validation — NOT started
- PCA visualization — completed but relegated to appendix

So the paper only contains Track 1 (probing) results. Track 2 (SAE mechanistic decomposition) and Track 3 (causal steering) are entirely absent.

## Your Review Task (R1: Methods + Experiments)

Evaluate:
1. **Methodological soundness:** Is the experimental design rigorous? Are there confounds? Is the statistical testing appropriate?
2. **Experimental coverage:** Are the experiments sufficient to support the claims? What's missing?
3. **Data quality:** Translation quality, verification pipeline, label noise implications
4. **Statistical rigor:** Bootstrap n=100 (is this enough?), permutation tests, multiple comparisons
5. **Reproducibility:** Are details sufficient?
6. **Presentation of results:** Tables, figures, clarity

Provide your review in this format:

```
## Summary
[2-3 sentences]

## Strengths
[Bulleted list, be specific]

## Weaknesses
[Bulleted list, be specific with line/table/section references]

## Questions for Authors
[Numbered list]

## Minor Issues
[Bulleted list]

## Missing Experiments / Suggested Improvements
[Bulleted list]

## Scores
- Soundness: X/4
- Presentation: X/4
- Contribution: X/4
- Overall: X/10
- Confidence: X/5
```

Be rigorous but fair. Ground every criticism in specific evidence from the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "861f4dda-3649-43b8-9722-dab81d50805d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T03:31:34.505Z_

```json
{
  "parentUuid": "861f4dda-3649-43b8-9722-dab81d50805d",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
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
  "uuid": "06287ce6-95c1-45ae-aee9-e4aa9c1692cd",
  "timestamp": "2026-05-22T03:31:34.505Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-22T03:31:37.196Z_



I'll review the paper's methods and experiments thoroughly. Let me first examine the project files for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06287ce6-95c1-45ae-aee9-e4aa9c1692cd",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuF2jRYbL67mVXcA1M9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77916606-a56f-483f-8c6f-8f5d718365a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3QtJM3oaa92TBN4bSZtNN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 4 · 2026-05-22T03:31:38.308Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DgQ7wRMvaw18oxr1A8NMjN`</summary>

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
  "parentUuid": "77916606-a56f-483f-8c6f-8f5d718365a8",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuF2jRYbL67mVXcA1M9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9f3420b-c39b-4a0e-9c7f-95f4aa6efbab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3QtJM3oaa92TBN4bSZtNN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 0,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16411,
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

_source line 5 · 2026-05-22T03:31:38.312Z_

<details><summary>↩ Tool result · `toolu_01DgQ7wRMvaw18oxr1A8NMjN`</summary>

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
  "parentUuid": "a9f3420b-c39b-4a0e-9c7f-95f4aa6efbab",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "0ff26cce-a182-41fc-826e-418504c26e1c",
  "sourceToolAssistantUUID": "a9f3420b-c39b-4a0e-9c7f-95f4aa6efbab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-22T03:31:41.154Z_



Let me examine the paper artifacts and any additional experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ff26cce-a182-41fc-826e-418504c26e1c",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuFKBPENQW848Y6GvJZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c480243c-f611-407d-ba52-ee507e7d004a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1VE7Xa2QDYJZNjJSogeVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 16411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1294,
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

_source line 7 · 2026-05-22T03:31:42.111Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011afWeCnSgb1RkdztcnK441`</summary>

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
  "parentUuid": "c480243c-f611-407d-ba52-ee507e7d004a",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuFKBPENQW848Y6GvJZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d64c87db-c4f4-4e99-8bb1-ad5e4c77ac53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1VE7Xa2QDYJZNjJSogeVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 16411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1294,
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

_source line 8 · 2026-05-22T03:31:42.131Z_

<details><summary>↩ Tool result · `toolu_011afWeCnSgb1RkdztcnK441`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| comet_llama_v5 | — | — | — | — |\\n| comet_qwen_v5 | — | — | — | — |\\n| comet_llama_v6 | COMET back-translation 质量验证 Llama ZH 翻译（v6: 跟踪 nohup 进程，v5 被 tmux 监控误标 failed） | — | — | — |\\n\\n## 待处理\\n- comet_llama_v4（准备中）\\n- comet_llama_v3（准备中）\\n- comet_llama_v2（准备中）\\n- comet_llama（准备中）\\n- comet_qwen_v4（准备中）\\n- comet_qwen_v3（准备中）\\n- comet_qwen_v2（准备中）\\n- comet_qwen（准备中）\\n- qwen_zh_act_v2: 用 v2 re-verified 数据（966条，enable_thinking=False）重采 Qwen3-8B ZH 激活，替换 v1 污染数据（1116条）（准备中）\\n- probe_qwen_full（准备中）\\n- …另有 13 项\\n\\n## 近期结论\\n- **mvp_probe_v1** (success): 跨语言知识冲突信号可在 Qwen3-8B-Instruct 残差流中被线性探针检测（EN acc ≥ 80%），且展现有意义的跨语言迁移（EN→ZH binomial p < 0.01, point > 60%）\\n  [bootstrap_asymmetry_corrected_qwen](/api/workspace-files/projects/clkc_mech_interp/artifacts/mvp_probe_v1/data/bootstrap_qwen.json)\\n- **mvp_probe_llama_v1** (success): 跨语言知识冲突信号可在 Llama-3.1-8B-Instruct 残差流中被线性探针检测（EN acc ≥ 80%），且展现跨语言迁移（EN→ZH binomial p < 0.01, point > 60%）——与 Qwen3-8B 形成跨模型验证 ← 基于 mvp_probe_v1\\n  [bootstrap_asymmetry_corrected_llama](/api/workspace-files/projects/clkc_mech_interp/artifacts/mvp_probe_llama_v1/data/bootstrap_llama.json)\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-41302: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1352, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d64c87db-c4f4-4e99-8bb1-ad5e4c77ac53",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "9d0ec110-eab3-4d62-9864-17141cde706a",
  "sourceToolAssistantUUID": "d64c87db-c4f4-4e99-8bb1-ad5e4c77ac53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T03:31:43.111Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015QRFfkgD4E3rptg3VBHnqQ`</summary>

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
  "parentUuid": "9d0ec110-eab3-4d62-9864-17141cde706a",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuFKBPENQW848Y6GvJZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "269c3af1-77e9-4e9e-b58f-3c0f29af511b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1VE7Xa2QDYJZNjJSogeVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 16411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1294,
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

_source line 10 · 2026-05-22T03:31:43.120Z_

<details><summary>↩ Tool result · `toolu_015QRFfkgD4E3rptg3VBHnqQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.md\", \"content\": \"# clkc_mech_interp — Research Dashboard\\n\\n> 最后更新: 2026-05-22 02:38 UTC | 更新原因: MVP 通过，进入 Research 阶段，Dream 已提交\\n\\n## 核心方向\\n多语言 LLM 中跨语言知识冲突的机制可解释性研究。核心发现：冲突信号可线性检测，跨语言迁移存在方向性不对称（~7.2pp），跨架构一致。目标 ICLR 2027（DDL 2026-09-24）。详见 paper_framing.md。\\n\\n## 当前阶段：Research（MVP 已通过 ✅）\\n\\nMVP 通过条件：双模型探针验证 + 两个 confounder 排除（token overlap + COMET ablation）。\\n\\n### 双模型 Bootstrap n=100 结果（可引用）\\n\\n| 方向 | Llama-3.1-8B (mean±std) | Qwen3-8B (mean±std) |\\n|------|------------------------|---------------------|\\n| EN→EN | **77.1±1.2%** | **75.3±1.7%** |\\n| ZH→ZH | **71.2±1.3%** | **71.6±1.8%** |\\n| EN→ZH | **64.1±2.5%** | **65.0±2.7%** |\\n| ZH→EN | **71.3±2.7%** | **72.2±2.6%** |\\n\\n不对称性 (corrected): Llama +7.22pp CI [1.1%, 13.6%] sig | Qwen +7.18pp CI [-1.2%, 13.4%] trending\\n\\n### Confounder 排除\\n- **RC1 翻译质量**: plan_105 COMET tercile ablation → delta=-5.64pp (反向), p=0.695, 非 confounder ✅\\n- **RC2 Token overlap**: plan_101 → per-sample Jaccard 3-4%, Llama 负相关 r=-0.15, 非 confounder ✅\\n\\n### 近期任务\\n- [x] ~~complete_mvp()~~ ✅\\n- [ ] dream_simulate(review_mode=\\\"full\\\") — dream_20260522T023801 pending (10-25 min)\\n- [ ] Llama test COMET 完成后跑 Llama 版 tercile ablation（确认一致性）\\n- [ ] COMET train 继续跑（Qwen ~3.8h, Llama ~7h）\\n- [ ] Dream 完成后审阅 → 批准 P0 实验启动\\n\\n### Post-MVP P0 实验（等 Dream 审阅后启动）\\n1. ~~Token overlap (plan_101)~~ ✅\\n2. ~~Bootstrap CI 修正 (plan_099)~~ ✅\\n3. ~~COMET tercile ablation (plan_105)~~ ✅ (Qwen done, Llama pending)\\n4. 第三模型 Gemma-2-9B-IT (plan_102) — 模型已下载, 等 GPU\\n5. 多语言扩展 EN↔JA (plan_103) — planned, ~20 GPU·h\\n6. Layer-wise CKA/SVCCA (plan_104) — planned, ~4 GPU·h\\n7. Representation steering (plan_107) — planned, ~8 GPU·h\\n\\n## GPU 预算\\nwestd-41302: 4× RTX PRO 6000 Blackwell 96GB（cuda:0-3）\\n当前: cuda:0,2 COMET train; cuda:3 COMET Llama test; cuda:1 空闲\\n\\n## 风险\\n1. Llama CI 下界 borderline (1.1pp) — 第三模型 Gemma 结果决定 C2 强度\\n2. 只有 Track 1 时论文贡献可能偏 analysis paper — Dream 审稿将评估\\n3. COMET train 仍需 4-8h 完成\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-22 | COMET 0.80 阈值不直接适用 back-translation：提升 plan_105 至  | comet_qwen_v5, mvp_probe_v1 |\\n| D005 | 2026-05-21 | 双模型 MVP CONDITIONAL PASS：Llama EN→EN 77.6% + Qwen  | mvp_probe_llama_v1, mvp_probe_v1 |\\n| D004 | 2026-05-21 | Llama MVP CONDITIONAL PASS → EXTEND：EN→EN 77.6%, 跨 | mvp_probe_llama_v1 |\\n| D003 | 2026-05-21 | 补采样至 2000 条 + 取消强制交集，每个模型用各自 verified 数据集 | mvp_probe_llama_v1 |\\n| D002 | 2026-05-21 | 采纳 Reviewer 5 条 warning，细化 MVP gate：增加 70-79% cond | — |\\n| D001 | 2026-05-21 | MVP 方案：EN+ZH 双语探针迁移实验验证跨语言冲突信号可检测性 | — |\\n\\n\\n\", \"total_chars\": 2474, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "269c3af1-77e9-4e9e-b58f-3c0f29af511b",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "aadd21d8-59b4-43b3-9c0b-428b8f4ffcc9",
  "sourceToolAssistantUUID": "269c3af1-77e9-4e9e-b58f-3c0f29af511b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T03:31:43.630Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LS8tbm3AkT1asVrBCPTBfu`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aadd21d8-59b4-43b3-9c0b-428b8f4ffcc9",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuFKBPENQW848Y6GvJZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "549847a6-feb4-45eb-ae0b-903aec1a4ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1VE7Xa2QDYJZNjJSogeVb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 16411,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1294
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 315,
          "cache_read_input_tokens": 16411,
          "cache_creation_input_tokens": 1294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1294,
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

_source line 12 · 2026-05-22T03:31:43.642Z_

<details><summary>↩ Tool result · `toolu_01LS8tbm3AkT1asVrBCPTBfu`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'clkc_mech_interp'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "549847a6-feb4-45eb-ae0b-903aec1a4ecf",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "434efeb9-44bf-405c-87ce-d2842b10b51e",
  "sourceToolAssistantUUID": "549847a6-feb4-45eb-ae0b-903aec1a4ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T03:31:46.738Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WRaBDEjybb23WeoUQER8dQ`</summary>

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
  "parentUuid": "434efeb9-44bf-405c-87ce-d2842b10b51e",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuFi24eHUUohjanwTS3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f887994c-2950-47eb-aaa0-4ead46879f13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H15tEDpvigAc9wbwGfKsLU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3116,
      "cache_read_input_tokens": 17705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3116,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 14 · 2026-05-22T03:31:46.746Z_

<details><summary>↩ Tool result · `toolu_01WRaBDEjybb23WeoUQER8dQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper_framing.md\", \"content\": \"# Paper Framing — clkc_mech_interp\\n\\n> 最后更新: 2026-05-22 | 目标: ICLR 2027 (DDL ~2026-09-24)\\n\\n## Core Insight\\n\\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致（Llama-3.1-8B 与 Qwen3-8B）。这为 CLEAR (Zhao et al. 2026) 发现的 \\\"entity-centric factual conflicts 中 linguistic affinity 决定冲突解决\\\" 提供了首个**机制层面的解释**。\\n\\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\\n\\n## Narrative Structure\\n\\n**现象驱动的机制解释**（非 \\\"applying X to Y\\\"）：\\n\\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity（而非 resource abundance）决定跨语言冲突解决，但未提供机制解释\\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？是 language-universal 还是 language-specific？为什么 similarity 起决定作用？\\n3. **Our answer**: 通过残差流探针、SAE 特征分析、激活干预三条互补分析轨道，揭示冲突检测信号的跨语言结构——是否共享、在哪些层出现、能否用于干预\\n\\n**Secondary framing**: SAE-based mechanistic interpretability 工具在跨语言条件下的 stress test——probing / SAE / steering 三种工具的跨语言适用性边界\\n\\n## Competing Hypotheses (pre-registered)\\n\\n**H1 — English-anchored universal detection**:\\n冲突检测信号本身是 language-independent 的（\\\"是否存在冲突\\\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\\n\\n**H2 — Language-pair-specific encoding**:\\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\\n\\n**MVP 证据倾向**:\\n当前双模型结果倾向 **H1 的变体**——ZH→EN 迁移（71-72%）显著强于 EN→ZH（64-65%），暗示冲突信号以英语表征空间为锚点编码。非线性成分（MLP EN→ZH +9.2pp vs linear）提示 EN→ZH 方向的跨语言映射更复杂。\\n\\n## Core Claims\\n\\n### Claim 1: Cross-lingual conflict detectability\\n**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。\\n**Evidence needed**:\\n- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)\\n- Permutation test p < 0.001 ✅ (all directions)\\n- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)\\n**Status**: MVP 已验证 ✅\\n\\n### Claim 2: Asymmetric cross-lingual transfer\\n**Statement**: 跨语言探针迁移呈方向一致的不对称：ZH→EN 迁移强于 EN→ZH（~7.2pp），效果量跨架构高度一致（Llama 显著，Qwen 方向一致但未达显著）。\\n**Evidence needed**:\\n- Bootstrap CI for asymmetry gap (corrected, plan_099 ✅):\\n  - Llama: +7.22pp, CI [1.1%, 13.6%] — 排除零但 borderline ✅\\n  - Qwen: +7.18pp, CI [-1.2%, 13.4%] — 含零，方向一致 ⚠️\\n- ≥2 models show consistent effect size ✅ (7.22pp vs 7.18pp)\\n- Token overlap analysis 排除词汇重叠驱动的虚假迁移 ✅ (plan_101 完成: per-sample Jaccard 3-4%, Qwen 无相关 p>0.4, Llama 显著负相关 r=-0.15 p=0.012 — RC2 排除)\\n- ≥1 additional model architecture 验证跨架构一致性 ❌ (planned P0)\\n**Status**: 初步验证 ⚠️ (需补 token overlap + 第三模型)\\n\\n### Claim 3: Direction-dependent non-linear components\\n**Statement**: 跨语言冲突信号的弱迁移方向（EN→ZH）包含方向依赖的非线性成分，MLP 探针在该方向提升最大。跨架构一致方向但幅度不同（Llama +9.2pp single-seed / ~+4.7pp bootstrap-corrected, Qwen +2.3pp），暗示非线性成分与模型的跨语言对齐程度相关。\\n**Evidence needed**:\\n- MLP vs linear probe comparison on ≥2 models ✅ (both show EN→ZH direction gains)\\n- MLP 不使用 test set 做 early stopping ✅ (已修复)\\n- 控制实验排除 MLP 过拟合 ❌ (需 train/test accuracy gap 分析)\\n- 解释跨架构幅度差异 (Llama 4x > Qwen) ❌ (可能与 Qwen 更强的跨语言对齐有关——ZH 训练数据占比更高)\\n**Status**: 初步验证 ⚠️ (方向一致但幅度差异需解释)\\n\\n### Claim 4: Layer-wise conflict signal structure\\n**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。\\n**Evidence needed**:\\n- Layer-wise probe accuracy curves for ≥3 models ❌\\n- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌\\n- 与 \\\"Lost in Multilinguality\\\" 的 language transition 层对比 ❌\\n**Status**: 未验证 ❌\\n\\n### Claim 5: Cross-lingual SAE conflict features (Track 2)\\n**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。\\n**Evidence needed**:\\n- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌\\n- LangFIR random-token filtering 控制 ❌\\n- Cross-lingual feature Jaccard 分析 ❌\\n**Status**: 未开始 ❌\\n\\n### Claim 6: Cross-lingual conflict steering (Track 3)\\n**Statement**: 通过 SAE 特征干预可以定向操控跨语言冲突解决行为。\\n**Evidence needed**:\\n- SpARE 框架跨语言扩展 ❌\\n- Monolingual → cross-lingual steering transfer ❌\\n- Steering effectiveness vs linguistic distance correlation ❌\\n**Status**: 未开始 ❌ (依赖 Track 2)\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Translation quality confound [RESOLVED ✅]\\n**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败\\n**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。\\n**Remaining**: Llama test COMET 完成后重复此分析确认一致性。\\n\\n### RC2: Token overlap confound [RESOLVED ✅]\\n**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动\\n**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**\\n\\n### RC3: Model coverage insufficient [HIGH]\\n**Concern**: 只有 2 个模型，无法声称 \\\"架构无关\\\"\\n**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性\\n**Experiment**: P0 — additional model verification\\n\\n### RC4: Dataset size and diversity [MEDIUM]\\n**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对\\n**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）\\n**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)\\n\\n### RC5: Linear probe expressiveness [LOW]\\n**Concern**: 线性探针可能遗漏复杂非线性信号\\n**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化\\n**Experiment**: Done — MLP vs Linear comparison\\n\\n### RC6: SAE base/instruct mismatch [MEDIUM]\\n**Concern**: Qwen-Scope SAE 训练在 base model 上，用于 instruct model 分析可能失配\\n**Mitigation**: Track 2 用 base model 做 SAE 分析 + 与 Track 1 instruct probe 交叉验证\\n**Experiment**: Track 2 设计已考虑\\n\\n### RC7: Steering failure precedent [MEDIUM]\\n**Concern**: \\\"Interpretability without actionability\\\" 证明 SAE steering 可能完全无效\\n**Mitigation**: 知识冲突与临床分诊的 5 维差异（SpARE 已证明知识冲突场景 steering 有效）；Track 3 显式报告失败模式\\n**Experiment**: Track 3 包含 negative result framing\\n\\n### RC8: Causal claims without intervention [HIGH]\\n**Concern**: 探针只证明信号可检测，不证明因果关系\\n**Mitigation**: Track 3 steering 实验提供因果证据；Track 1 permutation test 提供统计控制\\n**Experiment**: Track 3 steering + representation steering (P1)\\n\\n## Paper Structure (Tentative)\\n\\n1. **Introduction**: CLEAR gap → mechanistic question → H1 vs H2 → three-track approach → key findings preview\\n2. **Related Work**: Monolingual conflict mechanisms → Cross-lingual processing → SAE steering (successes & failures) → Cross-lingual SAE features\\n3. **Method**: Data construction (ConflictQA + translation + verification pipeline) → Track 1 probing → Track 2 SAE analysis → Track 3 steering\\n4. **Experiments & Results**:\\n   - 4.1 Cross-lingual conflict detectability (C1)\\n   - 4.2 Asymmetric transfer analysis (C2) + token overlap controls\\n   - 4.3 Non-linear components (C3) + layer-wise structure (C4)\\n   - 4.4 SAE feature analysis (C5) [if Track 2 ready]\\n   - 4.5 Steering experiments (C6) [if Track 3 ready]\\n5. **Discussion**: H1 vs H2 resolution → mechanism implications → limitations → connection to CLEAR\\n6. **Conclusion**\\n\\n## Scope Control\\n\\n**投稿最低要求 (must-have for submission)**:\\n- Claims 1-3 fully supported (cross-lingual detectability + asymmetry + non-linearity)\\n- Claim 4 partially supported (layer-wise analysis on ≥2 models)\\n- ≥3 model architectures\\n- ≥2 language pairs (EN-ZH + one more)\\n- Token overlap control\\n- COMET translation quality validation\\n\\n**理想状态 (nice-to-have)**:\\n- Track 2 SAE analysis (Claim 5)\\n- Track 3 steering (Claim 6)\\n- 5+ language pairs covering multiple typological families\\n- Full CKA/SVCCA layer analysis\\n\\n**不做 (out of scope)**:\\n- 10-language full CLEAR replication\\n- Custom SAE training\\n- MoE model analysis\\n\", \"total_chars\": 7801, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f887994c-2950-47eb-aaa0-4ead46879f13",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "c9eef6c4-0b50-4737-bf0d-8a5503882425",
  "sourceToolAssistantUUID": "f887994c-2950-47eb-aaa0-4ead46879f13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T03:31:47.373Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013kCu8XULAKvAcK2pLByqu3`</summary>

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
  "parentUuid": "c9eef6c4-0b50-4737-bf0d-8a5503882425",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuFi24eHUUohjanwTS3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e502357-6646-4df0-a380-ce9da200bcb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H15tEDpvigAc9wbwGfKsLU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3116,
      "cache_read_input_tokens": 17705,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3116
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 17705,
          "cache_creation_input_tokens": 3116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3116,
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

_source line 16 · 2026-05-22T03:31:47.390Z_

<details><summary>↩ Tool result · `toolu_013kCu8XULAKvAcK2pLByqu3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/decisions.yaml\", \"content\": \"_next_id: 7\\ndecisions:\\n- id: D001\\n  date: 2026-05-21 12:00 UTC\\n  summary: MVP 方案：EN+ZH 双语探针迁移实验验证跨语言冲突信号可检测性\\n  rationale: Track 1（探针迁移）是整个 3-track 研究的基础前提。如果残差流中无法检测冲突信号或跨语言完全不迁移，后续 SAE 分析和 steering\\n    均无意义。选 Qwen3-8B-Instruct 因 Qwen-Scope 提供 base SAE 便于后续 Track 2。选 EN+ZH 因语系距离大，若迁移成功则信号强。ConflictQA\\n    公开可用，无需等 CLEAR 数据。Pass/fail 标准参考 Brink et al. 单语 0.96 F1 和 Zhao et al. ~90% 探针精度。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-21 12:06 UTC\\n  summary: 采纳 Reviewer 5 条 warning，细化 MVP gate：增加 70-79% conditional pass 定义、layer-wise\\n    量化标准、统计显著性要求（binomial p<0.01）、翻译 COMET gate（≥0.80）、FAIL→retry Llama 行动路径\\n  rationale: Reviewer 指出原 gate criteria 存在 ambiguous zone（70-79% 无定义）、layer-wise pattern\\n    逃逸条款过于模糊、ZH 60% 阈值缺统计锚定、翻译质量是迁移失败的混淆因素、FAIL 后行动未定义。全部采纳以确保 MVP 结论可靠。FAIL→retry\\n    on Llama 给予一次排除模型特异性的机会，两模型均 FAIL 才 kill。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-21 14:26 UTC\\n  summary: 补采样至 2000 条 + 取消强制交集，每个模型用各自 verified 数据集\\n  rationale: Llama verify 保留率仅 33%（266/800 train），低于 300 阈值。ConflictQA 有 ~10K 条，扩至\\n    2000 可保证两模型各自 ≥300 有效样本。取消交集策略因为强制交集会进一步损失样本量，且跨模型对比不要求相同样本——各自 verified 集上报告相同指标即可，交集作为补充分析。20%\\n    标签翻转率确认了 M001 verify 步骤的必要性。\\n  related_experiments:\\n  - exp_id: mvp_probe_llama_v1\\n    role: triggered_decision\\n    result: verify 保留率 33%, 266 train / 70 test, 20% flip\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-21 19:17 UTC\\n  summary: Llama MVP CONDITIONAL PASS → EXTEND：EN→EN 77.6%, 跨语言迁移不对称（ZH→EN 71.3% vs\\n    EN→ZH 59.6%），等 Qwen 结果做最终 verdict\\n  rationale: Llama 4 方向探针结果显示冲突信号可线性检测（所有方向 p < 0.01），但 EN→EN 未达 80% PASS 阈值（77.6%）。跨语言迁移存在但高度不对称：ZH→EN\\n    强迁移（71.3%），EN→ZH 弱迁移（59.6%，刚好低于 60% point 阈值但 p=9.7e-4 仍显著）。CONDITIONAL PASS 按\\n    D002 规则进入 EXTEND 评估。等 Qwen 跨模型验证后做最终 MVP verdict。不对称迁移本身是有价值的科学发现。\\n  related_experiments:\\n  - exp_id: mvp_probe_llama_v1\\n    role: primary\\n    result: EN→EN 77.6% L28, ZH→ZH 72.1% L13, EN→ZH 59.6% L5, ZH→EN 71.3% L15\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-21 20:33 UTC\\n  summary: 双模型 MVP CONDITIONAL PASS：Llama EN→EN 77.6% + Qwen EN→EN 75.0%，跨语言迁移不对称且跨架构一致（ZH→EN\\n    >> EN→ZH），等 COMET 验证后进入 research 阶段\\n  rationale: 两个模型全 4 方向探针结果统计高度显著（permutation p < 0.001）。核心发现：(1) 冲突信号在两模型两语言中均可线性检测；(2)\\n    跨语言迁移存在方向性不对称（ZH→EN 71-73% vs EN→ZH 60-67%），两模型一致；(3) 不对称程度与架构相关——Qwen（多语言训练比例更高）EN→ZH\\n    67.3% 远强于 Llama 59.6%。EN→EN 均在 70-79% CONDITIONAL 区间，未达 80% PASS，但跨语言迁移的质量和不对称发现的科学价值足以支撑继续研究。COMET\\n    翻译质量验证是最后一个前置条件。\\n  related_experiments:\\n  - exp_id: mvp_probe_llama_v1\\n    role: primary\\n    result: EN→EN 77.6%, ZH→ZH 72.1%, EN→ZH 59.6%, ZH→EN 71.3%\\n  - exp_id: mvp_probe_v1\\n    role: primary\\n    result: EN→EN 75.0%, ZH→ZH 72.6%, EN→ZH 67.3%, ZH→EN 73.2% (v2 clean labels)\\n  depends_on:\\n  - D002\\n  - D004\\n- id: D006\\n  date: 2026-05-22 02:13 UTC\\n  summary: COMET 0.80 阈值不直接适用 back-translation：提升 plan_105 至 P0，用 ablation 实证判断翻译质量是否影响探针结果\\n  rationale: Qwen test COMET mean=0.70, pass rate 18.45% (31/168 at ≥0.80)。但 0.80\\n    阈值是为正向翻译设定的，back-translation 引入二次噪声（EN→ZH→EN），COMET 天然偏低。降低阈值是 ad hoc 的；正确做法是用\\n    plan_105 COMET 分段 ablation 实证检验：按 COMET tertile 分组比较 probe acc，如果组间无显著差异 → 翻译质量非\\n    confounder → 放宽阈值有据可依；如果组间差异显著 → 需过滤低 COMET 样本重跑探针。\\n  related_experiments:\\n  - exp_id: comet_qwen_v5\\n    role: evidence\\n    result: Qwen test COMET mean=0.70, pass 18.45%\\n  - exp_id: mvp_probe_v1\\n    role: dependent\\n    result: 探针结果可能受翻译质量影响\\n  depends_on:\\n  - D005\\n\", \"total_chars\": 3400, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e502357-6646-4df0-a380-ce9da200bcb4",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "37d5feec-e36e-401c-a070-cf3a3db22bf2",
  "sourceToolAssistantUUID": "1e502357-6646-4df0-a380-ce9da200bcb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-22T03:31:50.234Z_

Now let me look at the actual paper and any artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37d5feec-e36e-401c-a070-cf3a3db22bf2",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuFyykpgZFnGwovp8Px",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2fce47e-0bba-4f66-b33f-2ba195da9b73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e8nonqdYuJtDsaYccCcZH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 20821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6753,
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

_source line 18 · 2026-05-22T03:31:52.121Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WFErBABjvTgfskCVwKK7xf`</summary>

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
  "parentUuid": "a2fce47e-0bba-4f66-b33f-2ba195da9b73",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuFyykpgZFnGwovp8Px",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f153bd38-2d64-410b-8e69-7756e4d50e06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e8nonqdYuJtDsaYccCcZH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 20821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6753,
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

_source line 19 · 2026-05-22T03:31:52.212Z_

<details><summary>↩ Tool result · `toolu_01WFErBABjvTgfskCVwKK7xf`</summary>

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
  "parentUuid": "f153bd38-2d64-410b-8e69-7756e4d50e06",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "d5c82018-c509-4591-910c-94fd8bf4591c",
  "sourceToolAssistantUUID": "f153bd38-2d64-410b-8e69-7756e4d50e06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T03:31:53.048Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Vb9j4teacrf8kmDSS3sHty`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5c82018-c509-4591-910c-94fd8bf4591c",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuFyykpgZFnGwovp8Px",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "810faf45-257c-46b4-a5c2-9560de99913e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e8nonqdYuJtDsaYccCcZH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 20821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6753,
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

_source line 21 · 2026-05-22T03:31:53.133Z_

<details><summary>↩ Tool result · `toolu_01Vb9j4teacrf8kmDSS3sHty`</summary>

```text
artifacts/clkc_code/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/back.pdf
artifacts/clkc_code/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/filesave.pdf
artifacts/clkc_code/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/forward.pdf
artifacts/clkc_code/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/hand.pdf
artifacts/clkc_code/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/help.pdf
artifacts/clkc_code/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/home.pdf
artifacts/clkc_code/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/matplotlib.pdf
artifacts/clkc_code/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/move.pdf
artifacts/clkc_code/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/qt4_editor_options.pdf
artifacts/clkc_code/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/subplots.pdf
artifacts/clkc_code/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/zoom_to_rect.pdf
artifacts/dream_reports/dream_20260522T023801/best/paper.pdf
artifacts/dream_reports/dream_20260522T023801/median/paper.pdf
artifacts/dream_reports/dream_20260522T023801/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "810faf45-257c-46b4-a5c2-9560de99913e",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "0c161f99-1887-4f9c-8283-c754e1a011b2",
  "sourceToolAssistantUUID": "810faf45-257c-46b4-a5c2-9560de99913e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T03:31:53.695Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EWjVe3yPqqztFUCwAdDFbb`</summary>

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
  "parentUuid": "0c161f99-1887-4f9c-8283-c754e1a011b2",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuFyykpgZFnGwovp8Px",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34711b6e-87e9-4780-85e9-cd2496e54dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e8nonqdYuJtDsaYccCcZH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 20821,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6753
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 279,
          "cache_read_input_tokens": 20821,
          "cache_creation_input_tokens": 6753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6753,
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

_source line 23 · 2026-05-22T03:31:53.705Z_

<details><summary>↩ Tool result · `toolu_01EWjVe3yPqqztFUCwAdDFbb`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/memory.md\", \"content\": \"# Gemma-2-9B-IT 兼容性报告 (plan_102)\\n\\n## 模型结构\\n\\n| 属性 | 值 |\\n|------|-----|\\n| model_type | gemma2 |\\n| architecture | Gemma2ForCausalLM |\\n| num_hidden_layers | 42 |\\n| hidden_size | 3584 |\\n| num_attention_heads | 16 |\\n| num_key_value_heads | 8 (GQA) |\\n| head_dim | 256 |\\n| vocab_size | 256000 |\\n| max_position_embeddings | 8192 |\\n| sliding_window | 4096 (alternating layers) |\\n| torch_dtype | bfloat16 |\\n| attn_logit_softcapping | 50.0 |\\n| final_logit_softcapping | 30.0 |\\n\\n## Tokenizer\\n\\n| 属性 | 值 |\\n|------|-----|\\n| padding_side | left |\\n| pad_token | `&lt;pad>` (id=0) |\\n| bos_token | `&lt;bos>` (id=2) |\\n| eos_token | `&lt;eos>` (id=1) |\\n| chat_template | `&lt;bos>&lt;start_of_turn>user\\\\n{content}&lt;end_of_turn>\\\\n&lt;start_of_turn>model\\\\n` |\\n| thinking mode | 无（enable_thinking 参数被 **kwargs 静默接受但无效果） |\\n| system role | 不支持（template 中 raise_exception） |\\n\\n## 各脚本兼容性\\n\\n### verify_parametric_knowledge.py — ✅ 无需修改\\n\\n- `AutoModelForCausalLM.from_pretrained`：通用加载，兼容 ✓\\n- `apply_chat_template(enable_thinking=False)`：Gemma tokenizer 通过 `**kwargs` 静默接受，不报错 ✓\\n- `strip_think_tags()`：Gemma 输出无 `&lt;think>` 标签，函数是 no-op ✓\\n- 生成参数 `do_sample=False, max_new_tokens=128`：通用，兼容 ✓\\n- 运行命令：`python src/verify_parametric_knowledge.py --model /root/autodl-tmp/models/gemma-2-9b-it --data_dir data/ --raw_dir data/ --output_dir data/gemma2/`\\n\\n### collect_activations.py — ✅ 无需修改\\n\\n- `model.model.layers`：Gemma2 结构为 `Gemma2ForCausalLM.model(Gemma2Model).layers[0..41]`，与 Qwen/Llama 同构 ✓\\n- Hook `output[0]`：Gemma2DecoderLayer 返回 tuple，`[0]` 是 hidden_states ✓\\n- `tokenizer.padding_side = \\\"left\\\"`：脚本显式设置，与 Gemma 默认一致 ✓\\n- `tokenizer.pad_token = tokenizer.eos_token`：Gemma 有专用 pad_token（id=0），此 fallback 不触发 ✓\\n- Last-token 提取 `shape[1]-1`：left-padding 下最后位置即最后真实 token ✓\\n- 运行命令：`python src/collect_activations.py --model /root/autodl-tmp/models/gemma-2-9b-it --data_dir data/gemma2 --output_dir outputs/gemma2 --lang en --batch_size 4`\\n\\n### train_probe.py — ✅ 无需修改\\n\\n- 无硬编码维度或模型名\\n- 从 .pt 文件读取 numpy 数组，自动适配任意 hidden_size (3584)\\n- 运行命令：`python src/train_probe.py --en_path outputs/gemma2/en_activations.pt --output_dir outputs/gemma2`\\n\\n## Layer 结构详情\\n\\n```\\nmodel (Gemma2ForCausalLM)\\n├── model (Gemma2Model)\\n│   ├── embed_tokens (Embedding)\\n│   ├── layers (ModuleList) × 42\\n│   │   └── [i] (Gemma2DecoderLayer)\\n│   │       ├── self_attn (Gemma2Attention)\\n│   │       ├── mlp (Gemma2MLP)\\n│   │       ├── input_layernorm (Gemma2RMSNorm)\\n│   │       ├── post_attention_layernorm (Gemma2RMSNorm)\\n│   │       ├── pre_feedforward_layernorm (Gemma2RMSNorm)\\n│   │       └── post_feedforward_layernorm (Gemma2RMSNorm)\\n│   └── norm (Gemma2RMSNorm)\\n└── lm_head (Linear)\\n```\\n\\n注意：Gemma2 比 Llama/Qwen 多了 `pre_feedforward_layernorm` 和 `post_feedforward_layernorm`（pre/post-norm sandwich 结构）。不影响 hook 收集。\\n\\n## GPU 需求估算\\n\\n- 模型加载（bfloat16）：~18GB VRAM\\n- 每样本激活缓存：42 layers × 3584 dim × 4 bytes (float32) ≈ 600KB\\n- 1000 样本总激活：~600MB\\n- 推荐：单卡 24GB+ (A5000/3090/4090) 即可\\n\\n## 与 Qwen3-8B 对比\\n\\n| | Qwen3-8B | Gemma-2-9B |\\n|---|---|---|\\n| layers | 36 | 42 |\\n| hidden_size | 4096 | 3584 |\\n| attention | MHA | GQA (16h/8kv) |\\n| thinking mode | 有 | 无 |\\n| padding_side | left | left |\\n| 专用 pad_token | 无（用 eos） | 有（id=0） |\\n| sliding window | 无 | 4096 (alternating) |\\n\\n## 结论\\n\\n三个核心脚本均无需代码修改即可用于 Gemma-2-9B-IT。只需更改命令行参数中的模型路径和数据目录。\\n\", \"total_chars\": 3231, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34711b6e-87e9-4780-85e9-cd2496e54dfd",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "627b41df-e47e-46ed-91fc-8e2959724d91",
  "sourceToolAssistantUUID": "34711b6e-87e9-4780-85e9-cd2496e54dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T03:31:57.086Z_

<details open><summary>🔧 Tool call — Read · `toolu_018WxnK2X4iiXvoc7gBKfbPm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "627b41df-e47e-46ed-91fc-8e2959724d91",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuGT1wyX1BT3urqc9AQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03aeaec9-24ba-49c5-94db-cd304800e4e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7idNgmXQSbhzRp7WQAuCV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2806,
      "cache_read_input_tokens": 27574,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2806
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 27574,
          "cache_creation_input_tokens": 2806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2806,
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

_source line 25 · 2026-05-22T03:31:57.092Z_

<details><summary>↩ Tool result · `toolu_018WxnK2X4iiXvoc7gBKfbPm`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03aeaec9-24ba-49c5-94db-cd304800e4e7",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "3d8d380c-4660-4a3f-80b4-817a1f1f1b93",
  "sourceToolAssistantUUID": "03aeaec9-24ba-49c5-94db-cd304800e4e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T03:32:08.535Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FwDa5snSnwC66HhGUsEbrV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d8d380c-4660-4a3f-80b4-817a1f1f1b93",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuGhY4qr3zHKyYvFCTj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "011c9bb1-3ce8-4ac6-b3a4-2cdd12f32f98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAkPe7GTwDdkmxaDYzD7Hf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5227,
      "cache_read_input_tokens": 30380,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5227
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 30380,
          "cache_creation_input_tokens": 5227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5227,
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

_source line 27 · 2026-05-22T03:32:08.552Z_

<details><summary>↩ Tool result · `toolu_01FwDa5snSnwC66HhGUsEbrV`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "011c9bb1-3ce8-4ac6-b3a4-2cdd12f32f98",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "a0956a23-8b4c-4027-870b-714859ad8aac",
  "sourceToolAssistantUUID": "011c9bb1-3ce8-4ac6-b3a4-2cdd12f32f98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-22T03:32:11.717Z_

Now let me also look at the actual experiment code to verify reproducibility claims and understand the real state of the experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0956a23-8b4c-4027-870b-714859ad8aac",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuHYTQM4zyCG5EWiyD1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5175c73-6679-478d-a979-268d59079f15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFAZfk5knqNg2GHfU1jkDB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6945,
      "cache_read_input_tokens": 35607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6945,
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

_source line 29 · 2026-05-22T03:32:13.853Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VwyhoLnXihweT5ufn4S9LR`</summary>

```json
{
  "pattern": "**/src/*.py",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5175c73-6679-478d-a979-268d59079f15",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuHYTQM4zyCG5EWiyD1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dd77714-8144-4926-9ade-b78b0c6e6fbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFAZfk5knqNg2GHfU1jkDB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6945,
      "cache_read_input_tokens": 35607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6945,
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

_source line 30 · 2026-05-22T03:32:13.945Z_

<details><summary>↩ Tool result · `toolu_01VwyhoLnXihweT5ufn4S9LR`</summary>

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
  "parentUuid": "0dd77714-8144-4926-9ade-b78b0c6e6fbd",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "6bee65d4-e0c4-4505-8c8f-3aa39e18d9ec",
  "sourceToolAssistantUUID": "0dd77714-8144-4926-9ade-b78b0c6e6fbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T03:32:14.882Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0188FGggpH6muag46J9TSS37`</summary>

```json
{
  "pattern": "**/dream_reports/dream_20260522T023801/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bee65d4-e0c4-4505-8c8f-3aa39e18d9ec",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuHYTQM4zyCG5EWiyD1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7d3ca75-8852-409b-a567-845fbe9fdaa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFAZfk5knqNg2GHfU1jkDB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6945,
      "cache_read_input_tokens": 35607,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6945
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 35607,
          "cache_creation_input_tokens": 6945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6945,
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

_source line 32 · 2026-05-22T03:32:14.968Z_

<details><summary>↩ Tool result · `toolu_0188FGggpH6muag46J9TSS37`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7d3ca75-8852-409b-a567-845fbe9fdaa8",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "f697eb46-1cb9-437d-9fb6-8daa420657a0",
  "sourceToolAssistantUUID": "b7d3ca75-8852-409b-a567-845fbe9fdaa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T03:32:19.138Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017BsCSH8TRigXWXbZ3saT7q`</summary>

```json
{
  "pattern": "**/dream_reports/dream_20260522T023801/**/*",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f697eb46-1cb9-437d-9fb6-8daa420657a0",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuJ1sfBe6nvn3TMj91m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51055f42-a506-4604-b6ea-5a0bef667057",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1rcm22geVusUcx5xdASnK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 42552,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 406
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 42552,
          "cache_creation_input_tokens": 406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 406,
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

_source line 34 · 2026-05-22T03:32:19.243Z_

<details><summary>↩ Tool result · `toolu_017BsCSH8TRigXWXbZ3saT7q`</summary>

```text
artifacts/dream_reports/dream_20260522T023801/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260522T023801/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260522T023801/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260522T023801/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260522T023801/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T023801/best/experiment_data.json
artifacts/dream_reports/dream_20260522T023801/best/paper_framing.md
artifacts/dream_reports/dream_20260522T023801/best/paper.tex
artifacts/dream_reports/dream_20260522T023801/best/paper.aux
artifacts/dream_reports/dream_20260522T023801/best/paper.out
artifacts/dream_reports/dream_20260522T023801/best/paper.pdf
artifacts/dream_reports/dream_20260522T023801/best/paper.log
artifacts/dream_reports/dream_20260522T023801/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260522T023801/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T023801/median/experiment_data.json
artifacts/dream_reports/dream_20260522T023801/median/paper_framing.md
artifacts/dream_reports/dream_20260522T023801/median/paper.tex
artifacts/dream_reports/dream_20260522T023801/median/paper.aux
artifacts/dream_reports/dream_20260522T023801/median/paper.out
artifacts/dream_reports/dream_20260522T023801/median/paper.pdf
artifacts/dream_reports/dream_20260522T023801/median/paper.log
artifacts/dream_reports/dream_20260522T023801/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260522T023801/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T023801/worst/experiment_data.json
artifacts/dream_reports/dream_20260522T023801/worst/paper_framing.md
artifacts/dream_reports/dream_20260522T023801/worst/references.bib
artifacts/dream_reports/dream_20260522T023801/worst/paper.tex
artifacts/dream_reports/dream_20260522T023801/worst/paper.bbl
artifacts/dream_reports/dream_20260522T023801/worst/paper.blg
artifacts/dream_reports/dream_20260522T023801/worst/paper.aux
artifacts/dream_reports/dream_20260522T023801/worst/paper.out
artifacts/dream_reports/dream_20260522T023801/worst/paper.pdf
artifacts/dream_reports/dream_20260522T023801/worst/paper.log
artifacts/dream_reports/dream_20260522T023801/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260522T023801/best/review_context.yaml
artifacts/dream_reports/dream_20260522T023801/logs/review_best.log
artifacts/dream_reports/dream_20260522T023801/median/review_context.yaml
artifacts/dream_reports/dream_20260522T023801/best/review_report.md
artifacts/dream_reports/dream_20260522T023801/logs/review_median.log
artifacts/dream_reports/dream_20260522T023801/median/review_report.md
artifacts/dream_reports/dream_20260522T023801/logs/orchestrator.log
artifacts/dream_reports/dream_20260522T023801/worst/review_context.yaml
artifacts/dream_reports/dream_20260522T023801/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51055f42-a506-4604-b6ea-5a0bef667057",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "5b7f5883-75b5-4054-aa18-3ac9cb3e2039",
  "sourceToolAssistantUUID": "51055f42-a506-4604-b6ea-5a0bef667057",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T03:32:22.446Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q5ARK39wzhewGQSNhGUhZQ`</summary>

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
  "parentUuid": "5b7f5883-75b5-4054-aa18-3ac9cb3e2039",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuJKzpzksPSvuP79LNG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9758167f-2b5f-4b26-98dd-309f7a60711a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015aVAq2Bdw6LKUSYiY3NYv2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1102,
      "cache_read_input_tokens": 42958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1102,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 36 · 2026-05-22T03:32:22.754Z_

<details><summary>↩ Tool result · `toolu_01Q5ARK39wzhewGQSNhGUhZQ`</summary>

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
  "parentUuid": "9758167f-2b5f-4b26-98dd-309f7a60711a",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "37ad8fa5-c975-4cbb-8d5b-64d944c81598",
  "sourceToolAssistantUUID": "9758167f-2b5f-4b26-98dd-309f7a60711a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T03:32:23.071Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Muq2CbsQVDAVh3JiUqNDYL`</summary>

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
  "parentUuid": "37ad8fa5-c975-4cbb-8d5b-64d944c81598",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuJKzpzksPSvuP79LNG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f78e2fd-f811-4c0c-a185-0c5a7df265f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015aVAq2Bdw6LKUSYiY3NYv2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1102,
      "cache_read_input_tokens": 42958,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1102
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 42958,
          "cache_creation_input_tokens": 1102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1102,
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

_source line 38 · 2026-05-22T03:32:23.544Z_

<details><summary>↩ Tool result · `toolu_01Muq2CbsQVDAVh3JiUqNDYL`</summary>

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
  "parentUuid": "0f78e2fd-f811-4c0c-a185-0c5a7df265f1",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "a3934cee-74d6-4381-9d69-6fe7697e50a9",
  "sourceToolAssistantUUID": "0f78e2fd-f811-4c0c-a185-0c5a7df265f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-22T03:32:26.817Z_

Now let me check the actual experimental code to verify reproducibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3934cee-74d6-4381-9d69-6fe7697e50a9",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuJeRbu7AUnZFB9RMkx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "436bc92b-0078-4392-a8ec-a353ea4d52aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNFeTn6DGvB9MQbpmgEDDM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32261,
      "cache_read_input_tokens": 44060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32261,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 40 · 2026-05-22T03:32:28.439Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SJGYMtLCuxhBGLBtGZ5vY8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/src/train_probe.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "436bc92b-0078-4392-a8ec-a353ea4d52aa",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuJeRbu7AUnZFB9RMkx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d0a0fc6-bdd7-4190-a1b4-32c8fa664f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNFeTn6DGvB9MQbpmgEDDM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32261,
      "cache_read_input_tokens": 44060,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32261
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 44060,
          "cache_creation_input_tokens": 32261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32261,
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

_source line 41 · 2026-05-22T03:32:28.445Z_

<details><summary>↩ Tool result · `toolu_01SJGYMtLCuxhBGLBtGZ5vY8`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d0a0fc6-bdd7-4190-a1b4-32c8fa664f23",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "6e54ca67-daec-4ff7-9ca6-62dc2e354344",
  "sourceToolAssistantUUID": "7d0a0fc6-bdd7-4190-a1b4-32c8fa664f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-22T03:32:35.159Z_

I now have sufficient context to write a thorough review. Let me examine one more critical piece -- the discrepancy between the paper as submitted (the "best" dream paper) and the actual state of experiments as documented in the ROADMAP.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e54ca67-daec-4ff7-9ca6-62dc2e354344",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuK1c4nxom4oZsWRccJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dd2fabe-45de-4065-8c9d-bc2d2c1c3680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019541JVxwZqpjvFYM7uMEpL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1349,
      "cache_read_input_tokens": 76321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1349,
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

_source line 43 · 2026-05-22T03:32:36.331Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C2VkhyDDD3nbZiUJLirDSc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dd2fabe-45de-4065-8c9d-bc2d2c1c3680",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuK1c4nxom4oZsWRccJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7eebd8cc-cb4a-4f40-a575-48fe3db3f949",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019541JVxwZqpjvFYM7uMEpL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1349,
      "cache_read_input_tokens": 76321,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1349
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 76321,
          "cache_creation_input_tokens": 1349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1349,
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

_source line 44 · 2026-05-22T03:32:36.336Z_

<details><summary>↩ Tool result · `toolu_01C2VkhyDDD3nbZiUJLirDSc`</summary>

```text
1	---
2	dream_id: dream_20260522T023801
3	tier: best
4	overall_score: 5 - Marginally below acceptance threshold
5	timestamp: 2026-05-22T03:24:45.301030+00:00
6	---
7	
8	
9	---
10	reviewer: R1 (Methods & Experiments Focus)
11	venue: ICLR 2027
12	paper: "Cross-Lingual Knowledge Conflict Signals in Multilingual LLMs: Directional Asymmetry, Layer Structure, and Causal Probing"
13	---
14	
15	### Summary
16	
17	This paper investigates how cross-lingual knowledge conflict signals are encoded in the residual stream of multilingual LLMs, using linear probes, CKA/SVCCA analysis, SAE feature decomposition, and representation steering across three architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) and two language pairs (EN-ZH, EN-JA). The central finding is a directional asymmetry in cross-lingual probe transfer: transfer toward English (X->EN) consistently outperforms transfer away from English (EN->X) by 6.3-7.9pp across all model-language-pair combinations. The paper frames this within a hypothesis-testing structure (H1: English-anchored universal detection vs. H2: language-pair-specific encoding) and marshals three tracks of evidence -- probing, SAE decomposition, and causal steering -- to support H1. The paper is ambitious in scope and commendably transparent about limitations.
18	
19	### Strengths
20	
21	**S1. Hypothesis-driven structure is exemplary for interpretability research.** The H1 vs. H2 framework generates specific, falsifiable predictions (mid-layer > late-layer Jaccard; directional consistency across language pairs) that are then tested. This elevates the work above typical exploratory probing studies. The pre-registered competing hypotheses are the methodological highlight of the paper.
22	
23	**S2. Three-track convergence provides increasingly strong evidence types.** The detection (probing) -> decomposition (SAE) -> intervention (steering) pipeline is well-conceived. The fact that the steering flip rate asymmetry (ZH->EN 24.3% > EN->ZH 17.8% for Llama probe-based; ZH->EN 31.0% > EN->ZH 24.0% for SAE-based) mirrors the probe transfer asymmetry is the paper's strongest individual result, because it moves the asymmetry claim from correlational to causal territory. This triangulation design is a genuine methodological contribution.
24	
25	**S3. Cross-architecture effect size consistency is striking.** The asymmetry gaps of +7.2pp / +7.2pp / +7.9pp across three architectures with CV < 6% is remarkably homogeneous. The Cochran's Q test (p=0.68, I-squared=0%) provides appropriate meta-analytic justification. Even if individual models have borderline significance, this homogeneity is itself strong evidence that the effect is real rather than artifactual.
26	
27	**S4. Confound exclusion pipeline is thorough and well-designed.** The COMET tercile ablation is the right experiment: rather than imposing an arbitrary quality threshold, the authors directly test whether translation quality predicts probe accuracy, finding a null/reversed relationship (delta = -1.6pp Llama, -5.6pp Qwen, Fisher p > 0.69). The token overlap analysis (per-sample Jaccard 3-4%, negative correlation in Llama) correctly addresses a plausible alternative explanation. The label noise robustness curve (graceful degradation at ~2.6pp per 5% noise) provides appropriate safety margins given the pipeline's estimated <5% error rate. These three controls together form a solid confound exclusion argument.
28	
29	**S5. The steering experiment includes appropriate controls.** Random orthogonal directions as control (5-6% flip rate vs. 18-34% active) is the right baseline. Coherence preservation at 91% addresses the concern that steering simply degrades outputs. The feature-set ablation (shared features 28% vs. language-specific 9-11%) is a particularly incisive test of H1.
30	
31	**S6. Honest reporting of negative/inconclusive results.** The SAE base-instruct mismatch (Appendix B), the Qwen CI including zero at n~1000, the EN-JA gap not reaching significance -- these are reported straightforwardly without spin. This builds credibility.
32	
33	### Weaknesses
34	
35	**W1 (Major). The "English-anchored conflict detection" claim is confounded with general English-anchored cross-lingual transfer.** The X->EN > EN->X asymmetry could be a general property of any cross-lingual semantic probing task on English-dominant models, not specific to conflict detection. English occupies a privileged position in the representation space of all three models due to pre-training data composition. The paper provides no non-conflict semantic baseline (e.g., probing for entailment, factual category, or sentiment across languages) to demonstrate that the asymmetry is conflict-specific. Without this control, the contribution reduces from "novel mechanistic finding about conflict encoding" to "replication of known cross-lingual transfer asymmetry on a new task." This is computationally trivial to add -- the entire probing pipeline exists, only the labels change -- making its absence particularly conspicuous.
36	
37	**W2 (Major). Statistical power is insufficient for the central claim (C2).** At the reported sample sizes, only 2/3 models (or 3/4 model-language-pair combinations in the best-case scenario) reach 95% CI significance for the asymmetry. The paper's use of Cumming (2014) "new statistics" framing -- emphasizing effect sizes and CIs over NHST -- is legitimate in principle but risks appearing as post-hoc rationalization when applied selectively to the one model that fails significance. Specific issues:
38	
39	- Bootstrap n=100 is below the conventional minimum of n>=1000 (Efron & Tibshirani 1993). At n=100, the 2.5th percentile is literally the 2nd or 3rd most extreme value, making CI endpoints highly volatile. For a claim where the lower CI bound matters (Qwen's -1.2pp), this is consequential. This is cheap to fix.
40	- The permutation test uses n=1000, which is adequate for p<0.001 claims but the paper does not report exact permutation p-values for the asymmetry itself (only for the per-direction probe accuracy vs. chance).
41	- The dataset expansion from n~1000 to n~1800 (Section 4.1) tightens the Qwen CI to [2.3, 11.7], which does exclude zero. But the paper presents both the original and expanded results, and the expanded dataset is not used for all subsequent analyses (CKA, steering, etc.), creating an inconsistency in the evidence base.
42	
43	**W3 (Major). Both language pairs are CJK languages -- typological diversity is insufficient for "universal" claims.** EN-ZH and EN-JA share the CJK cultural sphere and similar embedding in English-dominant training corpora. H2 predicts language-pair-specific patterns; testing only pairs where the non-English languages are typologically similar cannot meaningfully falsify H2. An Indo-European pair (EN-DE, EN-FR) or a morphologically rich language (EN-TR, EN-FI) would provide a genuine test. The paper uses "universal" language in the H1 formulation but the evidence supports only "consistent across two CJK pairs."
44	
45	**W4 (Moderate). SAE analysis operates on base model while probing operates on instruct model -- the cross-validation is weaker than claimed.** The Qwen-Scope SAEs are trained on Qwen3-8B-Base. RLHF/instruction tuning systematically reorganizes representations, particularly in mid-to-late layers -- precisely where the paper claims critical conflict processing occurs. The paper's acknowledgment (Appendix B) that base-instruct cosine similarity is only 0.71 and only 35% of features are interpretable on the instruct model actually undermines rather than supports cross-track validation. The Jaccard analysis (Table 8) operates entirely in the SAE's base-model feature space, and projecting these results onto instruct-model behavior is a logical gap. Furthermore, SAE analysis covers only Qwen -- there is no cross-architecture SAE validation.
46	
47	**W5 (Moderate). Probe accuracy of 69-77% is substantially below prior monolingual work (~90+ F1) without adequate explanation.** The 23-31% undetectable fraction is non-trivial. The paper claims conflict signals are "linearly detectable" but does not characterize what fraction of the signal is linear vs. non-linear (the MLP analysis addresses only the cross-lingual transfer direction, not within-language detectability ceiling). Possible explanations -- intrinsic difficulty of the cross-lingual setting, label noise from the verification pipeline, genuinely distributed/non-linear signal -- are not systematically investigated or distinguished.
48	
49	**W6 (Moderate). The CKA-probe correlation (r = -0.71) is computed over 3 data points.** This cannot be presented as a statistical finding. Three points always produce a correlation that appears large. The paper should report the raw numbers and qualitative pattern without computing a correlation coefficient or implying statistical meaning.
50	
51	**W7 (Moderate). Steering captures a minority of samples without characterization of non-responding samples.** Flip rates of 17-35% mean 65-83% of samples are unaffected. The paper does not analyze which samples respond to steering vs. which do not. If non-responding samples are systematically different (e.g., higher model confidence, different entity types, different conflict types), this would significantly refine the mechanistic story. The Cohen's d of 0.41 is a small-to-medium effect, honestly reported, but the paper would benefit from connecting this to the probe accuracy ceiling (W5).
52	
53	**W8 (Minor). Small feature counts make Jaccard statistics fragile.** The mid-layer Jaccard of 0.28 is based on 8 shared features out of 21 EN and 18 ZH features. The late-layer Jaccard of 0.12 is based on 3 shared features out of 14 EN and 10 ZH features. Reclassifying a single feature (e.g., by shifting the MI threshold by 0.01) could move mid-layer Jaccard from 0.28 to 0.23 or 0.33. No sensitivity analysis over the MI > 0.15 threshold or filtering criteria is provided.
54	
55	**W9 (Minor). MLP probe overfitting risk is not addressed.** A single hidden layer with 256 units trained on ~1000 samples risks overfitting, especially in the EN->ZH direction where the MLP gain is largest (up to 6.1pp for Gemma). The paper does not report the train-test accuracy gap for MLP probes. Without this, the MLP gains could partially reflect overfitting rather than genuine non-linear signal.
56	
57	**W10 (Minor). Using the same model for translation and probing introduces circularity potential.** The target models themselves generate the Chinese/Japanese translations. If the model's translation biases systematically correlate with its internal conflict representations, the translated text could contain subtle cues that inflate probe accuracy for within-model transfer. Using an independent translation model (or professional human translation for a subset) would control for this.
58	
59	### Questions for Authors
60	
61	**Q1 (Critical).** Have you tested the X->EN > EN->X asymmetry on a non-conflict semantic task using the same pipeline? This is the single most important experiment missing from the paper. If the same asymmetry appears for sentiment or topic probing, the conflict-specificity claim is falsified.
62	
63	**Q2.** Why was bootstrap n set to 100 rather than the conventional >=1000? The entire probing pipeline uses logistic regression, so each bootstrap iteration takes seconds. Was this a deliberate choice or an oversight?
64	
65	**Q3.** For the steering experiment, how was the optimal alpha (reported as 2.5 for probe-based, 3.5 in the summary) selected? Was it tuned on a held-out validation set or on the test set? If the latter, flip rates are optimistically biased.
66	
67	**Q4.** How is "coherence preserved at 91%" operationalized? Is this human evaluation, an automated metric (e.g., perplexity delta), or something else? The paper does not define this metric.
68	
69	**Q5.** In Table 3 (MLP non-linearity), the text claims the gain anti-correlates with Chinese pre-training data proportion. What are the actual Chinese data proportions for these three models? Gemma-2-9B-IT having the largest non-linear gain (+6.1pp) seems surprising given Google's substantial multilingual training data.
70	
71	**Q6.** For the SAE analysis, why not run the probing track on the base model as well, to enable direct comparison within the same model version? This would eliminate the base-instruct mismatch entirely for at least one architecture.
72	
73	**Q7.** The paper reports balanced accuracy throughout. What is the class balance in the test sets? If close to 50/50, balanced and unbalanced accuracy are equivalent and reporting both would increase transparency.
74	
75	### Missing Experiments/Controls
76	
77	1. **Non-conflict semantic baseline (Critical).** Probe for a non-conflict binary semantic distinction (entailment, sentiment, factual category) and measure whether the X->EN > EN->X asymmetry persists. If it does, reframe the contribution. If it does not, the conflict-specificity claim is validated. Computationally trivial.
78	
79	2. **Non-CJK language pair (High).** EN-DE, EN-FR, or EN-TR would test whether the pattern holds across typological families. Without this, "universal" framing is unsupported.
80	
81	3. **Bootstrap n >= 2000 (Medium).** Increase bootstrap iterations for all CI computations. Cheap, strengthens all CI-based claims.
82	
83	4. **MLP train-test gap analysis (Medium).** Report MLP probe accuracy on training data alongside test data to assess overfitting, especially for the EN->ZH direction where gains are largest.
84	
85	5. **Steering alpha selection protocol (Medium).** Clarify whether alpha was tuned on test data (leakage) or a held-out validation split. If the former, re-run with proper held-out tuning.
86	
87	6. **Characterization of steering non-responders (Low-Medium).** Analyze properties of the 65-83% of samples that do not flip under steering: model confidence, entity type, COMET score, conflict type.
88	
89	7. **SAE sensitivity analysis (Low-Medium).** Vary the MI > 0.15 threshold and filtering criteria to demonstrate that the mid-layer > late-layer Jaccard finding is robust to these choices.
90	
91	8. **Independent translation control (Low).** Use an independent translation model (not the probing target) for a subset to verify that same-model translation does not inflate results.
92	
93	### Scores
94	
95	| Dimension | Score | Justification |
96	|-----------|-------|---------------|
97	| **Soundness** | **3 / 4** | Methods are generally appropriate and correctly applied. Probing framework, permutation testing, CKA analysis, and steering controls are sound. Deductions for: missing non-conflict baseline (the largest methodological gap), bootstrap n=100 inadequacy, base-instruct SAE mismatch, r=-0.71 on 3 points, and no MLP overfitting control. The statistical framework is competent but not airtight. |
98	| **Presentation** | **3 / 4** | Paper is clearly written with a logical structure. H1/H2 framework aids readability. 13 tables create visual density but are individually well-designed. Limitations section is honest. Deductions for: thin bibliography (8 references), missing definition of "coherence preservation," and some overclaiming relative to evidence (e.g., "universal" with only CJK pairs). |
99	| **Contribution** | **3 / 4** | Novel intersection of mechanistic interpretability and multilingual NLP. The three-track convergence design and the specific finding of probe-steering asymmetry alignment are genuine contributions. However, if the non-conflict baseline reveals the asymmetry is a general cross-lingual transfer property (W1), the contribution drops to incremental. Current contribution is conditional on this experiment's outcome. |
100	| **Overall** | **5** | Marginally below acceptance threshold. The paper asks a genuinely interesting question and designs a methodologically sophisticated multi-track investigation. Cross-architecture consistency is impressive, confound controls are thorough, and the steering-probing alignment is a strong result. However, the missing non-conflict baseline (W1) introduces fundamental interpretive ambiguity in the central claim, both language pairs are CJK (W3), bootstrap n=100 is inadequate for the precision required (W2), and the SAE base-instruct mismatch (W4) weakens the cross-track validation that is the paper's structural signature. These are addressable in revision -- the non-conflict baseline and bootstrap increase are computationally trivial, and one non-CJK language pair would significantly strengthen the "universal" framing. I would raise my score to 6 if the non-conflict baseline confirms conflict-specificity and one non-CJK pair is added. |
101	| **Confidence** | **4 / 5** | I have examined the source code, experimental artifacts, bootstrap results, and paper text in detail. I am confident in my assessment of the methods and statistical procedures. My main uncertainty is whether the SAE analysis (Track 2) results in the "best" tier are imagined vs. actual -- this does not affect my evaluation of Track 1, which is grounded in real experimental results. |
102	
103	### Recommendation
104	
105	**Marginally below acceptance threshold (5/10). Revise and resubmit.**
106	
107	The paper presents a well-motivated investigation at a productive intersection of two fields, with a commendable hypothesis-driven design and multi-track evidence structure. The cross-architecture consistency of the asymmetry effect and the probing-steering alignment are strong results.
108	
109	However, three issues prevent acceptance in current form:
110	
111	1. **The missing non-conflict baseline is a fatal gap for the central claim.** Without demonstrating that the directional asymmetry is conflict-specific rather than a general property of cross-lingual transfer, the paper's main contribution is underdetermined. This is a cheap experiment that must be run.
112	
113	2. **Typological diversity is insufficient for "universal" claims.** Two CJK language pairs cannot distinguish H1 (universal English anchoring) from a CJK-specific pattern. One Indo-European pair would substantially strengthen the evidence.
114	
115	3. **Statistical infrastructure needs tightening.** Bootstrap n=100 is below standard for the precision required by the paper's claims. The r=-0.71 on 3 points should not be reported as a statistical finding. MLP overfitting needs to be ruled out.
116	
117	The paper's strengths -- novel question, clean experimental design, honest reporting, and genuine triangulation -- position it well for acceptance after revision. The required experiments are computationally inexpensive (non-conflict baseline, bootstrap increase) or moderately expensive (one non-CJK language pair). I encourage the authors to address W1-W3 and resubmit.
118	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7eebd8cc-cb4a-4f40-a575-48fe3db3f949",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "85ac694c-9b27-4818-b5b6-4c036f567290",
  "sourceToolAssistantUUID": "7eebd8cc-cb4a-4f40-a575-48fe3db3f949",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-22T03:32:42.147Z_

Now I have comprehensive context. Let me also check the actual paper that was submitted for review (the "summary" in the task description mentions a paper with Gemma showing +1.0pp asymmetry, which differs from the "best" dream paper). This suggests I should review based on the paper summary provided in the task prompt, not the "best-case" dream paper. Let me check the "median" version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85ac694c-9b27-4818-b5b6-4c036f567290",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuKbGNfvmgz8VSFHZJt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93bca854-657f-4af1-9111-60004d262b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbGTRzHQSFpUmzVdDQVR9f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4983,
      "cache_read_input_tokens": 77670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4983,
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

_source line 46 · 2026-05-22T03:32:44.400Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XECeGTKP33gq3psNBRPtzH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.tex",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93bca854-657f-4af1-9111-60004d262b39",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuKbGNfvmgz8VSFHZJt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c693b9d-9773-4cf1-ab8a-5293233b6818",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbGTRzHQSFpUmzVdDQVR9f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4983,
      "cache_read_input_tokens": 77670,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4983
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 77670,
          "cache_creation_input_tokens": 4983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4983,
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

_source line 47 · 2026-05-22T03:32:44.419Z_

<details><summary>↩ Tool result · `toolu_01XECeGTKP33gq3psNBRPtzH`</summary>

```text
1	\documentclass{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{hyperref}
8	\usepackage{xcolor}
9	\usepackage{natbib}
10	\usepackage[margin=1in]{geometry}
11	\usepackage{multirow}
12	\usepackage{array}
13	\usepackage{caption}
14	
15	\title{Cross-Lingual Knowledge Conflict Signals in Multilingual LLMs:\\Directional Asymmetry, Layer Structure, and Causal Probing}
16	
17	\author{
18	  Anonymous Authors
19	}
20	
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	%% ===== ABSTRACT =====
27	\begin{abstract}
28	Multilingual large language models (LLMs) must resolve knowledge conflicts when parametric memory and contextual evidence disagree across languages. Recent work (CLEAR; Zhao et al., 2026) shows that linguistic affinity governs conflict resolution in entity-centric factual tasks, but the internal mechanism remains unknown. We present a systematic investigation of how cross-lingual conflict signals are encoded in residual stream representations.
29	
30	Using linear probes across three architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) and two language pairs (EN--ZH, EN--JA), we establish three findings.
31	First, conflict signals are linearly detectable in residual streams with balanced accuracy 69--77\% across all models, far above chance (\emph{C1}).
32	Second, cross-lingual probe transfer exhibits a \emph{remarkably consistent} directional asymmetry: ZH$\to$EN transfer exceeds EN$\to$ZH by a pooled effect of $6.6 \pm 0.9$ percentage points across all three architectures (range 5.4--7.2\,pp), with $I^2 = 0\%$ heterogeneity, despite only 1/3 models reaching conventional significance---emphasizing effect-size stability over $p$-values (\emph{C2}).
33	Third, layer-wise CKA analysis reveals that conflict detection peaks during the language-universal-to-specific transition window (50--55\% depth), with probe accuracy peaking at architecture-dependent depths (67--88\%) (\emph{C4}).
34	
35	Representation steering using probe-weight directions yields answer-flip rates of 18--34\% (vs.\ 6\% random control, Cohen's $d = 0.41$), providing correlational evidence consistent with a causal role for the detected signal. Preliminary sparse autoencoder analysis is reported in the appendix as an honest boundary of current tools. Our work provides the first mechanistic account of cross-lingual conflict encoding and contributes a confound-exclusion methodology (token overlap analysis, COMET ablation, label noise robustness) applicable to future cross-lingual probing studies.
36	\end{abstract}
37	
38	%% ===== 1. INTRODUCTION =====
39	\section{Introduction}
40	
41	When multilingual LLMs encounter knowledge conflicts---cases where parametric memory and contextual evidence provide contradictory answers---they must resolve the conflict, often in language-dependent ways. CLEAR \citep{zhao2026clear} demonstrated that for entity-centric factual conflicts, \emph{linguistic affinity} (typological similarity between source and target languages) is the primary determinant of conflict resolution, rather than resource abundance. However, CLEAR characterizes this as a behavioral phenomenon without explaining the underlying mechanism: \emph{how} are conflict signals encoded internally, and \emph{why} does linguistic similarity matter?
42	
43	We address this mechanistic gap through three complementary analysis tracks. \textbf{Track~1} (probing) establishes that cross-lingual conflict signals are linearly detectable in residual streams and exhibit directional transfer asymmetry. \textbf{Track~2} (sparse autoencoder analysis) attempts to decompose conflict features at the individual neuron level. \textbf{Track~3} (causal steering) tests whether detected signals play a causal role in conflict resolution.
44	
45	Our investigation is guided by two competing hypotheses:
46	\begin{itemize}
47	    \item \textbf{H1 (English-anchored universal detection)}: Conflict detection is language-independent, encoded in mid-layer shared representations. The English-dominant training distribution anchors the representation space, making English the ``lingua franca'' of internal conflict encoding.
48	    \item \textbf{H2 (Language-pair-specific encoding)}: Conflict features are language-pair-specific from mid-layers onward, with linguistic distance directly encoded in conflict representations.
49	\end{itemize}
50	
51	Our results favor a variant of H1: across three architectures spanning two design families (GQA vs.\ parallel attention), ZH$\to$EN transfer consistently exceeds EN$\to$ZH with a pooled effect of $6.6 \pm 0.9$\,pp and zero heterogeneity ($I^2 = 0\%$). Following the ``new statistics'' framework \citep{cumming2014new}, we emphasize this remarkably stable effect size over individual $p$-values: only Llama-3.1-8B reaches conventional significance, but the consistent directionality across 3/3 models and the narrow effect-size range (5.4--7.2\,pp) provide stronger evidence than any single test.
52	
53	Our contributions are:
54	\begin{enumerate}
55	    \item \textbf{Phenomenon characterization}: First demonstration that cross-lingual conflict signals are linearly detectable and exhibit architecture-consistent directional asymmetry (Section~\ref{sec:detectability}--\ref{sec:asymmetry}).
56	    \item \textbf{Methodology}: A confound-exclusion pipeline comprising token-overlap analysis, COMET translation-quality ablation, and label-noise robustness testing, applicable to future cross-lingual probing studies (Section~\ref{sec:method}).
57	    \item \textbf{Mechanistic analysis}: Layer-wise CKA/SVCCA analysis linking conflict signal peaks to the language transition window \citep{wendler2024lost}, plus probe-based representation steering providing preliminary causal evidence (Sections~\ref{sec:layerwise}--\ref{sec:steering}).
58	\end{enumerate}
59	
60	%% ===== 2. RELATED WORK =====
61	\section{Related Work}
62	
63	\paragraph{Knowledge conflicts in LLMs.}
64	Knowledge conflicts arise when parametric and contextual information disagree \citep{longpre2021entity,chen2022rich,xie2024adaptive}. Most work focuses on monolingual (English) settings. ConflictQA \citep{xie2024adaptive} provides entity-centric factual conflicts; CLEAR \citep{zhao2026clear} extends this to multilingual settings, finding that linguistic affinity governs resolution in entity-centric tasks.
65	
66	\paragraph{Cross-lingual representations.}
67	Multilingual transformers develop shared representations across languages in intermediate layers, transitioning to language-specific representations in upper layers \citep{pires2019multilingual,chi2020finding,wendler2024lost}. The ``language transition'' typically begins at 50--60\% depth. Our CKA analysis connects conflict signal encoding to this transition.
68	
69	\paragraph{Mechanistic interpretability.}
70	Linear probing \citep{belinkov2022probing} remains a standard tool for detecting encoded information. Sparse autoencoders (SAEs) decompose activations into interpretable features \citep{bricken2023monosemanticity,cunningham2023sparse}. SpARE \citep{wu2025spare} demonstrates SAE-based steering for monolingual knowledge conflicts. We extend probing to cross-lingual conflicts and report preliminary SAE results as an honest boundary assessment.
71	
72	\paragraph{Representation steering.}
73	Activation addition \citep{turner2023activation} and related techniques modify model behavior by adding steering vectors. We use probe-weight directions as steering vectors, following \citet{marks2024geometry}, providing correlational evidence for the causal relevance of detected conflict signals.
74	
75	%% ===== 3. METHOD =====
76	\section{Method}
77	\label{sec:method}
78	
79	\subsection{Data Construction}
80	
81	We use ConflictQA \citep{xie2024adaptive} as the primary source of entity-centric factual conflicts. Each instance contains a question with both a parametric answer (from the model's training data) and a contextual answer (from a provided passage), where these answers disagree.
82	
83	\paragraph{Translation and verification.}
84	English instances are translated to Chinese (ZH) and Japanese (JA) using a neural MT pipeline. Translation quality is verified via back-translation COMET scores. For EN--ZH, $n \approx 1{,}000$ instances pass quality filters; for EN--JA, $n \approx 680$ (lower coverage due to Wikidata JA label sparsity).
85	
86	\paragraph{Dataset expansion.}
87	To strengthen statistical power, we expand the EN--ZH dataset to $n \approx 1{,}800$ by additional ConflictQA sampling and incorporating a ParaRel-conflict subset. Cross-dataset consistency is 0.92.
88	
89	\subsection{Probing Framework}
90	
91	For each model and language, we extract residual-stream activations at every layer for conflict vs.\ non-conflict instances. We train logistic regression probes (L2-regularized) on these activations.
92	
93	\paragraph{Transfer protocol.}
94	We train probes in four configurations: EN$\to$EN, ZH$\to$ZH, EN$\to$ZH, and ZH$\to$EN (and analogously for JA). The cross-lingual transfer gap---$\text{acc}(\text{ZH}\to\text{EN}) - \text{acc}(\text{EN}\to\text{ZH})$---quantifies directional asymmetry.
95	
96	\paragraph{Statistical testing.}
97	All accuracy estimates use balanced accuracy with 100-iteration bootstrap confidence intervals. Permutation tests ($n = 10{,}000$) assess above-chance performance. For the asymmetry gap, we report bootstrap CIs and the fraction of positive bootstrap iterations.
98	
99	\subsection{Confound Exclusion Pipeline}
100	
101	\paragraph{Token overlap control.}
102	Cross-lingual transfer might be driven by shared tokens (numbers, proper nouns, punctuation). We compute per-sample Jaccard similarity between EN and ZH token sets and test its correlation with probe accuracy.
103	
104	\paragraph{COMET translation quality ablation.}
105	We stratify instances into COMET terciles and compare probe accuracy across quality bins to test whether translation quality confounds conflict detection.
106	
107	\paragraph{Label noise robustness.}
108	We inject 5--20\% systematic label noise and measure probe degradation to bound the impact of verification pipeline errors (estimated at $\sim$4\%).
109	
110	\subsection{Layer-wise Representation Analysis}
111	
112	We compute Centered Kernel Alignment (CKA; \citealp{kornblith2019similarity}) and SVCCA \citep{raghu2017svcca} between EN and ZH conflict activations at each layer to track cross-lingual representation similarity. We identify the language-transition onset as the layer where CKA drops below 0.80.
113	
114	\subsection{Representation Steering}
115	
116	We use probe weight vectors as steering directions, adding $\alpha \cdot \mathbf{w}_{\text{probe}}$ to residual-stream activations at the best probe layer. We measure the answer-flip rate (fraction of instances where the model's answer changes from parametric to contextual or vice versa) and coherence preservation rate. A random orthogonal direction serves as control.
117	
118	\subsection{Preliminary SAE Analysis}
119	
120	We apply Qwen-Scope pretrained SAEs (65,536 features, trained on Qwen3-8B-Base) to analyze conflict activations. We select features by mutual information (MI $> 0.15$) and apply LangFIR random-token filtering to separate language-identity from conflict features. Due to the base--instruct distribution mismatch (Appendix~\ref{app:sae}), these results are preliminary.
121	
122	%% ===== 4. EXPERIMENTS AND RESULTS =====
123	\section{Experiments and Results}
124	
125	\subsection{Cross-Lingual Conflict Detectability (C1)}
126	\label{sec:detectability}
127	
128	Table~\ref{tab:expanded} shows that expanding the dataset from $n \approx 1{,}000$ to $n \approx 1{,}800$ (Llama-3.1-8B, EN--ZH) tightens the asymmetry CI from [1.1, 13.6] to [2.3, 11.7]\,pp while preserving the effect size at 7.0\,pp. Across all models and configurations, within-language probe accuracy ranges from 69.4\% to 77.1\% (balanced), with all permutation $p$-values $ < 0.01$, confirming that conflict signals are robustly detectable in residual streams.
129	
130	\begin{table}[t]
131	\centering
132	\caption{Dataset expansion effect on asymmetry CI (Llama-3.1-8B, EN--ZH).}
133	\label{tab:expanded}
134	\begin{tabular}{lcccc}
135	\toprule
136	Dataset & $n$ & Gap (pp) & 95\% CI & Significant? \\
137	\midrule
138	ConflictQA original & $\sim$1000 & 7.22 & [1.1, 13.6] & Yes (borderline) \\
139	ConflictQA expanded & $\sim$1500 & 7.0 & [1.8, 12.2] & Yes \\
140	+ ParaRel subset & $\sim$1800 & 7.0 & [2.3, 11.7] & Yes \\
141	\bottomrule
142	\end{tabular}
143	\end{table}
144	
145	\subsection{Cross-Architecture Asymmetry Consistency (C2)}
146	\label{sec:asymmetry}
147	
148	We extend our analysis to Gemma-2-9B-IT, an architecture employing parallel attention and GeGLU (distinct from the sequential GQA of Llama and Qwen). Table~\ref{tab:gemma} presents the Gemma transfer results.
149	
150	\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c693b9d-9773-4cf1-ab8a-5293233b6818",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "a87bf043-66ce-42b8-900f-e3c90934b979",
  "sourceToolAssistantUUID": "1c693b9d-9773-4cf1-ab8a-5293233b6818",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-22T03:32:48.189Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T8QFjN8cP9rXghfngLMJ4o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.tex",
  "offset": 150,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a87bf043-66ce-42b8-900f-e3c90934b979",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuLBoGWnSakJNWzromN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38600cc9-6ec3-47aa-9538-3e0215df80a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016b8Hu3FWh7imUeJQdoSYPC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3997,
      "cache_read_input_tokens": 82653,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3997
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 82653,
          "cache_creation_input_tokens": 3997,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3997,
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

_source line 49 · 2026-05-22T03:32:48.201Z_

<details><summary>↩ Tool result · `toolu_01T8QFjN8cP9rXghfngLMJ4o`</summary>

```text
150	\begin{table}[t]
151	\centering
152	\caption{Gemma-2-9B-IT probe transfer accuracy (balanced accuracy, $n = 100$ bootstrap).}
153	\label{tab:gemma}
154	\begin{tabular}{lccc}
155	\toprule
156	Train$\to$Test & Bal.\ Acc (\%) & 95\% CI & Perm.\ $p$ \\
157	\midrule
158	EN$\to$EN & 73.1 & [70.2, 76.0] & $<$0.001 \\
159	ZH$\to$ZH & 69.4 & [66.3, 72.5] & $<$0.001 \\
160	EN$\to$ZH & 64.1 & [59.9, 68.3] & 0.006 \\
161	ZH$\to$EN & 69.5 & [65.7, 73.3] & $<$0.001 \\
162	\midrule
163	Gap (ZH$\to$EN $-$ EN$\to$ZH) & +5.4 & [$-$0.8, 11.6] & --- \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	Table~\ref{tab:cross-arch} consolidates the three-model comparison. The pooled effect size is $6.6 \pm 1.0$\,pp (mean $\pm$ SD), with all three models showing the same direction (ZH$\to$EN $>$ EN$\to$ZH). A Cochran's $Q$ test yields $p = 0.68$, indicating no significant heterogeneity ($I^2 = 0\%$). Following \citet{cumming2014new}, this consistent effect size across architectures spanning two design families provides stronger evidence than the mixed significance pattern (1/3 reaching $p < 0.05$).
169	
170	\begin{table}[t]
171	\centering
172	\caption{Cross-architecture asymmetry consistency. Effect sizes are remarkably stable ($6.6 \pm 0.9$\,pp) despite varying statistical power.}
173	\label{tab:cross-arch}
174	\begin{tabular}{lcccc}
175	\toprule
176	Model & Gap (pp) & 95\% CI & Significant? & Direction \\
177	\midrule
178	Llama-3.1-8B & 7.22 & [1.1, 13.6] & Yes (borderline) & ZH$\to$EN $>$ EN$\to$ZH \\
179	Qwen3-8B & 7.18 & [$-$1.2, 13.4] & No & ZH$\to$EN $>$ EN$\to$ZH \\
180	Gemma-2-9B-IT & 5.4 & [$-$0.8, 11.6] & No & ZH$\to$EN $>$ EN$\to$ZH \\
181	\midrule
182	Mean $\pm$ SD & $6.60 \pm 1.04$ & --- & 1/3 sig, 3/3 consistent & --- \\
183	\bottomrule
184	\end{tabular}
185	\end{table}
186	
187	The Gemma gap (5.4\,pp) is 1.8\,pp below the Llama/Qwen values, which we attribute to Gemma's parallel attention providing more uniform cross-layer information flow, reducing the directional mapping difficulty differential. Importantly, 94/100 bootstrap iterations for Gemma are positive, and the non-significance reflects limited statistical power at this effect size, not absence of the effect.
188	
189	\subsection{Multilingual Extension: EN--JA}
190	\label{sec:multilingual}
191	
192	To test whether the asymmetry generalizes beyond EN--ZH, we extend to EN--JA on Llama-3.1-8B (Table~\ref{tab:ja}). Japanese is typologically more distant from English than Chinese (SOV word order, agglutinative morphology), providing a stronger test.
193	
194	\begin{table}[t]
195	\centering
196	\caption{EN$\leftrightarrow$JA probe transfer (Llama-3.1-8B, $n = 680$).}
197	\label{tab:ja}
198	\begin{tabular}{lccc}
199	\toprule
200	Train$\to$Test & Bal.\ Acc (\%) & 95\% CI & Perm.\ $p$ \\
201	\midrule
202	EN$\to$EN & 77.1 & [74.3, 79.9] & $<$0.001 \\
203	JA$\to$JA & 67.3 & [63.5, 71.1] & $<$0.001 \\
204	EN$\to$JA & 61.2 & [56.9, 65.5] & 0.021 \\
205	JA$\to$EN & 65.8 & [61.6, 70.0] & 0.002 \\
206	\midrule
207	Gap (JA$\to$EN $-$ EN$\to$JA) & +4.6 & [$-$2.1, 11.3] & --- \\
208	\bottomrule
209	\end{tabular}
210	\end{table}
211	
212	The same directional pattern holds: JA$\to$EN transfer (65.8\%) exceeds EN$\to$JA (61.2\%) by 4.6\,pp (88/100 bootstrap iterations positive). Table~\ref{tab:cross-lang} compares the two language pairs. The smaller gap for EN--JA (4.6 vs.\ 7.2\,pp) may reflect either greater typological distance compressing asymmetry or reduced statistical power from the smaller sample ($n = 680$ vs.\ ${\sim}1{,}000$). The consistent direction across both language pairs supports the English-anchored hypothesis (H1), though discriminating H1 from H2 requires additional language pairs.
213	
214	\begin{table}[t]
215	\centering
216	\caption{Cross-language-pair asymmetry comparison (Llama-3.1-8B).}
217	\label{tab:cross-lang}
218	\begin{tabular}{lcccc}
219	\toprule
220	Language Pair & Gap (pp) & 95\% CI & $n$ & Direction \\
221	\midrule
222	EN$\leftrightarrow$ZH & 7.22 & [1.1, 13.6] & $\sim$1000 & ZH$\to$EN $>$ EN$\to$ZH \\
223	EN$\leftrightarrow$JA & 4.6 & [$-$2.1, 11.3] & $\sim$680 & JA$\to$EN $>$ EN$\to$JA \\
224	\bottomrule
225	\end{tabular}
226	\end{table}
227	
228	\subsection{Layer-wise Representation Analysis (C4)}
229	\label{sec:layerwise}
230	
231	Table~\ref{tab:cka} shows CKA between EN and ZH conflict activations across layer groups in Llama-3.1-8B. CKA decreases monotonically from 0.92 (early layers) to 0.63 (final layers), consistent with the language-transition phenomenon \citep{wendler2024lost}. Probe accuracy peaks in the 60--85\% depth range where CKA is actively declining, and the correlation between probe peak and CKA drop is $r = -0.67$.
232	
233	\begin{table}[t]
234	\centering
235	\caption{Layer-wise CKA between EN and ZH conflict activations (Llama-3.1-8B). Probe accuracy peaks in the CKA transition zone.}
236	\label{tab:cka}
237	\begin{tabular}{lcccc}
238	\toprule
239	Layer Range & Depth \% & CKA (mean $\pm$ std) & Probe Acc (\%) \\
240	\midrule
241	0--8 & 0--25\% & $0.92 \pm 0.03$ & 54.2 \\
242	8--19 & 25--60\% & $0.78 \pm 0.05$ & 62.8 \\
243	19--27 & 60--85\% & $0.71 \pm 0.04$ & 73.6 \\
244	27--32 & 85--100\% & $0.63 \pm 0.06$ & 69.1 \\
245	\bottomrule
246	\end{tabular}
247	\end{table}
248	
249	Table~\ref{tab:transition} compares the language-transition onset and probe peak across models. The transition onset is consistent (50--55\% depth), but the probe peak varies substantially (67--88\% depth), suggesting that peak location is architecture-dependent while the transition zone itself is a shared property.
250	
251	\begin{table}[t]
252	\centering
253	\caption{Language transition onset and probe peak across architectures.}
254	\label{tab:transition}
255	\begin{tabular}{lccc}
256	\toprule
257	Model & Transition Onset (\%) & Probe Peak (\%) & CKA at Peak \\
258	\midrule
259	Llama-3.1-8B & 55\% & 88\% & 0.64 \\
260	Qwen3-8B & 50\% & 67\% & 0.73 \\
261	Gemma-2-9B-IT & 52\% & 72\% & 0.70 \\
262	\bottomrule
263	\end{tabular}
264	\end{table}
265	
266	SVCCA correlates highly with CKA ($r = 0.94$), confirming robustness across representation similarity metrics. The CKA difference between conflict and non-conflict instances peaks at 0.08 at the best probe layer---too small to support a strong claim that conflicts alter cross-lingual alignment, but consistent with a subtle perturbation.
267	
268	\subsection{PCA Visualization}
269	\label{sec:pca}
270	
271	Table~\ref{tab:pca} reports PCA clustering metrics across layers. The first two principal components explain only 23\% of variance, limiting the interpretive value of 2D projections. Nonetheless, two qualitative patterns emerge: (1)~EN--ZH overlap decreases from 0.78 (early) to 0.41 (late), paralleling the CKA decline; (2)~cross-lingual centroid distance increases from 0.82 to 2.08, consistent with progressive language specialization.
272	
273	\begin{table}[t]
274	\centering
275	\caption{PCA cluster metrics across layers (Llama-3.1-8B). Low silhouette values reflect the moderate probe accuracy ($\sim$75\%), not a clean separation.}
276	\label{tab:pca}
277	\begin{tabular}{lcccc}
278	\toprule
279	Layer & Depth \% & Silhouette & EN--ZH Overlap & Centroid Dist. \\
280	\midrule
281	Layer 10 & 31\% & 0.18 & 0.78 & 0.82 \\
282	Layer 18 & 56\% & 0.28 & 0.62 & 1.24 \\
283	Layer 25 & 78\% & 0.31 & 0.48 & 1.73 \\
284	Layer 28 & 88\% & 0.34 & 0.41 & 2.08 \\
285	\bottomrule
286	\end{tabular}
287	\end{table}
288	
289	\subsection{Representation Steering}
290	\label{sec:steering}
291	
292	Table~\ref{tab:steering} presents steering intervention results on Llama-3.1-8B. Probe-weight directions yield substantially higher flip rates (18--34\%) than random orthogonal controls (6\%), with Cohen's $d = 0.41$ (medium effect).
293	
294	\begin{table}[t]
295	\centering
296	\caption{Steering intervention results (Llama-3.1-8B, best probe layer).}
297	\label{tab:steering}
298	\begin{tabular}{lccc}
299	\toprule
300	Condition & Flip Rate (\%) & Coherence (\%) & Random Ctrl (\%) \\
301	\midrule
302	ZH$\to$EN probe direction & 34.2 & 74.1 & 5.8 \\
303	EN$\to$ZH probe direction & 18.1 & 71.3 & 6.2 \\
304	Averaged probe direction & 26.5 & 72.8 & 6.0 \\
305	Random orthogonal direction & 6.0 & 89.5 & --- \\
306	\bottomrule
307	\end{tabular}
308	\end{table}
309	
310	The ZH$\to$EN direction produces nearly twice the flip rate of EN$\to$ZH (34.2\% vs.\ 18.1\%), echoing the probe-transfer asymmetry: the direction that transfers better also steers more effectively. Table~\ref{tab:alpha} shows the steering strength--coherence trade-off. At $\alpha = 3.5$, the ``net useful flips'' (flip rate $\times$ coherence) peak at 25.3\%.
311	
312	\begin{table}[t]
313	\centering
314	\caption{Steering strength sensitivity (ZH$\to$EN direction, Llama-3.1-8B).}
315	\label{tab:alpha}
316	\begin{tabular}{lccc}
317	\toprule
318	$\alpha$ & Flip Rate (\%) & Coherence (\%) & Net Useful Flips (\%) \\
319	\midrule
320	1.0 & 12.3 & 91.2 & 11.2 \\
321	2.0 & 22.8 & 84.6 & 19.3 \\
322	3.5 & 34.2 & 74.1 & 25.3 \\
323	5.0 & 38.9 & 58.3 & 22.7 \\
324	7.0 & 41.2 & 42.1 & 17.3 \\
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	\paragraph{Interpretation.} These results provide correlational evidence consistent with a causal role for the detected conflict signal, but fall short of definitive causal demonstration. The probe-weight direction captures variance \emph{associated} with conflict, not necessarily the \emph{causal} direction governing resolution. Definitive causal claims require activation patching \citep{vig2020investigating} or distributed alignment search \citep{geiger2024finding}, which we leave to future work.
330	
331	%% ===== 5. DISCUSSION =====
332	\section{Discussion}
333	
334	\subsection{H1 vs.\ H2: Evidence Assessment}
335	
336	Our results favor H1 (English-anchored universal detection) over H2 (language-pair-specific encoding). The evidence:
337	\begin{itemize}
338	    \item \textbf{Directional asymmetry}: X$\to$EN transfer consistently exceeds EN$\to$X across three models and two language pairs, consistent with English as a representational anchor.
339	    \item \textbf{Effect-size stability}: The $6.6 \pm 0.9$\,pp pooled effect with $I^2 = 0\%$ suggests a shared mechanism rather than architecture-specific artifacts.
340	    \item \textbf{CKA transition}: Conflict signals peak during the universal$\to$specific transition, consistent with detection occurring in the shared representation space.
341	\end{itemize}
342	
343	Against H1: the probe peak depth varies substantially across models (67--88\%), suggesting architecture-dependent factors modulate where the transition completes. We interpret this as H1 holding for the \emph{existence} of asymmetry while the \emph{magnitude and peak location} are architecture-modulated.
344	
345	SAE-based feature overlap analysis (Appendix~\ref{app:sae}) was inconclusive due to the base--instruct distribution mismatch, leaving the strongest H1-vs-H2 test---whether mid-layer conflict features have higher cross-lingual Jaccard than late-layer features---unresolved.
346	
347	\subsection{Connection to CLEAR}
348	
349	CLEAR \citep{zhao2026clear} established that linguistic affinity governs conflict resolution in entity-centric tasks. Our probe-transfer asymmetry provides a candidate mechanism: if conflict detection is anchored in English representation space, then linguistically similar languages (sharing more representational structure with English) would have more effective conflict encoding, explaining the affinity effect. The EN--JA results (4.6\,pp gap vs.\ EN--ZH 7.2\,pp) are \emph{consistent} with this account, though the sample-size confound prevents definitive attribution to typological distance.
350	
351	\subsection{Non-linear Components (C3)}
352	
353	MLP probes show direction-dependent gains: EN$\to$ZH improves by 3.1\,pp (Gemma), consistent with 2.3\,pp (Qwen) and $\sim$4.7\,pp bootstrap-corrected (Llama). The weaker transfer direction benefits more from non-linear modeling, suggesting that EN$\to$ZH mapping involves more complex cross-lingual transformations. Architectures with stronger multilingual alignment (Qwen, with higher ZH training proportion) show smaller non-linear gains, consistent with simpler cross-lingual mappings.
354	
355	\subsection{Limitations}
356	
357	\begin{enumerate}
358	    \item \textbf{Two language pairs}: EN--ZH and EN--JA provide suggestive but insufficient evidence for broad typological claims. Additional pairs (EN--DE, EN--AR) would strengthen the linguistic distance analysis.
359	    \item \textbf{Dataset}: ConflictQA covers entity-centric factual conflicts; generalization to reasoning-intensive conflicts (where CLEAR found resource abundance dominates) is untested.
360	    \item \textbf{Causal evidence}: Steering results are correlational. The 34\% flip rate indicates the probe direction \emph{overlaps with} but does not \emph{constitute} the causal mechanism.
361	    \item \textbf{SAE analysis}: Base--instruct mismatch rendered Track~2 results inconclusive (Appendix~\ref{app:sae}).
362	    \item \textbf{Model scale}: All models are 8--9B parameters; behavior at larger scales may differ.
363	\end{enumerate}
364	
365	\subsection{Future Directions}
366	
367	Two high-priority directions emerge: (1)~SAE analysis with matched training distributions (training SAEs on the instruct models directly or using base models throughout), enabling clean H1-vs-H2 feature-overlap tests; (2)~cross-lingual SAE-based steering (Track~3), deferred here due to unreliable feature identification, which would establish whether monolingual conflict features can steer cross-lingual behavior.
368	
369	%% ===== 6. CONCLUSION =====
370	\section{Conclusion}
371	
372	We presented a systematic investigation of cross-lingual knowledge conflict encoding in multilingual LLMs. Our main finding is that conflict signals are linearly detectable in residual streams and exhibit a remarkably consistent directional asymmetry: transfer from non-English to English consistently exceeds the reverse, with a pooled effect of $6.6 \pm 0.9$\,pp across three architectures ($I^2 = 0\%$). This effect-size stability, rather than individual significance tests, constitutes the primary evidence for an English-anchored conflict encoding mechanism.
373	
374	Layer-wise CKA analysis reveals that conflict detection peaks during the language-universal-to-specific representation transition, and probe-based steering provides correlational evidence consistent with a causal role (Cohen's $d = 0.41$). Our confound-exclusion pipeline (token overlap, COMET ablation, label noise robustness) establishes that these results reflect genuine semantic-level signals rather than surface artifacts. We report preliminary SAE results honestly as a boundary of current tools, identifying the base--instruct distribution mismatch as a critical methodological challenge for future mechanistic interpretability work in multilingual settings.
375	
376	%% ===== APPENDICES =====
377	\appendix
378	
379	\section{Label Noise Robustness}
380	\label{app:noise}
381	
382	To assess sensitivity to verification pipeline errors (estimated at $\sim$4\%), we inject systematic label noise at rates from 5\% to 20\% (Table~\ref{tab:noise}).
383	
384	\begin{table}[h]
385	\centering
386	\caption{Probe accuracy under systematic label noise (Llama-3.1-8B, EN$\to$EN).}
387	\label{tab:noise}
388	\begin{tabular}{lccc}
389	\toprule
390	Noise Rate & Bal.\ Acc (\%) & $\Delta$ (pp) & 95\% CI \\
391	\midrule
392	0\% & 77.1 & --- & [74.3, 79.9] \\
393	5\% & 75.8 & $-$1.3 & [72.9, 78.7] \\
394	10\% & 73.8 & $-$3.3 & [70.7, 76.9] \\
395	15\% & 70.4 & $-$6.7 & [67.0, 73.8] \\
396	20\% & 66.8 & $-$10.3 & [63.1, 70.5] \\
397	\bottomrule
398	\end{tabular}
399	\end{table}
400	
401	At the estimated pipeline error rate of 4\%, the accuracy loss is $\sim$1\,pp, well within the CI width. Degradation accelerates beyond 10\%, but the noise-tolerance threshold (10\%) far exceeds our estimated error rate, confirming that label noise does not materially affect conclusions.
402	
403	\section{Preliminary SAE Analysis}
404	\label{app:sae}
405	
406	\subsection{Qwen-Scope Conflict Feature Identification}
407	
408	We applied Qwen-Scope pretrained SAEs (65,536 features, Qwen3-8B-Base) to conflict vs.\ control activations at layer~22. Table~\ref{tab:sae} summarizes the results.
409	
410	\begin{table}[h]
411	\centering
412	\caption{SAE conflict feature statistics (Qwen-Scope, layer 22). Results are noisy due to base--instruct distribution mismatch (cosine similarity 0.71).}
413	\label{tab:sae}
414	\begin{tabular}{lccc}
415	\toprule
416	Metric & EN & ZH & Overlap \\
417	\midrule
418	Activated features ($> 2\sigma$) & 312 & 256 & 78 \\
419	MI-selected ($> 0.15$) & 45 & 42 & 8 \\
420	Interpretable (manual) & 16/45 & 14/42 & 3/8 \\
421	Mean activation diff (conflict$-$control) & 2.31 & 1.87 & --- \\
422	\bottomrule
423	\end{tabular}
424	\end{table}
425	
426	The base--instruct cosine similarity of 0.71 indicates that $\sim$30\% of activation patterns are misaligned, causing the SAE to decompose instruct-specific patterns into multiple sparse features. Only 35\% of MI-selected features are manually interpretable, and the low EN--ZH overlap (8/45 $\approx$ 18\%) likely reflects noise rather than genuine language specificity. We caution against interpreting these results as evidence for or against H1/H2.
427	
428	\subsection{LangFIR Language Feature Decomposition}
429	
430	LangFIR random-token filtering identified 120 language-identity features. Of the 45 MI-selected conflict features, 22 (49\%) overlap with language-identity features (Table~\ref{tab:langfir}). After filtering, 23 residual conflict features remain with only 3 cross-lingual overlaps and 22\% interpretability.
431	
432	\begin{table}[h]
433	\centering
434	\caption{LangFIR conflict--language feature decomposition.}
435	\label{tab:langfir}
436	\begin{tabular}{lccc}
437	\toprule
438	Category & Count & Cross-lingual Overlap & Interpretable \\
439	\midrule
440	All MI-selected conflict features & 45 & 8 (18\%) & 16 (36\%) \\
441	Language-identity features (LangFIR) & 120 & --- & --- \\
442	Conflict $\cap$ Language & 22 & --- & --- \\
443	Residual conflict (post-filter) & 23 & 3 (13\%) & 5 (22\%) \\
444	\bottomrule
445	\end{tabular}
446	\end{table}
447	
448	The high overlap rate (49\%) suggests that many ``conflict features'' are actually language features mislabeled due to upstream SAE noise, further confirming that base--instruct mismatch is the primary limitation.
449	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38600cc9-6ec3-47aa-9538-3e0215df80a8",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "ac770b6258a8deee7",
  "type": "user",
  "uuid": "f20d7a19-ddf6-4229-b572-da2d36523047",
  "sourceToolAssistantUUID": "38600cc9-6ec3-47aa-9538-3e0215df80a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-22T03:34:32.452Z_

Now I have a thorough understanding of both the actual experimental state and the submitted paper. The paper summary in the task prompt describes a version closer to the actual experiments (with Gemma showing +1.0pp in one framing). However, based on my comprehensive reading of the "median" dream paper (which appears to be the most realistic version), I'll write my review. The task prompt's summary with Gemma at +1.0pp and steering at 8%/5% appears to reflect the actual completed experiments rather than the dream papers. Let me now write my review based on the paper content described in the task prompt.

---

## Summary

This paper probes residual stream activations in three multilingual LLMs (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B) to detect knowledge conflict signals and measure their cross-lingual transfer. The main claims are: (1) conflict signals are linearly detectable within-language at 68-77% balanced accuracy; (2) cross-lingual transfer shows a ZH-to-EN directional asymmetry of ~7pp in Llama/Qwen that collapses in Gemma-2-9B; (3) CKA decreases monotonically across layers with probe peaks after the language transition point. The steering experiments yield very weak results (3-8% flip rates). Track 2 (SAE) and Track 3 (causal steering via SAE) are entirely absent.

## Strengths

- **Well-structured hypothesis-driven design.** The H1 vs. H2 framework with falsifiable predictions (mid-layer sharing > late-layer, directional consistency) elevates this above exploratory probing. The paper clearly states what each hypothesis predicts before presenting results.

- **Thorough confound exclusion pipeline.** The COMET tercile ablation (Table 3) is the correct experiment: demonstrating that translation quality does not positively predict probe accuracy (delta = -5.64pp Qwen, -3.20pp Llama, both p > 0.48) addresses the most natural confound for cross-lingual probing. Token overlap analysis (Jaccard 3-4%, no positive correlation) addresses the shared-vocabulary alternative explanation. These controls together provide a solid methodological contribution.

- **Permutation testing is appropriate and rigorous.** Using n=1000 permutations with all p < 0.001 for within-language detection is the correct statistical approach for this setting. The binomial test baseline is also appropriate.

- **Label noise robustness provides useful calibration.** The graceful degradation (~3.3pp per 5% noise, Table 7) and the estimated <5% pipeline error rate together establish adequate safety margins. This is a model practice for probing papers.

- **Honest reporting of limitations.** Section 6 is unusually candid: acknowledging the absence of Tracks 2-3, the weak steering results, the ~8% label noise estimate, and the ~1000-sample limitation builds credibility.

- **Multi-architecture replication** across three model families with different design choices (GQA configurations, sliding window in Gemma, different tokenizers) is appropriate for generalizability.

## Weaknesses

- **W1 (Major). The central claim C2 (directional asymmetry) is contradicted by the Gemma results, yet the paper maintains the claim.** The paper states C2 as "architecture-dependent," but the reality is more damaging: Gemma-2-9B shows +1.0pp asymmetry (Table 1, CI [-4.5, 6.8]), fully consistent with zero. This is not "architecture-dependent asymmetry" -- it is evidence that the asymmetry may not be a robust phenomenon. With Llama significant, Qwen trending (CI includes zero), and Gemma null, the evidence base is 1/3 significant, 1/3 trending, 1/3 null. The paper's framing of this as "architecture-dependent" is a post-hoc rationalization of a failed replication. The paper should either (a) provide a mechanistic explanation for why Gemma specifically should lack the asymmetry, supported by independent evidence, or (b) downgrade C2 to "inconsistent across architectures."

- **W2 (Major). Steering results are too weak to support any causal interpretation.** Table 8 reports flip rates of 8%/5% (Llama), 6%/4% (Qwen), 3%/3% (Gemma). These are barely above random baselines (typically ~5% for random perturbations). The paper frames this as "weak causal evidence" but at these effect sizes, the signal cannot be distinguished from noise or from general model perturbation effects. A random-direction control with reported flip rate is not provided in the paper summary, making it impossible to assess whether the probe direction outperforms random perturbation. This weakness is particularly problematic because the paper's framing positions itself as providing mechanistic explanation, yet the only causal experiment is essentially null.

- **W3 (Major). Bootstrap n=100 is inadequate for the precision required by the asymmetry claim.** At n=100, the 95% CI endpoints are determined by the 2.5th and 97.5th percentiles, which correspond to literally the 2nd-3rd most extreme bootstrap values. For Qwen's CI of [-1.2, 13.4], this means the lower bound is highly unstable -- running the bootstrap again with a different seed could easily shift it to [0.5, 14.0] or [-2.8, 12.5]. The conventional minimum is n >= 1000 (Efron & Tibshirani, 1993). This is computationally trivial to fix (logistic regression is fast) and its absence is puzzling.

- **W4 (Major). The "English-anchored" interpretation (H1) lacks the critical non-conflict control.** The X-to-EN > EN-to-X pattern could be a general property of cross-lingual probing in English-dominant models, having nothing to do with conflict specifically. English representations are better formed (more training data), so probes trained on any English-language feature may transfer better FROM other languages TO English, simply because the English test set is easier. This confound is trivial to control: probe for a non-conflict semantic feature (e.g., entity type, sentiment) with the same pipeline. Its absence makes the conflict-specificity of the asymmetry entirely unsupported.

- **W5 (Moderate). CKA correlation of r=-0.71 reported on 3 data points (Table 6).** Computing a Pearson correlation on 3 points is meaningless -- any 3 non-collinear points will yield a correlation with magnitude > 0.5 by chance roughly 50% of the time. The paper should report the raw values and note the qualitative direction without computing or reporting a correlation coefficient.

- **W6 (Moderate). The COMET scores are low (mean 0.68-0.70) with only 12-18.5% passing the 0.80 threshold.** While the tercile ablation argues translation quality is not a confound for the probe, it does indicate the translations are of mediocre quality. This raises concerns about whether "conflict" and "non-conflict" labels are preserved reliably in translation. The verification step (requiring models to produce expected answers in both languages) partially addresses this, but the paper should report how many samples fail verification and whether the verified subset differs systematically from the full set.

- **W7 (Moderate). Only a single language pair (EN-ZH) for the core claims.** While the paper summary mentions EN-ZH for all three models, there is no evidence of EN-JA completion (stated as 15% done in the experimental plan). A single language pair cannot distinguish H1 (universal English anchoring) from a ZH-specific phenomenon. Both ZH and EN share substantial Wikidata entity overlap, shared script for numbers/proper nouns, etc.

- **W8 (Moderate). Probe accuracy ceiling of 68-77% is not adequately explained.** Prior monolingual conflict probing achieves 90+ F1 (Zhao et al. 2026 reports ~90% probe precision). The 23-32% undetectable fraction is large. Is this due to: (a) the cross-lingual setting inherently adding noise? (b) label errors from the verification pipeline? (c) the signal being genuinely weaker in these models? The paper does not investigate which factor dominates, making it difficult to interpret what "detectability" means here.

- **W9 (Minor). MLP vs. linear comparison (Table 4) lacks train-test gap reporting.** The MLP gains of +2.0 to +4.7pp could partially reflect overfitting. A 2-layer MLP with 256 hidden units has ~1M parameters trained on ~1000 samples with ~4000 features. The paper states 5-fold CV but does not report whether the MLP gain persists when measured strictly on held-out folds. Without train accuracy alongside test accuracy, overfitting cannot be ruled out.

- **W10 (Minor). The paper uses the target models themselves for translation, introducing potential circularity.** If Qwen's translation biases correlate with its internal conflict representations, the ZH text could carry model-specific artifacts that inflate same-model probing accuracy.

## Questions for Authors

1. Have you tested the asymmetry direction (X-to-EN > EN-to-X) on a non-conflict binary classification task using identical methodology? This is the single most important missing control.

2. Why was bootstrap n set to 100 rather than 1000 or 10000? Given that each iteration involves only logistic regression, the computational cost of 10000 iterations should be negligible.

3. What is the random-direction baseline flip rate for the steering experiments? Table 8 shows absolute flip rates but without a matched random-perturbation control, the 3-8% rates may be indistinguishable from noise.

4. For Gemma-2-9B showing +1.0pp asymmetry (vs. 7pp for Llama/Qwen): do you have a principled mechanistic explanation for why this specific architecture should differ, or is this a failed replication?

5. How many samples fail the verification step (both EN and ZH must elicit expected answers), and do the failed samples differ systematically from the passed samples in entity type or conflict difficulty?

6. What is the class balance (conflict vs. non-conflict) in the test sets? Balanced accuracy is reported, but the base rates affect interpretability.

7. For the MLP probes (Table 4), what are the training set accuracies? If training accuracy is substantially above test accuracy, the gains may reflect overfitting rather than genuine non-linear signal.

## Minor Issues

- The paper mentions "~8% label noise" (Section 6) but then the noise robustness experiment (Table 7) shows this would degrade probe accuracy by ~5pp, which is non-trivial relative to the reported effect sizes. The paper should reconcile whether the estimated pipeline error rate is <5% (as claimed when interpreting Table 7's safety margin) or ~8% (as stated in limitations).

- Table 6 reports "probe peak vs CKA transition" percentages (Llama 88% vs 75%, Qwen 67% vs 58%, Gemma 62% vs 55%) without explaining what comparison is being made or how these numbers relate.

- The paper does not report which specific layers achieve peak probe accuracy for each model, only depth ratios. Reporting actual layer indices (e.g., "layer 28/32 for Llama") aids reproducibility.

- Multiple comparisons: with 4 transfer directions x 3 models x multiple layers tested, some correction (Bonferroni or FDR) should be applied, particularly for the asymmetry claims.

- The PCA appendix (28% variance in PC1+PC2) shows the conflict signal is highly distributed. This is consistent with a probe that captures only a fraction of the signal but is not discussed in relation to the moderate probe accuracy.

## Missing Experiments / Suggested Improvements

- **Non-conflict semantic baseline (Critical).** Probe for any binary semantic feature (entity type, sentiment polarity, factual domain) using identical methodology. If the same X-to-EN > EN-to-X asymmetry appears, the paper's central claim is a replication of known cross-lingual transfer properties, not a conflict-specific finding.

- **Random-direction steering control (Critical).** Report flip rates when using a random vector of the same norm as the probe weight. Without this, the 3-8% flip rates in Table 8 cannot be interpreted.

- **Bootstrap n >= 2000 (High priority, trivial cost).** Stabilize all CI estimates, particularly for the asymmetry gap where CI boundaries determine the conclusion.

- **Non-CJK language pair (High priority).** EN-DE or EN-FR would test whether the pattern holds across typological families. Without this, "English-anchored" claims cannot be distinguished from CJK-specific phenomena.

- **MLP overfitting diagnostic (Medium priority).** Report training accuracy alongside test accuracy for MLP probes to rule out overfitting as the source of gains.

- **Characterization of the 23-32% undetectable fraction.** What properties do samples that the probe consistently misclassifies have? This could reveal boundary conditions of the conflict-detection claim.

- **SAE analysis on matched model (Medium priority).** Either run probing on Qwen3-8B-Base or train SAEs on the instruct model. The base-instruct gap makes cross-track validation impossible in the current setup.

- **Dataset expansion for statistical power.** ConflictQA has ~10K instances; expanding to 2000+ per model would resolve the Qwen significance question definitively.

## Scores

- **Soundness: 2/4** -- The probing framework itself is correct, but the paper's central claim (C2, directional asymmetry) is supported by only 1/3 models reaching significance, contradicted by Gemma's null result, and lacking the critical non-conflict control that would establish conflict-specificity. Bootstrap n=100 is below accepted standards for the precision required. The steering experiment is essentially null at 3-8% flip rates. The CKA "correlation" on 3 points is not a valid statistic.

- **Presentation: 3/4** -- The paper is clearly organized, tables are readable, and the limitations section is admirably honest. The H1/H2 structure aids comprehension. Deductions for: framing Gemma's null as "architecture-dependent" rather than a failed replication, computing r on 3 points, and inconsistent label-noise estimates (8% vs. <5%).

- **Contribution: 2/4** -- The paper asks a genuinely interesting question and the confound-exclusion methodology is a useful contribution. However, with Tracks 2-3 absent, steering essentially null, and the core asymmetry claim contested by Gemma, the contribution reduces to "conflict signals are linearly detectable cross-lingually at 63-77%" -- which is interesting but incremental. The claimed mechanistic explanation for CLEAR is not established without the non-conflict control and with only 1/3 architectures showing significant asymmetry.

- **Overall: 4/10** -- The paper is marginally below the acceptance threshold. It asks a good question and demonstrates methodological care in some areas (confound exclusion), but the core claims are insufficiently supported: the asymmetry finding is contradicted by one of three models, the causal evidence (steering) is essentially null, Tracks 2-3 are entirely absent despite being framed as part of the contribution, and the missing non-conflict baseline leaves the fundamental interpretive question unanswered. The gap between what the paper promises (mechanistic explanation of CLEAR) and what it delivers (one significant, one trending, one null probe transfer experiment) is too large for acceptance.

- **Confidence: 4/5** -- I have examined the experimental code, project artifacts, bootstrap results, and multiple versions of the paper in detail. I am highly confident in my assessment of the statistical and methodological issues. My only uncertainty is whether some results described in the paper summary (e.g., Gemma at +1.0pp) reflect the actual submitted paper or an intermediate version, though the experimental logs confirm that Tracks 2-3 and the JA extension were never completed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f20d7a19-ddf6-4229-b572-da2d36523047",
  "isSidechain": true,
  "agentId": "ac770b6258a8deee7",
  "requestId": "req_011CbGuLU647J8NBH1YjkAMz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4d19823-6a37-4455-89f6-16b7cf3c6107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Ys35tqzJBn9qKeznpSPSy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6903,
      "cache_read_input_tokens": 86650,
      "output_tokens": 3836,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6903
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3836,
          "cache_read_input_tokens": 86650,
          "cache_creation_input_tokens": 6903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6903,
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
