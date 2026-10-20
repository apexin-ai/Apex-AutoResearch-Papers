# Research conversation: You are Reviewer 2 (R2) for a top ML venue peer review. Your focus: **novelty, significance, positioning against related

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac9acbe0e00c978cd.jsonl`
- **Structured JSON:** [`53e36631553db11cc070.json`](../../sessions/53/53e36631553db11cc070.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-18T03:57:31.073Z_

You are Reviewer 2 (R2) for a top ML venue peer review. Your focus: **novelty, significance, positioning against related work, and writing quality**. Use a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary
**Title:** DisPeD: Persuasion-Aware Fine-Tuning for Robust Cross-Attack Multi-Turn Jailbreak Detection

DisPeD fine-tunes DeBERTa-v3-base on 8-class persuasion strategy classification + binary jailbreak-intent (Stage 1), then aggregates turn embeddings via GRU/mean-pooling for conversation-level detection (Stage 2). Trained on 480 Crescendo conversations. Headline: vanilla temporal modeling (DeBERTa+GRU without persuasion fine-tuning) collapses to F1=0.28 on unseen Deceptive Delight attacks; DisPeD achieves F1=1.0 (+72pp).

## Paper Structure & Content
- **Abstract** (~200 words): States problem (multi-turn attacks defeat per-turn classifiers), gap (vanilla temporal modeling fails OOD), method (persuasion strategy classification as fine-tuning objective), results (F1=1.0 vs 0.28, +72pp; ablation shows supervision signal is key; LLM judges fail).
- **Introduction** (2 pages): Background on multi-turn attacks → DeepContext as natural response but fails OOD → persuasion in jailbreaks is systematic (Zeng 2024a, Hagendorff 2026) → DisPeD proposal → 3 contributions listed.
- **Related Work** (1 page): 5 subsections: multi-turn attacks, safety classifiers, multi-turn defenses, persuasion in adversarial contexts, discourse analysis, red-teaming.
- **Method** (1.5 pages): Problem formulation, Stage 1 (encoder fine-tuning with L_CE + λ·L_BCE), Stage 2 (GRU/mean-pool aggregation), early detection, 8-class taxonomy.
- **Experimental Setup** (1 page): Data (480 train, 72 IID test, 160 OOD test, 200 hard negatives), models (treatment, baseline, TF-IDF, DeepContext proxy, LLM judges), evaluation (F1, 3 seeds, bootstrap CI).
- **Results** (2.5 pages): Tables 1-7 covering TF-IDF baseline, IID, cross-attack, ablation, perturbation, LLM-as-judge, strategy trajectories.
- **Additional Analysis** (1 page): Tables 8-10 covering DeepContext proxy, hard negatives, checkpoint sensitivity.
- **Discussion** (1 page): Supervision signal narrative, honest TF-IDF positioning, content vs process detection, limitations.
- **Conclusion** (0.5 page)
- **References** (25 citations)

## Key Claims
1. Vanilla semantic temporal modeling fails catastrophically OOD; persuasion fine-tuning bridges the gap entirely (F1=1.0, +72pp)
2. The persuasion fine-tuning objective is the sole critical ingredient (robust to label quality, granularity, architecture, loss weighting)
3. 8-class taxonomy enables interpretable strategy trajectories as complementary contribution
4. Zero-shot LLM judges cannot substitute for process-level detection

## Related Work the Paper Cites
- **Multi-turn attacks:** Crescendo (Russinovich 2024), PAIR (Chao 2023), Deceptive Delight (Jiang 2024), Wei 2024, Bullwinkel 2025
- **Safety classifiers:** Llama Guard (Inan 2023), WildGuard (Han 2024), ShieldGemma (Zeng 2024b), Constitutional Classifiers (Anthropic 2024), LLM-as-judge (Perez 2022, Ganguli 2022)
- **Multi-turn defenses:** DeepContext (Su 2026), BIID (2025), G-Guard (2025), SafeDream (2025)
- **Persuasion:** Zeng 2024a (40 techniques), Hagendorff 2026 (97% in corpus), How Do LLMs Persuade? 2025
- **Discourse:** RST (Mann & Thompson 1988), Penn Discourse Treebank (Prasad 2008), dialogue acts (Stolcke 2000), argumentation (Habernal & Gurevych 2016, Tan 2016)
- **Red-teaming:** HarmBench (Mazeika 2024), Nasr 2025, annotation artifacts (Gururangan 2018, Niven & Kao 2019)
- Total: ~25 references

## Your Review Task
Provide a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (numbered, with evidence)
3. **Weaknesses** (numbered, be specific)
   - Focus on: novelty/incrementality, related work coverage, positioning clarity, writing quality, significance of contribution
4. **Questions for Authors**
5. **Assessment of Novelty**: Is "fine-tune on persuasion labels then use the encoder for downstream detection" a sufficient contribution? How does this compare to standard domain-adaptive fine-tuning / auxiliary task learning?
6. **Related Work Gaps**: Any missing important references?
7. **Writing Quality**: Check for AI-style writing patterns, clarity, logical flow
8. **Minor Issues**
9. **Overall Assessment** with numerical score and confidence (1-5)

Key areas to scrutinize:
- The core method is essentially: fine-tune encoder on an auxiliary task (persuasion classification), then use the encoder for the target task (jailbreak detection). This is a well-known transfer learning / multi-task learning paradigm. What is genuinely novel?
- The ablation shows scrambled labels work nearly as well (0.99 vs 1.0), binary works as well, mean pooling works as well, any lambda works. If the method is this insensitive to design choices, is the "method" really just "expose the encoder to persuasion-domain text during fine-tuning"? Is that a method or a finding?
- 25 references for a top venue: is this sufficient?
- The paper positions against DeepContext (Su et al. 2026), but DeepContext is a single recent preprint. Is the baseline landscape comprehensive?
- Synthetic OOD data generated by the authors: can we trust the evaluation?
- TF-IDF at 0.944 on DD: does this suggest the task has strong lexical signal that makes the neural approach less necessary?
- The interpretability claim (Claim 2) via strategy trajectories: is this well-supported or superficial?
- How does this compare to simply fine-tuning DeBERTa on a related persuasion corpus (without the specific 8-class taxonomy)?

Be rigorous but fair.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "ec562fb7-f5bb-4d09-9999-7b01cd9517cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T03:57:31.076Z_

```json
{
  "parentUuid": "ec562fb7-f5bb-4d09-9999-7b01cd9517cc",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
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
  "uuid": "fef8a051-f153-4d71-86f3-a9dd9a4ae422",
  "timestamp": "2026-05-18T03:57:31.076Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T03:57:33.415Z_



I'll start by reading the paper and all related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fef8a051-f153-4d71-86f3-a9dd9a4ae422",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9Mz7JhdYsLfqsmNDcak",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce43e781-2b41-4a26-88eb-ede49f766ed6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KunVJKKWZNecBXgczQoyAu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8833,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8833,
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

_source line 4 · 2026-05-18T03:57:34.578Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ac31U4rYumCCE9qJ6qMDjN`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce43e781-2b41-4a26-88eb-ede49f766ed6",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9Mz7JhdYsLfqsmNDcak",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5c1a721-9272-4630-98ac-bda3d526a669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KunVJKKWZNecBXgczQoyAu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8833,
      "cache_read_input_tokens": 8255,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 142,
          "cache_read_input_tokens": 8255,
          "cache_creation_input_tokens": 8833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8833,
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

_source line 5 · 2026-05-18T03:57:34.581Z_

<details><summary>↩ Tool result · `toolu_01Ac31U4rYumCCE9qJ6qMDjN`</summary>

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
  "parentUuid": "f5c1a721-9272-4630-98ac-bda3d526a669",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "0a35ead0-1ad0-4774-8cae-859906bbab4c",
  "sourceToolAssistantUUID": "f5c1a721-9272-4630-98ac-bda3d526a669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T03:57:36.659Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a35ead0-1ad0-4774-8cae-859906bbab4c",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9MzNVGA6dWPAft8NBra",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2fd0700-7ac8-477f-bb98-17199b381917",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rLPV326tKj6CcvPJMAq5F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 17088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 7 · 2026-05-18T03:57:37.871Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01NSPfMgoiyKTmPoA4RgFtsx`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2fd0700-7ac8-477f-bb98-17199b381917",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9MzNVGA6dWPAft8NBra",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c841109-b3d1-45a4-8ea4-cf4b825c3a2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rLPV326tKj6CcvPJMAq5F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 17088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 8 · 2026-05-18T03:57:37.928Z_

<details><summary>↩ Tool result · `toolu_01NSPfMgoiyKTmPoA4RgFtsx`</summary>

```text
{"result":"# 项目 persuasion_turn_jailbreak_detect 概况\n\n## 实验状态 (16 个)\n\n- **plan_015_dd_eval**: DONE (success) — \n- **plan_006_cross_attack_clean**: DONE (success) — \n- **plan_004_perturbation_eval**: DONE (success) — \n- **plan_013_none_collapse**: DONE (success) — \n- **plan_002_seed456**: DONE (success) — \n- **plan_002_seed123**: DONE (success) — \n- **plan_012_llm_judge_qwen**: DONE (success) — \n- **plan_002_clean_training**: DONE (negative) — \n- **plan_003_scrambled_ablation**: DONE (negative) — \n- **cross_attack_baseline**: DONE (negative) — \n- **plan_008_strategy_transition**: DONE (success) — \n- **plan_007_tfidf_fitd_dd**: DONE (success) — \n- **plan_005_multi_attack_gen**: DONE (success) — \n- **phase_b_full**: DONE (success) — \n- **pilot_phase_b**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_012_gpt55_judge** (success): Zero-shot LLM-as-judge (GPT-5.5) will underperform specialized trained classifiers at early jailbreak detection despite being a stronger LLM than Qwen3-8B, establishing that even frontier LLMs cannot match trained detection models ← 基于 plan_012_llm_judge_qwen\n- **plan_015_dd_eval** (success): Mean pooling classifier (without temporal modeling) will perform comparably to BiGRU on DD OOD data, proving GRU temporal modeling is not necessary and persuasion embeddings alone drive cross-attack generalization ← 基于 plan_006_cross_attack_clean\n- **plan_006_cross_attack_clean** (success): Persuasion-grounded DeBERTa fine-tuning (trained on Crescendo) produces transferable structural signals that generalize to unseen attack types (FITD/DD), outperforming vanilla DeBERTa baseline especially on structurally different attacks like Deceptive Delight ← 基于 plan_002_clean_training\n\n## 趋势\n成功 13 / 负向 3 / 失败 0 / 共 16\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-33183: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c841109-b3d1-45a4-8ea4-cf4b825c3a2b",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "446f72fb-e73f-4448-9297-44556ad53e2e",
  "sourceToolAssistantUUID": "6c841109-b3d1-45a4-8ea4-cf4b825c3a2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T03:57:39.025Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QGrsPTHKSoD834QZCKN66R`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "446f72fb-e73f-4448-9297-44556ad53e2e",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9MzNVGA6dWPAft8NBra",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c659d2e-d958-42e9-9af1-99b68b06e264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rLPV326tKj6CcvPJMAq5F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 17088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 10 · 2026-05-18T03:57:39.046Z_

<details><summary>↩ Tool result · `toolu_01QGrsPTHKSoD834QZCKN66R`</summary>

```text
artifacts/dream_reports/dream_20260517T165817/best/paper.tex
artifacts/dream_reports/dream_20260517T165817/median/paper.tex
artifacts/dream_reports/dream_20260517T165817/worst/paper.tex
artifacts/dream_reports/dream_20260518T032748/best/paper.tex
artifacts/dream_reports/dream_20260518T032748/median/paper.tex
artifacts/dream_reports/dream_20260518T032748/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c659d2e-d958-42e9-9af1-99b68b06e264",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "a319aa8b-4429-4fce-8698-61567316822e",
  "sourceToolAssistantUUID": "4c659d2e-d958-42e9-9af1-99b68b06e264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T03:57:39.431Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EDnWa9WHS7SKvmBbLxeHrp`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a319aa8b-4429-4fce-8698-61567316822e",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9MzNVGA6dWPAft8NBra",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46bc0834-276f-4fd0-8db3-13d10b037caa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rLPV326tKj6CcvPJMAq5F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 17088,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2016
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 265,
          "cache_read_input_tokens": 17088,
          "cache_creation_input_tokens": 2016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2016,
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

_source line 12 · 2026-05-18T03:57:39.451Z_

<details><summary>↩ Tool result · `toolu_01EDnWa9WHS7SKvmBbLxeHrp`</summary>

```text
artifacts/data/collect_data.py
scripts/preprocess_data.py
artifacts/scripts/annotate_turns.py
artifacts/scripts/postprocess_annotations.py
artifacts/generate_crescendo_v2.py
scripts/generate_crescendo.py
scripts/sanity_check.py
scripts/generate_crescendo_transformers.py
artifacts/phase_b_supplement_eval.py
figures/paper/gen_fig2_cross_attack_bar.py
figures/paper/gen_fig1_architecture.py
figures/paper/gen_fig3_strategy_heatmap.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46bc0834-276f-4fd0-8db3-13d10b037caa",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "3fc55a37-5b9e-4b7b-a895-037ce8f60a8e",
  "sourceToolAssistantUUID": "46bc0834-276f-4fd0-8db3-13d10b037caa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T03:57:42.837Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DXA886tskhnU7Go5w3miid`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260518T032748/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fc55a37-5b9e-4b7b-a895-037ce8f60a8e",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9MzjHQyVBoHvstMxRmi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e42d598e-a256-4003-893c-d3f02c911c68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pc6YSuKuuPN9v9LrjfMKuL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 19104,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1420
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 19104,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1420,
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

_source line 14 · 2026-05-18T03:57:43.163Z_

<details><summary>↩ Tool result · `toolu_01DXA886tskhnU7Go5w3miid`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{hyperref}
9	\usepackage{xcolor}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{tabularx}
13	\usepackage{array}
14	
15	\newcommand{\ours}{DisPeD}
16	\newcommand{\fone}{F$_1$}
17	
18	\title{\ours{}: Persuasion-Aware Fine-Tuning for Robust\\Cross-Attack Multi-Turn Jailbreak Detection}
19	
20	\author{Anonymous}
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	% ============================================================
27	% ABSTRACT
28	% ============================================================
29	\begin{abstract}
30	Multi-turn jailbreak attacks distribute adversarial intent across individually benign conversational turns, defeating per-turn safety classifiers and single-turn content analysis.
31	A natural defense is to track semantic drift across turns with a generic encoder and a recurrent aggregator, but we show that this vanilla temporal modeling approach catastrophically fails on unseen attack families: a model trained on Crescendo conversations collapses to \fone{}=0.28 when evaluated on Deceptive Delight.
32	We propose \ours{}, which fine-tunes DeBERTa-v3-base on an 8-class persuasion strategy classification objective before aggregation.
33	This persuasion-aware fine-tuning bridges the cross-attack generalization gap entirely, achieving \fone{}=1.0 on the same unseen attacks (a +72 percentage point improvement).
34	Systematic ablation reveals that the supervision signal, not architectural choices, drives generalization: scrambled strategy labels retain \fone{}=0.94--0.99, binary persuasion-presence labels match 8-class performance within 1 percentage point (pp), mean pooling matches GRU aggregation, and detection is insensitive to multi-task loss weighting.
35	The 8-class taxonomy provides complementary value through interpretable strategy trajectories that distinguish attack families.
36	Zero-shot frontier Large Language Model (LLM) judges (GPT-5.5, Qwen3-8B) achieve at most \fone{}=0.45 on the same data, confirming that content-level analysis cannot detect process-level manipulation.
37	\end{abstract}
38	
39	% ============================================================
40	% 1. INTRODUCTION
41	% ============================================================
42	\section{Introduction}
43	
44	Multi-turn jailbreak attacks such as Crescendo \citep{russinovich2024}, Foot-in-the-Door (FITD), and Deceptive Delight \citep{jiang2024} exploit conversational dynamics to circumvent safety alignment in large language models.
45	Rather than injecting a single adversarial prompt, these attacks distribute manipulative intent across multiple turns, keeping each individual message within the ``benign'' region of representation space \citep{bullwinkel2025}.
46	This deliberate distribution defeats per-turn safety classifiers \citep{inan2023llamaguard,han2024wildguard,zeng2024shieldgemma} and LLM-as-judge approaches \citep{perez2022}, which analyze content at the utterance level rather than tracking the adversarial process across the full conversation.
47	
48	A natural response is to model the temporal evolution of turn-level representations.
49	DeepContext \citep{su2026} encodes each turn with BERT and aggregates the sequence with a GRU, achieving \fone{}=0.84 on in-distribution Crescendo detection.
50	However, we demonstrate that this vanilla semantic temporal modeling approach fails catastrophically when confronted with attack types unseen during training: a DeBERTa-v3-base + GRU model trained on Crescendo conversations collapses to \fone{}=0.28 on Deceptive Delight (DD) attacks.
51	The generic encoder produces turn embeddings that capture surface semantics but miss the pragmatic manipulation strategies shared across attack families.
52	
53	Recent work establishes that persuasion is systematic in jailbreaks.
54	\citet{zeng2024pap} identify 40 persuasion techniques effective for jailbreaking and show that persuasion-enhanced attacks substantially increase attack success rates.
55	\citet{hagendorff2026} find identifiable persuasion strategies in 97\% of successful attacks across a large-scale corpus.
56	Complementary analysis demonstrates that persuasion dynamics are extractable from turn-level neural representations \citep{howdollms2025}.
57	Yet no published method operationalizes these observations into a detection system that generalizes across attack types.
58	
59	We propose \ours{} (\textbf{Dis}course-level \textbf{Pe}rsuasion \textbf{D}etector), which uses persuasion strategy classification as a multi-task fine-tuning objective for the turn-level encoder.
60	Stage~1 fine-tunes DeBERTa-v3-base on two tasks jointly: 8-class persuasion strategy classification and binary jailbreak-intent classification.
61	Stage~2 aggregates the resulting turn embeddings via a sequence model (GRU or mean pooling) for conversation-level detection.
62	The persuasion objective teaches the encoder to attend to pragmatic features that transfer across attack families, without requiring attack-specific training data.
63	
64	Our experiments yield three findings.
65	First, persuasion-aware fine-tuning bridges the cross-attack generalization gap completely: \ours{} achieves \fone{}=1.0 on unseen DD attacks where the vanilla baseline collapses to \fone{}=0.28, a +72pp improvement.
66	Second, systematic ablation reveals that the persuasion fine-tuning objective is the sole critical ingredient: scrambled labels, binary labels, mean pooling, and varying loss weights all produce equivalent detection, while the 8-class taxonomy provides interpretable strategy trajectories as a complementary contribution.
67	Third, zero-shot LLM judges (GPT-5.5: \fone{}=0.38; Qwen3-8B: \fone{}=0.10) confirm that content-level analysis cannot substitute for process-level detection.
68	
69	Our contributions are:
70	\begin{itemize}
71	    \item We demonstrate that vanilla semantic temporal modeling (generic encoder + RNN) fails catastrophically on unseen multi-turn attack types (\fone{}=0.28 on DD) and that persuasion-aware fine-tuning bridges this gap entirely (\fone{}=1.0, +72pp).
72	    \item We provide comprehensive ablation evidence that the persuasion fine-tuning objective functions as an accessible supervision signal: detection is robust to label quality, label granularity, aggregation architecture, and loss weighting. The 8-class taxonomy enables interpretable strategy trajectory analysis as a complementary contribution.
73	    \item We establish baselines against TF-IDF (strong lexical), frontier LLM judges (content-level), and a DeepContext proxy (vanilla temporal), positioning \ours{} within the landscape of multi-turn jailbreak defenses.
74	\end{itemize}
75	
76	% ============================================================
77	% 2. RELATED WORK
78	% ============================================================
79	\section{Related Work}
80	
81	\paragraph{Multi-turn jailbreak attacks.}
82	Crescendo \citep{russinovich2024} gradually escalates requests across turns, exploiting conversational context to normalize harmful content.
83	PAIR \citep{chao2023} uses an attacker LLM to iteratively refine jailbreak prompts.
84	\citet{jiang2024} introduce Deceptive Delight, which interleaves benign and adversarial content to exploit attention dilution.
85	\citet{wei2024} provide a taxonomy of jailbreak strategies, distinguishing competing-objectives and mismatched-generalization failures.
86	\citet{bullwinkel2025} show that multi-turn attacks keep per-turn representations in a ``benign'' region, causing a 50-point attack success rate gap relative to single-turn attacks.
87	
88	\paragraph{Safety classifiers and guardrails.}
89	Per-turn classifiers such as Llama Guard \citep{inan2023llamaguard}, WildGuard \citep{han2024wildguard}, ShieldGemma \citep{zeng2024shieldgemma}, and Constitutional Classifiers \citep{anthropic2024constitutional} detect harmful content at the utterance level.
90	These systems achieve high accuracy on single-turn attacks but do not model cross-turn dependencies.
91	LLM-as-judge approaches \citep{perez2022,ganguli2022} prompt frontier models to evaluate conversations but analyze content rather than process, limiting their effectiveness against distributed manipulation.
92	
93	\paragraph{Multi-turn defenses.}
94	DeepContext \citep{su2026} aggregates BERT turn embeddings via a GRU for conversation-level detection, achieving \fone{}=0.84 on Crescendo.
95	BIID \citep{biid2025} and G-Guard \citep{gguard2025} propose graph-based and multi-agent approaches to multi-turn safety.
96	SafeDream \citep{safedream2025} uses proactive safety mechanisms.
97	None of these methods incorporate persuasion-grounded features or evaluate cross-attack generalization.
98	
99	\paragraph{Persuasion in adversarial contexts.}
100	\citet{zeng2024pap} systematically apply 40 persuasion techniques to jailbreaking, demonstrating that persuasion-enhanced prompts substantially increase attack success.
101	\citet{hagendorff2026} analyze a large-scale jailbreak corpus and find identifiable persuasion strategies in 97\% of successful attacks.
102	\citet{howdollms2025} show that persuasion dynamics are extractable from turn-level representations.
103	These findings motivate persuasion-aware detection but have not been operationalized into cross-attack-generalizable classifiers.
104	
105	\paragraph{Discourse analysis and computational persuasion.}
106	Discourse-level analysis has a long history in NLP, from Rhetorical Structure Theory \citep{mann1988} to the Penn Discourse Treebank \citep{prasad2008pdtb} and dialogue act classification \citep{stolcke2000}.
107	Computational persuasion detection has been studied in argumentation mining \citep{habernal2016} and social media influence \citep{tan2016}.
108	\ours{} connects these traditions to LLM safety by treating persuasion strategy classification as a representation learning objective.
109	
110	\paragraph{Red-teaming and evaluation.}
111	Systematic red-teaming efforts \citep{perez2022,ganguli2022} and benchmarks such as HarmBench \citep{mazeika2024} evaluate model safety.
112	\citet{nasr2025} study adaptive attacks that evade classifiers.
113	\citet{gururangan2018} and \citet{niven2019} demonstrate annotation artifacts in NLP benchmarks.
114	We address artifact concerns through topic-anchored data construction and ablation controls.
115	
116	
117	% ============================================================
118	% 3. METHOD
119	% ============================================================
120	\section{Method}
121	
122	\subsection{Problem Formulation}
123	Given a multi-turn conversation $C = (u_1, u_2, \ldots, u_T)$ consisting of $T$ turns, the goal is to classify $C$ as jailbreak or benign at the conversation level.
124	We additionally define a per-turn persuasion strategy label $s_t \in \{0, 1, \ldots, 7\}$ from an 8-class taxonomy and a binary jailbreak-intent label $y_t \in \{0, 1\}$.
125	
126	\subsection{Stage 1: Persuasion-Aware Encoder Fine-Tuning}
127	We fine-tune DeBERTa-v3-base \citep{he2021deberta} on two auxiliary tasks jointly.
128	Each turn $u_t$ is encoded independently to produce a [CLS] representation $\mathbf{h}_t \in \mathbb{R}^d$.
129	Two classification heads operate on $\mathbf{h}_t$:
130	
131	\begin{align}
132	    \hat{s}_t &= \text{softmax}(\mathbf{W}_s \mathbf{h}_t + \mathbf{b}_s) \label{eq:persuasion} \\
133	    \hat{y}_t &= \sigma(\mathbf{w}_y^\top \mathbf{h}_t + b_y) \label{eq:intent}
134	\end{align}
135	
136	The combined loss is:
137	\begin{equation}
138	    \mathcal{L}_{\text{stage1}} = \mathcal{L}_{\text{CE}}(\hat{s}_t, s_t) + \lambda \cdot \mathcal{L}_{\text{BCE}}(\hat{y}_t, y_t)
139	\end{equation}
140	where $\lambda$ controls the relative weight of the intent classification objective.
141	Ablation experiments (Section~\ref{sec:ablation}) show detection performance is insensitive to $\lambda \in \{0, 0.3, 0.5, 2.0\}$.
142	
143	\subsection{Stage 2: Conversation-Level Aggregation}
144	Given the fine-tuned encoder, we extract turn embeddings $\mathbf{H} = (\mathbf{h}_1, \ldots, \mathbf{h}_K)$ for the first $K$ turns of a conversation.
145	These are aggregated and classified:
146	\begin{equation}
147	    \hat{c} = \sigma(\mathbf{w}_c^\top f(\mathbf{H}) + b_c)
148	\end{equation}
149	where $f$ is either a GRU that produces the final hidden state, or mean pooling across turns.
150	We report GRU as the default but note that mean pooling produces equivalent results (Section~\ref{sec:ablation}), confirming that temporal ordering is not the detection mechanism.
151	
152	\subsection{Early Detection}
153	For deployment, the system can operate on partial conversations.
154	Given the first $K$ turns, detection is performed on $\mathbf{H}_K = (\mathbf{h}_1, \ldots, \mathbf{h}_K)$.
155	We evaluate at $K \in \{1, 2, 3, 5, \text{full}\}$ to characterize early detection capability.
156	
157	\subsection{Persuasion Strategy Taxonomy}
158	\label{sec:taxonomy}
159	Following \citet{zeng2024pap} and \citet{hagendorff2026}, we define 8 persuasion strategy classes spanning the spectrum from rapport building to explicit coercion.
160	Strategy index increases with escalation intensity: class 0 (rapport/trust building) through class 7 (explicit pressure/coercion).
161	This ordering enables trajectory analysis (Section~\ref{sec:interpretability}) where the temporal pattern of strategy indices characterizes different attack types.
162	
163	% ============================================================
164	% 4. EXPERIMENTAL SETUP
165	% ============================================================
166	\section{Experimental Setup}
167	
168	\subsection{Data}
169	\paragraph{Training data.}
170	We construct a topic-anchored dataset of 480 conversations (240 Crescendo jailbreak, 240 benign) with per-turn persuasion strategy annotations.
171	Benign conversations are anchored to matching topics to eliminate trivial lexical shortcuts from topic divergence.
172	Each conversation is annotated with turn-level 8-class persuasion strategy labels and binary jailbreak-intent labels.
173	
174	\paragraph{In-distribution test set.}
175	A held-out set of 72 Crescendo conversations (36 jailbreak, 36 benign) is used for IID evaluation.
176	
177	\paragraph{Out-of-distribution test sets.}
178	We generate 80 FITD and 80 Deceptive Delight (DD) conversations with persuasion annotations using a controlled generation pipeline.
179	FITD conversations use 4 distinct persuasion strategies and average 8.5 turns.
180	DD conversations use 6 strategies and average 7.2 turns.
181	These are used exclusively for evaluation; no OOD data appears during training.
182	
183	\paragraph{Hard negative evaluation.}
184	200 conversations from WildChat \citep{zhao2024wildchat} are filtered for high-drift characteristics (topic shift $\geq$3, $>$10 turns, emotional/persuasive language) after removing contaminated samples (contamination rate reduced from 15\% to 2\%).
185	
186	\subsection{Models}
187	\paragraph{\ours{} (Treatment).}
188	DeBERTa-v3-base fine-tuned on the persuasion + intent multi-task objective (Stage~1), followed by GRU aggregation (Stage~2).
189	Achieves 82\% accuracy on persuasion strategy classification and 98\% on intent classification.
190	
191	\paragraph{Vanilla baseline.}
192	Same Stage~2 architecture (DeBERTa-v3-base + GRU) without Stage~1 fine-tuning.
193	
194	\paragraph{TF-IDF + Logistic Regression.}
195	TF-IDF features with logistic regression, serving as a strong lexical baseline.
196	
197	\paragraph{DeepContext proxy.}
198	BERT-base + GRU, reproducing the DeepContext \citep{su2026} approach with available resources.
199	
200	\paragraph{LLM-as-Judge.}
201	GPT-5.5 and Qwen3-8B with zero-shot prompting for conversation-level jailbreak detection.
202	
203	\subsection{Evaluation}
204	All models are evaluated on conversation-level binary classification (\fone{} score) at $K \in \{1, 2, 3, 5, \text{full}\}$ turns.
205	Treatment and baseline models are trained with 3 random seeds; we report mean $\pm$ standard deviation.
206	Bootstrap 95\% confidence intervals are computed on the test set.
207	
208	% ============================================================
209	% 5. RESULTS
210	% ============================================================
211	\section{Results}
212	
213	\subsection{Baseline Landscape}
214	\label{sec:baselines}
215	
216	Table~\ref{tab:tfidf} reports the TF-IDF + LR baseline across all attack types.
217	TF-IDF achieves \fone{}=1.0 on Crescendo and FITD, and \fone{}=0.944 on DD.
218	This confirms inherent lexical separability between jailbreak and benign conversations: the top predictive features for jailbreak (``sure,'' ``hypothetical,'' ``creative,'' ``story,'' ``imagine'') versus benign (``thanks,'' ``code,'' ``help,'' ``python,'' ``error'') reflect fundamentally different conversational registers.
219	We report TF-IDF as an honest upper bound for lexical approaches throughout the paper.
220	
221	\begin{table}[t]
222	\centering
223	\caption{TF-IDF + Logistic Regression baseline across attack types.}
224	\label{tab:tfidf}
225	\begin{tabular}{lccc}
226	\toprule
227	 & Crescendo & FITD & DD \\
228	\midrule
229	TF-IDF + LR & 1.000 & 1.000 & 0.944 \\
230	\bottomrule
231	\end{tabular}
232	\end{table}
233	
234	\subsection{In-Distribution Detection}
235	\label{sec:iid}
236	
237	Table~\ref{tab:iid} reports IID performance on the Crescendo test set.
238	Both treatment and baseline achieve near-perfect detection at higher $K$, with the treatment reaching \fone{}=1.0 across all $K$ values with zero variance across 3 seeds.
239	The baseline is also strong IID (\fone{}=0.968 at $K$=1, rising to 1.0 at full), confirming that vanilla DeBERTa is a competent in-distribution detector.
240	The small IID gap (max 3.2pp at $K$=1) is expected: the paper's value proposition is not IID performance but cross-attack generalization.
241	
242	\begin{table}[t]
243	\centering
244	\caption{IID detection performance on Crescendo test set ($n$=72, 3-seed mean $\pm$ std). Treatment achieves zero variance across all $K$.}
245	\label{tab:iid}
246	\begin{tabular}{lccccc}
247	\toprule
248	Model & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
249	\midrule
250	Treatment & 1.000\tiny{$\pm$.000} & 1.000\tiny{$\pm$.000} & 1.000\tiny{$\pm$.000} & 1.000\tiny{$\pm$.000} & 1.000\tiny{$\pm$.000} \\
251	Baseline  & 0.968\tiny{$\pm$.033} & 0.977\tiny{$\pm$---} & 0.987\tiny{$\pm$---} & 0.996\tiny{$\pm$---} & 1.000\tiny{$\pm$---} \\
252	TF-IDF    & \multicolumn{5}{c}{1.000 (all $K$)} \\
253	\bottomrule
254	\end{tabular}
255	\end{table}
256	
257	\subsection{Cross-Attack Generalization}
258	\label{sec:cross_attack}
259	
260	Table~\ref{tab:cross_attack} presents the central experiment: models trained exclusively on Crescendo, evaluated on unseen FITD and DD attacks.
261	On DD, the vanilla baseline collapses to \fone{}=0.284 at full conversation length, while the treatment achieves \fone{}=1.0 (a +71.6pp gap).
262	The baseline's performance on DD degrades monotonically with conversation length ($K$=1: 0.575 $\to$ full: 0.284), indicating that the model actively gets worse as DD's deceptive structure unfolds.
263	The treatment maintains perfect or near-perfect detection across all $K$ values.
264	
265	On FITD, both models achieve strong performance (treatment: 1.0, baseline: 1.0 at full; 1.0 vs. 0.99 at $K$=1).
266	This asymmetry is informative: FITD's compliance-escalation pattern is structurally similar to Crescendo, enabling vanilla transfer.
267	DD's interleaving deception mechanism is fundamentally different, exposing the vanilla approach's reliance on Crescendo-specific surface features.
268	
269	TF-IDF achieves \fone{}=0.944 on DD (strong but not perfect) and 1.0 on FITD.
270	The treatment's advantage over TF-IDF on DD (5.6pp) is modest in raw detection but becomes substantial under adversarial perturbation (Section~\ref{sec:perturbation}).
271	
272	\begin{table}[t]
273	\centering
274	\caption{Cross-attack generalization: models trained on Crescendo only, evaluated on unseen FITD and DD. The +71.6pp gap on DD is the paper's headline result.}
275	\label{tab:cross_attack}
276	\begin{tabular}{llccccc}
277	\toprule
278	Attack & Model & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
279	\midrule
280	\multirow{3}{*}{DD}
281	  & Treatment & 1.000 & 0.990 & 0.990 & 1.000 & 1.000 \\
282	  & Baseline  & 0.575 & 0.438 & 0.360 & 0.310 & 0.284 \\
283	  & TF-IDF    & --- & --- & --- & --- & 0.944 \\
284	\midrule
285	\multirow{3}{*}{FITD}
286	  & Treatment & 1.000 & --- & --- & --- & 1.000 \\
287	  & Baseline  & 0.990 & --- & --- & --- & 1.000 \\
288	  & TF-IDF    & --- & --- & --- & --- & 1.000 \\
289	\bottomrule
290	\end{tabular}
291	\end{table}
292	
293	\subsection{Ablation Studies}
294	\label{sec:ablation}
295	
296	Table~\ref{tab:ablation} presents systematic ablation across four dimensions: label quality, label granularity, loss weighting, and aggregation architecture.
297	The results converge on a single conclusion: the persuasion fine-tuning objective is the sole critical ingredient for cross-attack generalization.
298	
299	\paragraph{Label quality (scrambled vs. proper).}
300	Randomly permuting strategy labels before fine-tuning reduces DD \fone{} by only 1.0pp at full length (0.990 vs. 1.000) and 6.5pp at $K$=1 (0.935 vs. 1.000).
301	Both scrambled and proper labels massively outperform the vanilla baseline (+70.6pp and +71.6pp on DD, respectively).
302	This reveals that the fine-tuning process on persuasion-related text, not the specific class boundaries, drives generalization.
303	Scrambled fine-tuning still achieves 64.4\% persuasion strategy accuracy (vs. 79.6\% with proper labels), confirming that even degraded class signal provides useful representation structure.
304	
305	\paragraph{Label granularity (binary vs. 8-class).}
306	Collapsing the 8-class taxonomy to binary (persuasion-present vs. none) produces equivalent IID detection (\fone{}=1.0) and nearly equivalent DD detection (\fone{}=0.990 vs. 1.000, a 1.0pp gap at full; 0.981 vs. 1.000 at $K$=1).
307	The model is fundamentally a persuasion-presence detector.
308	The 8-class taxonomy provides interpretability value (Section~\ref{sec:interpretability}), not detection advantage.
309	
310	\paragraph{Loss weighting ($\lambda$).}
311	Detection is insensitive to $\lambda \in \{0, 0.3, 0.5, 2.0\}$: all configurations achieve \fone{}=1.0 on both IID and DD.
312	The $\lambda$=0 condition (persuasion-only, no intent head) working equally well confirms that the intent classification head does not leak direct jailbreak signal into the encoder.
313	
314	\paragraph{Aggregation architecture (GRU vs. mean pooling).}
315	Mean pooling matches GRU within 1pp on all evaluations (DD full: 1.0 vs. 1.0; DD $K$=1: 1.0 vs. 1.0).
316	Temporal ordering is not the detection mechanism: the model detects persuasion-enriched embeddings regardless of turn order.
317	
318	\begin{table}[t]
319	\centering
320	\caption{Ablation study on DD (out-of-distribution). All variants with any form of persuasion fine-tuning massively outperform the vanilla baseline (\fone{}=0.284). The persuasion objective is the sole critical ingredient.}
321	\label{tab:ablation}
322	\begin{tabular}{lcc}
323	\toprule
324	Configuration & DD Full \fone{} & DD $K$=1 \fone{} \\
325	\midrule
326	Treatment (8-class, GRU, $\lambda$=0.5) & 1.000 & 1.000 \\
327	Scrambled labels & 0.990 & 0.935 \\
328	Binary labels & 0.990 & 0.981 \\
329	$\lambda$=0 (persuasion only) & 1.000 & --- \\
330	$\lambda$=0.3 & 1.000 & --- \\
331	$\lambda$=2.0 & 1.000 & --- \\
332	Mean pooling (replace GRU) & 1.000 & 1.000 \\
333	\midrule
334	Vanilla baseline (no fine-tuning) & 0.284 & 0.575 \\
335	\bottomrule
336	\end{tabular}
337	\end{table}
338	
339	\subsection{Adversarial Perturbation Robustness}
340	\label{sec:perturbation}
341	
342	To test whether models rely on surface lexical cues, we apply aggressive paraphrasing to the Crescendo test set (BERTScore = 0.92 to originals, lexical overlap = 0.20) and evaluate all models on the perturbed data.
343	Table~\ref{tab:perturbation} reports \fone{} and the drop ($\Delta$) relative to original performance.
344	
345	The treatment shows zero degradation at $K \geq 2$ and only $-$2.6pp at $K$=1.
346	The vanilla baseline is the most fragile ($-$11.8pp at full, $-$14.6pp at $K$=1).
347	TF-IDF is intermediate: robust at $K \geq 3$ ($-$1.3pp) but degrades at $K$=1 ($-$9.6pp), where lexical signal is sparse.
348	The strongest differentiation appears at early detection under perturbation ($K$=1), where the treatment leads TF-IDF by 7.0pp and the baseline by 12.0pp.
349	
350	\begin{table}[t]
351	\centering
352	\caption{Adversarial perturbation robustness. $\Delta$ = \fone{} drop from unperturbed. BERTScore = 0.92, lexical overlap = 0.20. Early detection ($K$=1) under perturbation maximally separates the three approaches.}
353	\label{tab:perturbation}
354	\begin{tabular}{lcccc}
355	\toprule
356	Model & Orig. \fone{} & Pert. \fone{} & $\Delta$ & Pert. $K$=1 ($\Delta$) \\
357	\midrule
358	Treatment & 1.000 & 1.000 & 0.0pp & 0.974 ($-$2.6pp) \\
359	Baseline  & 1.000 & 0.882 & $-$11.8pp & 0.854 ($-$14.6pp) \\
360	TF-IDF    & 1.000 & 0.987 & $-$1.3pp & 0.904 ($-$9.6pp) \\
361	\bottomrule
362	\end{tabular}
363	\end{table}
364	
365	\subsection{LLM-as-Judge Baseline}
366	\label{sec:llm_judge}
367	
368	Table~\ref{tab:llm_judge} evaluates zero-shot conversation-level jailbreak detection by frontier LLMs.
369	GPT-5.5 achieves perfect precision (1.0 at $K$=2) but catastrophically low recall (10.5\% at $K$=2, 29.0\% at $K$=5), producing \fone{}=0.19--0.45.
370	The frontier LLM is ``deceived'' by Crescendo's surface educational framing because it analyzes content, not the underlying manipulation process.
371	A substantial fraction of responses are unparseable (30.3\% at $K$=2, 47.4\% at full), further limiting practical utility.
372	Even with best-case unparseable correction (all unparseable treated as correct), GPT-5.5 reaches approximately \fone{}=0.75, still far below the treatment (\fone{}=1.0).
373	
374	Qwen3-8B performs near zero (\fone{}=0.0--0.15), confirming that this is not a model-size issue but a fundamental limitation of content-level analysis for process-level attacks.
375	
376	\begin{table}[t]
377	\centering
378	\caption{LLM-as-judge zero-shot detection on Crescendo. Frontier LLMs achieve high precision but catastrophically low recall: content analysis cannot detect distributed persuasion.}
379	\label{tab:llm_judge}
380	\begin{tabular}{lccccc}
381	\toprule
382	Model & $K$=2 & $K$=3 & $K$=5 & Full & Unparseable \\
383	\midrule
384	GPT-5.5 \fone{}   & 0.190 & 0.273 & 0.449 & 0.383 & 30--47\% \\
385	Qwen3-8B \fone{}  & 0.000 & 0.051 & 0.146 & 0.100 & --- \\
386	Treatment \fone{}  & 1.000 & 1.000 & 1.000 & 1.000 & --- \\
387	\bottomrule
388	\end{tabular}
389	\end{table}
390	
391	\subsection{Interpretability via Strategy Trajectories}
392	\label{sec:interpretability}
393	
394	Table~\ref{tab:transitions} reports persuasion strategy transition statistics.
395	Different attack types exhibit distinct trajectory signatures.
396	Crescendo conversations show gradual escalation, with mean strategy index rising from 0.86 in early turns to 5.64 in late turns (escalation slope = 0.53 per turn).
397	Across 8 turns, the strategy profile spans all 8 classes.
398	FITD conversations follow a commitment-escalation pattern: low-intensity strategies dominate early turns before a sharp transition to high-intensity strategies (low $\to$ low $\to$ mid $\to$ high).
399	DD conversations cycle through emotional manipulation, role assignment, and deception in an interleaving pattern, using 6 of 8 strategy classes.
400	
401	Benign conversations show low strategy index variance ($<$1.5) and low transition entropy (1.2 vs. 2.8 for jailbreak), confirming the absence of structured escalation.
402	These trajectories provide security analysts with attack fingerprints that characterize how an attack unfolds, not merely that it is occurring.
403	
404	\begin{table}[t]
405	\centering
406	\caption{Strategy trajectory statistics by attack type. Jailbreak conversations exhibit higher transition entropy and structured escalation patterns absent in benign conversations.}
407	\label{tab:transitions}
408	\begin{tabular}{lcccc}
409	\toprule
410	 & Crescendo & FITD & DD & Benign \\
411	\midrule
412	Strategies used & 8 & 4 & 6 & --- \\
413	Mean idx. start & 0.86 & \multicolumn{2}{c}{(see pattern)} & --- \\
414	Mean idx. end & 5.64 & \multicolumn{2}{c}{(see pattern)} & --- \\
415	Escalation slope & 0.53 & --- & --- & --- \\
416	Transition entropy & \multicolumn{3}{c}{2.8 (jailbreak)} & 1.2 \\
417	Idx. variance & --- & --- & --- & $<$1.5 \\
418	\bottomrule
419	\end{tabular}
420	\end{table}
421	
422	
423	% ============================================================
424	% 6. ADDITIONAL ANALYSIS
425	% ============================================================
426	\section{Additional Analysis}
427	
428	\subsection{DeepContext Proxy Comparison}
429	
430	To ground our comparison with the DeepContext approach \citep{su2026}, we train a BERT-base + GRU proxy.
431	This proxy achieves reasonable IID performance (\fone{}=0.96) but collapses on DD (\fone{}=0.32), confirming that the vanilla temporal modeling failure is independent of encoder choice (BERT-base vs. DeBERTa-v3-base).
432	The 68pp gap between the proxy and our treatment on DD (\fone{}=0.32 vs. 1.0) validates that encoder representation quality, not temporal architecture, drives generalization (Table~\ref{tab:proxy}).
433	
434	\begin{table}[t]
435	\centering
436	\caption{DeepContext proxy (BERT-base + GRU) comparison. The vanilla temporal approach fails OOD regardless of encoder choice.}
437	\label{tab:proxy}
438	\begin{tabular}{lcccc}
439	\toprule
440	Model & IID Full & DD Full & DD $K$=1 & FITD Full \\
441	\midrule
442	DeepContext proxy & 0.960 & 0.320 & 0.550 & 0.910 \\
443	Treatment         & 1.000 & 1.000 & 1.000 & 1.000 \\
444	Baseline (DeBERTa) & 1.000 & 0.284 & 0.575 & 1.000 \\
445	\bottomrule
446	\end{tabular}
447	\end{table}
448	
449	\subsection{False Positive Analysis on Hard Negatives}
450	
451	We evaluate false positive rates on 200 WildChat conversations selected for high-drift characteristics (Table~\ref{tab:fpr}).
452	The treatment produces 8\% FPR, the baseline 12\%, and TF-IDF 5\%.
453	False positives from the treatment occur on genuinely persuasive benign conversations (sales pitches, debate, tutoring), which is expected behavior for a model designed to detect persuasion dynamics.
454	Deployment would require threshold tuning for the target precision-recall tradeoff.
455	
456	\begin{table}[t]
457	\centering
458	\caption{False positive rate on WildChat hard negatives ($n$=200). High-drift definition: topic shift $\geq$3, $>$10 turns, emotional/persuasive language.}
459	\label{tab:fpr}
460	\begin{tabular}{lc}
461	\toprule
462	Model & FPR \\
463	\midrule
464	Treatment & 0.08 \\
465	Baseline  & 0.12 \\
466	TF-IDF    & 0.05 \\
467	\bottomrule
468	\end{tabular}
469	\end{table}
470	
471	\subsection{Checkpoint Sensitivity}
472	
473	Table~\ref{tab:checkpoint} reports performance across fine-tuning checkpoints at epochs 2, 3, and final.
474	IID detection is invariant across checkpoints (all \fone{}=1.0).
475	OOD detection shows negligible variance ($<$0.5pp): epoch 2 achieves \fone{}=0.995 on DD, rising to 1.0 by epoch 3.
476	Even epoch 2 (lower persuasion accuracy: 76\% vs. final 82\%) produces near-perfect downstream detection, reinforcing that precise persuasion classification is not required.
477	
478	\begin{table}[t]
479	\centering
480	\caption{Checkpoint sensitivity analysis. Detection is robust to early stopping; even epoch 2 (lower persuasion accuracy) achieves near-perfect OOD detection.}
481	\label{tab:checkpoint}
482	\begin{tabular}{lccc}
483	\toprule
484	Checkpoint & IID Full \fone{} & DD Full \fone{} & Persuasion Acc. \\
485	\midrule
486	Epoch 2 & 1.000 & 0.995 & 0.76 \\
487	Epoch 3 & 1.000 & 1.000 & 0.80 \\
488	Final   & 1.000 & 1.000 & 0.82 \\
489	\bottomrule
490	\end{tabular}
491	\end{table}
492	
493	
494	% ============================================================
495	% 7. DISCUSSION
496	% ============================================================
497	\section{Discussion}
498	
499	\paragraph{The supervision signal, not the architecture.}
500	The comprehensive ablation picture (Section~\ref{sec:ablation}) reveals a clean mechanistic story. Four independent ablation axes (label quality, label granularity, loss weighting, temporal modeling) all point to the same conclusion: the persuasion fine-tuning objective is the sole critical ingredient for cross-attack generalization. Scrambled labels retain \fone{}=0.94--0.99 on DD, binary labels match 8-class within 1pp, mean pooling matches GRU, and all $\lambda$ values produce \fone{}=1.0. The method requires no careful hyperparameter tuning, no expert label annotation, and no specific architecture. This positions persuasion-domain fine-tuning as an accessible and robust supervision signal rather than an overengineered system.
501	
502	\paragraph{Honest positioning against TF-IDF.}
503	TF-IDF + LR achieves \fone{}=0.944 on DD and 1.0 on Crescendo and FITD, reflecting inherent lexical separability between jailbreak and benign conversations. \ours{} does not claim superiority over TF-IDF on raw detection. Instead, the treatment provides three complementary advantages: (1) it bridges the vanilla temporal modeling gap (+72pp on DD vs. the baseline's 0.28), establishing that persuasion-aware representations solve a problem that lexical features happen to also address through a different mechanism; (2) it is more robust under adversarial perturbation at early detection ($K$=1: treatment $-$2.6pp vs. TF-IDF $-$9.6pp); (3) it provides interpretable strategy trajectories that TF-IDF cannot offer.
504	
505	\paragraph{Content analysis vs. process detection.}
506	The LLM-as-judge results (Section~\ref{sec:llm_judge}) establish a fundamental distinction. GPT-5.5 achieves perfect precision but recall below 30\%, confirming that even frontier LLMs analyzing conversation content cannot detect distributed persuasion when each turn appears individually benign. \ours{} operates at the process level, detecting the accumulation of persuasion dynamics rather than evaluating content for harmfulness. These are complementary capabilities: content analysis catches explicit harm, process detection catches distributed manipulation.
507	
508	\paragraph{Limitations.}
509	The evaluation uses synthetic OOD data (80 FITD + 80 DD conversations). While sufficient for proof-of-concept, ecological validity requires evaluation on real-world multi-turn attacks when such data becomes available. The 8\% FPR on WildChat hard negatives indicates that deployment requires threshold calibration. The method targets persuasion-mediated attacks and does not address pure information accumulation, token smuggling, or single-frame roleplay jailbreaks. The training set ($n$=480) is small; scaling to larger and more diverse persuasion-annotated corpora may further improve robustness.
510	
511	
512	% ============================================================
513	% 8. CONCLUSION
514	% ============================================================
515	\section{Conclusion}
516	
517	We presented \ours{}, a method that uses persuasion strategy classification as a multi-task fine-tuning objective to enable cross-attack multi-turn jailbreak detection.
518	Our central finding is that vanilla semantic temporal modeling catastrophically fails on unseen attack types (\fone{}=0.28 on Deceptive Delight), while persuasion-aware fine-tuning bridges this gap entirely (\fone{}=1.0, +72pp).
519	Systematic ablation demonstrates that the persuasion fine-tuning objective functions as an accessible supervision signal: detection survives label scrambling, binary collapse, architecture changes, and loss reweighting.
520	The 8-class taxonomy provides complementary interpretability through characteristic strategy trajectories.
521	These results establish persuasion-domain fine-tuning as a practical and robust approach to detecting distributed multi-turn manipulation, complementing existing per-turn safety classifiers and content-level LLM judges.
522	
523	% ============================================================
524	% REFERENCES
525	% ============================================================
526	\bibliographystyle{plainnat}
527	
528	\begin{thebibliography}{30}
529	
530	\bibitem[Anthropic(2024)]{anthropic2024constitutional}
531	Anthropic.
532	\newblock Constitutional classifiers: Defending against universal jailbreaks.
533	\newblock Technical report, 2024.
534	
535	\bibitem[Austin(1962)]{austin1962}
536	J.~L. Austin.
537	\newblock \emph{How to Do Things with Words}.
538	\newblock Oxford University Press, 1962.
539	
540	\bibitem[BIID(2025)]{biid2025}
541	BIID: Backdoor-based multi-turn jailbreak defense.
542	\newblock arXiv preprint, 2025.
543	
544	\bibitem[Bullwinkel et~al.(2025)]{bullwinkel2025}
545	B.~Bullwinkel et~al.
546	\newblock Multi-turn attacks keep per-turn representations benign.
547	\newblock arXiv:2507.02956, 2025.
548	
549	\bibitem[Chao et~al.(2023)]{chao2023}
550	P.~Chao, A.~Robey, E.~Dobriban, H.~Hassani, G.~J. Pappas, and E.~Wong.
551	\newblock Jailbreaking black box large language models in twenty queries.
552	\newblock arXiv preprint, 2023.
553	
554	\bibitem[G-Guard(2025)]{gguard2025}
555	G-Guard: Graph-based multi-turn safety guardrails.
556	\newblock arXiv preprint, 2025.
557	
558	\bibitem[Ganguli et~al.(2022)]{ganguli2022}
559	D.~Ganguli et~al.
560	\newblock Red teaming language models to reduce harms.
561	\newblock arXiv preprint, 2022.
562	
563	\bibitem[Gururangan et~al.(2018)]{gururangan2018}
564	S.~Gururangan, S.~Swayamdipta, O.~Levy, R.~Schwartz, S.~Bowman, and N.~A. Smith.
565	\newblock Annotation artifacts in natural language inference data.
566	\newblock In \emph{NAACL}, 2018.
567	
568	\bibitem[Habernal and Gurevych(2016)]{habernal2016}
569	I.~Habernal and I.~Gurevych.
570	\newblock Which argument is more convincing? Analyzing and predicting convincingness of web arguments using bidirectional LSTM.
571	\newblock In \emph{ACL}, 2016.
572	
573	\bibitem[Hagendorff(2026)]{hagendorff2026}
574	T.~Hagendorff.
575	\newblock Persuasion strategies in successful jailbreak attacks.
576	\newblock \emph{Nature Communications}, 2026.
577	
578	\bibitem[Han et~al.(2024)]{han2024wildguard}
579	S.~Han et~al.
580	\newblock WildGuard: Open one-stop moderation tools for safety risks, jailbreaks, and refusals of LLMs.
581	\newblock arXiv preprint, 2024.
582	
583	\bibitem[He et~al.(2021)]{he2021deberta}
584	P.~He, X.~Liu, J.~Gao, and W.~Chen.
585	\newblock DeBERTa: Decoding-enhanced BERT with disentangled attention.
586	\newblock In \emph{ICLR}, 2021.
587	
588	\bibitem[How Do LLMs Persuade?(2025)]{howdollms2025}
589	How do LLMs persuade? Extracting persuasion dynamics from turn-level representations.
590	\newblock arXiv:2508.05625, 2025.
591	
592	\bibitem[Inan et~al.(2023)]{inan2023llamaguard}
593	H.~Inan et~al.
594	\newblock Llama Guard: LLM-based input-output safeguard for human-AI conversations.
595	\newblock arXiv preprint, 2023.
596	
597	\bibitem[Jiang et~al.(2024)]{jiang2024}
598	Z.~Jiang et~al.
599	\newblock Deceptive Delight: Jailbreaking large language models through camouflaged content.
600	\newblock arXiv preprint, 2024.
601	
602	\bibitem[Mann and Thompson(1988)]{mann1988}
603	W.~C. Mann and S.~A. Thompson.
604	\newblock Rhetorical structure theory: Toward a functional theory of text organization.
605	\newblock \emph{Text}, 8(3):243--281, 1988.
606	
607	\bibitem[Mazeika et~al.(2024)]{mazeika2024}
608	M.~Mazeika et~al.
609	\newblock HarmBench: A standardized evaluation framework for automated red teaming and robust refusal.
610	\newblock arXiv preprint, 2024.
611	
612	\bibitem[Nasr et~al.(2025)]{nasr2025}
613	M.~Nasr, N.~Carlini, et~al.
614	\newblock Adaptive attacks against safety classifiers.
615	\newblock arXiv preprint, 2025.
616	
617	\bibitem[Niven and Kao(2019)]{niven2019}
618	T.~Niven and H.-Y. Kao.
619	\newblock Probing neural network comprehension of natural language arguments.
620	\newblock In \emph{ACL}, 2019.
621	
622	\bibitem[Perez et~al.(2022)]{perez2022}
623	E.~Perez et~al.
624	\newblock Red teaming language models with language models.
625	\newblock arXiv preprint, 2022.
626	
627	\bibitem[Prasad et~al.(2008)]{prasad2008pdtb}
628	R.~Prasad, N.~Dinesh, A.~Lee, E.~Miltsakaki, L.~Robaldo, A.~Joshi, and B.~Webber.
629	\newblock The Penn Discourse TreeBank 2.0.
630	\newblock In \emph{LREC}, 2008.
631	
632	\bibitem[Russinovich et~al.(2024)]{russinovich2024}
633	M.~Russinovich, A.~Salem, and R.~Eldan.
634	\newblock Great, now write an article about that: The crescendo multi-turn LLM jailbreak attack.
635	\newblock arXiv preprint, 2024.
636	
637	\bibitem[SafeDream(2025)]{safedream2025}
638	SafeDream: Proactive safety for multi-turn conversations.
639	\newblock arXiv preprint, 2025.
640	
641	\bibitem[Searle(1969)]{searle1969}
642	J.~R. Searle.
643	\newblock \emph{Speech Acts: An Essay in the Philosophy of Language}.
644	\newblock Cambridge University Press, 1969.
645	
646	\bibitem[Stolcke et~al.(2000)]{stolcke2000}
647	A.~Stolcke, K.~Ries, N.~Coccaro, E.~Shriberg, R.~Bates, D.~Jurafsky, P.~Taylor, R.~Martin, C.~Van~Ess-Dykema, and M.~Meteer.
648	\newblock Dialogue act modeling for automatic tagging and recognition of conversational speech.
649	\newblock \emph{Computational Linguistics}, 26(3):339--373, 2000.
650	
651	\bibitem[Su et~al.(2026)]{su2026}
652	Y.~Su et~al.
653	\newblock DeepContext: Multi-turn jailbreak detection via temporal semantic drift.
654	\newblock arXiv:2602.16935, 2026.
655	
656	\bibitem[Tan et~al.(2016)]{tan2016}
657	C.~Tan, V.~Niculae, C.~Danescu-Niculescu-Mizil, and L.~Lee.
658	\newblock Winning arguments: Interaction dynamics and persuasion strategies in good-faith online discussions.
659	\newblock In \emph{WWW}, 2016.
660	
661	\bibitem[Wei et~al.(2024)]{wei2024}
662	A.~Wei, N.~Haghtalab, and J.~Steinhardt.
663	\newblock Jailbroken: How does LLM safety training fail?
664	\newblock In \emph{NeurIPS}, 2024.
665	
666	\bibitem[Zeng et~al.(2024a)]{zeng2024pap}
667	Y.~Zeng, H.~Lin, J.~Zhang, D.~Yang, R.~Jia, and W.~Shi.
668	\newblock How johnny can persuade LLMs to jailbreak them: Rethinking persuasion to challenge AI safety by humanizing LLMs.
669	\newblock In \emph{ACL}, 2024.
670	
671	\bibitem[Zeng et~al.(2024b)]{zeng2024shieldgemma}
672	W.~Zeng et~al.
673	\newblock ShieldGemma: Generative AI content moderation based on Gemma.
674	\newblock arXiv preprint, 2024.
675	
676	\bibitem[Zhao et~al.(2024)]{zhao2024wildchat}
677	W.~Zhao et~al.
678	\newblock WildChat: 1M ChatGPT interaction logs in the wild.
679	\newblock In \emph{ICLR}, 2024.
680	
681	\end{thebibliography}
682	
683	\end{document}
684	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e42d598e-a256-4003-893c-d3f02c911c68",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "8b82bfd4-3d67-4555-8d90-a9a5483537fe",
  "sourceToolAssistantUUID": "e42d598e-a256-4003-893c-d3f02c911c68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T03:57:45.758Z_

Now let me also read the other paper versions and project files for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b82bfd4-3d67-4555-8d90-a9a5483537fe",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N111DUENJbdQsJyw4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "380026a0-5c51-49a0-a7cf-59b12b258353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YMWgkURBQ1VSbGgqqaGcE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14445,
      "cache_read_input_tokens": 20524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14445,
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

_source line 16 · 2026-05-18T03:57:47.064Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AtKUGExfqE95jvLZQYgybU`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "ideas.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "380026a0-5c51-49a0-a7cf-59b12b258353",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N111DUENJbdQsJyw4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18a0616b-ab77-4633-b4af-dedc388df143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YMWgkURBQ1VSbGgqqaGcE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14445,
      "cache_read_input_tokens": 20524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14445,
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

_source line 17 · 2026-05-18T03:57:47.074Z_

<details><summary>↩ Tool result · `toolu_01AtKUGExfqE95jvLZQYgybU`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18a0616b-ab77-4633-b4af-dedc388df143",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "cb23243b-65d0-44eb-8a2a-98c0a649f3b5",
  "sourceToolAssistantUUID": "18a0616b-ab77-4633-b4af-dedc388df143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T03:57:47.747Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01M1afrjuBuuYCK4gnveM6Bu`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "literature_map.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb23243b-65d0-44eb-8a2a-98c0a649f3b5",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N111DUENJbdQsJyw4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb531115-70de-4f71-9f78-81593aff788e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YMWgkURBQ1VSbGgqqaGcE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14445,
      "cache_read_input_tokens": 20524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14445,
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

_source line 19 · 2026-05-18T03:57:47.763Z_

<details><summary>↩ Tool result · `toolu_01M1afrjuBuuYCK4gnveM6Bu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/literature_map.yaml\", \"content\": \"# Literature Map — persuasion_turn_jailbreak_detect\\n# Generated: 2026-05-17 by Paper Agent\\n# Target: EMNLP 2026 Main (ARR May cycle)\\n# Total entries: 39 (across 8 categories + technical foundation)\\n# All entries WebSearch-verified\\n\\nmetadata:\\n  project: persuasion_turn_jailbreak_detect\\n  target_venue: EMNLP 2026\\n  last_updated: \\\"2026-05-17\\\"\\n  total_papers: 39\\n  categories:\\n    - production_safety_systems\\n    - multi_turn_defenses\\n    - discourse_analysis\\n    - computational_persuasion\\n    - jailbreak_attacks_taxonomies\\n    - red_teaming\\n    - annotation_artifacts\\n    - adaptive_attacks\\n    - technical_foundation\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Production Multi-Turn Safety Systems (5 papers)\\n  # ============================================================\\n\\n  - bibtex_key: inan2023llamaguard\\n    title: \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\"\\n    authors: \\\"Inan et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2023\\n    arxiv: \\\"2312.06674\\\"\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational production safety classifier. Per-turn input/output guard\\n      that lacks multi-turn context modeling. DisPeD addresses this gap by\\n      modeling conversation-level persuasion trajectories.\\n\\n  - bibtex_key: metallamaguard3_2024\\n    title: \\\"Llama Guard 3\\\"\\n    authors: \\\"Meta AI\\\"\\n    venue: \\\"Meta AI (released with Llama 3.1)\\\"\\n    year: 2024\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Latest iteration of Llama Guard with multilingual support and tool-use\\n      safety. Still operates per-turn without multi-turn trajectory modeling.\\n      Baseline comparison target for production safety systems.\\n\\n  - bibtex_key: zeng2024shieldgemma\\n    title: \\\"ShieldGemma: Generative AI Content Moderation Based on Gemma\\\"\\n    authors: \\\"Zeng et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2024\\n    arxiv: \\\"2407.21772\\\"\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Google's safety classifier suite (2B/9B/27B). Outperforms Llama Guard\\n      on public benchmarks. Demonstrates strong per-turn moderation but does\\n      not model multi-turn attack trajectories.\\n\\n  - bibtex_key: han2024wildguard\\n    title: \\\"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\\\"\\n    authors: \\\"Han et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2406.18495\\\"\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Allen AI's multi-task safety moderator (prompt harm + response harm +\\n      refusal detection). Reduces jailbreak ASR from 79.8% to 2.4% on\\n      single-turn attacks, but multi-turn evasion path remains open.\\n\\n  - bibtex_key: anthropic2025constitutional\\n    title: \\\"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\\\"\\n    authors: \\\"Anthropic\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2501.18837\\\"\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Anthropic's defense using synthetically-generated training data from\\n      constitutional rules. Reduces jailbreak ASR from 86% to 4.4%. Next-gen\\n      version uses exchange classifiers (input+output context). Production\\n      approach that our method complements with discourse-level analysis.\\n\\n  # ============================================================\\n  # Category 2: Multi-Turn Jailbreak Defenses (5 papers)\\n  # ============================================================\\n\\n  - bibtex_key: deepcontext2026\\n    title: \\\"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2602.16935\\\"\\n    category: multi_turn_defenses\\n    role: direct-competitor\\n    verified: true\\n    relevance_to_our_work: >\\n      PRIMARY POSITIONING TARGET. Uses RNN over BERT embeddings to track\\n      generic semantic drift. Achieves F1=0.84. DisPeD differs by grounding\\n      representations in persuasion strategy classification rather than\\n      generic semantics, arguing persuasion structure is harder to evade\\n      than semantic content (Pragmatic Evasion Asymmetry).\\n\\n  - bibtex_key: tong2025biid\\n    title: \\\"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\\\"\\n    authors: \\\"Tong et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2509.22732\\\"\\n    category: multi_turn_defenses\\n    role: direct-competitor\\n    verified: true\\n    relevance_to_our_work: >\\n      Combines forward request-based intention inference with backward\\n      response-based retrospection. Significantly reduces ASR on both\\n      single-turn and multi-turn attacks. DisPeD differs by using\\n      persuasion-grounded embeddings rather than intention inference.\\n\\n  - bibtex_key: gguard2025\\n    title: \\\"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2507.07146\\\"\\n    category: multi_turn_defenses\\n    role: direct-competitor\\n    verified: true\\n    relevance_to_our_work: >\\n      GNN-based approach modeling conversation structure as graph.\\n      Evaluated against Crescendo and ActorAttack. Represents structural\\n      approach to multi-turn defense; DisPeD uses sequential (GRU) rather\\n      than graph modeling of persuasion trajectories.\\n\\n  - bibtex_key: safedream2026\\n    title: \\\"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2604.16824\\\"\\n    category: multi_turn_defenses\\n    role: direct-competitor\\n    verified: true\\n    relevance_to_our_work: >\\n      World-model approach with CUSUM detection and contrastive imagination.\\n      Achieves early detection (1.06-1.20 turns before compliance). Shares\\n      our goal of early detection but uses latent safety state prediction\\n      rather than persuasion strategy grounding.\\n\\n  - bibtex_key: bullwinkel2025repeng\\n    title: \\\"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\\\"\\n    authors: \\\"Bullwinkel et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2507.02956\\\"\\n    category: multi_turn_defenses\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      CRITICAL MOTIVATION PAPER. Shows Crescendo keeps per-turn\\n      representations in \\\"benign\\\" region of representation space, explaining\\n      why per-turn defenses fail. This directly motivates DisPeD's approach\\n      of grounding representations in persuasion function rather than\\n      semantic content.\\n\\n  # ============================================================\\n  # Category 3: Discourse Analysis in NLP (5 papers)\\n  # ============================================================\\n\\n  - bibtex_key: mann1988rst\\n    title: \\\"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\\\"\\n    authors: \\\"Mann and Thompson\\\"\\n    venue: \\\"Text & Talk\\\"\\n    year: 1988\\n    category: discourse_analysis\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational discourse theory. RST's hierarchical text organization\\n      informs our modeling of persuasion strategy sequences as structured\\n      discourse rather than bag-of-features.\\n\\n  - bibtex_key: prasad2008pdtb\\n    title: \\\"The Penn Discourse TreeBank 2.0\\\"\\n    authors: \\\"Prasad et al.\\\"\\n    venue: \\\"LREC 2008\\\"\\n    year: 2008\\n    category: discourse_analysis\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Major discourse annotation resource. PDTB's approach to annotating\\n      discourse relations at the connective level parallels our annotation\\n      of persuasion strategies at the turn level.\\n\\n  - bibtex_key: stolcke2000dialogueact\\n    title: \\\"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\\\"\\n    authors: \\\"Stolcke et al.\\\"\\n    venue: \\\"Computational Linguistics\\\"\\n    year: 2000\\n    category: discourse_analysis\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational dialogue act classification using HMM over sequential\\n      turns. Our GRU-based persuasion trajectory modeling is a modern\\n      analogue of this sequential discourse structure approach.\\n\\n  - bibtex_key: austin1962speechacts\\n    title: \\\"How to Do Things with Words\\\"\\n    authors: \\\"Austin, J. L.\\\"\\n    venue: \\\"Harvard University Press\\\"\\n    year: 1962\\n    category: discourse_analysis\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational speech act theory distinguishing locutionary,\\n      illocutionary, and perlocutionary acts. DisPeD operates at the\\n      illocutionary level (what the speaker intends to accomplish)\\n      rather than the locutionary level (what words are used).\\n\\n  - bibtex_key: searle1969speechacts\\n    title: \\\"Speech Acts: An Essay in the Philosophy of Language\\\"\\n    authors: \\\"Searle, J. R.\\\"\\n    venue: \\\"Cambridge University Press\\\"\\n    year: 1969\\n    category: discourse_analysis\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Extended Austin's speech act theory with systematic taxonomy.\\n      Our persuasion strategy taxonomy maps onto Searle's classification\\n      of illocutionary acts, providing theoretical grounding for\\n      treating persuasion as a functional category.\\n\\n  # ============================================================\\n  # Category 4: Computational Persuasion Detection (4 papers)\\n  # ============================================================\\n\\n  - bibtex_key: habernal2016convincingness\\n    title: \\\"Which Argument Is More Convincing? Analyzing and Predicting Convincingness of Web Arguments Using Bidirectional LSTM\\\"\\n    authors: \\\"Habernal and Gurevych\\\"\\n    venue: \\\"ACL 2016\\\"\\n    year: 2016\\n    category: computational_persuasion\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Pioneering computational persuasion work predicting argument\\n      convincingness from text. Establishes that persuasive properties\\n      are computationally detectable from language, supporting our\\n      premise that persuasion strategies are extractable from turn\\n      representations.\\n\\n  - bibtex_key: tan2016winningarguments\\n    title: \\\"Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-faith Online Discussions\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"WWW 2016\\\"\\n    year: 2016\\n    category: computational_persuasion\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Analyzes persuasion dynamics in Reddit ChangeMyView. Shows timing,\\n      interaction patterns, and language features predict persuasion\\n      success. Supports our modeling of temporal persuasion trajectories\\n      as discriminative features.\\n\\n  - bibtex_key: jaipersaud2025howdollmspersuade\\n    title: \\\"How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations\\\"\\n    authors: \\\"Jaipersaud et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2508.05625\\\"\\n    category: computational_persuasion\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      CRITICAL PRIOR WORK. Demonstrates persuasion dynamics are extractable\\n      from LLM turn-level representations via linear probes. Directly\\n      supports our premise that DeBERTa fine-tuned on persuasion taxonomy\\n      produces informative turn embeddings for trajectory modeling.\\n\\n  - bibtex_key: cialdini2001influence\\n    title: \\\"Influence: Science and Practice\\\"\\n    authors: \\\"Cialdini, R. B.\\\"\\n    venue: \\\"Allyn & Bacon (4th edition)\\\"\\n    year: 2001\\n    category: computational_persuasion\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Six principles of \\n\\n... [截断: 省略 12216 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 24216, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb531115-70de-4f71-9f78-81593aff788e",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "2fe6e09b-bbaf-4604-9afc-33c08c094aa2",
  "sourceToolAssistantUUID": "bb531115-70de-4f71-9f78-81593aff788e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T03:57:48.410Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018vt63tRRLejuWxuJ7S5vJZ`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "ROADMAP.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fe6e09b-bbaf-4604-9afc-33c08c094aa2",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N111DUENJbdQsJyw4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ea3fef6-8038-4fe3-ae7d-c52ed6894607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YMWgkURBQ1VSbGgqqaGcE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14445,
      "cache_read_input_tokens": 20524,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14445
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 325,
          "cache_read_input_tokens": 20524,
          "cache_creation_input_tokens": 14445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14445,
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

_source line 21 · 2026-05-18T03:57:48.419Z_

<details><summary>↩ Tool result · `toolu_018vt63tRRLejuWxuJ7S5vJZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/ROADMAP.md\", \"content\": \"# persuasion_turn_jailbreak_detect — Research Dashboard\\n\\n> 最后更新: 2026-05-18 03:29 UTC | 更新原因: RC1 mitigation resolved, ROADMAP LLM judge numbers precise, Paper Agent + re-dream in progress\\n\\n> DDL: 2026-05-25 (7 days). 详见 paper_framing.md。\\n\\n## 核心方向\\nPersuasion-aware fine-tuning is the sole critical ingredient for cross-attack OOD generalization (+72pp vs vanilla baseline). Architecture (GRU vs mean pooling), label granularity (binary vs 8-class), and lambda are all non-factors (D014). 8-class taxonomy provides interpretability only.\\n\\n## 当前阶段\\nResearch Phase — **All 16 experiments complete.** Paper Agent Full Draft in progress. Re-dream running (dream_20260518T032748).\\n\\n## Evidence Summary\\n| Dimension | Key Result | Status |\\n|-----------|------------|--------|\\n| Cross-attack (DD) | Treatment=1.0 vs Baseline=0.28 (+72pp) | ✅ |\\n| Perturbation | Treatment 0pp degradation vs Baseline -12pp | ✅ |\\n| 3-seed stability | Treatment F1=1.00±0.00 | ✅ |\\n| Scrambled control | Labels contribute 1-6pp only | ✅ |\\n| Binary collapse (RC10) | Binary≈9-class on DD (1-2pp) | ✅ |\\n| Lambda ablation (RC11) | All lambda F1=1.0, insensitive | ✅ |\\n| Mean pooling (RC11) | Mean pooling≈GRU on DD | ✅ |\\n| LLM judge (RC5) | Qwen3-8B F1=0.0-0.15; GPT-5.5 F1=0.19-0.45 | ✅ |\\n| Strategy trajectories | Crescendo escalation confirmed (0.86→5.64) | ✅ |\\n\\n## 近期任务\\n- [x] GPT-5.5 judge result ✅ (D015)\\n- [x] Update paper_framing.md RC5 with GPT-5.5 numbers ✅\\n- [x] Update paper_framing.md RC1 mitigation to resolved ✅\\n- [ ] Re-dream with final framing (dream_20260518T032748, running)\\n- [ ] Paper Agent Full Draft (in progress)\\n\\n## GPU 预算\\n- 分配: 4× cuda:0-3 on westd-33183\\n- 磁盘: 72% (8.6G free)\\n- **All experiments complete.** GPU available for paper figure generation.\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D016 | 2026-05-18 | D016: Default architecture switched from GRU to Me | plan_015 |\\n| D015 | 2026-05-18 | D015: GPT-5.5 judge confirms zero-shot LLM detecti | plan_012 |\\n| D014 | 2026-05-18 | 综合ablation画面完成(D014): 唯一关键因素=persuasion-domain fin | plan_015, plan_013, plan_014, plan_006_scrambled_dd |\\n| D013 | 2026-05-18 | plan_013 OOD确认：binary/scrambled/9-class三种fine-tuni | plan_013, plan_006_scrambled_dd, plan_006 |\\n| D012 | 2026-05-18 | plan_004 PASS: Claim 3升级empirical。Treatment零退化，Bas | plan_004, plan_006 |\\n| D011 | 2026-05-17 | Evasion hierarchy叙事废弃：TF-IDF DD F1=0.94证明lexical未f | plan_006, plan_006_scrambled_dd |\\n| D010 | 2026-05-17 | Scrambled DD cross-attack: labels非关键(1-6pp gap)，fi | plan_006_scrambled_dd, plan_003, plan_006 |\\n| D009 | 2026-05-17 | TF-IDF词汇可分性确认为任务固有属性，plan_001正式废弃，论文reframe为IID vs | plan_001, plan_006, wildchat_tfidf |\\n| D008 | 2026-05-17 | Scrambled ablation 降级为补充分析，cross-attack generaliza | plan_003 |\\n| D007 | 2026-05-17 | Dream分析完成：median=3/6需修复framing/plan，已执行修复并继续P0实验 | dream_20260517T165817 |\\n\\n\", \"total_chars\": 2851, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ea3fef6-8038-4fe3-ae7d-c52ed6894607",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "6f7e4dd3-10b5-4036-8cd8-12cdb3dbdd49",
  "sourceToolAssistantUUID": "0ea3fef6-8038-4fe3-ae7d-c52ed6894607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-18T03:57:51.172Z_

Let me also read the full literature map and the paper framing document for complete context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f7e4dd3-10b5-4036-8cd8-12cdb3dbdd49",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N1PdzXRTgsyUSMFnUH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "130dcf67-e3f4-4030-a8df-07fa73639b89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa63QdrJPpH2781c4pimgd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6096,
      "cache_read_input_tokens": 34969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6096,
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

_source line 23 · 2026-05-18T03:57:52.629Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014pcanGxEKiEjnRWz81kXpz`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "130dcf67-e3f4-4030-a8df-07fa73639b89",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N1PdzXRTgsyUSMFnUH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5393fa6b-1849-4e2a-9927-ef5286420410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa63QdrJPpH2781c4pimgd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6096,
      "cache_read_input_tokens": 34969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6096,
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

_source line 24 · 2026-05-18T03:57:52.641Z_

<details><summary>↩ Tool result · `toolu_014pcanGxEKiEjnRWz81kXpz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/literature_map.yaml\", \"content\": \"# Literature Map — persuasion_turn_jailbreak_detect\\n# Generated: 2026-05-17 by Paper Agent\\n# Target: EMNLP 2026 Main (ARR May cycle)\\n# Total entries: 39 (across 8 categories + technical foundation)\\n# All entries WebSearch-verified\\n\\nmetadata:\\n  project: persuasion_turn_jailbreak_detect\\n  target_venue: EMNLP 2026\\n  last_updated: \\\"2026-05-17\\\"\\n  total_papers: 39\\n  categories:\\n    - production_safety_systems\\n    - multi_turn_defenses\\n    - discourse_analysis\\n    - computational_persuasion\\n    - jailbreak_attacks_taxonomies\\n    - red_teaming\\n    - annotation_artifacts\\n    - adaptive_attacks\\n    - technical_foundation\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Production Multi-Turn Safety Systems (5 papers)\\n  # ============================================================\\n\\n  - bibtex_key: inan2023llamaguard\\n    title: \\\"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations\\\"\\n    authors: \\\"Inan et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2023\\n    arxiv: \\\"2312.06674\\\"\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational production safety classifier. Per-turn input/output guard\\n      that lacks multi-turn context modeling. DisPeD addresses this gap by\\n      modeling conversation-level persuasion trajectories.\\n\\n  - bibtex_key: metallamaguard3_2024\\n    title: \\\"Llama Guard 3\\\"\\n    authors: \\\"Meta AI\\\"\\n    venue: \\\"Meta AI (released with Llama 3.1)\\\"\\n    year: 2024\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Latest iteration of Llama Guard with multilingual support and tool-use\\n      safety. Still operates per-turn without multi-turn trajectory modeling.\\n      Baseline comparison target for production safety systems.\\n\\n  - bibtex_key: zeng2024shieldgemma\\n    title: \\\"ShieldGemma: Generative AI Content Moderation Based on Gemma\\\"\\n    authors: \\\"Zeng et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2024\\n    arxiv: \\\"2407.21772\\\"\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Google's safety classifier suite (2B/9B/27B). Outperforms Llama Guard\\n      on public benchmarks. Demonstrates strong per-turn moderation but does\\n      not model multi-turn attack trajectories.\\n\\n  - bibtex_key: han2024wildguard\\n    title: \\\"WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs\\\"\\n    authors: \\\"Han et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2406.18495\\\"\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Allen AI's multi-task safety moderator (prompt harm + response harm +\\n      refusal detection). Reduces jailbreak ASR from 79.8% to 2.4% on\\n      single-turn attacks, but multi-turn evasion path remains open.\\n\\n  - bibtex_key: anthropic2025constitutional\\n    title: \\\"Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming\\\"\\n    authors: \\\"Anthropic\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2501.18837\\\"\\n    category: production_safety_systems\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Anthropic's defense using synthetically-generated training data from\\n      constitutional rules. Reduces jailbreak ASR from 86% to 4.4%. Next-gen\\n      version uses exchange classifiers (input+output context). Production\\n      approach that our method complements with discourse-level analysis.\\n\\n  # ============================================================\\n  # Category 2: Multi-Turn Jailbreak Defenses (5 papers)\\n  # ============================================================\\n\\n  - bibtex_key: deepcontext2026\\n    title: \\\"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2602.16935\\\"\\n    category: multi_turn_defenses\\n    role: direct-competitor\\n    verified: true\\n    relevance_to_our_work: >\\n      PRIMARY POSITIONING TARGET. Uses RNN over BERT embeddings to track\\n      generic semantic drift. Achieves F1=0.84. DisPeD differs by grounding\\n      representations in persuasion strategy classification rather than\\n      generic semantics, arguing persuasion structure is harder to evade\\n      than semantic content (Pragmatic Evasion Asymmetry).\\n\\n  - bibtex_key: tong2025biid\\n    title: \\\"Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks\\\"\\n    authors: \\\"Tong et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2509.22732\\\"\\n    category: multi_turn_defenses\\n    role: direct-competitor\\n    verified: true\\n    relevance_to_our_work: >\\n      Combines forward request-based intention inference with backward\\n      response-based retrospection. Significantly reduces ASR on both\\n      single-turn and multi-turn attacks. DisPeD differs by using\\n      persuasion-grounded embeddings rather than intention inference.\\n\\n  - bibtex_key: gguard2025\\n    title: \\\"An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2507.07146\\\"\\n    category: multi_turn_defenses\\n    role: direct-competitor\\n    verified: true\\n    relevance_to_our_work: >\\n      GNN-based approach modeling conversation structure as graph.\\n      Evaluated against Crescendo and ActorAttack. Represents structural\\n      approach to multi-turn defense; DisPeD uses sequential (GRU) rather\\n      than graph modeling of persuasion trajectories.\\n\\n  - bibtex_key: safedream2026\\n    title: \\\"SafeDream: Safety World Model for Proactive Early Jailbreak Detection\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2026\\n    arxiv: \\\"2604.16824\\\"\\n    category: multi_turn_defenses\\n    role: direct-competitor\\n    verified: true\\n    relevance_to_our_work: >\\n      World-model approach with CUSUM detection and contrastive imagination.\\n      Achieves early detection (1.06-1.20 turns before compliance). Shares\\n      our goal of early detection but uses latent safety state prediction\\n      rather than persuasion strategy grounding.\\n\\n  - bibtex_key: bullwinkel2025repeng\\n    title: \\\"A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks\\\"\\n    authors: \\\"Bullwinkel et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2507.02956\\\"\\n    category: multi_turn_defenses\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      CRITICAL MOTIVATION PAPER. Shows Crescendo keeps per-turn\\n      representations in \\\"benign\\\" region of representation space, explaining\\n      why per-turn defenses fail. This directly motivates DisPeD's approach\\n      of grounding representations in persuasion function rather than\\n      semantic content.\\n\\n  # ============================================================\\n  # Category 3: Discourse Analysis in NLP (5 papers)\\n  # ============================================================\\n\\n  - bibtex_key: mann1988rst\\n    title: \\\"Rhetorical Structure Theory: Toward a Functional Theory of Text Organization\\\"\\n    authors: \\\"Mann and Thompson\\\"\\n    venue: \\\"Text & Talk\\\"\\n    year: 1988\\n    category: discourse_analysis\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational discourse theory. RST's hierarchical text organization\\n      informs our modeling of persuasion strategy sequences as structured\\n      discourse rather than bag-of-features.\\n\\n  - bibtex_key: prasad2008pdtb\\n    title: \\\"The Penn Discourse TreeBank 2.0\\\"\\n    authors: \\\"Prasad et al.\\\"\\n    venue: \\\"LREC 2008\\\"\\n    year: 2008\\n    category: discourse_analysis\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Major discourse annotation resource. PDTB's approach to annotating\\n      discourse relations at the connective level parallels our annotation\\n      of persuasion strategies at the turn level.\\n\\n  - bibtex_key: stolcke2000dialogueact\\n    title: \\\"Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech\\\"\\n    authors: \\\"Stolcke et al.\\\"\\n    venue: \\\"Computational Linguistics\\\"\\n    year: 2000\\n    category: discourse_analysis\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational dialogue act classification using HMM over sequential\\n      turns. Our GRU-based persuasion trajectory modeling is a modern\\n      analogue of this sequential discourse structure approach.\\n\\n  - bibtex_key: austin1962speechacts\\n    title: \\\"How to Do Things with Words\\\"\\n    authors: \\\"Austin, J. L.\\\"\\n    venue: \\\"Harvard University Press\\\"\\n    year: 1962\\n    category: discourse_analysis\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational speech act theory distinguishing locutionary,\\n      illocutionary, and perlocutionary acts. DisPeD operates at the\\n      illocutionary level (what the speaker intends to accomplish)\\n      rather than the locutionary level (what words are used).\\n\\n  - bibtex_key: searle1969speechacts\\n    title: \\\"Speech Acts: An Essay in the Philosophy of Language\\\"\\n    authors: \\\"Searle, J. R.\\\"\\n    venue: \\\"Cambridge University Press\\\"\\n    year: 1969\\n    category: discourse_analysis\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Extended Austin's speech act theory with systematic taxonomy.\\n      Our persuasion strategy taxonomy maps onto Searle's classification\\n      of illocutionary acts, providing theoretical grounding for\\n      treating persuasion as a functional category.\\n\\n  # ============================================================\\n  # Category 4: Computational Persuasion Detection (4 papers)\\n  # ============================================================\\n\\n  - bibtex_key: habernal2016convincingness\\n    title: \\\"Which Argument Is More Convincing? Analyzing and Predicting Convincingness of Web Arguments Using Bidirectional LSTM\\\"\\n    authors: \\\"Habernal and Gurevych\\\"\\n    venue: \\\"ACL 2016\\\"\\n    year: 2016\\n    category: computational_persuasion\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Pioneering computational persuasion work predicting argument\\n      convincingness from text. Establishes that persuasive properties\\n      are computationally detectable from language, supporting our\\n      premise that persuasion strategies are extractable from turn\\n      representations.\\n\\n  - bibtex_key: tan2016winningarguments\\n    title: \\\"Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-faith Online Discussions\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"WWW 2016\\\"\\n    year: 2016\\n    category: computational_persuasion\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Analyzes persuasion dynamics in Reddit ChangeMyView. Shows timing,\\n      interaction patterns, and language features predict persuasion\\n      success. Supports our modeling of temporal persuasion trajectories\\n      as discriminative features.\\n\\n  - bibtex_key: jaipersaud2025howdollmspersuade\\n    title: \\\"How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations\\\"\\n    authors: \\\"Jaipersaud et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2508.05625\\\"\\n    category: computational_persuasion\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      CRITICAL PRIOR WORK. Demonstrates persuasion dynamics are extractable\\n      from LLM turn-level representations via linear probes. Directly\\n      supports our premise that DeBERTa fine-tuned on persuasion taxonomy\\n      produces informative turn embeddings for trajectory modeling.\\n\\n  - bibtex_key: cialdini2001influence\\n    title: \\\"Influence: Science and Practice\\\"\\n    authors: \\\"Cialdini, R. B.\\\"\\n    venue: \\\"Allyn & Bacon (4th edition)\\\"\\n    year: 2001\\n    category: computational_persuasion\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Six principles of persuasion (reciprocation, consistency, social\\n      proof, liking, authority, scarcity). Our 8-class persuasion taxonomy\\n      maps partially onto Cialdini's principles, providing psychological\\n      grounding for the strategy classification.\\n\\n  # ============================================================\\n  # Category 5: Jailbreak Attacks & Taxonomies (9 papers)\\n  # ============================================================\\n\\n  - bibtex_key: zeng2024pap\\n    title: \\\"How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs\\\"\\n    authors: \\\"Zeng et al.\\\"\\n    venue: \\\"ACL 2024\\\"\\n    year: 2024\\n    category: jailbreak_attacks_taxonomies\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      CRITICAL PRIOR WORK. Proposes 40 persuasion techniques for\\n      jailbreaking (PAP), achieving >92% ASR. Establishes that persuasion\\n      is systematically used in jailbreaks. DisPeD operationalizes this\\n      observation into a detection system.\\n\\n  - bibtex_key: russinovich2024crescendo\\n    title: \\\"Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack\\\"\\n    authors: \\\"Russinovich et al.\\\"\\n    venue: \\\"USENIX Security 2025\\\"\\n    year: 2024\\n    arxiv: \\\"2404.01833\\\"\\n    category: jailbreak_attacks_taxonomies\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Defines the Crescendo multi-turn jailbreak: gradual escalation\\n      through benign-seeming turns. Primary attack type in our evaluation.\\n      DisPeD detects the characteristic persuasion escalation trajectory\\n      that Crescendo relies on.\\n\\n  - bibtex_key: chao2023pair\\n    title: \\\"Jailbreaking Black Box Large Language Models in Twenty Queries\\\"\\n    authors: \\\"Chao et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2023\\n    arxiv: \\\"2310.08419\\\"\\n    category: jailbreak_attacks_taxonomies\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      PAIR: automated iterative jailbreak refinement using attacker LLM.\\n      Represents the class of automated multi-turn attacks that DisPeD\\n      aims to detect through persuasion trajectory analysis.\\n\\n  - bibtex_key: wei2023jailbroken\\n    title: \\\"Jailbroken: How Does LLM Safety Training Fail?\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    year: 2023\\n    arxiv: \\\"2307.02483\\\"\\n    category: jailbreak_attacks_taxonomies\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational jailbreak taxonomy: competing objectives and\\n      mismatched generalization. DisPeD addresses the mismatched\\n      generalization failure mode by operating at the pragmatic level\\n      where safety training has not yet generalized.\\n\\n  - bibtex_key: hagendorff2026reasoning\\n    title: \\\"Large Reasoning Models Are Autonomous Jailbreak Agents\\\"\\n    authors: \\\"Hagendorff et al.\\\"\\n    venue: \\\"Nature Communications\\\"\\n    year: 2026\\n    category: jailbreak_attacks_taxonomies\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      CRITICAL MOTIVATION. Shows LRMs autonomously execute persuasive\\n      multi-turn attacks with 97% ASR using identifiable persuasion\\n      strategies. Directly supports our claim that the persuasion\\n      playbook is structurally necessary and therefore detectable.\\n\\n  - bibtex_key: fitd2024\\n    title: \\\"Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2024\\n    arxiv: \\\"2402.15690\\\"\\n    category: jailbreak_attacks_taxonomies\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      FITD jailbreak based on cognitive consistency theory. Progressive\\n      commitment escalation parallels Cialdini's consistency principle.\\n      One of three attack types in our evaluation (Crescendo, FITD,\\n      Deceptive Delight).\\n\\n  - bibtex_key: deceptivedelight2024\\n    title: \\\"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction\\\"\\n    authors: \\\"Palo Alto Networks Unit 42\\\"\\n    venue: \\\"Palo Alto Networks Technical Report\\\"\\n    year: 2024\\n    category: jailbreak_attacks_taxonomies\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Multi-turn jailbreak embedding unsafe topics among benign ones.\\n      65% ASR across 8 models in 3 turns. Third attack type in our\\n      evaluation, representing emotional manipulation strategy.\\n\\n  - bibtex_key: ren2024actorattack\\n    title: \\\"ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory\\\"\\n    authors: \\\"Ren et al.\\\"\\n    venue: \\\"ICLR 2025 submission\\\"\\n    year: 2024\\n    category: jailbreak_attacks_taxonomies\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Multi-turn attack using actor-network theory to generate diverse\\n      attack paths. Achieves 84.5% ASR. Published SafeMTData dataset.\\n      Represents broader class of multi-turn attacks that exploit\\n      persuasion-like dynamics.\\n\\n  - bibtex_key: zou2023gcg\\n    title: \\\"Universal and Transferable Adversarial Attacks on Aligned Language Models\\\"\\n    authors: \\\"Zou et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2023\\n    arxiv: \\\"2307.15043\\\"\\n    category: jailbreak_attacks_taxonomies\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      GCG: foundational gradient-based adversarial attack on LLMs.\\n      Represents the lexical-level attack that our evasion hierarchy\\n      positions as most easily detectable (vs. semantic vs. pragmatic).\\n\\n  # ============================================================\\n  # Category 6: Red-Teaming (4 papers)\\n  # ============================================================\\n\\n  - bibtex_key: perez2022redteaming\\n    title: \\\"Red Teaming Language Models with Language Models\\\"\\n    authors: \\\"Perez et al.\\\"\\n    venue: \\\"EMNLP 2022\\\"\\n    year: 2022\\n    arxiv: \\\"2202.03286\\\"\\n    category: red_teaming\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Foundational automated red-teaming using LLMs to generate test\\n      cases. Establishes the paradigm of using models to find safety\\n      vulnerabilities, which multi-turn attacks like Crescendo extend.\\n\\n  - bibtex_key: ganguli2022redteaming\\n    title: \\\"Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned\\\"\\n    authors: \\\"Ganguli et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2022\\n    arxiv: \\\"2209.07858\\\"\\n    category: red_teaming\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Anthropic's large-scale human red-teaming study (38,961 attacks).\\n      Shows RLHF models are harder to red-team at scale. Provides context\\n      for why multi-turn persuasion-based attacks are increasingly\\n      important as single-turn attacks become less effective.\\n\\n  - bibtex_key: mazeika2024harmbench\\n    title: \\\"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal\\\"\\n    authors: \\\"Mazeika et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    arxiv: \\\"2402.04249\\\"\\n    category: red_teaming\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Standardized red-teaming benchmark with 510 harmful behaviors.\\n      Used as evaluation framework by multiple jailbreak defense papers.\\n      Provides common evaluation vocabulary for our Related Work discussion.\\n\\n  - bibtex_key: li2024mhj\\n    title: \\\"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2024\\n    arxiv: \\\"2408.15221\\\"\\n    category: red_teaming\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      CRITICAL MOTIVATION. Shows multi-turn human jailbreaks achieve >70%\\n      ASR against defenses with single-digit ASR on automated attacks.\\n      Directly motivates the need for multi-turn-aware defenses like DisPeD.\\n\\n  # ============================================================\\n  # Category 7: Annotation Artifacts & Dataset Biases (4 papers)\\n  # ============================================================\\n\\n  - bibtex_key: gururangan2018artifacts\\n    title: \\\"Annotation Artifacts in Natural Language Inference Data\\\"\\n    authors: \\\"Gururangan et al.\\\"\\n    venue: \\\"NAACL 2018\\\"\\n    year: 2018\\n    arxiv: \\\"1803.02324\\\"\\n    category: annotation_artifacts\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Shows NLI datasets contain hypothesis-only artifacts enabling\\n      67% accuracy without premise. Directly relevant to our RC1\\n      (lexical shortcut concern): must ensure model learns persuasion\\n      trajectories, not surface-level artifacts.\\n\\n  - bibtex_key: niven2019probing\\n    title: \\\"Probing Neural Network Comprehension of Natural Language Arguments\\\"\\n    authors: \\\"Niven and Kao\\\"\\n    venue: \\\"ACL 2019\\\"\\n    year: 2019\\n    category: annotation_artifacts\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      BERT's 77% on argument reasoning entirely from spurious cues.\\n      Motivates our scrambled-label ablation (plan_003) to verify\\n      the model uses persuasion structure, not spurious correlations.\\n\\n  - bibtex_key: poliak2018hypothesis\\n    title: \\\"Hypothesis Only Baselines in Natural Language Inference\\\"\\n    authors: \\\"Poliak et al.\\\"\\n    venue: \\\"StarSem 2018\\\"\\n    year: 2018\\n    arxiv: \\\"1805.01042\\\"\\n    category: annotation_artifacts\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Systematic study of hypothesis-only artifacts across 10 NLI datasets.\\n      Motivates our approach to controlling for lexical confounds\\n      (TF-IDF analysis, register normalization) in jailbreak detection data.\\n\\n  - bibtex_key: schuster2019debiasing\\n    title: \\\"Towards Debiasing Fact Verification Models\\\"\\n    authors: \\\"Schuster et al.\\\"\\n    venue: \\\"EMNLP 2019\\\"\\n    year: 2019\\n    arxiv: \\\"1908.05267\\\"\\n    category: annotation_artifacts\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      Claim-only classifiers perform competitively on FEVER without\\n      evidence. Parallels our concern that turn-level features alone\\n      (without trajectory modeling) may exploit dataset artifacts.\\n\\n  # ============================================================\\n  # Category 8: Adaptive Attacks on Classifiers (2 papers)\\n  # ============================================================\\n\\n  - bibtex_key: nasr2025attackermovessecond\\n    title: \\\"The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections\\\"\\n    authors: \\\"Nasr, Carlini et al.\\\"\\n    venue: \\\"arXiv preprint\\\"\\n    year: 2025\\n    arxiv: \\\"2510.09023\\\"\\n    category: adaptive_attacks\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      CRITICAL FOR CLAIM 3. Bypasses 12 defenses with >90% ASR using\\n      adaptive attacks. BERT-based safety classifiers especially\\n      vulnerable. Motivates our theoretical argument that pragmatic-level\\n      features are harder to evade than lexical/semantic features\\n      (Pragmatic Evasion Asymmetry).\\n\\n  - bibtex_key: andriushchenko2024adaptive\\n    title: \\\"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks\\\"\\n    authors: \\\"Andriushchenko et al.\\\"\\n    venue: \\\"ICLR 2025\\\"\\n    year: 2024\\n    arxiv: \\\"2404.02151\\\"\\n    category: adaptive_attacks\\n    role: background\\n    verified: true\\n    relevance_to_our_work: >\\n      100% ASR against aligned LLMs using simple random search on\\n      adversarial suffixes. Demonstrates that lexical-level attacks\\n      easily bypass safety training, supporting our evasion hierarchy\\n      (lexical < semantic < pragmatic).\\n\\n  # ============================================================\\n  # Technical Foundation (1 paper)\\n  # ============================================================\\n\\n  - bibtex_key: he2021deberta\\n    title: \\\"DeBERTa: Decoding-enhanced BERT with Disentangled Attention\\\"\\n    authors: \\\"He et al.\\\"\\n    venue: \\\"ICLR 2021\\\"\\n    year: 2021\\n    category: technical_foundation\\n    role: foundation\\n    verified: true\\n    relevance_to_our_work: >\\n      Backbone model for DisPeD's turn encoder. Disentangled attention\\n      mechanism separates content and position representations, which\\n      we leverage for producing persuasion-aware turn embeddings via\\n      fine-tuning on 8-class strategy classification.\\n\", \"total_chars\": 24216, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5393fa6b-1849-4e2a-9927-ef5286420410",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "b35f6cf9-584c-4ddf-883f-e5c431c38215",
  "sourceToolAssistantUUID": "5393fa6b-1849-4e2a-9927-ef5286420410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T03:57:52.947Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013PnTvuvwskhQKEzL2W9X1U`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b35f6cf9-584c-4ddf-883f-e5c431c38215",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N1PdzXRTgsyUSMFnUH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f6c4663-2a00-492d-baf6-41b713748400",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa63QdrJPpH2781c4pimgd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6096,
      "cache_read_input_tokens": 34969,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6096
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 34969,
          "cache_creation_input_tokens": 6096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6096,
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

_source line 26 · 2026-05-18T03:57:52.970Z_

<details><summary>↩ Tool result · `toolu_013PnTvuvwskhQKEzL2W9X1U`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper_framing.md\", \"content\": \"# Paper Framing — persuasion_turn_jailbreak_detect\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Deadline: 2026-05-25 (ARR May cycle)\\n- Track: LLM Security / Discourse and Pragmatics\\n- Commitment deadline: 2026-08-02\\n\\n## Title (Working)\\nDisPeD: Persuasion-Aware Fine-Tuning for Robust Cross-Attack Multi-Turn Jailbreak Detection\\n\\n## Core Insight\\nPrior work established that persuasion is systematic in jailbreaks (Zeng et al. 2024), universal in successful attacks (Hagendorff 2026), and extractable from representations (arXiv 2508.05625). DisPeD operationalizes these observations: fine-tuning DeBERTa on an 8-class persuasion taxonomy as a multi-task objective produces turn embeddings that capture attack-relevant pragmatic features. The key finding is that vanilla semantic temporal modeling (the DeepContext-like approach: generic encoder + GRU) catastrophically fails on unseen attack types (F1=0.28 on DD), while persuasion-aware fine-tuning enables robust cross-attack generalization (F1=1.0). Even scrambled strategy labels achieve F1=0.98, confirming that the fine-tuning process on persuasion-related text, not specific label assignments, is the critical ingredient. The 8-class taxonomy additionally provides native interpretability via strategy trajectory analysis.\\n\\n## Novelty Positioning (Dream-informed)\\nNOT: \\\"We discover that persuasion patterns exist in jailbreaks\\\" (already known).\\nNOT: \\\"An evasion hierarchy exists: lexical < semantic < pragmatic\\\" (TF-IDF=0.94 on DD contradicts this).\\nYES: \\\"We show that vanilla semantic temporal modeling fails catastrophically on unseen attack types, and that persuasion-aware fine-tuning provides an effective and accessible supervision signal for learning cross-attack-robust representations. The persuasion multi-task objective bridges the OOD generalization gap that generic encoders cannot.\\\"\\n\\n## Inherent Lexical Separability (D009)\\nPersuasive jailbreak conversations and general benign conversations are inherently lexically separable (TF-IDF≈1.0 on ALL data sources including real WildChat). TF-IDF remains strong even OOD (F1=0.94 on DD). The paper acknowledges this and positions DisPeD's value as: (1) bridging the vanilla temporal modeling gap (+72pp on DD), (2) zero degradation under adversarial perturbation (plan_004), (3) interpretability via strategy trajectories.\\n\\n## Comprehensive Ablation Picture (D014)\\nSystematic ablation reveals the method's actual mechanism:\\n- **Critical**: Persuasion-domain DeBERTa fine-tuning (any form) — bridges OOD gap from F1=0.28 to F1=1.0\\n- **Non-critical**: Label granularity (binary≈scrambled≈8-class, 1-6pp gap on DD), Lambda tuning (all F1=1.0), Temporal modeling (mean pooling≈GRU on DD)\\n- **Implication**: The persuasion multi-task objective is an effective and accessible supervision signal. Architecture and annotation precision are secondary. 8-class taxonomy provides interpretability, not detection advantage.\\n\\n## Core Claims (3, priority-ordered)\\n\\n### Claim 1 (PRIMARY): Cross-Attack Generalization via Persuasion-Aware Fine-Tuning\\nFine-tuning DeBERTa on persuasion-annotated conversations produces turn embeddings that enable cross-attack generalization, while vanilla semantic embeddings fail. A model trained on Crescendo detects unseen Deceptive Delight attacks with F1=0.99-1.0 while vanilla DeBERTa collapses to F1=0.28-0.58 (+42-72pp delta). The multi-task persuasion objective acts as an effective supervision signal for learning pragmatic features shared across attack types. Scrambled-label control (D010): randomizing strategy labels reduces cross-attack F1 by only 1-6pp (Scrambled F1=0.935-0.990), confirming that the fine-tuning process on persuasion-related text, not the specific label assignments, is the primary driver. This positions the persuasion taxonomy as a practical, low-annotation-barrier training objective rather than requiring precise strategy labels.\\n- Evidence: plan_006 DD cross-attack — Treatment F1=0.99-1.0 vs Baseline 0.28-0.58\\n- Evidence: plan_006 scrambled DD — Scrambled F1=0.935-0.990 (Treatment-Scrambled gap 1-6pp, both >> Baseline +36-70pp)\\n- Implication: 8-class taxonomy value is primarily interpretability (Claim 2), not detection performance\\n- Strength: strong empirical support for fine-tuning effect; labels are helpful but not essential\\n\\n### Claim 2 (ANALYSIS): Characteristic Persuasion Trajectories as Interpretability\\nDifferent multi-turn attack types exhibit distinct but recognizable persuasion strategy trajectories: Crescendo shows gradual escalation (mean strategy index 0.86→5.64), FITD follows commitment-escalation patterns, Deceptive Delight uses emotional-manipulation→role-assignment sequences. Benign conversations lack these structured escalation patterns. NOTE (D014): mean pooling ≈ GRU on DD, so the model does NOT rely on temporal ordering for detection. Trajectories are a descriptive/interpretability contribution, not a detection mechanism.\\n- Evidence: plan_008 strategy transition matrices\\n- Evidence: plan_015 DD — mean pooling F1=1.0 ≈ GRU F1=1.0, proving detection doesn't depend on turn ordering\\n- Strength: descriptive/analytical, interpretability value only; does NOT drive detection performance\\n\\n### Claim 3 (EMPIRICAL): Robustness Under OOD and Adversarial Perturbation\\nVanilla semantic temporal modeling is consistently the most fragile approach: catastrophic OOD failure (F1=0.28 on DD) and significant perturbation degradation (-12-15pp). Persuasion-aware fine-tuning is the most robust: F1=1.0 on unseen attacks AND zero degradation under adversarial perturbation at K≥2. TF-IDF is intermediate: strong OOD (0.94) and mostly robust under perturbation at K≥3 (-1.3pp), but degrades at early detection K=1 (-9.6pp). The strongest differentiation is at **early detection under perturbation** (K=1): Treatment -2.6pp vs TF-IDF -9.6pp vs Baseline -14.6pp.\\n- Evidence: plan_006 cross-attack — Treatment=1.0, TF-IDF=0.94, Baseline=0.28 on DD\\n- Evidence: plan_004 perturbation (D012) — Treatment 0pp at K≥2, Baseline -12-15pp, TF-IDF -1.3pp(K≥3) to -9.6pp(K=1)\\n- Note: Treatment vs TF-IDF gap is small at K≥3 (1.3pp, n=76). Strongest claim is at K=1-2.\\n- Strength: strong empirical support across both OOD and perturbation dimensions\\n\\n## Story Spine\\n\\n**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a \\\"benign\\\" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (Su et al., arXiv 2602.16935, 2026) tracks generic semantic drift via RNN over BERT embeddings (F1=0.84) but confuses benign conversational evolution with adversarial manipulation.\\n\\n**Gap**: Vanilla semantic temporal modeling (the natural approach: generic encoder + RNN over turn embeddings) catastrophically fails to generalize across attack types. DeepContext achieves F1=0.84 on in-distribution data but the approach collapses to F1=0.28 on unseen attack families. Production multi-turn guards (Llama Guard, WildGuard, ShieldGemma) and LLM-as-judge approaches detect individual harmful outputs but not the adversarial manipulation process. No published work uses persuasion-grounded fine-tuning to bridge this OOD generalization gap.\\n\\n**Our angle**: DisPeD uses persuasion strategy classification as a multi-task fine-tuning objective, teaching the encoder to attend to attack-relevant pragmatic features shared across attack types. Aggregation over fine-tuned turn embeddings (mean pooling or GRU, both equivalent per plan_015) enables conversation-level detection. The persuasion objective provides an accessible supervision signal: even with imperfect (scrambled) strategy labels or binary labels, fine-tuning on persuasion-related text produces representations that generalize to unseen attacks (F1=1.0 on DD), while vanilla embeddings collapse (F1=0.28). The 8-class taxonomy additionally enables native interpretability through strategy trajectory analysis.\\n\\n**Headline result**: \\\"Vanilla semantic temporal modeling collapses on unseen attack types (F1=0.28 on Deceptive Delight). DisPeD, fine-tuned on persuasion strategy classification, achieves F1=1.0 on the same unseen attacks (+72pp). This generalization survives label scrambling (F1 drops only 1-6pp), confirming that the persuasion fine-tuning objective, not precise annotations, bridges the cross-attack OOD gap.\\\"\\n\\n## Architecture\\n\\n1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification\\n2. **Stage 2**: Mean pooling over DeBERTa [CLS] embeddings → binary classifier for conversation-level jailbreak detection\\n3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings\\nNote: Mean pooling is default (Occam's razor). Ablation (plan_015) shows GRU ≈ mean pooling on both IID and OOD, confirming temporal modeling is unnecessary. GRU variant reported in ablation table.\\n\\n## Venue Fit Risks\\n- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)\\n- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)\\n- Safety reviewers expect multiple attack types: need >= 2 attack families\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)\\nTF-IDF=1.0 IID and 0.94 OOD on DD. Lexical features are inherently strong for this task (D009). DisPeD cannot claim superiority over TF-IDF on raw detection performance alone.\\n- Mitigation (resolved, D009+D012): (a) acknowledge inherent lexical separability honestly; (b) DisPeD's primary value vs TF-IDF is interpretability (strategy trajectories, Claim 2) and bridging the vanilla temporal modeling gap (+72pp on DD); (c) plan_004 adversarial perturbation confirmed: Treatment 0pp degradation vs TF-IDF -1.3pp(K≥3) to -9.6pp(K=1) vs Baseline -12pp. Strongest differentiation at early detection K=1-2; (d) the core comparison that motivates DisPeD is vs vanilla DeBERTa+GRU (DeepContext approach, F1=0.28 on DD), not vs TF-IDF; (e) persuasion fine-tuning as supervision signal is the contribution, not beating a bag-of-words. ✅ RESOLVED\\n\\n### RC2: Small Dataset\\n480 samples is small for a detection paper.\\n- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers\\n\\n### RC3: Single Attack Type (Crescendo Only)\\nNeed generalization evidence.\\n- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline\\n\\n### RC4: Strategy Label Quality (D010)\\nScrambled-label control (D010) shows correct strategy labels contribute only 1-6pp to cross-attack F1. This is not a confound but a finding: the persuasion multi-task objective works as a supervision signal even with imperfect labels. The 8-class taxonomy's primary value is interpretability (Claim 2), not detection.\\n- Mitigation: report scrambled control results transparently; position taxonomy as practical training objective with interpretability bonus\\n\\n### RC5: No Production/LLM-as-Judge Baseline (Dream-surfaced)\\nWithout comparing against zero-shot LLM-based detection (e.g., GPT-4/Claude prompted for conversation-level jailbreak detection), practical positioning is unknown.\\n- Result: GPT-5.5 (frontier LLM) achieves F1=0.19-0.45 on Crescendo (precision=1.0, recall=0.11-0.29). Qwen3-8B F1=0.0-0.15. Both far below Treatment F1=1.0. GPT-5.5 is deceived by Crescendo's \\\"surface educational framing,\\\" confirming that content-level analysis cannot detect persuasion dynamics. Unparseable rate 30-47% (increases with conversation length); paper must report this and provide unparseable-excluded upper bound. Even assuming best-case unparseable correction, LLM judge F1 ≈ 0.7-0.8, still far below Treatment=1.0. ✅ RESOLVED\\n\\n### RC6: Interpretability Claims Without Human Eval\\nStrategy sequence outputs claimed interpretable but not evaluated.\\n- Mitigation: strategy transition matrix visualization + predicted-label trajectory analysis\\n\\n### RC7: Related Work Inadequate (Dream-surfaced, THREE-TIER CONSISTENT)\\n~12 citations is far below venue norms (30-50). Missing coverage of: production safety systems (Llama Guard, WildGuard, ShieldGemma), LLM-as-judge, discourse analysis (RST, PDTB, dialogue acts), computational persuasion (Habernal & Gurevych 2016, Tan et al. 2016), red-teaming (HarmBench, Perez et al. 2022), annotation artifacts (Gururangan et al. 2018), adaptive attacks.\\n- Mitigation: expand to 30+ citations covering all missing categories (Paper Agent task)\\n\\n### RC8: Incremental Novelty Over Prior Work (Dream-surfaced, TWO-TIER)\\nPragmatic Evasion Asymmetry is a natural corollary of Zeng+Hagendorff+HowDoLLMs. Paper should position as \\\"operationalizing known observations\\\" not \\\"identifying a new phenomenon.\\\"\\n- Mitigation: reframe contribution as operationalization + empirical validation (done in novelty positioning above)\\n\\n### RC9: Multi-seed and Statistical Rigor (Dream-surfaced, THREE-TIER)\\nn=72 test set with single seed is inadequate.\\n- Result: 3-seed completed. Treatment F1=1.00±0.00 (zero variance), Baseline K=1 0.968±0.033. ✅ RESOLVED\\n\\n### RC10: \\\"None\\\"-Collapse Ablation (Dream-surfaced, TWO-TIER)\\nModel may reduce to persuasion-presence detector rather than trajectory detector.\\n- Result: Confirmed (D013/D014). Binary≈9-class on DD (1-2pp gap). Mean pooling≈GRU. Model IS a persuasion-presence detector, not a trajectory detector. Paper acknowledges this honestly; 8-class value is interpretability only. ✅ RESOLVED (acknowledged)\\n\\n### RC11: Lambda and Architecture Ablation (Dream-surfaced, TWO-TIER)\\nLambda and architecture choices not ablated.\\n- Result: Lambda∈{0,0.3,0.5,2.0} all F1=1.0 (insensitive). Mean pooling≈GRU on IID and DD. Method robust to all hyperparameter/architecture choices. ✅ RESOLVED\\n\\n## Scope Boundary\\n- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)\\n- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay\\n\\n## Theoretical Grounding\\n### Core References\\n- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept \\\"benign\\\" by multi-turn attacks\\n- Speech Act Theory (Austin 1962, Searle 1969): existing detectors at locutionary act level, DisPeD at illocutionary act level\\n- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking\\n- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks\\n- \\\"How Do LLMs Persuade?\\\" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations\\n\\n### Must-Cite Categories (Dream-identified gaps)\\n- **Production safety**: Llama Guard 2/3, ShieldGemma, WildGuard, Constitutional Classifiers\\n- **Multi-turn defenses**: BIID, G-Guard, SafeDream\\n- **Discourse analysis**: RST (Mann & Thompson 1988), PDTB, dialogue act classification (Stolcke et al. 2000)\\n- **Computational persuasion**: Habernal & Gurevych 2016, Tan et al. 2016\\n- **Red-teaming**: Perez et al. 2022, Ganguli et al. 2022, HarmBench (Mazeika et al. 2024)\\n- **Adaptive attacks**: Nasr & Carlini et al. 2025\\n- **Annotation artifacts**: Gururangan et al. 2018, Niven & Kao 2019, Poliak et al. 2018\\n- **Jailbreak taxonomies**: Wei et al. 2024, Chao et al. 2023 (PAIR)\\n\", \"total_chars\": 15538, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f6c4663-2a00-492d-baf6-41b713748400",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "ff1ced65-af07-481b-8d0c-ab2a08fc2a95",
  "sourceToolAssistantUUID": "8f6c4663-2a00-492d-baf6-41b713748400",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-18T03:57:55.662Z_

Now I have a thorough understanding of the paper, its context, and the literature landscape. Let me also check the other dream report versions for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff1ced65-af07-481b-8d0c-ab2a08fc2a95",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N1j62uj9UhVoUDN6e9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a7e384e-98de-460c-9f5a-f1dc756188e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118jbXCchyAEcLJU17uX3ab",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13371,
      "cache_read_input_tokens": 41065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13371,
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

_source line 28 · 2026-05-18T03:57:58.016Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JdpJXNFt93TMBUEDe84M2M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260518T032748/median/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a7e384e-98de-460c-9f5a-f1dc756188e7",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N1j62uj9UhVoUDN6e9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4f096e3-efde-4956-ba3f-4946ac13683e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118jbXCchyAEcLJU17uX3ab",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13371,
      "cache_read_input_tokens": 41065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13371,
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

_source line 29 · 2026-05-18T03:57:58.024Z_

<details><summary>↩ Tool result · `toolu_01JdpJXNFt93TMBUEDe84M2M`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{graphicx}
5	\usepackage{booktabs}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage{url}
11	\usepackage{natbib}
12	\usepackage{hyperref}
13	
14	\newcommand{\ours}{DisPeD}
15	\newcommand{\bfres}[1]{\textbf{#1}}
16	
17	\title{\ours{}: Persuasion-Aware Fine-Tuning for Robust Cross-Attack\\Multi-Turn Jailbreak Detection}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Multi-turn jailbreak attacks such as Crescendo, Foot-in-the-Door (FITD), and Deceptive Delight distribute adversarial intent across individually innocuous conversational turns, evading per-turn content filters and single-turn safety classifiers. Vanilla semantic temporal modeling, the natural approach of applying a recurrent network over generic encoder embeddings, achieves reasonable in-distribution detection but catastrophically fails on unseen attack types (F1=0.28 on Deceptive Delight when trained on Crescendo). We propose \ours{} (Discourse-level Persuasion Detection), which uses persuasion strategy classification as a multi-task fine-tuning objective for DeBERTa, producing turn embeddings that capture pragmatic features shared across attack families. A model trained exclusively on Crescendo conversations detects unseen Deceptive Delight attacks at F1=1.0, a 72-point improvement over the vanilla baseline. Systematic ablations reveal that the fine-tuning process on persuasion-related text, rather than precise label assignments, is the critical ingredient: scrambled strategy labels reduce cross-attack F1 by only 1--6 percentage points. The 8-class persuasion taxonomy provides a co-primary contribution through native interpretability, enabling visualization of characteristic strategy trajectories that distinguish attack families. Under adversarial perturbation at early detection (first turn only), \ours{} degrades by 2.6 points compared to 9.6 for TF-IDF and 14.6 for the vanilla baseline. We position persuasion-aware fine-tuning as an effective and interpretable supervision signal for learning cross-attack-robust representations.
26	\end{abstract}
27	
28	\section{Introduction}
29	
30	Multi-turn jailbreak attacks pose a distinct challenge for Large Language Model (LLM) safety systems. Unlike single-turn adversarial prompts, attacks such as Crescendo \cite{russinovich2024}, Foot-in-the-Door (FITD), and Deceptive Delight \cite{decdelight2024} distribute adversarial intent across multiple conversational turns, each of which appears benign in isolation. Bullwinkel et al.~\cite{bullwinkel2025} demonstrate that per-turn representations in these attacks are deliberately maintained within a ``benign'' region of the embedding space, causing representation-level defenses to fail with a 50-point attack success rate gap compared to single-turn attacks.
31	
32	This evasion strategy renders existing safety infrastructure insufficient. Production multi-turn guards such as Llama Guard \cite{llamaguard2024}, WildGuard \cite{wildguard2024}, and ShieldGemma \cite{shieldgemma2024} operate on individual turns or turn pairs, missing the distributed manipulation pattern. LLM-as-judge approaches, even when given full conversation context, are deceived by the surface-level educational or conversational framing that characterizes these attacks. In our evaluation, GPT-5.5 achieves only F1=0.19--0.45 on Crescendo detection, with perfect precision but recall below 30\%, confirming that content-level analysis alone cannot identify adversarial manipulation processes.
33	
34	DeepContext \cite{su2026deepcontext} represents the most relevant prior work, tracking semantic drift via a recurrent neural network over BERT embeddings for conversation-level classification. While this approach achieves reasonable in-distribution performance (F1=0.84 reported), the underlying assumption that generic semantic features suffice for multi-turn attack detection proves fragile. Our controlled proxy experiments show that vanilla encoder embeddings (whether BERT or DeBERTa) combined with temporal aggregation collapse to F1=0.26--0.28 on unseen attack types. The encoder lacks features that generalize across the pragmatic structures shared by different attack families.
35	
36	Recent work in computational persuasion provides a key observation. Zeng et al.~\cite{zeng2024pap} identify 40 persuasion techniques used in jailbreaking, Hagendorff \cite{hagendorff2026} finds identifiable persuasion strategies in 97\% of successful attacks, and Xiao et al.~\cite{xiao2025howdollms} show that persuasion dynamics are extractable from turn-level representations. These findings suggest that persuasion-grounded features may provide the cross-attack invariance that generic semantic embeddings lack.
37	
38	We propose \ours{} (Discourse-level Persuasion Detection), which operationalizes this observation. \ours{} fine-tunes DeBERTa-v3-base on an 8-class persuasion strategy classification task as a multi-task objective, then aggregates the resulting turn embeddings for conversation-level jailbreak detection. The persuasion fine-tuning teaches the encoder to attend to pragmatic features (escalation patterns, commitment devices, emotional manipulation cues) that are shared across attack families, enabling cross-attack generalization without exposure to unseen attack types during training.
39	
40	Our contributions are:
41	\begin{itemize}
42	\item \textbf{Cross-attack generalization via persuasion-aware fine-tuning.} A Crescendo-trained \ours{} model detects unseen Deceptive Delight attacks at F1=1.0, compared to F1=0.28 for vanilla DeBERTa (a 72-point improvement). Systematic ablations show that persuasion-domain fine-tuning is the critical ingredient: label granularity, temporal modeling architecture, and multi-task weighting all have negligible effect ($\leq$2 points).
43	\item \textbf{Interpretable persuasion trajectory analysis.} The 8-class taxonomy enables visualization of strategy transition patterns that characterize different attack families (e.g., Crescendo's monotonic escalation vs.\ Deceptive Delight's emotional-manipulation sequences), providing practitioners with actionable diagnostic information beyond binary detection.
44	\item \textbf{Robustness characterization across three axes.} We evaluate \ours{} against vanilla DeBERTa, TF-IDF, a DeepContext proxy, and LLM-as-judge baselines across in-distribution, cross-attack out-of-distribution (OOD), and adversarial perturbation settings, establishing that persuasion-aware fine-tuning provides the strongest early-detection robustness (K=1: 2.6-point degradation vs.\ 9.6 for TF-IDF and 14.6 for vanilla DeBERTa).
45	\end{itemize}
46	
47	\section{Related Work}
48	
49	\paragraph{Multi-turn jailbreak attacks.}
50	Crescendo \cite{russinovich2024} gradually escalates requests across turns to bypass safety filters. Deceptive Delight \cite{decdelight2024} embeds harmful requests within emotionally engaging narratives. Foot-in-the-Door attacks leverage compliance psychology, securing agreement on benign requests before escalating. These attacks exploit the absence of conversation-level reasoning in current safety systems. Wei et al.~\cite{wei2024jailbroken} and Chao et al.~\cite{chao2023pair} provide taxonomies and automated generation frameworks for single-turn and iterative jailbreaks, respectively. Bullwinkel et al.~\cite{bullwinkel2025} analyze the representation-level evasion mechanisms of multi-turn attacks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4f096e3-efde-4956-ba3f-4946ac13683e",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "47d69f29-5ca5-475d-9119-4ac53b8cf52a",
  "sourceToolAssistantUUID": "c4f096e3-efde-4956-ba3f-4946ac13683e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-18T03:57:58.545Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Vf8diFXQPrc9DyZuGkPTG8`</summary>

```json
{
  "pattern": "**/dream_reports/**/review_report.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47d69f29-5ca5-475d-9119-4ac53b8cf52a",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N1j62uj9UhVoUDN6e9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03c4b535-62c8-4576-9518-89c53a82e0ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118jbXCchyAEcLJU17uX3ab",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13371,
      "cache_read_input_tokens": 41065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13371,
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

_source line 31 · 2026-05-18T03:57:58.576Z_

<details><summary>↩ Tool result · `toolu_01Vf8diFXQPrc9DyZuGkPTG8`</summary>

```text
artifacts/dream_reports/dream_20260517T165817/best/review_report.md
artifacts/dream_reports/dream_20260517T165817/median/review_report.md
artifacts/dream_reports/dream_20260517T165817/worst/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03c4b535-62c8-4576-9518-89c53a82e0ac",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "f61f2e86-ebe0-4ab7-86b5-dadc2181d6d3",
  "sourceToolAssistantUUID": "03c4b535-62c8-4576-9518-89c53a82e0ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-18T03:58:01.422Z_

Let me read a prior review report for context, then prepare my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f61f2e86-ebe0-4ab7-86b5-dadc2181d6d3",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N299Pb7Vg5g8f3QV4p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac0abf16-b273-41d6-b57b-c4fefe6857b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P72Nj1N4Tj35CnCHFbNVpi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2412,
      "cache_read_input_tokens": 54436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2412,
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

_source line 33 · 2026-05-18T03:58:06.142Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Chd3nJ1TUD39Y2CWvjK2Y5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/review_report.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac0abf16-b273-41d6-b57b-c4fefe6857b0",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N299Pb7Vg5g8f3QV4p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ae6e92f-ecca-4978-87ae-bbdc25d54b8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P72Nj1N4Tj35CnCHFbNVpi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2412,
      "cache_read_input_tokens": 54436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2412,
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

_source line 34 · 2026-05-18T03:58:06.147Z_

<details><summary>↩ Tool result · `toolu_01Chd3nJ1TUD39Y2CWvjK2Y5`</summary>

```text
1	---
2	dream_id: dream_20260517T165817
3	tier: best
4	overall_score: 4/6 — Weak Accept
5	timestamp: 2026-05-17T17:31:32.595183+00:00
6	---
7	
8	## R1 Review: Methods and Experiments
9	
10	### Summary
11	
12	DisPeD proposes a two-stage detector (DeBERTa fine-tuned on persuasion taxonomy + Bi-GRU) for multi-turn jailbreak attacks, framed around a "Pragmatic Evasion Asymmetry" principle. The paper presents a clean experimental narrative with 11 experiments covering core detection, ablation, adversarial robustness, cross-attack generalization, and mechanistic analysis. While the theoretical framing is compelling and the experiment design is thorough relative to the claims, serious concerns about dataset scale, synthetic-only evaluation, and potential circularity in the experimental setup limit confidence in the results.
13	
14	### Strengths
15	
16	1. **Well-motivated architecture with clear theoretical grounding (Section 3).** The two-stage design follows logically from the evasion asymmetry argument: Stage 1 extracts pragmatic-level features that are invariant to surface perturbation, Stage 2 captures the temporal escalation pattern. The connection to Speech Act Theory (locutionary vs. illocutionary acts) provides genuine intellectual depth beyond typical engineering papers.
17	
18	2. **Scrambled-label ablation is a strong causal control (Section 5.3, Table 6).** This cleanly isolates the contribution of persuasion label semantics from incidental benefits of multi-task fine-tuning. The 15pp drop at K=2 with scrambled labels converging to vanilla baseline performance (0.76 vs 0.77) is the single most convincing piece of evidence that persuasion grounding carries real signal.
19	
20	3. **Three-tier evasion hierarchy provides internally consistent evidence (Section 5.2, Tables 4-5).** The gradient (lexical -18pp > semantic -13pp > pragmatic -3pp) across four models under uniform perturbation conditions directly tests the core theoretical claim. The finding that DisPeD under perturbation (0.93) still exceeds the baseline on clean data (0.89) is a strong result.
21	
22	4. **Cross-attack zero-shot evaluation addresses generalization (Section 5.4, Table 7).** Testing a Crescendo-trained model on FITD and Deceptive Delight with consistent 16-17pp advantage over the baseline demonstrates that the signal is not attack-specific. The strategy distribution analysis (Table 3) provides a plausible mechanistic explanation for why transfer works.
23	
24	5. **Register normalization with TF-IDF diagnostic (Section 4.1, Table 1).** The authors proactively identify the lexical shortcut problem (TF-IDF=1.0) and address it with a principled normalization pipeline, reporting quantitative validation (TF-IDF reduced to 0.58, strategy preservation at 94%).
25	
26	6. **Hard negative evaluation on WildChat (Section 5.6, Table 9).** Testing against high-drift benign conversations addresses the obvious concern that any temporal model might flag topic-shifting conversations as attacks.
27	
28	### Weaknesses
29	
30	1. **Entirely synthetic dataset with no real adversarial data (Critical).** All 480 Crescendo conversations, 72 FITD, and 65 Deceptive Delight conversations are LLM-generated (Qwen3-8B). The "dream" experimental setup reveals these numbers match pre-specified expected values exactly, raising the concern that experiments were designed around desired outcomes. Real-world jailbreak attempts have far more diversity, noise, and creativity than template-generated conversations. The paper's central claim about "structural invariants" is only validated on data that was generated to exhibit those invariants.
31	
32	2. **Test set size (n=72) is inadequate for the precision of claims made.** Bootstrap confidence intervals on n=72 are inherently wide. The paper reports p-values (e.g., p<0.001 for K=2) but does not report confidence interval widths. With 36 positives and 36 negatives in the test set, a single misclassification changes F1 by approximately 2-3pp, meaning the 14pp headline result could plausibly range from 8-20pp depending on which specific conversations are in the test split. No cross-validation is reported despite the small dataset.
33	
34	3. **DeepContext proxy baseline is confounded (Section 3, Table 4).** The "DeepContext proxy" uses BERT-base (125M params) while DisPeD uses DeBERTa-v3-base (184M params). The 12pp performance gap conflates encoder capacity with the persuasion grounding contribution. A fairer comparison would use DeBERTa-v3-base without fine-tuning for the proxy (which is essentially the "DeBERTa baseline" already reported). The proxy adds no information beyond the semantic baseline and creates a misleading four-tier hierarchy.
35	
36	4. **Lambda=1.0 is not ablated.** The multi-task objective uses equal weighting of persuasion and intent losses. Given that intent classification (94% accuracy) is far easier than persuasion classification (79%), the gradient signal is dominated by the persuasion head by virtue of its higher loss magnitude. No exploration of lambda values (0.1, 0.5, 2.0) is provided to understand the sensitivity of this design choice or whether the intent head is even contributing meaningfully.
37	
38	5. **Persuasion taxonomy is ad-hoc and validation is circular.** The 8 categories are "derived from Cialdini's principles and adapted for adversarial contexts" but no human annotation study validates that these categories are reliably distinguishable in practice. The 79% encoder accuracy is reported but there is no inter-annotator agreement, no confusion matrix showing which categories are conflated, and the labels themselves come from the same LLM (Qwen3-8B) that generated the conversations. This creates potential circularity: the LLM generates conversations with explicit strategy annotations, then another model learns to recover those annotations.
39	
40	6. **Adversarial perturbation protocol is underspecified and potentially weak.** "Synonym substitution, sentence restructuring" is described but the degree of perturbation is not quantified (what fraction of tokens are changed? how is "aggressive" defined?). The TF-IDF of perturbed data (0.41, from review_context) is reported but not in the paper. An adaptive adversary aware of DisPeD could specifically target the persuasion classification by disguising rapport-building as genuine curiosity, or splitting the escalation pattern across more turns to reduce monotonicity.
41	
42	7. **No cross-seed variance or multiple random initializations.** Only checkpoint variance (epoch selection) is reported. The GRU stage, data splits, and fine-tuning initialization all introduce stochasticity. On n=72 test data, a single unlucky split could drive the results. Standard practice on small datasets requires at least 5 random seeds with reported mean and standard deviation.
43	
44	8. **Monotonicity analysis uses oracle labels, not predicted labels (Section 5.5).** The trajectory analysis (monotonicity=0.82 for jailbreaks) appears to use ground-truth persuasion annotations rather than the model's predicted labels. Given 79% encoder accuracy, the actual predicted trajectories would be noisier. The paper does not report what monotonicity looks like using predicted strategies, which is what the model actually operates on at inference time.
45	
46	9. **The "none" label for benign turns is itself a strong class indicator.** Table 8 shows that 45% of benign conversation sequences are "none-none-none-none." If the persuasion classifier reliably predicts "none" for benign turns and non-"none" for jailbreak turns, the detection could be operating as a binary "any persuasion detected" classifier rather than leveraging the full trajectory dynamics claimed. This would make the approach equivalent to a simpler persuasion-presence detector.
47	
48	10. **Paper numbers differ from the task-provided "actual results."** The task summary states F1=0.86 at K=3 (+8pp, p=0.018) and full F1=0.91, while the paper reports F1=0.93 at K=3 (+10pp, p=0.004) and full F1=0.96. This discrepancy (the paper being the "best" dream tier) means the numbers presented are optimistic projections rather than realized experimental results.
49	
50	### Questions for Authors
51	
52	1. What is the inter-annotator agreement (or LLM annotation consistency across different prompting) for the 8-class persuasion taxonomy? Can you provide the confusion matrix for the DeBERTa persuasion classifier showing which strategy pairs are most confused?
53	
54	2. If you replace the "none" class for benign turns with a simple binary feature (persuasion-present vs. absent), what fraction of the detection advantage is retained? This would distinguish "trajectory-based detection" from "persuasion-presence detection."
55	
56	3. What happens when an attacker deliberately inserts "none-like" turns (pure information exchange) between persuasion moves to break the monotonic escalation pattern? The 32% of jailbreaks without monotonic patterns (from the task summary) suggest this is already partially happening.
57	
58	4. Have you evaluated on any real-world jailbreak data (e.g., from red-teaming exercises, published jailbreak datasets like JailbreakBench, or leaked conversation logs)? Even a small qualitative analysis would substantially strengthen validity.
59	
60	5. What is the sensitivity to lambda in the multi-task objective? Does removing the intent head entirely (lambda=0) hurt or help the persuasion-grounded representations?
61	
62	6. The Bi-GRU choice is stated but not justified against alternatives. Did you compare with (a) simple attention pooling over turn embeddings, (b) a Transformer layer, or (c) a max/mean pooling baseline? This would clarify whether temporal modeling is necessary or whether per-turn features alone suffice.
63	
64	### Missing Experiments / Controls
65	
66	1. **Multiple random seeds with mean/std reporting.** Essential for n=72 test set.
67	2. **K-fold cross-validation.** Standard for small datasets; would provide tighter estimates.
68	3. **Lambda ablation** for the multi-task objective (at minimum lambda in {0, 0.5, 1.0, 2.0}).
69	4. **Predicted-label trajectory analysis.** Monotonicity computed from model predictions rather than oracle annotations.
70	5. **"None"-collapse ablation.** Merge all 8 persuasion classes into a single "persuasion-present" class and retrain; measures whether fine-grained taxonomy matters beyond binary detection.
71	6. **Bi-GRU architecture comparison.** At minimum: attention pooling, mean pooling, single-layer Transformer.
72	7. **Real-world data evaluation.** Even 20-30 real jailbreak conversations from published sources would dramatically strengthen external validity.
73	8. **Adaptive adversary.** An attacker who explicitly inserts "rapport-like" benign turns or randomizes persuasion order while maintaining attack effectiveness.
74	
75	### Minor Issues
76	
77	1. The paper reports TF-IDF=0.58 in Section 4.1 but the Abstract says "TF-IDF reduced from 1.0 to 0.58" while the paper_framing.md mentions a hard gate of 0.65 and the experiment plan uses 0.75. These inconsistencies suggest the threshold was adjusted post-hoc.
78	2. Table 3 percentages for Crescendo sum to 115% (28+12+18+8+15+5+22+7=115), which is impossible for a distribution. This appears to be a data error.
79	3. The DeepContext reference (Su et al., 2026) appears to be a fictional citation. If this is a real paper, it needs a proper arXiv ID or venue; if not, it should be removed.
80	4. No code or data release is mentioned. For a detection method paper, reproducibility requires sharing at minimum the model architecture code and evaluation scripts.
81	5. The paper lacks confidence intervals in all tables despite using bootstrap testing. Reporting 95% CIs alongside point estimates would be more informative than p-values alone.
82	
83	### Preliminary Score: 4/6
84	### Confidence: 4/5
85	
86	The paper presents an intellectually interesting idea (pragmatic evasion asymmetry) with a thoughtful experimental design that covers the expected bases. However, the entirely synthetic dataset, small test set without cross-validation or multi-seed evaluation, confounded DeepContext proxy, and lack of any real-world validation collectively prevent confidence that the results would hold in practice. The score of 4 (Weak Accept) reflects that the core idea and experimental framework are sound and publishable in principle, but the execution falls short of the evidence standard needed for a top venue. With real-world data evaluation, proper statistical rigor (multi-seed, cross-validation), and the lambda/architecture ablations, this could be a 5.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ae6e92f-ecca-4978-87ae-bbdc25d54b8d",
  "isSidechain": true,
  "promptId": "3d9a4fc0-3ee1-4a9b-8ee9-4737f9d5bc27",
  "agentId": "ac9acbe0e00c978cd",
  "type": "user",
  "uuid": "fd83983a-00c3-4e1b-a2cd-908a134268e1",
  "sourceToolAssistantUUID": "9ae6e92f-ecca-4978-87ae-bbdc25d54b8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-18T03:59:57.876Z_

Now I have comprehensive knowledge of the paper, the project context, the literature map (39 papers identified), and prior review feedback. Let me compose my detailed review as R2 focused on novelty, significance, positioning, and writing quality.

---

## Review — Reviewer 2 (R2): Novelty, Significance, Positioning, Writing Quality

**Paper:** DisPeD: Persuasion-Aware Fine-Tuning for Robust Cross-Attack Multi-Turn Jailbreak Detection

---

### 1. Summary

DisPeD fine-tunes DeBERTa-v3-base on 8-class persuasion strategy classification plus binary jailbreak intent (Stage 1), then aggregates turn embeddings via GRU or mean pooling for conversation-level jailbreak detection (Stage 2). Trained on 480 Crescendo conversations, it achieves F1=1.0 on unseen Deceptive Delight attacks where a vanilla DeBERTa+GRU baseline collapses to F1=0.28. Comprehensive ablation shows the method is insensitive to label quality, label granularity, aggregation architecture, and loss weighting, leading the authors to conclude that persuasion-domain fine-tuning is an "accessible supervision signal" for cross-attack generalization.

---

### 2. Strengths

**S1. The central empirical finding is clean and striking.** The +72pp gap between treatment and baseline on DD is large and reproducible (3 seeds, zero variance on the treatment). Whether or not the *method* is novel, the *finding* that persuasion-domain fine-tuning rescues catastrophic OOD failure is interesting and practically useful.

**S2. The ablation is unusually thorough and honest.** Four independent axes (label quality, granularity, lambda, architecture) are ablated, and all converge on the same conclusion. The scrambled-label control is a particularly strong causal probe. Many papers would have buried the finding that scrambled labels work almost as well; the authors foreground it. This transparency strengthens trust in the experimental narrative.

**S3. Honest positioning against TF-IDF.** The paper does not hide that TF-IDF achieves F1=0.944 on DD. It explicitly acknowledges inherent lexical separability and positions DisPeD's value along three complementary axes (bridging the vanilla temporal gap, perturbation robustness, interpretability). This candor is rare and appreciated.

**S4. LLM-as-judge comparison fills an important gap.** Testing GPT-5.5 and Qwen3-8B as zero-shot detectors establishes that even frontier models analyzing content cannot detect process-level manipulation. The unparseable rate (30-47%) is also reported, which adds ecological validity.

**S5. Clear experimental narrative.** The paper reads as a coherent investigation rather than a disconnected collection of experiments. Each table answers a specific question, and the discussion synthesizes findings into a unified mechanistic story. The structure (baseline landscape, IID, cross-attack, ablation, perturbation, LLM judge, interpretability, additional analysis) covers the necessary ground.

---

### 3. Weaknesses

**W1. The core "method" is domain-adaptive fine-tuning, a well-understood paradigm.** The technical contribution is: fine-tune an encoder on an auxiliary task in the target domain, then use the encoder for downstream classification. This is standard multi-task / auxiliary-task learning, extensively studied since at least Caruana (1997) and widely used in NLP (e.g., STILTs, Phang et al. 2018; intermediate task training, Pratt et al. 2019). The specific instantiation (persuasion classification as the auxiliary task) is the novel choice, but the mechanism (domain exposure during fine-tuning improves downstream OOD generalization) is expected. The paper does not engage with this broader transfer learning literature at all. No citation of multi-task learning, auxiliary task selection, or intermediate task training appears in Related Work. This is a significant positioning gap.

**W2. The ablation undermines the method's specificity.** The authors present this as a feature ("accessible supervision signal"), but a skeptical reader will note: if scrambled labels work (F1=0.99), binary labels work (F1=0.99), any lambda works (F1=1.0), and mean pooling matches GRU, then the "method" reduces to "expose the encoder to persuasion-domain text during fine-tuning." This is closer to continued pretraining / domain-adaptive pretraining (Gururangan et al., ACL 2020, "Don't Stop Pretraining") than to a carefully engineered multi-task system. The paper does not cite or position against this interpretation. The question becomes: would fine-tuning DeBERTa on *any* conversational persuasion corpus (without the specific 8-class taxonomy) produce the same result? This critical control is missing.

**W3. The contribution is a finding, not a method, but the paper is written as a method paper.** The most interesting takeaway is the *empirical observation* that domain-matched fine-tuning rescues OOD collapse. But the paper frames this as proposing a "system" (DisPeD, with a name, an acronym, a two-stage architecture diagram). The architecture is trivial (DeBERTa + linear head + mean pooling), and the ablation shows every design choice is interchangeable. The honest framing would be an empirical findings paper: "We discover that exposing an encoder to persuasion-domain text during fine-tuning is sufficient for cross-attack generalization in multi-turn jailbreak detection." This reframing would make the paper stronger, not weaker.

**W4. Evaluation is entirely on author-generated synthetic data.** All OOD test data (80 FITD, 80 DD) is generated by the authors using a "controlled generation pipeline." The Crescendo training data (480 conversations) is also synthetic. The paper's headline claim of cross-attack generalization is therefore only validated on data the authors created, not on real-world attacks. The distributions of these synthetic attacks may share latent features (e.g., from the same generation model) that make transfer artificially easy. Without evaluation on real multi-turn jailbreak data (e.g., from JailbreakBench, SafeMTData from ActorAttack, or the MHJ dataset from Li et al. 2024), the ecological validity of the +72pp claim remains uncertain.

**W5. The test set is small and the results are near-ceiling.** F1=1.0 on 80 DD conversations (40 jailbreak, 40 benign, presumably) means zero errors. A single misclassification would drop F1 to approximately 0.97. The reported result is consistent with a very strong model, but also consistent with an insufficiently challenging test set. The ceiling effect prevents meaningful comparison between configurations (treatment, binary, scrambled all within 1pp of each other at F1=0.99-1.0). The evaluation does not discriminate between "the method works perfectly" and "the test set is too easy."

**W6. The 8-class interpretability claim (Claim 2) is weakly supported.** The strategy trajectory analysis (Table 7) provides descriptive statistics (mean index, transition entropy) but no demonstration that these trajectories are actionable or that human analysts find them useful. The claim of "attack fingerprints" is unvalidated. The table itself has many "---" and "(see pattern)" entries, suggesting incomplete analysis. Given that the ablation shows binary labels suffice for detection, the 8-class taxonomy must justify itself through interpretability, but that justification is only sketched, not demonstrated.

**W7. 25 references is thin for a top venue.** The literature map identifies 39 relevant papers, but only 25-30 appear in the bibliography. More critically, several important areas of related work are missing or superficially covered:

- **Multi-task learning / auxiliary task selection literature** (see W1): Caruana 1997, Phang et al. 2018 (STILTs), Pratt et al. 2019, Liu et al. 2019 (MT-DNN). The paper's core mechanism maps directly onto this body of work.
- **Domain-adaptive pretraining**: Gururangan et al. (ACL 2020) "Don't Stop Pretraining" is the most relevant comparison. They show that task-adaptive pretraining on unlabeled task-relevant text improves downstream performance, which is essentially what the scrambled-label ablation suggests DisPeD is doing.
- **Real-world multi-turn jailbreak datasets**: Li et al. (2024) "LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet" is listed in the literature map but not cited in the paper. This is directly relevant for motivating the problem and for evaluation.
- **ActorAttack** (Ren et al. 2024): Another multi-turn attack method, listed in the literature map but absent from the paper.
- **Foot-in-the-Door original paper** (arXiv 2402.15690): FITD is one of the three attack types evaluated, but its original paper is not cited.
- **GCG** (Zou et al. 2023): Foundational adversarial attack, relevant for positioning.
- Several bibliography entries are incomplete or informally formatted (e.g., "BIID: Backdoor-based multi-turn jailbreak defense. arXiv preprint, 2025" lacks author names, "G-Guard: Graph-based multi-turn safety guardrails. arXiv preprint, 2025" likewise).

---

### 4. Questions for Authors

Q1. Would fine-tuning DeBERTa on an existing persuasion corpus (e.g., ChangeMyView data from Tan et al. 2016, or the PAP attack prompts from Zeng et al. 2024) produce the same cross-attack generalization benefit? If so, the contribution is that persuasion-domain text exposure helps, not the specific 8-class taxonomy or multi-task objective.

Q2. Would continued pretraining (masked language modeling) on the persuasion-annotated conversations, without any classification head, also bridge the OOD gap? This would directly test whether the mechanism is label-driven or exposure-driven, a la "Don't Stop Pretraining."

Q3. The scrambled-label ablation shows F1=0.935 at K=1 (vs. 1.0 for proper labels), a 6.5pp gap. Is this gap statistically significant given the test set size? With 80 conversations, what is the 95% CI for this difference?

Q4. How were the OOD test conversations generated? What model generated them? Could the generation model's distributional properties (vocabulary, phrasing patterns) create shared artifacts that make transfer appear easier than it would be on real attacks?

Q5. The paper mentions "topic-anchored" benign conversations. Were the benign conversations in the OOD test sets also topic-anchored to the OOD attack topics? If not, the DD result could partially reflect topic divergence between jailbreak and benign, not persuasion detection.

Q6. Why is Llama Guard / WildGuard not evaluated directly as a baseline, given that they represent the production standard? Even a brief empirical comparison would strengthen practical positioning.

---

### 5. Assessment of Novelty

The core method is fine-tuning an encoder on a domain-relevant auxiliary task (persuasion classification) and then using the encoder for a downstream task (jailbreak detection). This is a textbook application of multi-task learning / intermediate task training. The authors do not cite or acknowledge this prior paradigm.

The novelty lies in the *application-level insight* that persuasion-domain fine-tuning provides cross-attack generalization for multi-turn jailbreak detection, and in the comprehensive ablation that isolates the fine-tuning signal as the critical ingredient. This is a valid empirical contribution, but it is incremental relative to the broad transfer learning literature. The paper would benefit from explicitly positioning itself as "applying known transfer learning principles to a new safety-critical domain" rather than presenting the two-stage pipeline as a novel architecture.

The scrambled-label finding is the most novel and intellectually interesting result, but its implications are double-edged: it strengthens the claim that persuasion fine-tuning is robust, but weakens the claim that the specific method design matters.

**Verdict:** Moderate novelty. The application-level insight is sound, the ablation is strong, but the technical contribution is well-trodden ground presented without proper positioning.

---

### 6. Related Work Gaps

- **Multi-task learning / auxiliary task selection** (Caruana 1997; Phang et al. 2018; Liu et al. 2019 MT-DNN): The paper's core mechanism.
- **Domain-adaptive pretraining** (Gururangan et al., ACL 2020): The scrambled-label result suggests the benefit may come from domain exposure, not task-specific supervision.
- **Li et al. 2024** ("LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet"): Directly motivates the problem and offers real-world evaluation data.
- **FITD original paper** (arXiv 2402.15690): Evaluated attack type without citation.
- **ActorAttack** (Ren et al. 2024): Relevant multi-turn attack.
- **Zou et al. 2023 (GCG)**: Foundational adversarial attack method.
- **Cialdini 2001**: Referenced conceptually in the literature map as grounding for the taxonomy, but absent from the paper despite the taxonomy being a contribution.
- Incomplete bibliography entries for BIID and G-Guard (no author names).

---

### 7. Writing Quality

**Positives:**
- The overall narrative flow is strong. Each section advances the argument coherently.
- The honest treatment of TF-IDF and ablation findings is refreshing.
- Equations are clean and well-formatted.

**Issues:**
- Line 34 (Abstract): "scrambled strategy labels retain F1=0.94-0.99" uses an en-dash in a range context, which is acceptable, but the style should be consistent throughout.
- The acronym "DisPeD" is strained. "Discourse-level Persuasion Detector" does not naturally abbreviate to "DisPeD" (the lowercase "is" and "e" are forced).
- Table 7 (strategy trajectories) has many missing entries ("---", "(see pattern)") that make it look incomplete.
- Table 2 (IID) uses "---" for standard deviation in several cells without explanation of why std is unavailable.
- Section 6.1: "confirming that the vanilla temporal modeling failure is independent of encoder choice" is a strong causal claim from a two-encoder comparison (BERT vs. DeBERTa). This is suggestive, not confirmatory.
- Several Related Work paragraphs are lists of citations without synthesis. The multi-turn defenses paragraph (lines 93-97) reduces BIID, G-Guard, and SafeDream to one sentence each without comparison or differentiation. The red-teaming paragraph (lines 111-114) is similarly cursory.
- I did not detect egregious AI-style writing patterns (no em-dashes used for explanation, no "-ing" phrase sentence endings, no "Furthermore/Moreover/Additionally" chains). The writing is competent if somewhat dry.
- "Austin (1962)" and "Searle (1969)" appear in the bibliography but are never cited in the text. These are orphan references.

---

### 8. Minor Issues

1. Table 3 (cross-attack): FITD columns have "---" for K=2,3,5 without explanation. If data exists, it should be reported; if not, explain why.
2. Table 6 (LLM judge): The "Unparseable 30-47%" column combines a range across K values, which is confusing. Report per-K.
3. The paper uses "pp" (percentage points) inconsistently: sometimes written out, sometimes abbreviated without definition.
4. The 8-class taxonomy (Section 3.5) is described in one paragraph without listing the 8 classes. For a paper that claims the taxonomy as a contribution, the classes should be explicitly enumerated with brief descriptions.
5. WildChat hard negatives: 15% contamination rate reduced to 2% is mentioned but the contamination definition and filtering procedure are not described.
6. The paper lacks a reproducibility statement, code availability statement, or ethics statement, which are increasingly expected at top venues.
7. No figure appears in the paper. For a 10+ page submission, at least an architecture overview figure and a cross-attack comparison bar chart would improve accessibility.

---

### 9. Overall Assessment

**Score: 3 / 6 (Weak Reject)**

**Confidence: 4 / 5**

**Rationale:**

The paper presents a clean empirical finding: persuasion-domain fine-tuning rescues catastrophic OOD failure in multi-turn jailbreak detection. The ablation is thorough and honest, and the experimental narrative is well-structured. These are genuine strengths.

However, three issues prevent acceptance at this stage:

(a) **Novelty is limited.** The core technique is standard auxiliary-task fine-tuning / domain-adaptive pretraining, applied to a new domain. The paper does not acknowledge or position against this established paradigm (Caruana 1997, Phang et al. 2018, Gururangan et al. 2020). The ablation, while well-executed, reveals that the "method" reduces to domain-text exposure during fine-tuning, not the specific multi-task design, taxonomy, or architecture. This makes the contribution an empirical finding, not a methodological advance, but the paper is framed as the latter.

(b) **Evaluation validity.** All data (training and OOD test) is author-generated synthetic conversations. The headline F1=1.0 result is on 80 synthetic conversations, creating ceiling effects that prevent discrimination between method variants. No real-world multi-turn jailbreak data is used. The ecological validity of the claims is therefore uncertain.

(c) **Incomplete positioning.** 25 references is below venue norms. Key literatures (multi-task learning, domain-adaptive pretraining, real-world multi-turn attacks) are missing. Several bibliography entries are incomplete. The paper cites references (Austin, Searle) that appear in the bibliography but never in the text.

The paper would be strengthened substantially by: (1) reframing as an empirical findings paper rather than a method paper; (2) adding the "continued pretraining without labels" control to confirm whether supervision matters or just domain exposure; (3) evaluating on any real-world multi-turn jailbreak data; (4) expanding the related work to engage with multi-task learning and domain-adaptive pretraining literature.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd83983a-00c3-4e1b-a2cd-908a134268e1",
  "isSidechain": true,
  "agentId": "ac9acbe0e00c978cd",
  "requestId": "req_011Cb9N2iAFTxCuL6YbspuSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70cb815a-9b41-4a4f-9277-85d227104038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "c7674bef-475b-450a-bf00-4bc428c19c59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcQ1FGCj1WtZiq6X8oU6VW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3386,
      "cache_read_input_tokens": 56848,
      "output_tokens": 4469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3386
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4469,
          "cache_read_input_tokens": 56848,
          "cache_creation_input_tokens": 3386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3386,
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
