# Research conversation: You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a3d7f21605785749c.jsonl`
- **Structured JSON:** [`3c6514af2fe4861e1ce0.json`](../../sessions/3c/3c6514af2fe4861e1ce0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

54 recorded events

### User

_source line 1 · 2026-05-14T21:31:39.556Z_

You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus areas are **novelty** and **related work**.

## Paper Summary

Title: "Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation–Selection Gap"

The paper investigates whether consistency-based confidence signals can serve as quality estimators and sample selectors for structured information extraction (NER and RE). It compares 5 unsupervised confidence signals: log-probability (per-sample), exact-match rate, Fleiss' κ, soft Jaccard (SJ), and entity voting confidence (all instance-level). Evaluated on 2 models (Qwen3-8B, LLaMA-3.1-8B) × 2 datasets (SciERC, CoNLL-2003), plus abandoned WNUT-17 (social media NER).

**Main claims:**
1. Structural consistency signals correlate marginally more with output quality than log-probability (Δρ = +0.01–0.04 on NER), but differences are small and statistically fragile.
2. On RE, log-probability matches or exceeds structural signals.
3. **Correlation-selection gap**: Despite positive quality-estimation correlations, NO signal achieves best-of-N selection above greedy on NER. Oracle headroom is +15pp but entirely unexploited.
4. The gap is structural: instance-level signals assign the same score to all N samples from an input → degenerate to random selection for best-of-N. Only per-sample log-prob can rank → succeeds on RE (+2.3pp) but not NER.
5. N=8→16 and signal ensembling fail to close the gap.

**Key related work cited:**
- Wang et al. 2023: Self-consistency for reasoning (majority voting)
- Nédellec & Xia 2026: Consistency-accuracy correlation for hard-prompted LLMs on plant health NER/RE using surface string matching
- Kuhn et al. 2023: Semantic entropy
- Manakul et al. 2023: SelfCheckGPT
- Kadavath et al. 2022: "Language models know what they know"
- Guo et al. 2017: Calibration of neural networks
- Desai & Durrett 2020: Calibration for NLP
- Snell et al. 2024: Test-time compute scaling
- Brown et al. 2024: Large language monkeys
- CoCoA (Vashurin et al. 2025): Combining confidence + consistency
- Geifman & El-Yaniv 2017: Selective prediction
- Kuleshov & Liang 2015: Calibrated structured prediction
- Jagannatha & Yu 2022: Calibrating structured output predictors

**Key tables:**
- Table 1: 5-signal comparison on SciERC (SJ ρ=0.36 vs log-prob ρ=0.33 on NER; on RE log-prob exceeds SJ)
- Table 3: 2×2 model-dataset matrix showing SJ ρ=0.34-0.36, SJ-LP gap +0.02 to +0.06
- Table 6: Best-of-N — ALL signals ≤ greedy on NER, only log-prob beats greedy on RE
- Table 9: OOD — SJ degrades asymmetrically (hallucination consistency)
- Ensemble: AUROC +0.02, selection still fails

The paper frames itself as a "negative result / cautionary analysis" showing that self-consistency doesn't help for structured IE with fine-tuned models.

## Your Review Task

Write a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (focus on novelty, positioning, and related work coverage)
3. **Weaknesses** (focus on novelty, positioning, and related work coverage)
4. **Questions for authors**
5. **Minor issues**
6. **Overall assessment** (1-2 sentences)
7. **Scores**: Overall (1-6), Confidence (1-5)

Be thorough, critical, and fair. Evaluate:

- **Novelty**: Is the correlation-selection gap a genuinely new insight, or is it obvious / already known? The paper itself admits "this distinction between quality estimation and sample selection is well-known in calibration research but has not been empirically demonstrated for structured IE." Is empirical demonstration alone a sufficient contribution?
- **Positioning relative to Nédellec & Xia 2026**: They already studied consistency-accuracy correlation for IE. The structural metrics (SJ) could be seen as a minor extension. Is this sufficiently differentiated?
- **Contribution level**: The paper proposes no new method, no solution to the gap. Is "identifying a problem and stopping" sufficient for a top venue? Would this be Findings-level?
- **Related work completeness**: Are there missing references? Is the calibration literature coverage adequate?
- **Framing**: The paper leads with "negative finding + explanation." Is this framing effective, or does it read as post-hoc rationalization?
- **The "correlation-selection gap" concept**: Is the explanation (instance-level vs per-sample) trivial once stated? "Instance-level aggregates can't rank individual samples" — is this obvious?

Remember: this is evaluated against top ML venue standards (~25% acceptance rate).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "bcecb5f3-4274-4ba4-928f-307670bd6d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T21:31:39.559Z_

```json
{
  "parentUuid": "bcecb5f3-4274-4ba4-928f-307670bd6d6b",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
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
  "uuid": "b1aa5f57-8cb0-4818-a811-409678c5a881",
  "timestamp": "2026-05-14T21:31:39.559Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T21:31:42.530Z_



I'll start by reading the paper and related project files to ground my review in the actual content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1aa5f57-8cb0-4818-a811-409678c5a881",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3B8mMr63qzfbSLZw5qY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5dffd1a-6e94-44b6-ab7a-fc70e768e484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLztw7dLt7xYeVhePeark3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7168,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7168,
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

_source line 4 · 2026-05-14T21:31:43.091Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014tnvKSiDMQbHQjAdEn7GhN`</summary>

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
  "parentUuid": "d5dffd1a-6e94-44b6-ab7a-fc70e768e484",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3B8mMr63qzfbSLZw5qY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa1193c2-bc33-48f6-bb62-d999f0945e90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLztw7dLt7xYeVhePeark3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7168,
      "cache_read_input_tokens": 8251,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7168
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7168,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7168,
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

_source line 5 · 2026-05-14T21:31:43.095Z_

<details><summary>↩ Tool result · `toolu_014tnvKSiDMQbHQjAdEn7GhN`</summary>

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
  "parentUuid": "aa1193c2-bc33-48f6-bb62-d999f0945e90",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "a46066bc-005b-4548-a0df-63c25b405549",
  "sourceToolAssistantUUID": "aa1193c2-bc33-48f6-bb62-d999f0945e90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T21:31:46.027Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01Qq65iVwu733A9wTeMNqKuH`</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a46066bc-005b-4548-a0df-63c25b405549",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3B92VBKKRPZfsam4Nmh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c7f5f77-9f72-4034-81c6-7cbdd4b11a02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VGWJ8At7v8jH8gFHXGcEs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 7 · 2026-05-14T21:31:46.319Z_

<details><summary>↩ Tool result · `toolu_01Qq65iVwu733A9wTeMNqKuH`</summary>

```text
{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (63 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp008_re_n16（准备中）\n- exp_002_merge_conll2003（准备中）\n- exp_007_ner_llama（准备中）\n- exp001_seed456（准备中）\n- exp001_seed123（准备中）\n- exp_001_n16_seed456_full（准备中）\n- exp_001_n16_seed123_full（准备中）\n\n## 近期结论\n- **exp_017_llama_conll_n16_s456** (success): LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\n- **exp_017_llama_conll_n16** (success): —\n- **exp_017_llama_conll_n16_s123** (success): LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\n  [exp_017_llama_conll_n16_s123_5signal_report](autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123/all_signals_report.json)\n\n## 趋势\n成功 36 / 负向 17 / 失败 1 / 共 56\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c7f5f77-9f72-4034-81c6-7cbdd4b11a02",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "27f45473-7539-411b-b9c1-6dde9a065678",
  "sourceToolAssistantUUID": "3c7f5f77-9f72-4034-81c6-7cbdd4b11a02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T21:31:46.705Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01STySTBxB95nNkFfVDzTtwS`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27f45473-7539-411b-b9c1-6dde9a065678",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3B92VBKKRPZfsam4Nmh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4e1cebf-3191-4e21-9ce8-8c500dcd348c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VGWJ8At7v8jH8gFHXGcEs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15419,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1449
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 15419,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1449,
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

_source line 9 · 2026-05-14T21:31:46.716Z_

<details><summary>↩ Tool result · `toolu_01STySTBxB95nNkFfVDzTtwS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp008_re_n16（准备中）\\n- exp_002_merge_conll2003（准备中）\\n- exp_007_ner_llama（准备中）\\n- exp001_seed456（准备中）\\n- exp001_seed123（准备中）\\n- exp_001_n16_seed456_full（准备中）\\n- exp_001_n16_seed123_full（准备中）\\n\\n## 近期结论\\n- **exp_017_llama_conll_n16_s456** (success): LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\\n- **exp_017_llama_conll_n16** (success): —\\n- **exp_017_llama_conll_n16_s123** (success): LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\\n  [exp_017_llama_conll_n16_s123_5signal_report](autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123/all_signals_report.json)\\n\\n## 趋势\\n成功 36 / 负向 17 / 失败 1 / 共 56\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- ft_002: 已被终止 — unknown\\n- mvp_pilot_002: 训练失败 — unknown\\n- exp_008_re_n16_full: 已被终止 — unknown\\n\", \"total_chars\": 1038, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4e1cebf-3191-4e21-9ce8-8c500dcd348c",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "8d69ad97-b95d-432f-9eec-a83da3967fc0",
  "sourceToolAssistantUUID": "a4e1cebf-3191-4e21-9ce8-8c500dcd348c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T21:31:49.608Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Jh6qYCMqQkUbwFKyYizu18`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d69ad97-b95d-432f-9eec-a83da3967fc0",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3B9J9kwMQ8KY63j8Zfu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d0d953c-1aef-46f6-ab1e-e4c291837ccd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRxwgsArQRoKyKfv3SjUZZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 16868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1801,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 11 · 2026-05-14T21:31:49.617Z_

<details><summary>↩ Tool result · `toolu_01Jh6qYCMqQkUbwFKyYizu18`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d0d953c-1aef-46f6-ab1e-e4c291837ccd",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "0b451384-b681-40de-8e49-07f21f0ca68c",
  "sourceToolAssistantUUID": "4d0d953c-1aef-46f6-ab1e-e4c291837ccd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T21:31:50.576Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Y3Z2KXabYsgVuqG1sfgHAx`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b451384-b681-40de-8e49-07f21f0ca68c",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3B9J9kwMQ8KY63j8Zfu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de19b1d1-908c-461a-8689-615fd8c9d197",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRxwgsArQRoKyKfv3SjUZZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 16868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1801,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 13 · 2026-05-14T21:31:50.587Z_

<details><summary>↩ Tool result · `toolu_01Y3Z2KXabYsgVuqG1sfgHAx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md\", \"content\": \"# Paper Framing — struct_self_consist_ie\\n\\n> Updated 2026-05-14 post-exp-016 pivot (D019). CRITICAL NARRATIVE CHANGE: best-of-N selection fails on NER (all signals ≤ greedy). Pivot from \\\"TTS improvement\\\" to \\\"confidence estimation + correlation-selection gap\\\".\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (via ARR May 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May cycle, 2026-05-25\\n\\n## Core Claims (3 条)\\n\\n### Claim 1 (Positive — Quality Estimation)\\nStructural consistency signals (entity voting confidence, soft Jaccard) are the strongest unsupervised quality estimators for entity-level IE, significantly outperforming model confidence (log-probability) and surface agreement (FK, exact-match) at instance-level quality prediction. Entity voting achieves AUROC 0.73 / ρ=0.50 on NER, SJ achieves AUROC 0.67 / ρ=0.36 — both far above logprob (AUROC 0.56 / ρ=0.14). Voting leads SJ on full set; SJ retains unique strength in conditional evaluation (ρ=0.41) and is temperature-robust (Δρ=±0.01).\\n\\n**Key insight**: The contribution is about a FAMILY of structural consistency signals for QUALITY ESTIMATION (predicting which instances are reliable), not for per-sample selection. SJ and voting_conf both capture entity-across-sample consistency. SJ generalizes to arbitrary structured outputs; voting is simpler.\\n\\n**Evidence** (SciERC, N=8, T=1.0, unified exp_015 evaluation):\\n- NER full (n=529): voting ρ=0.502/τ=0.377/AUROC=0.728, SJ ρ=0.357/τ=0.266/AUROC=0.666, FK ρ=0.265/τ=0.203/AUROC=0.624, EM ρ=0.257/τ=0.192/AUROC=0.623, logprob ρ=0.140/τ=0.101/AUROC=0.559\\n- NER cond (n=501): voting ρ=0.450, SJ ρ=0.412, EM ρ=0.343, FK ρ=0.306, logprob ρ=0.163\\n- RE full (n=397): voting ρ=0.422/AUROC=0.716, FK ρ=0.253/AUROC=0.631, logprob ρ=0.247/AUROC=0.635, SJ ρ=0.211/AUROC=0.582, EM ρ=0.100/AUROC=0.504\\n- RE cond (n=296): voting ρ=0.463, SJ ρ=0.368, EM ρ=0.361, FK ρ=0.317, logprob ρ=0.146\\n- Temperature robustness: SJ Δρ=±0.01 across T=0.7/1.0; FK Δρ=±0.06-0.09 (SJ far more stable)\\n\\n### Claim 2 (Novel Finding — Correlation-Selection Gap)\\nInstance-level quality estimation ≠ per-sample selection ability. Despite strong instance-level correlation (ρ≈0.39-0.43), NO unsupervised confidence signal beats greedy decoding for NER best-of-N selection. On RE, only log-probability (+2.4pp over greedy) enables effective selection. The oracle headroom is large (NER +16pp, RE +18pp) but current signals cannot exploit it.\\n\\n**exp-016 evidence** (SciERC, N=8, T=1.0, n=529):\\n- NER best-of-N: greedy 0.6094 > logprob 0.6087 > ensemble 0.6043 > sj 0.6042 > voting 0.5959 > random 0.5796 (oracle 0.7692)\\n- RE best-of-N: logprob 0.3971 > greedy 0.3735 > sj 0.3680 > voting 0.3379 ≈ random 0.3380 (oracle 0.5610)\\n- Instance-level AUROC: voting_conf 0.700, SJ 0.689, ensemble 0.735 >> logprob 0.591\\n\\n**Key insight**: Consistency signals are INSTANCE-LEVEL aggregates (one score per instance). They predict which inputs are easy/hard, NOT which sample is best. Log-prob is the only PER-SAMPLE signal and uniquely enables selection on uncertain tasks (RE). This distinction between quality estimation and sample selection is the paper's most practically important finding.\\n\\n**Implications**: (a) For selective prediction / abstention → use structural consistency (AUROC 0.70+). (b) For best-of-N selection → use logprob, but only on tasks where greedy is suboptimal (RE). (c) For NER, greedy is near-optimal → TTS offers no advantage with current signals.\\n\\n### Claim 3 (Diagnostic — task-complexity boundary)\\nThe effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.\\n\\n**MVP evidence**: RE full rho_sj=0.234, RE cond rho_sj=0.372 (SJ>FK +11.8pp). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.\\n\\n**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.\\n\\n**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):\\n- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10\\n- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392\\n- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.\\n- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.\\n\\n## Story Spine\\n\\n**Problem**: LLM-based structured prediction (IE) increasingly uses multi-sample generation, but practitioners lack guidance on which confidence signals to trust — and for what purpose. Crucially, it is unknown whether signals that predict output quality (instance-level) also enable effective sample selection (per-sample-level).\\n\\n**Existing approaches & gaps**: Self-consistency in reasoning uses exact-match voting (Wang et al. 2023). USC (Chen et al. 2024) uses LLM-as-judge. For structured prediction, no systematic comparison exists across confidence signal families. More importantly, prior work conflates quality estimation with selection — assuming that high correlation with accuracy translates to effective best-of-N selection.\\n\\n**Our framing**: We systematically compare five confidence signals across four families for IE: (1) model confidence (log-probability), (2) surface agreement (FK, exact-match), (3) set-aware structural similarity (SJ), (4) entity-level majority voting. We make three findings:\\n1. Structural consistency (voting_conf/SJ) provides the strongest quality estimation (AUROC 0.73 vs logprob 0.56)\\n2. However, a **correlation-selection gap** exists: despite strong instance-level correlation, NO signal beats greedy decoding for NER selection; only logprob helps for RE (+2.4pp)\\n3. All signals degrade on relational tasks due to compound error propagation\\n\\n**Headline result template**: \\\"On NER, entity voting confidence achieves AUROC 0.73 and ρ=0.50 for quality estimation, significantly outperforming log-probability (AUROC 0.56, ρ=0.14). However, this quality estimation capability does NOT translate to effective best-of-N selection — no signal surpasses greedy decoding on NER (oracle headroom: +16pp). We identify a fundamental correlation-selection gap: instance-level consistency predicts WHICH INPUTS are reliable, not WHICH OUTPUTS are best. On RE, only per-sample log-probability enables selection (+2.4pp), while all consistency signals degrade.\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"Only one NER dataset — generalization unclear\\\"\\n- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.\\n- **Priority**: P0\\n\\n### R2: \\\"Only one model family (Qwen3-8B)\\\"\\n- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect\\n- **Priority**: P0\\n\\n### R3: \\\"FK is a strawman baseline — what about log-prob, USC, exact-match?\\\"\\n- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (SJ+voting) >> log-prob >> FK ≈ exact-match. USC discussed in related work (LLM-as-judge, orthogonal approach).\\n- **Priority**: P0, RESOLVED — results decisive\\n\\n### R3b: \\\"Voting confidence beats SJ — why use SJ?\\\"\\n- **Mitigation**: SJ generalizes to arbitrary structured outputs (relations, events, any set-structured prediction). Voting is entity-specific. NER full: voting leads (ρ=0.50 vs 0.36), but SJ retains unique strength in conditional evaluation (ρ=0.41 vs voting 0.45) and is more temperature-robust (Δρ=±0.01). RE cond: SJ ρ=0.37 competitive with voting 0.46. SJ is also more interpretable (pairwise similarity). Paper presents both as complementary instantiations of the structural consistency principle, with voting as practical default and SJ as robust/generalizable option.\\n- **Priority**: P1 — narrative adjustment needed given exp_015 unified values\\n\\n### R4: \\\"No actual TTS improvement demonstrated\\\"\\n- **Status**: ⚠️ CONFIRMED NEGATIVE by exp-016. Best-of-N selection DOES NOT beat greedy on NER with any signal. RE: only logprob +2.4pp over greedy.\\n- **Mitigation**: Paper PIVOTS to \\\"confidence estimation + correlation-selection gap analysis.\\\" exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.\\n- **Priority**: P0 — narrative pivot required\\n\\n### R5: \\\"Sample size N=8 may be too small for reliable SJ estimation\\\"\\n- **Mitigation**: exp-001 (N=16) with multi-seed robustness\\n- **Priority**: P0\\n\\n### R6: \\\"Conditional analysis cherry-picks favorable instances\\\"\\n- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.\\n- **Priority**: P0 (add sensitivity analysis)\\n\\n### R7: \\\"Only ρ as evaluation metric\\\"\\n- **Mitigation**: Add AUROC, calibration plots, Kendall's τ for all experiments\\n- **Priority**: P0\\n\\n### R8: \\\"Formula-implementation discrepancy\\\"\\n- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)\\n- **Priority**: P0, paper writing fix\\n\\n### R9: \\\"Evaluation circularity (T>0 consistency vs T=0 F1)\\\"\\n- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).\\n- **Priority**: P0\\n\\n### R10: \\\"Insufficient related work\\\" (三档一致 [B][M][W])\\n- **Mitigation**: Expand to 35+ references. Must cite:\\n  - USC (Chen 2024) — empirical differentiation, not just citation\\n  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)\\n  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021\\n  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020\\n  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016\\n  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023\\n  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024\\n  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022\\n  - **IE confidence**: Culotta & McCallum 2004\\n  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)\\n  - **[2025-2026 新颖性自查补充 — 必引]**:\\n    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出\\n    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap\\n    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案\\n    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量\\n    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\\\"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承\\\"overlooks semantically consistent outputs\\\"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机\\n  - **[2025-2026 新颖性自查补充 — 应引]**:\\n    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述\\n    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述\\n    - Semantic Entropy Probes (2024) — 低成本不确定性估计\\n    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性\\n    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务\\n    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关\\n    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位\\n    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE\\n    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE\\n  - **需新增 Related Work 小节**:\\n    - \\\"Test-Time Scaling & Sample Selection\\\" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap\\n    - \\\"Consistency for Structured IE\\\" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation\\n- **Priority**: P0, Paper Agent handles\\n\\n### R11: \\\"SJ+logprob ensemble missing\\\" (Dream 2 — both reviewers)\\n- **Status**: ✅ RESOLVED by exp-016. Results:\\n  - Ensemble AUROC: NER 0.735 (+3.5pp over best single), RE 0.719 (−0.2pp, no improvement)\\n  - Linear combo: SJ+voting best at α=0.3 (NER ρ=0.489); RE α=0.0 (pure voting)\\n  - FK negative coefficient in logistic regression → surface agreement is net-negative when structural signals present\\n  - **Interpretation**: voting_conf captures nearly all discriminative information; ensemble adds marginal value on NER, none on RE. Supports the \\\"structural consistency family\\\" narrative.\\n- **Priority**: DONE — write into paper with honest interpretation\\n\\n### R12: \\\"No supervised upper bound / reward model comparison\\\" (Dream 2)\\n- **Mitigation**: Simple logistic regression on [SJ, FK, logprob, voting_conf, EM] as proxy for trained verifier (included in exp-016). Full reward model training out of scope for this paper — discuss as future work.\\n- **Priority**: P1 (partially addressed by exp-016 ensemble)\\n\\n### R13: \\\"Headroom capture rate low (37% NER, 11% RE)\\\" (Dream 2)\\n- **Mitigation**: Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline.\\n- **Priority**: P0, paper writing\\n\\n### R14: \\\"Cross-model validation thin — need more than 2×8B\\\" (Dream 2)\\n- **Mitigation**: exp-017 (LLaMA on CoNLL, P1). 70B model infeasible within GPU budget. Acknowledge as limitation.\\n- **Priority**: P1\\n\\n### R15: \\\"Log-prob definition ambiguity — Eq.1 vs best-of-N ranking\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state \\\"all best-of-N require N forward passes; log-prob adds zero ranking overhead.\\\"\\n- **Priority**: P0, Paper Agent handles\\n\\n### R16: \\\"Zero figures — data-rich paper with only tables\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.\\n- **Priority**: P0, Paper Agent handles\\n\\n### R17: \\\"Diagnostic framework overclaimed — descriptive not prescriptive\\\" (Dream 2 cross-tier, [M][W])\\n- **Mitigation**: Soften \\\"diagnostic framework\\\" to \\\"diagnostic analysis\\\" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.\\n- **Priority**: P0, Paper Agent handles\\n\\n### R18: \\\"No discussion of when consistency WOULD help\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.\\n- **Priority**: P1, Paper Agent handles\\n\\n### R19: \\\"Negative result partially predictable for fine-tuned models\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.\\n- **Priority**: P1, Paper Agent handles\\n\\n## Venue Fit\\n\\nEMNLP is well-suited for:\\n- Systematic empirical comparison of confidence signals for structured prediction\\n- Diagnostic findings with principled explanations\\n- The \\\"comparison + boundary condition\\\" contribution pattern\\n\\nRisk assessment (post-Dream 2, all tiers 3/6):\\n- **Structural risks (三档一致)**: (1) novelty perceived as incremental, (2) related work thin, (3) single RE dataset. These are presentation/positioning issues, NOT data issues — fixable by Paper Agent.\\n- **Data-dependent risks (观察中)**: SJ vs LOGPROB ranking may be dataset-dependent (Dream imagined this; awaiting exp-002/003 real data). If confirmed → reframe as \\\"complementary signals\\\" rather than \\\"SJ dominates.\\\"\\n- **Confirmed strength**: SJ >> LOGPROB on SciERC (AUROC 0.70 vs 0.59). Structural consistency family consistently top on existing data.\\n- **Critical path**: Paper Agent (related work 35+ refs, 3+ figures, contribution reframe) > new GPU experiments.\\n\", \"total_chars\": 17895, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de19b1d1-908c-461a-8689-615fd8c9d197",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "66549572-e4ec-432e-b7bf-c2b8787bd7be",
  "sourceToolAssistantUUID": "de19b1d1-908c-461a-8689-615fd8c9d197",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T21:31:51.027Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011muGVqHpqTTJLcsWUFpN2n`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66549572-e4ec-432e-b7bf-c2b8787bd7be",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3B9J9kwMQ8KY63j8Zfu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a6db51a-d0a5-403e-be03-0441f1e9afe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRxwgsArQRoKyKfv3SjUZZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 16868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1801,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 15 · 2026-05-14T21:31:51.065Z_

<details><summary>↩ Tool result · `toolu_011muGVqHpqTTJLcsWUFpN2n`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-14T21:00:00.000Z'\\n  total_papers: 55\\ncategories: []\\npapers:\\n  wang2023selfconsistency:\\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\\n    authors:\\n    - Xuezhi Wang\\n    - Jason Wei\\n    - Dale Schuurmans\\n    - Quoc Le\\n    - Ed Chi\\n    - Sharan Narang\\n    - Aakanksha Chowdhery\\n    - Denny Zhou\\n    year: 2023\\n    venue: ICLR 2023\\n    url: https://arxiv.org/abs/2203.11171\\n    doi: ''\\n    bibtex_key: wang2023selfconsistency\\n    category: self_consistency_reasoning\\n    role: foundation\\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\\n      from closed-form answers to structured IE outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  taubenfeld2025cisc:\\n    title: Confidence Improves Self-Consistency in LLMs\\n    authors:\\n    - Amir Taubenfeld\\n    - Tom Sheffer\\n    - Eran Ofek\\n    - Amir Feder\\n    - Ariel Goldstein\\n    - Zorik Gekhman\\n    - Gal Yona\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://arxiv.org/abs/2502.06233\\n    doi: 10.18653/v1/2025.findings-acl.1030\\n    bibtex_key: taubenfeld2025cisc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\\n      same \\\"strong predictor, weak selector\\\" gap but for structured outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kang2025selfcertainty:\\n    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\n    authors:\\n    - Zhewei Kang\\n    - Xuandong Zhao\\n    - Dawn Song\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2502.18581\\n    doi: ''\\n    bibtex_key: kang2025selfcertainty\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free\\n      quality estimation that we compare against for structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kim2026reasc:\\n    title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\n    authors:\\n    - Junseok Kim\\n    - Nakyeong Yang\\n    - Kyungmin Min\\n    - Kyomin Jung\\n    year: 2026\\n    venue: ACL 2026\\n    url: https://arxiv.org/abs/2601.02970\\n    doi: ''\\n    bibtex_key: kim2026reasc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost\\n      by 70% on GSM8K. Directly relevant to our efficiency analysis.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  thirukovalluru2024atomic:\\n    title: Atomic Self-Consistency for Better Long Form Generations\\n    authors:\\n    - Raghuveer Thirukovalluru\\n    - Yukun Huang\\n    - Bhuwan Dhingra\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.706/\\n    doi: 10.18653/v1/2024.emnlp-main.706\\n    bibtex_key: thirukovalluru2024atomic\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related\\n      to our structured output aggregation approach.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  chen2024usc:\\n    title: Universal Self-Consistency for Large Language Model Generation\\n    authors:\\n    - Xinyun Chen\\n    - Renat Aksitov\\n    - Uri Alon\\n    - Jie Ren\\n    - Kefan Xiao\\n    - Pengcheng Yin\\n    - Sushant Prakash\\n    - Charles Sutton\\n    - Xuezhi Wang\\n    - Denny Zhou\\n    year: 2024\\n    venue: arXiv preprint (ICML 2024 Workshop ICL)\\n    url: https://arxiv.org/abs/2311.17311\\n    doi: ''\\n    bibtex_key: chen2024usc\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers\\n      to free-form generation. Precursor to our structured consistency approach.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  manakul2023selfcheckgpt:\\n    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'\\n    authors:\\n    - Potsawee Manakul\\n    - Adian Liusie\\n    - Mark Gales\\n    year: 2023\\n    venue: EMNLP 2023\\n    url: https://aclanthology.org/2023.emnlp-main.557/\\n    doi: 10.18653/v1/2023.emnlp-main.557\\n    bibtex_key: manakul2023selfcheckgpt\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations\\n      diverge. Motivates our consistency-based quality signal for IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  wan2025rasc:\\n    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'\\n    authors:\\n    - Guangya Wan\\n    - Yuqi Wu\\n    - Jie Chen\\n    - Sheng Li\\n    year: 2025\\n    venue: NAACL 2025\\n    url: https://aclanthology.org/2025.naacl-long.184/\\n    doi: 10.18653/v1/2025.naacl-long.184\\n    bibtex_key: wan2025rasc\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples\\n      by ~70%. Complements our approach of structured quality-aware aggregation.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  nedellec2026consistency:\\n    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings\\n      from plant-health data'\\n    authors:\\n    - Claire Nédellec\\n    - Jingbo Xia\\n    year: 2026\\n    venue: Genomics & Informatics\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\\n    doi: 10.1186/s44342-025-00063-2\\n    bibtex_key: nedellec2026consistency\\n    category: consistency_structured_ie\\n    role: direct-competitor\\n    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and\\n      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  vashurin2025cocoa:\\n    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'\\n    authors:\\n    - Roman Vashurin\\n    - Maiya Goloburda\\n    - Albina Ilina\\n    - Aleksandr Rubashevskii\\n    - Preslav Nakov\\n    - Artem Shelmanov\\n    - Maxim Panov\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2502.04964\\n    doi: ''\\n    bibtex_key: vashurin2025cocoa\\n    category: consistency_structured_ie\\n    role: background\\n    relevance: CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.\\n      Provides theoretical grounding for our dual-signal approach in structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  hobelsberger2025systematic:\\n    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\n    authors:\\n    - Christian Hobelsberger\\n    - Theresa Winner\\n    - Andreas Nawroth\\n    - Oliver Mitevski\\n    - Anna-Carolina Haensch\\n    year: 2025\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2510.20460\\n    doi: ''\\n    bibtex_key: hobelsberger2025systematic\\n    category: consistency_structured_ie\\n    role: background\\n    relevance: Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid\\n      CoCoA yields best calibration, supporting our multi-signal aggregation design.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  geng2024confidence:\\n    title: A Survey of Confidence Estimation and Calibration in Large Language Models\\n    authors:\\n    - Jiahui Geng\\n    - Fengyu Cai\\n    - Yuxia Wang\\n    - Heinz Koeppl\\n    - Preslav Nakov\\n    - Iryna Gurevych\\n    year: 2024\\n    venue: NAACL 2024\\n    url: https://arxiv.org/abs/2311.08298\\n    doi: 10.18653/v1/2024.naacl-long.366\\n    bibtex_key: geng2024confidence\\n    category: confidence_surveys\\n    role: survey\\n    relevance: Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for\\n      positioning our consistency-based confidence approach within the broader landscape.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  wen2025know:\\n    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'\\n    authors:\\n    - Bingbing Wen\\n    - Jihan Yao\\n    - Shangbin Feng\\n    - Chenjun Xu\\n    - Yulia Tsvetkov\\n    - Bill Howe\\n    - Lucy Lu Wang\\n    year: 2025\\n    venue: TACL 2025\\n    url: https://arxiv.org/abs/2407.18418\\n    doi: 10.1162/tacl_a_00754\\n    bibtex_key: wen2025know\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering\\n      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  xia2025survey:\\n    title: A Survey of Uncertainty Estimation Methods on Large Language Models\\n    authors:\\n    - Zhiqiu Xia\\n    - Jinxuan Xu\\n    - Yuqian Zhang\\n    - Hang Liu\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://aclanthology.org/2025.findings-acl.1101/\\n    doi: ''\\n    bibtex_key: xia2025survey\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,\\n      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps\\n      with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  liu2025uqcalibration:\\n    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'\\n    authors:\\n    - Xiaoou Liu\\n    - Tiejin Chen\\n    - Longchao Da\\n    - Chacha Chen\\n    - Zhen Lin\\n    - Hua Wei\\n    year: 2025\\n    venue: KDD 2025\\n    url: https://arxiv.org/abs/2503.15850\\n    doi: 10.1145/3711896.3736569\\n    bibtex_key: liu2025uqcalibration\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements\\n      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps\\n      with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  kuhn2023semantic:\\n    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'\\n    authors:\\n    - Lorenz Kuhn\\n    - Yarin Gal\\n    - Sebastian Farquhar\\n    year: 2023\\n    venue: ICLR 2023\\n    url: https://arxiv.org/abs/2302.09664\\n    doi: ''\\n    bibtex_key: kuhn2023semantic\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs. Foundation\\n      for our structured consistency metric that operates at the semantic level of IE triples.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  kadavath2022language:\\n    title: Language Models (Mostly) Know What They Know\\n    authors:\\n    - Saurav Kadavath\\n    - Tom Conerly\\n    - Amanda Askell\\n    - Tom Henighan\\n    - Dawn Drain\\n    - Ethan Perez\\n    - Nicholas Schiefer\\n    - Zac Hatfield-Dodds\\n    - Nova DasSarma\\n    - Eli Tran-Johnson\\n    - Scott Johnston\\n    - Sheer El-Showk\\n    - Andy Jones\\n    - Nelson Elhage\\n    - Tristan Hume\\n    - Anna Chen\\n    - Yuntao Bai\\n    - Sam Bowman\\n    - Stanislav Fort\\n    - Deep Ganguli\\n    - Danny Hernandez\\n    - Josh Jacobson\\n    - Jackson Kernion\\n    - Shauna Kravec\\n    - Liane Lovitt\\n    - Kamal Ndousse\\n    - Catherine Olsson\\n    - Sam Ringer\\n    - Dario Amodei\\n    - Tom Brown\\n    - Jack Clark\\n    - Nicholas Joseph\\n    - Ben Mann\\n    - Sam McCandlish\\n    - Chris Olah\\n    - Jared Kaplan\\n    year: 2022\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2207.05221\\n    doi: ''\\n    bibtex_key: kadavath2022language\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge\\n      as a confidence signal, which we extend to structured IE output quality estimation.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  guo2017calibration:\\n    title: On Calibration of Modern Neural Networks\\n    authors:\\n    - Chuan Guo\\n    - Geoff Pleiss\\n    - Yu Sun\\n    - Kilian Q. Weinberger\\n    year: 2017\\n    venue: ICML 2017\\n    url: https://arxiv.org/abs/1706.04599\\n    doi: ''\\n    bibtex_key: guo2017calibration\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational\\n      reference for all calibration work including our LLM confidence calibration for IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  desai2020calibration:\\n    title: Calibration of Pre-trained Transformers\\n    authors:\\n    - Shrey Desai\\n    - Greg Durrett\\n    year: 2020\\n    venue: EMNLP 2020\\n    url: https://arxiv.org/abs/2003.07892\\n    doi: 10.18653/v1/2020.emnlp-main.21\\n    bibtex_key: desai2020calibration\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical\\n      calibration to the transformer era, motivating our LLM-specific calibration analysis.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  kossen2024semantic:\\n    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'\\n    authors:\\n    - Jannik Kossen\\n    - Jiatong Han\\n    - Muhammed Razzak\\n    - Lisa Schut\\n    - Shreshth Malik\\n    - Yarin Gal\\n    year: 2024\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2406.15927\\n    doi: ''\\n    bibtex_key: kossen2024semantic\\n    category: uncertainty_calibration\\n    role: background\\n    relevance: Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing\\n      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  xiong2024verbalized:\\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\n    authors:\\n    - Miao Xiong\\n    - Zhiyuan Hu\\n    - Xinyang Lu\\n    - Yifei Li\\n    - Jie Fu\\n    - Junxian He\\n    - Bryan Hooi\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2306.13063\\n    doi: ''\\n    bibtex_key: xiong2024verbalized\\n    category: uncertainty_calibration\\n    role: background\\n    relevance: Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly\\n      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  fisch2021conformal:\\n    title: Few-Shot Conformal Prediction with Auxiliary Tasks\\n    authors:\\n    - Adam Fisch\\n    - Tal Schuster\\n    - Tommi Jaakkola\\n    - Regina Barzilay\\n    year: 2021\\n    venue: ICML 2021\\n    url: https://arxiv.org/abs/2102.08898\\n    doi: 10.5555/3524938.3525234\\n    bibtex_key: fisch2021conformal\\n    category: conformal_prediction\\n    role: supplementary\\n    relevance: 'Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter\\n      prediction sets with formal coverage guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  angelopoulos2021conformal:\\n    title: Uncertainty Sets for Image Classifiers using Conformal Prediction\\n    authors:\\n    - Anastasios N. Angelopoulos\\n    - Stephen Bates\\n    - Jitendra Malik\\n    - Michael I. Jordan\\n    year: 2021\\n    venue: ICLR 2021\\n    url: https://arxiv.org/abs/2009.14193\\n    doi: ''\\n    bibtex_key: angelopoulos2021conformal\\n    category: conformal_prediction\\n    role: foundation\\n    relevance: Introduces RAPS (Regularized Adaptive Prediction Sets) with finite-sample coverage guarantees. Foundation for\\n      conformal prediction methodology we adapt to structured IE output sets.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  bates2021rcps:\\n    title: Distribution-Free, Risk-Controlling Prediction Sets\\n    authors:\\n    - Stephen Bates\\n    - Anastasios Angelopoulos\\n    - Lihua Lei\\n    - Jitendra Malik\\n    - Michael I. Jordan\\n    year: 2021\\n    venue: Journal of the ACM 2021\\n    url: https://arxiv.org/abs/2101.02703\\n    doi: 10.1145/3478535\\n    bibtex_key: bates2021rcps\\n    category: conformal_prediction\\n    role: supplementary\\n    relevance: 'Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample\\n      guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  xiao2019uncertainty:\\n    title: Quantifying Uncertainties in Natural Language Processing Tasks\\n    authors:\\n    - Yijun Xiao\\n    - William Yang Wang\\n    year: 2019\\n    venue: AAAI 2019\\n    url: https://arxiv.org/abs/1811.07253\\n    doi: 10.1609/aaai.v33i01.33017322\\n    bibtex_key: xiao2019uncertainty\\n    category: token_span_uncertainty_ner\\n    role: foundation\\n    relevance: Pioneers Bayesian uncertainty quantification for NLP tasks including NER, showing that modeling data and model\\n      uncertainty improves both performance and reliability for token-level predictions.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  shelmanov2021active:\\n    title: Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\n    authors:\\n    - Artem Shelmanov\\n    - Dmitri Puzyrev\\n    - Lyubov Kupriyanova\\n    - Denis Belyakov\\n    - Daniil Larionov\\n    - Nikita Khromov\\n    - Olga Kozlova\\n    - Ekaterina Artemova\\n    - Dmitry V. Dylov\\n    - Alexander Panchenko\\n    year: 2021\\n    venue: EACL 2021\\n    url: https://arxiv.org/abs/2101.08133\\n    doi: 10.18653/v1/2021.eacl-main.145\\n    bibtex_key: shelmanov2021active\\n    category: token_span_uncertainty_ner\\n    role: foundation\\n    relevance: Extensive empirical study of Bayesian uncertainty estimation (MC dropout variants) for sequence tagging with\\n      pre-trained models. Establishes best practices for uncertainty-guided active learning in NER.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  zhang2023ener:\\n    title: 'E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition'\\n    authors:\\n    - Zhen Zhang\\n    - Mengting Hu\\n    - Shiwan Zhao\\n    - Minlie Huang\\n    - Haotian Wang\\n    - Lemao Liu\\n    - Zhirui Zhang\\n    - Zhe Liu\\n    - Bingzhe Wu\\n    year: 2023\\n    venue: ACL Findings 2023\\n    url: https://arxiv.org/abs/2305.17854\\n    doi: 10.18653/v1/2023.findings-acl.103\\n    bibtex_key: zhang2023ener\\n    category: token_span_uncertainty_ner\\n    role: background\\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  lakshminarayanan2017ensembles:\\n    title: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\n    authors:\\n    - Balaji Lakshminarayanan\\n    - Alexander Pritzel\\n    - Charles Blundell\\n    year: 2017\\n    venue: NeurIPS 2017\\n    url: https://arxiv.org/abs/1612.01474\\n    doi: ''\\n    bibtex_key: lakshminarayanan2017ensembles\\n    category: ensemble_mc_dropout\\n    role: foundation\\n    relevance: Proposes deep ensembles as a simple, scalable alternative to Bayesian NNs for predictive uncertainty estimation.\\n      Foundational baseline for ensemble-based uncertainty quantification we compare against.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  gal2016dropout:\\n    title: 'Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning'\\n    authors:\\n    - Yarin Gal\\n    - Zoubin Ghahramani\\n    year: 2016\\n    venue: ICML 2016\\n    url: https://arxiv.org/abs/1506.02142\\n    doi: ''\\n    bibtex_key: gal2016dropout\\n    category: ensemble_mc_dropout\\n    role: foundation\\n    relevance: Establishes theoretical framework casting dropout as approximate Bayesian inference, enabling MC dropout for\\n      uncertainty estimation. Foundation for all dropout-based uncertainty methods we build upon.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  fomicheva2020unsupervised:\\n    title: Unsupervised Quality Estimation for Neural Machine Translation\\n    authors:\\n    - Marina Fomicheva\\n    - Shuo Sun\\n    - Lisa Yankovskaya\\n    - Frédéric Blain\\n    - Francisco Guzmán\\n    - Mark Fishel\\n    - Nikolaos Aletras\\n    - Vishrav Chaudhary\\n    - Lucia Specia\\n    year: 2020\\n    venue: TACL 2020\\n    url: https://arxiv.org/abs/2005.10608\\n    doi: 10.1162/tacl_a_00330\\n    bibtex_key: fomicheva2020unsupervised\\n    category: ensemble_mc_dropout\\n    role: background\\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  cobbe2021verifiers:\\n    title: Training Verifiers to Solve Math Word Problems\\n    authors:\\n    - Karl Cobbe\\n    - Vineet Kosaraju\\n    - Mohammad Bavarian\\n    - Mark Chen\\n    - Heewoo Jun\\n    - Lukasz Kaiser\\n    - Matthias Plappert\\n    - Jerry Tworek\\n    - Jacob Hilton\\n    - Reiichiro Nakano\\n    - Christopher Hesse\\n    - John Schulman\\n    year: 2021\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2110.14168\\n    doi: ''\\n    bibtex_key: cobbe2021verifiers\\n    category: verifier_reward_models\\n    role: foundation\\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\\n      Establishes the verify-then-select paradigm our method builds upon.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  lightman2024verify:\\n    title: Let's Verify Step by Step\\n    authors:\\n    - Hunter Lightman\\n    - Vineet Kosaraju\\n    - Yura Burda\\n    - Harri Edwards\\n    - Bowen Baker\\n    - Teddy Lee\\n    - Jan Leike\\n    - John Schulman\\n    - Ilya Sutskever\\n    - Karl Cobbe\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2305.20050\\n    doi: ''\\n    bibtex_key: lightman2024verify\\n    category: verifier_reward_models\\n    role: foundation\\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  wang2024mathshepherd:\\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\\n    authors:\\n    - Peiyi Wang\\n    - Lei Li\\n    - Zhihong Shao\\n    - Runxin Xu\\n    - Damai Dai\\n    - Yifei Li\\n    - Deli Chen\\n    - Yu Wu\\n    - Zhifang Sui\\n    year: 2024\\n    venue: ACL 2024\\n    url: https://arxiv.org/abs/2312.08935\\n    doi: ''\\n    bibtex_key: wang2024mathshepherd\\n    category: verifier_reward_models\\n    role: background\\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  snell2024scaling:\\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\n    authors:\\n    - Charlie Snell\\n    - Jaehoon Lee\\n    - Kelvin Xu\\n    - Aviral Kumar\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://arxiv.org/abs/2408.03314\\n    doi: ''\\n    bibtex_key: snell2024scaling\\n    category: tts_scaling\\n    role: foundation\\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  brown2024monkeys:\\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\\n    authors:\\n    - Bradley Brown\\n    - Jordan Juravsky\\n    - Ryan Ehrlich\\n    - Ronald Clark\\n    - Quoc V. Le\\n    - Christopher Ré\\n    - Azalia Mirhoseini\\n    year: 2024\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2407.21787\\n    doi: ''\\n    bibtex_key: brown2024monkeys\\n    category: tts_scaling\\n    role: foundation\\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  wu2024inference:\\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\\n    authors:\\n    - Yangzhen Wu\\n    - Zhiqing Sun\\n    - Shanda Li\\n    - Sean Welleck\\n    - Yiming Yang\\n    year: 2024\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2408.00724\\n    doi: ''\\n    bibtex_key: wu2024inference\\n    category: tts_scaling\\n    role: background\\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  kuleshov2015calibrated:\\n    title: Calibrated Structured Prediction\\n    authors:\\n    - Volodymyr Kuleshov\\n    - Percy Liang\\n    year: 2015\\n    venue: NeurIPS 2015\\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\\n    doi: ''\\n    bibtex_key: kuleshov2015calibrated\\n    category: structured_calibration_ie\\n    role: foundation\\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  culotta2004confidence:\\n    title: Confidence Estimation for Information Extraction\\n    authors:\\n    - Aron Culotta\\n    - Andrew McCallum\\n    year: 2004\\n    venue: HLT-NAACL 2004\\n    url: https://aclanthology.org/N04-4028/\\n    doi: ''\\n    bibtex_key: culotta2004confidence\\n    category: structured_calibration_ie\\n    role: foundation\\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\\n      levels. Establishes the problem setting our LLM-based approach addresses.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  jagannatha2020calibrating:\\n    title: Calibrating Structured Output Predictors for Natural Language Processing\\n    authors:\\n    - Abhyuday Jagannatha\\n    - Hong Yu\\n    year: 2020\\n    venue: ACL 2020\\n    url: https://aclanthology.org/2020.acl-main.188/\\n    doi: ''\\n    bibtex_key: jagannatha2020calibrating\\n    category: structured_calibration_ie\\n    role: background\\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  geifman2017selective:\\n    title: Selective Classification for Deep Neural Networks\\n    authors:\\n    - Yonatan Geifman\\n    - Ran El-Yaniv\\n    year: 2017\\n    venue: NeurIPS 2017\\n    url: https://arxiv.org/abs/1705.08500\\n    doi: ''\\n    bibtex_key: geifman2017selective\\n    category: selective_prediction\\n    role: foundation\\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  ren2023selfevaluation:\\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\\n    authors:\\n    - Jie Ren\\n    - Yao Zhao\\n    - Tu Vu\\n    - Peter J. Liu\\n    - Balaji Lakshminarayanan\\n    year: 2023\\n    venue: NeurIPS 2023 Workshop\\n    url: https://arxiv.org/abs/2312.09300\\n    doi: ''\\n    bibtex_key: ren2023selfevaluation\\n    category: selective_prediction\\n    role: background\\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  wadhwa2023revisiting:\\n    title: Revisiting Relation Extraction in the era of Large Language Models\\n    authors:\\n    - Somin Wadhwa\\n    - Silvio Amir\\n    - Byron Wallace\\n    year: 2023\\n    venue: ACL 2023\\n    url: https://aclanthology.org/2023.acl-long.868/\\n    doi: 10.18653/v1/2023.acl-long.868\\n    bibtex_key: wadhwa2023revisiting\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'Foundation paper: evaluates LLMs (GPT-3, Flan-T5) for relation extraction as seq2seq, showing few-shot prompting\\n      achieves near-SOTA performance. Establishes generative RE paradigm our structured consistency method builds upon.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  sainz2024gollie:\\n    title: 'GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction'\\n    authors:\\n    - Oscar Sainz\\n    - Iker García-Ferrero\\n    - Rodrigo Agerri\\n    - Oier Lopez de Lacalle\\n    - German Rigau\\n    - Eneko Agirre\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2310.03668\\n    doi: ''\\n    bibtex_key: sainz2024gollie\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'Foundation paper: fine-tunes LLM to follow annotation guidelines for zero-shot IE, achieving strong generalization\\n      to unseen tasks. Key baseline for guideline-driven structured generation in our framework.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  luan2018scierc:\\n    title: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\n    authors:\\n    - Yi Luan\\n    - Luheng He\\n    - Mari Ostendorf\\n    - Hannaneh Hajishirzi\\n    year: 2018\\n    venue: EMNLP 2018\\n    url: https://aclanthology.org/D18-1360/\\n    doi: 10.18653/v1/D18-1360\\n    bibtex_key: luan2018scierc\\n    category: generative_ie\\n    role: dataset\\n    relevance: 'Introduces SciERC dataset with entity, relation, and coreference annotations for scientific text. Primary evaluation\\n      benchmark for our structured IE experiments.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  tjongkimsang2003conll:\\n    title: 'Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition'\\n    authors:\\n    - Erik F. Tjong Kim Sang\\n    - Fien De Meulder\\n    year: 2003\\n    venue: CoNLL 2003\\n    url: https://aclanthology.org/W03-0419/\\n    doi: ''\\n    bibtex_key: tjongkimsang2003conll\\n    category: generative_ie\\n    role: dataset\\n    relevance: 'Introduces CoNLL-2003 NER dataset, the standard benchmark for named entity recognition. Core evaluation dataset\\n      for our NER consistency experiments.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  derczynski2017wnut:\\n    title: Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\n    authors:\\n    - Leon Derczynski\\n    - Eric Nichols\\n    - Marieke van Erp\\n    - Nut Limsopatham\\n    year: 2017\\n    venue: W-NUT Workshop at EMNLP 2017\\n    url: https://aclanthology.org/W17-4418/\\n    doi: ''\\n    bibtex_key: derczynski2017wnut\\n    category: generative_ie\\n    role: dataset\\n    relevance: 'Introduces WNUT-17 dataset for novel and emerging entity recognition in noisy text. Tests our method robustness\\n      on harder, low-resource NER scenarios.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  willard2023guided:\\n    title: Efficient Guided Generation for Large Language Models\\n    authors:\\n    - Brandon T. Willard\\n    - Rémi Louf\\n    year: 2023\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2307.09702\\n    doi: ''\\n    bibtex_key: willard2023guided\\n    category: generative_ie\\n    role: background\\n    relevance: 'Reformulates neural text generation as FSM transitions, enabling efficient constrained decoding with regexes and\\n      CFGs. Foundational for structured output guarantees in our IE generation pipeline.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  fleiss1971agreement:\\n    title: Measuring Nominal Scale Agreement Among Many Raters\\n    authors:\\n    - Joseph L. Fleiss\\n    year: 1971\\n    venue: Psychological Bulletin\\n    url: https://psycnet.apa.org/record/1972-05083-001\\n    doi: 10.1037/h0031619\\n    bibtex_key: fleiss1971agreement\\n    category: agreement_metrics\\n    role: foundation\\n    relevance: 'Introduces Fleiss kappa for measuring inter-rater agreement on nominal scales with multiple raters. Foundation\\n      metric for quantifying cross-sample consistency in our multi-generation IE aggregation.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  jaccard1901distribution:\\n    title: Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\n    authors:\\n    - Paul Jaccard\\n    year: 1901\\n    venue: Bulletin de la Société Vaudoise des Sciences Naturelles\\n    url: https://www.researchgate.net/publication/225035806\\n    doi: ''\\n    bibtex_key: jaccard1901distribution\\n    category: agreement_metrics\\n    role: foundation\\n    relevance: 'Introduces the Jaccard similarity coefficient for set comparison. Foundation metric for measuring pairwise overlap\\n      between extracted entity/relation sets across multiple LLM samples.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  wang2025rankedvoting:\\n    title: Ranked Voting based Self-Consistency of Large Language Models\\n    authors:\\n    - Weiqin Wang\\n    - Yile Wang\\n    - Hui Huang\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://arxiv.org/abs/2505.10772\\n    doi: ''\\n    bibtex_key: wang2025rankedvoting\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'Extends SC from single-answer majority vote to ranked answer lists with instant-runoff and Borda count voting.\\n      Relevant to our multi-candidate aggregation strategy for structured IE outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  oh2025latentsc:\\n    title: 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning'\\n    authors:\\n    - Jungsuk Oh\\n    - Jay-Yoon Lee\\n    year: 2025\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2508.18395\\n    doi: ''\\n    bibtex_key: oh2025latentsc\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'LSC: uses learnable summary token embeddings to compute semantic consistency across samples without text matching.\\n      Extends SC to long-form outputs with negligible overhead, relevant to our structured output consistency measurement.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  zhou2024uniner:\\n    title: 'UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition'\\n    authors:\\n    - Wenxuan Zhou\\n    - Sheng Zhang\\n    - Yu Gu\\n    - Muhao Chen\\n    - Hoifung Poon\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2308.03279\\n    doi: ''\\n    bibtex_key: zhou2024uniner\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'UniNER: distills ChatGPT NER capabilities into smaller models via targeted distillation on diverse entity types.\\n      Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T21:05:00.000Z'\\n  josifoski2022genie:\\n    title: 'GenIE: Generative Information Extraction'\\n    authors:\\n    - Martin Josifoski\\n    - Nicola De Cao\\n    - Maxime Peyrard\\n    - Fabio Petroni\\n    - Robert West\\n    year: 2022\\n    venue: NAACL 2022\\n    url: https://arxiv.org/abs/2112.08340\\n    doi: 10.18653/v1/2022.naacl-main.342\\n    bibtex_key: josifoski2022genie\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'First end-to-end autoregressive formulation of closed IE with bi-level constrained decoding (high-level triplet\\n      structure + prefix-trie entity/relation constraints). Directly relevant as the foundational constrained decoding approach for structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T22:00:00.000Z'\\n  li2023codeie:\\n    title: 'CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors'\\n    authors:\\n    - Peng Li\\n    - Tianxiang Sun\\n    - Qiong Tang\\n    - Hang Yan\\n    - Yuanbin Wu\\n    - Xuanjing Huang\\n    - Xipeng Qiu\\n    year: 2023\\n    venue: ACL 2023\\n    url: https://arxiv.org/abs/2305.05711\\n    doi: 10.18653/v1/2023.acl-long.855\\n    bibtex_key: li2023codeie\\n    category: generative_ie\\n    role: background\\n    relevance: 'Recasts IE as code generation, leveraging Code-LLMs structural output capabilities for NER and RE. Demonstrates\\n      alternative structured generation approach complementary to constrained decoding.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T22:00:00.000Z'\\n  wang2023instructuie:\\n    title: 'InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction'\\n    authors:\\n    - Xiao Wang\\n    - Weikang Zhou\\n    - Can Zu\\n    - Han Xia\\n    - Tianze Chen\\n    - Yuansen Zhang\\n    - Rui Zheng\\n    - Junjie Ye\\n    - Qi Zhang\\n    - Tao Gui\\n    - Jihua Kang\\n    - Jingsheng Yang\\n    - Siyuan Li\\n    - Chunsai Du\\n    year: 2023\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2304.08085\\n    doi: ''\\n    bibtex_key: wang2023instructuie\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'Unified instruction-tuned IE framework covering NER, RE, EE across 32 datasets. Demonstrates multi-task generative\\n      IE with instruction tuning, directly relevant as representative LLM-based unified IE system.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T22:00:00.000Z'\\n\", \"total_chars\": 43664, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a6db51a-d0a5-403e-be03-0441f1e9afe1",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "5e18f40a-76ff-4644-b410-30f551adda51",
  "sourceToolAssistantUUID": "5a6db51a-d0a5-403e-be03-0441f1e9afe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T21:31:51.691Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01D5bEjJ3yqtkTzPfCuVNQxt`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e18f40a-76ff-4644-b410-30f551adda51",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3B9J9kwMQ8KY63j8Zfu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24977618-f970-49f4-99d7-19a8e29b88b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRxwgsArQRoKyKfv3SjUZZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 16868,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1801
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 386,
          "cache_read_input_tokens": 16868,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1801,
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

_source line 17 · 2026-05-14T21:31:51.700Z_

<details><summary>↩ Tool result · `toolu_01D5bEjJ3yqtkTzPfCuVNQxt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 经验教训\\n\\n### Offset hallucination\\nFine-tuned generative IE 模型输出正确 entity text 但 hallucinate character offsets（准确率仅 16.7%）。必须用 span realignment 后处理修复。\\n\\n### Qwen3 think block vs XGrammar\\nQwen3 默认输出 `&lt;think>...&lt;/think>` 再接 JSON，但 XGrammar 强制 `{` 为第一个 token。必须在 `apply_chat_template` 中设 `enable_thinking=False`。\\n\\n### Train/inference prompt alignment\\n训练用 unified template \\\"Extract all structured information...\\\"，推理必须用完全一致的 template + schema hints。不对齐会导致模型不识别指令。\\n\\n### Parse failures from max_tokens truncation\\nmax_tokens=512 导致 3.7% parse failures。max_tokens=1024 完全消除（0/4408）。\\n\\n### submit_training_job 需要 tmux\\nAutoDL 5090 服务器默认无 tmux。已安装 tmux 3.2a。\\n\\n### OOM 修复：batch_size + gradient_checkpointing\\nQwen3-8B LoRA r=32 在 RTX 5090 32GB 上 batch_size=4 会 OOM。修复：batch_size=2 + gradient_accumulation_steps=8 + gradient_checkpointing=true。\\n\\n### vLLM 不能直接加载 LoRA adapter\\nvLLM 需要 merged model（有 config.json），必须先 LLaMA Factory export 合并。\\n\\n### 训练配置必须保留 best checkpoint\\nft_002_v2 的 best eval checkpoint 被 save_total_limit=3 删掉了。未来需 save_total_limit≥5 + load_best_model_at_end=true。\\n\\n### E1 否定乘性惩罚假说——RE SJ 问题是根本性的 (2026-05-14)\\n- head_sj ρ=0.210 远低于 NER ρ_sj=0.383（Δ=-0.173）\\n- 根因：span-level SJ 对 RE 根本缺乏区分力，不是公式问题\\n- 方案 B（度量分解）排除，走方案 A（NER-primary + RE 诊断）\\n\\n### SJ vs κ 在 NER 和 RE 上表现不对称——核心发现 (2026-05-14)\\n- **NER**: SJ 一致显著优于 κ（p=7e-20），ρ_sj 稳定 0.36-0.40\\n- **RE**: SJ ρ_sj 锁死 ~0.24-0.28 (取决于 N 和 T)\\n\\n### RE seed 鲁棒性确认——两 seed 高度一致 (2026-05-14)\\n- seed42: SJ ρ_full=0.281, F1=0%=44.3% | seed123: SJ ρ_full=0.2835, F1=0%=44.1%\\n- Cross-seed Δ: SJ ρ仅0.002, F1=0%仅0.2pp\\n- **结论**: RE 结构一致性弱是 task 本质属性（复合错误传播），非随机波动\\n- 不再需要额外 RE seed 测试\\n\\n### 温度对 logprob ρ 影响极大——已确认根因 (2026-05-14)\\n- T=0.7 logprob NER ρ≈0.31 vs T=1.0 ρ≈0.14-0.24\\n- 温度贡献了 ρ 差异的 74%，实例子集 22%，N 仅 4%\\n- 机制：T=1.0 使 logprob 分布更宽，噪声稀释 correlation\\n- **所有信号对比必须固定 T**。论文中 T=1.0 是标准\\n\\n### 温度对其他信号影响小 (2026-05-14)\\n- SJ ρ: T=0.7→T=1.0 变化 ±0.01\\n- FK: 温度更敏感 (NER +0.06 at T=0.7)\\n- 推荐 T=1.0 + conditional filtering\\n\\n### --num_test 200 默认值 bug (2026-05-14)\\nrun_mvp_pilot.py 默认 --num_test 200，导致多个实验只跑了 200/551 实例。已修复为 9999。\\n**所有推理命令必须显式传 --num_test 9999 或确认默认值已修改。**\\n\\n### Conditional filtering 定义不一致 (2026-05-14, 修复中)\\n- run.log 和 all_signals_report 对 \\\"conditional\\\" 定义不同，导致 RE cond ρ 差 0.127\\n- **标准定义: 排除 greedy_F1=0 的实例**（knowledge-gap instances）\\n- 在定义统一前，任何 conditional ρ 数字不可引用\\n\\n### N-scaling \\\"突破\\\" 证伪 (2026-05-14)\\n- 200 实例 T=0.7: RE voting_conf ρ=0.448（看似突破 0.40）\\n- 551 实例 T=1.0: RE voting_conf ρ=0.380（低于 0.40）\\n- 原因：小样本 + 低温度产生的 artifact。RE FAIL 确认。\\n\\n### Baseline 全景 (551 instances, T=1.0, N=16)\\nNER: voting_conf (0.399) ≈ SJ (0.398) > EM (0.339) > FK (0.288) > logprob (0.237)\\nRE: voting_conf (0.380) > logprob (0.293) > FK (0.281) > SJ (0.277) > EM (0.148)\\n\\n### exp-016 信号组合发现 (2026-05-14)\\n- SJ+voting_conf 线性组合 NER ρ=0.489 (+23%)\\n- Ensemble NER AUROC=0.735 vs best single 0.700 (+0.035)\\n- RE: logprob-best 是唯一超过 greedy 的选择策略 (0.397 vs 0.374)\\n- Oracle gap 巨大 (NER +0.16, RE +0.19)\\n\\n### exp-004 RE 诊断 (2026-05-14)\\n- FEATURE-OF 几乎无信号 (ρ≈0), HYPONYM-OF 最强 (ρ_fk=0.646)\\n- Entity span 错误占 RE FN 的 55.5%\\n- Fisher z: NER ρ_sj 显著 > RE ρ_sj (p=0.021)\\n\\n### WNUT-17 数据集不适合结构一致性分析 (2026-05-14, D045)\\n- **根因**：模型在社交媒体 NER 上能力不足（54% F1=0），信号无意义\\n- 下采样空实例到 25% 后重训仍 FAIL：SJ ρ=0.062 (p=0.106 不显著)\\n- **结论**：结构一致性信号依赖模型有足够 extraction 能力（Claim 3 capability boundary）\\n- 论文数据集收缩为 SciERC + CoNLL-2003（科学+新闻，两域足够）\\n\\n### 实验 subtask 标志必须与协议匹配 (2026-05-14)\\n- exp_001_seed456_v2 错用 `--subtask joint` 导致结果与 NER-only 的 seed42/123 不可比\\n- **规则**：3-seed 协议内的所有 run 必须用相同 --subtask 参数\\n- 需要重跑修复（exp_001_seed456_v2_ner 用 --subtask ner）\\n\\n### 查实验状态必须检查 checkpoints/ 目录 (2026-05-14)\\n- exp_017_llama_conll 被误判为 failed，因为只搜了 logs/ 和 output/\\n- 实际 checkpoint 在 checkpoints/llama3.1-8b-conll2003-lora/，日志在 checkpoints/exp017_train.log\\n- **规则**：查实验状态时搜索路径必须包含 checkpoints/, logs/, output/, 以及项目根目录\\n\\n### Cross-model SJ stability 确认——LLaMA vs Qwen (2026-05-14)\\n- LLaMA-3.1-8B NER ρ_sj=0.363 vs Qwen3-8B ρ_sj=0.398 (Δ=-0.035, 同量级)\\n- LLaMA RE ρ_sj=0.299 vs Qwen RE ρ_sj=0.277 (均弱, task-level 特性非模型特异)\\n- logprob 在 LLaMA 上更弱 (NER 0.183 vs 0.237) → SJ 优势跨模型放大\\n- **论文含义**: SJ 信号可 claim model-agnostic；RE 弱是 task 本身的属性\\n- 注意：LLaMA 用 N=8 vs Qwen N=16，N 差异可能影响精确对比\\n\\n### LLaMA CoNLL-2003 跨模型+跨数据集确认 (2026-05-14)\\n- LLaMA CoNLL N=8: SJ ρ=0.431, FK ρ=0.428, logprob ρ=0.307\\n- SJ > logprob 在所有 4 个 model×dataset 组合成立（Δ +0.124 ~ +0.180）\\n- CoNLL (easy task): SJ ≈ FK ≈ EM（easy 时 surface 信号也有效）\\n- ρ-AUROC 分离: logprob AUROC=0.761 > SJ AUROC=0.704\\n\\n### 3-seed NER 汇总——seed 鲁棒性需谨慎表述 (2026-05-14)\\n- **2-seed 对比可以 misleadingly stable**：seed42 ρ=0.428, seed123 ρ=0.424 (Δ=0.004) 看似极稳定\\n- 加入 seed456 后 ρ=0.384，Mean=0.412±0.025 (CV=6.0%)，方差比预期大\\n- **论文不应写 \\\"negligible seed variance\\\"**，应写 \\\"moderate variance (CV≈6%), structural > surface ranking preserved\\\"\\n- FK 最不稳定 (CV=12.2%)，EM 最 seed-robust (CV=1.5-3.5%)，可推荐为 robust 信号\\n- **核心 claim 不受影响**：Structural > Surface Δ≈0.15 在 3/3 seeds 全部成立\\n\\n### LLaMA CoNLL N=16 3-seed 完成——极高 seed 稳定性 (2026-05-14)\\n- 3-seed full ρ: SJ 0.463±0.007 (CV=1.6%), FK 0.455±0.006 (CV=1.3%), EM 0.460±0.008 (CV=1.7%), voting_conf 0.458±0.003 (CV=0.7%), logprob 0.310±0.006 (CV=1.8%)\\n- **所有信号 CV < 2%**，远优于 Qwen SciERC (CV=6%)\\n- 原因：CoNLL 样本量大 (n=2756) + easy task = 更稳定的估计\\n- structural > surface 3/3 seeds 全部成立 (Δ ≈ +0.15)\\n- N-scaling: 结构信号 Δρ ≈ +0.03, logprob Δρ ≈ 0 (结构信号受益 4×)\\n- **论文含义**：easy task 可 claim \\\"strong seed robustness (CV<2%)\\\"；hard task (SciERC) 为 \\\"moderate (CV≈6%)\\\"——符合 task-difficulty-dependent 叙事\\n\\n### Bootstrap CI / LOO gold_empty 过滤 bug (2026-05-14)\\n- **Bug**: bootstrap_ci_nscaling 和 loo_sj 脚本未过滤 CoNLL gold_empty 实例 (697/3453=20%)\\n- 修复前 CoNLL SJ ρ 被稀释为 0.125 (vs 正确值 0.436)\\n- **修复后验证**: CoNLL SJ ρ_N8=0.439, ρ_N16=0.450 与 registry 一致\\n- 修复后 bootstrap CI: Qwen SciERC SJ N-scaling 是唯一 95% CI 排除 0 的信号\\n- **教训**：分析脚本必须与评估脚本使用相同的数据过滤逻辑\\n\\n### Conclusion 标注规则 (2026-05-14, Director 纠正)\\n- `conclusion=failed`: 仅用于实验本身出错（crash/数据损坏/代码 bug）\\n- `conclusion=negative`: 假设未确认（verdict=FAIL），但实验正常完成\\n- `conclusion=success`: 实验正常完成且假设确认，或跨模型一致性等正面发现\\n\\n### autodl-5090 = bjb1-21071 (2026-05-14)\\n- 两个名字指向同一台机器（相同 GPU UUID）\\n- 之前\\\"cuda:0 神秘进程\\\"就是 exp_017_llama_conll\\n- **后续统一用 autodl-5090 作为服务器名**\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据集信息\\n- SciERC: 科学域, test=551 instances, HF (本地已有)\\n- CoNLL-2003: 新闻域, 4 types, test=3453, HF `BramVanroy/conll2003`\\n- WNUT-17: 社交媒体域, 6 types, test=1287 — **已放弃(D045)**，模型能力不足\\n\\n## voting_conf 命名澄清\\n- `entity_voting_conf` = per-entity majority voting (exp-014 定义, 用于 NER)\\n- `relation_tuple_match` = relation tuple exact match (exp-004 定义, 用于 RE)\\n\", \"total_chars\": 6981, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24977618-f970-49f4-99d7-19a8e29b88b7",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "6c022315-6322-4d70-a11a-3e5a6dd44f2e",
  "sourceToolAssistantUUID": "24977618-f970-49f4-99d7-19a8e29b88b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T21:31:59.282Z_

Now let me read the actual paper and the decisions/ROADMAP files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c022315-6322-4d70-a11a-3e5a6dd44f2e",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3B9s4gAgg6KEyY3eNyk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5aaa27b-53af-4736-9e73-336c53370692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xxh4JX8B39pw3comWobbWH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27250,
      "cache_read_input_tokens": 18669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27250,
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

_source line 19 · 2026-05-14T21:32:00.261Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01B6LEknFAfQTKrzENVhvcm2`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5aaa27b-53af-4736-9e73-336c53370692",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3B9s4gAgg6KEyY3eNyk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3574c53-d920-454c-8495-d669013ad658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xxh4JX8B39pw3comWobbWH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27250,
      "cache_read_input_tokens": 18669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27250,
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

_source line 20 · 2026-05-14T21:32:00.278Z_

<details><summary>↩ Tool result · `toolu_01B6LEknFAfQTKrzENVhvcm2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md\", \"content\": \"# struct_self_consist_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-14 21:11 UTC | 更新原因: abstract/conclusion/limitations 写作完成。Figures + Bootstrap CI Worker 进行中。\\n\\n## 核心方向\\n系统比较 5 类置信信号（log-prob / exact-match / FK / SJ / voting_conf）在 IE test-time scaling 中的有效性。核心发现：structural consistency family (SJ + voting_conf) 是最强质量估计器，但存在 correlation-selection gap。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Writing 阶段** — 全部 GPU 实验完成。Paper Agent Full Draft 进行中（Step 4 章节写作）。审稿进行中（Group C）。\\n\\n### 实验覆盖率\\n- **2×2 矩阵**: Qwen×{SciERC,CoNLL} + LLaMA×{SciERC,CoNLL}，全部 N=8 + N=16 完成\\n- **3-seed 鲁棒性**: Qwen SciERC (CV=6%) + LLaMA CoNLL (CV<2%) 均确认\\n- **Claim 1 覆盖**: ~85% (12/17 done, remaining: WNUT OOD blocked/abandoned)\\n- **Claim 2 覆盖**: 100% (4/4 done)\\n- **Core claim \\\"structural > logprob\\\"**: 4/4 设置全部成立，跨模型×跨数据集×跨 N×跨 seed\\n\\n### 确认发现\\n| 发现 | 来源 | 状态 |\\n|------|------|------|\\n| SJ >> logprob NER (ρ 0.383 vs 0.140, AUROC 0.689 vs 0.591) | exp-012/015 | ✅ |\\n| voting_conf ≈ SJ NER (ρ 0.502 vs 0.357) | exp-014/015 | ✅ |\\n| Correlation-selection gap: NER 无信号 beat greedy | exp-016 | ✅ |\\n| Ensemble AUROC 0.735 (+3.5pp) | exp-016 | ✅ |\\n| RE structural signals 系统性偏弱 | exp-008 | ✅ negative |\\n| RE SJ 按 sent_len 单调递增（非 inverted-U）| D047 | ✅ |\\n| FK N-scaling model-dependent（非 consistently degrading）| D050 | ✅ |\\n| LLaMA CoNLL 3-seed: structural mean ρ≈0.46, CV<2% | exp-017 | ✅ |\\n| Qwen SciERC 3-seed: SJ mean ρ=0.412, CV=6% | exp-001 | ✅ |\\n| ρ-AUROC 分离: logprob AUROC 高但 ρ 低 | 跨设置一致 | ✅ |\\n\\n### Paper Agent 进度\\n| 章节 | 状态 |\\n|------|------|\\n| experiments.tex | ✅ 完成（待 CRITICAL 修正） |\\n| method.tex | ✅ 完成（待 CRITICAL 修正：FK/EM/SJ 公式） |\\n| introduction.tex | ✅ 完成（2 WARNING 待修正） |\\n| related_work | 写作中 |\\n| discussion | 待写 |\\n| abstract.tex | ✅ 完成（~195 words, 3 key numbers） |\\n| conclusion.tex | ✅ 完成（~290 words, C1/C2/C3 + 4 future work） |\\n| limitations.tex | ✅ 完成（~210 words, 6 limitations） |\\n\\n**待修正 CRITICAL**:\\n1. method.tex FK 描述与代码不符（token-level → entity-level binary）\\n2. method.tex EM \\\"等价\\\"声称数学错误\\n3. method.tex SJ 公式过度简化（count → soft similarity sum）\\n4. experiments.tex proxy 独立性声称数据矛盾（|r|<0.15 混淆概念）\\n\\n## 近期任务\\n- [ ] Paper Agent 修正 method.tex 3 个 CRITICAL\\n- [ ] Paper Agent 修正 experiments.tex proxy 独立性 CRITICAL\\n- [x] Paper Agent 完成 abstract + conclusion + limitations\\n- [ ] Paper Agent 完成剩余章节（related_work → discussion）\\n- [ ] Paper Agent Step 5 Reviewer 循环\\n- [ ] Bootstrap CI 修复后数据整合到论文（Worker 进行中）\\n- [ ] 3+ figures 创建（Worker 进行中）\\n\\n## GPU 预算\\nautodl-5090: 4× RTX 5090 32GB — **4/4 空闲，全部实验完成**\\n**建议**：保留至论文提交前（可能需要补充实验），DDL 后释放。\\n\\n## 时间线\\n- **目标**: EMNLP 2026 via ARR May, DDL **2026-05-25**（距今 11 天）\\n- GPU 实验: ✅ 全部完成 | Paper Agent: 写作中（Step 4） | 论文迭代: 3-5 天\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D053 | 2026-05-14 | voting_conf 从 bootstrap CI 报告中排除，论文 CI 只覆盖 SJ/FK/E | exp_017_llama_conll_n16 |\\n| D052 | 2026-05-14 | P0: 热力图 conditional rho 含合成数据，暂停图表使用，从真实数据重新计算 | exp_015_unified, exp_015_v2, exp_001_seed42_v2, exp_001_seed123_v2 |\\n| D051 | 2026-05-14 | 热力图统一使用 3-seed mean，修复合成 conditional rho 数据 | exp_015_v2, exp_015_unified |\\n| D050 | 2026-05-14 | D048 修正：FK N-scaling 非一致退化，而是 setting-dependent（3/ | exp_017_llama_conll_n16, exp_002_conll_n16, exp_007_llama_n16 |\\n| D049 | 2026-05-14 | 实验端进入收尾：N=16 跨模型跨数据集确认 SJ N-scaling、FK N-degradati | exp_002_conll_n16, exp_007_llama_n16, exp_001_seed456_v2_ner, exp_009_v2_re_rerun |\\n| D048 | 2026-05-14 | FK N-scaling 退化跨设置确认：CoNLL Δ=-0.007, LLaMA SciERC  | exp_002_conll_n16, exp_007_llama_n16 |\\n| D047 | 2026-05-14 | Inverted-U 被否定：RE SJ 按 sent_len 单调递增 (Q1:0.110→Q4: | exp_009_v2_re_rerun, exp_009_capability_stratification |\\n| D046 | 2026-05-14 | seed456 NER 3-seed 确认：SJ rho=0.384, structural>sur | exp_001_seed456_v2_ner, exp_001_seed42_v2, exp_001_seed123_v2 |\\n| D045 | 2026-05-14 | WNUT-17 放弃深入：54% F1=0 + SJ rho 不显著，报告为 Claim 3 支撑证 | exp_003_wnut17_v2_infer, exp_003_wnut17_v2 |\\n| D044 | 2026-05-14 | 3-seed NER 协议完成：seed42 ρ=0.428, seed123 ρ=0.424, s | exp_001_seed456_v2_ner, exp_001_seed42_v2, exp_001_seed123_v2 |\\n\\n\", \"total_chars\": 3958, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3574c53-d920-454c-8495-d669013ad658",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "45b22c83-132b-4cc0-aac1-40883f71a78a",
  "sourceToolAssistantUUID": "a3574c53-d920-454c-8495-d669013ad658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T21:32:00.598Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012zHMyLnDvzhVQDuiACvRgB`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45b22c83-132b-4cc0-aac1-40883f71a78a",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3B9s4gAgg6KEyY3eNyk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2b6cb5f-4de5-467e-8b4a-50042facf4ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xxh4JX8B39pw3comWobbWH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27250,
      "cache_read_input_tokens": 18669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27250,
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

_source line 22 · 2026-05-14T21:32:00.614Z_

<details><summary>↩ Tool result · `toolu_012zHMyLnDvzhVQDuiACvRgB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 54\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发现两个评估缺陷必须先修：(a) 28% test instances 无 gold relations，会在 (consistency=1.0,\\n    F1=0) 处制造 artifact，必须排除；(b) 需报告 full ρ 和 conditional ρ（排除 all-samples-F1=0 的 instances），隔离\\n    knowledge-gap cluster 的稀释效应。方向反转是系统性错误（consistent wrongness），恰好对应 error taxonomy\\n    中的 \\\"systematic errors\\\" 类别——本身是有价值的分析数据点。\\n  related_experiments:\\n  - exp_id: ft_001\\n    role: gate0_eval\\n    result: NER 60.4% PASS, RE 33.8% FAIL\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 07:55 UTC\\n  summary: MVP pilot ft_001 结果：FAIL but positive signals. 等 ft_002 结果再做最终判定。\\n  rationale: ft_001 pilot 核心数据：RE ρ_sj_full=0.254 (FAIL <0.40), NER ρ_sj=0.362 (接近)。但\\n    conditional ρ（排除 knowledge-gap instances 后）显示正面信号：RE conditional ρ_sj=0.352 >\\n    ρ_fk=0.311 (Δ=+0.041)，NER conditional ρ_sj=0.369 > ρ_fk=0.357。核心假设\\\"structural\\n    > surface\\\"在控制 knowledge-gap 后成立。Oracle headroom 极大 (NER +16.9pp, RE +21.7pp)，TTS\\n    有巨大潜力。ft_002 (LoRA r=32, 5 epochs) 正在训练，如果 RE F1 提升到 ≥40%，knowledge-gap 减少可能将\\n    ρ_sj 推过 0.40。Parse failures 偏高，ft_002 pilot 需增加 max_tokens。\\n  related_experiments:\\n  - exp_id: ft_001\\n    role: mvp_pilot\\n    result: 'FAIL: RE ρ_sj_full=0.254, NER ρ_sj=0.362. Conditional: RE 0.352, NER\\n      0.369. Oracle headroom: RE +21.7pp, NER +16.9pp'\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-14 08:08 UTC\\n  summary: Narrative 选择方案 A (stay-the-course)：等 ft_002_v2 改进 RE 后重跑 pilot，保留强 claim\\n  rationale: ft_001 pilot FAIL (RE full ρ_sj=0.254 <0.30)，但诊断结论是模型 RE 质量不足而非假设方向错误。证据：(1)\\n    NER 方向全面正确 (SJ>FK, ρ=0.362)；(2) RE conditional ρ=0.352 进入 MARGINAL 且 SJ>FK (+0.041)；(3)\\n    58.3% RE samples F1=0 是 knowledge-gap 噪声淹没信号。ft_002_v2 (LoRA r=32, 5 epochs, 降\\n    batch + gradient checkpointing 防 OOM) 预期 RE F1 提升到 ≥40%，减少 knowledge-gap instances，将\\n    ρ 推向 0.40。成本仅 ~2h (训练 30min + pilot 60min)。如果 ft_002_v2 也不过，conditional ρ 分析作为\\n    fallback analytical contribution。不选 B (NER-only 太弱) 或 C (纯 conditional 有 cherry-picking\\n    风险)。\\n  related_experiments:\\n  - exp_id: mvp_pilot_001\\n    role: pilot\\n    result: 'FAIL: RE full ρ=0.254, cond ρ=0.352; NER ρ=0.362'\\n  - exp_id: ft_002\\n    role: retrain\\n    result: OOM at step 73, restarting as ft_002_v2\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 09:09 UTC\\n  summary: Gate 1 FAIL (RE rho_sj=0.244<0.30), 但 T=1.0 zero rate 44%>30% 触发协议内 T=0.7\\n    追加，暂不 pivot\\n  rationale: 1) RE full rho_sj=0.244 < 0.30 触发 ROADMAP FAIL 路径；2) 但 44.3% RE F1=0\\n    > 30% 阈值，按 Gate 1 设计追加 T=0.7 实验——这是协议预设步骤不是补救；3) RE cond rho_sj=0.316 > 0.30 说明排除\\n    all-zero 后进入 MARGINAL 区间，SJ 在\\\"可做\\\"实例上仍有信号；4) NER rho_sj=0.383 稳定正面；5) SJ vs FK\\n    翻转值得关注但可能与高 zero rate 有关，T=0.7 可能改善。最终 pivot 决策等 T=0.7 结果。\\n  related_experiments:\\n  - exp_id: mvp_pilot_004\\n    role: Gate 1 pilot (ft_002_v2)\\n    result: RE rho_sj=0.244 FAIL, NER rho_sj=0.383 PASS\\n  - exp_id: mvp_pilot_003\\n    role: Gate 1 pilot (ft_001) baseline\\n    result: RE rho_sj=0.237, NER rho_sj=0.381\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-14 09:25 UTC\\n  summary: E1 否定乘性惩罚假设，Narrative B 排除，确认走 Narrative A (NER-primary + RE diagnostic)\\n  rationale: E1 component-wise 分析：head_sj ρ=0.210 远低于 NER ρ=0.383（差 17pp），所有单组件 ρ\\n    都低于组合 SJ（0.244），加法/乘法聚合几乎相同（0.243 vs 0.244）。结论：RE consistency 信号本质弱于 NER，是复合错误传播的固有属性，不是\\n    metric 设计问题。Narrative B（度量分解修复 RE）不可行。Narrative A（NER 为主 + RE 诊断分析）是唯一可行路径。pilot_005\\n    (T=0.7) 作为最后确认仍在运行，设硬截止线：RE rho_sj < 0.30 = 确认 FAIL，不再调参。\\n  related_experiments:\\n  - exp_id: e1_component_wise_re_sj\\n    role: RE SJ 分解诊断\\n    result: 乘性惩罚假设 REJECTED，head_sj ρ=0.210 << NER 0.383\\n  - exp_id: mvp_pilot_004\\n    role: Gate 1 数据源\\n    result: RE rho_sj=0.244 FAIL\\n  - exp_id: mvp_pilot_005\\n    role: T=0.7 最后确认\\n    result: 运行中\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-14 09:25 UTC\\n  summary: E1 否定乘性惩罚假说，方案 B 排除，确认走方案 A（NER-primary + RE 诊断）\\n  rationale: E1 component-wise 分解显示 head_sj ρ=0.210 远低于 NER ρ=0.383，每个 component 单独都比乘性组合差——问题是\\n    span-level SJ 对 relation 任务根本缺乏区分力，不是聚合公式问题。additive fix 也无效（ρ差0.001）。方案 B（度量分解\\n    pivot）无法修复 RE。方案 A 可行：NER 强正向（ρ=0.383, SJ>FK 12pp, p=7e-20）作为 core claim + RE\\n    分解作为诊断贡献。下一步：NER 多数据集验证 + N=16 扩展。\\n  related_experiments:\\n  - exp_id: e1_component_wise_re_sj\\n    role: diagnostic\\n    result: 乘性惩罚假说 REJECTED, head_sj ρ=0.210 << NER ρ=0.383\\n  - exp_id: mvp_pilot_004\\n    role: Gate 1 base\\n    result: RE FAIL, NER PASS\\n  depends_on:\\n  - D007\\n- id: D010\\n  date: 2026-05-14 09:30 UTC\\n  summary: pilot_005 T=0.7 确认 RE full FAIL (rho=0.234<0.30)，但 RE cond rho_sj=0.372\\n    全系列最高，SJ>FK 11.8pp。MVP 结论：NER PASS + RE conditional positive + RE full FAIL。进入\\n    research 阶段走 Narrative A。\\n  rationale: 1) RE full rho_sj=0.234 < 0.30 硬截止线，确认 FAIL，不再调参；2) 但 RE conditional\\n    rho_sj=0.372（接近0.40），SJ>FK优势11.8pp——T=0.7自然分离knowledge-gap vs uncertainty两类错误，恰好支撑核心论点；3)\\n    T=1.0时FK反超SJ是采样噪声伪像（FK从0.278降到0.184），SJ在conditional set上实际增强；4) NER rho_sj=0.388全系列最高，SJ>FK稳健(p=2e-20)；5)\\n    MVP整体：假设部分验证——entity-level有效，relation-level需capability-aware分析。数据足够支撑Narrative\\n    A + 丰富的诊断分析。\\n  related_experiments:\\n  - exp_id: mvp_pilot_005\\n    role: T=0.7最后确认\\n    result: RE full rho=0.234 FAIL; RE cond rho=0.372 SJ>FK 11.8pp; NER rho=0.388\\n  - exp_id: mvp_pilot_004\\n    role: T=1.0 baseline\\n    result: RE full rho=0.244; RE cond rho=0.316\\n  - exp_id: e1_component_wise_re_sj\\n    role: 度量分解诊断\\n    result: 乘性假设REJECTED\\n  depends_on:\\n  - D008\\n- id: D011\\n  date: 2026-05-14 10:52 UTC\\n  summary: 'Dream 三档全 3/6 暴露结构性缺陷：缺强 baseline (log-prob/exact-match/entity-voting)\\n    是 #1 问题。大幅修订 framing + plan：加 4 个 baseline 实验 (exp-012~015)，扩评估指标，改 framing 为\\\"系统性比较\\n    4 类置信信号\\\"。需 re-dream 验证。'\\n  rationale: Dream dream_20260514T093336 三档（best/median/worst）全部 3/6 Weak Reject。跨档一致的结构性问题：(1)\\n    只对比 FK 一个弱 baseline，审稿人必问 log-prob/USC/exact-match；(2) novelty 薄——\\\"metric substitution\\\"\\n    without theoretical grounding；(3) 公式-实现不一致；(4) 评估指标单一(ρ only)；(5) 引用不足(10 refs)。最关键：如果\\n    SJ 不能胜过 log-prob（零额外推理成本），16x 推理成本不合理，论文实际贡献大幅缩水。修订方案：framing 从\\\"SJ vs FK\\\"升级为\\\"4\\n    类置信信号系统比较\\\"，加 exp-012~015 baseline 实验，全部 P0。exp-012 (log-prob) 是 make-or-break。\\n  related_experiments:\\n  - exp_id: dream_20260514T093336\\n    role: Dream simulation\\n    result: best 3/6, median 3/6, worst 3/6 — structural issues\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-14 11:12 UTC\\n  summary: 'exp-012 log-prob baseline: SJ 压倒性胜出 (NER Δρ=+0.217, 2.55x)。Make-or-break\\n    通过，论文走\\\"强贡献\\\"路线。统一后续数据源为 exp_012 格式（含全指标）。'\\n  rationale: 'NER full: SJ ρ=0.357 vs logprob 0.140 (2.55x); NER cond: SJ ρ=0.412\\n    vs logprob 0.163; RE cond: SJ 0.368 vs logprob 0.146. Log-prob AUROC=0.591 近乎随机。SJ\\n    捕获了模型置信度之外的结构信息，16x 推理成本合理。RE 上所有信号均退化，进一步证实 task-complexity boundary 跨信号家族适用。注意：exp_012\\n    重采样导致 SJ ρ=0.357 vs pilot 0.383（Δ=2.6pp），需统一数据源。max_tokens=512 vs pilot 1024 需修正。'\\n  related_experiments:\\n  - exp_id: exp_012_logprob_baseline\\n    role: make-or-break baseline comparison\\n    result: 'SJ >> logprob: NER Δρ=+0.217, AUROC 0.689 vs 0.591'\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-14 11:21 UTC\\n  summary: 'exp-013/014: voting confidence 与 SJ 持平(NER)/更优(RE)。Claim 1 从\\\"SJ 最优\\\"修改为\\\"structural\\n    consistency family (SJ+voting) >> log-prob/FK/EM\\\"。论文贡献从单 metric 升级为 signal family\\n    特征描述。'\\n  rationale: 'NER: voting_conf ρ=0.392 vs SJ 0.383 (Δ=0.9pp, 噪声级别); RE: voting_conf\\n    ρ=0.340 vs SJ 0.244 (Δ=9.6pp, 显著). 两者都远优于 log-prob (0.14) 和 FK (0.26). voting_conf\\n    本质是简化版 SJ——都捕获实体跨样本一致性。NER 上无差别说明信息高度重叠; RE 上 voting 更优可能因 relation tuple 稀疏时\\n    Jaccard 不稳定。论文 framing 更安全也更有洞察力：发现 structural consistency FAMILY 的优势，而非推销单一 metric。SJ\\n    的价值在泛化性（适用于任意结构化输出），voting 在 NER 上更简洁但不泛化。'\\n  related_experiments:\\n  - exp_id: exp_013_exact_match\\n    role: exact-match baseline\\n    result: NER ρ=0.294, RE ρ=0.156 — 偏弱如预期\\n  - exp_id: exp_014_entity_voting\\n    role: entity voting baseline\\n    result: voting_conf NER ρ=0.392 ≈ SJ; RE ρ=0.340 > SJ 0.244\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-14 11:53 UTC\\n  summary: 'Reviewer WARNING: pilot_004 vs exp_012 SJ ρ 不一致 (Δ=0.026-0.033)，根因是 exp_012\\n    重新采样而非复用 pilot_004 数据。exp-015 统一计算修复。'\\n  rationale: Reviewer 发现 exp_005 温度分析报告混用 pilot_004 的 ρ 和 exp_012 的 τ/AUROC，两者对同一任务的\\n    SJ ρ 差 0.026-0.033，与温度效应 Δρ=±0.01 同量级。根因已知：exp_012 生成了新样本而非复用 pilot_004。修复：exp-015\\n    从 pilot_004 原始样本统一计算所有指标（ρ/τ/AUROC/bootstrap CI/LOO-SJ），论文所有数字必须来自同一数据源。温度比较（T=1.0\\n    vs T=0.7）各自内部一致，核心结论（SJ 温度鲁棒）应该成立但需 bootstrap CI 验证。\\n  related_experiments:\\n  - exp_id: exp_005\\n    role: flagged\\n    result: 'WARNING: mixed data sources'\\n  - exp_id: exp_012_logprob_baseline\\n    role: root_cause\\n    result: used fresh samples instead of pilot_004\\n  - exp_id: exp_015_metrics_expansion\\n    role: fix\\n    result: unified computation from pilot_004\\n  depends_on:\\n  - D012\\n  - D013\\n- id: D015\\n  date: 2026-05-14 12:03 UTC\\n  summary: Dream 2 初步分析 + GPU 全面重新分配：exp_001 补跑全实例集，8 GPU 全排满\\n  rationale: Dream 2 best=4/6 (↑1), median=3/6 (持平). Baseline 添加解决了 dream 1 核心问题，但\\n    novelty 仍是最大障碍。median 新担忧：SJ vs logprob 可能 dataset-dependent——这是 data-dependent\\n    问题，等 exp-002/003 真实数据验证。Reviewer 发现 exp_001 只跑了 200/551 实例（严重），6/8 GPU 空闲。行动：(1)\\n    exp_001 在 cuda:0 重跑全实例集 (2) exp_003/007 在 cuda:2/3 启动 (3) gpu-5090-4x-2 分配给 exp_001\\n    seeds + exp_008 (4) 新增 exp-016 ensemble 分析 (P0 CPU) 和 exp-017 LLaMA-CoNLL (P1)。Dream\\n    2 新增 reviewer concerns R11-R14 已更新到 paper_framing.md。\\n  related_experiments:\\n  - exp_id: exp_001_ner_n16_scierc\\n    role: 需补跑全实例集\\n    result: 200/551 实例完成, NER voting_conf ρ=0.401, RE voting_conf ρ=0.448\\n  - exp_id: exp_004_re_diagnostic\\n    role: RE diagnostic 完成\\n    result: SJ>FK NER 显著, Fisher z NER>RE p=0.021, entity span errors=55.5% FN\\n  - exp_id: dream_20260514T105303\\n    role: re-dream 审稿\\n    result: best 4/6, median 3/6, worst pending\\n  depends_on:\\n  - D013\\n  - D011\\n- id: D016\\n  date: 2026-05-14 12:13 UTC\\n  summary: 'Dream 2 跨三档分析完成 (best=3/6, median=3/6, worst=3/6): 问题全为结构性，非数据依赖'\\n  rationale: '三档评分全部 3/6 (Weak Reject)，说明即使 best-case 数据也无法突破当前 framing/presentation\\n    限制。跨档分析提取 19 个 distinct issue，分类如下：\\n\\n\\n    **确认行动项（三档一致，通用）：**\\n\\n    1. I1: 相关工作严重不足 [B][M][W] → 35+ refs，补 conformal prediction / token-level NER\\n    / ensemble / verifier 文献。Paper Agent P0。\\n\\n    2. I2: 单 RE 数据集限制 Claim 2 [B][M][W] → 承认 limitation，N-scaling 发现部分缓解。\\n\\n    3. I3: 缺 SJ+logprob ensemble [B][M][W] → exp-016 已在跑（CPU）。\\n\\n    4. I4: 新颖性增量 [B][M][W] → 不改架构，通过 ensemble 实验+diagnostic analysis+practical guidelines\\n    补强。\\n\\n\\n    **新增 paper_framing.md 条目：** R15 (log-prob 定义歧义), R16 (零图表), R17 (diagnostic framework\\n    过度声称→改为 analysis), R18 (何时 consistency 有用), R19 (负面结果可预测性辩护)。R10 更新具体缺失文献清单。\\n\\n\\n    **观察项（两档一致，数据依赖）：**\\n\\n    - I5: SJ vs logprob dataset-dependent [B][M] → exp-002/003 决定\\n\\n    - I6: Best-of-N F1 差异不显著 [B][M] → exp-016 bootstrap CI 验证\\n\\n\\n    **忽略项：** best tier 的 data integrity concern（dream artifact），narrative repositioning\\n    concern（dream 对内部决策日志的过度解读）。\\n\\n\\n    **Claim 2 决策：** 批准从\\\"task-complexity boundary\\\"升级为\\\"sample-complexity gradient\\\"，但需全实例集\\n    T=1.0 确认后才正式写入。\\n\\n\\n    **不 re-dream：** 所有确认行动项均为 paper writing 级别（Paper Agent 处理），非 framing 结构性改变。P0\\n    实验已全部审批并运行，等真实数据后再评估是否 re-dream。'\\n  related_experiments:\\n  - exp_id: dream_20260514T105303\\n    role: dream\\n    result: best=3/6, median=3/6, worst=3/6 — 全结构性问题\\n  - exp_id: exp_016\\n    role: addresses I3 (ensemble)\\n    result: running\\n  - exp_id: exp_002\\n    role: validates I5 (dataset dependency)\\n    result: running\\n  - exp_id: exp_003\\n    role: validates I5 (dataset dependency)\\n    result: running\\n  depends_on:\\n  - D015\\n- id: D017\\n  date: 2026-05-14 12:14 UTC\\n  summary: Dream 2 全三档 3/6 (Weak Reject) — 问题是结构性的(presentation/positioning)，非数据问题。确认行动项：reframe\\n    novelty + 扩展 related work 35+ refs + 添加 3+ figures + soften diagnostic framework\\n    claim。观察项：SJ vs LOGPROB dataset-dependency (等 exp-002/003)、Best-of-N significance\\n    (等 exp-006/015)、cross-model stability (等 exp-007)。已运行 GPU 实验继续（数据收集独立于 framing）。framing\\n    修改完成后 re-dream 验证。\\n  rationale: 'Dream 2 三档一致问题: (D01) novelty = metric substitution, (D02) related work\\n    thin, (D03) single RE dataset。两档一致: ensemble missing (exp-016 已规划), diagnostic\\n    framework overclaimed, negative result predictability。Best case 都无法达到 4/6 说明 framing\\n    + positioning 是 bottleneck, 不是 experimental evidence。Paper Agent 是 critical path\\n    — related work 扩展、figures 添加、contribution reframe 比新 GPU 实验更紧急。但 GPU 实验(esp exp-002/003\\n    cross-dataset validation)的结果将决定 Claim 1 的最终强度。'\\n  related_experiments:\\n  - exp_id: exp-016\\n    role: planned_mitigation\\n    result: addresses D04 (ensemble missing) — P0, CPU-only\\n  - exp_id: exp-002\\n    role: observation_target\\n    result: will determine if SJ vs LOGPROB is dataset-dependent (D05)\\n  - exp_id: exp-003\\n    role: observation_target\\n    result: will determine if SJ vs LOGPROB is dataset-dependent (D05)\\n  - exp_id: exp-007\\n    role: observation_target\\n    result: will determine cross-model stability (D20)\\n  - exp_id: exp-015\\n    role: planned_mitigation\\n    result: addresses D12 (bootstrap CIs) — already planned\\n  depends_on:\\n  - D015\\n- id: D018\\n  date: 2026-05-14 12:27 UTC\\n  summary: 'exp-016 揭示 correlation-selection gap: 结构一致性信号 instance-level ρ~0.43 但\\n    best-of-N 选择全部不如 greedy (NER)。Paper framing 必须从 \\\"TTS improvement\\\" 转向 \\\"confidence\\n    signal analysis\\\"，核心贡献升级为发现 quality estimation ≠ sample selection。'\\n  rationale: 'exp-016 best-of-N 选择结果：NER 所有信号均不如 greedy (best: logprob 0.6087 vs greedy\\n    0.6094)；RE 仅 logprob (+2.4pp) 超过 greedy，结构信号均失败。Oracle headroom 巨大 (NER +16pp)\\n    但不可达。\\n\\n\\n    根因分析：SJ/voting_conf 是 instance-level aggregate (一个 instance 一个分数)，无法对 instance\\n    内的 N 个 sample 排序；logprob 是天然 per-sample 信号但 NER 上 greedy 已接近最优，采样只增加噪声。RE 上模型不确定性更大，部分\\n    sample 优于 greedy，logprob 可以发现它们。\\n\\n\\n    这改变了论文的核心叙事：\\n\\n    - 旧 framing: \\\"SJ 是 TTS 最佳信号 → 用更多 compute 换更高质量\\\"\\n\\n    - 新 framing: \\\"结构一致性是最强的质量估计信号 (instance-level)，但 quality estimation ≠ sample selection\\n    → correlation-selection gap 是 structured IE TTS 的根本挑战\\\"\\n\\n\\n    correlation-selection gap 是 genuinely novel finding，比原来的 \\\"SJ vs logprob ranking\\\"\\n    更有概念贡献，可能正好解决 Dream 审稿反复提的 novelty 不足问题。'\\n  related_experiments:\\n  - exp_id: exp_016_signal_ensemble\\n    role: primary_evidence\\n    result: 'NER best-of-N: all signals < greedy; RE: only logprob +2.4pp > greedy;\\n      ensemble AUROC +3.5pp NER, -0.2pp RE; data leakage in Part 4'\\n  - exp_id: exp_012_logprob_baseline\\n    role: context\\n    result: instance-level SJ >> logprob (ρ 0.383 vs 0.140)\\n  - exp_id: exp_014_entity_voting\\n    role: context\\n    result: voting_conf instance-level ρ=0.392, AUROC=0.704 — strong estimation but\\n      cannot select\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-14 12:27 UTC\\n  summary: '论文叙事关键转向: 从 \\\"TTS improvement via structural consistency\\\" 转向 \\\"confidence\\n    estimation for structured IE + correlation-selection gap analysis\\\"。exp-016 证明\\n    best-of-N selection 在 NER 上全部不如 greedy，RE 仅 logprob 胜出。instance-level correlation\\n    ≠ per-sample selection 是核心新发现。'\\n  rationale: 'exp-016 数据不可回避:\\n\\n    1. NER best-of-N: greedy 0.6094 > 所有信号（logprob 0.6087, sj 0.6042, voting 0.5959）。Oracle\\n    headroom +16pp 但无信号可利用。\\n\\n    2. RE best-of-N: 仅 logprob 0.3971 > greedy 0.3735，结构信号全部不如 greedy。\\n\\n    3. Instance-level AUROC: voting_conf 0.700, SJ 0.689 >> logprob 0.591 → quality\\n    estimation 仍然有效。\\n\\n    4. Ensemble: NER AUROC +3.5pp（微弱），RE -0.2pp（无提升）。\\n\\n\\n    结论: 结构一致性信号擅长\\\"预测哪些实例做得好\\\"(quality estimation)，但不能\\\"从 N 个 sample 中选出最好的\\\"(selection)。paper_framing.md\\n    的 Story Spine 预设 best-of-N 正面结果，现在不成立。必须 pivot。\\n\\n\\n    Reviewer 独立审查确认: (1) C1-B 降 P2 (2) C3-B TACRED 不可行降 P3 (3) R4 mitigation 失效 (4)\\n    叙事一致性是最大风险。\\n\\n\\n    新叙事方向: confidence estimation + correlation-selection gap as novel finding + task-complexity\\n    boundary。所有现有实验数据仍有效，pivot 不需要重新跑实验。'\\n  related_experiments:\\n  - exp_id: exp-016\\n    role: trigger\\n    result: best-of-N selection 全部不如 greedy (NER); RE 仅 logprob 胜出; instance-level\\n      AUROC 仍有效\\n  - exp_id: exp-006\\n    role: invalidated\\n    result: adaptive compute demo 的 best-of-N framing 需要重新设计\\n  - exp_id: exp-012\\n    role: supporting\\n    result: logprob ρ=0.140 vs SJ 0.383 — instance-level 差距大但 selection 差距小/反转\\n  - exp_id: exp-014\\n    role: supporting\\n    result: voting_conf AUROC 0.704 — quality estimation 仍是最强信号\\n  depends_on:\\n  - D017\\n- id: D020\\n  date: 2026-05-14 12:45 UTC\\n  summary: 'exp-002 CoNLL: EM > SJ (Δρ=-0.015, significant) — signal ranking is task-difficulty-dependent.\\n    SJ >> logprob confirmed cross-dataset (Δρ=+0.120). Voting first to beat greedy\\n    (+0.18pp). Framing: optimal signal depends on task difficulty, not universal winner.'\\n  rationale: 'CoNLL (easy task, greedy F1=91.2%): EM ρ=0.451 (#1) > SJ 0.436 (#2)\\n    > voting 0.424 (#3). SciERC (hard task, F1=67%): voting 0.392 (#1) > SJ 0.383\\n    (#2) > EM 0.294 (#4). EM jumps from #4 to #1 across difficulty levels.\\n\\n\\n    根因: 简单任务上 sample 输出高度一致, exact match 足以捕获一致性, SJ 的 soft matching 无额外价值。困难任务上 sample\\n    间差异大, 需要结构化匹配 (SJ) 来识别有意义的一致性。\\n\\n\\n    对叙事的影响:\\n\\n    - Claim 1 从 \\\"SJ universally best\\\" 改为 \\\"optimal signal is task-difficulty-dependent:\\n    SJ for hard tasks, EM for easy tasks\\\"\\n\\n    - 这实际上 EXTENDS Claim 3 (task-complexity boundary): 不仅 NER↔RE 有 boundary, NER 内部不同难度也有\\n    boundary\\n\\n    - 增加了论文概念深度: signal utility = f(task difficulty)\\n\\n\\n    关键确认:\\n\\n    - SJ >> logprob 跨数据集稳健 (SciERC Δρ=+0.217, CoNLL Δρ=+0.120, both significant)\\n\\n    - Voting 首次 beat greedy (CoNLL +0.18pp) → correlation-selection gap 也是 task-difficulty-dependent\\n\\n    - All signals AUROC > 0.75 on CoNLL → easy tasks 上信号选择 ROI 低\\n\\n\\n    ⚠️ AUROC bug: pilot script logprob AUROC=0.5000 (F1=1.0 二值化问题), 需修复以免 WNUT 复现。'\\n  related_experiments:\\n  - exp_id: exp_002_ner_conll2003\\n    role: primary_evidence\\n    result: EM ρ=0.451 > SJ 0.436 > voting 0.424 > FK 0.400 > logprob 0.316. SJ vs\\n      logprob Δρ=+0.120 significant. Voting beats greedy +0.18pp.\\n  - exp_id: exp_016_signal_ensemble\\n    role: context\\n    result: 'SciERC: no signal beats greedy. CoNLL: voting beats greedy → correlation-selection\\n      gap is task-difficulty-dependent.'\\n  - exp_id: exp_012_logprob_baseline\\n    role: context\\n    result: SciERC SJ >> logprob confirmed. CoNLL adds cross-dataset validation.\\n  depends_on:\\n  - D018\\n- id: D021\\n  date: 2026-05-14 12:50 UTC\\n  summary: 'exp-002 CoNLL SUCCESS: Claim 1 跨数据集验证通过，SJ vs logprob Δρ=+0.12 bootstrap显著，信号排序与SciERC一致'\\n  rationale: 'CoNLL-2003 NER (N=8, T=1.0): SJ ρ=0.436 vs logprob ρ=0.316, Δρ=+0.12,\\n    95% CI [+0.088, +0.154]。所有结构信号 > logprob，排序与 SciERC 一致。EM 在 CoNLL 略胜 SJ (+0.015)，表明高准确率场景下\\n    EM 更有效，但 SJ 泛化性更强——论文应讨论此 tradeoff。CoNLL 整体 ρ 值更高（SJ 0.436 vs SciERC 0.398），支持\\n    Claim 2 的 task-complexity 叙事：简单任务信号更强。FK 涨幅最大 (+0.112)，表面匹配在高 F1 regime 更有效。Claim\\n    1 现在有 2/3 数据集验证，等 exp-003 WNUT 完成后达到 3 个。'\\n  related_experiments:\\n  - exp_id: exp_002_ner_conll2003\\n    role: primary\\n    result: success\\n  - exp_id: exp_003_ner_wnut17\\n    role: next\\n    result: running\\n  depends_on:\\n  - D020\\n- id: D022\\n  date: 2026-05-14 13:24 UTC\\n  summary: 'D021: 激活 Paper Agent Full Draft + GPU 全面恢复指令。Paper Agent 启动条件满足（P0 完成度\\n    75%, 3 claims 各 ≥2 settings 支撑）。GPU 空闲 28 分钟不可接受，发综合指令要求立即排满 8 卡。'\\n  rationale: Dream 2 全三档 3/6 瓶颈是 presentation 不是实验数据。11 天 DDL，Paper Agent 是关键路径——越早启动越好。GPU\\n    利用率 0/8 是硬伤，必须立即修复。exp-001 seed123 和 exp-007 LLaMA 两个失败需要诊断修复。Conditional filtering\\n    修复完成可以 unblock T=1.0 全集重跑。\\n  related_experiments:\\n  - exp_id: exp-002\\n    role: trigger\\n    result: CoNLL 成功，Paper Agent 激活条件满足\\n  - exp_id: exp-016\\n    role: trigger\\n    result: ensemble 分析完成，correlation-selection gap 确认\\n  - exp_id: exp-001\\n    role: blocked\\n    result: seed123 失败待诊断\\n  - exp_id: exp-007\\n    role: blocked\\n    result: LLaMA NER 失败待诊断\\n  depends_on:\\n  - D020\\n  - D019\\n  - D017\\n- id: D023\\n  date: 2026-05-14 13:30 UTC\\n  summary: RE task SJ vs FK 排序在 joint 模式和 RE-only 模式之间反转，论文必须明确标注 evaluation protocol\\n  rationale: Reviewer 发现：Joint 模式 seed123 RE SJ ρ=0.267 < FK ρ=0.315（FK wins），RE-only\\n    模式 seed42 RE SJ ρ=0.304 > FK ρ=0.269（SJ wins）。可能原因：(1) joint 模式下 NER 错误传播到 RE，(2)\\n    seed 效应。论文若 claim SJ 在 RE 上优于 FK，必须区分 joint vs RE-only protocol，否则审稿人可攻击。后续需要：同\\n    seed 下对比 joint vs RE-only 以隔离变量。\\n  related_experiments:\\n  - exp_id: exp_001_ner_n16_seed123\\n    role: evidence\\n    result: 'joint模式 RE: SJ ρ=0.267 < FK ρ=0.315'\\n  - exp_id: exp_008_re_n16_full\\n    role: evidence\\n    result: 'RE-only模式: SJ ρ=0.304 > FK ρ=0.269'\\n  depends_on: []\\n- id: D024\\n  date: 2026-05-14 13:38 UTC\\n  summary: RE full set 上 SJ 不优于 FK（2/3 seeds FK > SJ），论文 claim 必须按评估 regime 分层\\n  rationale: Reviewer 独立核实 3 seeds N=16 T=1.0 全集结果：RE full set SJ rho 均值 ~0.26 vs\\n    FK ~0.29（FK 在 seed123/42 上反超）。但 conditional set（排除 F1=0 ~44% 样本后）SJ 恢复优势（mean\\n    rho_sj ~0.32 vs rho_fk ~0.14）。logprob 在 conditional set 近乎零（-0.03~0.02）。论文叙事调整为：(1)\\n    NER：SJ 稳健优于 FK/logprob；(2) RE full set：所有信号弱且差异不显著，根因是 ~44% zero-F1 实例；(3) RE\\n    conditional：SJ 恢复优势且 logprob 失效 → structural signals 在排除 knowledge-gap 后仍有价值。这比\\n    \\\"SJ always wins\\\" 更诚实，且 conditional 分析是独特贡献。\\n  related_experiments:\\n  - exp_id: exp_001_seed456_t10_full\\n    role: evidence\\n    result: 'RE full: SJ 0.268 vs FK 0.260 (marginal)'\\n  - exp_id: exp_001_seed123_t10_full\\n    role: evidence\\n    result: 'RE full: SJ 0.265 vs FK 0.315 (FK wins)'\\n  - exp_id: exp_008_re_n16_t10_full\\n    role: evidence\\n    result: 'RE-only: SJ 0.304 > FK 0.269'\\n  depends_on:\\n  - D023\\n- id: D025\\n  date: 2026-05-14 13:44 UTC\\n  summary: WNUT17 SJ rho=0.082 近乎失效，暂停纳入 Claim 1 泛化证据，待诊断数据质量后决定论文定位\\n  rationale: 'WNUT17 pilot: rho_sj=0.082, logprob=-0.414, greedy_f1=0.525, 53.7% zero-rate。三种可能：(1)\\n    数据格式 bug（gold_empty 46.5% 异常高需验证）；(2) 模型能力不足导致 SJ 无信号（高一致性+低准确 = 一致地错）；(3) SJ\\n    方法在社交媒体噪声文本上的真实边界。诊断前不做 framing 决定。如果是 (2)/(3)，WNUT17 可正面利用为 Claim 3 补充——一致性 ≠\\n    正确性是方法的重要边界条件。如果是 (1)，修复后重跑。'\\n  related_experiments:\\n  - exp_id: exp_003_ner_wnut17\\n    role: evidence\\n    result: rho_sj=0.082, logprob=-0.414, greedy_f1=0.525\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 13:44 UTC\\n  summary: WNUT-17 SJ 近乎失效(ρ=0.082)，需先诊断数据质量再决定论文定位\\n  rationale: WNUT17 greedy_f1=0.525, 53.7% zero-F1, SJ rho=0.082, logprob rho=-0.414。两种可能：(1)\\n    数据格式/评估 bug → 修复后重跑；(2) 模型能力不足的真实边界条件（SJ_mean=0.882 说明一致但错误）。如果是 (2)，可作为 Claim\\n    3 (task-complexity boundary) 的延伸——不仅任务难度，模型能力不足也会使信号退化。conditional set SJ 恢复到\\n    0.275 > FK 0.164 支持此叙事。已派 Agent 诊断，结果决定最终 framing。\\n  related_experiments:\\n  - exp_id: exp_003_ner_wnut17\\n    role: evidence\\n    result: SJ rho=0.082, logprob rho=-0.414, greedy_f1=0.525, 53.7% zero-F1\\n  depends_on:\\n  - D024\\n- id: D027\\n  date: 2026-05-14 14:15 UTC\\n  summary: 'exp-007 LLaMA cross-model PASS: SJ model-agnostic claim 成立。RE cond SJ=0.405\\n    首破 0.40。补算 voting_conf/EM (CPU)，N=16 重跑列为 P1'\\n  rationale: Reviewer PASS。LLaMA NER rho_sj=0.363 vs Qwen 0.383，信号排序完全一致 (SJ>FK>logprob)。RE\\n    conditional SJ=0.405 是全项目首次破 0.40，且 logprob RE_cond 在 LLaMA 上不显著(p=0.143)，强化 SJ>>logprob\\n    on RE 的 claim。两个 warning 处理：(1) voting_conf/EM 从 samples.jsonl 补算，零 GPU 成本，必做；(2)\\n    N=16 重跑列为 P1——当前 N=8 足够支撑定性 cross-model claim，论文表格注明 N 差异即可，有 GPU 余量再补 N=16。\\n  related_experiments:\\n  - exp_id: exp_007_llama_inference\\n    role: primary\\n    result: LLaMA NER rho_sj=0.363, RE rho_sj=0.299, RE_cond_sj=0.405\\n  depends_on:\\n  - D022\\n- id: D028\\n  date: 2026-05-14 14:18 UTC\\n  summary: WNUT-17 P0 修复批准：下采样空实例 ≤25% 重训+重推理。无论结果如何都对论文 story 有利（task-difficulty-dependent\\n    证据或跨域泛化证据）\\n  rationale: 'Reviewer 确认根因：训练集 63.8% 空实例 vs SciERC 0%，导致模型过强空输出先验，SJ/logprob 信号失效。修复成本仅\\n    ~3h GPU，当前 7/8 GPU 空闲，成本微不足道。修复后两种结果均有价值：(1) SJ 恢复 > logprob → 跨域泛化证据；(2) SJ 仍\\n    < logprob → task-difficulty-dependent signal ranking 的第三个数据点（CoNLL: EM>SJ, SciERC:\\n    SJ>>logprob, WNUT: logprob≥SJ），与 D020 narrative 完美互补。空实例率对 consistency 信号的影响机制本身也是论文值得讨论的分析洞察。'\\n  related_experiments:\\n  - exp_id: exp_003_ner_wnut17\\n    role: primary\\n    result: 'SJ rho=0.082 (full), 0.275-0.288 (conditional); root cause: 63.8% empty\\n      training instances'\\n  depends_on:\\n  - D025\\n  - D026\\n  - D020\\n- id: D029\\n  date: 2026-05-14 14:26 UTC\\n  summary: WNUT-17 降级 P2，转为 negative case study（方法边界分析）。D028 重训仍保留但仅在 P0 实验全部排满后有余力时执行\\n  rationale: Reviewer 独立验证确认：WNUT-17 训练数据 63.8% 空实例是 SJ 失效根因（vs SciERC 0%）。CoNLL-2003\\n    已提供跨数据集验证（exp-002 success），LLaMA 提供跨模型验证（exp-007 pass）。DDL 11 天，WNUT-17 重训 ROI\\n    不确定——即使重训后 SJ 可能仍弱（社交媒体实体歧义大）。更好的论文定位：WNUT-17 作为 method boundary analysis——\\\"当训练数据空实例比例过高时，模型习得过强空输出先验，所有置信信号均退化\\\"。这比忽略结果更诚实，也是\\n    framing 升级（展示方法适用边界 = 学术严谨性）。\\n  related_experiments:\\n  - exp_id: exp_003_ner_wnut17\\n    role: trigger\\n    result: SJ rho=0.082 near failure\\n  - exp_id: exp_002_ner_conll2003\\n    role: alternative evidence\\n    result: success, cross-dataset validated\\n  depends_on:\\n  - D028\\n  - D025\\n  - D026\\n- id: D030\\n  date: 2026-05-14 14:29 UTC\\n  summary: LLaMA cross-model SJ 确认完成。NER SJ>logprob 跨模型成立。LLaMA N=16 不补跑（N=8 足够支撑\\n    model-agnostic claim）\\n  rationale: 'LLaMA-3.1-8B N=8: NER ρ_sj=0.363 vs ρ_logprob=0.183，SJ>logprob 优势比 Qwen\\n    上更大。两个模型架构 SJ ranking 一致，足够支撑 model-agnostic claim。N=8 vs N=16 不影响 signal ranking\\n    结论（cross-model 验证的目标是 ranking 一致性不是绝对值）。DDL 11 天，GPU 时间优先给 exp-001 seed robustness\\n    和 exp-008 RE N=16。'\\n  related_experiments:\\n  - exp_id: exp_007_llama_inference\\n    role: primary\\n    result: NER ρ_sj=0.363(LLaMA) vs 0.398(Qwen), ρ_logprob=0.183 vs 0.237. Cross-model\\n      SJ>logprob confirmed.\\n  depends_on:\\n  - D027\\n- id: D031\\n  date: 2026-05-14 14:30 UTC\\n  summary: 批准 WNUT-17 P0 修复：下采样空实例到≤25%重训，8 GPU 全分配铺开 P0 实验\\n  rationale: WNUT-17 训练数据 63.8% 空实例导致模型对空输出过度自信（logprob≈-0.007），full 集 SJ ρ=0.082。方法在非空预测上有效（conditional\\n    ρ=0.288）。P0 修复成本低（~3h），预期显著提升 full 集指标。同时 8 GPU 全部分配：WNUT 重训(1)+NER N=16 三种子(3)+LLaMA\\n    fine-tune(2)+logprob baseline(1)+RE N=16(1)，CPU 并行跑 exact-match 和 entity voting\\n    baseline。DDL 11 天，不允许空卡。\\n  related_experiments:\\n  - exp_id: exp-003\\n    role: target\\n    result: P0 retrain approved\\n  - exp_id: exp-001\\n    role: parallel\\n    result: 3 seeds queued\\n  - exp_id: exp-007\\n    role: parallel\\n    result: pending status confirmation\\n  - exp_id: exp-012\\n    role: parallel\\n    result: logprob baseline queued\\n  - exp_id: exp-008\\n    role: parallel\\n    result: RE N=16 queued\\n  depends_on: []\\n- id: D032\\n  date: 2026-05-14 14:33 UTC\\n  summary: 收尾阶段：批准 exp-017 LLaMA CoNLL (2 GPU)，WNUT-17 重训跳过（D029 boundary framing\\n    成立）\\n  rationale: P0 实验全部完成。exp-017 补上 cross-model×cross-dataset 2×2 矩阵最后一格（LLaMA 目前只在\\n    SciERC 验证），10 GPU-hours 成本低、对 model-agnostic claim 收益高。WNUT-17 重训跳过：D029 已将其定位为\\n    method boundary analysis，Paper Agent 已纳入论文 framing（空实例占比过高时所有信号退化），重训边际收益低于论文写作聚焦。剩余\\n    2 GPU 保留给 AUROC bugfix rerun 和 Paper Agent 数据需求。\\n  related_experiments:\\n  - exp_id: exp-017\\n    role: approved\\n    result: LLaMA CoNLL fine-tune + inference\\n  - exp_id: exp-003\\n    role: skipped\\n    result: D029 boundary case study framing stands\\n  depends_on:\\n  - D029\\n  - D031\\n- id: D033\\n  date: 2026-05-14 14:51 UTC\\n  summary: 新颖性自查通过：核心 idea 在 2024-2026 文献中无直接竞争者，需补引 4 篇 2025-2026 必引文献\\n  rationale: Manager 要求做新颖性自查。搜索 Semantic Scholar/arXiv/ACL Anthology 8 个维度，确认：(1)\\n    无论文同时做 structured IE 多信号对比 + set-aware consistency + correlation-selection gap；(2)\\n    最接近的 CISC(ACL'25)、Self-Certainty(ICLR'26)、ReASC(2026) 均限于 reasoning 离散答案，不处理 set-structured\\n    IE；(3) related work 需补 CISC、Self-Certainty、ReASC、Atomic SC 等 2025-2026 文献，并新增\\n    TTS & Sample Selection 小节。已更新 paper_framing.md R10。\\n  related_experiments: []\\n  depends_on: []\\n- id: D034\\n  date: 2026-05-14 14:56 UTC\\n  summary: 新颖性自查（第二轮）：发现直接竞争者 Nédellec 2026，核心新颖性仍成立，需补引 3 篇\\n  rationale: 'Manager 要求深度新颖性自查。搜索 Semantic Scholar + Web 发现最直接竞争者 Nédellec & Xia\\n    (Genomics Informatics, 2026-02): consistency-accuracy correlation for NER/RE with\\n    4 LLMs。但他们只用 surface-level string matching、不研究 best-of-N selection、单领域 hard-prompted。我们的\\n    SJ structural metrics + 5 信号家族系统比较 + correlation-selection gap 均为差异化贡献。同时发现 CoCoA\\n    (NeurIPS 2025) 和 Vashurin 2025 系统评估需补引。已更新 paper_framing.md R10 新增 3 篇文献 + 新增\\n    \\\"Consistency for Structured IE\\\" related work 小节要求。'\\n  related_experiments: []\\n  depends_on:\\n  - D033\\n- id: D035\\n  date: 2026-05-14 15:04 UTC\\n  summary: Heatmap数据源统一：采用方案A，全部用exp_015统一评估数据。Voting显著领先SJ（NER ρ 0.502 vs 0.357），调整叙事为\\\"structural\\n    consistency family\\\"内互补定位\\n  rationale: 审计发现heatmap混用3个独立推理run（pilot_004 SJ/FK/voting/EM + exp_012 logprob +\\n    可能pilot_005 RE cond），同instance entity集合不同。方案A用exp_015统一5信号在同一推理run上的评估，数据诚信度最高。叙事调整：voting是NER最强单信号（ρ=0.502），SJ的独特价值重新定位为(a)温度鲁棒Δρ≤0.01\\n    (b)泛化到任意structured output (c)conditional filtering下ρ=0.412仍强 (d)与voting ensemble互补（exp-016\\n    AUROC 0.735）。\\\"Structural consistency family\\\"（SJ+voting）仍为最强家族，内部分工更清晰。\\n  related_experiments:\\n  - exp_id: exp_015\\n    role: 统一评估数据源\\n    result: voting ρ=0.502 >> SJ 0.357 NER full\\n  - exp_id: exp_016\\n    role: ensemble验证\\n    result: SJ+voting ensemble AUROC 0.735\\n  depends_on:\\n  - D019\\n- id: D036\\n  date: 2026-05-14 15:04 UTC\\n  summary: Heatmap 数据源：采用方案 D（v2 统一推理数据替换），exp_015 数据源不可信\\n  rationale: Reviewer critical 发现 exp_015 数据源三重不一致（registry 说 pilot_004、代码注释说 pilot_005\\n    T=0.7、实际指向 exp_012）。exp_015 不能作为 ground truth。方案 A 排除。方案 D：用正在运行的 v2 实验（exp-001v2\\n    seed42 N=16，含全部 5 信号同源推理）替换 SciERC heatmap 数据。优势：(1) 同一 inference run 天然无混源; (2)\\n    N=16 统计功效更高; (3) 不额外占 GPU。N=16 vs CoNLL N=8 在图中注明即可。若 v2 失败则 fallback 到方案 C（1\\n    GPU-hour 统一 N=8 重新推理）。\\n  related_experiments:\\n  - exp_id: exp_015\\n    role: 问题源\\n    result: 数据源三重不一致，不可信\\n  - exp_id: exp_001_seed42_v2\\n    role: 替代数据源\\n    result: RUNNING, N=16 全信号同源\\n  depends_on:\\n  - D014\\n- id: D037\\n  date: 2026-05-14 15:09 UTC\\n  summary: N=16 结果确认：NER SJ scaling 成立(+0.071)，RE full SJ≈logprob(0.281 vs 0.287)但RE\\n    cond logprob 崩溃(-0.026)。叙事需任务分化\\n  rationale: exp-001v2 (seed42/123) + exp-008v2 (RE N=16) 三实验完成。NER seed鲁棒性极佳(SJ Δ<0.01)。N=16\\n    NER SJ从0.357→0.428(+0.071)，支持scaling叙事。但RE full上logprob 0.287反超SJ 0.281，不能笼统声称\\\"结构信号全面领先\\\"。RE\\n    cond上logprob完全失效(ρ=-0.026, p=0.685)而SJ仍有0.308——支持Claim 3的conditional filtering价值。叙事调整：NER全面领先\\n    + RE full持平 + RE cond结构信号独特价值。v2缺voting_conf和EM，需零GPU后处理补全。\\n  related_experiments:\\n  - exp_id: exp_001_seed42_v2\\n    role: NER N=16 seed robustness\\n    result: SJ full ρ=0.428, cross-seed Δ<0.01\\n  - exp_id: exp_001_seed123_v2\\n    role: NER N=16 seed robustness\\n    result: SJ full ρ=0.424\\n  - exp_id: exp_008_re_n16_v2\\n    role: RE N=16 validation\\n    result: SJ full ρ=0.281 ≈ logprob 0.287, SJ cond 0.308 vs logprob -0.026\\n  depends_on:\\n  - D035\\n  - D024\\n- id: D038\\n  date: 2026-05-14 15:21 UTC\\n  summary: NER seed 鲁棒性确认；RE subtask 结构一致性信号系统性偏弱\\n  rationale: exp_001 三个 seed (42/123/456 v2) NER SJ ρ 高度一致 (0.428/0.424)，结构信号稳定优于表面信号\\n    (+0.147/0.149)，cross-seed robustness 确认。RE 方面，exp_008 所有变体 (v2/seed123) + exp_007\\n    LLaMA (seed123/456) 全部 FAIL：full set SJ ρ 均 <0.30，F1=0 比例 >40%。RE 的 conditional\\n    set 有信号 (SJ ρ 0.29-0.40)，但 full set 一致性信号弱是系统性问题，非随机波动。论文 framing 应将 RE 定位为 honest\\n    negative finding + conditional analysis 的 nuanced story。\\n  related_experiments:\\n  - exp_id: exp_001_seed42_v2\\n    role: evidence\\n    result: success\\n  - exp_id: exp_001_seed123_v2\\n    role: evidence\\n    result: success\\n  - exp_id: exp_008_re_n16_v2\\n    role: evidence\\n    result: negative\\n  - exp_id: exp_007_llama_seed123\\n    role: evidence\\n    result: negative\\n  - exp_id: exp_007_llama_seed456\\n    role: evidence\\n    result: negative\\n  - exp_id: exp_008_re_seed123\\n    role: evidence\\n    result: negative\\n  depends_on: []\\n- id: D039\\n  date: 2026-05-14 15:22 UTC\\n  summary: NER seed robustness confirmed; RE structural signal systemically weak\\n  rationale: 'Seed experiments (42, 123, 456) show NER SJ ρ highly consistent (0.424-0.428),\\n    structural > surface advantage stable (+0.147-0.149). RE experiments (v2, seed123)\\n    all FAIL: SJ ρ_full 0.281-0.296, F1=0 rate >40%. RE weakness is systematic, not\\n    seed-dependent. LLaMA cross-model: NER signal present (SJ ρ=0.287-0.366), RE fails\\n    joint threshold. Paper framing should present RE as honest negative finding with\\n    conditional-set salvage (SJ ρ_cond 0.29-0.40).'\\n  related_experiments:\\n  - exp_id: exp_001_seed42_v2\\n    role: NER seed robustness\\n    result: success, SJ ρ=0.428\\n  - exp_id: exp_001_seed123_v2\\n    role: NER seed robustness\\n    result: success, SJ ρ=0.424\\n  - exp_id: exp_008_re_n16_v2\\n    role: RE confirmation\\n    result: negative, SJ ρ=0.281\\n  - exp_id: exp_008_re_seed123\\n    role: RE seed check\\n    result: negative, SJ ρ=0.284\\n  - exp_id: exp_007_llama_seed123\\n    role: cross-model seed\\n    result: negative (RE), NER SJ ρ=0.287\\n  - exp_id: exp_007_llama_seed456\\n    role: cross-model seed\\n    result: negative (RE), NER SJ ρ=0.287\\n  depends_on: []\\n- id: D040\\n  date: 2026-05-14 15:31 UTC\\n  summary: Registry 修复 + 3 GPU 全量调度：WNUT-17(cuda:1) + seed456(cuda:2) + CPU 分析批次\\n  rationale: 6 个 stale RUNNING 实验已修复标记。cuda:1/2/3 空闲，距 DDL 11 天不能浪费。exp-003 WNUT-17\\n    是唯一未覆盖的 P0 新数据集；seed456 完成 3-seed 鲁棒性协议；CPU 实验（RE diagnostic / stratification\\n    / selection curves）填补 paper 分析空白。\\n  related_experiments:\\n  - exp_id: exp_001_seed42_v2\\n    role: confirmed\\n    result: success, ρ=0.428\\n  - exp_id: exp_001_seed123_v2\\n    role: confirmed\\n    result: success, ρ=0.424\\n  - exp_id: exp_008_re_n16_v2\\n    role: confirmed\\n    result: negative, ρ=0.281\\n  - exp_id: exp-003\\n    role: dispatched\\n    result: WNUT-17 fine-tune+inference\\n  - exp_id: exp-001-seed456\\n    role: dispatched\\n    result: 3-seed completion\\n  depends_on:\\n  - D039\\n  - D032\\n- id: D041\\n  date: 2026-05-14 15:33 UTC\\n  summary: 关闭 RE seed 测试线——两 seed 确认 RE 结构一致性弱是 task 本质属性\\n  rationale: exp_008_re_seed123 (seed=123) RE SJ ρ=0.2835 vs seed42 ρ=0.281，Δ仅0.002，F1=0比例差0.2pp。跨seed高度一致，证明RE结构一致性信号退化是task复杂度的固有属性而非随机波动。Claim\\n    3 evidence base已充分，无需额外seed测试，释放资源给其他实验。\\n  related_experiments:\\n  - exp_id: exp_008_re_seed123\\n    role: confirmation\\n    result: RE SJ ρ=0.2835, cross-seed Δ=0.002\\n  - exp_id: exp_008_re_n16\\n    role: primary\\n    result: RE SJ ρ=0.281 seed42\\n  depends_on: []\\n- id: D042\\n  date: 2026-05-14 15:42 UTC\\n  summary: exp_009_v2 RE 重跑：过滤无 gold relation 实例 + proxy 独立性修正为 2 维 + inverted-U 假设未确认\\n  rationale: 'Reviewer CRITICAL: RE 分析包含 154/551 无 gold relation 实例（SJ→1.0, F1=0），sj_rho\\n    从 ~0.28 被拉低到 0.063。exp_006_v2/exp_008 均正确过滤到 397 实例。同时 ent_count 与 type_diversity\\n    ρ=0.931，独立 proxy 实为 2 个非 3 个。Inverted-U 未被确认（NER 稳定，RE 单调），论文 Claim 3 需相应调整叙事。'\\n  related_experiments:\\n  - exp_id: exp_009_v2\\n    role: primary\\n    result: CRITICAL — RE 数据未过滤，需重跑\\n  - exp_id: exp_006_v2\\n    role: reference\\n    result: 正确过滤到 397 实例\\n  - exp_id: exp_008_re_n16\\n    role: reference\\n    result: 正确过滤到 397 实例\\n  depends_on: []\\n- id: D043\\n  date: 2026-05-14 17:36 UTC\\n  summary: 放弃 WNUT-17 benchmark，聚焦 SciERC + CoNLL 双数据集；取消 LLaMA WNUT-17 fine-tuning\\n  rationale: exp_003_wnut17_v2_infer FAIL：54% F1=0（即使 downsample empty 到 25%），SJ full\\n    rho=0.062 (p=0.106 不显著)，logprob full rho=-0.411（异常负相关）。模型在社交媒体 NER 上严重不足，structural\\n    consistency 信号在此基础上无意义。继续投入（调 T/调 prompt/训 LLaMA WNUT-17）的期望收益低于成本。SciERC + CoNLL（科学+新闻，两个域）已构成充分的\\n    cross-dataset 证据。DDL 还 11 天，资源应集中在已有正面信号的实验线。\\n  related_experiments:\\n  - exp_id: exp_003_wnut17_v2_infer\\n    role: WNUT-17 推理\\n    result: 'FAIL: 54% F1=0, SJ rho=0.062 (p=0.106), logprob rho=-0.411'\\n  depends_on:\\n  - D040\\n- id: D044\\n  date: 2026-05-14 17:36 UTC\\n  summary: 3-seed NER 协议完成：seed42 ρ=0.428, seed123 ρ=0.424, seed456 ρ=0.384; cross-seed\\n    一致性确认\\n  rationale: exp_001_seed456_v2_ner 结果：SJ full rho=0.384, structural_beats_surface=true\\n    (+0.160)。三个 seed 一致显示 structural > surface，但 seed456 略低于 seed42/123（0.384 vs 0.428/0.424,\\n    Δ≈0.04）。greedy_f1=0.664, oracle=0.811, 12.3% F1=0——均在正常范围。verdict=MARGINAL 但 structural_beats_surface=true\\n    是核心 claim 的直接支持。3-seed 均值 ρ≈0.412，SD≈0.025，robustness 充分。\\n  related_experiments:\\n  - exp_id: exp_001_seed456_v2_ner\\n    role: 3-seed 第三个\\n    result: 'MARGINAL: SJ rho=0.384, structural>surface +0.160'\\n  - exp_id: exp_001_seed42_v2\\n    role: seed42\\n    result: SJ rho=0.428\\n  - exp_id: exp_001_seed123_v2\\n    role: seed123\\n    result: SJ rho=0.424\\n  depends_on:\\n  - D039\\n- id: D045\\n  date: 2026-05-14 17:37 UTC\\n  summary: WNUT-17 放弃深入：54% F1=0 + SJ rho 不显著，报告为 Claim 3 支撑证据；取消 LLaMA WNUT-17\\n  rationale: exp_003_wnut17_v2_infer 结果：greedy_f1=0.525, 54% F1=0, SJ full rho=0.062\\n    (p=0.106 不显著), logprob full rho=-0.411（异常负相关）。即使 downsample 到 25% empty，模型在社交媒体\\n    NER 上能力不足，structural consistency 信号无意义。与 RE 的 44% F1=0 相同模式——超出模型能力边界时所有信号失效。决策：(1)\\n    WNUT-17 不再追加投入（不调 T/prompt）；(2) 取消已授权的 LLaMA WNUT-17 fine-tuning；(3) 论文中报告为 Claim\\n    3（task-complexity boundary）的跨数据集支撑——当模型 F1=0 比例超过 50% 时信号退化，与 RE 发现一致。论文 cross-dataset\\n    证据用 SciERC + CoNLL-2003 两个正面数据集。\\n  related_experiments:\\n  - exp_id: exp_003_wnut17_v2_infer\\n    role: WNUT-17 inference\\n    result: 'FAIL: 54% F1=0, SJ full rho=0.062 (not significant), logprob rho=-0.411'\\n  - exp_id: exp_003_wnut17_v2\\n    role: WNUT-17 fine-tune\\n    result: success (train_loss=0.105, eval_loss=0.084)\\n  depends_on:\\n  - D040\\n- id: D046\\n  date: 2026-05-14 17:37 UTC\\n  summary: seed456 NER 3-seed 确认：SJ rho=0.384, structural>surface (+0.160)，cross-seed\\n    一致性 Δmax=0.044\\n  rationale: exp_001_seed456_v2_ner 结果：rho_sj=0.384, structural_beats_surface=true,\\n    rho_advantage=0.160, 12.3% F1=0。3-seed 对比：seed42 rho=0.428, seed123 rho=0.424,\\n    seed456 rho=0.384。最大 cross-seed Δ=0.044（seed42 vs seed456），比之前报告的 Δ<0.004（seed42\\n    vs seed123）大，但三个 seed 全部 structural>surface 且 p<0.001。结论：NER SJ 信号方向稳定，幅度有中等 seed\\n    敏感性。论文报告 mean±std：rho=0.412±0.025。\\n  related_experiments:\\n  - exp_id: exp_001_seed456_v2_ner\\n    role: seed456 NER rerun\\n    result: 'MARGINAL: rho=0.384, structural_beats_surface=true, advantage=0.160'\\n  - exp_id: exp_001_seed42_v2\\n    role: seed42 reference\\n    result: rho=0.428\\n  - exp_id: exp_001_seed123_v2\\n    role: seed123 reference\\n    result: rho=0.424\\n  depends_on:\\n  - D039\\n- id: D047\\n  date: 2026-05-14 19:18 UTC\\n  summary: Inverted-U 被否定：RE SJ 按 sent_len 单调递增 (Q1:0.110→Q4:0.473, p=0.004*)，论文 Claim\\n    3 禁用 inverted-U 表述\\n  rationale: Reviewer 对 exp_009_v2_re_rerun（过滤后 397 实例）独立核实：SJ 按 sent_len 分层呈单调递增而非\\n    inverted-U。Fisher z p=0.004 显著。同时确认 rel_count 不是独立 proxy（与 ent_count ρ=0.769），论文只应使用\\n    sent_len + ent_count 作为独立代理变量。\\n  related_experiments:\\n  - exp_id: exp_009_v2_re_rerun\\n    role: primary\\n    result: monotonic increase confirmed\\n  - exp_id: exp_009_capability_stratification\\n    role: baseline\\n    result: original stratification\\n  depends_on:\\n  - D042\\n- id: D048\\n  date: 2026-05-14 19:18 UTC\\n  summary: FK N-scaling 退化跨设置确认：CoNLL Δ=-0.007, LLaMA SciERC Δ=-0.019，论文需讨论此现象\\n  rationale: Reviewer 在 N=8→N=16 对比中发现 FK 一致性退化不是随机波动——两个独立设置（Qwen CoNLL + LLaMA SciERC）都显示退化。可能原因：FK\\n    对 category-level 频率敏感，N 增大时边缘类别波动增大。SJ 改善 +0.014/+0.016 方向正确。论文应将此作为 SJ 优于 FK\\n    的又一论据。\\n  related_experiments:\\n  - exp_id: exp_002_conll_n16\\n    role: evidence\\n    result: FK Δ=-0.007\\n  - exp_id: exp_007_llama_n16\\n    role: evidence\\n    result: FK Δ=-0.019\\n  depends_on: []\\n- id: D049\\n  date: 2026-05-14 19:20 UTC\\n  summary: 实验端进入收尾：N=16 跨模型跨数据集确认 SJ N-scaling、FK N-degradation、logprob N-invariant；3-seed\\n    鲁棒性全部通过；RE 重跑修复代理独立性。LLaMA CoNLL N=16 为最后一个 GPU 实验\\n  rationale: N=16 五信号对比跨 CoNLL 和 SciERC 一致，SJ Δρ 均为正（+0.014/+0.016），FK 均为负（-0.007/-0.019），这提供了\\n    Claim 1 (structural > surface) 在 N-scaling 维度的强证据。3-seed SD<0.025 确认结果稳定性。RE rerun\\n    修复了 proxy independence 问题（|ρ| 0.512→0.011），Claim 3 数据可靠。剩余只有 LLaMA CoNLL N=16\\n    一个 GPU 实验，之后全力转 paper writing。\\n  related_experiments:\\n  - exp_id: exp_002_conll_n16\\n    role: N-scaling cross-dataset\\n    result: SJ +0.014, FK -0.007\\n  - exp_id: exp_007_llama_n16\\n    role: N-scaling cross-model\\n    result: SJ ρ=0.379, voting_conf ρ=0.452\\n  - exp_id: exp_001_seed456_v2_ner\\n    role: 3-seed robustness\\n    result: SD<0.025, ranking stable\\n  - exp_id: exp_009_v2_re_rerun\\n    role: RE proxy fix\\n    result: SJ 0.063→0.281, ent_count |ρ| 0.512→0.011\\n  depends_on:\\n  - D044\\n  - D046\\n  - D047\\n  - D048\\n- id: D050\\n  date: 2026-05-14 19:55 UTC\\n  summary: D048 修正：FK N-scaling 非一致退化，而是 setting-dependent（3/4 退化，LLaMA CoNLL 改善 +0.029/+0.032）\\n  rationale: 'LLaMA CoNLL N=16 seed42/123 均显示 FK 改善（Δ=+0.029/+0.032），与 D048 \\\"consistently\\n    degrades\\\" 结论矛盾。可能解释：CoNLL 高基准 F1（0.924）使增加 N 提高了 FK 统计稳定性，而 SciERC 低基准 F1（0.645）增加\\n    N 引入更多噪声。论文 FK N-scaling 讨论需改为 \\\"inconsistent behavior: improvement on easy tasks,\\n    degradation on hard tasks\\\" — 与 task-complexity boundary 叙事一致。'\\n  related_experiments:\\n  - exp_id: exp_017_llama_conll_n16\\n    role: new evidence\\n    result: FK +0.029/+0.032 (2 seeds)\\n  - exp_id: exp_002_conll_n16\\n    role: prior\\n    result: FK -0.007\\n  - exp_id: exp_007_llama_n16\\n    role: prior\\n    result: FK -0.019\\n  depends_on:\\n  - D048\\n- id: D051\\n  date: 2026-05-14 21:30 UTC\\n  summary: 热力图统一使用 3-seed mean，修复合成 conditional rho 数据\\n  rationale: 'Reviewer critical: 热力图 SciERC NER/RE Qwen 行的 conditional rho 是 CoNLL\\n    比值估算的合成值，非真实测量。现已有 3-seed 真实数据，统一全行为 3-seed mean（与 LLaMA CoNLL 行一致），移除所有静默 fallback。'\\n  related_experiments:\\n  - exp_id: exp_015_v2\\n    role: 旧数据源(2-seed full rho)\\n    result: 被替换\\n  - exp_id: exp_015_unified\\n    role: 错误数据源(pilot_005 N=8)\\n    result: 弃用\\n  depends_on: []\\n- id: D052\\n  date: 2026-05-14 21:30 UTC\\n  summary: 'P0: 热力图 conditional rho 含合成数据，暂停图表使用，从真实数据重新计算'\\n  rationale: 'Reviewer CRITICAL: SciERC NER/RE Qwen 行的 conditional rho 是代码 fallback\\n    用 CoNLL 比值估算的合成值（JSON 路径错误触发静默 fallback），非实验测量。原始数据已有（exp_001_seed42_v2/seed123_v2\\n    的 samples.jsonl），重新计算后替换。'\\n  related_experiments:\\n  - exp_id: exp_015_unified\\n    role: 问题源\\n    result: 数据实为 pilot_005 N=8 单次运行\\n  - exp_id: exp_015_v2\\n    role: full rho 正确源\\n    result: seed42+seed123 均值\\n  - exp_id: exp_001_seed42_v2\\n    role: 修复数据源\\n    result: 需从 samples.jsonl 计算 conditional rho\\n  - exp_id: exp_001_seed123_v2\\n    role: 修复数据源\\n    result: 需从 samples.jsonl 计算 conditional rho\\n  depends_on: []\\n- id: D053\\n  date: 2026-05-14 21:31 UTC\\n  summary: voting_conf 从 bootstrap CI 报告中排除，论文 CI 只覆盖 SJ/FK/EM/logprob\\n  rationale: Bootstrap 代码中 voting_conf 定义与主 pipeline 不一致（多了 majority 过滤），导致 ρ 系统性偏低\\n    ~0.04。修代码简单但重跑 B=10000 耗时。论文排除 voting_conf CI 是最快最干净的修复，4 个信号的 CI 已足够支撑结论。\\n  related_experiments:\\n  - exp_id: exp_017_llama_conll_n16\\n    role: bootstrap 数据源\\n    result: SJ/FK/logprob bootstrap 与 registry 一致，voting_conf 偏低 0.04\\n  depends_on: []\\n\", \"total_chars\": 43404, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2b6cb5f-4de5-467e-8b4a-50042facf4ed",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "2bd89f23-ed7a-47c1-90eb-23f2babd9045",
  "sourceToolAssistantUUID": "a2b6cb5f-4de5-467e-8b4a-50042facf4ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T21:32:04.050Z_

Now let me look at the actual paper draft to ground my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bd89f23-ed7a-47c1-90eb-23f2babd9045",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BAL7MvvTDftK28o3Zd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3433199a-4ab2-46bd-8720-89c5fd3fba6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBYGCxahmKGzBsMTBen8mp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27312,
      "cache_read_input_tokens": 45919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27312,
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

_source line 24 · 2026-05-14T21:32:05.410Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VTBLAEdPLPQmx6tob7zWcR`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3433199a-4ab2-46bd-8720-89c5fd3fba6e",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BAL7MvvTDftK28o3Zd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7fc5f94-7625-4bec-98ee-aee314e0402b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBYGCxahmKGzBsMTBen8mp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27312,
      "cache_read_input_tokens": 45919,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27312
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 45919,
          "cache_creation_input_tokens": 27312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27312,
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

_source line 25 · 2026-05-14T21:32:05.435Z_

<details><summary>↩ Tool result · `toolu_01VTBLAEdPLPQmx6tob7zWcR`</summary>

```text
artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
docs/paper/main.tex
artifacts/_project/paper/experiments.tex
docs/paper/sections/method.tex
docs/paper/sections/introduction.tex
artifacts/_project/paper/introduction.tex
docs/paper/sections/related_work.tex
artifacts/_project/paper/related_work.tex
docs/paper/sections/discussion.tex
artifacts/_project/paper/discussion.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
docs/paper/sections/abstract.tex
artifacts/_project/paper/abstract.tex
docs/paper/sections/conclusion.tex
artifacts/_project/paper/conclusion.tex
docs/paper/sections/limitations.tex
artifacts/_project/paper/limitations.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7fc5f94-7625-4bec-98ee-aee314e0402b",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "8ec99249-5570-422f-9370-404b94340938",
  "sourceToolAssistantUUID": "f7fc5f94-7625-4bec-98ee-aee314e0402b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T21:32:08.048Z_

<details open><summary>🔧 Tool call — Read · `toolu_018SMNfJvdvPQ6obGhQX1v1t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ec99249-5570-422f-9370-404b94340938",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BAg7PTVHjbRTioWAJ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfe0e607-1951-4d64-9a71-f5e2442d1cb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fjCochkVdsFgU7a6VjKX3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 73231,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 476
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 73231,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 476,
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

_source line 27 · 2026-05-14T21:32:08.052Z_

<details><summary>↩ Tool result · `toolu_018SMNfJvdvPQ6obGhQX1v1t`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\end{document}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfe0e607-1951-4d64-9a71-f5e2442d1cb3",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "2b498817-95e5-45af-9986-196452b34e7b",
  "sourceToolAssistantUUID": "dfe0e607-1951-4d64-9a71-f5e2442d1cb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T21:32:11.432Z_

<details open><summary>🔧 Tool call — Read · `toolu_013NhpTk7ssWErADyjA9JwUQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b498817-95e5-45af-9986-196452b34e7b",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BAsN4CFisrJVLCzZqe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb609fcf-d0b6-4259-898f-affbe3a9a076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjXAB2hfEnrnetTkUZ3TAu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 73707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 495,
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

_source line 29 · 2026-05-14T21:32:11.470Z_

<details><summary>↩ Tool result · `toolu_013NhpTk7ssWErADyjA9JwUQ`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb609fcf-d0b6-4259-898f-affbe3a9a076",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "155753ed-ecc1-426a-be20-38add16f6c8f",
  "sourceToolAssistantUUID": "eb609fcf-d0b6-4259-898f-affbe3a9a076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T21:32:11.946Z_

<details open><summary>🔧 Tool call — Read · `toolu_014uWV9XS9AFRntnJSnhRDJC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "155753ed-ecc1-426a-be20-38add16f6c8f",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BAsN4CFisrJVLCzZqe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18275791-88bb-4698-a88a-1e9842355802",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjXAB2hfEnrnetTkUZ3TAu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 73707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 495,
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

_source line 31 · 2026-05-14T21:32:12.151Z_

<details><summary>↩ Tool result · `toolu_014uWV9XS9AFRntnJSnhRDJC`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives.
14	\textit{Quality estimation} asks which inputs the model handles reliably---a ranking over instances.
15	\textit{Sample selection} asks which of $N$ candidate outputs is best for a given input---a ranking over samples.
16	These require fundamentally different signal properties: the former benefits from instance-level aggregation across all $N$ samples, while the latter demands per-sample discrimination.
17	Existing evaluations rarely separate the two.
18	Self-consistency methods designed for discrete answers \cite{wang2023selfconsistency, chen2024usc} assume outputs can be grouped by equivalence and counted, an assumption that breaks when outputs are entity sets with partial overlap.
19	Weighted variants that incorporate model confidence \cite{taubenfeld2025cisc, kang2025selfcertainty} have shown promise for best-of-$N$ selection on reasoning tasks, but their applicability to structured prediction remains untested.
20	The most directly relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based entity and relation extraction but relies on surface-level matching, a limitation the authors themselves acknowledge: their approach ``overlooks semantically consistent outputs'' that differ only in surface form.
21	No existing work systematically compares confidence signals across the structural, surface, and model-internal families for generative IE, nor disentangles quality estimation from sample selection in this setting.
22	
23	Our central finding is that consistency-based signals are effective instance-level quality estimators but poor sample selectors for structured IE.
24	Consistency signals aggregate over $N$ samples to produce a single score per input, making them well-suited to predict input difficulty---instances where the model consistently extracts similar structures are indeed easier.
25	Entity voting confidence, our best signal, achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, a correlation strong enough to be practically useful for quality-aware routing.
26	Yet this correlation does not translate into selection gains: on NER best-of-$N$, no signal surpasses greedy decoding despite 16 percentage points of oracle headroom.
27	We term this the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}).
28	The gap arises because instance-level signals cannot discriminate among $N$ candidates that share similar consistency profiles---they predict \textit{which inputs} are hard, not \textit{which output} is best.
29	Only log-probability, the sole per-sample signal in our comparison, achieves selection gains, and only on relation extraction (+2.3~pp over greedy), where per-sample variance is higher.
30	We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
31	
32	Our contributions are as follows:
33	\begin{enumerate}
34	    \item \textbf{First systematic comparison of confidence signals for generative IE.}
35	    We evaluate five signals from three families on quality estimation for NER and RE.
36	    Entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$; structural signals outperform surface and model-internal alternatives on complex schemas (SciERC), while surface signals dominate on simpler tasks (CoNLL).
37	
38	    \item \textbf{Identification of the correlation-selection gap.}
39	    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.
40	    Despite strong instance-level correlations ($\rho$ up to 0.50), no consistency signal improves NER best-of-$N$ over greedy decoding; only log-probability helps on RE (+2.3~pp).
41	    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.
42	
43	    \item \textbf{Task-complexity boundary conditions.}
44	    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, where 54\% of instances receive zero F1).
45	    This establishes practical guidance for signal selection based on expected task difficulty.
46	\end{enumerate}
47	
48	The remainder of this paper is organized as follows.
49	\S\ref{sec:method} formalizes the problem and defines the five confidence signals.
50	\S\ref{sec:experiments} presents quality estimation results, the correlation-selection gap analysis, and robustness evaluations.
51	\S\ref{sec:related} situates our work in the broader landscape of self-consistency, uncertainty estimation, and LLM-based IE.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18275791-88bb-4698-a88a-1e9842355802",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "8038cabb-a833-47ed-b3af-2d5ae846f024",
  "sourceToolAssistantUUID": "18275791-88bb-4698-a88a-1e9842355802",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T21:32:12.426Z_

<details open><summary>🔧 Tool call — Read · `toolu_0117aHfaVzBkyG34b72Q7ePf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8038cabb-a833-47ed-b3af-2d5ae846f024",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BAsN4CFisrJVLCzZqe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec0e0d74-a1e9-494a-b9a8-9f7a16da2df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjXAB2hfEnrnetTkUZ3TAu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 73707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 495,
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

_source line 33 · 2026-05-14T21:32:12.479Z_

<details><summary>↩ Tool result · `toolu_0117aHfaVzBkyG34b72Q7ePf`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	Our work connects three research threads: self-consistency and test-time scaling methods developed for reasoning tasks, confidence estimation for structured information extraction, and broader uncertainty quantification for language models.
4	
5	\subsection{Self-Consistency and Test-Time Scaling}
6	
7	\paragraph{Self-consistency for discrete and free-form tasks.}
8	Self-consistency decoding \cite{wang2023selfconsistency} improves chain-of-thought reasoning by sampling multiple rationales and selecting the most frequent answer via majority vote.
9	This paradigm assumes a discrete answer space where outputs can be grouped by equivalence and counted---an assumption that holds for arithmetic, commonsense QA, and similar tasks but breaks for set-valued structured outputs.
10	\citet{chen2024usc} extend self-consistency to free-form text generation by replacing exact matching with LLM-based semantic comparison, while SelfCheckGPT \cite{manakul2023selfcheckgpt} leverages cross-sample consistency to detect hallucinations in open-ended generation.
11	\citet{thirukovalluru2024atomic} decompose long-form outputs into atomic sub-claims and measure per-claim consistency, moving beyond whole-output comparison.
12	These methods operate on text-level equivalence or entailment; our work instead compares \textit{structured sets} of entities and relations, requiring set-theoretic similarity measures that account for partial overlap, type constraints, and span-level matching.
13	
14	\paragraph{Test-time scaling and sample selection.}
15	A growing body of work studies how to allocate additional compute at inference time.
16	\citet{snell2024scaling} characterize the scaling laws governing test-time compute, showing that repeated sampling with effective selection can substitute for model scaling.
17	\citet{brown2024monkeys} demonstrate that best-of-$N$ sampling with large $N$ yields substantial gains across diverse tasks.
18	Several recent methods aim to improve selection without trained reward models.
19	CISC \cite{taubenfeld2025cisc} combines confidence scores with majority voting, weighting each sample's contribution to the consensus.
20	Self-Certainty \cite{kang2025selfcertainty} uses KL divergence between a sample's token distribution and the prior to select high-quality outputs, demonstrating that reward-free selection is viable for mathematical reasoning.
21	ReASC \cite{kim2026reasc} adaptively adjusts the number of samples based on estimated difficulty, while \citet{wang2025rankedvoting} replace plurality voting with ranked aggregation, and \citet{oh2025latentsc} perform consistency estimation in latent space rather than output space.
22	
23	All of these methods target reasoning and QA tasks with discrete or near-discrete answer spaces.
24	Our work is, to our knowledge, the first to extend self-consistency to set-valued structured outputs in IE, and the first to identify the correlation-selection gap: strong quality estimation ($\rho{=}0.50$) coexists with selection failure (no gain over greedy on NER).
25	In direct dialogue with \citet{kang2025selfcertainty}, who show that reward-free selection succeeds for reasoning, our results demonstrate that this success does not transfer to structured extraction, where the combinatorial output space and instance-level nature of consistency signals preclude effective per-sample discrimination.
26	
27	\subsection{Consistency and Confidence for Structured IE}
28	
29	The most directly relevant prior work is \citet{nedellec2026consistency}, who study consistency--accuracy correlations in hard-prompted LLMs for NER and relation extraction on plant-health data.
30	Their findings corroborate our quality-estimation results: higher inter-sample consistency predicts higher extraction accuracy.
31	However, three key limitations motivate our work.
32	First, they rely on surface-level string matching and explicitly acknowledge that their approach ``overlooks semantically consistent outputs''---precisely the gap our Soft Jaccard signal addresses through type-aware bipartite matching with span overlap.
33	Second, they do not study best-of-$N$ selection, leaving the quality-estimation-to-selection transfer question unexamined.
34	Third, their evaluation covers a single domain with hard-prompted (temperature-zero) generation and no comparison across signal families.
35	Our work extends their analysis to multi-domain benchmarks, temperature-based sampling, and a systematic five-signal comparison that reveals when structural signals outperform surface alternatives and vice versa.
36	
37	CoCoA \cite{vashurin2025cocoa} proposes a minimum Bayes risk framework that fuses model confidence with inter-sample consistency for uncertainty quantification on QA, summarization, and translation.
38	Their confidence-consistency ensemble parallels our analysis of signal combinations, but they do not address structured extraction, where the unit of comparison shifts from text sequences to entity and relation sets.
39	
40	Our evaluation setting---LLMs performing IE as a generation task---builds on a line of work establishing generative approaches to entity and relation extraction.
41	UniNER \cite{zhou2024uniner} and GoLLIE \cite{sainz2024gollie} train universal IE models via instruction tuning; \citet{wadhwa2023revisiting} and InstructUIE \cite{wang2023instructuie} demonstrate that instruction-following LLMs can perform extraction zero-shot or with minimal supervision; GenIE \cite{josifoski2022genie} and CodeIE \cite{li2023codeie} frame IE as constrained sequence generation.
42	We adopt constrained decoding \cite{willard2023guided} following this paradigm and study confidence estimation as an orthogonal dimension: given that LLMs generate structured outputs, how reliably can we estimate extraction quality from multiple samples?
43	
44	\subsection{Uncertainty Estimation and Calibration}
45	
46	\paragraph{Confidence and uncertainty for LLMs.}
47	Several surveys chart the landscape of confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and their intersection with calibration \cite{hobelsberger2025systematic}.
48	Our work bridges confidence estimation and selective prediction: we use confidence signals not only to rank instances by reliability but also to attempt best-of-$N$ selection, revealing that these two objectives impose different requirements on the underlying signal.
49	
50	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning rather than surface form and estimates uncertainty from cluster statistics.
51	\citet{kossen2024semantic} distill semantic entropy into lightweight probes, and P(True) \cite{kadavath2022language} directly queries the model for its confidence.
52	These approaches measure uncertainty over the model's belief distribution; our structural signals instead measure agreement over output \textit{structure}, comparing extracted entity sets rather than semantic content of free-form text.
53	
54	\paragraph{Calibration and ensembles.}
55	Modern neural networks are often miscalibrated \cite{guo2017calibration}, and calibration techniques for pre-trained language models \cite{desai2020calibration} aim to align predicted probabilities with empirical accuracy.
56	Our reliability diagrams assess whether confidence signals are calibrated for IE, extending calibration analysis beyond classification to structured prediction.
57	Deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation, requiring multiple forward passes through different model parameters.
58	Our multi-sample approach is conceptually related---we also use variation across stochastic outputs---but requires no model modification or access to internal parameters beyond token log-probabilities, operating entirely post-hoc on generated outputs.
59	
60	\paragraph{Uncertainty for token-level and span-level NER.}
61	Prior work on NER uncertainty operates within discriminative, pre-LLM paradigms: \citet{xiao2019uncertainty} study Bayesian inference for sequence labeling, \citet{shelmanov2021active} leverage uncertainty for active learning in NER, and \citet{zhang2023ener} estimate entity-level uncertainty from span probabilities.
62	These methods assume access to per-token classification logits from a discriminative model.
63	In the generative LLM setting we study, entity boundaries are implicit in the decoded text and uncertainty must be estimated from the generation process itself.
64	
65	\paragraph{Related paradigms.}
66	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides distribution-free coverage guarantees but targets prediction sets rather than quality ranking.
67	Trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and reward models \cite{wang2024mathshepherd} learn to score outputs from labeled data; we focus on unsupervised signals that require no additional training.
68	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework of abstaining when uncertain; our contribution is characterizing which confidence signals support this objective for generative IE and where the quality-estimation-to-selection transfer breaks down.
69	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec0e0d74-a1e9-494a-b9a8-9f7a16da2df1",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "7624c9e8-0575-47bd-9841-65b3c1633e6a",
  "sourceToolAssistantUUID": "ec0e0d74-a1e9-494a-b9a8-9f7a16da2df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T21:32:13.322Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WMQY4mdVYamGuiVKKitiaU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7624c9e8-0575-47bd-9841-65b3c1633e6a",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BAsN4CFisrJVLCzZqe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7c486a6-7c06-440f-98a1-a02d3cd22dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjXAB2hfEnrnetTkUZ3TAu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 73707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 495,
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

_source line 35 · 2026-05-14T21:32:13.337Z_

<details><summary>↩ Tool result · `toolu_01WMQY4mdVYamGuiVKKitiaU`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.
12	This gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\S\ref{sec:complexity_robustness}).
13	
14	\paragraph{Models.}
15	Our primary model is \textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.
16	For cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.
17	
18	\paragraph{Sampling and Evaluation.}
19	For each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.
20	We use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.\footnote{$N{=}16$ experiments for CoNLL (Qwen) and SciERC (LLaMA) have also been completed with consistent results; see Table~\ref{tab:robustness}.}
21	Quality estimation is measured along two axes: \textit{rank correlation} with instance-level F1 via Spearman $\rho$ and Kendall $\tau$, and \textit{binary discrimination} via AUROC (instances above vs.\ below median F1).
22	Downstream utility is assessed through \textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instance.
23	Instance-level F1 uses exact span matching for NER and head-tail-label matching for RE, where a relation is correct only when both argument entities and the relation label match the gold annotation.
24	The greedy decoding baseline ($T{=}0$, $N{=}1$) establishes performance without test-time scaling.
25	
26	\paragraph{Confidence Signals.}
27	We compare five signals from three families (detailed in \S\ref{sec:signals}).
28	\textit{Structural} signals operate on extracted entity/relation sets: \textbf{Voting Confidence} aggregates per-extraction frequency across samples, and \textbf{Soft Jaccard (SJ)} measures pairwise set similarity \cite{jaccard1901distribution}.
29	\textit{Surface} signals operate on string representations: \textbf{Fleiss' $\kappa$ (FK)} quantifies inter-sample agreement treating samples as independent annotators \cite{fleiss1971agreement}, and \textbf{Exact Match (EM)} computes the fraction of identical sample pairs.
30	The \textit{model-internal} signal is \textbf{log-probability (logprob)}, the mean token-level log-likelihood.
31	
32	\paragraph{Implementation.}
33	Inference uses vLLM with XGrammar constrained decoding \cite{willard2023guided} to enforce valid JSON output structure.
34	A span realignment post-processing step corrects character-level offset mismatches between generated and gold annotation spans.
35	All confidence signals are computed from the $N$ samples without access to gold labels.
36	
37	%% ============================================================
38	\subsection{Quality Estimation Results}
39	\label{sec:qe_results}
40	
41	\begin{table*}[t]
42	\centering
43	\small
44	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families.}
45	\label{tab:quality_estimation}
46	\begin{tabular}{ll cc cc cc cc}
47	\toprule
48	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
49	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
50	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
51	\midrule
52	Voting Conf. & Structural & \textbf{.502} & \textbf{.728} & \textbf{.422} & \textbf{.716} & .424 & .789 & .426 & .709 \\
53	Soft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \textbf{.431} & .704 \\
54	Fleiss' $\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\
55	Exact Match  & Surface    & .257 & .623 & .100 & .504 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
56	Log-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \textbf{.761} \\
57	\bottomrule
58	\end{tabular}
59	\end{table*}
60	
61	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
62	
63	\paragraph{Structural signals dominate on complex schemas.}
64	On SciERC NER, Voting Confidence achieves $\rho{=}0.502$, substantially outperforming the second-best signal, SJ ($\rho{=}0.357$; bootstrap 95\% CI: [0.295, 0.459]), and all remaining signals ($\rho{\leq}0.265$).
65	Voting's advantage reflects its extraction-level granularity: it rewards entities that appear consistently while penalizing hallucinated or missed ones, whereas SJ compares entire sets and is sensitive to both overlap and total extraction count.
66	The structural advantage persists on RE, where Voting ($\rho{=}0.422$) again leads.
67	However, all signals weaken on RE: 44\% of instances receive zero F1, creating a floor effect that compresses the discriminable range.
68	Notably, FK ($\rho{=}0.253$) exceeds SJ ($\rho{=}0.211$) on RE---a reversal from NER that shows no single structural signal dominates across both tasks.
69	
70	\paragraph{Signal rankings shift with task difficulty.}
71	On CoNLL NER, where greedy decoding achieves ${>}$91\% micro F1, the signal landscape changes substantially.
72	Exact Match leads with $\rho{=}0.451$ and AUROC${=}0.816$, surpassing SJ ($\rho{=}0.436$) and Voting ($\rho{=}0.424$).
73	When most samples are near-correct, binary agreement captures the remaining variance more efficiently than set-level similarity.
74	This reversal---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on intrinsic task difficulty.
75	
76	\paragraph{Cross-model stability.}
77	Comparing Qwen and LLaMA on CoNLL, SJ shows remarkable stability: $\rho{=}0.436$ (Qwen) vs.\ $\rho{=}0.431$ (LLaMA), a gap of only 0.005.
78	This model-agnostic property is expected for structural signals that operate on outputs rather than internal model states, and provides the strongest evidence that SJ generalizes across architectures.
79	The SJ--FK gap also narrows with schema simplification: $\Delta\rho{=}0.092$ on SciERC NER (6 entity types) vs.\ $\Delta\rho{=}0.003$ on CoNLL with LLaMA (4 types), suggesting that set-level structure contributes less when the type inventory is small.
80	
81	\paragraph{The logprob paradox.}
82	Log-probability reveals a dissociation between ranking and classification.
83	On CoNLL with LLaMA, it achieves the highest AUROC (0.761) yet the lowest $\rho$ (0.307) among all signals.
84	This pattern indicates that logprob assigns well-separated scores to easy vs.\ hard instances (strong binary discrimination) but provides little resolution within each group (weak ranking), making it better suited for binary filtering than continuous quality estimation.
85	We return to this distinction in \S\ref{sec:complexity_robustness} and visualize it in Figure~\ref{fig:signal_heatmap}.
86	
87	\paragraph{Oracle headroom and practical ceilings.}
88	On CoNLL, oracle best-of-$N$ selection yields only +4.2~pp (Qwen) and +1.8~pp (LLaMA) over greedy.
89	When the model already operates near its performance ceiling, confidence signals serve as \textit{reliability assurance}---confirming that outputs are trustworthy---rather than enabling selective prediction gains.
90	We therefore focus selection analysis (\S\ref{sec:selection_gap}) on SciERC, where oracle headroom exceeds 16~pp.
91	
92	%% ============================================================
93	\subsection{The Correlation-Selection Gap}
94	\label{sec:selection_gap}
95	
96	\begin{table}[t]
97	\centering
98	\small
99	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \textbf{bold}. EM produces binary agreement without sample ranking.}
100	\label{tab:selection}
101	\begin{tabular}{lcc}
102	\toprule
103	Method & NER F1 & RE F1 \\
104	\midrule
105	Oracle & 0.769 & 0.561 \\
106	\midrule
107	Log-prob           & 0.609 & \textbf{0.397} \\
108	Ensemble (SJ+Vot.) & 0.604 & 0.367 \\
109	Soft Jaccard       & 0.604 & 0.368 \\
110	Voting             & 0.596 & 0.338 \\
111	Exact Match        & ---   & ---   \\
112	\midrule
113	Greedy ($T{=}0$)   & \textbf{0.609} & 0.374 \\
114	Random             & 0.580 & 0.338 \\
115	\bottomrule
116	\end{tabular}
117	\end{table}
118	
119	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection.
120	Table~\ref{tab:selection} compares selection F1 on SciERC ($N{=}8$).
121	
122	\paragraph{NER: no signal surpasses greedy.}
123	The oracle upper bound (0.769) reveals 16.0~pp of headroom above greedy (0.609).
124	Yet no confidence signal closes this gap.
125	Log-probability (0.609) merely ties greedy; the best quality estimator, Voting ($\rho{=}0.502$), selects to only 0.596, \textit{below} greedy.
126	An ensemble of SJ and Voting (AUROC${=}0.735$) also fails, achieving 0.604.
127	The greedy--logprob tie is revealing: log-probability selects the sample with highest model confidence, which on average matches the deterministic greedy output, implying that the $N$ samples cluster at a similar quality level with insufficient variance for any signal to exploit.
128	The Random baseline (0.580) confirms that not all samples are equal---uniform selection loses 2.9~pp vs.\ greedy---but the discriminative structure captured by confidence signals adds no value beyond greedy's deterministic choice.
129	
130	\paragraph{RE: logprob uniquely succeeds.}
131	For RE, log-probability is the only signal to exceed greedy (0.397 vs.\ 0.374, +2.3~pp).
132	Structural signals trail or match greedy: SJ selects to 0.368 and Voting to 0.338.
133	The oracle gap of 18.7~pp (0.561 vs.\ 0.374) indicates substantially more per-instance variance than NER.
134	Log-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.
135	
136	\paragraph{Quality estimation $\neq$ output selection.}
137	We attribute this gap (Figure~\ref{fig:selection_gap}) to a fundamental distinction: instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best for a given input.
138	When per-sample variance is low relative to instance-level difficulty---as in NER, where the model often produces $N$ similar extractions---even perfect quality estimation cannot discriminate among near-identical candidates.
139	
140	\paragraph{Implications for test-time scaling.}
141	This correlation-selection gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}.
142	Scaling inference compute through repeated sampling assumes a selector can identify the best sample.
143	Our results show that for structured prediction, existing confidence signals serve as quality \textit{estimators}---useful for flagging unreliable predictions---but not as effective \textit{selectors}.
144	Closing this gap likely requires signals that capture per-sample rather than per-instance variation, such as trained verifiers \cite{cobbe2021verifiers} or pairwise comparison models.
145	
146	%% ============================================================
147	\subsection{Task Complexity and Signal Robustness}
148	\label{sec:complexity_robustness}
149	
150	\paragraph{Task difficulty as a boundary condition.}
151	Signal effectiveness varies systematically with task difficulty.
152	On CoNLL (greedy micro F1${>}$0.91), EM leads all signals ($\rho{=}0.451$); on SciERC NER (micro F1$\,{\approx}\,$0.66), SJ overtakes EM ($\rho{=}0.357$ vs.\ 0.257); on SciERC RE, where 44\% of instances score zero F1, all signals converge to $\rho{\approx}0.25$.
153	The NER--RE difference is statistically confirmed: Fisher's $z$-test on $\rho_\text{SJ}$ yields $z{=}2.31$, $p{=}0.021$.
154	
155	\paragraph{Per-relation diagnostic.}
156	RE signal degradation is relation-specific.
157	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
158	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
159	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
160	
161	\paragraph{Capability stratification.}
162	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
163	The SJ advantage over logprob remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
164	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
165	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
166	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
167	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: Voting reaches $\rho{=}0.630$, logprob $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
168	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
169	
170	\paragraph{Method boundary: WNUT-17.}
171	WNUT-17 establishes where the approach breaks down.
172	SJ achieves $\rho{=}0.062$ ($p{=}0.106$, not statistically significant), with 54\% of instances at zero F1.
173	Log-probability shows a strong \textit{negative} correlation ($\rho{=}{-}0.411$): the model is confidently wrong on novel entities, a calibration failure that no post-hoc consistency signal can remedy.
174	This is a boundary of the method, not a limitation of the datasets.
175	
176	\begin{table}[t]
177	\centering
178	\small
179	\caption{Signal robustness across temperature and sample size on SciERC (Spearman $\rho$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
180	\label{tab:robustness}
181	\begin{tabular}{llcc}
182	\toprule
183	& & NER $\rho$ & RE $\rho$ \\
184	\midrule
185	\multicolumn{4}{l}{\textit{Temperature} ($N{=}8$)} \\
186	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
187	\quad SJ & $T{=}1.0$ & 0.357 & 0.211 \\
188	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
189	\quad FK & $T{=}1.0$ & 0.265 & 0.253 \\
190	\midrule
191	\multicolumn{4}{l}{\textit{Sample size} ($T{=}1.0$)} \\
192	\quad SJ & $N{=}8$  & 0.357 & 0.211 \\
193	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
194	\quad FK & $N{=}8$  & 0.265 & 0.253 \\
195	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
196	\bottomrule
197	\end{tabular}
198	\end{table}
199	
200	\paragraph{Robustness analysis.}
201	Table~\ref{tab:robustness} reports signal stability across temperature and sample size on SciERC.
202	\textit{Temperature.}
203	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.357 ($T{=}1.0$), a difference of 0.031 whose bootstrap confidence interval includes zero.
204	FK shows mixed behavior: NER $\rho$ drops by 0.056, while RE $\rho$ increases by 0.069, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
205	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.357 vs.\ 0.265 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
206	
207	\textit{Sample size.}
208	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.357 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.071$.
209	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
210	FK shows inconsistent $N$-scaling behavior: modest gains on SciERC ($+0.015$) but degradation on CoNLL ($\Delta{=}{-}0.007$) and with LLaMA ($\Delta{=}{-}0.019$), suggesting that surface agreement is sensitive to the sampling distribution in ways that structural signals are not.
211	Voting confidence also scales positively ($+0.005$ on CoNLL, $+0.018$ on SciERC), while logprob is approximately $N$-invariant ($\Delta{\leq}0.021$).
212	This divergence---structural signals improve or hold steady with $N$ while FK degrades---provides additional evidence for the structural family's robustness.
213	SJ also achieves the lowest calibration error (ECE$\,{=}\,$0.075--0.102 across settings), suggesting that its confidence estimates are better aligned with actual extraction quality.
214	For RE at $N{=}16$, SJ ($\rho{=}0.281$), FK ($\rho{=}0.279$), and logprob ($\rho{=}0.287$) all plateau at comparable levels, suggesting that compound entity-then-relation errors impose a ceiling that additional samples cannot overcome.
215	
216	\paragraph{Cross-model transfer.}
217	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.363$, FK $\rho{=}0.327$).
218	On CoNLL, the cross-model gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
219	On conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
220	At $N{=}16$, the structural-over-logprob advantage holds across all tested settings: Qwen SciERC (Voting $\rho{=}0.411$ vs.\ logprob 0.259, $\Delta{=}{+}0.152$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ logprob 0.328, $\Delta{=}{+}0.135$), and LLaMA SciERC (Voting $\rho{=}0.452$ vs.\ logprob 0.277, $\Delta{=}{+}0.175$).
221	
222	\paragraph{Evaluation circularity.}
223	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\Delta\rho$ of $3.1{\times}10^{-4}$.
224	Evaluation circularity is negligible.
225	
226	\paragraph{Conditional filtering reveals signal divergence.}
227	Filtering to non-zero F1 instances improves SJ correlations: NER $\rho{=}0.412$ (from 0.357), RE $\rho{=}0.368$ at $N{=}8$.
228	At $N{=}16$, signal families diverge sharply on conditional RE: SJ maintains $\rho{=}0.308$, while logprob drops to $\rho{=}{-}0.026$---effectively zero---showing that logprob's apparent RE utility at $N{=}8$ does not generalize to larger sample sets.
229	For applications that can first filter out catastrophic failures, SJ's effective ranking approaches $\rho{\approx}0.4$ on both NER and RE, a regime where quality-aware aggregation can provide meaningful benefit.
230	
231	\paragraph{Binary filtering vs.\ continuous ranking.}
232	The logprob paradox observed in Table~\ref{tab:quality_estimation}---highest AUROC (0.761) but lowest $\rho$ (0.307) on CoNLL with LLaMA---reflects a fundamental distinction in how signals encode quality information.
233	Log-probability provides coarse separation between reliable and unreliable instances (suited for accept/reject thresholds), while structural signals like SJ and Voting provide finer-grained ranking (suited for prioritization and quality-aware aggregation).
234	Figure~\ref{fig:reliability} visualizes this complementarity across the difficulty spectrum.
235	Practitioners should select signal type based on the downstream application: binary filtering favors logprob; ranking-dependent decisions favor structural consistency.
236	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7c486a6-7c06-440f-98a1-a02d3cd22dd1",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "ba8f3692-1f4e-4ac4-adbf-61e2951785cf",
  "sourceToolAssistantUUID": "d7c486a6-7c06-440f-98a1-a02d3cd22dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T21:32:13.776Z_

<details open><summary>🔧 Tool call — Read · `toolu_016EziK9J5Bytp4Dz1EfcBtb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba8f3692-1f4e-4ac4-adbf-61e2951785cf",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BAsN4CFisrJVLCzZqe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67385866-2610-4ba2-bed7-a3656dc37d6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjXAB2hfEnrnetTkUZ3TAu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 73707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 495,
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

_source line 37 · 2026-05-14T21:32:13.818Z_

<details><summary>↩ Tool result · `toolu_016EziK9J5Bytp4Dz1EfcBtb`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	Our results suggest different signal choices depending on the deployment scenario.
5	For per-instance quality estimation, entity voting provides the strongest single signal ($\rho{=}0.50$, Table~\ref{tab:quality_estimation}).
6	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}), and it generalizes beyond entity-level structure to any set-valued output.
7	Under conditional filtering, SJ achieves $\rho{\approx}0.4$ on both NER and RE (\S\ref{sec:complexity_robustness}), and its ensemble with voting reaches AUROC${=}0.735$.
8	For binary accept/reject decisions, logprob is most effective (AUROC${=}0.761$ on CoNLL with LLaMA).
9	For best-of-$N$ selection, greedy decoding is near-optimal on NER; on RE, logprob is the only helpful signal (+2.3~pp, Table~\ref{tab:selection}).
10	
11	\paragraph{Signals discriminate between instances, not within strata.}
12	When instances are stratified by greedy F1, within-stratum correlations approach zero for all signals.
13	Confidence signals capture \textit{between-instance} quality differences---identifying which inputs the model handles reliably---rather than providing fine-grained discrimination among instances of similar difficulty.
14	This is the complementary face of the correlation-selection gap (\S\ref{sec:selection_gap}): signals that predict input difficulty cannot rank outputs within a difficulty stratum.
15	The practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.
16	
17	\paragraph{Task-difficulty-dependent signal selection.}
18	Across all three $N{=}16$ settings, the structural-over-logprob ordering holds consistently (\S\ref{sec:complexity_robustness}).
19	However, the \textit{optimal} signal shifts with task difficulty: EM dominates on easy tasks (CoNLL, greedy F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17, 54\% zero F1).
20	This ordering is model-agnostic---cross-model rankings between Qwen and LLaMA are identical---suggesting that the difficulty gradient, not model-specific behavior, determines which signal family is most informative.
21	
22	\paragraph{Capability boundary framework.}
23	Structural signals are most effective within the model's capability range.
24	Beyond it---RE with 44\% zero-F1 instances, WNUT-17 with 54\%---all signals converge toward zero or negative correlation.
25	Within the capability range, output complexity modulates signal effectiveness: the high-complexity RE subset ($n{=}81$) yields substantially stronger correlations (Voting $\rho{=}0.630$, SJ $\rho{=}0.502$) than the full set.
26	Conditional filtering further separates signal families: at $N{=}16$, SJ maintains $\rho{=}0.308$ on RE while logprob collapses to $\rho{=}{-}0.026$ (\S\ref{sec:complexity_robustness}).
27	The ``sweet spot'' for structural confidence signals is the intersection of sufficient model capability and sufficient output complexity---a regime where the model can produce varied but partially correct extractions rather than uniform failures.
28	
29	\paragraph{Methodological implications of $\rho$--AUROC separation.}
30	The logprob paradox on CoNLL with LLaMA---lowest $\rho$ (0.307) yet highest AUROC (0.761, Table~\ref{tab:quality_estimation})---reveals that rank correlation and binary discrimination measure fundamentally different signal properties.
31	Logprob provides coarse separation between reliable and unreliable instances, while structural signals provide finer-grained ranking across the quality spectrum.
32	Different downstream decisions therefore require different signals: threshold-based filtering favors logprob; ranking-dependent applications favor structural consistency.
33	Evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67385866-2610-4ba2-bed7-a3656dc37d6f",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "bf86deac-e984-444a-a9e5-d71fc8162156",
  "sourceToolAssistantUUID": "67385866-2610-4ba2-bed7-a3656dc37d6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T21:32:14.252Z_

<details open><summary>🔧 Tool call — Read · `toolu_014jbjpewZ9tHRQo15MBPmNb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf86deac-e984-444a-a9e5-d71fc8162156",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BAsN4CFisrJVLCzZqe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "935a6b85-824e-41be-b8fd-43c9e5df99a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjXAB2hfEnrnetTkUZ3TAu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 73707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 495,
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

_source line 39 · 2026-05-14T21:32:14.271Z_

<details><summary>↩ Tool result · `toolu_014jbjpewZ9tHRQo15MBPmNb`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Several directions remain open.
13	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
14	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.
15	Integration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.
16	Finally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "935a6b85-824e-41be-b8fd-43c9e5df99a0",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "3cc442a2-3b64-4726-9057-cf0a562f57b0",
  "sourceToolAssistantUUID": "935a6b85-824e-41be-b8fd-43c9e5df99a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T21:32:14.540Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VUsU7sfoyy6DPH6KHvE2DH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cc442a2-3b64-4726-9057-cf0a562f57b0",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BAsN4CFisrJVLCzZqe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c0b84fd-a32b-4b08-8f43-7460e585ee05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjXAB2hfEnrnetTkUZ3TAu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 73707,
      "output_tokens": 537,
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
          "output_tokens": 537,
          "cache_read_input_tokens": 73707,
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

_source line 41 · 2026-05-14T21:32:14.554Z_

<details><summary>↩ Tool result · `toolu_01VUsU7sfoyy6DPH6KHvE2DH`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.071$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL, the SJ--FK gap is only 0.004 ($\rho{=}0.436$ vs.\ $0.431$ for LLaMA), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c0b84fd-a32b-4b08-8f43-7460e585ee05",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "f8b7a35e-f5e3-4caf-848c-53525ca2ed59",
  "sourceToolAssistantUUID": "8c0b84fd-a32b-4b08-8f43-7460e585ee05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-14T21:32:18.233Z_

Now let me also check the method section and any dream review reports for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8b7a35e-f5e3-4caf-848c-53525ca2ed59",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BBMUVnEaph2w7XhzSD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d753c6d5-e280-4d03-9e5f-8e72a425bc82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMsd8vqStLiWHZp9CCufNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14147,
      "cache_read_input_tokens": 74202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14147,
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

_source line 43 · 2026-05-14T21:32:19.634Z_

<details open><summary>🔧 Tool call — Read · `toolu_018gsdQ26mDgDbQMA4BvNao2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d753c6d5-e280-4d03-9e5f-8e72a425bc82",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BBMUVnEaph2w7XhzSD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68d0cbc8-d727-49c5-a2e6-3c946fcf0708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMsd8vqStLiWHZp9CCufNe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14147,
      "cache_read_input_tokens": 74202,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14147
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 74202,
          "cache_creation_input_tokens": 14147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14147,
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

_source line 44 · 2026-05-14T21:32:19.639Z_

<details><summary>↩ Tool result · `toolu_018gsdQ26mDgDbQMA4BvNao2`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	We present a framework for evaluating confidence signals in test-time scaling for information extraction.
4	This section formalizes the problem (\S\ref{sec:formulation}), defines five confidence signals spanning three families (\S\ref{sec:signals}), and introduces the evaluation protocol (\S\ref{sec:evaluation}).
5	
6	\subsection{Problem Formulation}\label{sec:formulation}
7	
8	Given a language model $\mathcal{M}$ and an input instance $x$, we independently sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$.
9	Each $y_i$ is a structured extraction result---an entity set for NER or a relation set for RE---produced via constrained decoding \cite{willard2023guided} to ensure valid output structure.
10	Our goal is to define a confidence signal $c$ that serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among the $N$ candidates.
11	
12	A key distinction underlies this framework.
13	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct ranking of the $N$ candidates.
14	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
15	Instance-level signals can estimate overall prediction reliability but do not inherently rank individual samples.
16	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
17	
18	Table~\ref{tab:notation} summarizes our notation.
19	
20	\begin{table}[h]
21	\centering
22	\small
23	\begin{tabular}{cl}
24	\toprule
25	Symbol & Meaning \\
26	\midrule
27	$\mathcal{M}$ & Language model \\
28	$x$ & Input instance \\
29	$y_i$ & $i$-th stochastic sample \\
30	$N$ & Number of samples \\
31	$T$ & Sampling temperature \\
32	$c(\cdot)$ & Confidence signal \\
33	SJ & Soft Jaccard similarity \\
34	FK & Fleiss' $\kappa$ \\
35	EM & Exact-match voting rate \\
36	\bottomrule
37	\end{tabular}
38	\caption{Notation used throughout the paper.}
39	\label{tab:notation}
40	\end{table}
41	
42	\subsection{Confidence Signals}\label{sec:signals}
43	
44	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
45	
46	\paragraph{Log-probability (model-internal, per-sample).}
47	The only per-sample signal in our comparison.
48	For a sample $y_i$ consisting of tokens $t_1, \ldots, t_{|y_i|}$, we define:
49	\begin{equation}\label{eq:logprob}
50	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
51	\end{equation}
52	This is the length-normalized mean log-likelihood, reflecting the model's internal confidence in its generation.
53	Because it scores each sample independently, it can directly rank the $N$ candidates for sample selection.
54	
55	\paragraph{Exact match voting (surface, instance-level).}
56	Following self-consistency \cite{wang2023selfconsistency}, we measure pairwise agreement across samples at the string level:
57	\begin{equation}\label{eq:em}
58	c_{\text{em}}(x) = \frac{1}{\binom{N}{2}} \sum_{i<j} \mathbb{1}[y_i = y_j]
59	\end{equation}
60	Equivalently, this can be expressed as the majority fraction $\max_y |\{i : y_i = y\}| / N$.
61	EM treats entire outputs as atomic units: two samples either match exactly or not, with no notion of partial overlap.
62	
63	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
64	We adapt the inter-rater agreement measure of \citet{fleiss1971agreement} by treating the $N$ samples as independent annotators, token positions as items, and the token vocabulary as the set of categories:
65	\begin{equation}\label{eq:fk}
66	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
67	\end{equation}
68	where $\bar{P}$ is the observed agreement rate across token positions and $\bar{P}_e$ is the agreement expected by chance.
69	Unlike EM, FK captures partial agreement---two samples that share most tokens but differ in a few positions receive a high score.
70	However, FK operates at the string level and does not account for the structure of the extracted output.
71	
72	\paragraph{Soft Jaccard (structural, instance-level).}
73	Our core structural signal extends Jaccard similarity \cite{jaccard1901distribution} to operate on extracted entity or relation \textit{sets} rather than raw strings.
74	For two samples $y_i$ and $y_j$, we first group extractions by entity type.
75	Within each group, we compute a bipartite matching using the Hungarian algorithm with span overlap as the similarity metric.
76	The pairwise Soft Jaccard score is:
77	\begin{equation}\label{eq:sj}
78	\text{SJ}(y_i, y_j) = \frac{|M|}{\max(|A_i|, |A_j|)}
79	\end{equation}
80	where $|M|$ is the number of matched extraction pairs and $|A_i|$, $|A_j|$ are the extraction counts of each sample.
81	The instance-level signal averages over all sample pairs:
82	\begin{equation}\label{eq:sj_instance}
83	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i<j} \text{SJ}(y_i, y_j)
84	\end{equation}
85	Two design choices distinguish SJ from surface signals.
86	First, type-aware grouping prevents spurious matches between extractions of different entity types.
87	Second, span-overlap matching tolerates near-synonym variations (e.g., ``machine learning'' vs.\ ``ML''), which would be penalized by exact string comparison.
88	
89	\paragraph{Entity voting confidence (structural, instance-level).}
90	While SJ compares entire extraction sets, entity voting operates at the granularity of individual extractions.
91	For each entity $e$ appearing in the union $E_\cup$ of all $N$ samples, we compute its frequency:
92	\begin{equation}\label{eq:freq}
93	\text{freq}(e) = \frac{|\{i : e \in y_i\}|}{N}
94	\end{equation}
95	The instance-level confidence is the mean frequency across all observed entities:
96	\begin{equation}\label{eq:voting}
97	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
98	\end{equation}
99	This adapts majority voting \cite{wang2023selfconsistency} from discrete answer selection to set-valued extraction.
100	Entities that appear consistently across samples contribute high frequency; hallucinated or idiosyncratic extractions that appear in only one or two samples pull the score down.
101	This per-entity granularity enables the signal to distinguish instances where the model reliably extracts a core set of entities (high $c_{\text{vote}}$) from those where extractions vary widely across samples (low $c_{\text{vote}}$).
102	
103	\subsection{Evaluation Framework}\label{sec:evaluation}
104	
105	We assess confidence signals along two complementary dimensions.
106	
107	\paragraph{Quality estimation.}
108	Quality estimation asks: \textit{for which instances does the model produce reliable outputs?}
109	We measure rank correlation between the confidence signal and instance-level F1 via Spearman $\rho$ and Kendall $\tau$.
110	For binary discrimination, we compute AUROC by classifying instances as above or below median F1.
111	These metrics evaluate whether a signal can identify reliable vs.\ unreliable predictions without access to gold labels.
112	
113	\paragraph{Sample selection.}
114	Sample selection asks: \textit{given $N$ candidates for a single instance, which one is best?}
115	We report best-of-$N$ F1: for each instance, the signal selects one sample, and we compute micro F1 over all instances.
116	We compare against an \textit{oracle} (which always selects the highest-F1 sample) and a \textit{greedy baseline} ($T{=}0$, $N{=}1$).
117	Per-sample signals like log-probability directly rank the $N$ candidates.
118	Instance-level signals (SJ, FK, EM, Voting) produce a single score per instance and thus require an auxiliary strategy for sample selection---we select the sample closest to the consensus output, i.e., the one with highest average pairwise similarity to all other samples.
119	
120	\paragraph{The two dimensions are complementary, not redundant.}
121	A signal with high rank correlation accurately predicts relative instance difficulty, making it useful for quality-aware routing or selective prediction.
122	However, high correlation does not guarantee effective sample selection: if per-sample variance is low---the model produces $N$ similar outputs for a given input---even a perfect quality estimator cannot distinguish among near-identical candidates.
123	We investigate this decoupling empirically in \S\ref{sec:selection_gap}.
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68d0cbc8-d727-49c5-a2e6-3c946fcf0708",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "d2c80ed4-427c-4bf6-ab1b-0a2ee313584d",
  "sourceToolAssistantUUID": "68d0cbc8-d727-49c5-a2e6-3c946fcf0708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-14T21:32:22.711Z_

Now I have a thorough understanding of the paper. Let me also check the dream review reports for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2c80ed4-427c-4bf6-ab1b-0a2ee313584d",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BBiy4TLWdyHaems9bq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4de7313-2543-45fa-9993-4e6108d71daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5vZoiaEcGvreEsoDsPTVT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2804,
      "cache_read_input_tokens": 88349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2804,
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

_source line 46 · 2026-05-14T21:32:23.725Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TwUisgceD9tYSzh7xUvPRy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/best/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4de7313-2543-45fa-9993-4e6108d71daa",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BBiy4TLWdyHaems9bq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcb9833e-bec3-484c-9e73-bb7d2db9f2ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5vZoiaEcGvreEsoDsPTVT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2804,
      "cache_read_input_tokens": 88349,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2804
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 88349,
          "cache_creation_input_tokens": 2804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2804,
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

_source line 47 · 2026-05-14T21:32:23.732Z_

<details><summary>↩ Tool result · `toolu_01TwUisgceD9tYSzh7xUvPRy`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{multirow}
7	\usepackage{xcolor}
8	\usepackage{pgfplots}
9	\pgfplotsset{compat=1.17}
10	\usepackage{hyperref}
11	\usepackage[capitalise]{cleveref}
12	\usepackage{subcaption}
13	\usepackage{enumitem}
14	
15	\definecolor{structblue}{RGB}{31,119,180}
16	\definecolor{logprobred}{RGB}{214,39,40}
17	\definecolor{surfacegray}{RGB}{127,127,127}
18	\definecolor{oraclegreen}{RGB}{44,160,44}
19	
20	\title{Structural Self-Consistency for Quality Estimation\\in LLM-Based Information Extraction}
21	
22	\author{Anonymous}
23	\date{}
24	
25	\begin{document}
26	\maketitle
27	
28	% ============================================================
29	% ABSTRACT
30	% ============================================================
31	\begin{abstract}
32	Large language models increasingly tackle structured information extraction (IE) via multi-sample generation, yet practitioners lack principled guidance on which confidence signals to trust---and for what purpose.
33	We systematically compare five unsupervised confidence signals spanning four families---model confidence (log-probability), surface agreement (Fleiss' $\kappa$, exact match), set-aware structural similarity (Soft Jaccard), and entity-level majority voting---for named entity recognition (NER) and relation extraction (RE) across two models (Qwen3-8B, LLaMA-3.1-8B) and two datasets (SciERC, CoNLL-2003).
34	We report three findings.
35	\textbf{(1)}~Structural consistency signals provide the strongest unsupervised quality estimation: entity voting achieves AUROC 0.73 and $\rho{=}0.50$ on NER, substantially outperforming log-probability (AUROC 0.56, $\rho{=}0.14$).
36	\textbf{(2)}~A \emph{correlation--selection gap} exists: despite strong instance-level correlation, no unsupervised signal beats greedy decoding for NER best-of-$N$ selection; only log-probability enables selection on RE (+2.4pp).
37	\textbf{(3)}~All signals degrade on relational tasks due to compound error propagation, but remain valid within the model's capability range.
38	These results hold across a $2{\times}2$ model--dataset matrix ($|\Delta\rho|{\le}0.006$ cross-model) and three random seeds ($\sigma_\rho{\le}0.008$).
39	Our findings disentangle quality estimation from sample selection and provide actionable guidance for deploying multi-sample IE systems.
40	\end{abstract}
41	
42	% ============================================================
43	% 1. INTRODUCTION
44	% ============================================================
45	\section{Introduction}
46	
47	Multi-sample generation---drawing $N$ candidate outputs from a language model and selecting or aggregating among them---has become a standard tool for improving LLM performance on reasoning tasks~\cite{wang2023selfconsistency,snell2024scaling,brown2024tts}.
48	For structured information extraction (IE), where outputs are entity sets or relation tuples, the natural question is: \emph{which confidence signal should guide the selection or abstention decision?}
49	
50	This question is more nuanced than it appears.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcb9833e-bec3-484c-9e73-bb7d2db9f2ab",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "c1114d5b-40c3-457b-896d-bc43582e9819",
  "sourceToolAssistantUUID": "dcb9833e-bec3-484c-9e73-bb7d2db9f2ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-14T21:32:26.882Z_

I now have sufficient material to write a thorough review. Let me also check the `paper_checklist.yaml` for any additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1114d5b-40c3-457b-896d-bc43582e9819",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BC2CQVhFbQ5xYCDkxo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98508ffd-9b72-4b75-9bf9-d99e4ba05cf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEeZq1QY4cQLtQa5M85MV3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 91153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1099,
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

_source line 49 · 2026-05-14T21:32:27.572Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019PfFcfW14PoppXLBqRfmx5`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98508ffd-9b72-4b75-9bf9-d99e4ba05cf0",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BC2CQVhFbQ5xYCDkxo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c11cdef9-0f8b-4674-9732-fd4e677017f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEeZq1QY4cQLtQa5M85MV3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 91153,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1099
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 91153,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1099,
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

_source line 50 · 2026-05-14T21:32:27.586Z_

<details><summary>↩ Tool result · `toolu_019PfFcfW14PoppXLBqRfmx5`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c11cdef9-0f8b-4674-9732-fd4e677017f0",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "4c5bc6fa-188d-47a4-9ee2-3acc1460f4cb",
  "sourceToolAssistantUUID": "c11cdef9-0f8b-4674-9732-fd4e677017f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-14T21:32:30.381Z_

Now let me submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c5bc6fa-188d-47a4-9ee2-3acc1460f4cb",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BCJrGDiy5t6UFqUqLx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "008c6ada-9818-4786-8501-f6aa489867d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJiGVRZ3RWB3jZeeaaFYUe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 92252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 202,
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

_source line 52 · 2026-05-14T21:32:30.926Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KFfsCW2bAZ7S898bpvPV67`</summary>

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
  "parentUuid": "008c6ada-9818-4786-8501-f6aa489867d1",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BCJrGDiy5t6UFqUqLx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b31b5a13-48da-4e3f-bf03-196a1f020bf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJiGVRZ3RWB3jZeeaaFYUe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 92252,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 202
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 92252,
          "cache_creation_input_tokens": 202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 202,
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

_source line 53 · 2026-05-14T21:32:30.928Z_

<details><summary>↩ Tool result · `toolu_01KFfsCW2bAZ7S898bpvPV67`</summary>

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
  "parentUuid": "b31b5a13-48da-4e3f-bf03-196a1f020bf8",
  "isSidechain": true,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "agentId": "a3d7f21605785749c",
  "type": "user",
  "uuid": "28eb8bd9-420d-4c0c-987d-e2d9a0dfab79",
  "sourceToolAssistantUUID": "b31b5a13-48da-4e3f-bf03-196a1f020bf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-14T21:33:54.551Z_



Now I have all the material needed. Let me write the review directly.

---

## Review: "Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation-Selection Gap"

**Reviewer R2 — Focus: Novelty and Related Work**

---

### 1. Summary

This paper compares five unsupervised confidence signals (log-probability, exact match, Fleiss' kappa, Soft Jaccard, entity voting) for quality estimation and best-of-N selection in LLM-based information extraction (NER and RE). The central finding is a "correlation-selection gap": structural consistency signals strongly predict instance-level quality (voting rho=0.50, AUROC=0.73 on NER) but fail to improve best-of-N selection over greedy decoding on NER, with only log-probability helping on RE (+2.3pp). The paper attributes this to the instance-level nature of consistency signals, which cannot discriminate among N candidates for a single input.

### 2. Strengths

**S1. The quality estimation vs. selection disentanglement is well-executed.** The paper cleanly separates two objectives that are indeed conflated in much prior work on self-consistency. The experimental demonstration across 2 models x 2 datasets is thorough, and the method section (Section 2) formalizes the per-sample vs. instance-level signal distinction clearly. This separation is the paper's strongest conceptual contribution.

**S2. Comprehensive related work, given the revised draft.** The related work section is well-organized into three subsections (self-consistency/TTS, consistency for structured IE, uncertainty/calibration) and covers the relevant 2024-2026 literature with appropriate depth. The positioning against Nedellec & Xia (2026) is explicit and fair, identifying three concrete gaps (surface matching only, no selection analysis, single domain). The coverage of CISC, Self-Certainty, ReASC, and CoCoA situates the work within the broader TTS landscape. The conformal prediction, token-level NER uncertainty, and verifier/reward model threads are appropriately included as related paradigms.

**S3. Honest reporting of negative results and method boundaries.** The WNUT-17 analysis (54% zero F1, SJ rho=0.062 not significant, logprob negative correlation) is reported transparently as a capability boundary rather than buried. The task-difficulty-dependent signal ranking (EM leads on easy tasks, SJ on hard tasks) is a nuanced finding that avoids overclaiming a universal winner.

**S4. The task-difficulty-dependent signal ranking is a genuine empirical contribution.** The observation that EM > SJ on CoNLL but SJ > EM on SciERC, with convergence when model capability is insufficient, provides actionable guidance. This is more informative than a simple "our metric wins" narrative.

### 3. Weaknesses

**W1. The "correlation-selection gap" explanation is close to tautological once stated.** The paper's central conceptual contribution — that instance-level aggregates cannot rank individual samples — is presented as a discovery, but it follows almost directly from the definition. An instance-level signal c_il: (x, {y_i}) -> R produces one number per input; it *cannot* rank N candidates by construction. The paper acknowledges this in Section 2 ("instance-level signals... do not inherently rank individual samples") but then treats the empirical confirmation as a major finding. The genuine surprise would be if instance-level signals *did* help selection (e.g., by identifying easy instances where random selection suffices). The fact that they don't is the expected null result. What is mildly interesting is that even the consensus-closest-sample selection strategy fails, but this is underexplored — the paper devotes only one sentence to how instance-level signals are adapted for selection (Section 2.3: "we select the sample closest to the consensus output").

This weakness is significant for novelty assessment. The conceptual contribution reduces to: (a) instance-level signals can't rank samples (definitional), and (b) log-probability, the only per-sample signal, helps on RE but not NER (a single empirical observation). Neither alone meets the novelty bar for a top venue.

**W2. Insufficient differentiation from Nedellec & Xia (2026).** The paper argues three differences: structural metrics vs. surface matching, best-of-N analysis, and multi-domain evaluation. However:
- The structural metrics (SJ, voting) are relatively straightforward extensions of Jaccard similarity and frequency counting to entity sets. The Hungarian matching with span overlap is a reasonable design choice but not technically novel.
- The best-of-N analysis yields a negative result (no signal beats greedy on NER), which, combined with W1, amounts to showing that something definitionally incapable of ranking samples indeed fails to rank samples.
- The multi-domain evaluation is valuable but incremental.

The paper reads as "Nedellec & Xia (2026) + better metrics + negative selection result." The SJ metric itself is the main technical delta, and it is not a major methodological contribution — it is a sensible instantiation of set similarity that one would naturally try.

**W3. No proposed solution or path forward beyond "use trained verifiers."** The paper identifies a gap and stops. The conclusion lists future work (trained verifiers, conformal prediction, larger models) but does not even attempt a preliminary solution. For a top venue, a pure negative-result paper needs either (a) a very surprising negative result, or (b) deep mechanistic understanding that enables future solutions. The explanation here ("instance-level signals can't rank samples") is shallow — it does not explain *why* the consensus-closest strategy fails, whether per-sample structural signals could be constructed, or what properties a successful selector would need. The oracle headroom analysis (NER +16pp, RE +19pp) tantalizes but receives no further investigation.

**W4. The contribution is positioned ambiguously between "systematic comparison" and "novel finding."** The paper's title and framing emphasize the correlation-selection gap as a novel finding, but the bulk of the experimental content is a systematic comparison of five signals. Systematic comparisons are valuable but are typically positioned as resource papers or Findings-level contributions unless they reveal unexpected phenomena. The unexpected phenomenon here (the gap) is, per W1, close to expected once the signal taxonomy is laid out. The paper would be strengthened by committing to one framing: either a rigorous systematic comparison (in which case, more signals, datasets, and models would be expected) or a mechanistic analysis of the gap (in which case, deeper investigation is needed).

**W5. Missing related work on minimum Bayes risk (MBR) decoding for structured prediction.** MBR decoding — selecting the sample that maximizes expected utility against the other samples — is the natural approach when you have N samples and a utility function. The paper's SJ metric could be directly used as a utility function in MBR, selecting argmax_i sum_j SJ(y_i, y_j) rather than just computing the mean. This is mentioned obliquely ("closest to consensus") but not connected to the MBR literature (Eikema & Aziz 2020, 2022; Freitag et al. 2022, 2023). The MBR framing would also clarify why instance-level signals fail: MBR selects the sample closest to the "center" of the distribution, which is a per-sample ranking. If MBR-with-SJ also fails, that is a much stronger negative result. If it succeeds, it resolves the gap. Either way, omitting this connection is a significant gap in the related work.

**W6. The "logprob paradox" (high AUROC, low rho) is not deeply analyzed.** This is presented as a paradox but has a straightforward explanation: logprob produces a bimodal distribution (high confidence for easy instances, low for hard) that separates classes well (AUROC) but provides poor ranking within each mode (rho). This is a well-known property of miscalibrated classifiers (Guo et al. 2017). Presenting it as a novel observation overstates the contribution.

### 4. Questions for Authors

**Q1.** For best-of-N selection with instance-level signals, you use "the sample closest to the consensus output" (Section 2.3). This is effectively MBR decoding with SJ as the utility function. Did you also try other per-sample adaptations of instance-level signals, such as leave-one-out SJ (the SJ of sample i against the remaining N-1)? If so, what were the results? If not, why not — this seems like the most natural per-sample structural signal.

**Q2.** The oracle headroom on NER is +16pp. Can you characterize which instances contribute to this headroom? Specifically, for oracle-selected samples, does the oracle choose samples that are structurally different from the consensus (suggesting that consensus-based selection is fundamentally wrong) or samples that are close to the consensus but slightly better (suggesting that finer-grained discrimination is needed)?

**Q3.** You report that "within-stratum correlations approach zero for all signals" (Discussion). This is a strong claim. Can you provide the actual numbers and confidence intervals? If true, this means confidence signals have *zero* discriminative power conditional on difficulty — but this seems to conflate "difficulty stratum" (defined by greedy F1) with "confidence stratum" (defined by the signal), which are correlated but not identical.

**Q4.** The paper title in the submission summary mentions "Why Self-Consistency Fails" but the actual paper title is different ("Strong Predictors, Weak Selectors"). Which is the intended title? The "fails" framing is stronger and more specific but also more misleading — self-consistency does not fail for quality estimation.

**Q5.** Why is Fleiss' kappa computed at the token level rather than the entity level? Entity-level FK (treating each entity type as a category and each sample as a rater) would be more naturally comparable to the structural signals and might narrow the structural-surface gap.

### 5. Minor Issues

- Table 2 (selection): EM shows "---" entries. The text explains this is because "EM produces binary agreement without sample ranking," but binary agreement can still be used for selection (select any sample from the majority cluster, or random among all when EM=0). This should be clarified or EM should be included with a random-within-majority strategy.

- The paper mentions WNUT-17 in the abstract and experimental setup as a third dataset but it contributes only a single paragraph of negative results (Section 4.3). Listing it as a primary dataset overstates its role; it would be more accurately described as a "probe" or "boundary case."

- Section 4.3 reports "Fisher's z-test on rho_SJ yields z=2.31, p=0.021" for NER vs. RE comparison. This tests whether two correlations differ, but the NER and RE evaluations are on overlapping instances (SciERC has joint NER/RE annotations), so the independence assumption of Fisher's z-test is violated. A permutation test or bootstrap comparison would be more appropriate.

- The paper uses "three families" (structural, surface, model-internal) in the main text but the paper_framing.md and dream reports reference "four families." This inconsistency should be resolved.

- ECE is mentioned once (Section 4.3: "SJ also achieves the lowest calibration error (ECE = 0.075-0.102)") but no reliability diagrams or calibration analysis is presented despite being referenced. If ECE is claimed, it needs methodological support (bin size, how F1-based ECE is defined for continuous outputs).

- The notation table (Table 1) is unnecessary and consumes space. The symbols are standard and self-explanatory.

### 6. Overall Assessment

The paper presents a competent empirical comparison of confidence signals for LLM-based information extraction, with thorough experimental coverage (2 models, 2+ datasets, 3 seeds, 2 sample sizes). The quality estimation results are solid and practically useful. However, the central novelty claim — the correlation-selection gap — is close to tautological for instance-level signals and only mildly surprising for log-probability on NER. The lack of any proposed solution, combined with the straightforward nature of the metrics (Jaccard similarity, frequency voting) and the close proximity to Nedellec & Xia (2026), places this below the acceptance threshold for a top venue main track. The work would be appropriate for Findings, where the systematic comparison and honest negative results would be valued without requiring the novelty bar of the main conference.

### 7. Scores

- **Overall**: 3 (Weak Reject)
- **Confidence**: 4 (High — I have read the paper carefully and am familiar with the relevant literature on self-consistency, uncertainty estimation, and structured prediction confidence)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28eb8bd9-420d-4c0c-987d-e2d9a0dfab79",
  "isSidechain": true,
  "agentId": "a3d7f21605785749c",
  "requestId": "req_011Cb3BCYzKNq3bkZMWidu1k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b431401d-15fa-4287-a185-4b8c182e262d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQBwqk6DM7CwnraoZhFSqm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 675,
      "cache_read_input_tokens": 92454,
      "output_tokens": 3004,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 675
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3004,
          "cache_read_input_tokens": 92454,
          "cache_creation_input_tokens": 675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 675,
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
