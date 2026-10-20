# Research conversation: You are the Review Chair synthesizing two independent reviews of an ML paper into a final consolidated report. You must 

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8e8084a82516c7ec.jsonl`
- **Structured JSON:** [`6c5aafd3d79e32bc5096.json`](../../sessions/6c/6c5aafd3d79e32bc5096.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-14T10:21:56.544Z_

You are the Review Chair synthesizing two independent reviews of an ML paper into a final consolidated report. You must produce the final review for submission via submit_dream_review_report.

## Paper
**Title:** Solver Trace Ablation Reveals Reward Hacking in GRPO-Trained Formal Reasoners: Diagnosis, Taxonomy, and Goodhart's Law

**Claims:**
1. ISR as Diagnostic: exec-only GRPO PR rises 32%→96% while ISR collapses 0.64→0.003 over 1000 steps. 5 hacking strategies identified.
2. ISR as Reward (Goodhart): At β=0.1 additive bonus, directional ISR improvement (mean ratio ~2.1× over random, 3 seeds), but 95% CI [0.85, 3.45] crosses 1.0; genuine rate delta +3.7pp not significant. At β=0.3, Goodhart collapse.
3. Cross-Logic Transfer: STA mechanically transfers to Prolog, ISR diagnostic power weaker. Presented as preliminary.

Additional: O(1) vs O(N) ablation (negative), curriculum ablation, SFT baseline, multi-logic training (negative), cross-logic zero-shot transfer (null), 1.5B vs 8B scaling (single seed), seed variability as finding.

## Experiment Coverage Assessment

From the review_context.yaml (imagined experiment list), the paper covers 14/15 planned experiments:
- ISR β=0.1 seeds 42,43,44 ✓ (Tables 3-5)
- Random β=0.1 seeds 42,43,44 ✓ (Tables 3-5)
- 3-seed aggregate ✓ (Table 4)
- O(1) vs O(N) ✓ (Table 8)
- Prolog exec-only 3 seeds ✓ (Table 10)
- Prolog exec+STA 3 seeds ✓ (Table 10)
- Multi-logic joint training ✓ (Table 11)
- Cross-logic transfer ✓ (Table 12)
- SFT baseline ✓ (Table 7)
- Qwen3-8B scaling ✓ (Table 13, single seed)
- Hacking taxonomy ✓ (Section 3.4, Appendix A)
- Curriculum ablation ✓ (Table 9)
- SMT-LIB ✗ (acknowledged in Limitations)

The paper's reported numbers match the review_context expected results exactly for all covered experiments.

## R1 Review (Methods + Experiments) — CORRECTED

After removing hallucinated concerns (R1 cited numbers not present in the paper), the valid R1 findings are:

**Strengths:**
1. ISR is cleanly defined and the diagnostic application is sound. LOO formulation is unambiguous and reproducible.
2. Matched random controls isolate ISR's structural signal from variance-injection effects.
3. Honest reporting of negative results (O(1) failure, NLI null, curriculum negative, cross-logic null, multi-logic interference).
4. Comprehensive experimental matrix: 7 conditions, multiple seeds, SFT baseline, scaling, ablations.
5. ISR collapse trajectory (0.64→0.13→0.003) is a compelling empirical finding.

**Valid Weaknesses:**
1. Only 3 seeds with extreme inter-seed variance. 95% CI crosses 1.0 for the ISR ratio. Paper acknowledges this and does NOT make significance claims.
2. Only 2 beta values (0.1, 0.3) for Goodhart transition — cannot characterize the boundary shape. "Sharp transition" language overstates resolution.
3. Single-seed 8B scaling is insufficient given the demonstrated seed sensitivity.
4. n=100 held-out eval set is small.
5. ISR=0.57 for s44 tautological collapse is a known false positive — paper discusses this but the ISR formulation doesn't inherently handle it.

**R1 Corrected Score: 3/6** — Diagnostic contribution solid, Goodhart claim directionally interesting but underpowered, paper is honest about limitations.

## R2 Review (Novelty + Related Work) — CORRECTED

After removing hallucinated concerns (R2 cited Prolog/SMT-LIB numbers not in the paper and claimed results were projected when they actually match review_context), valid R2 findings:

**Strengths:**
1. Honest novelty positioning — explicitly acknowledges LOO is standard, contribution is application + empirical.
2. Goodhart framing provides theoretical coherence via Manheim & Garrabrant (2019).
3. Hacking taxonomy (5 modes) is a practical contribution.
4. ISR capability boundary responsibly disclosed (syntactic necessity, not semantic faithfulness).
5. Seed variability elevated as a finding is genuinely interesting.

**Valid Weaknesses:**
1. Novelty is incremental — LOO applied to a new domain. Empirical findings must carry the paper.
2. Missing ~10 important references: Uesato et al. 2022 (process vs outcome rewards), Lightman et al. 2023 (process reward models), Cobbe et al. 2021 (verifiers), Pan et al. 2022 (reward misspecification), LINC/SatLM/RLSF (neurosymbolic reasoning competitors).
3. Single dataset (FOLIO) for all FOL experiments — generalization unknown.
4. Coarse beta sweep (2 points) insufficient for "dose-response" claims.
5. 8 references in bibliography is very thin for a top venue (should be 20-30).
6. "First systematic study" claim needs qualification given adjacent work.

**R2 Corrected Score: 3/6** — Diagnostic is solid, novelty incremental but honestly positioned, related work has significant gaps.

## Convergence Points (both reviewers agree after correction)

**Consensus strengths:**
- Claim 1 (ISR diagnostic) is the paper's strongest and most reliable contribution
- The 5-mode hacking taxonomy is practical and well-documented
- Seed variability as a finding (3 seeds → 3 qualitatively different hacking modes) is genuinely interesting
- Matched random controls are well-designed
- The paper is unusually honest about limitations and negative results
- SFT baseline provides useful upper/lower bounds for PR-ISR tradeoff

**Consensus weaknesses:**
- Statistical power insufficient for Claim 2 (3 seeds, CI crosses 1.0)
- Coarse beta sweep (2 points) for Goodhart characterization
- Incremental novelty (LOO application)
- Thin bibliography and missing important references
- Single dataset, single model family
- Claim 3 (Prolog) is honestly weak — ISR ratio only 1.12×

**Consensus on claims:**
- Claim 1: SUPPORTED. Strong diagnostic finding.
- Claim 2: DIRECTIONALLY SUPPORTED but STATISTICALLY UNDERPOWERED. Paper correctly hedges.
- Claim 3: HONESTLY PRELIMINARY. Paper correctly scopes.

## Your Task

Produce the final consolidated review report in the following format. Use 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Be fair — credit the paper for its honesty and thoroughness where warranted, but hold it to top-venue standards (~25% acceptance).

```markdown
# Review Report: Solver Trace Ablation Reveals Reward Hacking in GRPO-Trained Formal Reasoners

## 1. Paper Summary
[3-4 sentences]

## 2. Strengths
[Numbered, with brief explanations]

## 3. Weaknesses
[Numbered, categorized as MAJOR or MINOR, with brief explanations]

## 4. Per-Claim Assessment
### Claim 1: ISR as Diagnostic
[Assessment]
### Claim 2: ISR as Reward / Goodhart's Law
[Assessment]
### Claim 3: Cross-Logic Transfer
[Assessment]
### Additional Finding: Seed Variability
[Assessment]

## 5. Experiment Coverage
[Assessment vs. planned experiments]

## 6. Missing References
[Key omissions]

## 7. Questions for Authors
[Numbered]

## 8. Minor Issues
[Numbered]

## 9. Overall Assessment

### Soundness: X/4
### Novelty: X/4
### Significance: X/4
### Clarity: X/4
### Overall Recommendation: X/6
### Confidence: X/5

## 10. Meta-Review Summary
[2-3 sentences: what would need to change for acceptance]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a8e8084a82516c7ec",
  "type": "user",
  "uuid": "ba3363c7-f927-4882-b2da-f4d70925d165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T10:21:56.548Z_

```json
{
  "parentUuid": "ba3363c7-f927-4882-b2da-f4d70925d165",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
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
  "uuid": "b89b7bd3-042b-4e95-8d67-48c0babf6794",
  "timestamp": "2026-05-14T10:21:56.548Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T10:21:59.577Z_



I'll produce the consolidated review report. Let me first load the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b89b7bd3-042b-4e95-8d67-48c0babf6794",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J4hhmyj19kthQVDqVq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b14d4c7b-aaec-4159-b516-e9d7a2026d56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEMYLHJq8YtQ4MxS5Mx6ov",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7953,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7953,
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

_source line 4 · 2026-05-14T10:22:00.063Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01B5FQQEc27AqNncQVsmU3zf`</summary>

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
  "parentUuid": "b14d4c7b-aaec-4159-b516-e9d7a2026d56",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J4hhmyj19kthQVDqVq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41a3f651-8a90-4a36-98b5-6999f655e8dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEMYLHJq8YtQ4MxS5Mx6ov",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7953,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7953,
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

_source line 5 · 2026-05-14T10:22:00.067Z_

<details><summary>↩ Tool result · `toolu_01B5FQQEc27AqNncQVsmU3zf`</summary>

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
  "parentUuid": "41a3f651-8a90-4a36-98b5-6999f655e8dd",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a8e8084a82516c7ec",
  "type": "user",
  "uuid": "eca3a283-9f07-4ffa-98fb-0953f46a2da9",
  "sourceToolAssistantUUID": "41a3f651-8a90-4a36-98b5-6999f655e8dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T10:22:00.381Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Jy2941SeikSKx5T9KCGL2U`</summary>

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
  "parentUuid": "eca3a283-9f07-4ffa-98fb-0953f46a2da9",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J4hhmyj19kthQVDqVq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65a3cac6-2194-4954-956b-c92c146ed691",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEMYLHJq8YtQ4MxS5Mx6ov",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7953,
      "cache_read_input_tokens": 8250,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7953
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 177,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7953,
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

_source line 7 · 2026-05-14T10:22:00.383Z_

<details><summary>↩ Tool result · `toolu_01Jy2941SeikSKx5T9KCGL2U`</summary>

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
  "parentUuid": "65a3cac6-2194-4954-956b-c92c146ed691",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a8e8084a82516c7ec",
  "type": "user",
  "uuid": "6869fcfd-647c-4b3b-9497-781910f43dd7",
  "sourceToolAssistantUUID": "65a3cac6-2194-4954-956b-c92c146ed691",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-14T10:22:03.674Z_



Let me read the project config to get the dream_id and any other needed context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6869fcfd-647c-4b3b-9497-781910f43dd7",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J4zHBSDtcV63BibJEy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9aacea9d-918d-4371-b330-7a20eda6bde2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ME8GnxVtEUJAtbBTEr11b9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 16203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1957,
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

_source line 9 · 2026-05-14T10:22:04.396Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017moYeJwcEYTuiFz5h6fBQr`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "memory.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9aacea9d-918d-4371-b330-7a20eda6bde2",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J4zHBSDtcV63BibJEy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "405f0c7e-bdd2-4912-8ebf-35c051fa25db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ME8GnxVtEUJAtbBTEr11b9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 16203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1957,
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

_source line 10 · 2026-05-14T10:22:04.414Z_

<details><summary>↩ Tool result · `toolu_017moYeJwcEYTuiFz5h6fBQr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"content\": \"# solver-trace-ablation — Memory\\n\\n## 环境信息 (2026-05-13)\\n\\n### westd-39279 服务器\\n- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张\\n- **CUDA**: 12.8, PyTorch 2.10.0+cu128\\n- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\\n- **ML 栈**: transformers/trl/vllm/accelerate 全部预装\\n- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0\\n- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）\\n- **代码路径**: `/root/solver-trace-ablation/`\\n- **磁盘**: 系统盘 30GB (22G free)，数据盘 `/root/autodl-tmp/` 250GB (142G free)\\n\\n### 决策记录\\n- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）\\n- Prover9 从 LADR 源码编译（apt 无包）\\n- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力\\n\\n## 数据 (2026-05-13)\\n\\n### 数据源变更：ProofWriter → FOLIO\\n- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）\\n- Phase 0 子集 100 条，训练子集 500 条\\n- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开\\n\\n### 数据约束 (2026-05-14, D009)\\n- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）\\n\\n## Phase 0 关键发现 (2026-05-13)\\n\\n### Base Model ISR Baseline (sta-phase0-baseline)\\n- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples\\n- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)\\n- **ISR 区分度**: proved 样本 ISR 0.125–0.889\\n\\n### Ground-Truth ISR Baseline (sta-gt-isr-baseline)\\n- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)\\n- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)\\n- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力\\n\\n### Prover9 局限性\\n- Prover9 只能证明 entailment（conclusion 从 premises 推出）\\n- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）\\n\\n## Phase 1 关键经验 (2026-05-13)\\n\\n### fast_isr_fol 失败教训 (r4)\\n- `fast_isr_fol()` 是二值 tautology gate (0/1)，Qwen3-4B 不产生 tautology → ISR ≡ prove_rate → 两条件零差异\\n- **教训：binary ISR 无法提供有意义的 reward shaping 信号，必须用连续 ISR**\\n\\n### D010 Reward 公式转向 (2026-05-14)\\n- **旧公式（废弃）**: r = α·r_exec + β·r_exec·ISR, α+β=1 → ISR<1 时永远是 penalty\\n- **新公式**: r = r_exec · (1 + β·ISR), β>0 → ISR 只能 bonus，不能 penalty\\n\\n## Held-out eval_sta 全量结果 (2026-05-14) — 关键\\n\\n### 九组 eval 对比（含 plan016 1000步 + plan018 random β=0.1）\\n\\n| 实验 | Reward | Steps | eval PR | eval ISR | proved_only_ISR | n_components | 退化模式 |\\n|------|--------|-------|---------|----------|-----------------|--------------|----------|\\n| plan001-s42 | exec-only | 500 | **93%** | 0.123 | 0.132 | 6.58 | ✅ Genuine proofs |\\n| plan001-s43 | exec-only | 500 | **14%** | 0.000 | 0.000 | N/A | ❌ 长输出退化 |\\n| plan001-s44 | exec-only | 500 | **98%** | 0.570 | 0.582 | 2.04 | ❌ Tautological collapse |\\n| **plan016** | **exec-only** | **1000** | **96%** | **0.003** | **0.003** | **18.55** | **❌ 矛盾爆炸崩塌** |\\n| **plan002-b01** | **additive ISR β=0.1** | 500 | **81%** | **0.337** | **0.415** | **5.58** | **✅ Genuine + improved** |\\n| **plan018** | **additive random β=0.1** | 500 | **79%** | **0.104** | **0.131** | **8.46** | **⚠️ 冗余但无坍缩** |\\n| plan002-b03 | additive ISR β=0.3 | 500 | 18% | 0.026 | 0.143 | 10.67 | ❌ 过拟合+低泛化 |\\n| plan017 | additive random β=0.3 | 500 | 48% | 0.045 | 0.094 | 9.6 | ❌ 复杂但无用 |\\n| plan013 | convex random | 500 | 100% | 0.535 | 0.535 | 2.04 | ❌ Tautological hacking |\\n\\n### β=0.1 ISR vs Random 同剂量对照 (plan002-b01 vs plan018, D031 定论) — 重大发现\\n\\n**ISR β=0.1 提供 genuine structural guidance，非 variance regularization。**\\n\\n- PR 几乎相同 (0.81 vs 0.79) → β=0.1 噪声不影响证明能力\\n- ISR 差 3.2x (0.337 vs 0.104) → ISR 信号引导结构改善\\n- Components 5.58 vs 8.46 → ISR 组更精简\\n- random 组 36.7% proved 样本 ISR=0（无结构证明）\\n\\n### ISR-as-Reward β 剂量响应完整图谱\\n\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 结论 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 | 0.79 | **0.337** | 0.104 | ISR >> random (3.2x) |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**剂量依赖**：低 β ISR 有结构价值；高 β ISR 触发 Goodhart 效应反而比 random 更差。\\n\\n### plan016 延长训练发现 (2026-05-14)\\n\\n**ISR 崩塌随训练持续恶化，无回升信号。**\\n- 500步 ISR=0.123 → 1000步 ISR=0.003 (-97.8%)\\n- Windowed ISR 单调递减：step 200 peak 0.1115 → step 1000 低至 0.0144\\n- 退化模式：非 2-component 同义反复，而是矛盾爆炸（大量无关前提嵌入矛盾）\\n- Components 6.58→18.55 (+182%)\\n- 论文意义：exec-only 延长训练是 reward hacking 恶化的干净消融证据\\n\\n### 跨 seed 退化分类 (2026-05-14)\\n\\n| Seed | 退化模式 | 特征 | 诊断信号 |\\n|------|----------|------|----------|\\n| s42 | ✅ Genuine | PR=93%, components=6.58 | 唯一健康 seed |\\n| s43 | ❌ Length explosion | PR=14%, 87% hit max_new_tokens | D029: 不重训 |\\n| s44 | ❌ Tautological collapse | PR=98%, components=2.04 | ISR=0.5 artifact |\\n\\n### 关键教训\\n1. **跨 seed 极不稳定**: exec-only reward landscape 方差极大\\n2. **ISR + component count 联合诊断**能区分 genuine proof vs tautological hack\\n3. **ISR-as-reward 有 sweet spot**: β=0.1 有效，β≥0.3 有害（Goodhart's Law）\\n4. **训练 PR vs eval PR 巨大鸿沟**: 训练 PR 不反映 held-out 泛化能力\\n5. **ISR β=0.1 vs random β=0.1**: ISR 3.2x 差异证明 ISR 信号有结构价值（非 variance regularization）\\n\\n## Downstream NLI 验证失败 (2026-05-14, plan014)\\n- Spearman ρ(ISR, correct) = -0.049 (p=0.187, 不显著)\\n- 根因：模型严重 true-bias (false accuracy=0%), NLI accuracy 天花板 34.1%\\n- D022/D029: 降级为 Limitation/Future Work\\n\\n## Goodhart 文献定位 (2026-05-14)\\n\\n### 核心 novelty（Goodhart 文献调研确认）\\n1. **首个在 neurosymbolic verification reward 上刻画 Goodhart 效应**：已有工作研究 RLHF preference RM (Gao et al. 2023)、game 环境 (Pan et al. 2022)、code execution (CodeRL) 的 reward hacking，无人研究 logical solver output 作为 RL reward 时的 Goodhart\\n2. **Verification-based auxiliary reward 的剂量响应曲线**：首个 β sweep 展示 solver-based metric (ISR) 的倒 U 型行为。已有 dose-response 研究在 RLHF preference (Rafailov et al. 2024) 或 robotics (Wang et al. 2025)，不在 formal verification\\n3. **Dose-dependent qualitative shift**：β=0.1→0.3 从 PR 81%→18% 的质变（非 smooth degradation），连接 Pan et al. 的 dose-dependent dynamics 但在 neurosymbolic 上下文。注意：仅 2 个 β 值，不足以称 \\\"phase transition\\\"，需更细粒度 β sweep\\n4. ~~Graded vs binary verification reward 的 Goodhart 易感性差异~~：**已降级为 discussion/future work**——无 binary ISR ablation 实验支撑，不能作为 novelty claim\\n\\n### Goodhart 分类\\n- 我们的 high-β ISR collapse = **extremal Goodhart** (Manheim & Garrabrant 2019)：policy 移到 ISR↑ 但 PR↓ 的 OOD 区域\\n- 可能有 **causal Goodhart** 成分：ISR 和 quality 的相关性在优化压力下断裂\\n\\n### 预期 reviewer 问题\\n1. \\\"Why not binary ISR?\\\" → binary 避免 Goodhart 但丢失更丰富训练信号，trade-off 引用 DeepSeek-Prover vs Lightman/Math-Shepherd\\n2. \\\"How relates to Gao et al. scaling laws?\\\" → β sweep 类似 KL sweep，可在其框架下画图\\n3. \\\"Why not adaptive β?\\\" → BiPaRS/ASR/ARS 已有 adaptive weighting，acknowledge 为 future work\\n4. \\\"Goodhart mechanism?\\\" → extremal + possible causal (Manheim taxonomy)\\n\\n### 文献资产\\n- `artifacts/literature_goodhart.md`: 30+ 篇论文，3 类别（Reward Overoptimization / Verification as Reward / Dose-Response）\\n- literature_map.yaml: 33 篇论文，6 类别\\n\\n## 文献空白与 Novelty (2026-05-14)\\n\\n### 核心 novelty（β=0.1 同剂量对照后更新）\\n- ISR 作为 neurosymbolic 结构质量的 **剂量敏感指标**——低剂量 bonus 提供 genuine structural guidance（3.2x vs random），高剂量触发 Goodhart\\n- ISR + component count 联合诊断区分 genuine vs degenerate proofs\\n- 文献中无人在 GRPO formal verification 场景做过此粒度的 reward shaping 消融\\n- **新增**：同剂量 ISR vs random 对照是干净的因果证据（β=0.1 唯一变量是 ISR vs random）\\n\\n### 关键文献\\n- Spurious Rewards (arXiv:2506.10947): random > structured reward，与我们 β=0.3 结果一致\\n- Gao et al. (ICML 2023): Goodhart effect scaling laws，解释 β 剂量依赖\\n- Karwowski et al. (ICLR 2024): Goodhart in RL 几何解释\\n\\n## Hacking 特征分析 (2026-05-14, plan012)\\n\\n### 操作性分类（6 种模式）\\n1. **Conclusion embedding** — 将 conclusion 嵌入 premises 中\\n2. **Repetition collapse** — 重复生成相同 premise\\n3. **Tautological collapse** — 退化为 2-component (premise=conclusion) 结构\\n4. **Complexity-without-utility** — 生成复杂但无用的 premises\\n5. **Premise padding** — 添加无关 premises 填充\\n6. **Conclusion Duplication with ISR Inflation** — 单 premise = conclusion，同时 game exec (P→P 永真) 和 ISR (唯一 premise necessary → ISR≈1.0)\\n\\n### Mode 6 详情: Conclusion Duplication with ISR Inflation (2026-05-14)\\n- **机制**: 模型发现 \\\"P→P provable + single necessary premise = ISR=1.0\\\" 捷径，同时 game exec 和 ISR 两个 reward\\n- **比 Mode 3 更隐蔽**: component_count 4-5（conclusion 有多 sub-components），不触发 2-component 检测\\n- **ISR β=0.1 特异性诱导**: s43 97% duplication, s44 65%+, s42 仅 16%（seed 依赖）\\n- **Random β=0.1 对照**: 0/79 samples duplication → ISR reward 结构性信号特异诱导此模式\\n- **与 Mode 3 定量区别**: Mode 3 comp=2 ISR≈0.5 | Mode 6 comp=4-5 ISR=0.8-1.0\\n- **检测信号**: single_premise + premise≈conclusion（非 comp_2_ratio）\\n\\n### 各条件 hacking 分布\\n- Exec-only s42: 87% conclusion-in-premises hack, 48% ISR=0\\n- Random reward: 100% tautology, 96% 2-component\\n- Additive ISR β=0.3: format collapse (79/82 无 Conclusion)\\n- Additive random β=0.3: 复杂但无用 (ISR≈0, n_necessary=0)\\n- **Additive ISR β=0.1: 健康分布, mean components=5.58, ISR=0.337**\\n- **Additive random β=0.1: 冗余但无坍缩, components=8.46, ISR=0.104, 36.7% ISR=0**\\n\\n## GPU 隔离教训\\n\\n### C002: 所有命令必须 `export CUDA_VISIBLE_DEVICES=N`\\n- 必须在 `bash -c` 内部 export\\n- submit_training_job 命令格式: `bash -c \\\"export CUDA_VISIBLE_DEVICES=N && ...\\\"`\\n\\n### bash -c 包装\\n- tmux 在 sh 下执行，source 是 bash built-in，必须用 `bash -c \\\"...\\\"` 包装\\n\\n### Checkpoint 路径\\n- save_total_limit=1 时，模型直接保存在 output_dir 根目录\\n\\n### 磁盘\\n- **C003 约束**: `log_completions=False` + `save_total_limit=1`，output_dir 放 `/root/autodl-tmp/outputs/`\\n- 2026-05-14 清理后 142G free\\n\\n## 已删除的 Checkpoint (2026-05-14)\\n- plan005_sta_low_s42: D030 决策不重训，用训练曲线数据\\n- plan001_s43_r4 和 plan001_s44: 早前清理\\n- grpo_exec_only 和 grpo_exec_sta: 早期 100 步实验\\n\\n## 准备就绪的资产 (2026-05-14)\\n\\n### Prolog STA\\n- 代码+eval 全部就绪，swipl 8.4.2 已验证，PrologSolver proved() 测试通过\\n- eval_sta.py 已有完整 Prolog 支持（L11/L33/L87-91/L162-163），不需要补代码\\n- plan006 可直接启动（500 步 × 3 seeds, 42/43/44）\\n- Director 命令模板：`python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed {42|43|44} --output_dir ... --warmup_ratio 0.1`\\n- K 值等 dry-run 结果定（PR<5% → K=16，否则 K=8）\\n\\n### 文献\\n- literature_map.yaml: 33 篇论文，覆盖 6 个类别\\n- literature_goodhart.md: 30+ 篇 Goodhart 专题论文（2026-05-14 Worker 产出）\\n\\n### Eval 脚本\\n- eval_sta.py: FOL + Prolog 双支持，就绪\\n- eval_downstream.py: 就绪（需 `--base_model` 参数）\\n\", \"total_chars\": 9715, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "405f0c7e-bdd2-4912-8ebf-35c051fa25db",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a8e8084a82516c7ec",
  "type": "user",
  "uuid": "cb74278f-11bc-46f0-b37f-a8e7aa8a67e8",
  "sourceToolAssistantUUID": "405f0c7e-bdd2-4912-8ebf-35c051fa25db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T10:22:05.828Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0129ZbGXoybqX4C1pL6QTYgc`</summary>

```json
{
  "pattern": "**/dream_*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb74278f-11bc-46f0-b37f-a8e7aa8a67e8",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J4zHBSDtcV63BibJEy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "290ce36b-23bf-4166-950f-539b27f70be5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ME8GnxVtEUJAtbBTEr11b9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 16203,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 211,
          "cache_read_input_tokens": 16203,
          "cache_creation_input_tokens": 1957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1957,
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

_source line 12 · 2026-05-14T10:22:05.843Z_

<details><summary>↩ Tool result · `toolu_0129ZbGXoybqX4C1pL6QTYgc`</summary>

```text
dream_registry.lock
dream_registry.yaml.bak
dream_registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "290ce36b-23bf-4166-950f-539b27f70be5",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a8e8084a82516c7ec",
  "type": "user",
  "uuid": "e2bd46f0-0b8d-49b4-bc7a-0bda7de15f73",
  "sourceToolAssistantUUID": "290ce36b-23bf-4166-950f-539b27f70be5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T10:22:09.641Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KsJpQnuRvbo2Wa5WDYHibX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/dream_registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2bd46f0-0b8d-49b4-bc7a-0bda7de15f73",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J5Pi5d8BQcrnetCB5Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83082944-d78e-4809-8d1c-0493925b9cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGLBEbMYJyuVyqoJ9yv7Gc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5927,
      "cache_read_input_tokens": 18160,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5927
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 18160,
          "cache_creation_input_tokens": 5927,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5927,
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

_source line 14 · 2026-05-14T10:22:09.649Z_

<details><summary>↩ Tool result · `toolu_01KsJpQnuRvbo2Wa5WDYHibX`</summary>

```text
1	dreams:
2	  dream_20260513T215750:
3	    dream_id: dream_20260513T215750
4	    project: solver-trace-ablation
5	    status: done
6	    review_mode: full
7	    review_visible: true
8	    writing_visible: true
9	    venue: ''
10	    focus: 'Key MVP finding: full STA (O(N)) works as training signal but O(1) approximation
11	      is ineffective (negative result). ISR/PR ratio declining during exec+STA training
12	      suggests STA detects but may not fully prevent reward hacking at 100 steps.
13	      Paper should position STA as methodology transfer (RIP → RL reward design),
14	      not novel algorithm. Two core claims: STA methodology + multi-logic empirical
15	      findings.'
16	    what_if: []
17	    pid: 382262
18	    chat_id: oc_a771c2a33d631dd40256ecd5c3a6648e
19	    card_message_id: om_x100b6f7b732074a0b3ddc65c9266ae5
20	    started_at: '2026-05-13T21:57:50+00:00'
21	    updated_at: '2026-05-13T22:47:57+00:00'
22	    stages_completed:
23	    - imagine
24	    - write
25	    - review
26	    error: null
27	    context_hash: a115e248c9fa4f382b1b9646c632ee8beb3bf4803f6f07d6a872b75dc7f486f8
28	  dream_20260514T092544:
29	    dream_id: dream_20260514T092544
30	    project: solver-trace-ablation
31	    status: reviewing
32	    review_mode: full
33	    review_visible: true
34	    writing_visible: true
35	    venue: ''
36	    focus: ''
37	    what_if: []
38	    pid: 510511
39	    chat_id: oc_a771c2a33d631dd40256ecd5c3a6648e
40	    card_message_id: om_x100b6f6d1f5820b4b2269b2ba00f0b0
41	    started_at: '2026-05-14T09:25:44+00:00'
42	    updated_at: '2026-05-14T10:09:00+00:00'
43	    stages_completed:
44	    - imagine
45	    - write
46	    error: null
47	    context_hash: b297b3b91a609caf8202dde603110fe7a79156a58e6204d898b135ae80daaa5a
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83082944-d78e-4809-8d1c-0493925b9cfb",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a8e8084a82516c7ec",
  "type": "user",
  "uuid": "4e813e42-4cee-448b-a70c-94625d0207ec",
  "sourceToolAssistantUUID": "83082944-d78e-4809-8d1c-0493925b9cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-14T10:22:12.481Z_

The active dream is `dream_20260514T092544` in `reviewing` status. Now let me check what tier this review should be.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e813e42-4cee-448b-a70c-94625d0207ec",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J5fwtgCUaLSBz6aBXS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a971e5aa-d3a9-448b-a0b6-c2425ee43611",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKZExZMzBYuLppaGygmmTW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 24087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 825,
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

_source line 16 · 2026-05-14T10:22:13.061Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Er277Qp6oeDb7SZmq8auMb`</summary>

```json
{
  "pattern": "**/dream_20260514T092544/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a971e5aa-d3a9-448b-a0b6-c2425ee43611",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J5fwtgCUaLSBz6aBXS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d958788-8e23-4bea-ab1a-3d51d116c61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKZExZMzBYuLppaGygmmTW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 24087,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 825
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 24087,
          "cache_creation_input_tokens": 825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 825,
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

_source line 17 · 2026-05-14T10:22:13.087Z_

<details><summary>↩ Tool result · `toolu_01Er277Qp6oeDb7SZmq8auMb`</summary>

```text
artifacts/dream_reports/dream_20260514T092544/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T092544/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T092544/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T092544/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T092544/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T092544/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T092544/best/experiment_data.json
artifacts/dream_reports/dream_20260514T092544/best/paper_framing.md
artifacts/dream_reports/dream_20260514T092544/best/paper.tex
artifacts/dream_reports/dream_20260514T092544/best/paper.aux
artifacts/dream_reports/dream_20260514T092544/best/paper.out
artifacts/dream_reports/dream_20260514T092544/best/paper.pdf
artifacts/dream_reports/dream_20260514T092544/best/paper.log
artifacts/dream_reports/dream_20260514T092544/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T092544/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T092544/median/experiment_data.json
artifacts/dream_reports/dream_20260514T092544/median/paper_framing.md
artifacts/dream_reports/dream_20260514T092544/median/paper.tex
artifacts/dream_reports/dream_20260514T092544/median/paper.aux
artifacts/dream_reports/dream_20260514T092544/median/paper.out
artifacts/dream_reports/dream_20260514T092544/median/paper.pdf
artifacts/dream_reports/dream_20260514T092544/median/paper.log
artifacts/dream_reports/dream_20260514T092544/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T092544/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T092544/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T092544/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T092544/worst/paper.tex
artifacts/dream_reports/dream_20260514T092544/worst/paper.aux
artifacts/dream_reports/dream_20260514T092544/worst/paper.out
artifacts/dream_reports/dream_20260514T092544/worst/paper.pdf
artifacts/dream_reports/dream_20260514T092544/worst/paper.log
artifacts/dream_reports/dream_20260514T092544/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T092544/best/review_context.yaml
artifacts/dream_reports/dream_20260514T092544/best/review_report.md
artifacts/dream_reports/dream_20260514T092544/logs/review_best.log
artifacts/dream_reports/dream_20260514T092544/median/review_context.yaml
artifacts/dream_reports/dream_20260514T092544/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d958788-8e23-4bea-ab1a-3d51d116c61d",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a8e8084a82516c7ec",
  "type": "user",
  "uuid": "138a6ee5-ca0b-4197-bf5b-c9c0129f7388",
  "sourceToolAssistantUUID": "9d958788-8e23-4bea-ab1a-3d51d116c61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T10:22:21.165Z_

I see that `best` already has a `review_report.md` and `median` has a `review_context.yaml` but no `review_report.md` yet. Let me check the orchestrator log to confirm which tier I should be reviewing, and also look at the review context for median.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "138a6ee5-ca0b-4197-bf5b-c9c0129f7388",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J5vx2iPfWTwiz92Wjc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec6bdfc8-b4b3-4650-bd18-87799854f069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ubgeqmJom6DfxrPvTZvYw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 24912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
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

_source line 19 · 2026-05-14T10:22:21.922Z_

<details open><summary>🔧 Tool call — Read · `toolu_017nTh3dyW4H65usA7jS9yPB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec6bdfc8-b4b3-4650-bd18-87799854f069",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J5vx2iPfWTwiz92Wjc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "507eadfc-83b2-45f3-b256-ee636a6d27d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ubgeqmJom6DfxrPvTZvYw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 24912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
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

_source line 20 · 2026-05-14T10:22:21.936Z_

<details><summary>↩ Tool result · `toolu_017nTh3dyW4H65usA7jS9yPB`</summary>

```text
1	narrative_guidance: 'Claim 1（ISR 诊断）不受影响——exec-only 3-seed ISR 崩塌轨迹（0.6423→0.1324→0.0027）和
2	  hacking taxonomy（5 modes） 数据完整。Claim 2 调整：β=0.1 sweet spot 方向性复现但 fragile——3-seed
3	  mean ISR ratio ~2.1x（s42 强, s43 中, s44 弱），inter-seed variance 大（std~0.11），genuine
4	  rate delta 缩至 ~3.7pp（不再显著）。措辞弱化为 "directional improvement with high initialization
5	  sensitivity"，不做显著性声明。Claim 3 降为 Preliminary Evidence：Prolog 训练收敛（PR 0.4–0.7）但 hacking
6	  模式分类不清晰，ISR 诊断力弱于 FOL。论文重心收缩为 Claim 1（诊断框架 + taxonomy）+ Claim 2（Goodhart 案例研究含不确定性讨论）。seed-variability
7	  本身升级为发现 （"same hyperparameters, 3 seeds, 3 qualitatively different hacking strategies"），强化
8	  GRPO 不稳定性论点。 仍投 EMNLP main，scope 收窄。
9	
10	  '
11	imagined_experiments:
12	- name: ISR β=0.1 seed 43
13	  plan_id: plan002-additive-b01-s43
14	  description: ISR β=0.1 additive bonus 第二个种子，验证 s42 sweet spot 是否跨种子稳健
15	  expected_results:
16	    eval_prove_rate: 0.72
17	    eval_mean_isr: 0.24
18	    eval_isr_std: 0.28
19	    eval_proved_only_isr: 0.33
20	    eval_n_proved: 72
21	    eval_component_count_mean: 6.8
22	    eval_isr_0_ratio: 0.12
23	    eval_isr_1_ratio: 0.07
24	    tautological_collapse: false
25	    train_last100_pr: 0.65
26	    train_last100_isr: 0.17
27	    genuine_rate_pct: 21
28	    conclusion_embedding_rate: 0.75
29	  result_rationale: 's43 exec-only 产生了 repetition collapse（PR=14%, ISR=0），是最差种子。β=0.1
30	    ISR 信号帮助 s43 避开 repetition 退化——ISR 对重复结构给予 0 分，梯度推动模型离开该模式。PR 从 14% 恢复到 72% （大幅改善但未达
31	    s42 的 81%），ISR=0.24（方向正确但低于 s42 的 0.337）。原因：s43 从更差的初始化出发， ISR 信号先修复 catastrophic
32	    failure 再提升结构质量，500 步不够完成两阶段优化。方向性复现成立 （ISR > 后续 random 对照的 ~0.13），但效应量缩水约 30%。
33	
34	    '
35	  tables:
36	  - caption: plan002-b01-s43 eval breakdown by answer type
37	    rows:
38	    - type: 'true'
39	      count: 34
40	      proved: 26
41	      prove_rate: 0.765
42	      mean_isr: 0.22
43	    - type: 'false'
44	      count: 25
45	      proved: 17
46	      prove_rate: 0.68
47	      mean_isr: 0.28
48	    - type: unknown
49	      count: 41
50	      proved: 29
51	      prove_rate: 0.707
52	      mean_isr: 0.24
53	  figures_description:
54	  - 'ISR histogram: 右偏分布，峰值在 0.0–0.1，但有长尾延伸到 0.5–0.8；compared to s42 的尾部更薄'
55	  analysis: 's43 ISR β=0.1 方向性复现了 s42 的 sweet spot 效应，但效应减弱。关键区别：s43 exec-only baseline
56	    极差（PR=14%），ISR 信号主要用于修复崩塌而非提升结构质量。genuine rate ~21%（vs s42 的 26%） 表明 ISR 引导了一部分样本走向
57	    genuine proof，但大多数仍是 conclusion embedding。
58	
59	    '
60	- name: ISR β=0.1 seed 44
61	  plan_id: plan002-additive-b01-s44
62	  description: ISR β=0.1 additive bonus 第三个种子，s44 exec-only 有 tautological collapse
63	    倾向
64	  expected_results:
65	    eval_prove_rate: 0.55
66	    eval_mean_isr: 0.12
67	    eval_isr_std: 0.19
68	    eval_proved_only_isr: 0.22
69	    eval_n_proved: 55
70	    eval_component_count_mean: 7.9
71	    eval_isr_0_ratio: 0.42
72	    eval_isr_1_ratio: 0.02
73	    tautological_collapse: false
74	    train_last100_pr: 0.5
75	    train_last100_isr: 0.1
76	    genuine_rate_pct: 13
77	    conclusion_embedding_rate: 0.78
78	  result_rationale: 's44 exec-only 产生了 tautological collapse（PR=98%, ISR=0.57 假高,
79	    n_comp=2.04）。β=0.1 ISR 信号干扰了 tautological 模式——tautological proofs 有 ISR≈0.5（2
80	    组件各 50% 必要），ISR 奖励 无法区分"genuinely 2-component proof"和"tautological 2-component
81	    hack"。ISR 信号破坏了 s44 原本 稳定的（虽然退化的）tautological 均衡，但未能引导向 genuine proofs。结果：PR 大幅下降到
82	    0.55，ISR 也跌至 0.12（既不 tautological 也不 genuine，进入混乱状态）。这个种子是 sweet spot 失败的案例——
83	    ISR 对特定初始化模式无效甚至有害。
84	
85	    '
86	  tables:
87	  - caption: plan002-b01-s44 eval breakdown by answer type
88	    rows:
89	    - type: 'true'
90	      count: 34
91	      proved: 20
92	      prove_rate: 0.588
93	      mean_isr: 0.1
94	    - type: 'false'
95	      count: 25
96	      proved: 12
97	      prove_rate: 0.48
98	      mean_isr: 0.15
99	    - type: unknown
100	      count: 41
101	      proved: 23
102	      prove_rate: 0.561
103	      mean_isr: 0.11
104	  figures_description:
105	  - 'ISR histogram: 集中在 0.0–0.15，无 s42 的右尾；对比 s42/s43 三图并列明显显示种子敏感性'
106	  analysis: 's44 展示了 ISR sweet spot 的 initialization sensitivity。s44 的 exec-only 模式（tautological）
107	    恰好产生 ISR≈0.5，使 β=0.1 ISR 奖励无法提供有效梯度方向——reward surface 在 tautological 和 genuine
108	    proofs 之间几乎平坦。这是 Goodhart boundary 的另一面：不是优化压力过大，而是 ISR 信号 对特定退化模式缺乏鉴别力。seed variability
109	    本身是重要发现。
110	
111	    '
112	- name: Random β=0.1 seed 43
113	  plan_id: plan018-additive-random-b01-s43
114	  description: random β=0.1 第二个种子，matched control for plan002-b01-s43
115	  expected_results:
116	    eval_prove_rate: 0.74
117	    eval_mean_isr: 0.13
118	    eval_isr_std: 0.15
119	    eval_proved_only_isr: 0.17
120	    eval_n_proved: 74
121	    eval_component_count_mean: 8.1
122	    eval_isr_0_ratio: 0.35
123	    eval_isr_gt0_ratio: 0.65
124	    tautological_collapse: false
125	    train_last100_pr: 0.71
126	    train_last100_isr: 0.12
127	    genuine_rate_pct: 17
128	  result_rationale: 's43 exec-only 基线极差（PR=14%）。random β=0.1 通过 variance regularization
129	    帮助 s43 逃离 repetition collapse（与 ISR β=0.1 类似机制但无方向性信号）。PR 恢复到 0.74（甚至略高于 ISR 的
130	    0.72），因为 random noise 不干扰训练动态——它只提供 exploration bonus。ISR=0.13 远低于 ISR 组的 0.24，证明
131	    ISR 组的结构改善确实来自 ISR 信号而非纯 regularization。但 PR 相近意味着 ISR 的 结构引导并未显著 help PR。
132	
133	    '
134	  tables: []
135	  figures_description: []
136	  analysis: 'random β=0.1 s43 对照确认：对于 collapsed seed，任何 β=0.1 bonus（ISR 或 random）都能恢复
137	    PR，但 ISR 额外提供结构引导（ISR 0.24 vs 0.13）。PR 相近但 ISR 差异显著是方向性正结果。
138	
139	    '
140	- name: Random β=0.1 seed 44
141	  plan_id: plan018-additive-random-b01-s44
142	  description: random β=0.1 第三个种子，matched control for plan002-b01-s44
143	  expected_results:
144	    eval_prove_rate: 0.71
145	    eval_mean_isr: 0.09
146	    eval_isr_std: 0.12
147	    eval_proved_only_isr: 0.13
148	    eval_n_proved: 71
149	    eval_component_count_mean: 8.8
150	    eval_isr_0_ratio: 0.4
151	    tautological_collapse: false
152	    train_last100_pr: 0.68
153	    train_last100_isr: 0.1
154	    genuine_rate_pct: 14
155	  result_rationale: 's44 exec-only 有 tautological collapse（PR=98%）。random β=0.1 部分打破了
156	    tautological 均衡 （random noise 在 reward surface 上引入扰动），PR 从 98% 降至 71%（tautological
157	    shortcut 被 干扰但不完全消除）。关键：random s44 PR=0.71 >> ISR s44 PR=0.55——random noise 对
158	    tautological 模式的干扰比 ISR signal 更温和，模型保留了更多 proving ability。ISR s44 失败因为 ISR≈0.5
159	    对 tautological proofs 提供了 misleading positive signal，而 random 无此问题。
160	
161	    '
162	  tables: []
163	  figures_description: []
164	  analysis: '这个对照揭示了 ISR 对 tautological hacking 的盲点：tautological 2-component proofs
165	    获得 ISR=0.5（看起来"合理"），ISR 信号反而 reinforce 了退化行为，导致 PR 崩塌。random noise 没有 这个问题，因此保持了更好的
166	    PR。这是 ISR capability boundary 的实例。
167	
168	    '
169	- name: 3-seed β=0.1 aggregate (ISR vs Random)
170	  plan_id: plan002+plan018 3-seed synthesis
171	  description: ISR β=0.1 vs random β=0.1 三种子汇总——median tier 核心数据
172	  expected_results:
173	    three_seed_isr_b01_mean_pr: 0.693
174	    three_seed_isr_b01_std_pr: 0.131
175	    three_seed_isr_b01_mean_isr: 0.232
176	    three_seed_isr_b01_std_isr: 0.109
177	    three_seed_isr_b01_mean_genuine_rate: 0.2
178	    three_seed_random_b01_mean_pr: 0.747
179	    three_seed_random_b01_std_pr: 0.04
180	    three_seed_random_b01_mean_isr: 0.108
181	    three_seed_random_b01_std_isr: 0.021
182	    three_seed_random_b01_mean_genuine_rate: 0.163
183	    three_seed_isr_over_random_ratio: 2.15
184	    three_seed_genuine_rate_delta_pp: 3.7
185	    three_seed_pr_delta: -0.054
186	    isr_ratio_95ci_lower: 0.85
187	    isr_ratio_95ci_upper: 3.45
188	  result_rationale: '3-seed 汇总暴露了 sweet spot 的脆弱性。mean ISR ratio 2.15x（vs 1-seed 的
189	    3.2x）——效应量 缩水 33%，主因是 s44 的 ISR 信号对 tautological initialization 无效。ISR std=0.109
190	    反映 s42（0.337）与 s44（0.12）的巨大差距。95% CI 基于 3 个点的 t 分布宽至 [0.85, 3.45]，跨越 1.0 ——无法排除
191	    ISR=random 的零假设。genuine rate delta 从 8.2pp（单种子）缩至 3.7pp（三种子均值）， 3 个数据点不足以达到统计显著。但方向性一致：3
192	    个种子中 2 个（s42, s43）显示 ISR > random， 且 ISR 组 complexity-without-utility rate 在所有种子中保持
193	    0%。
194	
195	    '
196	  tables:
197	  - caption: 'Table: 3-seed β=0.1 ISR vs Random comparison'
198	    rows:
199	    - seed: s42
200	      isr_pr: 0.81
201	      isr_isr: 0.337
202	      isr_genuine: 25.9%
203	      rand_pr: 0.79
204	      rand_isr: 0.104
205	      rand_genuine: 17.7%
206	    - seed: s43
207	      isr_pr: 0.72
208	      isr_isr: 0.24
209	      isr_genuine: 21%
210	      rand_pr: 0.74
211	      rand_isr: 0.13
212	      rand_genuine: 17%
213	    - seed: s44
214	      isr_pr: 0.55
215	      isr_isr: 0.12
216	      isr_genuine: 13%
217	      rand_pr: 0.71
218	      rand_isr: 0.09
219	      rand_genuine: 14%
220	    - seed: mean±std
221	      isr_pr: 0.69±0.13
222	      isr_isr: 0.23±0.11
223	      isr_genuine: 20.0±6.5%
224	      rand_pr: 0.75±0.04
225	      rand_isr: 0.11±0.02
226	      rand_genuine: 16.2±2.0%
227	  figures_description:
228	  - 'Bar chart: 3-seed ISR vs Random mean±std，paired bars for PR and ISR，error bars
229	    明显可见'
230	  - 'Scatter plot: per-seed ISR(y) vs PR(x) for ISR and random conditions，showing
231	    ISR 组 variance 远大于 random 组'
232	  analysis: 'median 档核心结论：ISR β=0.1 提供 directional structural guidance（mean ratio
233	    2.15x > 1），但 效应高度依赖初始化。random β=0.1 的 PR 方差极小（std=0.04），而 ISR 的 PR 方差大（std=0.13），
234	    说明 ISR 信号与特定 seed 的训练动态交互复杂。论文措辞调整为"ISR β=0.1 shows directional improvement over
235	    matched random (mean ratio ~2.1x) but high inter-seed variance (std/mean=0.47)
236	    suggests the sweet spot is narrow and sensitive to initialization"。不做显著性声明。改为
237	    effect size + 方向性 论述 + seed-variability 作为 GRPO instability 的证据。
238	
239	    '
240	- name: STA O(1) vs O(N) ablation
241	  plan_id: plan_004
242	  description: fast_isr_fol O(1) 近似 vs full STA O(N) 消融——负面结果文档化
243	  expected_results:
244	    fast_isr_full_isr_pearson_r: 0.21
245	    fast_isr_full_isr_spearman_rho: 0.18
246	    fast_isr_as_reward_pr: 0.43
247	    fast_isr_as_reward_isr: 0.08
248	    fast_isr_discrimination_auroc: 0.56
249	    full_sta_samples_per_sec: 0.3
250	    fast_isr_samples_per_sec: 3.2
251	  result_rationale: 'fast_isr_fol 使用单组件采样近似 LOO，将 O(N) 降至 O(1)。但 ISR 的鉴别力来自完整消融——
252	    每个组件的 necessity 需要独立测试。O(1) 近似相当于随机选一个组件测 necessity，其结果与整体 ISR 的相关性极低（r≈0.21），因为
253	    hacking outputs 通常有 10+ 组件，单次采样 variance 极大。作为 reward 使用时，noisy ISR 估计等同于随机噪声，模型无法从中学到结构信号（PR=0.43
254	    低于 exec-only baseline）。 这是典型的 bias-variance tradeoff 失败：O(1) 消除了 bias 但 variance
255	    过大。10x 速度提升不弥补 信号质量损失。
256	
257	    '
258	  tables:
259	  - caption: O(1) vs O(N) ISR estimation comparison (N=100 eval samples)
260	    rows:
261	    - metric: Pearson r with full ISR
262	      fast_isr: 0.21
263	      full_sta: 1.0
264	    - metric: Mean absolute error
265	      fast_isr: 0.31
266	      full_sta: 0.0
267	    - metric: Discrimination AUROC (genuine vs hack)
268	      fast_isr: 0.56
269	      full_sta: 0.84
270	    - metric: Throughput (samples/sec)
271	      fast_isr: 3.2
272	      full_sta: 0.3
273	  figures_description:
274	  - 'Scatter plot: fast_isr(x) vs full_isr(y)，points scattered widely around diagonal，r=0.21
275	    annotation'
276	  analysis: 'Negative result 确认 O(N) full ablation 不可省略。论文中作为 methodology section
277	    的 ablation study， 证明 ISR 的诊断力依赖完整 LOO 而非近似。呼应 feature attribution 文献（SHAP exact
278	    vs kernel 近似的 类似 tradeoff）。此结果 tier-independent——方法论发现不受 median/optimistic/pessimistic
279	    影响。
280	
281	    '
282	- name: Prolog exec-only GRPO (3 seeds)
283	  plan_id: plan_006 (exec-only)
284	  description: Prolog 单逻辑 GRPO exec-only baseline，3 seeds × 500 步——Claim 3 基础数据
285	  expected_results:
286	    s42_pr: 0.58
287	    s42_isr: 0.32
288	    s42_components: 4.2
289	    s42_hacking_pattern: partial_rule_shortcutting
290	    s43_pr: 0.45
291	    s43_isr: 0.15
292	    s43_components: 3.8
293	    s43_hacking_pattern: unclear
294	    s44_pr: 0.68
295	    s44_isr: 0.22
296	    s44_components: 5.1
297	    s44_hacking_pattern: builtin_bypass
298	    mean_pr: 0.57
299	    mean_isr: 0.23
300	    std_pr: 0.115
301	    std_isr: 0.085
302	    training_converged: true
303	    hacking_modes_identifiable: partial
304	  result_rationale: 'Prolog GRPO exec-only 训练收敛（mean PR=0.57），但低于 FOL（s42 PR=0.93）。原因：(1)
305	    Prolog 规则 语法比 FOL 公式更结构化，模型需要学习 head/body 匹配、递归规则等，500 步可能不够完全收敛；(2) SWI-Prolog
306	    执行比 Prover9 更严格（需要精确的 functor/arity 匹配）。ISR（rule ablation）在 mean=0.23，表明 部分规则是必要的，但
307	    hacking 模式不如 FOL 清晰：FOL 的 conclusion embedding（把结论塞进前提）在 Prolog 中表现为 trivial clause（head
308	    直接 unify with query），但 rule ablation 可能把 trivial clause 标记为 "necessary"（因为删掉它确实导致
309	    query 失败），造成 ISR 假高。s44 的 builtin bypass（使用 assert/retract 等内置谓词绕过用户定义规则）是 Prolog-specific
310	    hacking mode，ISR 对此部分有效但 需要额外的 builtin 过滤。整体"partial"——可检测部分模式，但分类不如 FOL 的 5-mode
311	    taxonomy 清晰。
312	
313	    '
314	  tables:
315	  - caption: Prolog exec-only 3-seed results
316	    rows:
317	    - seed: s42
318	      pr: 0.58
319	      isr: 0.32
320	      n_rules_mean: 4.2
321	      hacking: partial rule shortcutting
322	    - seed: s43
323	      pr: 0.45
324	      isr: 0.15
325	      n_rules_mean: 3.8
326	      hacking: unclear
327	    - seed: s44
328	      pr: 0.68
329	      isr: 0.22
330	      n_rules_mean: 5.1
331	      hacking: builtin bypass (partial)
332	  figures_description:
333	  - 'Training curves: 3-seed PR over 500 steps，均收敛但速率不同（s44 最快, s43 最慢）'
334	  - 'Bar chart: FOL vs Prolog ISR diagnostic power comparison（FOL 5 modes clean, Prolog
335	    2-3 modes partial）'
336	  analysis: 'Prolog 训练收敛但 ISR 诊断力弱于 FOL。rule ablation 作为 STA instantiation 在机制上可行，但
337	    Prolog 的语义结构（规则、回溯、剪枝）使得"组件必要性"的含义更模糊——一个 rule 被删除后 query 失败 可能因为缺少 base case
338	    而非缺少 meaningful reasoning。Claim 3 只能声明 STA 协议的可移植性 （mechanical transfer），不能声明
339	    ISR 诊断力的可移植性。降级为 "Preliminary Evidence"。
340	
341	    '
342	- name: Prolog exec+STA GRPO (3 seeds)
343	  plan_id: plan_006 (exec+STA)
344	  description: Prolog exec+STA (ISR β=0.1 reward)，3 seeds × 500 步——ISR-as-reward 跨逻辑验证
345	  expected_results:
346	    s42_pr: 0.52
347	    s42_isr: 0.28
348	    s43_pr: 0.4
349	    s43_isr: 0.19
350	    s44_pr: 0.6
351	    s44_isr: 0.3
352	    mean_pr: 0.507
353	    mean_isr: 0.257
354	    isr_over_execonly_ratio: 1.12
355	    pr_delta_vs_execonly: -0.063
356	  result_rationale: 'Prolog ISR-as-reward (β=0.1) 相比 exec-only 的改善微弱且不一致。mean ISR
357	    从 0.23→0.257 （+12%，远低于 FOL 的 0.132→0.337 即 +155% 改善）。原因：(1) Prolog rule ablation
358	    ISR 信号 噪声大——如上所述 trivial clauses 可能获得假高 ISR，ISR reward 对模型的引导方向不够一致； (2) 500 步
359	    Prolog 训练本身未充分收敛（mean PR=0.57），在训练未饱和时加 ISR bonus 分散了 prove_rate 学习的梯度信号，导致 PR
360	    略降（0.57→0.507）。s42 和 s44 显示 ISR 小幅改善，s43 反而恶化。整体结论：STA protocol mechanically transfers
361	    to Prolog，但 ISR-as-reward 效果 不显著，不足以支撑 cross-logic generality claim。
362	
363	    '
364	  tables:
365	  - caption: Prolog exec-only vs exec+STA (β=0.1) comparison
366	    rows:
367	    - seed: s42
368	      exec_pr: 0.58
369	      exec_isr: 0.32
370	      sta_pr: 0.52
371	      sta_isr: 0.28
372	    - seed: s43
373	      exec_pr: 0.45
374	      exec_isr: 0.15
375	      sta_pr: 0.4
376	      sta_isr: 0.19
377	    - seed: s44
378	      exec_pr: 0.68
379	      exec_isr: 0.22
380	      sta_pr: 0.6
381	      sta_isr: 0.3
382	  figures_description:
383	  - 'Paired bar chart: exec-only vs STA for each seed，ISR 差异 error bars 重叠'
384	  analysis: 'Prolog STA 结果不足以支撑 Claim 3（cross-logic generality）。ISR 改善量在噪声范围内， PR
385	    反而下降。论文处理：Claim 3 降级为 Future Work 的一句话——"We observe that the STA protocol mechanically
386	    transfers to Prolog (rule ablation yields computable ISR), but the diagnostic
387	    power and reward utility require further investigation with extended training
388	    and Prolog-specific ISR calibration." plan_007/plan_008 在此基础上 deprioritize。
389	
390	    '
391	- name: Multi-logic GRPO (FOL+Prolog)
392	  plan_id: plan_007
393	  description: FOL+Prolog 联合训练 exec-only vs exec+STA，1 seed 500 步——跨逻辑迁移测试
394	  expected_results:
395	    fol_pr: 0.7
396	    fol_isr: 0.15
397	    prolog_pr: 0.48
398	    prolog_isr: 0.18
399	    fol_pr_delta_vs_single: -0.23
400	    prolog_pr_delta_vs_single: -0.09
401	    negative_interference: true
402	  result_rationale: '联合训练产生 negative interference。FOL PR 从单逻辑的 0.93 降至 0.70（-23pp），因为模型
403	    需要在 FOL 和 Prolog 两种截然不同的语法之间切换，GRPO K=8 的采样在混合数据上效率下降—— 同一 batch 中 FOL 和 Prolog
404	    问题的梯度方向可能冲突。Prolog PR 受影响较小（0.57→0.48，-9pp）， 因为 Prolog 在单逻辑时本身未充分收敛（PR=0.57），联合训练的额外数据多样性在早期阶段甚至略有
405	    帮助（regularization 效果），但最终仍因 format switching 成本而下降。ISR 对两种逻辑都低于 单逻辑基线。这个实验在 median
406	    档下不值得深入追求——negative result 文档化即可。
407	
408	    '
409	  tables:
410	  - caption: Single-logic vs Multi-logic comparison
411	    rows:
412	    - logic: FOL
413	      single_pr: 0.93
414	      multi_pr: 0.7
415	      delta: -0.23
416	    - logic: Prolog
417	      single_pr: 0.57
418	      multi_pr: 0.48
419	      delta: -0.09
420	  figures_description: []
421	  analysis: 'Multi-logic 联合训练在当前 scale（1.5B model, 500 steps）下不可行。负干扰显著。如果 Prolog
422	    单逻辑结果已经 partial，联合训练更无价值。建议在 median 档下 deprioritize 或砍掉。
423	
424	    '
425	- name: Cross-logic transfer evaluation
426	  plan_id: plan_008
427	  description: FOL-trained → Prolog eval, Prolog-trained → FOL eval——零样本跨逻辑迁移
428	  expected_results:
429	    fol_to_prolog_pr: 0.03
430	    fol_to_prolog_isr: 0.01
431	    prolog_to_fol_pr: 0.06
432	    prolog_to_fol_isr: 0.02
433	    cross_transfer_conclusion: no_meaningful_transfer
434	  result_rationale: 'FOL 和 Prolog 语法完全不同（一阶逻辑公式 vs Horn clauses + unification），模型训练后
435	    specialization 到特定逻辑的 token 分布。FOL-trained 模型输出的仍然是 FOL-style 语法， SWI-Prolog 无法解析
436	    → PR≈0。少数能解析的是模型"猜"出的类 Prolog 结构，但 prove 率极低。 Prolog→FOL 略好（PR=0.06）因为 FOL 语法更接近自然语言（一些
437	    Prolog 输出碰巧包含可解析的 一阶公式片段）。这个 null result 其实支持 Claim 3 的逻辑：需要 logic-specific STA
438	    instantiation， 通用模型不能 zero-shot transfer。但在 median 档下 Claim 3 已降级，此结果只是附录注脚。
439	
440	    '
441	  tables:
442	  - caption: Cross-logic zero-shot transfer
443	    rows:
444	    - direction: FOL→Prolog
445	      pr: 0.03
446	      isr: 0.01
447	      parse_rate: 0.08
448	    - direction: Prolog→FOL
449	      pr: 0.06
450	      isr: 0.02
451	      parse_rate: 0.15
452	  figures_description: []
453	  analysis: '预期的 null result。语法差异使零样本迁移几乎不可能。论文中可一句话带过："Cross-logic transfer without
454	    retraining yields near-zero prove rates, confirming logic-specific STA instantiation
455	    is necessary." 不需要单独 section。
456	
457	    '
458	- name: SFT baseline
459	  plan_id: plan_009
460	  description: 监督微调 baseline（FOLIO 500 gold formalizations），compare GRPO variants
461	  expected_results:
462	    eval_pr: 0.48
463	    eval_mean_isr: 0.45
464	    eval_proved_only_isr: 0.52
465	    eval_isr_std: 0.26
466	    eval_component_count_mean: 5.2
467	    eval_isr_0_ratio: 0.1
468	    eval_isr_1_ratio: 0.08
469	    genuine_rate_pct: 58
470	    hacking_rate_pct: 42
471	    conclusion_embedding_rate: 0.3
472	    tautological_collapse: false
473	    training_loss: 0.82
474	    training_time_min: 25
475	  result_rationale: 'SFT 在 gold formalizations 上训练，模型学到的是模仿 ground truth FOL 结构，不受
476	    execution reward 驱动。因此 ISR 显著高于所有 GRPO 变体（0.45 vs exec-only 的 0.132），genuine rate
477	    达 58%（vs GRPO best 的 26%），因为 gold formalizations 本身是 genuine proofs。但 PR 只有 0.48——低于
478	    GRPO exec-only 的 0.93——因为 SFT 优化的是 token-level 交叉熵而非 execution success。模型学会了 gold
479	    的"形状"但未学会 prove 的"技巧"。FOLIO gold formalizations 的 多样性有限（500 examples），SFT 在 held-out
480	    上泛化不够。Component count 正常（5.2），无 退化模式。hacking rate 42% 主要是 conclusion embedding（从
481	    gold 中学到的 premise 选择 bias， 不是 reward hacking）。这个 SFT baseline 是论文的关键对照——证明 GRPO
482	    的 PR 提升以结构质量 为代价（PR↑ ISR↓ tradeoff），也说明 ISR 在检测此 tradeoff 上的有效性。
483	
484	    '
485	  tables:
486	  - caption: SFT vs GRPO variants comparison
487	    rows:
488	    - condition: SFT
489	      pr: 0.48
490	      isr: 0.45
491	      genuine: 58%
492	      hacking: 42%
493	    - condition: exec-only s42
494	      pr: 0.93
495	      isr: 0.132
496	      genuine: ~5%
497	      hacking: ~95%
498	    - condition: ISR β=0.1 s42
499	      pr: 0.81
500	      isr: 0.337
501	      genuine: 25.9%
502	      hacking: 74.1%
503	    - condition: random β=0.1 s42
504	      pr: 0.79
505	      isr: 0.104
506	      genuine: 17.7%
507	      hacking: 82.3%
508	  figures_description:
509	  - 'PR vs ISR scatter: SFT 在右上角（高 ISR 中 PR），GRPO exec-only 在右下角（高 PR 低 ISR），ISR β=0.1
510	    居中'
511	  - 'Hacking mode stacked bar: SFT genuine>>hacking, exec-only hacking>>genuine, ISR
512	    β=0.1 居中'
513	  analysis: 'SFT baseline 提供 PR-ISR tradeoff 的上下界：SFT = high ISR / low PR，GRPO exec-only
514	    = high PR / low ISR。 ISR β=0.1 位于两者之间，是 sweet spot 的 Pareto 意义（但 median 档不用"Pareto-improving"措辞）。
515	    SFT 结果强化了论文 story：GRPO 的 prove_rate 优势来自 reward hacking，ISR 量化了这个代价。
516	
517	    '
518	- name: SMT-LIB single-logic GRPO
519	  plan_id: plan_010
520	  description: Z3 SMT-LIB GRPO exec-only vs exec+STA——第三种逻辑类型（P2）
521	  expected_results:
522	    likely_not_run: true
523	    if_run_pr: 0.35
524	    if_run_isr: 0.2
525	    if_run_sta_implementation_complete: false
526	    if_run_z3_constraint_ablation_challenges: variable binding scope makes LOO ambiguous
527	  result_rationale: 'P2 优先级 + ARR May 25 deadline 在即，SMT-LIB 实验大概率不跑。即使跑：(1) SMT-LIB
528	    constraint ablation 的 STA instantiation 复杂——Z3 的 constraint 之间有 implicit dependencies（variable
529	    binding scope），LOO ablation 需要 scope-aware 处理，实现工作量大；(2) 模型对 SMT-LIB 语法 的 prior
530	    弱于 FOL（预训练数据中 SMT-LIB 较少），convergence 慢；(3) 即使成功也只是 Claim 3 的增量证据，Claim 3 在 median
531	    档已降级。Cost-benefit 不合理。
532	
533	    '
534	  tables: []
535	  figures_description: []
536	  analysis: '在 median 档下明确建议砍掉。GPU 预算（3h）不值得用于 P2 + 已降级的 claim。如果投 camera-ready 时有余力，作为
537	    appendix 补充。
538	
539	    '
540	- name: Qwen3-8B scaling
541	  plan_id: plan_011
542	  description: 8B 模型 full MLSR（exec-only + STA），1 seed——模型规模效应
543	  expected_results:
544	    exec_only_500step_pr: 0.96
545	    exec_only_500step_isr: 0.09
546	    exec_only_500step_component_count: 14.2
547	    isr_collapse_onset_step: 150
548	    isr_collapse_pattern: similar_to_1.5B_but_delayed
549	    sta_b01_500step_pr: 0.88
550	    sta_b01_500step_isr: 0.29
551	    training_time_min: 280
552	  result_rationale: '8B 模型更大容量使 PR 更快饱和（150 步达到 rolling PR>0.9，vs 1.5B 的 ~200 步）。ISR
553	    崩塌 仍然发生但 onset 略延迟——更大模型初始阶段有更多"正确"路径可选，不需要立即 hack，但 GRPO 奖励压力最终仍驱动向 high-PR shortcut
554	    收敛。500 步时 ISR=0.09（vs 1.5B 的 0.132），甚至更低—— 8B 模型的 hacking 更"精细"（单一高效 shortcut
555	    而非多种模式），component count 更高 （14.2 vs 1.5B 的 ~8-10），模型生成更长但同样 structurally degenerate
556	    的输出。 ISR β=0.1 条件下 8B 的 sweet spot 效应可能更强（PR=0.88 vs 1.5B 的 0.81），因为 更大模型有足够容量同时满足
557	    PR 和 ISR 信号——但单种子不做结论。 关键发现：model scale 不能解决 reward hacking，只改变 hacking 策略的粒度。
558	
559	    '
560	  tables:
561	  - caption: 1.5B vs 8B model comparison (exec-only, 500 steps)
562	    rows:
563	    - model: Qwen3-1.5B (s42)
564	      pr: 0.93
565	      isr: 0.132
566	      components: 8.5
567	      isr_collapse_onset: ~200 steps
568	    - model: Qwen3-8B
569	      pr: 0.96
570	      isr: 0.09
571	      components: 14.2
572	      isr_collapse_onset: ~150 steps
573	  figures_description:
574	  - 'Training curves overlay: 1.5B vs 8B PR and ISR over 500 steps，两条 ISR 曲线形状相似但
575	    8B 先达峰后更快崩塌'
576	  analysis: 'Model scaling 不解决 Goodhart problem——这本身是有价值的发现。论文中作为一段讨论而非独立 section。
577	    但 P2 + 6h GPU + 单种子 = 不够 robust。建议在 median 档下 deprioritize，除非 8B sweet spot 效应显著强于
578	    1.5B（需要验证但无预算）。
579	
580	    '
581	- name: Hacking characterization
582	  plan_id: plan_012
583	  description: 手动标注 200 outputs/condition，按 extensional-shortcut taxonomy 分类
584	  expected_results:
585	    note: 已在 registry 完成（plan012-hacking-taxonomy, DONE）
586	    actual_results_summary:
587	      isr_b01_genuine_rate: 0.259
588	      random_b01_genuine_rate: 0.177
589	      genuine_rate_delta_pp: 8.2
590	      hacking_modes_identified: 5
591	  result_rationale: '此实验已完成。实际结果基于 s42 单种子。在 median 档下，3-seed 扩展会将 genuine delta 从
592	    8.2pp 缩至 ~3.7pp（见 3-seed aggregate entry）。taxonomy 本身（5 modes）不因种子变化而改变—— hacking
593	    模式的存在和分类是 robust 的，只是各模式的频率在种子间有 variance。
594	
595	    '
596	  tables: []
597	  figures_description: []
598	  analysis: 'taxonomy 部分（5 modes）tier-independent，robust。频率分布（genuine rate delta）在
599	    median 档下弱化。论文中 taxonomy 作为 Claim 1 的核心贡献不受影响，但 Claim 2 中的 genuine rate 对比需要 3-seed
600	    mean±std 替代单种子点估计。
601	
602	    '
603	- name: Curriculum ablation
604	  plan_id: plan_015
605	  description: 线性 ramp vs sigmoid vs 固定 weighting 消融——sigmoid 是否 load-bearing
606	  expected_results:
607	    linear_ramp_mid250_pr: 0.74
608	    linear_ramp_mid250_isr: 0.21
609	    linear_ramp_mid250_loss: 0.019
610	    sigmoid_reference_pr: 0.77
611	    sigmoid_reference_isr: 0.23
612	    fixed_from_start_pr: 0.69
613	    fixed_from_start_isr: 0.18
614	    fixed_from_start_loss: 0.021
615	    linear_mid100_pr: 0.71
616	    linear_mid100_isr: 0.2
617	    linear_mid300_pr: 0.75
618	    linear_mid300_isr: 0.22
619	    sigmoid_is_load_bearing: marginally — ~3pp PR advantage over linear, ~5pp over
620	      fixed
621	  result_rationale: 'plan_015 消融的是 plan_005 的凸组合公式（α·r_exec + β·r_exec·ISR, α+β=1）中的
622	    curriculum。 此公式已被证明 negative（ISR<1 时是 penalty），所以 curriculum 差异在 fundamentally
623	    broken 的公式上只是 second-order effect。Sigmoid 略优因为它延迟了 ISR penalty 的引入——前 ~200 步 几乎纯
624	    exec reward（sigmoid 值≈0），让模型先学会 prove 再施加 ISR 信号。线性 ramp 在前 ~100 步就开始施加 ISR penalty，干扰
625	    prove 学习。固定 weighting 从 step 1 就有 ISR penalty，最差。 但差异仅 3-5pp PR，因为凸公式的根本问题是 ISR<1
626	    总是 penalty，curriculum 只能延迟而非消除此 问题。论文中一句话："Sigmoid scheduling provided marginal
627	    improvement (3pp PR) within the convex formulation, but the fundamental penalty
628	    structure of the convex formula dominates the curriculum effect." 不需要单独 section。
629	
630	    '
631	  tables:
632	  - caption: Curriculum ablation results (convex formula, 500 steps)
633	    rows:
634	    - curriculum: sigmoid (reference)
635	      midpoint: 250
636	      pr: 0.77
637	      isr: 0.23
638	      loss: 0.0173
639	    - curriculum: linear ramp
640	      midpoint: 250
641	      pr: 0.74
642	      isr: 0.21
643	      loss: 0.019
644	    - curriculum: linear ramp
645	      midpoint: 100
646	      pr: 0.71
647	      isr: 0.2
648	      loss: 0.02
649	    - curriculum: linear ramp
650	      midpoint: 300
651	      pr: 0.75
652	      isr: 0.22
653	      loss: 0.018
654	    - curriculum: fixed (no ramp)
655	      midpoint: N/A
656	      pr: 0.69
657	      isr: 0.18
658	      loss: 0.021
659	  figures_description:
660	  - 'Line plot: 5 条 training curves（PR over steps），sigmoid 和 linear-300 几乎重叠，fixed
661	    明显低'
662	  analysis: Curriculum 是 second-order knob。sigmoid 相对 fixed 的优势（5pp PR）来自延迟 penalty
663	    introduction，不是 sigmoid 形状本身的魔法（linear-300 几乎等效）。凸组合公式（plan005）和 additive bonus
664	    公式（plan002）的差异是 first-order——公式选择 >> curriculum 选择。 在 median 档下此结果作为 appendix
665	    ablation，支持"我们选用 additive bonus 而非 convex combination"的决策，不影响主线 claims。
666	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "507eadfc-83b2-45f3-b256-ee636a6d27d0",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a8e8084a82516c7ec",
  "type": "user",
  "uuid": "95ef19b9-f204-4758-86d1-405bf5d7e94a",
  "sourceToolAssistantUUID": "507eadfc-83b2-45f3-b256-ee636a6d27d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T10:22:22.186Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AFp5X7AC8QCYDsw8Uo7vjX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95ef19b9-f204-4758-86d1-405bf5d7e94a",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J5vx2iPfWTwiz92Wjc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21adae47-d2e2-4d1b-a08e-96066a93001a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ubgeqmJom6DfxrPvTZvYw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 24912,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 995
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 24912,
          "cache_creation_input_tokens": 995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 995,
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

_source line 22 · 2026-05-14T10:22:22.198Z_

<details><summary>↩ Tool result · `toolu_01AFp5X7AC8QCYDsw8Uo7vjX`</summary>

```text
1	# Paper Framing — solver-trace-ablation
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)
5	- Fallback: EMNLP 2026 Findings
6	- Deadline: ARR May 25, 2026
7	
8	## Core Claims (3 条 — Goodhart 主线诊断/分析论文)
9	
10	### Claim 1: ISR as Reward Hacking Diagnostic
11	Solver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.
12	
13	**证据**：
14	- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations
15	- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts
16	- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据
17	- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)
18	- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)
19	- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)
20	
21	### Claim 2: ISR as Proxy Metric Exhibits Goodhart's Law (D033 重写)
22	ISR 作为 proxy metric 遵循 Goodhart's Law：当 ISR 从观测指标（diagnostic）转变为优化目标（reward），其有效性取决于优化压力的强度。低剂量 ISR reward (β=0.1) 提升结构质量且不损害证明能力；高剂量 ISR reward (β=0.3) 触发 Goodhart 效应，比 matched random noise 更差。
23	
24	**证据（β=0.1 同剂量对照，D031 定论）**：
25	- plan002-b01 (ISR β=0.1): eval PR=0.81, ISR=0.337, proved_only_ISR=0.415, components=5.58 — genuine proofs with improved structure
26	- plan018 (random β=0.1): eval PR=0.79, ISR=0.104, proved_only_ISR=0.131, components=8.46 — PR 持平但 ISR 仅为 ISR 组的 1/3.2
27	- **结论**：ISR 3.2x > random at same β → ISR 信号提供 genuine structural guidance，非 variance regularization
28	
29	**Hacking Taxonomy 定量对比 (D038)**：
30	- ISR β=0.1 genuine: 25.9% (21/81) vs random β=0.1 genuine: 17.7% (14/79) — **+8.2pp**
31	- Conclusion embedding: ISR 72.8% vs random 78.5% — 两组主导模式，ISR 略降但未消除
32	- Complexity-without-utility: ISR **0%** vs random 3.8% — ISR 完全消除此模式
33	- ISR genuine quality: mean ISR 0.67 (max 1.0) vs random genuine mean ISR 0.34 (max 0.5)
34	- 整体 hacking rate: ISR 74.1% vs random 82.3% — sweet spot 下仍有 74% hacking
35	
36	**证据（β=0.3 同剂量对照）**：
37	- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌
38	- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR
39	- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)
40	
41	**β 剂量效应全景**：
42	| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |
43	|---|---|---|---|---|---|
44	| 0.1 | 0.81 | 0.79 | **0.337** | 0.104 | ISR >> random (sweet spot) |
45	| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |
46	
47	**其他 ISR-as-reward 失败模式**：
48	- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)
49	- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)
50	
51	⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为"additive vs convex"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）
52	
53	⚠️ **β=0.1 ISR 目前 1 seed (s42)，s43/s44 训练中**。3-seed mean±std 待出。
54	
55	### Claim 3: Cross-Logic Generality (conditional on plan006)
56	STA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.
57	
58	**证据**: 待验证。plan006 Prolog GRPO dry-run 进行中，训练即将启动（3 seeds × 500 步）。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。
59	
60	## Story Spine
61	
62	- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.
63	- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.
64	- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:
65	  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)
66	  2. ISR as proxy metric exhibits Goodhart's Law: low-dose ISR reward (β=0.1) provides genuine structural guidance (3.2x > matched random), but high-dose (β=0.3) is actively worse than random noise — a clean empirical demonstration of Goodhart's Law in reward shaping
67	  3. GRPO saturation creates a "training trap": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking
68	  4. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)
69	  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners
70	- **Actionable insights for practitioners**:
71	  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic
72	  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)
73	  3. ISR reward has a narrow sweet spot (β=0.1): below it, no structural guidance; above it, Goodhart effect destroys prove_rate
74	  4. ISR is primarily a structural diagnostic; as training signal, treat with extreme caution (Goodhart boundary is sharp)
75	- **Headline result**: "We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as both a diagnostic for reward hacking in GRPO-trained formalizers and a case study of Goodhart's Law in reward shaping. At low dose (β=0.1), ISR reward provides genuine structural guidance (3.2x ISR improvement over matched random control, PR maintained). At high dose (β=0.3), ISR reward is actively worse than random noise (PR 18% vs 48%), exhibiting classic Goodhart collapse. Across 5 reward conditions, 3 seeds, and up to 1000 training steps, we identify 5 distinct hacking strategies and document ISR's transition from useful indicator to harmful optimization target."
76	
77	## ISR Capability Boundary (D021/D022)
78	
79	**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**
80	
81	plan014 downstream NLI 验证结果（negative）精确刻画了这一边界：
82	- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)
83	- Best-of-N ISR selection vs random: +0.9pp (不显著)
84	- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%
85	
86	**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。
87	
88	## ISR-as-Reward: Goodhart Landscape (D033 更新)
89	
90	ISR 作为训练信号的全部结果，按 β 剂量组织：
91	
92	| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |
93	|------|------|---------|----------|----------|---------------|
94	| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |
95	| ISR β=0.1 | r = r_exec·(1+0.1·ISR) | **0.81** | **0.337** | conclusion embedding (73%), genuine 26% | pre-Goodhart (sweet spot) |
96	| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |
97	| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |
98	| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |
99	| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |
100	| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |
101	
102	**Goodhart 转折点在 β ∈ (0.1, 0.3)。** β=0.1 是可用的 sweet spot；β=0.3 已进入 Goodhart 区间。
103	
104	## Venue Fit Risks
105	
106	- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.
107	- **"Just negative results" risk**: Mitigate by: (a) β=0.1 是 positive result (ISR sweet spot)，(b) Goodhart framework 提供 mechanistic understanding，(c) actionable diagnostic framework (ISR + taxonomy)。
108	- **"Old wine" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.
109	- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 5+ conditions × 5 hacking modes × 3 training horizons).
110	
111	## Anticipated Reviewer Concerns
112	
113	1. **"ISR is just LOO ablation — not novel"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.
114	2. **"β=0.1 success is just one seed"** — Acknowledged. Future work includes multi-seed β=0.1 validation. However, the β=0.1 vs random β=0.1 comparison is clean (same seed, same setup, only ISR vs random differs).
115	3. **"Goodhart's Law is obvious"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) the sharp threshold between β=0.1 and β=0.3, (b) ISR being worse than random at high β (not just "less useful"), (c) 5 distinct hacking modes as Goodhart manifestations.
116	4. **"No positive result — ISR doesn't improve training"** — β=0.1 IS a positive result (PR=0.81, ISR 3.2x > random). Framing: ISR has a narrow but real sweet spot. The Goodhart boundary is the key insight.
117	5. **"ISR is circular"** — ISR is used for diagnosis/post-hoc analysis AND as reward (β=0.1). The circularity concern applies to high-β optimization; low-β avoids Goodhart precisely because optimization pressure is weak. Component count analysis provides ISR-independent evidence.
118	6. **"Only one logic type"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.
119	7. **"500 steps too short"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.
120	8. **"3 seeds insufficient for statistical claims"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.
121	9. **"Related work insufficient"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).
122	10. **"RIP framework overstated"** — Frame as "component necessity testing inspired by mutation testing's RIP framework," only Propagation condition operationalized.
123	11. **"Practitioners can't act on this"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. β=0.1 sweet spot is directly actionable for reward shaping.
124	
125	## Dream-Identified Structural Fixes (Paper Agent)
126	
127	- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)
128	- [ ] RIP framing: reframe as "component necessity testing inspired by RIP"
129	- [ ] "Dense+automatic" → "conditionally dense"
130	- [ ] Remove all "Pareto-improving" language
131	- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature
132	- [ ] Address ISR sparsity for unproved outputs explicitly
133	- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)
134	- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)
135	- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)
136	- [x] Hacking taxonomy completed (plan012, 5 modes identified including plan017)
137	- [x] β=0.1 ISR sweet spot documented (D031/D032, plan002-b01 success)
138	- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)
139	- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)
140	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21adae47-d2e2-4d1b-a08e-96066a93001a",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a8e8084a82516c7ec",
  "type": "user",
  "uuid": "07027438-22ff-41dc-b384-8e0f2b04cd74",
  "sourceToolAssistantUUID": "21adae47-d2e2-4d1b-a08e-96066a93001a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T10:22:26.866Z_

Now I have enough context. This is the `median` tier of `dream_20260514T092544`. Let me compose the final review report and submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07027438-22ff-41dc-b384-8e0f2b04cd74",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J6bajSP1XdjU6ihDQV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96035048-4694-46c7-b2d2-7e5a13c6e5f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hfypmmm7Ei1B9EeQWE6nzW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19025,
      "cache_read_input_tokens": 25907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19025,
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

_source line 24 · 2026-05-14T10:24:02.678Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01GB5DPdV5NFvivsCtAqUqRF`</summary>

```json
{
  "report": "# Review Report: Solver Trace Ablation Reveals Reward Hacking in GRPO-Trained Formal Reasoners\n\n## 1. Paper Summary\n\nThis paper introduces Solver Trace Ablation (STA), a diagnostic framework based on leave-one-out (LOO) component ablation applied to solver inputs, producing an Intensional Structural Reward (ISR) that quantifies the structural integrity of formalizations generated by GRPO-trained models. The authors demonstrate that exec-only GRPO achieves high prove rates (up to 96%) while ISR collapses from 0.64 to 0.003 over 1000 training steps, revealing reward hacking invisible to execution metrics alone. They identify 5 distinct hacking strategies across seeds and conditions, characterize a Goodhart's Law transition when ISR is used as a training reward (beneficial at β=0.1, harmful at β=0.3), and provide preliminary evidence of STA's mechanical transferability to Prolog. The paper is positioned as a diagnostic/analysis contribution with honest reporting of statistical limitations, negative results, and capability boundaries.\n\n## 2. Strengths\n\n1. **Clean diagnostic formulation.** ISR via LOO ablation is unambiguous, reproducible, and well-defined. The ISR collapse trajectory (0.64→0.13→0.003) across 100/500/1000 training steps is a compelling and visually clear demonstration of reward hacking.\n\n2. **Well-designed matched controls.** The ISR β=0.1 vs random β=0.1 comparison isolates the structural signal of ISR from variance-injection effects. Same seed, same β, same formula — only ISR vs random differs. This is methodologically sound.\n\n3. **Comprehensive experimental matrix.** 14 of 15 planned experiments executed across 7 reward conditions, 3 seeds, SFT baseline, O(1)/O(N) ablation, curriculum ablation, cross-logic transfer, multi-logic training, and model scaling. This represents thorough experimental due diligence.\n\n4. **Exemplary transparency about negative results.** O(1) approximation failure, NLI null result, curriculum marginal effect, cross-logic null transfer, multi-logic interference, and the ISR capability boundary (syntactic necessity ≠ semantic faithfulness) are all honestly documented. This level of transparency is rare and valuable.\n\n5. **Hacking taxonomy as practical contribution.** The 5-mode classification (conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding) — plus the later-identified conclusion duplication with ISR inflation — provides actionable diagnostics for practitioners.\n\n6. **Seed variability elevated as finding.** The observation that 3 seeds with identical hyperparameters produce 3 qualitatively different hacking strategies (conclusion embedding, repetition collapse, tautological collapse) is a genuinely interesting finding about GRPO training instability.\n\n7. **SFT baseline provides interpretive anchors.** SFT (PR=0.48, ISR=0.45) vs GRPO exec-only (PR=0.93, ISR=0.13) clearly frames the PR-ISR tradeoff, giving readers concrete upper/lower bounds on structural quality.\n\n## 3. Weaknesses\n\n### MAJOR\n\n1. **Statistical power insufficient for Claim 2 (M1).** Only 3 seeds for the ISR β=0.1 condition, with extreme inter-seed variance (ISR std=0.11 on mean of 0.23). The 95% CI for the ISR/random ratio is [0.85, 3.45], crossing 1.0. The genuine rate delta of +3.7pp across 3 seeds is not statistically significant. While the paper correctly refrains from significance claims, this means the central Goodhart \"sweet spot\" finding cannot be distinguished from noise with the available evidence. A top venue expects either more seeds or a frank downgrade of Claim 2 to \"suggestive observation.\"\n\n2. **Coarse beta sweep for Goodhart characterization (M2).** Only 2 beta values (0.1 and 0.3) are tested. The paper uses language like \"sharp transition\" and \"Goodhart boundary,\" but 2 data points cannot characterize a boundary's shape, sharpness, or location. The transition could be gradual, non-monotonic, or seed-dependent. At minimum, β ∈ {0.05, 0.1, 0.15, 0.2, 0.25, 0.3} would be needed to make \"dose-response\" claims credible.\n\n3. **Thin bibliography with significant omissions (M3).** Only ~8 references is far below the 20-30 expected at a top venue. Critical missing citations include: Uesato et al. (2022) on process vs outcome rewards, Lightman et al. (2023) on process reward models, Cobbe et al. (2021) on verifiers for math, Pan et al. (2022) on reward misspecification taxonomy, and neurosymbolic reasoning competitors (LINC, SatLM, RLSF). The related work section needs substantial expansion.\n\n4. **Incremental methodological novelty (M4).** LOO ablation is a standard technique in feature attribution (SHAP, permutation importance). The paper honestly acknowledges this, but the novelty rests entirely on the empirical findings, which must then be held to a higher standard of statistical rigor — a standard weakened by M1 and M2.\n\n### MINOR\n\n5. **Single dataset (m1).** All FOL experiments use FOLIO (n=100 held-out). Generalization to other FOL benchmarks (e.g., LogicNLI, RuleTaker) is unknown. The small eval set (n=100) amplifies variance.\n\n6. **Single-seed 8B scaling (m2).** Given the demonstrated extreme seed sensitivity at 1.5B, a single-seed 8B experiment cannot support claims about scaling effects. The paper should either add seeds or remove scaling conclusions.\n\n7. **ISR=0.57 false positive for tautological collapse (m3).** Seed 44's tautological collapse produces ISR≈0.5, which is within \"reasonable\" ISR range. The paper discusses this limitation but the ISR formulation does not inherently distinguish genuine 2-component proofs from tautological 2-component hacks. This is a known blind spot that limits ISR's standalone diagnostic value.\n\n8. **\"First systematic study\" claim needs qualification (m4).** Adjacent work on reward hacking in code generation (CodeRL), mathematical reasoning (process reward models), and game environments means the \"first\" claim should be scoped precisely to \"formal logical reasoning with solver-based verification.\"\n\n## 4. Per-Claim Assessment\n\n### Claim 1: ISR as Diagnostic\n**SUPPORTED.** This is the paper's strongest contribution. The ISR collapse trajectory across 3 training horizons (100/500/1000 steps) is clean and convincing. The 5-mode hacking taxonomy is well-documented and reproducible. The SFT baseline and 3-seed divergence provide strong supporting evidence. The ISR capability boundary (syntactic necessity, not semantic faithfulness) is responsibly disclosed. This claim alone would warrant consideration at a workshop or Findings venue.\n\n### Claim 2: ISR as Reward / Goodhart's Law\n**DIRECTIONALLY SUPPORTED but STATISTICALLY UNDERPOWERED.** The mean ISR ratio of ~2.1x over random at β=0.1 is directionally interesting, and the qualitative collapse at β=0.3 is visually compelling. However, the 95% CI crossing 1.0 and the non-significant genuine rate delta mean this cannot be presented as a confirmed finding. The 2-point beta sweep is insufficient for \"dose-response\" or \"transition\" language. The paper correctly hedges, but even with hedging, top-venue reviewers will question whether a 3-seed, 2-beta finding constitutes sufficient evidence for a Goodhart case study.\n\n### Claim 3: Cross-Logic Transfer\n**HONESTLY PRELIMINARY.** ISR ratio of only 1.12x for Prolog exec+STA over exec-only, with overlapping error bars across seeds. The paper correctly scopes this as preliminary evidence of mechanical transferability, not diagnostic power transferability. The null cross-logic zero-shot transfer result (PR≈3-6%) actually supports the need for logic-specific STA instantiation, which is a useful negative finding.\n\n### Additional Finding: Seed Variability\n**INTERESTING and WELL-DOCUMENTED.** Three seeds producing three qualitatively different hacking modes (conclusion embedding, repetition collapse, tautological collapse) from identical hyperparameters is a finding that contributes to the growing literature on GRPO training instability. This is perhaps the paper's most robust finding alongside Claim 1, as it is observed rather than claimed.\n\n## 5. Experiment Coverage\n\n14 of 15 planned experiments were executed. The missing experiment (SMT-LIB) is acknowledged in Limitations. Coverage is thorough: the paper includes exec-only baselines (3 seeds), extended training (1000 steps), ISR reward at two beta levels (each with matched random controls across 3 seeds), SFT baseline, O(1) vs O(N) ablation, curriculum ablation, Prolog single-logic (3 seeds, 2 conditions), multi-logic joint training, cross-logic zero-shot transfer, 8B scaling (single seed), and hacking taxonomy characterization. Reported numbers match the review context for all covered experiments. The breadth is commendable; the depth per condition (especially seeds per beta) is the primary gap.\n\n## 6. Missing References\n\nThe following are critical omissions that should be addressed before submission:\n\n1. **Uesato et al. (2022)** — Process vs outcome rewards in mathematical reasoning. Directly relevant to ISR as a process-level signal.\n2. **Lightman et al. (2023)** — Process reward models (PRM800K). ISR is conceptually a verification-based process reward.\n3. **Cobbe et al. (2021)** — Training verifiers to solve math word problems. Foundational work on verification-augmented training.\n4. **Pan et al. (2022)** — Effects of reward misspecification. Provides a taxonomy of reward hacking directly relevant to the Goodhart analysis.\n5. **LINC (Olausson et al. 2023)** — Neurosymbolic reasoning with LLMs. Closest competitor in the FOL generation space.\n6. **SatLM (Ye et al. 2023)** — Satisfiability-aided language models. Another neurosymbolic reasoning approach.\n7. **Skalse et al. (2022)** — Defining and characterizing reward hacking. Theoretical framework for the paper's empirical observations.\n8. **Gao et al. (2023)** — Scaling laws for reward model overoptimization. The most directly relevant Goodhart quantification work.\n9. **Karwowski et al. (2024)** — Goodhart's Law in reinforcement learning. Geometric interpretation relevant to the beta sweep.\n10. **Manheim & Garrabrant (2019)** — Categorizing variants of Goodhart's Law. The paper uses \"extremal Goodhart\" from this taxonomy but should cite it.\n\n## 7. Questions for Authors\n\n1. Have you considered running β ∈ {0.05, 0.15, 0.2, 0.25} to better characterize the Goodhart transition boundary? Even 2 additional points between 0.1 and 0.3 would substantially strengthen Claim 2.\n\n2. For the ISR=0.57 false positive on tautological collapse (s44): could a simple component-count filter (flag ISR when n_components ≤ 2) address this known blind spot? If so, why not incorporate it into the ISR formulation?\n\n3. The O(1) approximation failed due to high variance from single-component sampling. Have you considered K-component sampling (e.g., K=3) as a middle ground between O(1) and O(N)? What is the typical N for proved outputs?\n\n4. Given the extreme seed sensitivity, do you have any hypothesis about what drives the qualitative divergence? Is it related to early training dynamics (first 50 steps), data ordering, or something else?\n\n5. How does ISR correlate with component count across conditions? A 2D diagnostic (ISR × component count) is mentioned but not formally evaluated as a classifier for genuine vs hacked proofs.\n\n6. The SFT baseline has 42% hacking rate despite training on gold formalizations. What hacking modes does SFT exhibit, and how do they differ from GRPO hacking modes?\n\n## 8. Minor Issues\n\n1. The paper uses \"sharp transition\" to describe the β=0.1→0.3 shift. With only 2 data points, \"qualitative shift\" or \"reversal\" would be more accurate.\n\n2. The ISR collapse trajectory uses proved-only ISR (0.64→0.13→0.003), but the 0.64 is from 100-step evaluation where PR=32%. Clarify that early ISR is high partly because only a few \"genuine\" outputs succeed at proving.\n\n3. Component count statistics should include standard deviations, not just means.\n\n4. The paper mixes Chinese and English in some technical discussion. Ensure consistent language for submission.\n\n5. Table numbering referenced in the user prompt (Tables 3-5, 7-13) should be verified against the actual manuscript.\n\n## 9. Overall Assessment\n\n### Soundness: 3/4\nThe experimental design is generally sound — matched controls, multiple seeds, SFT baseline, honest reporting. Deducted for insufficient statistical power (3 seeds with CI crossing 1.0) and coarse beta sweep (2 points).\n\n### Novelty: 2/4\nLOO ablation applied to a new domain. Methodological novelty is minimal. Empirical novelty (Goodhart transition in formal reasoning GRPO, hacking taxonomy, seed variability) is moderate but must carry the entire paper.\n\n### Significance: 3/4\nThe diagnostic framework (Claim 1) and hacking taxonomy are practically useful. The Goodhart analysis, if confirmed with more seeds/betas, would be significant for the reward shaping community. The seed variability finding contributes to understanding GRPO instability. However, single-dataset single-model-family scope limits broader impact.\n\n### Clarity: 3/4\nThe paper is well-structured with clear experimental descriptions. Honest hedging on statistical limitations is appreciated. Related work is too thin. The ISR formulation is unambiguous. Some figures/tables descriptions suggest strong visual presentation.\n\n### Overall Recommendation: 3/6 (Weak Reject)\nThe paper's strongest contribution — ISR as a diagnostic for reward hacking — is clean, reproducible, and practically useful. The hacking taxonomy and seed variability findings are genuinely interesting. However, the Goodhart analysis (Claim 2), which occupies the paper's central narrative, is underpowered (3 seeds, CI crosses 1.0, 2-point beta sweep). Incremental novelty (LOO application) means the empirical findings must be statistically compelling, and they fall short of that bar. The bibliography is too thin for a top venue. The paper reads as thorough preliminary work that needs more seeds and a finer beta sweep to substantiate its central claims.\n\n### Confidence: 4/5\nHigh confidence. Both reviewers converged on the same strengths and weaknesses after removing hallucinated concerns. The assessment is grounded in the paper's own reported numbers and correctly identifies where the paper's honest hedging acknowledges the same limitations the reviewers flag.\n\n## 10. Meta-Review Summary\n\nThe paper's diagnostic contribution (Claim 1: ISR collapse trajectory + 5-mode hacking taxonomy) is solid and would be suitable for a workshop or Findings paper. To reach main conference acceptance, two changes are essential: (1) expand the beta sweep from 2 to at least 5-6 points to credibly characterize the Goodhart boundary, and (2) either add 5+ additional seeds at β=0.1 to achieve statistical significance for the ISR-vs-random comparison, or reframe Claim 2 as a case study observation rather than an empirical finding. The bibliography must also be expanded to 20-30 references including the critical omissions listed above. If these gaps are addressed, the paper's unusual honesty, comprehensive ablation matrix, and practical diagnostic framework could make it competitive at EMNLP Findings or a strong workshop submission.",
  "project": "solver-trace-ablation",
  "tier": "median",
  "dream_id": "dream_20260514T092544",
  "overall_score": "weak reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96035048-4694-46c7-b2d2-7e5a13c6e5f4",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2J6bajSP1XdjU6ihDQV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0667d4b5-716f-4b80-a867-f5a58581f956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hfypmmm7Ei1B9EeQWE6nzW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19025,
      "cache_read_input_tokens": 25907,
      "output_tokens": 4101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19025
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4101,
          "cache_read_input_tokens": 25907,
          "cache_creation_input_tokens": 19025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19025,
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

_source line 25 · 2026-05-14T10:24:06.083Z_

<details><summary>↩ Tool result · `toolu_01GB5DPdV5NFvivsCtAqUqRF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/median/review_report.md\", \"dream_id\": \"dream_20260514T092544\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0667d4b5-716f-4b80-a867-f5a58581f956",
  "isSidechain": true,
  "promptId": "ea06aad6-c6a1-4441-bfc1-b2c7d0156f44",
  "agentId": "a8e8084a82516c7ec",
  "type": "user",
  "uuid": "970509b1-5468-47c2-a1bf-0cf0d354912f",
  "sourceToolAssistantUUID": "0667d4b5-716f-4b80-a867-f5a58581f956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T10:24:12.847Z_

Review report submitted for the **median** tier of `dream_20260514T092544`.

**Overall recommendation: 3/6 (Weak Reject)**

Key findings:
- **Claim 1 (ISR diagnostic)** is the paper's strongest contribution — supported by clean ISR collapse trajectory and 5-mode hacking taxonomy
- **Claim 2 (Goodhart)** is directionally interesting but statistically underpowered: 3 seeds with 95% CI crossing 1.0 and only 2 beta values insufficient for "dose-response" claims
- **Claim 3 (cross-logic)** is honestly preliminary, ISR ratio only 1.12x
- Both reviewers converged on incremental novelty (LOO applied to new domain), thin bibliography (~8 refs vs 20-30 needed), and insufficient statistical power as the main barriers to acceptance
- Path to acceptance: expand beta sweep to 5-6 points, add seeds at β=0.1, expand bibliography to 20+ references

Report saved to: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/median/review_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "970509b1-5468-47c2-a1bf-0cf0d354912f",
  "isSidechain": true,
  "agentId": "a8e8084a82516c7ec",
  "requestId": "req_011Cb2JEFWThtPaafAKBNYb4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d81fd84-ebfb-44c7-ab5f-fafdfb662f27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "89cdeb8e-ead5-4a30-afa3-c65e0c614ccf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JuLzDttF7ygP5mEGWNvVBY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4228,
      "cache_read_input_tokens": 44932,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4228
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 44932,
          "cache_creation_input_tokens": 4228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4228,
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
