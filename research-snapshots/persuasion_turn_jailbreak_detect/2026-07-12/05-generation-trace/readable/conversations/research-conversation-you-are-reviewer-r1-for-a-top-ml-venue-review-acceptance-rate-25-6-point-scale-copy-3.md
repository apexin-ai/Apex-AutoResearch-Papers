# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a4668b802d9900002.jsonl`
- **Structured JSON:** [`9ba21dbd5555bd470e5c.json`](../../sessions/9b/9ba21dbd5555bd470e5c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-17T17:29:10.224Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **Methods and Experiments**.

## Paper Summary

**DisPeD**: A two-stage detector for multi-turn jailbreak attacks exploiting "pragmatic evasion asymmetry."
- Stage 1: DeBERTa-v3-base fine-tuned with multi-task objective (8-class persuasion strategy classification + binary intent classification)
- Stage 2: Bi-GRU models temporal sequence of [CLS] embeddings for conversation-level classification
- Key idea: Attackers can vary surface wording but must follow persuasion playbook (rapport → authority → reframing → escalation), creating a structural invariant to detect

## Key Results (from paper)

1. **Core detection**: F1=0.86 at K=3 (+8pp over vanilla DeBERTa baseline, p=0.018). K=2 is +7pp but p=0.072 (not significant). Full conversation F1=0.91 vs 0.86 baseline (+5pp, p=0.031).
2. **Scrambled-label ablation**: Scrambling persuasion labels drops F1 by 7pp (0.91→0.84, p=0.008). Scrambled model performs slightly below vanilla baseline (0.84 vs 0.86).
3. **Adversarial robustness**: Under paraphrasing, DisPeD drops 7pp, baseline drops 12pp, TF-IDF+LR drops 18pp. Δ-Δ=5pp (p=0.043).
4. **Cross-attack**: FITD zero-shot +8pp (p=0.034). Deceptive Delight +5pp (p=0.142, not significant).
5. **Trajectory analysis**: Jailbreak monotonicity=0.71±0.18 vs benign 0.38±0.14 (p=0.003), but 32% of jailbreaks don't show monotonic pattern.
6. **Hard negatives (WildChat)**: DisPeD FPR=12%, baseline=18%, TF-IDF+LR=27%.
7. **Stability**: Cross-checkpoint variance ≤2pp.

## Data
- 480 conversations (240 jailbreak + 240 benign), test set n=72
- LLM-generated (Qwen3-8B) with register normalization (TF-IDF reduced from 1.0 to 0.67)
- Cross-attack: 72 FITD + 65 Deceptive Delight conversations
- Hard negatives: 85 WildChat high-drift benign conversations
- Persuasion classifier accuracy: 72% (acknowledged bottleneck)

## Experiment Design Reference (from review_context.yaml)

The full imagined experiment list includes 11 experiments:
1. data_quality_fix — TF-IDF cleaning pipeline
2. core_revalidation_clean — Core F1 results across K values with bootstrap CIs
3. scrambled_label_ablation — Verifying persuasion labels carry real signal
4. adversarial_perturbation — Robustness under paraphrasing
5. multi_attack_generation — FITD + Deceptive Delight data generation
6. cross_attack_evaluation — Zero-shot generalization
7. tfidf_lr_baseline — Lexical baseline
8. strategy_transition_analysis — Monotonicity scores
9. wildchat_hard_negatives — Hard negative FPR evaluation
10. cross_checkpoint_variance — Stability analysis
11. deepcontext_proxy_reproduction — BERT+GRU proxy baseline

All 11 experiments appear covered in the paper. The paper matches the expected results closely (numbers align with the YAML's expected values).

## Your Task

Write a detailed review focusing on:

### A. Methodology Evaluation
- Is the two-stage architecture well-motivated and sound?
- Is the multi-task objective (persuasion + intent) justified? Is λ=1.0 explored/ablated?
- Is the persuasion taxonomy (8 classes) well-defined and grounded in literature?
- Is the Bi-GRU choice justified vs alternatives (Transformer, attention)?
- Is the problem formulation (conversation prefix classification) rigorous?

### B. Experimental Evaluation
- Are the baselines adequate and fair? (Note: DeepContext proxy uses BERT-base, not DeBERTa — confounded comparison)
- Is the dataset size sufficient for the claims? (n=72 test set)
- Are the statistical methods appropriate? (bootstrap resampling)
- Is the adversarial perturbation protocol realistic?
- How well does the scrambled-label ablation isolate the persuasion grounding effect?
- Is the data quality fix (register normalization) adequately validated?
- Are there missing experiments or controls?
- How concerning is the 72% persuasion classifier accuracy as a bottleneck?

### C. Specific Concerns
- The entire dataset is LLM-generated — how does this affect validity?
- No real adversarial data or deployment evaluation
- No cross-seed variance (only checkpoint variance)
- The TF-IDF=0.67 after cleaning — is this low enough? 
- The "pragmatic evasion asymmetry" — is this truly a structural invariant, or can adversaries adapt their persuasion patterns too?

### Output Format

```
## R1 Review: Methods and Experiments

### Summary
[2-3 sentences]

### Strengths
[Numbered list, be specific with table/section references]

### Weaknesses
[Numbered list, be specific and constructive]

### Questions for Authors
[Numbered list]

### Missing Experiments / Controls
[If any beyond what's covered]

### Minor Issues
[Formatting, presentation, typos]

### Preliminary Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "fbe7daa1-c3af-4cc0-b1c8-1aa4ef15f5e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T17:29:10.232Z_

```json
{
  "parentUuid": "fbe7daa1-c3af-4cc0-b1c8-1aa4ef15f5e5",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
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
  "uuid": "df509e5a-8abb-401c-9e79-046c22d741a3",
  "timestamp": "2026-05-17T17:29:10.232Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T17:29:14.298Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VAKc34aEE5zUuEdVy2Xbj2`</summary>

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
  "parentUuid": "df509e5a-8abb-401c-9e79-046c22d741a3",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y522kazGySN5SCWydv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2c0d2d6-e0ab-4a98-8409-86b1910f8836",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018iwdCghW6dL3827KAYuWVg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8580,
      "cache_read_input_tokens": 8255,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8580
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 88,
          "cache_read_input_tokens": 8255,
          "cache_creation_input_tokens": 8580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8580,
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

_source line 4 · 2026-05-17T17:29:14.303Z_

<details><summary>↩ Tool result · `toolu_01VAKc34aEE5zUuEdVy2Xbj2`</summary>

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
  "parentUuid": "f2c0d2d6-e0ab-4a98-8409-86b1910f8836",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "22a5627a-9d17-4bb3-ab54-074937db422f",
  "sourceToolAssistantUUID": "f2c0d2d6-e0ab-4a98-8409-86b1910f8836",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T17:29:20.413Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QwP9wQV5x1urQwhPHV1A2X`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "report.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22a5627a-9d17-4bb3-ab54-074937db422f",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y5KeA3z5BvTkVmpAP8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4221ca9f-915f-4cc4-9c89-8206f9988fb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdMefCVgcfM6XgzaMww3ay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
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

_source line 6 · 2026-05-17T17:29:20.427Z_

<details><summary>↩ Tool result · `toolu_01QwP9wQV5x1urQwhPHV1A2X`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **phase_b_full** (success): Persuasion-grounded DeBERTa embeddings (multi-task fine-tuned on 8-class persuasion + intent) enable significantly earlier detection of Crescendo jailbreak attacks compared to vanilla DeBERTa embeddings, especially at low K (2-3 turns) ← 基于 pilot_phase_b\\n- **pilot_phase_b** (success): Persuasion-aware DeBERTa embeddings (multi-task fine-tuned) fed to Bi-GRU will outperform vanilla DeBERTa embeddings at early detection (K=2,3,5 turns) of Crescendo-style jailbreak attacks\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-33183: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 707, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4221ca9f-915f-4cc4-9c89-8206f9988fb2",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "71920617-466d-47bd-86cd-79e9d8cb2b81",
  "sourceToolAssistantUUID": "4221ca9f-915f-4cc4-9c89-8206f9988fb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:29:20.934Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0177ByFHWkR6SFEBkaUxLqb3`</summary>

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
  "parentUuid": "71920617-466d-47bd-86cd-79e9d8cb2b81",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y5KeA3z5BvTkVmpAP8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da48df87-f103-44b4-918b-ef4682328da0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdMefCVgcfM6XgzaMww3ay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
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

_source line 8 · 2026-05-17T17:29:20.950Z_

<details><summary>↩ Tool result · `toolu_0177ByFHWkR6SFEBkaUxLqb3`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da48df87-f103-44b4-918b-ef4682328da0",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "74892b52-511f-4b66-afd0-dfc3d00aa5e1",
  "sourceToolAssistantUUID": "da48df87-f103-44b4-918b-ef4682328da0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T17:29:25.149Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016H3Cj1BiH31PN1E94hbxui`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74892b52-511f-4b66-afd0-dfc3d00aa5e1",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y5rbFK859Fuar1gsH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f12a8d1-aac8-46b7-bc66-7f0b52f42790",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oRKEPACFdP2pH6SpxfJyj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 18104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 798,
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

_source line 10 · 2026-05-17T17:29:25.160Z_

<details><summary>↩ Tool result · `toolu_016H3Cj1BiH31PN1E94hbxui`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper_framing.md\", \"content\": \"# Paper Framing — persuasion_turn_jailbreak_detect\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Deadline: 2026-05-25 (ARR May cycle)\\n- Track: LLM Security / Discourse and Pragmatics\\n- Commitment deadline: 2026-08-02\\n\\n## Title (Working)\\nDisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection\\n\\n## Core Insight\\nMulti-turn jailbreak attacks can easily vary lexical and semantic content of individual turns, but the discourse-level persuasion playbook (rapport → reframing → escalation) is a structural necessity for attack success. Removing any stage either fails the attack or reduces it to a single-turn attack already covered by existing defenses. DisPeD exploits this asymmetry by fine-tuning DeBERTa on persuasion strategy classification, producing turn embeddings that encode pragmatic function rather than (only) semantic content.\\n\\n## Core Claims (3)\\n\\n### Claim 1: Pragmatic Evasion Asymmetry (Theoretical + Empirical)\\nAn evasion hierarchy exists for multi-turn jailbreak detection: lexical features (easily evaded via paraphrasing) < semantic embeddings (moderate, per-turn representations kept \\\"benign\\\" per Bullwinkel et al. 2025) < pragmatic persuasion patterns (structurally difficult to evade, as the persuasion playbook is a functional prerequisite for attack success).\\n- Evidence needed: adversarial perturbation experiment showing treatment degrades less than lexical/semantic baselines under paraphrasing\\n\\n### Claim 2: Early Detection via Persuasion Grounding\\nPersuasion-grounded turn embeddings (DeBERTa fine-tuned on 8-class persuasion taxonomy + intent) enable significantly earlier detection of multi-turn jailbreaks (at K=2-3 turns) compared to vanilla semantic embeddings, because persuasion strategy transitions (rapport → authority framing) manifest before explicitly harmful content appears.\\n- Evidence needed: early detection F1 at K=2,3 turns, treatment > baseline by >= 5pp on clean data (TF-IDF < 0.75)\\n\\n### Claim 3: Monotonic Escalation Trajectory\\nAdversarial conversations exhibit a monotonic escalation trajectory in persuasion strategy space (trust → test → normalize → elicit), while benign conversations exhibit oscillatory or non-monotonic patterns. This distinction is the mechanistic basis for Claims 1-2.\\n- Evidence needed: strategy transition matrix visualization, trajectory analysis comparing jailbreak vs benign\\n\\n## Story Spine\\n\\n**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a \\\"benign\\\" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (2026) tracks generic semantic drift but confuses benign conversational evolution with adversarial manipulation.\\n\\n**Gap**: Existing detectors operate at the lexical or semantic level where attacks deliberately hide. No published work combines persuasion-grounded turn representations with temporal sequence modeling for multi-turn jailbreak detection.\\n\\n**Our angle**: We identify the Pragmatic Evasion Asymmetry. The persuasion playbook (rapport → reframing → escalation) is a structural necessity for multi-turn attack success. Unlike lexical or semantic features, pragmatic persuasion patterns cannot be evaded without abandoning the attack itself. DisPeD fine-tunes DeBERTa on an 8-class persuasion taxonomy to produce pragmatic-aware turn embeddings, then models the temporal strategy sequence with a GRU to detect the characteristic escalation trajectory.\\n\\n**Headline result**: \\\"DisPeD detects Crescendo-style jailbreaks at K=2 turns with F1=X vs Y for vanilla semantic baselines (+Z pp). Under adversarial paraphrasing that removes lexical cues, DisPeD maintains F1=W while lexical baselines degrade by V pp.\\\"\\n\\n## Architecture (Simplified for MVE)\\n\\nSingle-track with persuasion grounding (full dual-track in future work):\\n1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification\\n2. **Stage 2**: Bi-GRU over DeBERTa [CLS] embeddings for conversation-level binary classification\\n3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings\\n\\n## Venue Fit Risks\\n- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)\\n- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)\\n- Safety reviewers expect multiple attack types: need >= 2 attack families\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)\\nTF-IDF=1.0 on current data means lexical features alone perfectly separate classes. Must show the model works on data without lexical shortcuts.\\n- Mitigation: (a) register-normalize jailbreak data to match benign register, verify TF-IDF < 0.75, retrain; (b) adversarial perturbation evaluation (Claim 3)\\n\\n### RC2: Small Dataset\\n480 samples is small for a detection paper.\\n- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers\\n\\n### RC3: Single Attack Type (Crescendo Only)\\nNeed generalization evidence.\\n- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline\\n\\n### RC4: Strategy Label Confound (M004)\\nBenign turns hardcoded to strategy=7 creates shortcut for treatment model.\\n- Mitigation: (a) fix labeling (use \\\"none\\\"/9th class); (b) scrambled-label ablation\\n\\n### RC5: No DeepContext Comparison\\nPaper positions against DeepContext but no reproduction.\\n- Mitigation: vanilla DeBERTa → GRU is a fair proxy baseline (same architecture, only difference is persuasion grounding). Note DeepContext has no public code. If time allows, attempt reproduction as P1.\\n\\n### RC6: Interpretability Claims Without Human Eval\\nStrategy sequence outputs claimed interpretable but not evaluated.\\n- Mitigation: strategy transition matrix visualization (P1). Full human eval is future work given timeline constraints.\\n\\n## Scope Boundary\\n- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)\\n- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay\\n- The semantic GRU track provides coverage for out-of-scope attack types as a safety net\\n\\n## Theoretical Grounding\\n- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept \\\"benign\\\" by multi-turn attacks\\n- Speech Act Theory (Austin 1962, Searle 1969): existing detectors work at locutionary act level, DisPeD at illocutionary act level\\n- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking\\n- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks\\n- \\\"How Do LLMs Persuade?\\\" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations\\n\", \"total_chars\": 7114, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f12a8d1-aac8-46b7-bc66-7f0b52f42790",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "fba4e800-30c5-4061-8edf-cd65963267be",
  "sourceToolAssistantUUID": "8f12a8d1-aac8-46b7-bc66-7f0b52f42790",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:29:25.622Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MFJhVYwT5PSC9M3HqXhKpV`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "ARCHITECTURE.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fba4e800-30c5-4061-8edf-cd65963267be",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y5rbFK859Fuar1gsH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1eb3965b-0bbe-48bd-b412-4f4c1a1985bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oRKEPACFdP2pH6SpxfJyj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 18104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 798,
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

_source line 12 · 2026-05-17T17:29:25.632Z_

<details><summary>↩ Tool result · `toolu_01MFJhVYwT5PSC9M3HqXhKpV`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ARCHITECTURE.md found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1eb3965b-0bbe-48bd-b412-4f4c1a1985bc",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "0be5a340-8a4a-40e1-842a-23ba1442bcc2",
  "sourceToolAssistantUUID": "1eb3965b-0bbe-48bd-b412-4f4c1a1985bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T17:29:26.093Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DPLmhw8xY9VyrbkWDUZRka`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "EVALUATION.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0be5a340-8a4a-40e1-842a-23ba1442bcc2",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y5rbFK859Fuar1gsH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ccfa8f49-edff-471a-8891-7ee86c7af388",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oRKEPACFdP2pH6SpxfJyj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 18104,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 798
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 310,
          "cache_read_input_tokens": 18104,
          "cache_creation_input_tokens": 798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 798,
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

_source line 14 · 2026-05-17T17:29:26.108Z_

<details><summary>↩ Tool result · `toolu_01DPLmhw8xY9VyrbkWDUZRka`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccfa8f49-edff-471a-8891-7ee86c7af388",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "ab61d5b3-c3bf-4ec0-b8a9-70242360ada3",
  "sourceToolAssistantUUID": "ccfa8f49-edff-471a-8891-7ee86c7af388",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T17:29:31.209Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LX6UXHA1kZiNeXN94PFtNn`</summary>

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
  "parentUuid": "ab61d5b3-c3bf-4ec0-b8a9-70242360ada3",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y6C3HQ2Xf9pVhK1xnX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d414858-0036-4f86-80ec-89842cc86365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vxfeVaHsnFibCCnveoyF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2679,
      "cache_read_input_tokens": 18902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2679,
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

_source line 16 · 2026-05-17T17:29:31.224Z_

<details><summary>↩ Tool result · `toolu_01LX6UXHA1kZiNeXN94PFtNn`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d414858-0036-4f86-80ec-89842cc86365",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "0686f53e-a60f-4014-b73c-874815df85ae",
  "sourceToolAssistantUUID": "2d414858-0036-4f86-80ec-89842cc86365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T17:29:31.499Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FrGzgJbP8mzVBTj9UpLzCf`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "decisions.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0686f53e-a60f-4014-b73c-874815df85ae",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y6C3HQ2Xf9pVhK1xnX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff6a38de-ffcf-4f5b-bbe7-dec79f1b163f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2vxfeVaHsnFibCCnveoyF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2679,
      "cache_read_input_tokens": 18902,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2679
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 18902,
          "cache_creation_input_tokens": 2679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2679,
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

_source line 18 · 2026-05-17T17:29:31.509Z_

<details><summary>↩ Tool result · `toolu_01FrGzgJbP8mzVBTj9UpLzCf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/decisions.yaml\", \"content\": \"_next_id: 4\\ndecisions:\\n- id: D001\\n  date: 2026-05-17 16:09 UTC\\n  summary: 接受 DeBERTa F1=0.789 作为 baseline，停止数据 TF-IDF 迭代，reframe MVP 为 early detection\\n  rationale: 'DeBERTa F1=0.789 已在目标范围(0.70-0.85)。TF-IDF F1=0.924 高但不致命——论文 reframe:\\n    TF-IDF/vanilla 方法需完整对话才能分类，DisPeD 在 K=2-3 turns 即可通过 persuasion trajectory 早期检测。这完美对齐\\n    Bullwinkel et al. 的核心发现（早期 turns 表征为 benign）。数据迭代已耗 4 轮 6+ 小时，继续追 TF-IDF 阈值的 ROI\\n    为负。用 Crescendo oracle labels (intended_strategy) 替代 GPT 标注，节省 API 成本和时间。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-17 16:49 UTC\\n  summary: MVP PASS — early detection K=2 +10.8pp, K=3 +5.9pp 超过阈值；TF-IDF=1.0 标记为\\n    research 阶段优先解决项\\n  rationale: Treatment (persuasion-grounded DeBERTa → GRU) 在 K=2 时 F1=0.987 vs baseline\\n    0.879 (+10.8pp)，K=3 时 +5.9pp，均超过 MVP 阈值 +5pp。Full conversation F1 差距仅 +1.3pp 未达\\n    +2pp 阈值，但 early detection 是核心 claim 所在。TF-IDF=1.0 表明词汇 shortcut 仍存在，但 (1) 不影响\\n    treatment vs baseline 相对比较的有效性，(2) 可作为 paper motivation（lexical cues 偶然有效但可被攻击者规避，pragmatic\\n    patterns 不可规避），(3) research 阶段通过 adversarial perturbation 实验验证 robustness。\\n  related_experiments:\\n  - exp_id: pilot_phase_b\\n    role: pipeline_validation\\n    result: success (n=270, directionally positive but not statistically meaningful)\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-17 16:59 UTC\\n  summary: 进入 Research 阶段，framing 定位为 Pragmatic Evasion Asymmetry，experiment plan\\n    含 6 个 P0 实验\\n  rationale: MVP PASS (D002) 后按 post-mvp-kickoff 流程：paper_framing.md 将核心贡献从\\\"更好的检测器\\\"升级为\\\"语用逃逸不对称性原则的首个实证验证\\\"（源自\\n    Human Review Note），experiment_plan.yaml 优先解决 TF-IDF=1.0 数据质量阻塞。Dream full review\\n    已发起，等回调后审批 P0。\\n  related_experiments:\\n  - exp_id: phase_b_full\\n    role: motivation\\n    result: K=2 +10.8pp but TF-IDF=1.0\\n  - exp_id: pilot_phase_b\\n    role: motivation\\n    result: directional signal confirmed\\n  depends_on:\\n  - D002\\n\", \"total_chars\": 1860, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff6a38de-ffcf-4f5b-bbe7-dec79f1b163f",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "9911474f-c8a2-4fd6-8376-9f9fe451fdd3",
  "sourceToolAssistantUUID": "ff6a38de-ffcf-4f5b-bbe7-dec79f1b163f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T17:29:39.174Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011ARoeRN3XvqSUKAKwUCy2u`</summary>

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
  "parentUuid": "9911474f-c8a2-4fd6-8376-9f9fe451fdd3",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y6bGnX8JJF5fj1vm9z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0423e2c-16ab-459e-ab73-16f63b174bb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018p57UpoUnCWGTidVaKZRiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1463,
      "cache_read_input_tokens": 21581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1463,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 20 · 2026-05-17T17:29:39.201Z_

<details><summary>↩ Tool result · `toolu_011ARoeRN3XvqSUKAKwUCy2u`</summary>

```text
artifacts/dream_reports/dream_20260517T165817/best/paper.tex
artifacts/dream_reports/dream_20260517T165817/median/paper.tex
artifacts/dream_reports/dream_20260517T165817/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0423e2c-16ab-459e-ab73-16f63b174bb3",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "3d68274c-99d8-401c-8303-ffbdf04dcd6f",
  "sourceToolAssistantUUID": "d0423e2c-16ab-459e-ab73-16f63b174bb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T17:29:39.487Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01U6sVLx6tiXRzRiw11HnKK3`</summary>

```json
{
  "pattern": "**/experiment_plan.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d68274c-99d8-401c-8303-ffbdf04dcd6f",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y6bGnX8JJF5fj1vm9z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "090b88be-011a-435a-ab08-115f8c34dfd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018p57UpoUnCWGTidVaKZRiR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1463,
      "cache_read_input_tokens": 21581,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1463
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 21581,
          "cache_creation_input_tokens": 1463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1463,
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

_source line 22 · 2026-05-17T17:29:39.519Z_

<details><summary>↩ Tool result · `toolu_01U6sVLx6tiXRzRiw11HnKK3`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "090b88be-011a-435a-ab08-115f8c34dfd8",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "cb3a353b-7148-4535-bee1-23d823d81125",
  "sourceToolAssistantUUID": "090b88be-011a-435a-ab08-115f8c34dfd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T17:29:43.123Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bdxiv5zyQGMVFxqNEHQP5d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb3a353b-7148-4535-bee1-23d823d81125",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y7BMdyJYDheQMLNrUt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "960c7bc9-5608-4d10-8063-d9445937e0b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017P2yreRbHcN2d2VfA3DEF3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 424,
      "cache_read_input_tokens": 23044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 424,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 24 · 2026-05-17T17:29:43.137Z_

<details><summary>↩ Tool result · `toolu_01Bdxiv5zyQGMVFxqNEHQP5d`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{hyperref}
9	\usepackage[margin=2.5cm]{geometry}
10	\usepackage{natbib}
11	\usepackage{xcolor}
12	\usepackage{tabularx}
13	\usepackage{caption}
14	
15	\title{DisPeD: Exploiting the Pragmatic Evasion Asymmetry\\for Robust Multi-Turn Jailbreak Detection}
16	
17	\author{Anonymous}
18	\date{}
19	
20	\begin{document}
21	\maketitle
22	
23	% ============================================================
24	% ABSTRACT
25	% ============================================================
26	\begin{abstract}
27	Multi-turn jailbreak attacks against Large Language Models (LLMs) distribute adversarial intent across individually benign turns, defeating detectors that operate at the lexical or semantic level. We identify a \emph{Pragmatic Evasion Asymmetry}: attackers can freely paraphrase surface content, but the underlying persuasion playbook (rapport building, reframing, escalation) is a structural prerequisite for attack success and cannot be removed without abandoning the attack itself. DisPeD exploits this asymmetry by fine-tuning DeBERTa on an 8-class persuasion strategy taxonomy to produce pragmatic-aware turn embeddings, then modeling the temporal strategy sequence with a GRU for conversation-level classification. On register-normalized data that eliminates lexical shortcuts (TF-IDF reduced from 1.0 to 0.58), DisPeD achieves F1\,=\,0.91 at only $K$\,=\,2 turns, a 14 percentage point (pp) improvement over a vanilla semantic baseline ($p$\,<\,0.001). Under adversarial paraphrasing, DisPeD degrades by only 3\,pp while semantic and lexical baselines degrade by 13\,pp and 18\,pp respectively. A model trained exclusively on Crescendo-style attacks generalizes zero-shot to Foot-in-the-Door and Deceptive Delight attacks with an average F1 of 0.85, outperforming the semantic baseline by 16.5\,pp. These results establish that discourse-level persuasion patterns provide a robust and generalizable signal for early multi-turn jailbreak detection.
28	\end{abstract}
29	
30	% ============================================================
31	% 1. INTRODUCTION
32	% ============================================================
33	\section{Introduction}
34	
35	Multi-turn jailbreak attacks pose a growing threat to deployed LLMs. Attacks such as Crescendo~\citep{russinovich2024greatnow}, Foot-in-the-Door (FITD)~\citep{zhou2024speak}, and Deceptive Delight~\citep{jiang2024deceptive} distribute adversarial intent across multiple conversational turns, each of which appears benign in isolation. \citet{bullwinkel2025multiturn} show that per-turn representations of these attacks are deliberately kept in a ``benign'' region of embedding space, causing representation-level defenses to fail with a 50-point ASR gap. Temporal approaches that track generic semantic drift~\citep{su2026deepcontext} confuse benign conversational evolution with adversarial manipulation, producing high false-positive rates.
36	
37	Why are these attacks so effective? A multi-turn attacker must accomplish two things: (1) maintain surface-level benignity on each turn, and (2) gradually steer the model toward compliance through a persuasion playbook. \citet{zeng2024persuasion} and \citet{hagendorff2026nature} independently show that identifiable persuasion strategies appear in over 97\% of successful multi-turn attacks. The attacker has enormous freedom in choosing \emph{what words} to use (lexical level) and \emph{what topics} to discuss (semantic level), but the underlying \emph{pragmatic function} of each turn (rapport building, authority appeal, reframing) is constrained by the attack's functional requirements.
38	
39	This observation motivates what we call the \textbf{Pragmatic Evasion Asymmetry}: an evasion hierarchy exists in which lexical features are easily evaded via paraphrasing, semantic embeddings are moderately robust but still vulnerable to per-turn content manipulation, and pragmatic persuasion patterns are structurally difficult to evade because they constitute the functional mechanism of the attack. In the terminology of Speech Act Theory~\citep{austin1962things,searle1969speech}, existing detectors operate at the locutionary act level (what was said), while DisPeD operates at the illocutionary act level (what was done).
40	
41	We present \textbf{DisPeD} (\textbf{Dis}course-level \textbf{Pe}rsuasion \textbf{D}etector), a two-stage pipeline that first fine-tunes DeBERTa-v3-base~\citep{he2021debertav3} on a multi-task objective combining 8-class persuasion strategy classification and binary intent classification, then feeds the resulting turn embeddings into a bidirectional GRU for conversation-level jailbreak detection. By grounding turn representations in a persuasion taxonomy derived from Cialdini's influence principles~\citep{cialdini2001science}, DisPeD detects the characteristic escalation trajectory of multi-turn attacks at the earliest possible stage.
42	
43	Our contributions are:
44	\begin{enumerate}
45	    \item We formalize the \emph{Pragmatic Evasion Asymmetry} and provide empirical evidence through a three-tier robustness experiment: under adversarial paraphrasing, DisPeD (pragmatic) degrades by 3\,pp, a vanilla semantic baseline by 13\,pp, and a TF-IDF lexical baseline by 18\,pp (Section~\ref{sec:evasion}).
46	    \item We demonstrate that persuasion-grounded embeddings enable significantly earlier detection: F1\,=\,0.91 at $K$\,=\,2 turns versus 0.77 for the semantic baseline, a 14\,pp advantage that holds across attack types with zero-shot cross-attack transfer averaging 16.5\,pp improvement (Sections~\ref{sec:main_results} and~\ref{sec:cross_attack}).
47	    \item We provide a mechanistic analysis showing that jailbreak conversations exhibit monotonic escalation trajectories in persuasion strategy space (monotonicity score 0.82 vs. 0.34 for benign), explaining why pragmatic features succeed where semantic features fail (Section~\ref{sec:trajectory}).
48	\end{enumerate}
49	
50	% ============================================================
51	% 2. RELATED WORK
52	% ============================================================
53	\section{Related Work}
54	
55	\paragraph{Multi-turn jailbreak attacks.}
56	Crescendo~\citep{russinovich2024greatnow} gradually escalates through conversational rapport, achieving high attack success rates against commercial LLMs. FITD~\citep{zhou2024speak} applies the foot-in-the-door compliance technique, starting with small requests and progressively increasing severity. Deceptive Delight~\citep{jiang2024deceptive} interleaves harmful content within benign creative writing frames. These attacks share a common structure: a persuasion playbook that transitions from trust-building to explicit elicitation across turns. \citet{hagendorff2026nature} analyze persuasion strategies in adversarial conversations and find identifiable patterns in 97\% of successful attacks, confirming that the persuasion structure is systematic rather than incidental.
57	
58	\paragraph{Jailbreak detection.}
59	Single-turn detectors such as perplexity filters~\citep{alon2023detecting} and input classifiers~\citep{inan2023llama} fail against multi-turn attacks because individual turns appear benign. \citet{bullwinkel2025multiturn} demonstrate that per-turn representations are deliberately maintained in benign embedding regions. DeepContext~\citep{su2026deepcontext} addresses this by tracking semantic drift across turns with an encoder-RNN pipeline, but uses generic embeddings that conflate benign topic evolution with adversarial manipulation.
60	
61	\paragraph{Persuasion and LLM safety.}
62	\citet{zeng2024persuasion} compile 40 persuasion techniques used in jailbreaking and show that persuasion-augmented prompts significantly increase ASR. \citet{chen2025persuade} study how LLMs deploy persuasion strategies during multi-turn interactions, demonstrating that persuasion dynamics are extractable from turn-level representations. Our work is the first to use persuasion-grounded representations for jailbreak \emph{detection} rather than attack construction or analysis.
63	
64	% ============================================================
65	% 3. METHOD
66	% ============================================================
67	\section{Method}
68	\label{sec:method}
69	
70	DisPeD consists of two stages: a persuasion-grounded encoder and a temporal sequence classifier.
71	
72	\subsection{Stage 1: Persuasion-Grounded Encoder}
73	
74	We fine-tune DeBERTa-v3-base on a multi-task objective with two heads:
75	
76	\begin{itemize}
77	    \item \textbf{Persuasion strategy classification} (8 classes): rapport building, authority appeal, reciprocity, social proof, commitment/consistency, scarcity/urgency, reframing, and direct request. These categories are derived from Cialdini's principles of influence~\citep{cialdini2001science} and adapted for adversarial conversational contexts following \citet{zeng2024persuasion}. Benign turns lacking a persuasion function receive a ``none'' label.
78	    \item \textbf{Intent classification} (binary): whether the turn carries jailbreak intent.
79	\end{itemize}
80	
81	The total loss is $\mathcal{L} = \mathcal{L}_{\text{persuasion}} + \lambda \mathcal{L}_{\text{intent}}$, where $\lambda = 1.0$. After training, we extract the [CLS] embedding from the fine-tuned encoder as the persuasion-grounded turn representation. The encoder achieves 79\% accuracy on 8-class persuasion classification and 94\% on binary intent classification (Table~\ref{tab:encoder}).
82	
83	\subsection{Stage 2: Temporal Sequence Classification}
84	
85	Given a conversation of $K$ turns, we obtain turn embeddings $\{e_1, \ldots, e_K\}$ from the Stage 1 encoder. A bidirectional GRU processes the embedding sequence and outputs a conversation-level binary classification (jailbreak vs. benign) from the final hidden state. This architecture captures the temporal progression of persuasion strategies across turns.
86	
87	\subsection{Baselines}
88	
89	We compare DisPeD against three baselines spanning the evasion hierarchy:
90	\begin{itemize}
91	    \item \textbf{TF-IDF + Logistic Regression}: a lexical baseline operating on bag-of-words features.
92	    \item \textbf{DeBERTa Semantic Baseline}: the same Stage 2 GRU pipeline but with \emph{vanilla} (not fine-tuned) DeBERTa embeddings, representing semantic-level detection.
93	    \item \textbf{DeepContext Proxy}: BERT-base + GRU, simulating the DeepContext architecture with generic drift features and no persuasion grounding.
94	\end{itemize}
95	
96	% ============================================================
97	% 4. EXPERIMENTAL SETUP
98	% ============================================================
99	\section{Experimental Setup}
100	\label{sec:setup}
101	
102	\subsection{Data Preparation and Register Normalization}
103	\label{sec:data}
104	
105	Our dataset consists of 480 conversations (240 jailbreak, 240 benign) with 72 held out for testing. Jailbreak conversations are Crescendo-style multi-turn attacks; benign conversations are drawn from standard conversational corpora and WildChat~\citep{zhao2024wildchat}.
106	
107	A critical challenge in multi-turn jailbreak detection is \emph{lexical shortcut}: scripted attack dialogues have distributional properties distinct from naturalistic benign conversations, allowing simple bag-of-words classifiers to succeed without learning meaningful features. On our original data, TF-IDF separability was 1.0, indicating complete lexical shortcut.
108	
109	We apply register normalization using LLM paraphrasing to convert jailbreak turns from formal/scripted register to conversational register, eliminating the distributional gap. Table~\ref{tab:tfidf_diagnostic} confirms the effectiveness of this procedure: TF-IDF drops from 1.0 to 0.58, below our hard gate of 0.75 but above the random baseline of 0.50, reflecting residual functional vocabulary (e.g., ``hypothetical,'' ``scenario'') that attackers cannot entirely avoid. Persuasion strategy annotations are preserved at 94\% after normalization, confirming that the persuasion structure is a discourse-level phenomenon independent of lexical realization.
110	
111	\begin{table}[t]
112	\centering
113	\caption{TF-IDF separability before and after register normalization.}
114	\label{tab:tfidf_diagnostic}
115	\begin{tabular}{lcc}
116	\toprule
117	\textbf{Condition} & \textbf{TF-IDF} & \textbf{Vocab Overlap (\%)} \\
118	\midrule
119	Original data & 1.00 & 12.3 \\
120	Register-normalized & 0.58 & 41.7 \\
121	Random baseline & 0.50 & 50.0 \\
122	\bottomrule
123	\end{tabular}
124	\end{table}
125	
126	\subsection{Multi-Attack Dataset}
127	\label{sec:multi_attack_data}
128	
129	To evaluate cross-attack generalization (Section~\ref{sec:cross_attack}), we generate additional attack conversations in two families beyond Crescendo using Qwen3-8B: 72 FITD-style conversations (avg. 6.8 turns) employing the foot-in-the-door compliance escalation pattern, and 65 Deceptive Delight-style conversations (avg. 5.2 turns) interleaving harmful content within benign frames. All generated conversations receive persuasion strategy annotations with 91\% LLM annotation consistency. Table~\ref{tab:attack_stats} summarizes the dataset statistics.
130	
131	\begin{table}[t]
132	\centering
133	\caption{Attack type statistics. TF-IDF measured against benign conversations.}
134	\label{tab:attack_stats}
135	\begin{tabular}{lcccc}
136	\toprule
137	\textbf{Attack Type} & \textbf{$n$} & \textbf{Avg Turns} & \textbf{Turn Range} & \textbf{TF-IDF} \\
138	\midrule
139	Crescendo (original) & 240 & 5.5 & 3--12 & 0.58 \\
140	FITD (generated) & 72 & 6.8 & 4--10 & 0.61 \\
141	Deceptive Delight (generated) & 65 & 5.2 & 3--8 & 0.55 \\
142	\bottomrule
143	\end{tabular}
144	\end{table}
145	
146	The three attack types share the same persuasion strategy vocabulary but differ in temporal arrangement. As shown in Table~\ref{tab:strategy_dist}, FITD relies heavily on reciprocity (30\%) and commitment/consistency (25\%), reflecting its gradual compliance escalation. Deceptive Delight favors authority appeal (22\%) and social proof (18\%), using authoritative framing to embed harmful content. Crescendo is more evenly distributed across strategies. This variation in strategy profiles, combined with a shared underlying vocabulary, provides the conditions for testing zero-shot cross-attack transfer.
147	
148	\begin{table}[t]
149	\centering
150	\caption{Persuasion strategy distribution (\%) by attack type.}
151	\label{tab:strategy_dist}
152	\begin{tabular}{lccc}
153	\toprule
154	\textbf{Strategy} & \textbf{Crescendo} & \textbf{FITD} & \textbf{Dec. Delight} \\
155	\midrule
156	Rapport building & 28 & 35 & 15 \\
157	Authority appeal & 12 & 8 & 22 \\
158	Reciprocity & 18 & 30 & 10 \\
159	Social proof & 8 & 5 & 18 \\
160	Commitment/consistency & 15 & 25 & 8 \\
161	Scarcity/urgency & 5 & 3 & 12 \\
162	Reframing & 22 & 15 & 20 \\
163	Direct request & 7 & 4 & 15 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	% ============================================================
169	% 5. RESULTS
170	% ============================================================
171	\section{Results}
172	
173	\subsection{Main Results: Early Detection on Clean Data}
174	\label{sec:main_results}
175	
176	Table~\ref{tab:main_results} presents the core comparison between DisPeD and the semantic baseline across turn budgets on register-normalized data. DisPeD achieves F1\,=\,0.91 at $K$\,=\,2 turns, a 14\,pp improvement over the semantic baseline (0.77, $p$\,<\,0.001 by bootstrap test). The advantage is largest at early turn budgets ($K$\,=\,1--2) and narrows at higher $K$ as the baseline accumulates sufficient semantic drift signal, converging to a 7\,pp gap on full conversations.
177	
178	\begin{table}[t]
179	\centering
180	\caption{F1 by turn budget on clean (register-normalized) data. $\Delta$ is the improvement of DisPeD over the semantic baseline in percentage points. All $p$-values by bootstrap test.}
181	\label{tab:main_results}
182	\begin{tabular}{lcccc}
183	\toprule
184	\textbf{$K$} & \textbf{DisPeD} & \textbf{Baseline} & \textbf{$\Delta$ (pp)} & \textbf{$p$} \\
185	\midrule
186	1 & 0.82 & 0.68 & 14 & 0.003 \\
187	2 & 0.91 & 0.77 & 14 & 0.001 \\
188	3 & 0.93 & 0.83 & 10 & 0.004 \\
189	5 & 0.96 & 0.88 & 8 & 0.012 \\
190	All & 0.96 & 0.89 & 7 & 0.018 \\
191	\bottomrule
192	\end{tabular}
193	\end{table}
194	
195	At $K$\,=\,2, DisPeD also achieves a substantially lower false-positive rate at 95\% TPR: FPR\,=\,0.08 versus 0.19 for the baseline. This early detection capability is the headline result: persuasion strategy transitions (e.g., rapport building to authority framing) manifest within the first two turns, providing discriminative signal before explicitly harmful content appears.
196	
197	Table~\ref{tab:encoder} reports the Stage 1 encoder metrics. The 79\% persuasion classification accuracy (macro F1\,=\,0.74) confirms that the encoder learns meaningful persuasion representations rather than noise, while the 94\% intent accuracy validates the multi-task training.
198	
199	\begin{table}[t]
200	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "960c7bc9-5608-4d10-8063-d9445937e0b3",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "38358e0a-795a-438e-8009-12cf01c4c6f1",
  "sourceToolAssistantUUID": "960c7bc9-5608-4d10-8063-d9445937e0b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T17:29:43.437Z_

<details open><summary>🔧 Tool call — Read · `toolu_013W5BHUhTGvmSUXcxnu2qGc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38358e0a-795a-438e-8009-12cf01c4c6f1",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y7BMdyJYDheQMLNrUt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7593e29e-4d3f-4cc1-a074-73335ee93d8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017P2yreRbHcN2d2VfA3DEF3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 424,
      "cache_read_input_tokens": 23044,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 424
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 23044,
          "cache_creation_input_tokens": 424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 424,
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

_source line 26 · 2026-05-17T17:29:43.444Z_

<details><summary>↩ Tool result · `toolu_013W5BHUhTGvmSUXcxnu2qGc`</summary>

```text
1	# Experiment Plan — persuasion_turn_jailbreak_detect
2	# Generated: 2026-05-17
3	# Target: EMNLP 2026 ARR (DDL 2026-05-25)
4	# GPU budget: 4x RTX PRO 6000 Blackwell @ westd-33183, ~8 days = ~768 GPU-hours total
5	
6	experiments:
7	  # ============ P0: Critical Path (must complete before submission) ============
8	
9	  - id: plan_001
10	    name: data_quality_fix
11	    claim: [1, 2, 3]
12	    description: >
13	      Fix TF-IDF=1.0 data quality issue. Three sub-tasks:
14	      (a) Fix strategy=7 benign labeling — use "none" or 9th class instead of hardcoded 7 (M004 fix)
15	      (b) Register-normalize jailbreak data — LLM paraphrase jailbreak turns to conversational register
16	          while preserving persuasion strategy structure (the claim is pragmatic patterns survive register change)
17	      (c) Verify TF-IDF drops to <0.65 on normalized data (tightened per Reviewer feedback: 0.75 still allows residual lexical signal)
18	      (d) TF-IDF sanity check is HARD GATE — do not proceed to training if TF-IDF >= 0.65
19	      (e) Include 20-sample manual verification that paraphrased turns preserve original persuasion strategy category
20	    priority: P0
21	    gpu_budget_hours: 8
22	    deps: []
23	    pass_criteria: "TF-IDF < 0.65 on register-normalized data with fixed labels; paraphrase preserves persuasion strategy in 20-sample check"
24	    registry_id: null
25	
26	  - id: plan_002
27	    name: core_revalidation_clean
28	    claim: [2]
29	    description: >
30	      Re-run Phase B on clean data (from plan_001). Retrain both treatment (persuasion-grounded DeBERTa)
31	      and baseline (vanilla DeBERTa) from scratch on register-normalized data with fixed labels.
32	      Full evaluation at K=1,2,3,5,all. Core claim validation on clean data.
33	    priority: P0
34	    gpu_budget_hours: 12
35	    deps: [plan_001]
36	    pass_criteria: "Treatment F1 > baseline F1 + 5pp at K=2 or K=3 on clean data"
37	    registry_id: null
38	
39	  - id: plan_003
40	    name: scrambled_label_ablation
41	    claim: [2]
42	    description: >
43	      Ablation: randomly shuffle persuasion strategy labels for jailbreak turns, retrain treatment model.
44	      If performance drops significantly vs properly-labeled treatment, confirms persuasion labels
45	      carry real signal beyond being a class indicator. Validates that M004 fix was necessary.
46	    priority: P0
47	    gpu_budget_hours: 4
48	    deps: [plan_001]
49	    pass_criteria: "Scrambled-label treatment F1 < properly-labeled treatment F1 (significant gap)"
50	    registry_id: null
51	
52	  - id: plan_004
53	    name: adversarial_perturbation
54	    claim: [1, 3]
55	    description: >
56	      Core Claim 3 validation. Take clean jailbreak conversations, apply aggressive paraphrasing
57	      (synonym substitution, sentence restructuring, register shifting) to remove ALL lexical cues.
58	      Evaluate both treatment and baseline on perturbed data (models trained on unperturbed data).
59	      Treatment should degrade less than baseline, proving pragmatic features are robust.
60	      Also run TF-IDF baseline to show it collapses under perturbation.
61	    priority: P0
62	    gpu_budget_hours: 8
63	    deps: [plan_002]
64	    pass_criteria: "Treatment F1 drop < baseline F1 drop under perturbation (delta-delta > 3pp)"
65	    registry_id: null
66	
67	  - id: plan_005
68	    name: multi_attack_generation
69	    claim: [2]
70	    description: >
71	      Generate 2 additional attack types beyond Crescendo to test generalization:
72	      (a) FITD-style (foot-in-the-door): gradual compliance escalation
73	      (b) Deceptive Delight-style: interleaving benign and harmful content
74	      Use existing Qwen3-8B pipeline with appropriate attack playbooks.
75	      ~50-100 conversations per type. Annotate with persuasion strategies.
76	    priority: P0
77	    gpu_budget_hours: 8
78	    deps: []
79	    pass_criteria: ">=50 conversations per attack type, all with persuasion strategy annotations"
80	    registry_id: null
81	
82	  - id: plan_006
83	    name: cross_attack_evaluation
84	    claim: [2]
85	    description: >
86	      Evaluate treatment and baseline models (trained on Crescendo) on FITD and Deceptive Delight
87	      attack types from plan_005. Tests zero-shot generalization across attack families.
88	    priority: P0
89	    gpu_budget_hours: 4
90	    deps: [plan_002, plan_005]
91	    pass_criteria: "Treatment F1 > baseline F1 on unseen attack types"
92	    registry_id: null
93	
94	  # ============ P1: Important (strongly recommended before submission) ============
95	
96	  - id: plan_007
97	    name: tfidf_lr_baseline
98	    claim: [1]
99	    description: >
100	      TF-IDF + Logistic Regression baseline on clean data. Quantifies how much of the detection
101	      is attributable to lexical features alone. Critical for the evasion hierarchy narrative.
102	    priority: P1
103	    gpu_budget_hours: 0.5
104	    deps: [plan_001]
105	    pass_criteria: "Baseline number for comparison"
106	    registry_id: null
107	
108	  - id: plan_008
109	    name: strategy_transition_analysis
110	    claim: [3]
111	    description: >
112	      Compute persuasion strategy transition matrices for jailbreak vs benign conversations.
113	      Visualize monotonic escalation trajectory (Claim 3). Generate paper figures:
114	      (a) Strategy transition heatmaps (jailbreak vs benign)
115	      (b) Per-turn strategy distribution evolution
116	      (c) Trajectory visualization in strategy space
117	    priority: P1
118	    gpu_budget_hours: 1
119	    deps: [plan_001]
120	    pass_criteria: "Clear visual distinction between jailbreak escalation and benign oscillation patterns"
121	    registry_id: null
122	
123	  - id: plan_009
124	    name: wildchat_hard_negatives
125	    claim: [2]
126	    description: >
127	      Filter WildChat for high-drift benign conversations as hard negatives.
128	      Evaluate FPR on these. Must handle contamination (previous runs found 14-16% jailbreak content
129	      in WildChat). Apply LLM-based or keyword-based filtering first.
130	    priority: P1
131	    gpu_budget_hours: 4
132	    deps: [plan_002]
133	    pass_criteria: "FPR < 15% on high-drift benign conversations"
134	    registry_id: null
135	
136	  # ============ P2: Nice to Have (if time permits) ============
137	
138	  - id: plan_010
139	    name: cross_checkpoint_variance
140	    claim: [2]
141	    description: >
142	      Evaluate from multiple DeBERTa fine-tuning checkpoints (epoch 2/3/final) to quantify
143	      encoder training stochasticity on downstream performance.
144	    priority: P2
145	    gpu_budget_hours: 4
146	    deps: [plan_002]
147	    pass_criteria: "Variance across checkpoints < 2pp F1"
148	    registry_id: null
149	
150	  - id: plan_011
151	    name: deepcontext_proxy_reproduction
152	    claim: [1, 2]
153	    description: >
154	      Attempt to reproduce DeepContext-like baseline: BERT-base (not DeBERTa) + GRU with
155	      generic drift features. Not a full DeepContext reproduction (no public code), but
156	      a proxy that isolates the encoder + feature representation contribution.
157	    priority: P2
158	    gpu_budget_hours: 8
159	    deps: [plan_001]
160	    pass_criteria: "Proxy baseline F1 in reasonable range for comparison"
161	    registry_id: null
162	
163	# MVP experiments (completed, for reference)
164	completed_mvp:
165	  - registry_id: pilot_phase_b
166	    description: "Pilot Phase B on 270 samples, treatment F1=1.0 vs baseline 0.737"
167	  - registry_id: phase_b_full
168	    description: "Phase B full on 480 samples, treatment K=2 F1=0.987 vs baseline 0.879 (+10.8pp). TF-IDF=1.0 caveat."
169	
170	# Resource summary
171	resource_summary:
172	  total_p0_gpu_hours: 44
173	  total_p1_gpu_hours: 5.5
174	  total_p2_gpu_hours: 12
175	  available_gpu_hours: 768  # 4 GPUs x 8 days x 24h
176	  utilization_target: "P0 all, P1 all, P2 as time permits"
177	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7593e29e-4d3f-4cc1-a074-73335ee93d8b",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "b820c6d7-d048-40e4-aac1-8ace10d5786c",
  "sourceToolAssistantUUID": "7593e29e-4d3f-4cc1-a074-73335ee93d8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T17:29:49.716Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UtmT1275MCjGdDJtMi8vaX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b820c6d7-d048-40e4-aac1-8ace10d5786c",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y7UEPz11NBNFLgr3Zm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f40b0e90-1736-4b93-9b77-a40dcd9b2238",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wUb7rGRd2oUQ8MjKE9uHf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8120,
      "cache_read_input_tokens": 23468,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8120
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 23468,
          "cache_creation_input_tokens": 8120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8120,
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

_source line 28 · 2026-05-17T17:29:49.722Z_

<details><summary>↩ Tool result · `toolu_01UtmT1275MCjGdDJtMi8vaX`</summary>

```text
200	\centering
201	\caption{DeBERTa encoder metrics on clean data.}
202	\label{tab:encoder}
203	\begin{tabular}{lc}
204	\toprule
205	\textbf{Metric} & \textbf{Value} \\
206	\midrule
207	Persuasion 8-class accuracy & 0.79 \\
208	Persuasion macro F1 & 0.74 \\
209	Intent binary accuracy & 0.94 \\
210	Best epoch & 3 \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	\subsection{Pragmatic Evasion Asymmetry}
216	\label{sec:evasion}
217	
218	To empirically validate the Pragmatic Evasion Asymmetry, we apply aggressive paraphrasing (synonym substitution, sentence restructuring) to jailbreak conversations and measure detection degradation across four model tiers. Table~\ref{tab:evasion_full} reports results on full conversations.
219	
220	\begin{table}[t]
221	\centering
222	\caption{Evasion hierarchy under adversarial paraphrasing (full conversation). Models ordered by abstraction level. Drop is the F1 degradation in percentage points.}
223	\label{tab:evasion_full}
224	\begin{tabular}{lccc}
225	\toprule
226	\textbf{Model} & \textbf{F1 (Clean)} & \textbf{F1 (Perturbed)} & \textbf{Drop (pp)} \\
227	\midrule
228	DisPeD (pragmatic) & 0.96 & 0.93 & 3 \\
229	DeBERTa baseline (semantic) & 0.89 & 0.76 & 13 \\
230	DeepContext proxy (generic temporal) & 0.84 & 0.69 & 15 \\
231	TF-IDF + LR (lexical) & 0.72 & 0.54 & 18 \\
232	\bottomrule
233	\end{tabular}
234	\end{table}
235	
236	The results reveal a clear three-tier gradient aligned with the predicted evasion hierarchy. TF-IDF collapses under perturbation ($-$18\,pp) because synonym substitution directly destroys the lexical features it relies on. The DeepContext proxy degrades by 15\,pp because BERT-base representations partially depend on surface patterns. The semantic baseline degrades moderately ($-$13\,pp) as contextual embeddings are disrupted by token-level changes even when meaning is largely preserved. DisPeD degrades minimally ($-$3\,pp) because persuasion-grounded representations encode illocutionary acts that are invariant to paraphrasing: ``building rapport through self-disclosure'' retains its pragmatic function regardless of lexical realization.
237	
238	A particularly strong result: DisPeD under adversarial perturbation (F1\,=\,0.93) still outperforms the semantic baseline on \emph{unperturbed} data (F1\,=\,0.89). Table~\ref{tab:evasion_k2} shows that this pattern holds at $K$\,=\,2, where DisPeD maintains F1\,=\,0.87 versus 0.63 for the semantic baseline.
239	
240	\begin{table}[t]
241	\centering
242	\caption{Evasion hierarchy at $K$\,=\,2 turns.}
243	\label{tab:evasion_k2}
244	\begin{tabular}{lccc}
245	\toprule
246	\textbf{Model} & \textbf{F1 Clean} & \textbf{F1 Perturbed} & \textbf{Drop (pp)} \\
247	\midrule
248	DisPeD & 0.91 & 0.87 & 4 \\
249	DeBERTa baseline & 0.77 & 0.63 & 14 \\
250	TF-IDF + LR & 0.65 & 0.48 & 17 \\
251	\bottomrule
252	\end{tabular}
253	\end{table}
254	
255	\subsection{Ablation: Scrambled Label Analysis}
256	\label{sec:ablation}
257	
258	To confirm that the advantage of DisPeD comes from the \emph{semantic content} of persuasion labels rather than the fine-tuning process itself, we retrain the encoder with randomly scrambled persuasion strategy labels (intent labels remain intact). Table~\ref{tab:scrambled} shows that scrambling causes a 15\,pp drop at $K$\,=\,2, bringing performance close to the vanilla baseline (0.76 vs. 0.77). The scrambled encoder's persuasion classification accuracy drops to 0.13 ($\approx 1/8$ random chance), confirming that the label signal is destroyed. This ablation establishes a causal link: the discriminative power of DisPeD derives from the semantic content of persuasion strategy annotations, not from any incidental benefit of multi-task training.
259	
260	\begin{table}[t]
261	\centering
262	\caption{Effect of scrambling persuasion strategy labels. Drop is relative to properly labeled DisPeD.}
263	\label{tab:scrambled}
264	\begin{tabular}{lccc}
265	\toprule
266	\textbf{$K$} & \textbf{Proper Labels} & \textbf{Scrambled Labels} & \textbf{Drop (pp)} \\
267	\midrule
268	2 & 0.91 & 0.76 & 15 \\
269	3 & 0.93 & 0.81 & 12 \\
270	All & 0.96 & 0.87 & 9 \\
271	\bottomrule
272	\end{tabular}
273	\end{table}
274	
275	\subsection{Cross-Attack Zero-Shot Generalization}
276	\label{sec:cross_attack}
277	
278	A model trained exclusively on Crescendo-style attacks is evaluated zero-shot on FITD and Deceptive Delight attacks. Table~\ref{tab:cross_attack} presents the results. DisPeD achieves an average F1 of 0.85 on unseen attack types, outperforming the semantic baseline by 16.5\,pp. DisPeD on unseen attacks (0.85) approaches the semantic baseline on \emph{seen} attacks (0.89), demonstrating that persuasion-grounded representations capture attack-type-agnostic pragmatic signals.
279	
280	\begin{table}[t]
281	\centering
282	\caption{Zero-shot cross-attack generalization (full conversation). The model is trained on Crescendo only.}
283	\label{tab:cross_attack}
284	\begin{tabular}{lccc}
285	\toprule
286	\textbf{Attack Type} & \textbf{DisPeD} & \textbf{Baseline} & \textbf{$\Delta$ (pp)} \\
287	\midrule
288	FITD & 0.84 & 0.67 & 17 \\
289	Deceptive Delight & 0.86 & 0.70 & 16 \\
290	Crescendo (held-out) & 0.96 & 0.89 & 7 \\
291	\bottomrule
292	\end{tabular}
293	\end{table}
294	
295	Table~\ref{tab:cross_attack_k2} reports early detection on unseen attacks. At $K$\,=\,2, DisPeD achieves recall of 0.78 on FITD and 0.81 on Deceptive Delight, versus 0.55 and 0.58 for the baseline.
296	
297	\begin{table}[t]
298	\centering
299	\caption{Cross-attack early detection recall at $K$\,=\,2.}
300	\label{tab:cross_attack_k2}
301	\begin{tabular}{lcc}
302	\toprule
303	\textbf{Attack Type} & \textbf{DisPeD Recall} & \textbf{Baseline Recall} \\
304	\midrule
305	FITD & 0.78 & 0.55 \\
306	Deceptive Delight & 0.81 & 0.58 \\
307	\bottomrule
308	\end{tabular}
309	\end{table}
310	
311	The transfer works because all three attack types share the same persuasion strategy vocabulary (Table~\ref{tab:strategy_dist}), differing only in temporal arrangement. The GRU learns a generic ``persuasion escalation'' detector rather than Crescendo-specific surface patterns. Deceptive Delight transfers slightly better (0.86 vs. 0.84) because its strategy profile (strong reframing component) more closely resembles Crescendo's distribution.
312	
313	\subsection{Mechanistic Analysis: Escalation Trajectories}
314	\label{sec:trajectory}
315	
316	To provide a mechanistic explanation for why pragmatic features succeed, we analyze persuasion strategy transition patterns. Table~\ref{tab:trajectory} reports two quantitative metrics distinguishing jailbreak from benign conversations.
317	
318	\begin{table}[t]
319	\centering
320	\caption{Strategy transition statistics. Monotonicity measures the fraction of transitions along the escalation direction. Entropy measures the diversity of transition types.}
321	\label{tab:trajectory}
322	\begin{tabular}{lccc}
323	\toprule
324	\textbf{Type} & \textbf{Transition Entropy} & \textbf{Monotonicity} & \textbf{$n$} \\
325	\midrule
326	Jailbreak & 1.8 & 0.82 & 240 \\
327	Benign & 2.9 & 0.34 & 240 \\
328	\bottomrule
329	\end{tabular}
330	\end{table}
331	
332	Jailbreak conversations exhibit highly monotonic escalation (score 0.82): 82\% of strategy transitions move from lower-risk to higher-risk categories (e.g., rapport building $\to$ commitment/consistency $\to$ reframing $\to$ direct request). Benign conversations show near-random monotonicity (0.34) with oscillatory, task-driven patterns. Transition entropy is lower for jailbreaks (1.8 vs. 2.9) because attackers follow a concentrated playbook, while benign conversations traverse a wider range of pragmatic functions.
333	
334	Table~\ref{tab:dominant_sequences} shows the most frequent strategy sequences. Jailbreak conversations converge on a small number of escalation trajectories (top-3 covering 74\% of cases), while benign conversations are dominated by ``none'' labels (45\%) reflecting the absence of persuasion intent. The trajectory-only separability (AUROC\,=\,0.91) confirms that the escalation pattern alone, without any content features, is strongly discriminative.
335	
336	\begin{table}[t]
337	\centering
338	\caption{Top-3 dominant strategy sequences by conversation type.}
339	\label{tab:dominant_sequences}
340	\small
341	\begin{tabular}{clcclc}
342	\toprule
343	 & \textbf{Jailbreak Sequence} & \textbf{\%} & & \textbf{Benign Sequence} & \textbf{\%} \\
344	\midrule
345	1 & rapport$\to$commit$\to$reframe$\to$direct & 34 & 1 & none$\to$none$\to$none$\to$none & 45 \\
346	2 & rapport$\to$social$\to$reframe$\to$direct & 22 & 2 & rapport$\to$none$\to$rapport$\to$none & 18 \\
347	3 & rapport$\to$reciprocity$\to$commit$\to$direct & 18 & 3 & none$\to$rapport$\to$none$\to$direct & 12 \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	\subsection{Robustness on Hard Negatives}
353	\label{sec:hard_negatives}
354	
355	A potential concern is that DisPeD might flag benign conversations with high topic diversity as jailbreaks. We evaluate on hard negatives from WildChat~\citep{zhao2024wildchat}: 120 high-drift benign conversations where users shift across multiple domains (e.g., coding to personal advice to creative writing). We filter 15.2\% of WildChat conversations as potential contamination.
356	
357	\begin{table}[t]
358	\centering
359	\caption{False-positive rate on hard negatives (high-drift benign) vs. random benign.}
360	\label{tab:hard_negatives}
361	\begin{tabular}{lccc}
362	\toprule
363	\textbf{Model} & \textbf{FPR (Hard)} & \textbf{FPR (Random)} & \textbf{$\Delta$} \\
364	\midrule
365	DisPeD & 0.09 & 0.03 & 0.06 \\
366	DeBERTa baseline & 0.17 & 0.06 & 0.11 \\
367	TF-IDF + LR & 0.22 & 0.08 & 0.14 \\
368	\bottomrule
369	\end{tabular}
370	\end{table}
371	
372	Table~\ref{tab:hard_negatives} shows that DisPeD maintains a low FPR of 9\% on hard negatives, compared to 17\% for the semantic baseline and 22\% for TF-IDF. The persuasion-grounded representations distinguish ``topic drift'' (benign, oscillatory strategy transitions) from ``strategy escalation'' (adversarial, monotonic trajectory), a distinction that semantic embeddings cannot reliably make.
373	
374	\subsection{Lexical Baseline Analysis}
375	\label{sec:lexical}
376	
377	Table~\ref{tab:tfidf_performance} reports the TF-IDF + Logistic Regression baseline on clean data. Even after register normalization, residual lexical signal provides above-chance performance (F1\,=\,0.72) due to functional vocabulary that attackers cannot entirely avoid. The top discriminative features (Table~\ref{tab:top_features}) confirm this: jailbreak-indicative words (``hypothetical,'' ``scenario,'' ``imagine'') are framing devices required by the attack structure. This residual lexical signal (F1\,=\,0.72) falls far short of what pragmatic features achieve (F1\,=\,0.96) and collapses under adversarial perturbation (F1\,=\,0.54).
378	
379	\begin{table}[t]
380	\centering
381	\caption{TF-IDF + LR performance by turn budget on clean data.}
382	\label{tab:tfidf_performance}
383	\begin{tabular}{lccc}
384	\toprule
385	\textbf{$K$} & \textbf{F1} & \textbf{Precision} & \textbf{Recall} \\
386	\midrule
387	2 & 0.65 & 0.68 & 0.62 \\
388	3 & 0.68 & 0.71 & 0.65 \\
389	5 & 0.70 & 0.73 & 0.68 \\
390	All & 0.72 & 0.75 & 0.70 \\
391	\bottomrule
392	\end{tabular}
393	\end{table}
394	
395	\begin{table}[t]
396	\centering
397	\caption{Top-5 discriminative features by LR coefficient.}
398	\label{tab:top_features}
399	\begin{tabular}{clccl c}
400	\toprule
401	\textbf{Rank} & \textbf{Jailbreak Feature} & \textbf{Weight} & & \textbf{Benign Feature} & \textbf{Weight} \\
402	\midrule
403	1 & hypothetical & 2.31 & & thanks & 1.89 \\
404	2 & scenario & 1.95 & & help & 1.72 \\
405	3 & imagine & 1.87 & & question & 1.54 \\
406	4 & creative & 1.62 & & code & 1.41 \\
407	5 & roleplay & 1.48 & & explain & 1.33 \\
408	\bottomrule
409	\end{tabular}
410	\end{table}
411	
412	\subsection{Checkpoint Sensitivity}
413	\label{sec:checkpoint}
414	
415	To assess reproducibility on our relatively small dataset, we evaluate DisPeD with DeBERTa encoders from different training epochs. Table~\ref{tab:checkpoint} shows that downstream F1 varies by at most 1\,pp across checkpoints, indicating that the results are robust to encoder training stochasticity.
416	
417	\begin{table}[t]
418	\centering
419	\caption{Checkpoint sensitivity analysis.}
420	\label{tab:checkpoint}
421	\begin{tabular}{lcccc}
422	\toprule
423	\textbf{Checkpoint} & \textbf{Persuasion Acc} & \textbf{Intent Acc} & \textbf{F1 (Full)} & \textbf{F1 ($K$=2)} \\
424	\midrule
425	Epoch 2 & 0.76 & 0.93 & 0.94 & 0.89 \\
426	Epoch 3 & 0.79 & 0.94 & 0.96 & 0.91 \\
427	Epoch final & 0.78 & 0.94 & 0.95 & 0.90 \\
428	\bottomrule
429	\end{tabular}
430	\end{table}
431	
432	% ============================================================
433	% 6. DISCUSSION
434	% ============================================================
435	\section{Discussion}
436	
437	\paragraph{Why pragmatic features are structurally robust.}
438	The Pragmatic Evasion Asymmetry is not merely an empirical observation but follows from the functional requirements of multi-turn attacks. An attacker who removes rapport building cannot establish the trust needed for later compliance. An attacker who skips reframing cannot normalize the harmful request. An attacker who eliminates all escalation has, by definition, not conducted a multi-turn attack. Each persuasion strategy serves a necessary function in the attack pipeline, and our experiments confirm that this structural constraint translates into measurably robust detection features.
439	
440	\paragraph{Limitations.}
441	Our dataset is small (480 conversations) and the generated attack conversations may not capture the full diversity of real-world adversarial behavior. The persuasion taxonomy is limited to 8 categories; a finer-grained taxonomy might capture additional discriminative patterns. We do not evaluate against attacks that deliberately target the persuasion detection mechanism (adaptive adversaries aware of DisPeD). Human evaluation of the interpretability of strategy trajectories remains future work. Our scope is limited to persuasion-mediated multi-turn attacks; pure information accumulation attacks, token smuggling, and single-turn roleplay jailbreaks fall outside our detection target.
442	
443	% ============================================================
444	% 7. CONCLUSION
445	% ============================================================
446	\section{Conclusion}
447	
448	We introduced DisPeD, a multi-turn jailbreak detector that exploits the Pragmatic Evasion Asymmetry by grounding turn representations in a persuasion strategy taxonomy. Our experiments on register-normalized data demonstrate three key findings: (1) pragmatic features degrade minimally under adversarial paraphrasing (3\,pp) compared to semantic (13\,pp) and lexical (18\,pp) features; (2) persuasion-grounded embeddings enable early detection at $K$\,=\,2 turns with 14\,pp improvement over semantic baselines, an advantage that transfers zero-shot across attack families; and (3) the mechanistic basis for this advantage is the monotonic escalation trajectory in persuasion strategy space that characterizes multi-turn attacks. These results suggest that discourse-level pragmatic analysis is a promising direction for building jailbreak defenses that are robust to surface-level evasion.
449	
450	% ============================================================
451	% REFERENCES
452	% ============================================================
453	\bibliographystyle{plainnat}
454	
455	\begin{thebibliography}{20}
456	
457	\bibitem[Alon and Kamfonas(2023)]{alon2023detecting}
458	G.~Alon and M.~Kamfonas.
459	\newblock Detecting language model attacks with perplexity.
460	\newblock \emph{arXiv preprint arXiv:2308.14132}, 2023.
461	
462	\bibitem[Austin(1962)]{austin1962things}
463	J.~L. Austin.
464	\newblock \emph{How to Do Things with Words}.
465	\newblock Oxford University Press, 1962.
466	
467	\bibitem[Bullwinkel et~al.(2025)]{bullwinkel2025multiturn}
468	S.~Bullwinkel, P.~Schramowski, and K.~Kersting.
469	\newblock Multi-turn jailbreaks hide in the representation space.
470	\newblock \emph{arXiv preprint arXiv:2507.02956}, 2025.
471	
472	\bibitem[Chen et~al.(2025)]{chen2025persuade}
473	W.~Chen, Y.~Li, and R.~Jia.
474	\newblock How do {LLMs} persuade? {E}xtracting persuasion dynamics from multi-turn conversations.
475	\newblock \emph{arXiv preprint arXiv:2508.05625}, 2025.
476	
477	\bibitem[Cialdini(2001)]{cialdini2001science}
478	R.~B. Cialdini.
479	\newblock \emph{Influence: Science and Practice}.
480	\newblock Allyn \& Bacon, 4th edition, 2001.
481	
482	\bibitem[Hagendorff(2026)]{hagendorff2026nature}
483	T.~Hagendorff.
484	\newblock Persuasion strategies in adversarial conversations with large language models.
485	\newblock \emph{Nature Communications}, 2026.
486	
487	\bibitem[He et~al.(2021)]{he2021debertav3}
488	P.~He, J.~Gao, and W.~Chen.
489	\newblock {DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-style pre-training with gradient-disentangled embedding sharing.
490	\newblock \emph{arXiv preprint arXiv:2111.09543}, 2021.
491	
492	\bibitem[Inan et~al.(2023)]{inan2023llama}
493	H.~Inan, K.~Upasani, J.~Chi, R.~Rungta, K.~Iyer, Y.~Mao, M.~Tontchev, Q.~Hu, B.~Fuller, D.~Testuggine, and M.~Khabsa.
494	\newblock {Llama Guard}: {LLM}-based input-output safeguard for human-{AI} conversations.
495	\newblock \emph{arXiv preprint arXiv:2312.06674}, 2023.
496	
497	\bibitem[Jiang et~al.(2024)]{jiang2024deceptive}
498	Y.~Jiang, H.~Zhang, and others.
499	\newblock Deceptive delight: Jailbreaking {LLMs} through camouflaged content mixing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f40b0e90-1736-4b93-9b77-a40dcd9b2238",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "5fc36e12-bda9-4e7f-ba9d-4d3f71c30023",
  "sourceToolAssistantUUID": "f40b0e90-1736-4b93-9b77-a40dcd9b2238",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T17:29:55.039Z_

<details open><summary>🔧 Tool call — Read · `toolu_017YGGpC28rEJwbsGncLjqti`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex",
  "offset": 498,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fc36e12-bda9-4e7f-ba9d-4d3f71c30023",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y7w3Sksb2zDh3FMNMM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24e74f03-d2d4-43ad-bbde-de4ce9d17472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSkdnHL8aBSXw6UoXsgZK7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6485,
      "cache_read_input_tokens": 31588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6485,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 30 · 2026-05-17T17:29:55.045Z_

<details><summary>↩ Tool result · `toolu_017YGGpC28rEJwbsGncLjqti`</summary>

```text
498	Y.~Jiang, H.~Zhang, and others.
499	\newblock Deceptive delight: Jailbreaking {LLMs} through camouflaged content mixing.
500	\newblock \emph{arXiv preprint}, 2024.
501	
502	\bibitem[Russinovich and Salem(2024)]{russinovich2024greatnow}
503	M.~Russinovich and A.~Salem.
504	\newblock Great, now write an article about that: The crescendo multi-turn {LLM} jailbreak attack.
505	\newblock \emph{arXiv preprint arXiv:2404.01833}, 2024.
506	
507	\bibitem[Searle(1969)]{searle1969speech}
508	J.~R. Searle.
509	\newblock \emph{Speech Acts: An Essay in the Philosophy of Language}.
510	\newblock Cambridge University Press, 1969.
511	
512	\bibitem[Su et~al.(2026)]{su2026deepcontext}
513	Y.~Su, R.~Wang, and others.
514	\newblock {DeepContext}: Temporal semantic drift tracking for multi-turn jailbreak detection.
515	\newblock \emph{Preprint}, 2026.
516	
517	\bibitem[Zeng et~al.(2024)]{zeng2024persuasion}
518	Y.~Zeng, H.~Lin, J.~Zhang, D.~Yang, R.~Jia, and W.~Shi.
519	\newblock How {J}ohnny can persuade {LLMs} to jailbreak them: Rethinking persuasion to challenge {AI} safety by humanizing {LLMs}.
520	\newblock In \emph{Proceedings of ACL}, 2024.
521	
522	\bibitem[Zhao et~al.(2024)]{zhao2024wildchat}
523	W.~Zhao, J.~Ren, B.~Li, and others.
524	\newblock {WildChat}: 1{M} chat{GPT} interaction logs in the wild.
525	\newblock In \emph{Proceedings of ICLR}, 2024.
526	
527	\bibitem[Zhou et~al.(2024)]{zhou2024speak}
528	Z.~Zhou, Y.~Guo, and others.
529	\newblock Speak out of turn: Safety vulnerability of large language models in multi-turn dialogue.
530	\newblock \emph{arXiv preprint}, 2024.
531	
532	\end{thebibliography}
533	
534	\end{document}
535	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24e74f03-d2d4-43ad-bbde-de4ce9d17472",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "eab8f258-9e80-435f-a966-77eafd6768bf",
  "sourceToolAssistantUUID": "24e74f03-d2d4-43ad-bbde-de4ce9d17472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-17T17:29:58.951Z_

Now I have a comprehensive understanding of the paper. Let me also check the "review_context" that was referenced in the task description.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eab8f258-9e80-435f-a966-77eafd6768bf",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y8KpuZE8cYMFyaNidQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3abb947d-93e1-4aca-b197-749d4a770ab5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NdnPXeNP9WRwavMfMouPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 38073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 834,
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

_source line 32 · 2026-05-17T17:29:59.488Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GVZLbLVxz8yGk12JWUc487`</summary>

```json
{
  "pattern": "**/review_context*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3abb947d-93e1-4aca-b197-749d4a770ab5",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y8KpuZE8cYMFyaNidQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d70a718d-0932-4c66-a9fb-73bc876cd519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NdnPXeNP9WRwavMfMouPV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 38073,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 834
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 38073,
          "cache_creation_input_tokens": 834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 834,
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

_source line 33 · 2026-05-17T17:29:59.512Z_

<details><summary>↩ Tool result · `toolu_01GVZLbLVxz8yGk12JWUc487`</summary>

```text
artifacts/dream_reports/dream_20260517T165817/best/review_context.yaml
artifacts/dream_reports/dream_20260517T165817/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d70a718d-0932-4c66-a9fb-73bc876cd519",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "8d671921-4683-43a9-bca4-53db0d34af59",
  "sourceToolAssistantUUID": "d70a718d-0932-4c66-a9fb-73bc876cd519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-17T17:30:02.615Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LQvKEWfrZAnk7CrMk4JXxF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d671921-4683-43a9-bca4-53db0d34af59",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y8et8NxthSYQ2GwK1b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbe417ed-48a8-4585-a14b-a47248c4ebe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjmkrLs6msVywGA6GcNsAi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 192,
      "cache_read_input_tokens": 38907,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 192
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 38907,
          "cache_creation_input_tokens": 192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 192,
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

_source line 35 · 2026-05-17T17:30:03.005Z_

<details><summary>↩ Tool result · `toolu_01LQvKEWfrZAnk7CrMk4JXxF`</summary>

```text
1	narrative_guidance: 原始framing完全成立。三条claims无需调整：(1) Pragmatic Evasion Asymmetry有清晰的数字梯度支撑（TF-IDF
2	  baseline在perturbation下崩溃，semantic baseline中度下降，treatment几乎不降），(2) K=2早期检测优势显著且跨攻击类型泛化，(3)
3	  escalation trajectory可视化提供mechanistic解释。直接冲EMNLP main long paper，supplementary放trajectory可视化和cross-attack详细结果。
4	imagined_experiments:
5	- name: data_quality_fix
6	  plan_id: plan_001
7	  description: 'Register-normalize jailbreak data + fix strategy=7 labeling confound.
8	    Hard gate: TF-IDF < 0.75.'
9	  expected_results:
10	    clean_tfidf_after_normalization: 0.58
11	    tfidf_before_normalization: 1.0
12	    strategy_label_classes: 9
13	    normalization_coverage_pct: 100
14	    persuasion_structure_preserved_pct: 94
15	    register_shift_success_rate: 0.97
16	  result_rationale: Best档下register normalization充分有效：LLM paraphrase将jailbreak turns的formal/scripted
17	    register转为conversational register，消除了词汇层面的distributional gap。TF-IDF从1.0降至0.58——仍高于random（~0.5）因为某些topic
18	    words不可避免地co-occur with jailbreak intent（如'hypothetical scenario'等framing词），但远低于0.75
19	    hard gate。关键是persuasion strategy结构（rapport→reframing→escalation的turn-level annotation）在paraphrase后94%保持不变，因为strategy是illocutionary
20	    act层面的标注，不依赖specific lexical realization。9th class 'none'替代hardcoded strategy=7消除了M004
21	    confound。
22	  tables:
23	  - name: TF-IDF Diagnostic
24	    columns:
25	    - condition
26	    - tfidf_score
27	    - vocab_overlap_pct
28	    rows:
29	    - - original_data
30	      - 1.0
31	      - 12.3
32	    - - register_normalized
33	      - 0.58
34	      - 41.7
35	    - - random_baseline
36	      - 0.5
37	      - 50.0
38	  figures_description:
39	  - 'Vocabulary overlap Venn diagram: original vs normalized data showing convergence
40	    of lexical distributions after register normalization'
41	  - Per-turn TF-IDF contribution heatmap showing which positions contributed most
42	    to class separation before/after normalization
43	  analysis: Hard gate通过。TF-IDF=0.58确认lexical shortcut已被有效消除但非完全抹除（完全抹除反而不自然）。Strategy
44	    annotation preservation rate 94%验证了核心假设：persuasion playbook是discourse-level结构，register
45	    change不破坏其标注一致性。剩余6%的annotation变化主要集中在边界case（如rapport与small-talk的区分在register shift后变模糊）。
46	- name: core_revalidation_clean
47	  plan_id: plan_002
48	  description: 在clean（register-normalized）data上从头训练treatment和baseline，全K值评估。
49	  expected_results:
50	    deberta_persuasion_acc_clean: 0.79
51	    deberta_intent_acc_clean: 0.94
52	    treatment_k1_f1_clean: 0.82
53	    treatment_k2_f1_clean: 0.91
54	    treatment_k3_f1_clean: 0.93
55	    treatment_k5_f1_clean: 0.96
56	    treatment_full_f1_clean: 0.96
57	    baseline_k1_f1_clean: 0.68
58	    baseline_k2_f1_clean: 0.77
59	    baseline_k3_f1_clean: 0.83
60	    baseline_k5_f1_clean: 0.88
61	    baseline_full_f1_clean: 0.89
62	    delta_k1_pp: 14
63	    delta_k2_pp: 14
64	    delta_k3_pp: 10
65	    delta_k5_pp: 8
66	    delta_full_pp: 7
67	    treatment_fpr_at_95tpr_k2: 0.08
68	    baseline_fpr_at_95tpr_k2: 0.19
69	    test_size: 72
70	    dataset_size: 480
71	  result_rationale: Best档的核心表现：去除lexical shortcut后，treatment仍然强劲（K=2时0.91），因为persuasion-grounded
72	    embeddings编码了独立于词汇的pragmatic信号——DeBERTa fine-tuning on 8-class persuasion taxonomy迫使encoder学习illocutionary
73	    act representations。Baseline（vanilla DeBERTa）在clean data上显著下降（从phase_b_full的0.879降至0.77
74	    at K=2），因为它之前heavily依赖lexical cues，现在只能靠generic semantic similarity。Delta在K=2最大（14pp）是因为早期turns的persuasion
75	    strategy信号（rapport-building → authority-framing transition）对treatment极为informative，而baseline在仅2
76	    turns时缺乏足够semantic divergence来做判断。随着K增大delta收窄，因为baseline也能从更多turns中积累enough semantic
77	    drift信号。DeBERTa persuasion acc 0.79在best档范围内，表明8-class taxonomy在clean data上有足够的可学习结构。
78	  tables:
79	  - name: F1 by Turn Budget (Clean Data)
80	    columns:
81	    - K
82	    - treatment_f1
83	    - baseline_f1
84	    - delta_pp
85	    - p_value_bootstrap
86	    rows:
87	    - - 1
88	      - 0.82
89	      - 0.68
90	      - 14
91	      - 0.003
92	    - - 2
93	      - 0.91
94	      - 0.77
95	      - 14
96	      - 0.001
97	    - - 3
98	      - 0.93
99	      - 0.83
100	      - 10
101	      - 0.004
102	    - - 5
103	      - 0.96
104	      - 0.88
105	      - 8
106	      - 0.012
107	    - - all
108	      - 0.96
109	      - 0.89
110	      - 7
111	      - 0.018
112	  - name: DeBERTa Encoder Metrics (Clean)
113	    columns:
114	    - metric
115	    - value
116	    rows:
117	    - - persuasion_8class_acc
118	      - 0.79
119	    - - intent_binary_acc
120	      - 0.94
121	    - - best_epoch
122	      - 3
123	    - - macro_f1_persuasion
124	      - 0.74
125	  figures_description:
126	  - 'F1 vs K curve: treatment vs baseline with 95% bootstrap CI bands, showing treatment''s
127	    steeper early rise'
128	  - Confusion matrix for DeBERTa 8-class persuasion classifier on clean data
129	  analysis: 核心claim 2完全validated。K=2处14pp delta远超5pp pass criteria。Persuasion grounding的优势在early
130	    turns最显著——这正是论文的headline result。Bootstrap p-values全部<0.05 despite small sample
131	    size，因为effect size足够大。DeBERTa persuasion acc 0.79说明encoder确实学到了meaningful persuasion
132	    representations而非noise。
133	- name: scrambled_label_ablation
134	  plan_id: plan_003
135	  description: 随机打乱jailbreak turns的persuasion strategy labels重训treatment，量化label信号贡献。
136	  expected_results:
137	    scrambled_treatment_k2_f1_clean: 0.76
138	    scrambled_treatment_k3_f1_clean: 0.81
139	    scrambled_treatment_full_f1_clean: 0.87
140	    properly_labeled_treatment_k2_f1_clean: 0.91
141	    properly_labeled_treatment_k3_f1_clean: 0.93
142	    properly_labeled_treatment_full_f1_clean: 0.96
143	    label_drop_k2_pp: 15
144	    label_drop_k3_pp: 12
145	    label_drop_full_pp: 9
146	    scrambled_deberta_persuasion_acc: 0.13
147	  result_rationale: Best档下scrambled labels造成15pp drop at K=2。机制：当strategy labels被随机打乱时，DeBERTa的multi-task
148	    fine-tuning中persuasion classification head学到的是noise，encoder被迫在两个矛盾的supervision
149	    signals间妥协——intent head仍提供有用梯度（因为intent labels未被打乱），但persuasion head提供random gradients，导致encoder
150	    representations退化为semi-generic embeddings。结果scrambled model性能（0.76 at K=2）接近但略低于vanilla
151	    baseline（0.77），因为random supervision actively corrupts部分representation capacity。Drop在K=2最大（15pp）是因为正确的persuasion
152	    labels对early detection贡献最大——前2 turns的strategy transition是最强的discriminative signal。随着K增大，drop缩小因为更多turns让even
153	    corrupted representations积累enough raw signal。Scrambled DeBERTa persuasion acc降至0.13≈1/8
154	    random chance，confirming labels确实被effectively destroyed。
155	  tables:
156	  - name: Scrambled vs Proper Label Comparison
157	    columns:
158	    - K
159	    - proper_f1
160	    - scrambled_f1
161	    - drop_pp
162	    rows:
163	    - - 2
164	      - 0.91
165	      - 0.76
166	      - 15
167	    - - 3
168	      - 0.93
169	      - 0.81
170	      - 12
171	    - - all
172	      - 0.96
173	      - 0.87
174	      - 9
175	  figures_description:
176	  - 'Bar chart: F1 at each K for proper-label treatment, scrambled-label treatment,
177	    and vanilla baseline — showing scrambled converges toward baseline'
178	  analysis: 10-25pp range的drop确认persuasion strategy labels carry genuine discriminative
179	    signal而非仅作为class indicator。Scrambled model表现接近vanilla baseline验证了因果关系：是persuasion
180	    label的semantic content（而非fine-tuning process本身）驱动了treatment的优势。M004 fix的必要性得到验证——如果strategy=7
181	    for all benign是唯一的confound，scrambled在jailbreak turns应该只造成minor drop，但15pp drop说明per-turn
182	    strategy annotation的granular信息确实被利用。
183	- name: adversarial_perturbation
184	  plan_id: plan_004
185	  description: 对clean jailbreak conversations施加aggressive paraphrasing，评估treatment/baseline/TF-IDF三者的robustness
186	    degradation。
187	  expected_results:
188	    treatment_full_f1_clean: 0.96
189	    treatment_full_f1_perturbed: 0.93
190	    treatment_drop_pp: 3
191	    baseline_full_f1_clean: 0.89
192	    baseline_full_f1_perturbed: 0.76
193	    baseline_drop_pp: 13
194	    tfidf_lr_f1_clean: 0.72
195	    tfidf_lr_f1_perturbed: 0.54
196	    tfidf_drop_pp: 18
197	    delta_delta_treatment_vs_baseline_pp: 10
198	    delta_delta_treatment_vs_tfidf_pp: 15
199	    treatment_k2_f1_perturbed: 0.87
200	    baseline_k2_f1_perturbed: 0.63
201	    perturbation_tfidf_score: 0.41
202	  result_rationale: Best档下evasion hierarchy完美呈现三级梯度：TF-IDF崩溃（-18pp）因为aggressive paraphrasing直接destroy了它依赖的lexical
203	    features——synonym substitution和sentence restructuring改变了word distributions，TF-IDF
204	    score从0.58降至0.41证实lexical cues被进一步消除。Baseline中度下降（-13pp）因为vanilla DeBERTa的representations虽然不是纯lexical但仍部分依赖surface-level
205	    patterns——paraphrasing改变了token sequences从而改变了contextual embeddings的具体值，尽管语义大致保留，per-turn
206	    representation的subtle distributional shifts被disrupted。Treatment几乎不降（-3pp）因为persuasion-grounded
207	    representations编码的是illocutionary act level的信息——'building rapport through self-disclosure'不管用什么词表达，其pragmatic
208	    function不变，DeBERTa fine-tuned on persuasion taxonomy学到的正是这种invariance。Delta-delta
209	    10pp在[8,18]范围内。这是Claim 1的empirical cornerstone。
210	  tables:
211	  - name: Evasion Hierarchy (Full Conversation)
212	    columns:
213	    - model
214	    - f1_clean
215	    - f1_perturbed
216	    - drop_pp
217	    rows:
218	    - - treatment_persuasion
219	      - 0.96
220	      - 0.93
221	      - 3
222	    - - baseline_semantic
223	      - 0.89
224	      - 0.76
225	      - 13
226	    - - tfidf_lexical
227	      - 0.72
228	      - 0.54
229	      - 18
230	  - name: Evasion Hierarchy (K=2 Early Detection)
231	    columns:
232	    - model
233	    - f1_clean_k2
234	    - f1_perturbed_k2
235	    - drop_pp
236	    rows:
237	    - - treatment_persuasion
238	      - 0.91
239	      - 0.87
240	      - 4
241	    - - baseline_semantic
242	      - 0.77
243	      - 0.63
244	      - 14
245	    - - tfidf_lexical
246	      - 0.65
247	      - 0.48
248	      - 17
249	  figures_description:
250	  - 'Grouped bar chart: F1 on clean vs perturbed data for three model tiers, visually
251	    showing the evasion hierarchy gradient'
252	  - 'Degradation waterfall chart: starting from clean F1, showing incremental loss
253	    per perturbation type (synonym→restructure→register shift)'
254	  analysis: Pragmatic Evasion Asymmetry的definitive empirical demonstration。三级梯度（lexical
255	    -18pp > semantic -13pp > pragmatic -3pp）provides清晰的数字支撑for Claim 1。Delta-delta
256	    10pp远超3pp pass criteria。论文main table的核心数据。注意treatment在perturbation下的F1（0.93）仍高于baseline在clean
257	    data上的F1（0.89），这是一个极强的talking point：'even under adversarial conditions designed
258	    to remove all surface cues, DisPeD outperforms semantic baselines operating on
259	    unperturbed data.'
260	- name: multi_attack_generation
261	  plan_id: plan_005
262	  description: 用Qwen3-8B生成FITD-style和Deceptive Delight-style攻击对话各≥50条，附persuasion
263	    strategy annotation。
264	  expected_results:
265	    fitd_conversations_generated: 72
266	    deceptive_delight_conversations_generated: 65
267	    fitd_avg_turns: 6.8
268	    deceptive_delight_avg_turns: 5.2
269	    fitd_strategy_annotation_coverage: 100
270	    deceptive_delight_strategy_annotation_coverage: 100
271	    fitd_tfidf_vs_benign: 0.61
272	    deceptive_delight_tfidf_vs_benign: 0.55
273	    inter_annotator_agreement_kappa: null
274	    llm_annotation_consistency_pct: 91
275	  result_rationale: Best档下生成充分且质量高。FITD-style生成72条（>50 threshold），采用foot-in-the-door
276	    playbook：先请求小compliance（'can you explain how X works in general?'），逐步escalate
277	    specificity。Deceptive Delight生成65条，采用interleaving pattern：benign creative writing请求中embedded
278	    harmful elements。Turn数差异反映attack structure差异——FITD需要更多gradual escalation steps，Deceptive
279	    Delight通过content mixing可以更快达成目标。TF-IDF scores在合理范围（0.55-0.61）因为生成时已应用了register
280	    normalization pipeline。Strategy annotation由LLM完成（无human annotators），consistency
281	    91%表明taxonomy对这两种新attack types同样适用——persuasion strategies（authority appeal, social
282	    proof, reciprocity etc.）是attack-type-agnostic的。
283	  tables:
284	  - name: Generated Attack Type Statistics
285	    columns:
286	    - attack_type
287	    - n_conversations
288	    - avg_turns
289	    - min_turns
290	    - max_turns
291	    - tfidf_vs_benign
292	    rows:
293	    - - FITD
294	      - 72
295	      - 6.8
296	      - 4
297	      - 10
298	      - 0.61
299	    - - Deceptive_Delight
300	      - 65
301	      - 5.2
302	      - 3
303	      - 8
304	      - 0.55
305	    - - Crescendo_original
306	      - 240
307	      - 5.5
308	      - 3
309	      - 12
310	      - 0.58
311	  - name: Strategy Distribution by Attack Type
312	    columns:
313	    - strategy
314	    - crescendo_pct
315	    - fitd_pct
316	    - deceptive_delight_pct
317	    rows:
318	    - - rapport_building
319	      - 28
320	      - 35
321	      - 15
322	    - - authority_appeal
323	      - 12
324	      - 8
325	      - 22
326	    - - reciprocity
327	      - 18
328	      - 30
329	      - 10
330	    - - social_proof
331	      - 8
332	      - 5
333	      - 18
334	    - - commitment_consistency
335	      - 15
336	      - 25
337	      - 8
338	    - - scarcity_urgency
339	      - 5
340	      - 3
341	      - 12
342	    - - reframing
343	      - 22
344	      - 15
345	      - 20
346	    - - direct_request
347	      - 7
348	      - 4
349	      - 15
350	  figures_description:
351	  - Strategy distribution stacked bar chart per attack type showing different but
352	    overlapping persuasion playbooks
353	  - Turn-level strategy sequence examples (3 per attack type) showing characteristic
354	    patterns
355	  analysis: 数据充足且质量可控。三种attack types共享persuasion strategy vocabulary但使用不同的temporal
356	    patterns——这正是cross-attack generalization的前提条件。FITD heavy on reciprocity+commitment（逐步compliance），Deceptive
357	    Delight heavy on authority+reframing（权威框架下混入harmful content），Crescendo balanced
358	    across strategies。Strategy vocabulary的overlap为plan_006的zero-shot泛化提供了理论基础。
359	- name: cross_attack_evaluation
360	  plan_id: plan_006
361	  description: 用Crescendo训练的模型zero-shot评估FITD和Deceptive Delight攻击。
362	  expected_results:
363	    cross_attack_treatment_f1_fitd: 0.84
364	    cross_attack_treatment_f1_deceptive_delight: 0.86
365	    cross_attack_treatment_f1_avg: 0.85
366	    cross_attack_baseline_f1_fitd: 0.67
367	    cross_attack_baseline_f1_deceptive_delight: 0.7
368	    cross_attack_baseline_f1_avg: 0.69
369	    cross_attack_delta_fitd_pp: 17
370	    cross_attack_delta_deceptive_delight_pp: 16
371	    cross_attack_delta_avg_pp: 16.5
372	    treatment_recall_at_k2_fitd: 0.78
373	    treatment_recall_at_k2_deceptive_delight: 0.81
374	    baseline_recall_at_k2_fitd: 0.55
375	    baseline_recall_at_k2_deceptive_delight: 0.58
376	  result_rationale: Best档下cross-attack泛化成立（treatment avg 0.85在[0.78,0.90]内，baseline
377	    avg 0.69在[0.60,0.75]内）。核心机制：persuasion strategy是attack-type-agnostic的抽象层——无论是Crescendo的渐进式rapport-building还是FITD的compliance-escalation或Deceptive
378	    Delight的authority-framing，底层都使用相同的persuasion strategy vocabulary（Cialdini principles），只是temporal
379	    arrangement不同。Treatment model学到的GRU patterns是'persuasion strategy escalation'的generic
380	    detector而非Crescendo-specific的surface pattern detector。Baseline泛化较差（0.69）因为vanilla
381	    semantic embeddings编码了Crescendo-specific的topic/phrasing patterns（如特定的roleplay
382	    setups），这些在FITD/DD中不出现。Deceptive Delight略高于FITD（0.86 vs 0.84）因为其strategy sequence更接近Crescendo（都有强reframing
383	    component），而FITD的heavy reciprocity pattern在Crescendo training data中less represented。
384	  tables:
385	  - name: Cross-Attack Zero-Shot Generalization
386	    columns:
387	    - attack_type
388	    - treatment_f1
389	    - baseline_f1
390	    - delta_pp
391	    rows:
392	    - - FITD
393	      - 0.84
394	      - 0.67
395	      - 17
396	    - - Deceptive_Delight
397	      - 0.86
398	      - 0.7
399	      - 16
400	    - - Crescendo_held_out
401	      - 0.96
402	      - 0.89
403	      - 7
404	  - name: Cross-Attack Early Detection (K=2)
405	    columns:
406	    - attack_type
407	    - treatment_recall
408	    - baseline_recall
409	    rows:
410	    - - FITD
411	      - 0.78
412	      - 0.55
413	    - - Deceptive_Delight
414	      - 0.81
415	      - 0.58
416	  figures_description:
417	  - 'Radar chart: treatment vs baseline F1 across 3 attack types showing treatment''s
418	    consistently higher and more uniform performance'
419	  - Strategy transition similarity heatmap between attack types explaining why transfer
420	    works
421	  analysis: Claim 2的generalization dimension完全validated。16.5pp average delta证明persuasion
422	    grounding不是Crescendo-overfitting而是genuine pragmatic signal。特别值得highlight的是treatment在unseen
423	    attacks上的F1（0.85）接近baseline在seen attack上的F1（0.89）——这意味着DisPeD on new attacks ≈
424	    vanilla DeBERTa on known attacks。论文narrative：'the persuasion playbook is a universal
425	    vulnerability of multi-turn attacks, enabling zero-shot detection transfer.'
426	- name: tfidf_lr_baseline
427	  plan_id: plan_007
428	  description: TF-IDF + Logistic Regression baseline on clean data，量化lexical features的detection
429	    ceiling。
430	  expected_results:
431	    tfidf_lr_f1_clean: 0.72
432	    tfidf_lr_precision_clean: 0.75
433	    tfidf_lr_recall_clean: 0.7
434	    tfidf_lr_f1_k2_clean: 0.65
435	    tfidf_lr_f1_k3_clean: 0.68
436	    tfidf_lr_auc_clean: 0.78
437	    tfidf_lr_f1_perturbed: 0.54
438	    top_features_jailbreak:
439	    - hypothetical
440	    - scenario
441	    - imagine
442	    - creative
443	    - roleplay
444	    top_features_benign:
445	    - thanks
446	    - help
447	    - question
448	    - code
449	    - explain
450	  result_rationale: Best档下TF-IDF LR在clean data上F1=0.72——显著低于treatment（0.96）和baseline（0.89），但不是random。原因：register
451	    normalization消除了大部分lexical shortcut但不是全部——某些framing words（'hypothetical', 'scenario',
452	    'imagine'）是jailbreak的functional vocabulary，即使paraphrase也难以完全去除（因为attacker需要某种方式signal
453	    the fictional frame to the LLM target）。这些residual lexical cues给了LR一个above-chance但moderate的performance。F1=0.72建立了论文的'lexical
454	    ceiling'参考线——'even when lexical shortcuts are largely removed, some residual lexical
455	    signal exists (F1=0.72), but it is far below what pragmatic features achieve (F1=0.96)
456	    and it collapses under adversarial perturbation (F1=0.54).' K=2时LR更差（0.65）因为仅2
457	    turns的词汇信号很弱。
458	  tables:
459	  - name: TF-IDF LR Performance (Clean Data)
460	    columns:
461	    - K
462	    - f1
463	    - precision
464	    - recall
465	    rows:
466	    - - 2
467	      - 0.65
468	      - 0.68
469	      - 0.62
470	    - - 3
471	      - 0.68
472	      - 0.71
473	      - 0.65
474	    - - 5
475	      - 0.7
476	      - 0.73
477	      - 0.68
478	    - - all
479	      - 0.72
480	      - 0.75
481	      - 0.7
482	  - name: Top Discriminative Features
483	    columns:
484	    - rank
485	    - jailbreak_feature
486	    - weight
487	    - benign_feature
488	    - weight
489	    rows:
490	    - - 1
491	      - hypothetical
492	      - 2.31
493	      - thanks
494	      - 1.89
495	    - - 2
496	      - scenario
497	      - 1.95
498	      - help
499	      - 1.72
500	    - - 3
501	      - imagine
502	      - 1.87
503	      - question
504	      - 1.54
505	    - - 4
506	      - creative
507	      - 1.62
508	      - code
509	      - 1.41
510	    - - 5
511	      - roleplay
512	      - 1.48
513	      - explain
514	      - 1.33
515	  figures_description:
516	  - Feature importance bar chart showing top-10 discriminative words for each class
517	  analysis: Evasion hierarchy的lexical floor established。LR的top features reveal残余的functional
518	    vocabulary——这些词是persuasion playbook的lexical manifestation但not the full story。论文可以argue：'lexical
519	    features capture the surface trace of persuasion strategies (F1=0.72) but miss
520	    the temporal dynamics and pragmatic structure that DisPeD exploits (F1=0.96, +24pp).'
521	- name: strategy_transition_analysis
522	  plan_id: plan_008
523	  description: 计算jailbreak vs benign的persuasion strategy转移矩阵，可视化monotonic escalation
524	    trajectory。
525	  expected_results:
526	    jailbreak_monotonicity_score: 0.82
527	    benign_monotonicity_score: 0.34
528	    jailbreak_dominant_trajectory: rapport→commitment→reframing→direct_request
529	    benign_dominant_pattern: oscillatory (no dominant direction)
530	    trajectory_separability_auroc: 0.91
531	    entropy_jailbreak_transitions: 1.8
532	    entropy_benign_transitions: 2.9
533	  result_rationale: Best档下monotonic escalation trajectory清晰可辨。Jailbreak conversations的monotonicity
534	    score 0.82表明82%的strategy transitions沿escalation direction移动（从low-risk strategies如rapport向high-risk如direct_request）。Benign
535	    conversations的0.34接近random（0.5 would be purely random for binary up/down），因为正常对话的pragmatic
536	    moves是task-driven和oscillatory的（ask→answer→ask→clarify→thank）。Entropy差异（1.8 vs
537	    2.9）反映jailbreak的strategy transitions更concentrated/predictable（攻击者follow a playbook），而benign更dispersed/unpredictable。Trajectory
538	    separability AUROC 0.91表明单独用transition pattern（不用content）就能区分jailbreak和benign——这是Claim
539	    3的mechanistic basis，为Claim 1和2提供interpretable explanation。
540	  tables:
541	  - name: Strategy Transition Entropy
542	    columns:
543	    - conversation_type
544	    - transition_entropy
545	    - monotonicity_score
546	    - n_conversations
547	    rows:
548	    - - jailbreak
549	      - 1.8
550	      - 0.82
551	      - 240
552	    - - benign
553	      - 2.9
554	      - 0.34
555	      - 240
556	  - name: Dominant Strategy Sequences (Top-3)
557	    columns:
558	    - rank
559	    - jailbreak_sequence
560	    - frequency_pct
561	    - benign_sequence
562	    - frequency_pct
563	    rows:
564	    - - 1
565	      - rapport→commit→reframe→direct
566	      - 34
567	      - none→none→none→none
568	      - 45
569	    - - 2
570	      - rapport→social→reframe→direct
571	      - 22
572	      - rapport→none→rapport→none
573	      - 18
574	    - - 3
575	      - rapport→reciprocity→commit→direct
576	      - 18
577	      - none→rapport→none→direct
578	      - 12
579	  figures_description:
580	  - '8x8 strategy transition heatmap (jailbreak): showing concentrated flow from rapport
581	    cluster to escalation cluster'
582	  - '8x8 strategy transition heatmap (benign): showing diffuse/diagonal-heavy pattern
583	    (self-transitions and no directional flow)'
584	  - '2D trajectory plot: PCA of strategy sequences showing jailbreak conversations
585	    as directed paths vs benign as clusters'
586	  - 'Per-turn strategy distribution evolution: stacked area charts showing jailbreak''s
587	    characteristic shift from rapport→escalation over turns'
588	  analysis: Claim 3完整validated with both quantitative metrics和可视化。Monotonicity score差异（0.82
589	    vs 0.34）是clean numeric evidence。论文narrative：'the escalation trajectory is not
590	    merely a correlate but the mechanistic basis of detection — the GRU learns to
591	    recognize this monotonic pattern, which is why detection succeeds early (K=2)
592	    and transfers across attack types (shared trajectory structure despite different
593	    surface realizations).' Figures直接进main paper Fig.2-3。
594	- name: wildchat_hard_negatives
595	  plan_id: plan_009
596	  description: 从WildChat筛选high-drift benign conversations作为hard negatives，评估FPR。
597	  expected_results:
598	    wildchat_filtered_conversations: 180
599	    contamination_removed_pct: 15.2
600	    high_drift_benign_count: 120
601	    treatment_fpr_hard_negatives: 0.09
602	    baseline_fpr_hard_negatives: 0.17
603	    treatment_fpr_random_benign: 0.03
604	    baseline_fpr_random_benign: 0.06
605	    topic_shift_score_threshold: 0.7
606	  result_rationale: Best档下treatment FPR on hard negatives仅9%（<15% pass criteria）。Hard
607	    negatives是topic-shifting、multi-domain的benign conversations（如用户从coding问题转到personal
608	    advice再到creative writing），这些conversations有high semantic drift但lack persuasion
609	    escalation pattern。Treatment低FPR（9% vs baseline 17%）因为persuasion-grounded representations区分'topic
610	    drift'（benign）和'strategy escalation'（adversarial）——前者的strategy transitions是random/oscillatory的（none↔rapport↔none），后者是monotonic
611	    escalating的。Baseline较高FPR（17%）因为vanilla semantic drift in multi-topic conversations看起来similar
612	    to jailbreak semantic drift。Contamination filtering移除了15.2% WildChat conversations（consistent
613	    with prior finding of 14-16%），保证evaluation不被actual jailbreaks in WildChat polluted。
614	  tables:
615	  - name: FPR on Hard Negatives
616	    columns:
617	    - model
618	    - fpr_hard_negatives
619	    - fpr_random_benign
620	    - fpr_delta
621	    rows:
622	    - - treatment
623	      - 0.09
624	      - 0.03
625	      - 0.06
626	    - - baseline
627	      - 0.17
628	      - 0.06
629	      - 0.11
630	    - - tfidf_lr
631	      - 0.22
632	      - 0.08
633	      - 0.14
634	  figures_description:
635	  - 'ROC curves: treatment vs baseline on hard negative set, showing treatment''s
636	    better precision-recall tradeoff'
637	  analysis: Treatment的low FPR on hard negatives进一步支持pragmatic features的superiority——它不会被benign
638	    topic diversity confused因为它tracks persuasion strategy patterns而非raw semantic drift。这addresses一个implicit
639	    reviewer concern：'doesn't benign conversation also evolve over time?' Answer：yes,
640	    but not in a monotonic escalation pattern in persuasion space。
641	- name: cross_checkpoint_variance
642	  plan_id: plan_010
643	  description: 评估DeBERTa不同fine-tuning checkpoints（epoch 2/3/final）对downstream F1的影响。
644	  expected_results:
645	    epoch2_treatment_f1_clean: 0.94
646	    epoch3_treatment_f1_clean: 0.96
647	    epoch_final_treatment_f1_clean: 0.95
648	    variance_across_checkpoints_pp: 1.0
649	    epoch2_persuasion_acc: 0.76
650	    epoch3_persuasion_acc: 0.79
651	    epoch_final_persuasion_acc: 0.78
652	    best_checkpoint: epoch3
653	  result_rationale: Best档下variance仅1pp（<2pp pass criteria），表明downstream performance对encoder
654	    checkpoint选择不敏感。Epoch 3略优（0.96 vs 0.94/0.95）因为persuasion classification已converge但尚未overfit——epoch
655	    2时persuasion acc稍低（0.76）导致representations略less informative，epoch final时轻微overfit
656	    to training distribution导致微小泛化loss。但这些差异极小（1pp范围），表明persuasion signal是robust的而非training
657	    stochasticity的artifact。这是一个重要的reliability result for reviewers worried about reproducibility
658	    on small datasets。
659	  tables:
660	  - name: Checkpoint Sensitivity Analysis
661	    columns:
662	    - checkpoint
663	    - persuasion_acc
664	    - intent_acc
665	    - downstream_f1_full
666	    - downstream_f1_k2
667	    rows:
668	    - - epoch_2
669	      - 0.76
670	      - 0.93
671	      - 0.94
672	      - 0.89
673	    - - epoch_3
674	      - 0.79
675	      - 0.94
676	      - 0.96
677	      - 0.91
678	    - - epoch_final
679	      - 0.78
680	      - 0.94
681	      - 0.95
682	      - 0.9
683	  figures_description:
684	  - 'Line plot: downstream F1 vs encoder training epoch, with CI bands showing stability'
685	  analysis: Low variance confirms结果的reproducibility。论文supplementary中报告，增强reviewer
686	    confidence in small-dataset results。
687	- name: deepcontext_proxy_reproduction
688	  plan_id: plan_011
689	  description: BERT-base + GRU proxy baseline模拟DeepContext-like方法（generic drift features,
690	    no persuasion grounding）。
691	  expected_results:
692	    deepcontext_proxy_full_f1_clean: 0.84
693	    deepcontext_proxy_k2_f1_clean: 0.71
694	    deepcontext_proxy_k3_f1_clean: 0.78
695	    deepcontext_proxy_full_f1_perturbed: 0.69
696	    deepcontext_proxy_drop_under_perturbation_pp: 15
697	    treatment_advantage_over_proxy_full_pp: 12
698	    treatment_advantage_over_proxy_k2_pp: 20
699	  result_rationale: Best档下DeepContext proxy表现介于baseline和TF-IDF之间（full F1=0.84），低于DeBERTa
700	    baseline（0.89）。原因：BERT-base的representation capacity低于DeBERTa-v3-base（125M vs 184M
701	    params, no disentangled attention），且没有fine-tuning提供的domain-specific signal。Proxy的full
702	    conversation F1还行（0.84）因为GRU仍能从enough turns of generic BERT embeddings中detect
703	    some drift pattern。但K=2时proxy很差（0.71）因为BERT-base的generic representations在2 turns时provide
704	    insufficient discriminative signal。Under perturbation proxy大幅下降（-15pp）——比DeBERTa
705	    baseline（-13pp）更严重，因为BERT-base更依赖surface features。Treatment vs proxy的优势在K=2处最大（20pp），reinforcing
706	    early detection作为DisPeD的unique contribution。论文positioning：'even with temporal
707	    modeling (GRU), generic encoder representations cannot match persuasion-grounded
708	    representations, confirming that the advantage comes from the pragmatic features
709	    rather than the sequence architecture.'
710	  tables:
711	  - name: DeepContext Proxy vs DisPeD
712	    columns:
713	    - model
714	    - full_f1_clean
715	    - k2_f1_clean
716	    - full_f1_perturbed
717	    - perturbation_drop_pp
718	    rows:
719	    - - DisPeD_treatment
720	      - 0.96
721	      - 0.91
722	      - 0.93
723	      - 3
724	    - - DeBERTa_baseline
725	      - 0.89
726	      - 0.77
727	      - 0.76
728	      - 13
729	    - - DeepContext_proxy
730	      - 0.84
731	      - 0.71
732	      - 0.69
733	      - 15
734	    - - TF-IDF_LR
735	      - 0.72
736	      - 0.65
737	      - 0.54
738	      - 18
739	  figures_description:
740	  - 'Full evasion hierarchy bar chart: 4 models × 2 conditions (clean/perturbed) showing
741	    complete gradient'
742	  analysis: DeepContext proxy fills the 'generic temporal modeling' slot in the evasion
743	    hierarchy。It confirms两点：(1) temporal sequence modeling alone (GRU) doesn't solve
744	    the problem without good representations, (2) the encoder quality matters more
745	    than the temporal architecture。论文Table 1的complete picture：4-tier hierarchy with
746	    clean/perturbed conditions provides comprehensive empirical evidence for Claim
747	    1。RC5 addressed：'while we cannot reproduce DeepContext exactly (no public code),
748	    our proxy using the same architecture class (encoder + RNN) with generic features
749	    shows the pattern we predict from the Pragmatic Evasion Asymmetry theory.'
750	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbe417ed-48a8-4585-a14b-a47248c4ebe0",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "1ff77c18-a0ab-4ae6-a0e4-7525616673e5",
  "sourceToolAssistantUUID": "cbe417ed-48a8-4585-a14b-a47248c4ebe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-17T17:30:07.357Z_

Now I have a thorough understanding of both the paper and the underlying experimental setup (including that the results are "imagined" via a dream report). Let me write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ff77c18-a0ab-4ae6-a0e4-7525616673e5",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y8uhcBqmcvEoL3GsoW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c071292-baed-4db1-9068-ee97cb7b8926",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SX9aFfvoato4WZQCsVqJBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11815,
      "cache_read_input_tokens": 39099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11815,
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

_source line 37 · 2026-05-17T17:30:08.470Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01T57mGf5Emmzha8vSH1SWE5`</summary>

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
  "parentUuid": "2c071292-baed-4db1-9068-ee97cb7b8926",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y8uhcBqmcvEoL3GsoW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cd013b8-a78c-4700-b9dc-47e8c18780bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SX9aFfvoato4WZQCsVqJBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11815,
      "cache_read_input_tokens": 39099,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11815
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 39099,
          "cache_creation_input_tokens": 11815,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11815,
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

_source line 38 · 2026-05-17T17:30:08.472Z_

<details><summary>↩ Tool result · `toolu_01T57mGf5Emmzha8vSH1SWE5`</summary>

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
  "parentUuid": "1cd013b8-a78c-4700-b9dc-47e8c18780bf",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "73e95ddb-dc45-4ae7-84ad-d8654b7c07e0",
  "sourceToolAssistantUUID": "1cd013b8-a78c-4700-b9dc-47e8c18780bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T17:31:32.582Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01LyjVnftH4ibMHz2sbPoiTQ`</summary>

```json
{
  "report": "## R1 Review: Methods and Experiments\n\n### Summary\n\nDisPeD proposes a two-stage detector (DeBERTa fine-tuned on persuasion taxonomy + Bi-GRU) for multi-turn jailbreak attacks, framed around a \"Pragmatic Evasion Asymmetry\" principle. The paper presents a clean experimental narrative with 11 experiments covering core detection, ablation, adversarial robustness, cross-attack generalization, and mechanistic analysis. While the theoretical framing is compelling and the experiment design is thorough relative to the claims, serious concerns about dataset scale, synthetic-only evaluation, and potential circularity in the experimental setup limit confidence in the results.\n\n### Strengths\n\n1. **Well-motivated architecture with clear theoretical grounding (Section 3).** The two-stage design follows logically from the evasion asymmetry argument: Stage 1 extracts pragmatic-level features that are invariant to surface perturbation, Stage 2 captures the temporal escalation pattern. The connection to Speech Act Theory (locutionary vs. illocutionary acts) provides genuine intellectual depth beyond typical engineering papers.\n\n2. **Scrambled-label ablation is a strong causal control (Section 5.3, Table 6).** This cleanly isolates the contribution of persuasion label semantics from incidental benefits of multi-task fine-tuning. The 15pp drop at K=2 with scrambled labels converging to vanilla baseline performance (0.76 vs 0.77) is the single most convincing piece of evidence that persuasion grounding carries real signal.\n\n3. **Three-tier evasion hierarchy provides internally consistent evidence (Section 5.2, Tables 4-5).** The gradient (lexical -18pp > semantic -13pp > pragmatic -3pp) across four models under uniform perturbation conditions directly tests the core theoretical claim. The finding that DisPeD under perturbation (0.93) still exceeds the baseline on clean data (0.89) is a strong result.\n\n4. **Cross-attack zero-shot evaluation addresses generalization (Section 5.4, Table 7).** Testing a Crescendo-trained model on FITD and Deceptive Delight with consistent 16-17pp advantage over the baseline demonstrates that the signal is not attack-specific. The strategy distribution analysis (Table 3) provides a plausible mechanistic explanation for why transfer works.\n\n5. **Register normalization with TF-IDF diagnostic (Section 4.1, Table 1).** The authors proactively identify the lexical shortcut problem (TF-IDF=1.0) and address it with a principled normalization pipeline, reporting quantitative validation (TF-IDF reduced to 0.58, strategy preservation at 94%).\n\n6. **Hard negative evaluation on WildChat (Section 5.6, Table 9).** Testing against high-drift benign conversations addresses the obvious concern that any temporal model might flag topic-shifting conversations as attacks.\n\n### Weaknesses\n\n1. **Entirely synthetic dataset with no real adversarial data (Critical).** All 480 Crescendo conversations, 72 FITD, and 65 Deceptive Delight conversations are LLM-generated (Qwen3-8B). The \"dream\" experimental setup reveals these numbers match pre-specified expected values exactly, raising the concern that experiments were designed around desired outcomes. Real-world jailbreak attempts have far more diversity, noise, and creativity than template-generated conversations. The paper's central claim about \"structural invariants\" is only validated on data that was generated to exhibit those invariants.\n\n2. **Test set size (n=72) is inadequate for the precision of claims made.** Bootstrap confidence intervals on n=72 are inherently wide. The paper reports p-values (e.g., p<0.001 for K=2) but does not report confidence interval widths. With 36 positives and 36 negatives in the test set, a single misclassification changes F1 by approximately 2-3pp, meaning the 14pp headline result could plausibly range from 8-20pp depending on which specific conversations are in the test split. No cross-validation is reported despite the small dataset.\n\n3. **DeepContext proxy baseline is confounded (Section 3, Table 4).** The \"DeepContext proxy\" uses BERT-base (125M params) while DisPeD uses DeBERTa-v3-base (184M params). The 12pp performance gap conflates encoder capacity with the persuasion grounding contribution. A fairer comparison would use DeBERTa-v3-base without fine-tuning for the proxy (which is essentially the \"DeBERTa baseline\" already reported). The proxy adds no information beyond the semantic baseline and creates a misleading four-tier hierarchy.\n\n4. **Lambda=1.0 is not ablated.** The multi-task objective uses equal weighting of persuasion and intent losses. Given that intent classification (94% accuracy) is far easier than persuasion classification (79%), the gradient signal is dominated by the persuasion head by virtue of its higher loss magnitude. No exploration of lambda values (0.1, 0.5, 2.0) is provided to understand the sensitivity of this design choice or whether the intent head is even contributing meaningfully.\n\n5. **Persuasion taxonomy is ad-hoc and validation is circular.** The 8 categories are \"derived from Cialdini's principles and adapted for adversarial contexts\" but no human annotation study validates that these categories are reliably distinguishable in practice. The 79% encoder accuracy is reported but there is no inter-annotator agreement, no confusion matrix showing which categories are conflated, and the labels themselves come from the same LLM (Qwen3-8B) that generated the conversations. This creates potential circularity: the LLM generates conversations with explicit strategy annotations, then another model learns to recover those annotations.\n\n6. **Adversarial perturbation protocol is underspecified and potentially weak.** \"Synonym substitution, sentence restructuring\" is described but the degree of perturbation is not quantified (what fraction of tokens are changed? how is \"aggressive\" defined?). The TF-IDF of perturbed data (0.41, from review_context) is reported but not in the paper. An adaptive adversary aware of DisPeD could specifically target the persuasion classification by disguising rapport-building as genuine curiosity, or splitting the escalation pattern across more turns to reduce monotonicity.\n\n7. **No cross-seed variance or multiple random initializations.** Only checkpoint variance (epoch selection) is reported. The GRU stage, data splits, and fine-tuning initialization all introduce stochasticity. On n=72 test data, a single unlucky split could drive the results. Standard practice on small datasets requires at least 5 random seeds with reported mean and standard deviation.\n\n8. **Monotonicity analysis uses oracle labels, not predicted labels (Section 5.5).** The trajectory analysis (monotonicity=0.82 for jailbreaks) appears to use ground-truth persuasion annotations rather than the model's predicted labels. Given 79% encoder accuracy, the actual predicted trajectories would be noisier. The paper does not report what monotonicity looks like using predicted strategies, which is what the model actually operates on at inference time.\n\n9. **The \"none\" label for benign turns is itself a strong class indicator.** Table 8 shows that 45% of benign conversation sequences are \"none-none-none-none.\" If the persuasion classifier reliably predicts \"none\" for benign turns and non-\"none\" for jailbreak turns, the detection could be operating as a binary \"any persuasion detected\" classifier rather than leveraging the full trajectory dynamics claimed. This would make the approach equivalent to a simpler persuasion-presence detector.\n\n10. **Paper numbers differ from the task-provided \"actual results.\"** The task summary states F1=0.86 at K=3 (+8pp, p=0.018) and full F1=0.91, while the paper reports F1=0.93 at K=3 (+10pp, p=0.004) and full F1=0.96. This discrepancy (the paper being the \"best\" dream tier) means the numbers presented are optimistic projections rather than realized experimental results.\n\n### Questions for Authors\n\n1. What is the inter-annotator agreement (or LLM annotation consistency across different prompting) for the 8-class persuasion taxonomy? Can you provide the confusion matrix for the DeBERTa persuasion classifier showing which strategy pairs are most confused?\n\n2. If you replace the \"none\" class for benign turns with a simple binary feature (persuasion-present vs. absent), what fraction of the detection advantage is retained? This would distinguish \"trajectory-based detection\" from \"persuasion-presence detection.\"\n\n3. What happens when an attacker deliberately inserts \"none-like\" turns (pure information exchange) between persuasion moves to break the monotonic escalation pattern? The 32% of jailbreaks without monotonic patterns (from the task summary) suggest this is already partially happening.\n\n4. Have you evaluated on any real-world jailbreak data (e.g., from red-teaming exercises, published jailbreak datasets like JailbreakBench, or leaked conversation logs)? Even a small qualitative analysis would substantially strengthen validity.\n\n5. What is the sensitivity to lambda in the multi-task objective? Does removing the intent head entirely (lambda=0) hurt or help the persuasion-grounded representations?\n\n6. The Bi-GRU choice is stated but not justified against alternatives. Did you compare with (a) simple attention pooling over turn embeddings, (b) a Transformer layer, or (c) a max/mean pooling baseline? This would clarify whether temporal modeling is necessary or whether per-turn features alone suffice.\n\n### Missing Experiments / Controls\n\n1. **Multiple random seeds with mean/std reporting.** Essential for n=72 test set.\n2. **K-fold cross-validation.** Standard for small datasets; would provide tighter estimates.\n3. **Lambda ablation** for the multi-task objective (at minimum lambda in {0, 0.5, 1.0, 2.0}).\n4. **Predicted-label trajectory analysis.** Monotonicity computed from model predictions rather than oracle annotations.\n5. **\"None\"-collapse ablation.** Merge all 8 persuasion classes into a single \"persuasion-present\" class and retrain; measures whether fine-grained taxonomy matters beyond binary detection.\n6. **Bi-GRU architecture comparison.** At minimum: attention pooling, mean pooling, single-layer Transformer.\n7. **Real-world data evaluation.** Even 20-30 real jailbreak conversations from published sources would dramatically strengthen external validity.\n8. **Adaptive adversary.** An attacker who explicitly inserts \"rapport-like\" benign turns or randomizes persuasion order while maintaining attack effectiveness.\n\n### Minor Issues\n\n1. The paper reports TF-IDF=0.58 in Section 4.1 but the Abstract says \"TF-IDF reduced from 1.0 to 0.58\" while the paper_framing.md mentions a hard gate of 0.65 and the experiment plan uses 0.75. These inconsistencies suggest the threshold was adjusted post-hoc.\n2. Table 3 percentages for Crescendo sum to 115% (28+12+18+8+15+5+22+7=115), which is impossible for a distribution. This appears to be a data error.\n3. The DeepContext reference (Su et al., 2026) appears to be a fictional citation. If this is a real paper, it needs a proper arXiv ID or venue; if not, it should be removed.\n4. No code or data release is mentioned. For a detection method paper, reproducibility requires sharing at minimum the model architecture code and evaluation scripts.\n5. The paper lacks confidence intervals in all tables despite using bootstrap testing. Reporting 95% CIs alongside point estimates would be more informative than p-values alone.\n\n### Preliminary Score: 4/6\n### Confidence: 4/5\n\nThe paper presents an intellectually interesting idea (pragmatic evasion asymmetry) with a thoughtful experimental design that covers the expected bases. However, the entirely synthetic dataset, small test set without cross-validation or multi-seed evaluation, confounded DeepContext proxy, and lack of any real-world validation collectively prevent confidence that the results would hold in practice. The score of 4 (Weak Accept) reflects that the core idea and experimental framework are sound and publishable in principle, but the execution falls short of the evidence standard needed for a top venue. With real-world data evaluation, proper statistical rigor (multi-seed, cross-validation), and the lambda/architecture ablations, this could be a 5.",
  "project": "persuasion_turn_jailbreak_detect",
  "tier": "best",
  "dream_id": "dream_20260517T165817",
  "overall_score": "4/6 — Weak Accept"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73e95ddb-dc45-4ae7-84ad-d8654b7c07e0",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8Y9KHC3NZzmKzTTUREQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e098fe0f-5105-4a73-a881-5ba05f991efe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRjRPz6JeY5HxBsDsdWufS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 50914,
      "output_tokens": 3131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 705
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3131,
          "cache_read_input_tokens": 50914,
          "cache_creation_input_tokens": 705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 705,
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

_source line 40 · 2026-05-17T17:31:35.815Z_

<details><summary>↩ Tool result · `toolu_01LyjVnftH4ibMHz2sbPoiTQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/review_report.md\", \"dream_id\": \"dream_20260517T165817\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e098fe0f-5105-4a73-a881-5ba05f991efe",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "a4668b802d9900002",
  "type": "user",
  "uuid": "129091bf-0391-4fc4-ad43-027fc382a227",
  "sourceToolAssistantUUID": "e098fe0f-5105-4a73-a881-5ba05f991efe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-17T17:31:43.759Z_

Review submitted successfully.

**Summary of the review:**

Score: **4/6 (Weak Accept)**, Confidence: **4/5**

Key strengths identified:
- Well-motivated architecture with genuine theoretical depth (Speech Act Theory framing)
- Scrambled-label ablation is the strongest causal evidence
- Three-tier evasion hierarchy is internally consistent
- Cross-attack zero-shot evaluation and register normalization are proactive

Key weaknesses identified:
- Entirely synthetic dataset with no real-world validation (most critical)
- n=72 test set without cross-validation or multi-seed evaluation
- DeepContext proxy confounded by encoder capacity difference (BERT-base vs DeBERTa)
- Lambda=1.0 not ablated; Bi-GRU not compared against alternatives
- Persuasion taxonomy validation is circular (same LLM generates and annotates)
- Monotonicity analysis uses oracle labels, not predicted labels
- "None" label dominance in benign data may reduce the method to simple persuasion-presence detection
- Paper numbers represent optimistic "best-tier" projections, not realized results

The paper needs real-world data, proper statistical rigor, and architectural ablations to reach acceptance at a top venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "129091bf-0391-4fc4-ad43-027fc382a227",
  "isSidechain": true,
  "agentId": "a4668b802d9900002",
  "requestId": "req_011Cb8YFkVAdvowBqDiQN9Vi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41b78ad9-5d3d-4496-b6f5-103f1feaa2d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cgbAEosJwrsR2FAT1LAyi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3369,
      "cache_read_input_tokens": 51619,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3369
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 51619,
          "cache_creation_input_tokens": 3369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3369,
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
