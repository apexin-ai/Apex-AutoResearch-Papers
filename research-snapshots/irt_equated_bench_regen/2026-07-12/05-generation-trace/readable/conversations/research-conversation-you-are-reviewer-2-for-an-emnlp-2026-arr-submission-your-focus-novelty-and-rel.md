# Research conversation: You are Reviewer 2 for an EMNLP 2026 ARR submission. Your focus: **Novelty and Related Work**. Evaluate originality, pos

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3c9d662c10f2e121.jsonl`
- **Structured JSON:** [`95c522660addfb26945b.json`](../../sessions/95/95c522660addfb26945b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-21T11:55:28.066Z_

You are Reviewer 2 for an EMNLP 2026 ARR submission. Your focus: **Novelty and Related Work**. Evaluate originality, positioning against prior art, significance of contributions, and writing quality.

## Venue calibration (EMNLP 2026 via ARR)
- 5 = Award (top 2.5%), 4 = Conference accept, 3 = Findings, 2 = Major revision, 1 = Do not resubmit
- Acceptance rate ~21%. Be calibrated: a score of 4 means top ~20%.
- Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5)

## Paper summary

**Title**: "Psychometric DIF Analysis Reveals Systematic Temporal Instability in LLM Benchmark Items at Scale"

**Core idea**: Apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis — a standard psychometric technique from educational testing — to LLM benchmark evaluation. The paper analyzes 5,219 models × 12,508 MMLU items from METABENCH and finds 30.8% of items show large temporal DIF (ETS Category C) between pre-2024 and 2024 model cohorts. This generalizes across 6 benchmarks.

**Four claimed contributions**:
1. **Temporal instability at scale**: 30.8% MMLU items exhibit large DIF, generalizing across 6 benchmarks (17.5–30.8%), robust to threshold choice, multiple testing, architecture composition
2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 against existing labels is expected, not failure.
3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000), portable across benchmarks
4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal but are the least disruptive non-random removal strategy. Concrete audit protocol for benchmark maintainers.

**Related Work (Section 2)** covers four areas:
- Benchmark contamination detection: Min-K% (Shi et al. 2024), ConStat (Srivastava et al. 2024), n-gram overlap (Li et al. 2024), DVD (Dong et al. 2024)
- Benchmark evolution: LiveBench (White et al. 2024), SEAL (Scale 2024), Growing Pains (Perlitz et al. 2024b)
- DIF in psychometrics: MH (Mantel & Haenszel 1959), ETS (Zieky 1993), IFT (Strobl et al. 2015), Cumulative Bayesian DIF (Sinharay et al. 2006)
- IRT for LLMs: Polo et al. 2024, Gu et al. 2024

**Key framing**: "instability ≠ invalidity" — DIF flags items whose functioning changed across model generations, a diagnostic signal, not a quality verdict. Rankings remain stable (ρ=0.994 after removing all flagged items).

**Method**: Standard MH-DIF procedure with ETS classification. Novel contribution is cross-subject matching for semi-synthetic validation. Paper is empirical + methodological (not algorithmic).

**Results highlights**:
- 30.8% MMLU C-items, permutation p<0.001, 6-benchmark generalization
- Semi-synthetic ΔTPR=0.43 at p=0.5, ΔFPR=0.000 with cross-subject matching
- Simpson's paradox: OR flip 1.48→0.76 after conditioning on CTT properties
- IFT confirms breakpoint at 2023-Q4, ρ=0.78 agreement with MH
- Graceful degradation: ρ=0.994 at 31% removal
- Bifactor IRT pilot failed (CFI=0.73), item generation insufficient (ρ=0.41)
- Ensemble fusion marginal (+0.03 AUROC) — informative negative result
- RL robustness confirmed for alignment-RL only; reasoning-RL underpowered (N=13)

**Writing**: 8 pages main text, ~24 tables across main + overflow pages. Dense experimental coverage. 18 references.

## Your review task

Write a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, specific — focus on novelty, positioning, significance)
3. **Weaknesses** (bulleted, specific, with severity: major/minor — focus on novelty gaps, missing related work, overclaiming, framing issues)
4. **Questions for authors**
5. **Soundness score** (1-5 with justification)
6. **Excitement score** (1-5 with justification)
7. **Reproducibility score** (1-5 with justification)
8. **Overall Assessment** (using the ARR 1-5 half-point scale)
9. **Confidence** (1-5)

Key questions to consider:
- Is applying MH-DIF to LLM benchmarks sufficiently novel? The method itself is standard psychometrics.
- Is the Related Work complete? Are there missing citations in contamination detection, benchmark evolution, or psychometric testing for LLMs?
- Are the four contributions well-calibrated? Which are genuinely novel vs. straightforward applications?
- Is the "instability ≠ invalidity" framing original or obvious?
- Does the paper adequately distinguish itself from Growing Pains (Perlitz et al. 2024b) which also uses anchor items for benchmark evolution?
- Is the ground truth meta-critique (Contribution 2) a real contribution or an observation?
- How does this compare to concurrent work on benchmark dynamics?

Be rigorous but fair. A paper applying standard methods to a new domain can still be valuable if the empirical findings are significant and the application is non-trivial.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "34f15789-3654-486f-8ceb-40b4464c9199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T11:55:28.069Z_

```json
{
  "parentUuid": "34f15789-3654-486f-8ceb-40b4464c9199",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
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
  "uuid": "032e6922-450e-494c-b5bd-164bc9dd5d2c",
  "timestamp": "2026-05-21T11:55:28.069Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T11:55:30.814Z_



I'll conduct a thorough review by first reading the paper and all supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "032e6922-450e-494c-b5bd-164bc9dd5d2c",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfrm7gyASGKtQwtiWMv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e67c8f3e-22eb-4abf-9dc4-ef785321cc14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019orwUA2mPUPt89pDF5T93u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7808,
      "cache_read_input_tokens": 8720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7808,
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

_source line 4 · 2026-05-21T11:55:30.985Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014yz7zSzdY6N689zXxHocKG`</summary>

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
  "parentUuid": "e67c8f3e-22eb-4abf-9dc4-ef785321cc14",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfrm7gyASGKtQwtiWMv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfc299fd-ca6d-4e82-8943-ec36b8fadfb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019orwUA2mPUPt89pDF5T93u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7808,
      "cache_read_input_tokens": 8720,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7808
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 106,
          "cache_read_input_tokens": 8720,
          "cache_creation_input_tokens": 7808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7808,
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

_source line 5 · 2026-05-21T11:55:30.990Z_

<details><summary>↩ Tool result · `toolu_014yz7zSzdY6N689zXxHocKG`</summary>

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
  "parentUuid": "bfc299fd-ca6d-4e82-8943-ec36b8fadfb0",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "eb99418b-2667-449d-ab84-341013e0357a",
  "sourceToolAssistantUUID": "bfc299fd-ca6d-4e82-8943-ec36b8fadfb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T11:55:33.345Z_



Let me read the paper and supporting materials systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb99418b-2667-449d-ab84-341013e0357a",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfryoBR7PPp25SiEqKV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd68e79b-9690-46eb-bbd1-40484817fd29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfccTiaq72TDZHzGgq4P5W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 7 · 2026-05-21T11:55:35.233Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017oxuXZAr8AG9DVWfPJRi5c`</summary>

```json
{
  "pattern": "paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd68e79b-9690-46eb-bbd1-40484817fd29",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfryoBR7PPp25SiEqKV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10ee45dd-d9d7-4d0d-99fc-11d4aa06fdbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfccTiaq72TDZHzGgq4P5W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 8 · 2026-05-21T11:55:35.251Z_

<details><summary>↩ Tool result · `toolu_017oxuXZAr8AG9DVWfPJRi5c`</summary>

```text
paper/math_commands.tex
paper/main.tex
paper/sections/method.tex
paper/sections/related_work.tex
paper/sections/experiments.tex
paper/sections/appendix.tex
paper/sections/introduction.tex
paper/sections/limitations.tex
paper/sections/discussion.tex
paper/sections/conclusion.tex
paper/sections/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10ee45dd-d9d7-4d0d-99fc-11d4aa06fdbe",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "effeaa19-089b-457e-82f0-676d83511cd0",
  "sourceToolAssistantUUID": "10ee45dd-d9d7-4d0d-99fc-11d4aa06fdbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T11:55:36.177Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DRLviPsBmpSMZUK5JiyzEm`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "effeaa19-089b-457e-82f0-676d83511cd0",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfryoBR7PPp25SiEqKV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f504f4c9-67f8-4529-a034-5d8ab254c1b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfccTiaq72TDZHzGgq4P5W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 10 · 2026-05-21T11:55:36.192Z_

<details><summary>↩ Tool result · `toolu_01DRLviPsBmpSMZUK5JiyzEm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml\", \"content\": \"categories:\\n- key: contamination_detection\\n  name: Benchmark Contamination Detection\\n  narrative: Methods for detecting training data contamination in LLM benchmarks,\\n    including RL-robust approaches\\n- key: irt_equating\\n  name: IRT Methodology & Equating\\n  narrative: Item Response Theory models, calibration, equating, and their application\\n    to LLM evaluation\\n- key: benchmark_design\\n  name: Dynamic Benchmark Design\\n  narrative: Approaches for creating contamination-resistant or self-updating benchmarks\\n- key: dif_methodology\\n  name: DIF Statistical Methods\\n  narrative: Differential Item Functioning detection methods, power analysis, and\\n    small-sample strategies\\n- key: item_generation\\n  name: Automated Item Generation\\n  narrative: LLM-based test item generation with difficulty control and psychometric\\n    validation\\n- key: llm_evaluation\\n  name: LLM Evaluation Methodology\\n  narrative: General LLM evaluation methodology, benchmark psychometric analysis,\\n    evaluation surveys, and benchmark design principles\\nmeta:\\n  last_updated: '2026-05-21T03:50:29.840Z'\\n  total_papers: 45\\npapers:\\n  balloccu2024leak:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Balloccu, S.\\n    - Schmidtova, P.\\n    - Lango, M.\\n    - Dusek, O.\\n    bibtex_key: balloccu2024leak\\n    category: contamination_detection\\n    doi: 10.18653/v1/2024.eacl-long.5\\n    relevance: Systematic survey of data leakage in closed-source LLMs covering 255\\n      papers and 263 benchmarks; establishes scope of contamination problem motivating\\n      our detection approach\\n    role: foundation\\n    semantic_scholar_id: 798feda076ad710df65d509a7884bd15937c8056\\n    title: 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in\\n      Closed-Source LLMs'\\n    url: https://arxiv.org/abs/2402.03927\\n    venue: EACL 2024\\n    verified: true\\n    year: 2024\\n  belzak2020smallsample:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Belzak, W.\\n    bibtex_key: belzak2020smallsample\\n    category: dif_methodology\\n    doi: 10.1080/00273171.2019.1671162\\n    relevance: Parsimonious logistic regression with sum scores outperforms complex\\n      IRT models for DIF detection in small samples; directly applicable to our N=50-80\\n      model cohorts\\n    role: method-component\\n    semantic_scholar_id: 8f13882b6f37be1ade68c40539156277e5723395\\n    title: Testing Differential Item Functioning in Small Samples\\n    url: https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162\\n    venue: Multivariate Behavioral Research\\n    verified: true\\n    year: 2020\\n  dekoninck2024constat:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Dekoninck, J.\\n    - Mueller, M. N.\\n    - Vechev, M.\\n    bibtex_key: dekoninck2024constat\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Performance-based contamination detection via perturbation analysis;\\n      closest methodological parallel to our DIF approach in using behavioral patterns\\n      rather than memorization signals\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'ConStat: Performance-Based Contamination Detection in Large Language Models'\\n    url: https://arxiv.org/abs/2405.16281\\n    venue: NeurIPS 2024\\n    verified: true\\n    year: 2024\\n  golchin2024timetravel:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Golchin, S.\\n    - Surdeanu, M.\\n    bibtex_key: golchin2024timetravel\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Instance-level contamination detection via guided completion prompts;\\n      baseline approach for individual-item detection that our group-level DIF method\\n      extends\\n    role: method-component\\n    semantic_scholar_id: d6d0fd994f37b630f35945736b5e1bb198148404\\n    title: 'Time Travel in LLMs: Tracing Data Contamination in Large Language Models'\\n    url: https://arxiv.org/abs/2308.08493\\n    venue: ICLR 2024\\n    verified: true\\n    year: 2024\\n  hardy2026scalability:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Hardy, M.\\n    - Gilbert, J.\\n    - Domingue, B.\\n    bibtex_key: hardy2026scalability\\n    category: irt_equating\\n    doi: 10.48550/arXiv.2603.24999\\n    relevance: Nonparametric signed isotonic R2 scalability coefficients outperform\\n      IRT item diagnostics; lightweight pre-filter for item quality before our parametric\\n      calibration\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients\\n    url: https://arxiv.org/abs/2603.24999\\n    venue: arXiv\\n    verified: true\\n    year: 2026\\n  kim2019fpc:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Kim, S.\\n    - Kolen, M.\\n    bibtex_key: kim2019fpc\\n    category: irt_equating\\n    doi: 10.1080/08957347.2019.1660344\\n    relevance: Fixed-parameter calibration requires only N>=200 vs N>=500 for full\\n      calibration; core methodology for our bifactor IRT equating with anchor items\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data\\n    url: https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344\\n    venue: Applied Measurement in Education\\n    verified: true\\n    year: 2019\\n  li2024contamination:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Li, Y.\\n    - Guo, Y.\\n    - Guerin, F.\\n    - Lin, C.\\n    bibtex_key: li2024contamination\\n    category: contamination_detection\\n    doi: 10.18653/v1/2024.findings-emnlp.30\\n    relevance: Provides web-overlap contamination labels for MMLU and other benchmarks\\n      via Common Crawl matching; primary ground-truth comparison for our DIF-based\\n      contamination detection\\n    role: foundation\\n    semantic_scholar_id: 32e11cf020021c225782a3b77b5cfed4ae8e14a0\\n    title: An Open-Source Data Contamination Report for Large Language Models\\n    url: https://aclanthology.org/2024.findings-emnlp.30/\\n    venue: Findings of EMNLP 2024\\n    verified: true\\n    year: 2024\\n  liang2026dvd:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Liang, R.\\n    bibtex_key: liang2026dvd\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Detects variant contamination via generation variance (AUC 0.73-0.74\\n      vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under\\n      RL training\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'DVD: Detection via Variance of Generation Distribution for Variant Contamination'\\n    url: https://arxiv.org/abs/2601.04895\\n    venue: arXiv\\n    verified: true\\n    year: 2026\\n  shi2024mink:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Shi, W.\\n    - Ajith, A.\\n    - Xia, M.\\n    - Huang, Y.\\n    - Liu, D.\\n    - Blevins, T.\\n    - Chen, D.\\n    - Zettlemoyer, L.\\n    bibtex_key: shi2024mink\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Introduces Min-K% Prob method and WikiMIA benchmark for pretraining\\n      data detection; key baseline whose limitations under RL training motivate our\\n      DIF-based alternative\\n    role: foundation\\n    semantic_scholar_id: 3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a\\n    title: Detecting Pretraining Data from Large Language Models\\n    url: https://arxiv.org/abs/2310.16789\\n    venue: ICLR 2024\\n    verified: true\\n    year: 2024\\n  tao2026selfcritique:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Tao, Y.\\n    bibtex_key: tao2026selfcritique\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse\\n      detection, but remains individual-model-level; our DIF is group-level and complementary\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: Detecting Data Contamination from Reinforcement Learning Post-training\\n      for Large Language Models\\n    url: https://arxiv.org/abs/2510.09259\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  wang2026fragility:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Wang, H.\\n    - Li, H.\\n    - Ko, B.\\n    - Zhang, H.\\n    bibtex_key: wang2026fragility\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Proves GRPO/PPO RL training conceals contamination signals (14-20pp\\n      AUROC degradation), motivating our DIF-based approach which operates on behavioral\\n      patterns immune to NLL smoothing\\n    role: foundation\\n    semantic_scholar_id: 9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3\\n    title: On The Fragility of Benchmark Contamination Detection in Reasoning Models\\n    url: https://arxiv.org/abs/2510.02386\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  white2025livebench:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - White, C.\\n    bibtex_key: white2025livebench\\n    category: benchmark_design\\n    doi: 10.48550/arXiv.2406.19314\\n    relevance: Monthly-updated contamination-free benchmark with objective scoring;\\n      no difficulty calibration or psychometric equivalence across updates\\n    role: direct-competitor\\n    semantic_scholar_id: 4e5d86ea8eacd341d13123852d50d1ef62738744\\n    title: 'LiveBench: A Challenging, Contamination-Free LLM Benchmark'\\n    url: https://arxiv.org/abs/2406.19314\\n    venue: ICLR 2025\\n    verified: true\\n    year: 2025\\n  zhang2024gsm1k:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Zhang, H.\\n    bibtex_key: zhang2024gsm1k\\n    category: contamination_detection\\n    doi: ''\\n    relevance: GSM1K documents 10-13% average accuracy drops from contamination; provides\\n      ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4\\n      logits) critical for our DIF power analysis\\n    role: foundation\\n    semantic_scholar_id: ef62f95c16f668f031d649799cbd79081c6d2b0f\\n    title: A Careful Examination of Large Language Model Performance on Grade School\\n      Arithmetic\\n    url: https://arxiv.org/abs/2405.00332\\n    venue: arXiv\\n    verified: true\\n    year: 2024\\n  zhang2024minkpp:\\n    abstract: ''\\n    added_at: '2026-05-21T01:40:37.987Z'\\n    added_by: literature-gap-fill\\n    authors:\\n    - Zhang, J.\\n    - Sun, J.\\n    - Yeats, E.\\n    - Ouyang, Y.\\n    - Kuo, M.\\n    - Zhang, J.\\n    - Yang, H.\\n    - Li, H.\\n    bibtex_key: zhang2024minkpp\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Improves Min-K% with vocabulary-normalized token probabilities; key\\n      baseline whose AUC degrades to 0.43-0.68 on RL-trained models, motivating our\\n      DIF-based alternative\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large\\n      Language Models'\\n    url: https://arxiv.org/abs/2404.02936\\n    venue: arXiv\\n    verified: true\\n    year: 2024\\n  lalor2019irt:\\n    title: 'Learning Latent Parameters without Human Response Patterns: Item Response\\n      Theory with Artificial Crowds'\\n    authors:\\n    - Lalor, J.\\n    - Wu, H.\\n    - Yu, H.\\n    year: 2019\\n    venue: EMNLP-IJCNLP 2019\\n    url: https://aclanthology.org/D19-1434/\\n    doi: 10.18653/v1/D19-1434\\n    bibtex_key: lalor2019irt\\n    category: irt_equating\\n    role: foundation\\n    relevance: Pioneering application of IRT to NLP evaluation using artificial crowds\\n      of DNN models; establishes that IRT parameters from machine response patterns\\n      correlate with human-calibrated parameters\\n    abstract: ''\\n    semantic_scholar_id: df6cd8a8d836e75690141deb732f6d19f0176a2e\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T02:29:19.632Z'\\n  vania2021irt:\\n    title: Comparing Test Sets with Item Response Theory\\n    authors:\\n    - Vania, C.\\n    - Htut, P.M.\\n    - Huang, W.\\n    - Mungra, D.\\n    - Pang, R.Y.\\n    - Phang, J.\\n    - Liu, H.\\n    - Cho, K.\\n    - Bowman, S.R.\\n    year: 2021\\n    venue: ACL 2021\\n    url: https://aclanthology.org/2021.acl-long.92/\\n    doi: 10.18653/v1/2021.acl-long.92\\n    bibtex_key: vania2021irt\\n    category: irt_equating\\n    role: foundation\\n    relevance: IRT-based analysis of NLU benchmark discriminability; shows which test\\n      sets remain effective at differentiating strong models and which are saturated\\n    abstract: ''\\n    semantic_scholar_id: 4ca39cf99747b8962fe37e7e025e284872df3425\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T02:29:19.632Z'\\n  li2025atlas:\\n    title: 'Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static\\n      Benchmarks'\\n    authors:\\n    - Li, P.\\n    - Tang, X.\\n    - Chen, S.\\n    - Cheng, Y.\\n    - Metoyer, R.\\n    - Hua, T.\\n    - Chawla, N.V.\\n    year: 2025\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2511.04689\\n    doi: 10.48550/arXiv.2511.04689\\n    bibtex_key: li2025atlas\\n    category: irt_equating\\n    role: method-component\\n    relevance: IRT-based adaptive testing framework (ATLAS) reduces benchmark items\\n      by 90% while preserving ability estimates; demonstrates IRT enables efficient\\n      LLM evaluation\\n    abstract: ''\\n    semantic_scholar_id: 087ce2837a0d5562bc95a40e77a327a6d033366c\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T02:29:19.632Z'\\n  chen2025irtnet:\\n    title: Learning Compact Representations of LLM Abilities via Item Response Theory\\n    authors:\\n    - Chen, J.\\n    - Wang, C.\\n    - Zhang, G.\\n    - Ye, P.\\n    - Bai, L.\\n    - Hu, W.\\n    - Qu, Y.\\n    - Hu, S.\\n    year: 2025\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2510.00844\\n    doi: 10.48550/arXiv.2510.00844\\n    bibtex_key: chen2025irtnet\\n    category: irt_equating\\n    role: method-component\\n    relevance: Multidimensional IRT with MoE network for learning LLM ability vectors\\n      and query discrimination/difficulty; demonstrates IRT-based model routing and\\n      benchmark prediction\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T02:29:19.632Z'\\n  choi2026llmjudgeirt:\\n    title: Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\\n    authors:\\n    - Choi, J.\\n    - Park, S.\\n    - Cho, C.\\n    - Park, H.\\n    - Kim, B.\\n    year: 2026\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2602.00521\\n    doi: 10.48550/arXiv.2602.00521\\n    bibtex_key: choi2026llmjudgeirt\\n    category: irt_equating\\n    role: method-component\\n    relevance: Applies IRT Graded Response Model to diagnose LLM judge reliability;\\n      extends IRT application beyond benchmark scoring to evaluation pipeline quality\\n      assessment\\n    abstract: ''\\n    semantic_scholar_id: 4fc931a456c8162716deadbc9db6fd770189e632\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T02:29:19.632Z'\\n  holland1988mh:\\n    title: Differential Item Functioning and the Mantel-Haenszel Procedure\\n    authors:\\n    - Holland, P.W.\\n    - Thayer, D.T.\\n    year: 1988\\n    venue: In H. Wainer & H.I. Braun (Eds.), Test Validity, Lawrence Erlbaum\\n    url: https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x\\n    doi: 10.1002/j.2330-8516.1986.tb00186.x\\n    bibtex_key: holland1988mh\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Seminal paper introducing the Mantel-Haenszel procedure for DIF detection;\\n      establishes the ETS classification system (A/B/C) used as standard DIF effect-size\\n      metric\\n    abstract: ''\\n    semantic_scholar_id: 5fbc064e7104036b77a2bf6f0ad509031965c275\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  shealy1993sibtest:\\n    title: A Model-Based Standardization Approach that Separates True Bias/DIF from\\n      Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF\\n    authors:\\n    - Shealy, R.\\n    - Stout, W.\\n    year: 1993\\n    venue: Psychometrika\\n    url: https://link.springer.com/article/10.1007/BF02294572\\n    doi: 10.1007/BF02294572\\n    bibtex_key: shealy1993sibtest\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Introduces SIBTEST, a nonparametric DIF detection method that separates\\n      true item bias from group ability differences; alternative to MH that handles\\n      non-uniform DIF\\n    abstract: ''\\n    semantic_scholar_id: 82f3db496626afd828fedb01a41f719a50dbfc2c\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  clauser1998dif:\\n    title: Using Statistical Procedures to Identify Differentially Functioning Test\\n      Items\\n    authors:\\n    - Clauser, B.E.\\n    - Mazor, K.M.\\n    year: 1998\\n    venue: 'Educational Measurement: Issues and Practice'\\n    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x\\n    doi: 10.1111/j.1745-3992.1998.tb00619.x\\n    bibtex_key: clauser1998dif\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Comprehensive review of DIF detection methods (MH, SIBTEST, logistic\\n      regression, IRT-based); standard reference for comparing statistical approaches\\n      to DIF\\n    abstract: ''\\n    semantic_scholar_id: c2377c505c95b924e972e61dadec81e9c87dea18\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  zumbo1999handbook:\\n    title: 'A Handbook on the Theory and Methods of Differential Item Functioning\\n      (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type\\n      (Ordinal) Item Scores'\\n    authors:\\n    - Zumbo, B.D.\\n    year: 1999\\n    venue: 'Ottawa: Directorate of Human Resources Research and Evaluation, Department\\n      of National Defense'\\n    url: https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf\\n    doi: ''\\n    bibtex_key: zumbo1999handbook\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Foundational DIF handbook presenting logistic regression as a unitary\\n      framework for DIF analysis; establishes the Zumbo-Thomas logistic regression\\n      approach widely used in applied DIF research\\n    abstract: ''\\n    semantic_scholar_id: 7f88fb0ad98645582665532600d7c46406fa2db6\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  meredith1993invariance:\\n    title: Measurement Invariance, Factor Analysis and Factorial Invariance\\n    authors:\\n    - Meredith, W.\\n    year: 1993\\n    venue: Psychometrika\\n    url: https://link.springer.com/article/10.1007/BF02294825\\n    doi: 10.1007/BF02294825\\n    bibtex_key: meredith1993invariance\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Defines the measurement invariance hierarchy (configural, metric, scalar,\\n      strict factorial invariance); theoretical foundation linking DIF to latent variable\\n      fairness\\n    abstract: ''\\n    semantic_scholar_id: 7eb541983de0a39586a699e255563b26e9291340\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  vandenberg2000invariance:\\n    title: 'A Review and Synthesis of the Measurement Invariance Literature: Suggestions,\\n      Practices, and Recommendations for Organizational Research'\\n    authors:\\n    - Vandenberg, R.J.\\n    - Lance, C.E.\\n    year: 2000\\n    venue: Organizational Research Methods\\n    url: https://journals.sagepub.com/doi/10.1177/109442810031002\\n    doi: 10.1177/109442810031002\\n    bibtex_key: vandenberg2000invariance\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Comprehensive review of measurement invariance testing practices; establishes\\n      CFA-based invariance testing as prerequisite for valid cross-group comparisons,\\n      analogous to our cross-model DIF analysis\\n    abstract: ''\\n    semantic_scholar_id: 1c9389250c1fac06eda5dcf39a8ea16cf8c92c89\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  swaminathan1990logistic:\\n    title: Detecting Differential Item Functioning Using Logistic Regression Procedures\\n    authors:\\n    - Swaminathan, H.\\n    - Rogers, H.J.\\n    year: 1990\\n    venue: Journal of Educational Measurement\\n    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x\\n    doi: 10.1111/j.1745-3984.1990.tb00754.x\\n    bibtex_key: swaminathan1990logistic\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Introduces logistic regression for DIF detection, distinguishing uniform\\n      and non-uniform DIF; more powerful than MH for non-uniform DIF and directly\\n      applicable to our contamination-as-DIF framework\\n    abstract: ''\\n    semantic_scholar_id: d14b3b6e927ff8e51406fad1010244ecabc07da0\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  teresi2007dif:\\n    title: Differential Item Functioning and Health Assessment\\n    authors:\\n    - Teresi, J.A.\\n    - Fleishman, J.A.\\n    year: 2007\\n    venue: Quality of Life Research\\n    url: https://link.springer.com/article/10.1007/s11136-007-9184-6\\n    doi: 10.1007/s11136-007-9184-6\\n    bibtex_key: teresi2007dif\\n    category: dif_methodology\\n    role: method-component\\n    relevance: Reviews DIF detection strategies including propensity score matching\\n      approaches for controlling confounders; methodological basis for our propensity-matched\\n      contamination group comparison\\n    abstract: ''\\n    semantic_scholar_id: 5ddbe080c2c0cdff671d9b9c2a795e366b6eb098\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  lord1980irt:\\n    title: Applications of Item Response Theory to Practical Testing Problems\\n    authors:\\n    - Lord, F.M.\\n    year: 1980\\n    venue: 'Hillsdale, NJ: Lawrence Erlbaum Associates'\\n    url: https://www.routledge.com/Applications-of-Item-Response-Theory-To-Practical-Testing-Problems/Lord/p/book/9780898590067\\n    doi: ''\\n    bibtex_key: lord1980irt\\n    category: dif_methodology\\n    role: foundation\\n    relevance: Introduces Lord's chi-square test for IRT-based DIF detection by comparing\\n      item parameters across groups; foundational IRT reference for our parametric\\n      DIF approach\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  raju1988area:\\n    title: The Area between Two Item Characteristic Curves\\n    authors:\\n    - Raju, N.S.\\n    year: 1988\\n    venue: Psychometrika\\n    url: https://link.springer.com/article/10.1007/BF02294403\\n    doi: 10.1007/BF02294403\\n    bibtex_key: raju1988area\\n    category: dif_methodology\\n    role: method-component\\n    relevance: Develops signed and unsigned area measures between item characteristic\\n      curves for IRT-based DIF quantification; provides effect-size metrics complementing\\n      statistical significance tests\\n    abstract: ''\\n    semantic_scholar_id: 545c20c1f2575833f81418f4757cb78446465cd7\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:21:36.315Z'\\n  muthen1985mimic:\\n    title: A Method for Studying the Homogeneity of Test Items with Respect to Other\\n      Relevant Variables\\n    authors:\\n    - Muthén, B.\\n    year: 1985\\n    venue: Journal of Educational Statistics\\n    url: ''\\n    doi: 10.2307/1164966\\n    bibtex_key: muthen1985mimic\\n    category: dif_methodology\\n    role: method-component\\n    relevance: Seminal MIMIC model for DIF with continuous covariates; future-work\\n      alternative to failed θ-conditioning (plan_012)\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:34:08.189Z'\\n  woods2009mimic:\\n    title: Empirical Selection of Anchors for Tests of Differential Item Functioning\\n    authors:\\n    - Woods, C.M.\\n    year: 2009\\n    venue: Applied Psychological Measurement\\n    url: ''\\n    doi: 10.1177/0146621609331279\\n    bibtex_key: woods2009mimic\\n    category: dif_methodology\\n    role: method-component\\n    relevance: Modern MIMIC-based DIF detection with anchor selection; addresses impact-vs-DIF\\n      confound in our future work\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:34:08.189Z'\\n  habba2026growingpains:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Habba, E.\\n    - Itzhak, I.\\n    - Yehudai, A.\\n    - Perlitz, Y.\\n    - Bandel, E.\\n    - Shmueli-Scheuer, M.\\n    - Choshen, L.\\n    - Stanovsky, G.\\n    bibtex_key: habba2026growingpains\\n    category: irt_equating\\n    doi: 10.48550/arXiv.2604.12843\\n    relevance: Uses multidimensional IRT with fixed-parameter calibration and 100\\n      anchor items for extensible evaluation (rho>=0.9); addresses score comparability\\n      but NOT contamination detection or item regeneration\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter\\n      Calibration'\\n    url: https://arxiv.org/abs/2604.12843\\n    venue: arXiv\\n    verified: true\\n    year: 2026\\n  zhou2026psnirt:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Zhou, H.\\n    - Huang, H.\\n    - Zhao, Z.\\n    - Han, L.\\n    - Wang, H.\\n    - Chen, K.\\n    - Yang, M.\\n    - Bao, W.\\n    - Dong, J.\\n    - Xu, B.\\n    - Zhu, C.\\n    - Cao, H.\\n    - Zhao, T.\\n    bibtex_key: zhou2026psnirt\\n    category: irt_equating\\n    doi: ''\\n    relevance: PSN-IRT analyzes benchmark quality via 4PL IRT; provides published\\n      IRT parameters for MMLU we can use in semi-synthetic validation\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item\\n      Response Theory\\n    url: https://arxiv.org/abs/2505.15055\\n    venue: AAAI 2026\\n    verified: true\\n    year: 2026\\n  kipnis2024metabench:\\n    title: metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language\\n      Models\\n    authors:\\n    - Kipnis, A.\\n    - Voudouris, K.\\n    - Schulze Buschoff, L.M.\\n    - Schulz, E.\\n    year: 2024\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2407.12844\\n    doi: 10.48550/arXiv.2407.12844\\n    bibtex_key: kipnis2024metabench\\n    category: benchmark_design\\n    role: foundation\\n    relevance: Primary data source providing item-level response matrix across 5000+\\n      LLMs on 6 benchmarks; IRT-based item selection methodology enables our DIF analysis\\n      on compressed benchmark items\\n    abstract: ''\\n    semantic_scholar_id: dfd5186def202285a0f23cd3f08415a5780895c1\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  hendrycks2021mmlu:\\n    title: Measuring Massive Multitask Language Understanding\\n    authors:\\n    - Hendrycks, D.\\n    - Burns, C.\\n    - Basart, S.\\n    - Zou, A.\\n    - Mazeika, M.\\n    - Song, D.\\n    - Steinhardt, J.\\n    year: 2021\\n    venue: ICLR 2021\\n    url: https://arxiv.org/abs/2009.03300\\n    doi: ''\\n    bibtex_key: hendrycks2021mmlu\\n    category: benchmark_design\\n    role: foundation\\n    relevance: Seminal 57-subject benchmark for LLM evaluation; primary benchmark\\n      in our DIF analysis due to documented contamination and available IRT parameters\\n    abstract: ''\\n    semantic_scholar_id: 814a4f680b9ba6baba23b93499f4b48af1a27678\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  liang2023helm:\\n    title: Holistic Evaluation of Language Models\\n    authors:\\n    - Liang, P.\\n    - Bommasani, R.\\n    - Lee, T.\\n    - Tsipras, D.\\n    - Soylu, D.\\n    - Yasunaga, M.\\n    - Zhang, Y.\\n    - Narayanan, D.\\n    - Wu, Y.\\n    - Kumar, A.\\n    year: 2023\\n    venue: TMLR 2023\\n    url: https://arxiv.org/abs/2211.09110\\n    doi: 10.1111/nyas.15007\\n    bibtex_key: liang2023helm\\n    category: benchmark_design\\n    role: foundation\\n    relevance: Holistic multi-metric evaluation framework covering accuracy, calibration,\\n      robustness, fairness, and bias; establishes multi-dimensional evaluation philosophy\\n      complementary to our psychometric approach\\n    abstract: ''\\n    semantic_scholar_id: ce913026f693101e54d3ab9152e107034d81fce1\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  chiang2024chatbot:\\n    title: 'Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference'\\n    authors:\\n    - Chiang, W.-L.\\n    - Zheng, L.\\n    - Sheng, Y.\\n    - Angelopoulos, A.N.\\n    - Li, T.\\n    - Li, D.\\n    - Zhang, H.\\n    - Zhu, B.\\n    - Jordan, M.I.\\n    - Gonzalez, J.E.\\n    - Stoica, I.\\n    year: 2024\\n    venue: ICML 2024\\n    url: https://arxiv.org/abs/2403.04132\\n    doi: 10.48550/arXiv.2403.04132\\n    bibtex_key: chiang2024chatbot\\n    category: benchmark_design\\n    role: method-component\\n    relevance: Crowdsourced pairwise comparison with ELO ranking as contamination-resistant\\n      alternative to static benchmarks; contrasts with our item-level psychometric\\n      approach\\n    abstract: ''\\n    semantic_scholar_id: 53f4fb0e9972989194368faf288ff8e3cba5bd60\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  mialon2023gaia:\\n    title: 'GAIA: a benchmark for General AI Assistants'\\n    authors:\\n    - Mialon, G.\\n    - Fourrier, C.\\n    - Swift, C.\\n    - Wolf, T.\\n    - LeCun, Y.\\n    - Scialom, T.\\n    year: 2023\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2311.12983\\n    doi: 10.48550/arXiv.2311.12983\\n    bibtex_key: mialon2023gaia\\n    category: benchmark_design\\n    role: method-component\\n    relevance: Benchmark with verifiable ground-truth answers designed to resist memorization;\\n      exemplifies objective-scoring benchmark design philosophy shared by our regenerated\\n      items\\n    abstract: ''\\n    semantic_scholar_id: ab8169d6e4dfabfe7c30ebec1bb871bf3e1551cd\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  li2024latesteval:\\n    title: 'LatestEval: Addressing Data Contamination in Language Model Evaluation\\n      through Dynamic and Time-Sensitive Test Construction'\\n    authors:\\n    - Li, Y.\\n    - Guerin, F.\\n    - Lin, C.\\n    year: 2024\\n    venue: AAAI 2024\\n    url: https://arxiv.org/abs/2312.12343\\n    doi: 10.48550/arXiv.2312.12343\\n    bibtex_key: li2024latesteval\\n    category: benchmark_design\\n    role: direct-competitor\\n    relevance: Automated dynamic test construction from recent texts to avoid contamination;\\n      addresses temporal contamination but lacks psychometric difficulty calibration\\n      across test versions\\n    abstract: ''\\n    semantic_scholar_id: 8106d03fb984afd8c3d066cd4f993eb2616a0da5\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  kiela2021dynabench:\\n    title: 'Dynabench: Rethinking Benchmarking in NLP'\\n    authors:\\n    - Kiela, D.\\n    - Bartolo, M.\\n    - Nie, Y.\\n    - Kaushik, D.\\n    - Geiger, A.\\n    - Wu, Z.\\n    - Vidgen, B.\\n    - Prasad, G.\\n    - Singh, A.\\n    - Ringshia, P.\\n    - Ma, Z.\\n    - Thrush, T.\\n    - Riedel, S.\\n    - Talat, Z.\\n    - Stenetorp, P.\\n    - Jia, R.\\n    year: 2021\\n    venue: NAACL 2021\\n    url: https://arxiv.org/abs/2104.14337\\n    doi: 10.18653/v1/2021.naacl-main.324\\n    bibtex_key: kiela2021dynabench\\n    category: benchmark_design\\n    role: foundation\\n    relevance: Seminal dynamic adversarial benchmarking platform with human-and-model-in-the-loop\\n      dataset creation; establishes the paradigm of continuously evolving benchmarks\\n      that our IRT-equated regeneration extends with psychometric equivalence guarantees\\n    abstract: ''\\n    semantic_scholar_id: 77a096d80eb4dd4ccd103d1660c5a5498f7d026b\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T03:43:39.896Z'\\n  burnell2023rethink:\\n    title: Rethink reporting of evaluation results in AI\\n    authors:\\n    - Burnell, R.\\n    - Schellaert, W.\\n    - Burden, J.\\n    - Ullman, T.D.\\n    - Martinez-Plumed, F.\\n    - Tenenbaum, J.B.\\n    - Rutar, D.\\n    - Cheke, L.G.\\n    - Sohl-Dickstein, J.\\n    - Mitchell, M.\\n    - Kiela, D.\\n    - Shanahan, M.\\n    - Voorhees, E.M.\\n    - Cohn, A.G.\\n    - Leibo, J.Z.\\n    - Hernandez-Orallo, J.\\n    year: 2023\\n    venue: Science\\n    url: https://www.science.org/doi/10.1126/science.adf6369\\n    doi: 10.1126/science.adf6369\\n    bibtex_key: burnell2023rethink\\n    category: llm_evaluation\\n    role: background\\n    relevance: Argues that aggregate metrics and lack of item-level transparency in\\n      AI evaluation limit understanding of model capabilities; motivates psychometric\\n      item-level analysis\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:50:29.780Z'\\n  chang2024survey:\\n    title: A Survey on Evaluation of Large Language Models\\n    authors:\\n    - Chang, Y.\\n    - Wang, X.\\n    - Wang, J.\\n    - Wu, Y.\\n    - Zhu, K.\\n    - Chen, H.\\n    - Yang, L.\\n    - Yi, X.\\n    - Wang, C.\\n    - Wang, Y.\\n    - Ye, W.\\n    - Zhang, Y.\\n    - Chang, Y.\\n    - Yu, P.S.\\n    - Yang, Q.\\n    - Xie, X.\\n    year: 2024\\n    venue: ACM Transactions on Intelligent Systems and Technology\\n    url: https://dl.acm.org/doi/full/10.1145/3641289\\n    doi: 10.1145/3641289\\n    bibtex_key: chang2024survey\\n    category: llm_evaluation\\n    role: background\\n    relevance: Comprehensive survey covering what/where/how to evaluate LLMs across\\n      tasks and societal dimensions; provides landscape context for our psychometric\\n      evaluation approach\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:50:29.780Z'\\n  maiapolo2024tinybenchmarks:\\n    title: 'tinyBenchmarks: evaluating LLMs with fewer examples'\\n    authors:\\n    - Maia Polo, F.\\n    - Weber, L.\\n    - Choshen, L.\\n    - Sun, Y.\\n    - Xu, G.\\n    - Yurochkin, M.\\n    year: 2024\\n    venue: ICML 2024\\n    url: https://proceedings.mlr.press/v235/maia-polo24a.html\\n    doi: ''\\n    bibtex_key: maiapolo2024tinybenchmarks\\n    category: llm_evaluation\\n    role: direct-competitor\\n    relevance: Uses IRT to select representative benchmark subsets for efficient LLM\\n      evaluation with 100 items approximating full MMLU; directly related to our IRT-based\\n      equating methodology\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:50:29.780Z'\\n  wang2024mmlupro:\\n    title: 'MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding\\n      Benchmark'\\n    authors:\\n    - Wang, Y.\\n    - Ma, X.\\n    - Zhang, G.\\n    - Ni, Y.\\n    - Chandra, A.\\n    - Guo, S.\\n    - Ren, W.\\n    - Arulraj, A.\\n    - He, X.\\n    - Jiang, Z.\\n    - Li, T.\\n    - Ku, M.\\n    - Wang, K.\\n    - Zhuang, A.\\n    - Fan, R.\\n    - Xue, X.\\n    - Chen, W.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2406.01574\\n    doi: ''\\n    bibtex_key: wang2024mmlupro\\n    category: llm_evaluation\\n    role: evaluation\\n    relevance: Extends MMLU with harder reasoning items and 10-option format causing\\n      16-33% accuracy drop; demonstrates benchmark evolution that motivates psychometric\\n      equating across versions\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:50:29.780Z'\\n  ott2022benchmark:\\n    title: Mapping global dynamics of benchmark creation and saturation in artificial\\n      intelligence\\n    authors:\\n    - Ott, S.\\n    - Barbosa-Silva, A.\\n    - Blagec, K.\\n    - Brauner, J.\\n    - Samwald, M.\\n    year: 2022\\n    venue: Nature Communications\\n    url: https://www.nature.com/articles/s41467-022-34591-0\\n    doi: 10.1038/s41467-022-34591-0\\n    bibtex_key: ott2022benchmark\\n    category: llm_evaluation\\n    role: background\\n    relevance: Large-scale analysis of 3765 AI benchmarks showing rapid saturation\\n      dynamics; supports our argument that static benchmarks need psychometric equating\\n      and regeneration\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper_agent\\n    added_at: '2026-05-21T03:50:29.780Z'\\n\", \"total_chars\": 36146, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f504f4c9-67f8-4529-a034-5d8ab254c1b8",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "9e87118a-824c-40c5-99b7-42281217f48d",
  "sourceToolAssistantUUID": "f504f4c9-67f8-4529-a034-5d8ab254c1b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T11:55:36.589Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NiGwh1oD4Q65kUrVGAz9RE`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e87118a-824c-40c5-99b7-42281217f48d",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfryoBR7PPp25SiEqKV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae44e30a-a234-4533-aa3e-9e8d84f23d29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfccTiaq72TDZHzGgq4P5W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16528,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1289
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 16528,
          "cache_creation_input_tokens": 1289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1289,
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

_source line 12 · 2026-05-21T11:55:36.599Z_

<details><summary>↩ Tool result · `toolu_01NiGwh1oD4Q65kUrVGAz9RE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\\n\\n## Paper Type\\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \\\"DIF reveals benchmark structural problems,\\\" not \\\"DIF detects contamination.\\\"\\n\\n## Core Claims (4 条, 可证伪)\\n\\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\\n\\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\\n- Framing: aggressive — \\\"the field's standard validation approach is fundamentally mismatched for item-level detection\\\" — now with direct empirical evidence, not just conceptual argument\\n\\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\\n\\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \\\"items that changed across generations,\\\" not \\\"good items.\\\"\\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \\\"find bad items and remove\\\" but \\\"understand what changed and why.\\\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\\n- Growing Pains互补: \\\"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\\\"\\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\\n\\n## Story Spine (v2 — no-pivot narrative)\\n\\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \\\"Model B outperforms Model A on MMLU,\\\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\\n\\n**Key narrative principle**: \\\"Instability ≠ invalidity.\\\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\\n\\n**What we find** (4 contributions, focused):\\n\\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \\\"models got better.\\\"\\n\\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\\n\\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\\n\\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\\n\\n**Headline result**: \\\"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\\\"\\n\\n## Scope Control (main body vs appendix)\\n\\n**MAIN BODY (4 claims + robustness)**:\\n- §1 Introduction (problem + \\\"instability ≠ invalidity\\\" framing upfront)\\n- §2 Related Work (45 papers, 5 clusters)\\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\\n- §5 Discussion + Limitations\\n- §6 Conclusion\\n\\n**APPENDIX (pruned from main body)**:\\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\\n- RL robustness (plan_002) — N=13, underpowered\\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\\n- Bifactor equating pilot — below target fit\\n- Item generation pilot — below benchmarks\\n- Graceful degradation — clean but supplementary\\n- Item-Focused Trees — robustness check, supplementary\\n- ConStat/DVD comparisons — complementary baselines\\n\\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\\n\\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\\n\\n## Venue Fit\\n\\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \\\"Empirical, not algorithmic\\\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\\n\\n## Novelty Articulation (三层，显式化)\\n\\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\\n\\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\\n\\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\\n\\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\\n\\n**Framing**: \\\"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\\\"\\n\\n## Anticipated Reviewer Concerns (updated for pivot)\\n\\n1. **\\\"31% could just mean models got better / ability confound inflates C%\\\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\\n\\n2. **\\\"Ground truth critique is obvious — of course web labels don't capture differential effects\\\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\\n\\n3. **\\\"Semi-synthetic injection is artificial\\\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\\n\\n4. **\\\"DIF power is only sufficient for large effects\\\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\\n\\n5. **\\\"Only validated on MMLU\\\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\\n\\n6. **\\\"Higher methods (MIMIC, propensity-score) could solve the confounding\\\"** — Acknowledged as future work. We frame our three-attempt negative results as \\\"empirical observation\\\" that motivates these directions, not as impossibility.\\n\\n7. **\\\"ETS threshold is uncalibrated for LLM populations\\\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \\\"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\\\" Do NOT claim \\\">15% at all thresholds\\\" — be honest that 2.5 drops below.\\n\\n8. **\\\"Multiple testing: 12,508 simultaneous tests without correction\\\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\\n\\n9. **\\\"Only uniform DIF — non-uniform DIF plausible for LLMs\\\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \\\"our 31% uniform-only estimate is conservative.\\\"\\n\\n10. **\\\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\\\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\\n\\n11. **\\\"Ranking disruption result is tautological\\\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\\n\\n## Dropped from Original Framing\\n\\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\\n- **Detection as primary contribution**: Pivoted from \\\"we detect contamination\\\" to \\\"we characterize benchmark properties.\\\"\\n\", \"total_chars\": 20006, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae44e30a-a234-4533-aa3e-9e8d84f23d29",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "3732b6b6-f4bb-46e6-805d-d1c216eb80b4",
  "sourceToolAssistantUUID": "ae44e30a-a234-4533-aa3e-9e8d84f23d29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T11:55:40.172Z_

Now let me read the actual paper sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3732b6b6-f4bb-46e6-805d-d1c216eb80b4",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfsPnpRZgYcuySvxjKi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c60cdc3a-8876-4e61-ab9b-5b2a15a62f9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYt3m3piCvPo5pkr4WR2ZD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20510,
      "cache_read_input_tokens": 17817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20510,
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

_source line 14 · 2026-05-21T11:55:42.057Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WNfPbhNBpX4wZwFTG1LA2b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c60cdc3a-8876-4e61-ab9b-5b2a15a62f9f",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfsPnpRZgYcuySvxjKi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d5083fb-b9ae-4f62-a85e-05c9aee80403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYt3m3piCvPo5pkr4WR2ZD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20510,
      "cache_read_input_tokens": 17817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20510,
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

_source line 15 · 2026-05-21T11:55:42.062Z_

<details><summary>↩ Tool result · `toolu_01WNfPbhNBpX4wZwFTG1LA2b`</summary>

```text
1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet the assumption that individual items measure the same construct over time is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (DIF) analysis with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 total items), and find that 17.9--31.3\% of items exhibit large DIF (ETS Category~C) between 2023 and 2024 model cohorts---knowledge/reasoning benchmarks show higher instability (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$), each 45--174$\times$ above random baselines. This does not threaten benchmark validity ($\rho \approx 0.997$ between full and stable-item rankings) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of instability is item-specific; a Simpson's paradox in odds ratio regression confirms item properties, not accuracy gains, drive DIF. We expose a validation methodology gap: web-overlap labels measure global exposure, not differential functioning (enrichment $\approx 0.96$). A semi-synthetic injection framework with cross-subject matching preserves detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) with zero false positive inflation. DIF-flagged items concentrate cross-generational discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal), and a difficulty--direction interaction ($\rho = -0.597$) reveals that capability gains concentrate on hard items while easy items erode, suggesting DIF captures genuine capability change rather than noise. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d5083fb-b9ae-4f62-a85e-05c9aee80403",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "55fca3b4-a7b8-464f-8012-58ea490228d0",
  "sourceToolAssistantUUID": "7d5083fb-b9ae-4f62-a85e-05c9aee80403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T11:55:42.466Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cx4ymRKu5T89zfKkywxBbD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55fca3b4-a7b8-464f-8012-58ea490228d0",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfsPnpRZgYcuySvxjKi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a84c23e6-6019-4ba1-b002-f6b500b40045",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYt3m3piCvPo5pkr4WR2ZD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20510,
      "cache_read_input_tokens": 17817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20510,
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

_source line 17 · 2026-05-21T11:55:42.474Z_

<details><summary>↩ Tool result · `toolu_01Cx4ymRKu5T89zfKkywxBbD`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench}, and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, and Self-Critique~\citep{tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not measure \emph{differential item functioning}: whether an item behaves differently across model cohorts that may have had varying degrees of exposure or different training methodologies. \Cref{fig:global_vs_differential} illustrates the distinction. Most MMLU items are globally contaminated in the sense that they exist in web-accessible text, so all model cohorts encounter them and no differential signal arises. The items that function differentially are those where exposure or training methodology changed asymmetrically across cohorts. Validating differential detectors against global-exposure labels therefore conflates two phenomena. Direct comparison confirms near-independence between the two flag sets (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), consistent across contamination subtypes.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_1_global_vs_differential.pdf}
11	\caption{Global vs.\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}
12	\label{fig:global_vs_differential}
13	\end{figure}
14	
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), to our knowledge, the largest-scale DIF analysis on LLM benchmarks. This psychometric approach complements concurrent work on anchor-item calibration for score comparability~\citep{habba2026growingpains} and addresses the fragility of existing contamination detectors under post-training perturbation~\citep{wang2026fragility}. Semi-synthetic injection experiments confirm that DIF detects differential contamination when present ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminates false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural controls (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject pre-checks) confirm that the 31\% temporal instability cannot be attributed to methodological artifacts, establishing it as a robust empirical finding about LLM benchmark measurement properties, replicated across all six METABENCH benchmarks (\Cref{sec:gsm8k}).
16	
17	MMLU's 12,508 items provide sufficient measurement redundancy that removing nearly a third does not alter rank order ($\rho \approx 0.997$). DIF should therefore be understood as a diagnostic lens rather than a quality filter. DIF-flagged items concentrate discriminative signal: removing them degrades ranking discriminability more than random removal ($z = -8\sigma$ to $-49\sigma$ across 21 conditions). Model families show distinctive DIF profiles: Llama-3 derivatives gain a median of ${+}53$ rank positions under stable-item evaluation, while Mistral-based models lose a median of $35$; 25\% of models shift by $|\Delta\mathrm{Rank}| \geq 100$.
18	
19	The MH-DIF procedure is well-established in psychometrics~\citep{holland1988mh,clauser1998dif}; the cross-subject matching strategy has psychometric precedent~\citep{nandakumar1993dif}. Our contributions are therefore empirical and methodological, not algorithmic: (a)~the first large-scale DIF characterization across six LLM benchmarks (27,125 items, 5,227 models), finding 17.9--31.3\% temporal instability robust across thresholds and unrelated to accuracy gains (confirmed by Simpson's paradox in odds ratio regression); (b)~a ground truth meta-critique exposing that web-overlap labels are poorly suited to evaluate item-level differential detectors; (c)~a reusable semi-synthetic validation framework with cross-subject matching that addresses LLM-specific challenges (multi-domain local dependence handling and simultaneous contamination control, $\Delta\mathrm{FPR} = 0.000$), confirmed on GSM8K; and (d)~a concrete DIF audit protocol for benchmark maintenance (\Cref{sec:disc_protocol}). We make the following contributions:
20	
21	\begin{enumerate}
22	\item \textbf{Benchmark temporal comparability} (Claim 1): 31\% of MMLU items are functionally unstable across model generations under ETS~C classification; replication across all six METABENCH benchmarks yields C\% $= 17.9$--$31.3\%$ (45--174$\times$ above random baselines), with knowledge/reasoning benchmarks showing higher instability than procedural ones (\Cref{sec:temporal,sec:gsm8k}).
23	
24	\item \textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\citep{li2024contamination} do not provide appropriate ground truth for item-level differential detectors. Direct empirical comparison on 9,229 items shows near-independence (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), exposing a validation methodology gap in the contamination detection literature (\Cref{sec:groundtruth}).
25	
26	\item \textbf{Semi-synthetic validation framework} (Claim 3): Controlled injection with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\Cref{sec:semisynthetic,sec:gsm8k}).
27	
28	\item \textbf{DIF as diagnostic lens} (Claim 4): DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal, Jaccard overlap with high-discrimination items $= 0.12$) and exhibit a structured difficulty--direction interaction ($\rho = -0.597$): capability gains concentrate on hard items while easy items erode (\Cref{sec:downstream}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a84c23e6-6019-4ba1-b002-f6b500b40045",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "06dffc1d-1d89-43b8-8449-8edb206b04e5",
  "sourceToolAssistantUUID": "a84c23e6-6019-4ba1-b002-f6b500b40045",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T11:55:43.160Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UWzdzvzthEox4mAzxFFqq1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06dffc1d-1d89-43b8-8449-8edb206b04e5",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfsPnpRZgYcuySvxjKi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6e19f58-c687-4d08-9f52-1c6103bcb2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYt3m3piCvPo5pkr4WR2ZD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20510,
      "cache_read_input_tokens": 17817,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20510
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 17817,
          "cache_creation_input_tokens": 20510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20510,
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

_source line 19 · 2026-05-21T11:55:43.172Z_

<details><summary>↩ Tool result · `toolu_01UWzdzvzthEox4mAzxFFqq1`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (Claim~2, \Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrated that not all evaluation examples are equally informative. Recent extensions include PSN-IRT \citep{zhou2026psnirt} for benchmark quality at scale, TinyBenchmarks \citep{maiapolo2024tinybenchmarks} for IRT-based item selection, and scalability coefficients for detecting bad benchmark items \citep{hardy2026scalability}. The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which addresses score comparability through fixed-parameter calibration \citep[FPC;][]{kim2019fpc}. Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items violate this assumption.
9	
10	\paragraph{DIF Methodology and Measurement Invariance.}
11	The Mantel-Haenszel procedure for DIF detection was introduced by \citet{holland1988mh} and remains the most widely used method in educational testing due to its simplicity and well-characterized statistical properties \citep{clauser1998dif}. Alternative approaches include logistic regression DIF \citep{swaminathan1990logistic}, SIBTEST \citep{shealy1993sibtest}, Lord's $\chi^2$ test \citep{lord1980irt}, and the Raju area method \citep{raju1988area}; \citet{zumbo1999handbook} provides a comprehensive comparison. DIF analysis is a specific instance of measurement invariance testing \citep{meredith1993invariance, vandenberg2000invariance}, which examines whether a measurement instrument functions equivalently across populations. MIMIC models offer a latent-variable approach to the same problem \citep{muthen1985mimic, woods2009mimic}, and \citet{teresi2007dif} reviews DIF methods across applied domains. Cross-subject matching---computing the stratification variable from domains other than the one being tested---has psychometric precedent in the DIF literature \citep{nandakumar1993dif,donoghue1993mh}; our adaptation addresses LLM-specific challenges of multi-domain local dependence and simultaneous contamination control at scale. We do not modify the MH procedure; our contribution is the application context and the empirical findings it reveals. The scale of this analysis (5,227 examinees across a 57-subject multidimensional ability space) exceeds typical educational testing applications, where \citet{belzak2020smallsample} note that DIF methods can behave differently at extreme sample sizes. The primary methodological challenge is the impact-versus-DIF confound: genuine ability differences between temporal cohorts can inflate DIF estimates. We address this through matched-ability quintile analysis, IRT $\theta$-conditioning, and a random-split control (\Cref{sec:temporal}).
12	
13	\paragraph{Benchmark Design and Evaluation.}
14	Dynamic benchmarks such as Dynabench \citep{kiela2021dynabench}, LatestEval \citep{li2024latesteval}, and LiveBench \citep{white2025livebench} mitigate contamination by construction, yet none provides psychometric equating across versions. Chatbot Arena \citep{chiang2024chatbot} sidesteps static benchmarks through pairwise preference. Broader surveys \citep{chang2024survey, burnell2023rethink} identify benchmark saturation and lack of item-level transparency as systemic challenges. Our DIF analysis fills this gap by identifying which items have become unreliable for cross-generation comparison. METABENCH \citep{kipnis2024metabench} provides the large-scale response matrix that makes this analysis possible.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6e19f58-c687-4d08-9f52-1c6103bcb2ae",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "01b50dca-d4e6-450b-abe3-cd870201c9d1",
  "sourceToolAssistantUUID": "a6e19f58-c687-4d08-9f52-1c6103bcb2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T11:55:47.378Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AHeC8z3Msy1oqnPXACYXjn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01b50dca-d4e6-450b-abe3-cd870201c9d1",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfssxireCD2bwQ1xnoG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a25d08a5-2948-42a9-b745-39220a21a6ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dBVVHmX6qSjFQJTe56mDT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4405,
      "cache_read_input_tokens": 38327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4405,
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

_source line 21 · 2026-05-21T11:55:47.385Z_

<details><summary>↩ Tool result · `toolu_01AHeC8z3Msy1oqnPXACYXjn`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$) and computing a common odds ratio across strata. We use $K = 5$ equiprobable strata (quintile-based binning) following ETS recommended practice for large-scale assessments~\citep{donoghue1993mh,clauser1998dif}. Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
17	
18	\begin{equation}
19	\label{eq:mh}
20	\alpha_{\mathrm{MH}} = \frac{\displaystyle\sum_{k=1}^{K} A_k D_k \,/\, T_k}{\displaystyle\sum_{k=1}^{K} B_k C_k \,/\, T_k}\,,
21	\end{equation}
22	
23	\noindent where $A_k$ and $B_k$ are the number of correct and incorrect responses in the reference group for stratum $k$, $C_k$ and $D_k$ are the corresponding counts for the focal group, and $T_k$ is the total number of examinees in stratum $k$. Under the null hypothesis of no DIF, $\alpha_{\mathrm{MH}} = 1$. The log odds ratio is converted to the ETS delta scale:
24	
25	\begin{equation}
26	\label{eq:delta}
27	\Delta_{\mathrm{MH}} = -2.35 \ln(\alpha_{\mathrm{MH}})\,.
28	\end{equation}
29	
30	The Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\Delta_{\mathrm{MH}}|$. Category~A (negligible) requires $|\Delta_{\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\Delta_{\mathrm{MH}}| \geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \leq |\Delta_{\mathrm{MH}}| < 1.5$, or $|\Delta_{\mathrm{MH}}| \geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \emph{and} significance) guards against flagging items that show large but unreliable effect sizes. Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\%.
31	
32	The choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\emph{cross-subject matching} uses the total score on all subjects \emph{other than} the one containing the item under test, preventing the matching variable from absorbing injected contamination signals (\Cref{sec:injection}); and (3)~\emph{external matching} uses the total score on a different benchmark entirely (e.g., MMLU total score as the matching variable when testing DIF on GSM8K items), providing an independent ability proxy uncontaminated by the target benchmark. Cross-subject and external matching both address matching variable contamination but at different granularities: cross-subject operates within a multi-domain benchmark, while external operates across benchmarks.
33	
34	\subsection{Cohort Designs}
35	\label{sec:cohorts}
36	
37	We construct five cohort comparisons: (1)~\emph{Temporal}: 2023 ($N = 1{,}080$) vs.\ 2024 ($N = 807$) models, the primary comparison; (2)~\emph{Ability-quintile}: Q1--Q2 vs.\ Q4--Q5 within the same temporal window, testing whether ability differences alone produce DIF; (3)~\emph{Within-family}: Llama-2 ($N = 161$) vs.\ Llama-3 ($N = 308$), isolating generational changes within a single family; (4)~\emph{Within-subject}: per-subject DIF to test domain concentration; and (5)~\emph{Random split}: two random halves of the 2023 cohort ($N = 540$ each) as a sanity check.
38	
39	\subsection{Semi-Synthetic Injection Framework}
40	\label{sec:injection}
41	
42	To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.
43	
44	\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \in \{0.0, 0.3, 0.5, 0.7, 1.0\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\Delta\mathrm{TPR} = \mathrm{TPR}(\text{injected}) - \mathrm{TPR}(\text{baseline})$ and $\Delta\mathrm{FPR} = \mathrm{FPR}(\text{injected}) - \mathrm{FPR}(\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation.
45	
46	\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this problem by computing the matching variable from all subjects \emph{other than} the one being tested. Under this protocol, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU domains (bootstrap 95\% CI $= [0.000, 0.000]$, 5,000 resamples), while detection power is preserved ($\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$ for four of five subjects). The zero FPR is a structural guarantee: cross-subject stratification scores are algebraically invariant to within-subject injection~\citep{clauser1998dif, nandakumar1993dif}. We adopt cross-subject matching as the standard protocol for all semi-synthetic analyses.
47	
48	Diagnostic procedures (Yen's Q3 local independence, domain-specificity analysis, instability decomposition) and statistical details (multiple testing correction, threshold sensitivity, architecture heterogeneity checks) appear in \Cref{app:method_details}.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a25d08a5-2948-42a9-b745-39220a21a6ad",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "f68c65d0-fbf0-4621-8874-b0ffdbbf92a8",
  "sourceToolAssistantUUID": "a25d08a5-2948-42a9-b745-39220a21a6ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T11:55:47.956Z_

<details open><summary>🔧 Tool call — Read · `toolu_018P5gFg9HjFXF6wvQCLz4Ha`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f68c65d0-fbf0-4621-8874-b0ffdbbf92a8",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfssxireCD2bwQ1xnoG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c113f48-396e-49eb-90ee-f8499e9ddf75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dBVVHmX6qSjFQJTe56mDT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4405,
      "cache_read_input_tokens": 38327,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4405
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 38327,
          "cache_creation_input_tokens": 4405,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4405,
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

_source line 23 · 2026-05-21T11:55:47.960Z_

<details><summary>↩ Tool result · `toolu_018P5gFg9HjFXF6wvQCLz4Ha`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A power analysis using empirical MMLU IRT parameters confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$. Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\%. Crucially, the temporal cohort ability gap is negligible: Cohen's $d = -0.17$ (below the $|d| = 0.2$ small-effect threshold) with 76.4\% distributional overlap. Under strict 1:1 nearest-neighbor matching ($d \approx -0.010$, $N = 638$ per group, 5 seeds), C\% $= 28.9\% \pm 0.1\%$---a 7.7\% relative reduction from 31.3\%, confirming that at most $\sim$2.4 pp of observed DIF is attributable to ability mismatch.
17	
18	Across all 57 MMLU subjects, C\% ranges from 20.7\% to 48.4\% (mean $\approx 30\%$); within-subject matching on 5 subjects yields 38.1\% as a robustness check (\Cref{tab:temporal_landscape}). Item-level logistic regression shows domain accuracy improvement explains only 2.4 percentage points of 31.3\% C\% (pseudo $R^2 = 0.0007$); 92.4\% of instability is item-specific. Odds ratio regression reveals a Simpson's paradox: domain accuracy improvement positively predicts DIF at the aggregate level ($\mathrm{OR} = 1.55$ per 10 pp, $p = 0.001$) but reverses after controlling for item difficulty and discrimination ($\mathrm{OR} = 0.73$, $p = 0.030$; LR $\chi^2 = 647$), confirming that item properties---not accuracy gains---drive DIF classification. The conclusion is robust across thresholds: C\% $= 48.9\%$ at $|\Delta_{\mathrm{MH}}| \geq 1.0$, $18.3\%$ at $\geq 2.0$, $10.2\%$ at $\geq 2.5$.
19	
20	\begin{table}[t]
21	\centering
22	\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\Delta_{\mathrm{MH}}| \geq 1.5$. FPR is measured against Li et al.\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}
23	\label{tab:temporal_landscape}
24	\small
25	\resizebox{\columnwidth}{!}{%
26	\begin{tabular}{lcccc}
27	\toprule
28	Cohort Definition & $N_{\mathrm{ref}}$ / $N_{\mathrm{focal}}$ & C\% & FPR (clean) & Enrich. \\
29	\midrule
30	Temporal (2023 vs.\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\
31	Ability quintile (Q1--2 vs.\ Q4--5) & ${\sim}$2,600 / ${\sim}$2,600 & 2.9 & 0.027 & 1.19 \\
32	Within-family (Llama-2 vs.\ 3) & 161 / 308 & 61.3 & -- & -- \\
33	Random split (sanity) & 540 / 540 & 0.18 & -- & -- \\
34	Within-subject (avg, 5 subj.) & \textit{varies} & 38.1 & -- & -- \\
35	\bottomrule
36	\end{tabular}}
37	\end{table}
38	
39	\subsection{Ground Truth Mismatch}
40	\label{sec:groundtruth}
41	
42	Direct comparison of DIF flags against the web-overlap labels of \citet{li2024contamination} on 9,229 annotated items confirms that the two methods capture orthogonal signals. The enrichment ratio is 0.964 (\Cref{tab:temporal_landscape}): DIF-C rates are 30.7\% among web-contaminated items and 31.8\% among clean items. Association tests yield $\phi = 0.012$, $\chi^2 = 1.28$ ($p = 0.258$), and OR $= 1.05$ [0.96, 1.15]; the Jaccard index between flagged sets is 0.206. This near-independence holds across contamination subtypes (input-only enrichment $= 0.986$, input-and-label $= 0.960$). The null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \emph{global exposure} (whether an item exists in training corpora), while DIF measures \emph{differential functioning} (whether an item's relationship to ability changes across cohorts). The Li et al.\ labels are the wrong ground truth for a differential method.
43	
44	\begin{figure}[t]
45	\centering
46	\includegraphics[width=\columnwidth]{fig_2_dose_response.pdf}
47	\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\Delta\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF detects differential contamination when present. Baseline (no injection) produces $\Delta\mathrm{TPR} \approx 0$.}
48	\label{fig:dose_response}
49	\end{figure}
50	
51	\subsection{Structural Analysis}
52	\label{sec:structural}
53	
54	Three structural controls fail to reduce temporal C\% below 31\%: matched-ability quintiles, IRT $\theta$-conditioning ($r(\theta, \mathrm{total\ score}) = 0.9986$, FPR $= 0.312$), and within-subject DIF (C\% $= 38.1\%$, exceeding the 25\% bifactor viability threshold). Logistic regression DIF confirms 92.1\% concordance with MH and reveals additional non-uniform DIF (24.8\% at $|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% estimate conservative. Graduated de-duplication ($K{=}10$: 22.7\% vs.\ random 26.8\%; $K{=}20$: 29.1\% vs.\ 30.9\%) confirms family structure does not inflate C\%. Ability-matched within-family analysis reduces Llama-2 vs.\ Llama-3 C\% from 61.3\% to $28.3\% \pm 1.6\%$ (Cohen's $d = -0.99$, overlap $= 0.18$), while temporal matching reduces C\% from 31.3\% to $28.9\% \pm 0.1\%$ ($d = -0.17$, overlap $= 0.76$). The matched C\% values ($\sim$28--29\%) are consistent with each other despite vastly different unmatched rates (61.3\% vs.\ 31.3\%), suggesting that genuine item-level DIF accounts for $\sim$28--29\% of items, with the Llama comparison carrying 33 pp of additional ability confound (54\% reduction) versus only 2.4 pp for temporal cohorts (7.7\% reduction). Full details in \Cref{app:structural}.
55	
56	\subsection{Semi-Synthetic Framework Validation}
57	\label{sec:semisynthetic}
58	
59	The critical methodological finding is that the choice of matching strategy determines validity. Cross-subject matching computes the conditioning variable from subjects \emph{other than} the one being tested, achieving $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects while four of five produce $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$. Within-subject matching inflates FPR by ${+}0.186$ on average because the matching variable absorbs part of the injection signal. We adopt cross-subject matching as the standard protocol (\Cref{app:fig_matching}).
60	
61	\subsection{Downstream Impact}
62	\label{sec:downstream}
63	
64	Spearman correlation between full and stable-item rankings is $\rho \approx 0.997$: aggregate model ordering is preserved despite 31\% item instability. DIF-flagged items nonetheless carry more discriminative signal than average ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal across 21 conditions), though a circularity ablation shows DIF-based removal is the \emph{least} disruptive among non-random strategies (Jaccard overlap with high-discrimination items is only 0.12). Individual model families show distinctive DIF profiles: Llama-3 derivatives gain a median of ${+}53$ rank positions (mean ${+}121$), while Mistral-based models lose a median of $35$ (mean $-54$); individual extremes reach ${+}793$ and $-542$ (\Cref{app:fig_downstream}). Overall, 25\% of models shift by $|\Delta\mathrm{Rank}| \geq 100$. \Cref{sec:gsm8k} demonstrates that this instability pattern extends across all six METABENCH benchmarks.
65	
66	\subsection{Cross-Benchmark Validation}
67	\label{sec:gsm8k}
68	
69	Temporal DIF extends across all six METABENCH benchmarks (\Cref{tab:cross_benchmark}). C\% ranges from 17.9\% (HellaSwag) to 31.3\% (MMLU), each 45--174$\times$ above its random-split baseline---none attributable to sampling noise. A task-type dichotomy emerges: knowledge and reasoning benchmarks (MMLU, WinoGrande~\citep{sakaguchi2021winogrande}, TruthfulQA~\citep{lin2022truthfulqa}, ARC~\citep{clark2018arc}) show C\% $= 26.9$--$31.3\%$, while procedural benchmarks (GSM8K, HellaSwag~\citep{zellers2019hellaswag}) show C\% $= 17.9$--$18.9\%$, consistent with knowledge-intensive items being more sensitive to shifts in training data composition across model generations.
70	
71	\begin{table}[t]
72	\centering
73	\caption{Temporal DIF across six METABENCH benchmarks. C\% = ETS~C items ($|\Delta_{\mathrm{MH}}| \geq 1.5$) between 2023 and 2024 cohorts. All six show substantial instability (45--174$\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\% than procedural ones.}
74	\label{tab:cross_benchmark}
75	\small
76	\begin{tabular}{lrrrl}
77	\toprule
78	Benchmark & Items & C\% & Rand.\ C\% & Ratio \\
79	\midrule
80	MMLU & 12{,}508 & 31.3 & 0.18 & 174$\times$ \\
81	WinoGrande & 1{,}267 & 30.3 & 0.32 & 95$\times$ \\
82	TruthfulQA & 817 & 29.7 & 0.37 & 80$\times$ \\
83	ARC & 1{,}172 & 26.9 & 0.60 & 45$\times$ \\
84	GSM8K & 1{,}319 & 18.9 & 0.30 & 63$\times$ \\
85	HellaSwag & 10{,}042 & 17.9 & 0.28 & 64$\times$ \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	On GSM8K specifically, semi-synthetic injection with external matching confirms detection power ($\Delta\mathrm{TPR} = {+}0.514$ at $p = 0.5$; \Cref{app:gsm8k_details}). An exploratory GSM1K analysis ($N = 33$) shows a negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$, $p = 0.005$; partial $r = -0.385$, $p = 0.027$), suggesting DIF captures capability change distinct from memorization (\Cref{app:fig_gsm1k}).
91	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c113f48-396e-49eb-90ee-f8499e9ddf75",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "2665fa9c-6abe-4d1f-9b5c-4df2076a5cae",
  "sourceToolAssistantUUID": "8c113f48-396e-49eb-90ee-f8499e9ddf75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T11:55:52.793Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DsbpRw3t9ybrA9d2tAWJ9H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2665fa9c-6abe-4d1f-9b5c-4df2076a5cae",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFftEMoy7VJbUroA1GMq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61651667-38e3-440c-a146-5fb1b843073c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqznsxG83VSZvzPpHT7vvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 42732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 25 · 2026-05-21T11:55:52.797Z_

<details><summary>↩ Tool result · `toolu_01DsbpRw3t9ybrA9d2tAWJ9H`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C instability on MMLU is robust across thresholds and structural controls (\Cref{sec:structural}), and extends across all six METABENCH benchmarks (C\% $= 17.9$--$31.3\%$, 45--174$\times$ above random baselines; \Cref{tab:cross_benchmark}). Knowledge/reasoning benchmarks show higher instability (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$), and a Simpson's paradox in odds ratio regression ($\mathrm{OR}: 1.55 \to 0.73$ after controlling for item properties; LR $\chi^2 = 647$) confirms that item properties---not accuracy gains---drive DIF. This does not invalidate these benchmarks as ranking instruments ($\rho \approx 0.997$) but signals measurement drift across model generations.
8	
9	\subsection{Ground Truth Meta-Critique}
10	\label{sec:disc_groundtruth}
11	
12	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$; consistent across contamination subtypes) exposes a category error: web-overlap labels identify a condition shared by nearly all MMLU items (global exposure), so evaluating a differential method against them conflates two phenomena. Item-level differential detectors require item-level differential ground truth.
13	
14	\subsection{DIF as Diagnostic Lens}
15	\label{sec:disc_diagnostic}
16	
17	The GSM1K correlation ($r = -0.478$, $p = 0.005$, $N = 33$; \Cref{sec:gsm8k}) provides exploratory evidence that DIF-flagged items capture behavioral change distinct from memorization; partial correlation ($r = -0.385$, $p = 0.027$) after controlling for accuracy confirms this is not an artifact of general model quality.
18	
19	Item characterization reinforces this: DIF-C items are harder ($d = -0.247$) and more discriminating ($d = 0.230$), distributed uniformly across subjects ($\chi^2$ $p = 0.32$). A difficulty $\times$ direction interaction ($\rho = -0.597$, $p < 0.001$) shows capability gains concentrate on hard items (88.7\% focal-favoring in hardest decile) while easy items erode (96.2\% reference-favoring in easiest decile).
20	
21	Yen's Q3 analysis confirms that local dependence does not drive DIF: extreme LD correlates negligibly with subject-level C\% ($r = 0.09$, $p = 0.50$), while reasoning-heavy domains with low LD show higher DIF ($r = -0.36$, $p = 0.006$).
22	
23	\subsection{Recommended DIF Audit Protocol}
24	\label{sec:disc_protocol}
25	
26	These findings motivate a concrete benchmark maintenance protocol requiring only a binary response matrix and temporal cohort labels. We recommend: (1)~quarterly MH-DIF audits (or whenever $N \geq 80$ new models appear), using cross-subject matching; (2)~benchmark-wide C\% $> 20\%$ triggers item review, with items flagged ETS~C in consecutive audits labeled ``unstable''; (3)~graduated responses: flag-and-annotate, item rotation, or weighted scoring.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61651667-38e3-440c-a146-5fb1b843073c",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "4fd5e9fd-995b-42fb-8746-d2068caa4136",
  "sourceToolAssistantUUID": "61651667-38e3-440c-a146-5fb1b843073c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T11:55:53.281Z_

<details open><summary>🔧 Tool call — Read · `toolu_014J5u6JeTFwKXWCXufxNugB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fd5e9fd-995b-42fb-8746-d2068caa4136",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFftEMoy7VJbUroA1GMq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed77f420-25e8-44ce-b2af-abf0cc90abb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqznsxG83VSZvzPpHT7vvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 42732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 27 · 2026-05-21T11:55:53.286Z_

<details><summary>↩ Tool result · `toolu_014J5u6JeTFwKXWCXufxNugB`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Applying MH-DIF analysis to six METABENCH benchmarks (27,125 items, 5,227 models), we find 17.9--31.3\% temporal item instability under ETS~C classification---knowledge/reasoning benchmarks are more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). The instability is confirmed non-random (random controls $\leq 0.6\%$) and item-specific; a Simpson's paradox in odds ratio regression confirms item properties, not accuracy gains, drive DIF. Web-overlap labels show near-independence with DIF flags (enrichment $\approx 0.96$); our semi-synthetic framework ($\Delta\mathrm{FPR} = 0.000$, $\Delta\mathrm{TPR} = {+}0.508$) provides a controlled alternative.
5	
6	DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal) and exhibit a difficulty--direction interaction ($\rho = -0.597$): capability gains on hard items, erosion on easy ones. DIF is a diagnostic lens, not a quality filter. LLM benchmarks need psychometric monitoring alongside score reporting.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed77f420-25e8-44ce-b2af-abf0cc90abb0",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "c781dd62-b5aa-4a82-8b21-469e5d76ff07",
  "sourceToolAssistantUUID": "ed77f420-25e8-44ce-b2af-abf0cc90abb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T11:55:53.603Z_

<details open><summary>🔧 Tool call — Read · `toolu_01656W74BQYxvhYhjkEiLqvc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c781dd62-b5aa-4a82-8b21-469e5d76ff07",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFftEMoy7VJbUroA1GMq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d8bb135-07b4-4028-bd00-fe737d64bc05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqznsxG83VSZvzPpHT7vvv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 42732,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 42732,
          "cache_creation_input_tokens": 6447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6447,
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

_source line 29 · 2026-05-21T11:55:53.608Z_

<details><summary>↩ Tool result · `toolu_01656W74BQYxvhYhjkEiLqvc`</summary>

```text
1	\section*{Limitations}
2	
3	\paragraph{Methodological scope of MH-DIF.}
4	The Mantel-Haenszel procedure detects only \emph{uniform} DIF, where the odds ratio between cohorts is constant across ability strata. Logistic regression DIF analysis reveals an additional 24.8\% of items exhibiting non-uniform DIF ($|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% ETS~C estimate conservative. Future work should apply non-uniform DIF methods (e.g., logistic regression or IRT-based approaches) as the primary analysis to capture the full spectrum of item instability. Critically, MH-DIF is nonparametric and conditions on observed total score, not latent $\theta$---its validity does not depend on IRT model fit~\citep{holland1988mh}. Our Yen's Q3 analysis confirms that local dependence domains do not correlate with DIF domains ($r = 0.09$, $p = 0.50$), further supporting the robustness of the MH procedure in this setting.
5	
6	\paragraph{Ability confounding.}
7	Although the temporal cohort ability gap is negligible (Cohen's $d = -0.17$, overlap $= 76.4\%$) and nearest-neighbor matching confirms that at most 2.4 percentage points of C\% are attributable to ability mismatch, within-family comparisons with large ability gaps (e.g., Llama-2 vs.\ Llama-3, $d = -0.99$) produce substantially inflated C\% (61.3\% unmatched vs.\ 28.3\% matched). Any application of MH-DIF to cohorts with larger ability differences must incorporate ability matching or stratification beyond the standard 5-strata procedure.
8	
9	\paragraph{Sample size requirements.}
10	Our power analysis indicates reliable ETS~C detection requires $N \geq 80$ per cohort. The temporal cohorts (1,080 and 807 models) far exceed this threshold, but the GSM1K correlation analysis ($N = 33$) has limited statistical power (95\% CI $= [-0.71, -0.16]$). The negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$) is exploratory and warrants replication with larger model samples.
11	
12	\paragraph{Contamination vs.\ capability change.}
13	DIF analysis detects \emph{that} items function differently across cohorts but cannot determine \emph{why}. The differential signal may reflect contamination, capability change, training methodology shifts, or interactions among these factors. We present evidence that DIF captures something distinct from memorization (negative GSM1K correlation, semi-synthetic dose-response), but a definitive causal decomposition remains out of reach without access to model training data.
14	
15	\paragraph{Benchmark scope.}
16	We analyze six METABENCH benchmarks (MMLU, WinoGrande, TruthfulQA, ARC, GSM8K, HellaSwag; 27,125 total items), all multiple-choice or short-answer benchmarks scored as binary correct/incorrect. The generalizability to open-ended generation benchmarks (e.g., AlpacaEval, MT-Bench), coding benchmarks (e.g., HumanEval), or benchmarks with non-binary scoring remains untested. The binary response format is a prerequisite for MH-DIF; extending to continuous or partial-credit scoring would require polytomous DIF methods.
17	
18	\paragraph{Temporal cohort definition.}
19	We define cohorts by calendar year of model release (2023 vs.\ 2024), a coarse grouping that aggregates models with diverse training pipelines, data mixtures, and post-training procedures. Finer-grained cohort definitions (e.g., by training data cutoff, model family, or alignment method) might reveal more targeted patterns of item instability but would reduce per-cohort sample sizes and statistical power.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d8bb135-07b4-4028-bd00-fe737d64bc05",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "cc880b26-cc54-4613-be73-0c3be7d199a5",
  "sourceToolAssistantUUID": "7d8bb135-07b4-4028-bd00-fe737d64bc05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T11:55:57.611Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XFrujwAKQfZLNinEWEHx1b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc880b26-cc54-4613-be73-0c3be7d199a5",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfteYbyuHzCJm5VzfW9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25b8e8c6-8116-41af-82df-6c03c64caf4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqqfnnjNkAAh4DGLJmndXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2586,
      "cache_read_input_tokens": 49179,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2586,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 31 · 2026-05-21T11:55:57.615Z_

<details><summary>↩ Tool result · `toolu_01XFrujwAKQfZLNinEWEHx1b`</summary>

```text
1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.
19	
20	\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\Delta_{\mathrm{MH}}| \in \{1.0, 1.5, 2.0, 2.5\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\Delta_{\mathrm{MH}}| \geq 1.5$ corresponds to the ETS~C definition used throughout the paper.
21	
22	\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.
23	
24	\section{Structural Analysis Details}
25	\label{app:structural}
26	
27	Three progressively refined approaches fail to reduce the temporal false positive rate below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\% $= 38.1\%$, exceeding the 25\% threshold that would indicate viable bifactor structure. \Cref{tab:structural_comparison} summarizes these results.
28	
29	The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $5{\times}$ ratio, $p = 2.3 \times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\% persists under external matching (full Q3 distributions in Appendix~Figure~A2).
30	
31	\begin{table}[h]
32	\centering
33	\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\%, indicating that the observed instability is not an artifact of ability matching. Subscript $\pm$ values denote standard deviations across 5 injection seeds (baseline row only).}
34	\label{tab:structural_comparison}
35	\small
36	\resizebox{\columnwidth}{!}{%
37	\begin{tabular}{lcccc}
38	\toprule
39	Approach & Mechanism & Temp.\ FPR & TPR ($p{=}0.5$) & Outcome \\
40	\midrule
41	Baseline (ext.) & Cross-bench.\ total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
42	Matched-ability & Within-quintile temp.\ DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
43	$\theta$-cond. & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
44	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
45	\bottomrule
46	\end{tabular}}
47	\end{table}
48	
49	\section{Additional Figures}
50	\label{app:figures}
51	
52	\begin{figure}[h]
53	\centering
54	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
55	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
56	\label{app:fig_matching}
57	\end{figure}
58	
59	\begin{figure}[h]
60	\centering
61	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
62	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}
63	\label{app:fig_downstream}
64	\end{figure}
65	
66	\begin{figure}[h]
67	\centering
68	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
69	\caption{GSM1K contamination gap vs.\ DIF ranking advantage ($N = 33$). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items.}
70	\label{app:fig_gsm1k}
71	\end{figure}
72	
73	\section{Cross-Benchmark Comparison}
74	\label{app:gsm8k_details}
75	
76	\begin{table}[h]
77	\centering
78	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
79	\label{tab:gsm8k_comparison}
80	\small
81	\begin{tabular}{lcc}
82	\toprule
83	Metric & MMLU & GSM8K \\
84	\midrule
85	Items & 12,508 & 1,319 \\
86	Models & 5,227 & 6,702 \\
87	Temporal C\% & 31.3\% & 18.9\% \\
88	Sanity C\% & 0.18\% & 0.3\% \\
89	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
90	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25b8e8c6-8116-41af-82df-6c03c64caf4b",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "23ba9e98-5c5d-45ba-8085-f1da72d519cf",
  "sourceToolAssistantUUID": "25b8e8c6-8116-41af-82df-6c03c64caf4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T11:55:57.930Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XDkhXfAXyS6V9xKazpYTwi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23ba9e98-5c5d-45ba-8085-f1da72d519cf",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfteYbyuHzCJm5VzfW9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cd6c4dd-f6ec-4ec6-af47-065fb3c9b6a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqqfnnjNkAAh4DGLJmndXX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2586,
      "cache_read_input_tokens": 49179,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 49179,
          "cache_creation_input_tokens": 2586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2586,
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

_source line 33 · 2026-05-21T11:55:57.934Z_

<details><summary>↩ Tool result · `toolu_01XDkhXfAXyS6V9xKazpYTwi`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cd6c4dd-f6ec-4ec6-af47-065fb3c9b6a8",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "f9a0272e-9124-4637-9995-de13225734f8",
  "sourceToolAssistantUUID": "7cd6c4dd-f6ec-4ec6-af47-065fb3c9b6a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-21T11:56:01.035Z_

Now let me check the bibliography to assess reference completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9a0272e-9124-4637-9995-de13225734f8",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFftxyP2rd9wCojxV3hg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12ec0477-80c0-473f-bf8c-1445fc0e4d67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDHuqiBf46xiwZps2PEW6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3048,
      "cache_read_input_tokens": 51765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3048,
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

_source line 35 · 2026-05-21T11:56:01.513Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01N3EwWoMBk7823F8Lc5Wumk`</summary>

```json
{
  "pattern": "paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12ec0477-80c0-473f-bf8c-1445fc0e4d67",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFftxyP2rd9wCojxV3hg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ef6f8a9-a15e-4f4f-8da3-f8a821cf55ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDHuqiBf46xiwZps2PEW6i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3048,
      "cache_read_input_tokens": 51765,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3048
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 51765,
          "cache_creation_input_tokens": 3048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3048,
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

_source line 36 · 2026-05-21T11:56:01.536Z_

<details><summary>↩ Tool result · `toolu_01N3EwWoMBk7823F8Lc5Wumk`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ef6f8a9-a15e-4f4f-8da3-f8a821cf55ca",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "d36244f8-1315-49ae-a4b4-3a622a2540bb",
  "sourceToolAssistantUUID": "6ef6f8a9-a15e-4f4f-8da3-f8a821cf55ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T11:56:03.857Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SUuEmhP9pJHvjETa5FLpgx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d36244f8-1315-49ae-a4b4-3a622a2540bb",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfuEK7Qcbs3XKESMAWz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "feb58992-c47b-40c0-aab7-314a5fa36052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHxJciaiTFrLUGaXPkATvc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 136,
      "cache_read_input_tokens": 54813,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 136
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 54813,
          "cache_creation_input_tokens": 136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 136,
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

_source line 38 · 2026-05-21T11:56:03.863Z_

<details><summary>↩ Tool result · `toolu_01SUuEmhP9pJHvjETa5FLpgx`</summary>

```text
1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{balloccu2024leak,
6	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
7	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
8	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
9	  year      = {2024},
10	  doi       = {10.18653/v1/2024.eacl-long.5},
11	  url       = {https://arxiv.org/abs/2402.03927}
12	}
13	
14	@inproceedings{dekoninck2024constat,
15	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
16	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  year      = {2024},
19	  url       = {https://arxiv.org/abs/2405.16281}
20	}
21	
22	@inproceedings{golchin2024timetravel,
23	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
24	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
25	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2308.08493}
28	}
29	
30	@inproceedings{li2024contamination,
31	  title     = {An Open-Source Data Contamination Report for Large Language Models},
32	  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
34	  year      = {2024},
35	  doi       = {10.18653/v1/2024.findings-emnlp.30},
36	  url       = {https://aclanthology.org/2024.findings-emnlp.30/}
37	}
38	
39	@misc{liang2026dvd,
40	  title         = {{DVD}: Detection via Variance of Generation Distribution for Variant Contamination},
41	  author        = {Liang, Rongzhen},
42	  year          = {2026},
43	  eprint        = {2601.04895},
44	  archivePrefix = {arXiv},
45	  primaryClass  = {cs.CL},
46	  url           = {https://arxiv.org/abs/2601.04895}
47	}
48	
49	@inproceedings{shi2024mink,
50	  title     = {Detecting Pretraining Data from Large Language Models},
51	  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
52	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
53	  year      = {2024},
54	  url       = {https://arxiv.org/abs/2310.16789}
55	}
56	
57	@inproceedings{tao2026selfcritique,
58	  title     = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},
59	  author    = {Tao, Yixin},
60	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
61	  year      = {2026},
62	  url       = {https://arxiv.org/abs/2510.09259}
63	}
64	
65	@inproceedings{wang2026fragility,
66	  title     = {On The Fragility of Benchmark Contamination Detection in Reasoning Models},
67	  author    = {Wang, Haonan and Li, Haoyang and Ko, Boeun and Zhang, Hongyang},
68	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
69	  year      = {2026},
70	  url       = {https://arxiv.org/abs/2510.02386}
71	}
72	
73	@misc{zhang2024gsm1k,
74	  title         = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},
75	  author        = {Zhang, Hugh},
76	  year          = {2024},
77	  eprint        = {2405.00332},
78	  archivePrefix = {arXiv},
79	  primaryClass  = {cs.CL},
80	  url           = {https://arxiv.org/abs/2405.00332}
81	}
82	
83	@misc{zhang2024minkpp,
84	  title         = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
85	  author        = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},
86	  year          = {2024},
87	  eprint        = {2404.02936},
88	  archivePrefix = {arXiv},
89	  primaryClass  = {cs.CL},
90	  url           = {https://arxiv.org/abs/2404.02936}
91	}
92	
93	% ============================================================
94	% IRT Methodology & Equating
95	% ============================================================
96	
97	@inproceedings{rodriguez2021evaluation,
98	  title     = {Evaluation Examples Are Not Equally Informative: How Should That Change {NLP} Leaderboards?},
99	  author    = {Rodriguez, Pedro and Barrow, Joe and Hoyle, Alexander Miserlis and Lalor, John P. and Jia, Robin and Boyd-Graber, Jordan},
100	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
101	  year      = {2021},
102	  pages     = {4486--4503}
103	}
104	
105	@article{donoghue1993mh,
106	  title   = {An Empirical Examination of the {Mantel-Haenszel} Statistic for the Study of Differential Item Functioning},
107	  author  = {Donoghue, John R. and Allen, Nancy L.},
108	  journal = {Applied Measurement in Education},
109	  volume  = {6},
110	  number  = {2},
111	  pages   = {163--179},
112	  year    = {1993}
113	}
114	
115	@misc{hardy2026scalability,
116	  title         = {Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients},
117	  author        = {Hardy, Matthew and Gilbert, Juan and Domingue, Benjamin},
118	  year          = {2026},
119	  eprint        = {2603.24999},
120	  archivePrefix = {arXiv},
121	  primaryClass  = {cs.CL},
122	  url           = {https://arxiv.org/abs/2603.24999}
123	}
124	
125	@article{kim2019fpc,
126	  title   = {Application of {IRT} Fixed Parameter Calibration to Multiple-Group Test Data},
127	  author  = {Kim, Seonghoon and Kolen, Michael},
128	  journal = {Applied Measurement in Education},
129	  year    = {2019},
130	  doi     = {10.1080/08957347.2019.1660344},
131	  url     = {https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344}
132	}
133	
134	@inproceedings{lalor2019irt,
135	  title     = {Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds},
136	  author    = {Lalor, John and Wu, Hao and Yu, Hong},
137	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
138	  year      = {2019},
139	  doi       = {10.18653/v1/D19-1434},
140	  url       = {https://aclanthology.org/D19-1434/}
141	}
142	
143	@inproceedings{vania2021irt,
144	  title     = {Comparing Test Sets with Item Response Theory},
145	  author    = {Vania, Clara and Htut, Phu Mon and Huang, William and Mungra, Dhara and Pang, Richard Yuanzhe and Phang, Jason and Liu, Haokun and Cho, Kyunghyun and Bowman, Samuel R.},
146	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
147	  year      = {2021},
148	  doi       = {10.18653/v1/2021.acl-long.92},
149	  url       = {https://aclanthology.org/2021.acl-long.92/}
150	}
151	
152	@misc{li2025atlas,
153	  title         = {{ATLAS}: Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
154	  author        = {Li, Peiyang and Tang, Xiaobo and Chen, Sai and Cheng, Ying and Metoyer, Ronald and Hua, Tianyi and Chawla, Nitesh V.},
155	  year          = {2025},
156	  eprint        = {2511.04689},
157	  archivePrefix = {arXiv},
158	  primaryClass  = {cs.CL},
159	  url           = {https://arxiv.org/abs/2511.04689}
160	}
161	
162	@misc{chen2025irtnet,
163	  title         = {Learning Compact Representations of {LLM} Abilities via Item Response Theory},
164	  author        = {Chen, Jiayi and Wang, Chao and Zhang, Guoqiang and Ye, Peijin and Bai, Lei and Hu, Wenjun and Qu, Yongchao and Hu, Songlin},
165	  year          = {2025},
166	  eprint        = {2510.00844},
167	  archivePrefix = {arXiv},
168	  primaryClass  = {cs.CL},
169	  url           = {https://arxiv.org/abs/2510.00844}
170	}
171	
172	@misc{choi2026llmjudgeirt,
173	  title         = {Diagnosing the Reliability of {LLM}-as-a-Judge via Item Response Theory},
174	  author        = {Choi, Jiseong and Park, Seonho and Cho, Changwon and Park, Hojun and Kim, Bumsoo},
175	  year          = {2026},
176	  eprint        = {2602.00521},
177	  archivePrefix = {arXiv},
178	  primaryClass  = {cs.CL},
179	  url           = {https://arxiv.org/abs/2602.00521}
180	}
181	
182	@misc{habba2026growingpains,
183	  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},
184	  author        = {Habba, Eitam and Itzhak, Ido and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},
185	  year          = {2026},
186	  eprint        = {2604.12843},
187	  archivePrefix = {arXiv},
188	  primaryClass  = {cs.CL},
189	  url           = {https://arxiv.org/abs/2604.12843}
190	}
191	
192	@inproceedings{zhou2026psnirt,
193	  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
194	  author    = {Zhou, Hao and Huang, Heng and Zhao, Zhenheng and Han, Lin and Wang, Haoyu and Chen, Ke and Yang, Min and Bao, Weidong and Dong, Ji and Xu, Bo and Zhu, Changshui and Cao, Huijun and Zhao, Tiejun},
195	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
196	  year      = {2026},
197	  url       = {https://arxiv.org/abs/2505.15055}
198	}
199	
200	% ============================================================
201	% Dynamic Benchmark Design
202	% ============================================================
203	
204	@inproceedings{white2025livebench,
205	  title     = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
206	  author    = {White, Colin},
207	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
208	  year      = {2025},
209	  doi       = {10.48550/arXiv.2406.19314},
210	  url       = {https://arxiv.org/abs/2406.19314}
211	}
212	
213	@misc{kipnis2024metabench,
214	  title         = {metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},
215	  author        = {Kipnis, Alon and Voudouris, Konstantinos and Schulze Buschoff, Luca Maria and Schulz, Eric},
216	  year          = {2024},
217	  eprint        = {2407.12844},
218	  archivePrefix = {arXiv},
219	  primaryClass  = {cs.CL},
220	  url           = {https://arxiv.org/abs/2407.12844}
221	}
222	
223	@inproceedings{hendrycks2021mmlu,
224	  title     = {Measuring Massive Multitask Language Understanding},
225	  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
226	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
227	  year      = {2021},
228	  url       = {https://arxiv.org/abs/2009.03300}
229	}
230	
231	@article{liang2023helm,
232	  title   = {Holistic Evaluation of Language Models},
233	  author  = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya},
234	  journal = {Transactions on Machine Learning Research},
235	  year    = {2023},
236	  doi     = {10.1111/nyas.15007},
237	  url     = {https://arxiv.org/abs/2211.09110}
238	}
239	
240	@inproceedings{chiang2024chatbot,
241	  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},
242	  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},
243	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
244	  year      = {2024},
245	  doi       = {10.48550/arXiv.2403.04132},
246	  url       = {https://arxiv.org/abs/2403.04132}
247	}
248	
249	@misc{mialon2023gaia,
250	  title         = {{GAIA}: a benchmark for General {AI} Assistants},
251	  author        = {Mialon, Grégoire and Fourrier, Clémentine and Swift, Craig and Wolf, Thomas and LeCun, Yann and Scialom, Thomas},
252	  year          = {2023},
253	  eprint        = {2311.12983},
254	  archivePrefix = {arXiv},
255	  primaryClass  = {cs.CL},
256	  url           = {https://arxiv.org/abs/2311.12983}
257	}
258	
259	@inproceedings{li2024latesteval,
260	  title     = {{LatestEval}: Addressing Data Contamination in Language Model Evaluation through Dynamic and Time-Sensitive Test Construction},
261	  author    = {Li, Yucheng and Guerin, Frank and Lin, Chenghua},
262	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
263	  year      = {2024},
264	  doi       = {10.48550/arXiv.2312.12343},
265	  url       = {https://arxiv.org/abs/2312.12343}
266	}
267	
268	@inproceedings{kiela2021dynabench,
269	  title     = {{Dynabench}: Rethinking Benchmarking in {NLP}},
270	  author    = {Kiela, Douwe and Bartolo, Max and Nie, Yixin and Kaushik, Divyansh and Geiger, Atticus and Wu, Zhengxuan and Vidgen, Bertie and Prasad, Grusha and Singh, Amanpreet and Ringshia, Pratik and Ma, Zhiyi and Thrush, Tristan and Riedel, Sebastian and Talat, Zeerak and Stenetorp, Pontus and Jia, Robin},
271	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
272	  year      = {2021},
273	  doi       = {10.18653/v1/2021.naacl-main.324},
274	  url       = {https://arxiv.org/abs/2104.14337}
275	}
276	
277	% ============================================================
278	% DIF Statistical Methods
279	% ============================================================
280	
281	@article{belzak2020smallsample,
282	  title   = {Testing Differential Item Functioning in Small Samples},
283	  author  = {Belzak, William},
284	  journal = {Multivariate Behavioral Research},
285	  year    = {2020},
286	  doi     = {10.1080/00273171.2019.1671162},
287	  url     = {https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162}
288	}
289	
290	@incollection{holland1988mh,
291	  title     = {Differential Item Functioning and the {Mantel-Haenszel} Procedure},
292	  author    = {Holland, Paul W. and Thayer, Dorothy T.},
293	  booktitle = {Test Validity},
294	  editor    = {Wainer, Howard and Braun, Henry I.},
295	  publisher = {Lawrence Erlbaum Associates},
296	  year      = {1988},
297	  doi       = {10.1002/j.2330-8516.1986.tb00186.x},
298	  url       = {https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x}
299	}
300	
301	@article{shealy1993sibtest,
302	  title   = {A Model-Based Standardization Approach that Separates True Bias/{DIF} from Group Ability Differences and Detects Test Bias/{DTF} as Well as Item Bias/{DIF}},
303	  author  = {Shealy, Robin and Stout, William},
304	  journal = {Psychometrika},
305	  year    = {1993},
306	  doi     = {10.1007/BF02294572},
307	  url     = {https://link.springer.com/article/10.1007/BF02294572}
308	}
309	
310	@article{clauser1998dif,
311	  title   = {Using Statistical Procedures to Identify Differentially Functioning Test Items},
312	  author  = {Clauser, Brian E. and Mazor, Kathleen M.},
313	  journal = {Educational Measurement: Issues and Practice},
314	  year    = {1998},
315	  doi     = {10.1111/j.1745-3992.1998.tb00619.x},
316	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x}
317	}
318	
319	@book{zumbo1999handbook,
320	  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},
321	  author    = {Zumbo, Bruno D.},
322	  year      = {1999},
323	  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defense},
324	  address   = {Ottawa},
325	  url       = {https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf}
326	}
327	
328	@article{meredith1993invariance,
329	  title   = {Measurement Invariance, Factor Analysis and Factorial Invariance},
330	  author  = {Meredith, William},
331	  journal = {Psychometrika},
332	  year    = {1993},
333	  doi     = {10.1007/BF02294825},
334	  url     = {https://link.springer.com/article/10.1007/BF02294825}
335	}
336	
337	@article{vandenberg2000invariance,
338	  title   = {A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research},
339	  author  = {Vandenberg, Robert J. and Lance, Charles E.},
340	  journal = {Organizational Research Methods},
341	  year    = {2000},
342	  doi     = {10.1177/109442810031002},
343	  url     = {https://journals.sagepub.com/doi/10.1177/109442810031002}
344	}
345	
346	@article{swaminathan1990logistic,
347	  title   = {Detecting Differential Item Functioning Using Logistic Regression Procedures},
348	  author  = {Swaminathan, Hariharan and Rogers, H. Jane},
349	  journal = {Journal of Educational Measurement},
350	  year    = {1990},
351	  doi     = {10.1111/j.1745-3984.1990.tb00754.x},
352	  url     = {https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x}
353	}
354	
355	@article{teresi2007dif,
356	  title   = {Differential Item Functioning and Health Assessment},
357	  author  = {Teresi, Jeanne A. and Fleishman, John A.},
358	  journal = {Quality of Life Research},
359	  year    = {2007},
360	  doi     = {10.1007/s11136-007-9184-6},
361	  url     = {https://link.springer.com/article/10.1007/s11136-007-9184-6}
362	}
363	
364	@book{lord1980irt,
365	  title     = {Applications of Item Response Theory to Practical Testing Problems},
366	  author    = {Lord, Frederic M.},
367	  year      = {1980},
368	  publisher = {Lawrence Erlbaum Associates},
369	  address   = {Hillsdale, NJ}
370	}
371	
372	@article{raju1988area,
373	  title   = {The Area between Two Item Characteristic Curves},
374	  author  = {Raju, Nambury S.},
375	  journal = {Psychometrika},
376	  year    = {1988},
377	  doi     = {10.1007/BF02294403},
378	  url     = {https://link.springer.com/article/10.1007/BF02294403}
379	}
380	
381	@article{muthen1985mimic,
382	  title   = {A Method for Studying the Homogeneity of Test Items with Respect to Other Relevant Variables},
383	  author  = {Muth{\'e}n, Bengt},
384	  journal = {Journal of Educational Statistics},
385	  year    = {1985},
386	  doi     = {10.2307/1164966}
387	}
388	
389	@article{woods2009mimic,
390	  title   = {Empirical Selection of Anchors for Tests of Differential Item Functioning},
391	  author  = {Woods, Carol M.},
392	  journal = {Applied Psychological Measurement},
393	  year    = {2009},
394	  doi     = {10.1177/0146621609331279}
395	}
396	
397	% ============================================================
398	% LLM Evaluation Methodology
399	% ============================================================
400	
401	@article{burnell2023rethink,
402	  title   = {Rethink reporting of evaluation results in {AI}},
403	  author  = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Cheke, Lucy G. and Sohl-Dickstein, Jascha and Mitchell, Melanie and Kiela, Douwe and Shanahan, Murray and Voorhees, Ellen M. and Cohn, Anthony G. and Leibo, Joel Z. and Hernandez-Orallo, Jose},
404	  journal = {Science},
405	  year    = {2023},
406	  doi     = {10.1126/science.adf6369},
407	  url     = {https://www.science.org/doi/10.1126/science.adf6369}
408	}
409	
410	@article{chang2024survey,
411	  title   = {A Survey on Evaluation of Large Language Models},
412	  author  = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Zhu, Kaijie and Chen, Hao and Yang, Linyi and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},
413	  journal = {ACM Transactions on Intelligent Systems and Technology},
414	  year    = {2024},
415	  doi     = {10.1145/3641289},
416	  url     = {https://dl.acm.org/doi/full/10.1145/3641289}
417	}
418	
419	@inproceedings{maiapolo2024tinybenchmarks,
420	  title     = {{tinyBenchmarks}: evaluating {LLMs} with fewer examples},
421	  author    = {Maia Polo, Felipe and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
422	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
423	  year      = {2024},
424	  url       = {https://proceedings.mlr.press/v235/maia-polo24a.html}
425	}
426	
427	@inproceedings{wang2024mmlupro,
428	  title     = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},
429	  author    = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Xue, Xiang and Chen, Wenhu},
430	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
431	  year      = {2024},
432	  url       = {https://arxiv.org/abs/2406.01574}
433	}
434	
435	@article{ott2022benchmark,
436	  title   = {Mapping global dynamics of benchmark creation and saturation in artificial intelligence},
437	  author  = {Ott, Simon and Barbosa-Silva, Adriano and Blagec, Kathrin and Brauner, Jan and Samwald, Matthias},
438	  journal = {Nature Communications},
439	  year    = {2022},
440	  doi     = {10.1038/s41467-022-34591-0},
441	  url     = {https://www.nature.com/articles/s41467-022-34591-0}
442	}
443	
444	@article{nandakumar1993dif,
445	  author  = {Ratna Nandakumar},
446	  title   = {Simultaneous {DIF} amplification and cancellation: {Shealy}-{Stout}'s test for {DIF}},
447	  journal = {Journal of Educational Measurement},
448	  year    = {1993},
449	  volume  = {30},
450	  number  = {4},
451	  pages   = {293--311}
452	}
453	
454	@inproceedings{carlini2022quantifying,
455	  author    = {Nicholas Carlini and Daphne Ippolito and Matthew Jagielski and Katherine Lee and Florian Tram{\`e}r and Chiyuan Zhang},
456	  title     = {Quantifying Memorization Across Neural Language Models},
457	  booktitle = {International Conference on Learning Representations (ICLR)},
458	  year      = {2023},
459	  url       = {https://arxiv.org/abs/2202.07646}
460	}
461	
462	@inproceedings{tirumala2022memorization,
463	  author    = {Kushal Tirumala and Aram Markosyan and Luke Zettlemoyer and Armen Aghajanyan},
464	  title     = {Memorization Without Overfitting: Analyzing the Training Dynamics of Large Language Models},
465	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
466	  year      = {2022},
467	  url       = {https://arxiv.org/abs/2205.10770}
468	}
469	
470	% ============================================================
471	% Additional Benchmarks
472	% ============================================================
473	
474	@inproceedings{sakaguchi2021winogrande,
475	  title     = {{WinoGrande}: An Adversarial {Winograd} Schema Challenge at Scale},
476	  author    = {Sakaguchi, Keisuke and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
477	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
478	  volume    = {34},
479	  number    = {05},
480	  pages     = {8732--8740},
481	  year      = {2020}
482	}
483	
484	@inproceedings{lin2022truthfulqa,
485	  title     = {{TruthfulQA}: Measuring How Models Mimic Human Falsehoods},
486	  author    = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},
487	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
488	  year      = {2022},
489	  pages     = {3214--3252}
490	}
491	
492	@inproceedings{zellers2019hellaswag,
493	  title     = {{HellaSwag}: Can a Machine Really Finish Your Sentence?},
494	  author    = {Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farzaneh, Ali and Choi, Yejin},
495	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
496	  year      = {2019},
497	  pages     = {4791--4800}
498	}
499	
500	@article{clark2018arc,
501	  title   = {Think you have Solved Question Answering? Try {ARC}, the {AI2} Reasoning Challenge},
502	  author  = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
503	  journal = {arXiv preprint arXiv:1803.05457},
504	  year    = {2018}
505	}
506	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feb58992-c47b-40c0-aab7-314a5fa36052",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "d448da32-6b45-49c2-84b4-c16a510dab92",
  "sourceToolAssistantUUID": "feb58992-c47b-40c0-aab7-314a5fa36052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-21T11:56:07.252Z_

Now let me check if there are figures to understand the visual presentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d448da32-6b45-49c2-84b4-c16a510dab92",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfuQKco7FTU2pNMFfNY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edee2fc6-97bb-4484-aaf4-8146a8ce0fc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163Tj2tPA6yFYaugtR5q7kb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9285,
      "cache_read_input_tokens": 54949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9285,
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

_source line 40 · 2026-05-21T11:56:09.722Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CbjtrRZHo1uB71opixuuSa`</summary>

```json
{
  "pattern": "figures/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edee2fc6-97bb-4484-aaf4-8146a8ce0fc0",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfuQKco7FTU2pNMFfNY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb63c467-e90f-4b45-b77d-a7983a8f6980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163Tj2tPA6yFYaugtR5q7kb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9285,
      "cache_read_input_tokens": 54949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9285,
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

_source line 41 · 2026-05-21T11:56:09.744Z_

<details><summary>↩ Tool result · `toolu_01CbjtrRZHo1uB71opixuuSa`</summary>

```text
figures/paper/fig_2_dose_response.pdf
figures/paper/fig_3_within_subject_matching.pdf
figures/paper/fig_A1_subject_heatmap.pdf
figures/paper/fig_A2_q3_distribution.pdf
figures/paper/fig_4_downstream_impact.pdf
figures/paper/fig_1_global_vs_differential.pdf
figures/paper/fig_5_gsm1k_dif_correlation.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb63c467-e90f-4b45-b77d-a7983a8f6980",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "6480df92-8de1-47f2-af7a-1c38e0fac99e",
  "sourceToolAssistantUUID": "fb63c467-e90f-4b45-b77d-a7983a8f6980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T11:56:10.133Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Qi7Hq95cCheT3zx5wejkJD`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6480df92-8de1-47f2-af7a-1c38e0fac99e",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfuQKco7FTU2pNMFfNY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52c26e03-8ad9-439f-9210-424181e700f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163Tj2tPA6yFYaugtR5q7kb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9285,
      "cache_read_input_tokens": 54949,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9285
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 54949,
          "cache_creation_input_tokens": 9285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9285,
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

_source line 43 · 2026-05-21T11:56:10.150Z_

<details><summary>↩ Tool result · `toolu_01Qi7Hq95cCheT3zx5wejkJD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\\n\\n## 近期结论\\n- **plan_028_multi_bench_dif** (success): Temporal DIF (2023 vs 2024 cohort) 在 METABENCH 的 ARC, HellaSwag, WinoGrande, TruthfulQA 上均展现与 MMLU 类似的显著 C% (>15%)，证明 temporal DIF 现象跨 benchmark 泛化，不是 MMLU 特有的 artifact。所有 benchmark 的 random-split control C% < 1%。 ← 基于 plan_001_real_data_dif_mmlu\\n  [plan_028_multi_bench_summary](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/data/multi_bench_summary.csv) | [plan_028_multi_bench_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md) | [plan_028_script](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/intermediate/plan_028_multi_bench_dif.py)\\n- **plan_030_odds_ratio** (success): Logistic regression 的 odds ratio + CI 量化 accuracy change 与 DIF C flag 的关联强度。Item-level accuracy change (Model 3) 比 domain-level delta (Model 1) 提供更精确的预测。控制 item properties (difficulty + discrimination) 后，accuracy change 的 OR 反转（Simpson's paradox），说明 DIF C 主要由 item 固有属性驱动而非 accuracy shift。 ← 基于 plan_001_real_data_dif_mmlu\\n  [plan_030_odds_ratio_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_030_odds_ratio/report/odds_ratio_report.md) | [plan_030_odds_ratio_script](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_030_odds_ratio/intermediate/plan_030_odds_ratio.py)\\n- **plan_027_temporal_overlap** (success): Temporal cohort ability gap 很小 (d=-0.17)，ability-matched C% 接近 full 31.3%，确认 temporal DIF 非 ability confound 产物 ← 基于 plan_001_real_data_dif_mmlu\\n\\n## 趋势\\n成功 8 / 负向 6 / 失败 0 / 共 14\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2024, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52c26e03-8ad9-439f-9210-424181e700f0",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "c2e70f38-1ff3-443b-91a7-2092a5d4b2fb",
  "sourceToolAssistantUUID": "52c26e03-8ad9-439f-9210-424181e700f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-21T11:56:13.048Z_

I now have a thorough understanding of the paper. Let me also check the compiled PDF page count to verify the 8-page limit compliance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2e70f38-1ff3-443b-91a7-2092a5d4b2fb",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfusFrxxqLKAb8yt9RV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54a27914-5311-499d-b5ee-11946ef213b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLgKD9viY3ZnZbS6QsooRA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 64234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1479,
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

_source line 45 · 2026-05-21T11:56:14.056Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jg6qo6Dh8Ucwpm1wFBoU6w`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', 'paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"pdfinfo not available\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54a27914-5311-499d-b5ee-11946ef213b7",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfusFrxxqLKAb8yt9RV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba16360a-86bb-4e81-8cc7-0cc2b770b043",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLgKD9viY3ZnZbS6QsooRA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 64234,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1479
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 64234,
          "cache_creation_input_tokens": 1479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1479,
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

_source line 46 · 2026-05-21T11:56:14.277Z_

<details><summary>↩ Tool result · `toolu_01Jg6qo6Dh8Ucwpm1wFBoU6w`</summary>

```text
Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Thu May 21 11:03:57 2026 UTC
ModDate:         Thu May 21 11:03:57 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           13
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       561808 bytes
Optimized:       no
PDF version:     1.7
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba16360a-86bb-4e81-8cc7-0cc2b770b043",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "30d0e600-cee8-43f1-bedb-f1a2cbb2d635",
  "sourceToolAssistantUUID": "ba16360a-86bb-4e81-8cc7-0cc2b770b043",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-21T11:56:17.142Z_

13 pages total (8 main + limitations + references + appendix). Let me count references in the bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30d0e600-cee8-43f1-bedb-f1a2cbb2d635",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfvAf8CoWmLZTCzfwyg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb98a9a8-f542-4fc2-9bc5-1d924d3a50f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nw3NehpHJKcK8nh9Zv8b5t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 334,
      "cache_read_input_tokens": 65713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 334,
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

_source line 48 · 2026-05-21T11:56:18.247Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JfrxunbRVaWdjx73mLFBur`</summary>

```json
{
  "command": "grep -c '@' /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib | head -1 && grep '^@' /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib | wc -l"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb98a9a8-f542-4fc2-9bc5-1d924d3a50f5",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfvAf8CoWmLZTCzfwyg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "524c95d8-7bd5-4ca1-a60f-cb21cbebf601",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nw3NehpHJKcK8nh9Zv8b5t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 334,
      "cache_read_input_tokens": 65713,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 334
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 65713,
          "cache_creation_input_tokens": 334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 334,
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

_source line 49 · 2026-05-21T11:56:18.326Z_

<details><summary>↩ Tool result · `toolu_01JfrxunbRVaWdjx73mLFBur`</summary>

```text
54
54
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "524c95d8-7bd5-4ca1-a60f-cb21cbebf601",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "169518f4-1233-4806-9e7d-2607f809a2fc",
  "sourceToolAssistantUUID": "524c95d8-7bd5-4ca1-a60f-cb21cbebf601",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T11:56:21.305Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013mxZYmLterfTbnNtgXQEi5`</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
  "output_mode": "content",
  "head_limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "169518f4-1233-4806-9e7d-2607f809a2fc",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfvTxBF4qcUwCGGp4ns",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3779fa09-baf0-40ea-b77f-e63b20e06456",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129M8FttqSRtTsrQnSLZeUD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 192,
      "cache_read_input_tokens": 66047,
      "output_tokens": 143,
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
          "output_tokens": 143,
          "cache_read_input_tokens": 66047,
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

_source line 51 · 2026-05-21T11:56:21.326Z_

<details><summary>↩ Tool result · `toolu_013mxZYmLterfTbnNtgXQEi5`</summary>

```text
paper/sections/related_work.tex:5:[Omitted long matching line]
paper/sections/related_work.tex:8:[Omitted long matching line]
paper/sections/related_work.tex:11:[Omitted long matching line]
paper/sections/related_work.tex:14:[Omitted long matching line]
paper/sections/experiments.tex:4:We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
paper/sections/experiments.tex:16:[Omitted long matching line]
paper/sections/experiments.tex:42:[Omitted long matching line]
paper/sections/experiments.tex:69:[Omitted long matching line]
paper/sections/method.tex:9:[Omitted long matching line]
paper/sections/method.tex:16:The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$) and computing a common odds ratio across strata. We use $K = 5$ equiprobable strata (quintile-based binning) following ETS recommended practice for large-scale assessments~\citep{donoghue1993mh,clauser1998dif}. Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
paper/sections/method.tex:46:[Omitted long matching line]
paper/sections/limitations.tex:4:[Omitted long matching line]
paper/sections/introduction.tex:4:[Omitted long matching line]
paper/sections/introduction.tex:6:[Omitted long matching line]
paper/sections/introduction.tex:15:[Omitted long matching line]
paper/sections/introduction.tex:19:[Omitted long matching line]
paper/sections/introduction.tex:24:\item \textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\citep{li2024contamination} do not provide appropriate ground truth for item-level differential detectors. Direct empirical comparison on 9,229 items shows near-independence (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), exposing a validation methodology gap in the contamination detection literature (\Cref{sec:groundtruth}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3779fa09-baf0-40ea-b77f-e63b20e06456",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a3c9d662c10f2e121",
  "type": "user",
  "uuid": "c12c951f-e067-4af5-ab11-d7184ef6734d",
  "sourceToolAssistantUUID": "3779fa09-baf0-40ea-b77f-e63b20e06456",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-21T11:57:56.999Z_

I have now read all sections of the paper, the bibliography, literature map, paper framing document, and report. I have sufficient information to write a thorough review.

---

## Review: "Psychometric DIF Analysis Reveals Systematic Temporal Instability in LLM Benchmark Items at Scale"

**Reviewer 2 — Focus: Novelty and Related Work**

---

### 1. Summary

This paper applies the Mantel-Haenszel Differential Item Functioning (MH-DIF) procedure from educational psychometrics to LLM benchmark evaluation, analyzing 5,227 models across 12,508 MMLU items from the METABENCH dataset. The central finding is that 31% of MMLU items exhibit large temporal DIF (ETS Category C) between 2023 and 2024 model cohorts, generalizing across six benchmarks (17.9--31.3%). The paper frames this as a diagnostic finding ("instability does not equal invalidity"), critiques existing web-overlap ground truth labels as unsuitable for differential detectors, and proposes a semi-synthetic validation framework with cross-subject matching.

---

### 2. Strengths

- **Scale and thoroughness of empirical analysis.** The analysis spans 5,227 models x 12,508 items on MMLU alone, with replication across all six METABENCH benchmarks. The sheer scale of DIF analysis on LLM populations is genuinely unprecedented, and the paper exploits this scale to run numerous robustness checks (threshold sensitivity, BH correction, architecture homogeneity, graduated de-duplication, ability matching, random-split controls). This is among the most thorough psychometric analyses of LLM benchmarks I have seen.

- **Well-calibrated contribution claims.** The paper is refreshingly honest about what is and is not novel. The authors explicitly state that MH-DIF is standard psychometrics and that their contributions are "empirical and methodological, not algorithmic." This honest positioning is appropriate and prevents overclaiming. The four contributions are clearly enumerated and well-scoped.

- **Simpson's paradox analysis is compelling.** The odds ratio regression showing that domain accuracy improvement positively predicts DIF at the aggregate level (OR = 1.55) but reverses after controlling for item properties (OR = 0.73) is a sophisticated and convincing analysis. This effectively addresses the most natural objection ("31% just means models got better") with a clean statistical argument.

- **Cross-subject matching is a genuine methodological contribution.** The observation that within-subject matching contaminates the conditioning variable during semi-synthetic injection, and the solution of cross-subject matching achieving exact zero FPR, is a subtle and practically useful insight. This is portable to other multi-domain benchmarks and represents a concrete methodological advance.

- **Complementary positioning with Growing Pains.** The paper explicitly frames its relationship to Habba et al. (2026): "Growing Pains assumes anchor item stability; our DIF analysis diagnoses which items violate this assumption." This is a clear and compelling differentiation. The two papers address different aspects of the same problem.

- **Related Work is comprehensive and well-structured.** Four paragraphs covering contamination detection, IRT in LLM evaluation, DIF methodology, and benchmark design. The bibliography is substantial (54 entries), with appropriate coverage of both the NLP and psychometrics literatures. The inclusion of foundational psychometric references (Holland & Thayer 1988, Clauser & Mazor 1998, Meredith 1993, etc.) alongside recent NLP work is appropriate for a paper bridging these fields.

- **The "instability does not equal invalidity" framing is well-deployed.** Introducing this upfront in the Introduction, rather than burying it in Discussion, prevents the reader from misinterpreting the 31% figure as an attack on MMLU. The rho = 0.997 ranking stability result is a necessary complement to the headline finding.

- **Cross-benchmark generalization strengthens the story.** The extension from MMLU alone to six benchmarks with a coherent pattern (knowledge/reasoning > procedural) elevates this from a single-benchmark observation to a more general finding about LLM evaluation.

---

### 3. Weaknesses

- **(Major) The ground truth meta-critique (Contribution 2) is more observation than contribution.** The paper claims as a contribution that web-overlap labels measure "global exposure, not differential functioning." While empirically validated (enrichment = 0.964), this is arguably a straightforward conceptual observation once you frame the problem in DIF terms. The distinction between "an item exists on the web" and "an item functions differently across cohorts" is almost definitional once you adopt the DIF framework. The empirical confirmation that these are near-independent is useful but not surprising. Positioning this as one of four numbered contributions inflates its significance. Severity: major for framing, minor for substance (the analysis itself is fine; the issue is the weight placed on it).

- **(Major) Missing engagement with the "what does DIF mean for LLMs?" question.** The paper applies a human-testing framework to machine examinees without deeply engaging with whether the assumptions transfer. In educational testing, DIF detects unfairness: items that disadvantage demographic subgroups after controlling for ability. The ethical and theoretical motivation (fairness, equal opportunity) that gives DIF its significance in education does not straightforwardly apply to LLMs. What does "differential functioning across model cohorts" actually tell us, beyond "things changed"? The paper gestures at this ("diagnostic lens") but never confronts whether temporal DIF in LLM benchmarks might simply reflect legitimate capability change, training data evolution, or optimization pressure -- phenomena that have no analog in the human testing context where DIF was developed. The Limitations section mentions this but the Discussion should engage with it more substantively. Severity: major.

- **(Major) Causal ambiguity undermines interpretive claims.** The paper finds that 31% of items "function differently" but cannot determine whether this reflects contamination, capability change, training methodology shifts, or some combination. The Limitations acknowledge this, but the Introduction and Discussion still make interpretive claims that lean toward contamination-adjacent language ("differential contamination," "exploitation rate," etc.) while the evidence cannot distinguish between these explanations. The semi-synthetic framework only shows DIF *can* detect injected contamination, not that the observed temporal DIF *is* contamination. This weakens Contribution 4's interpretive framing. Severity: major.

- **(Minor) The difficulty-direction interaction (rho = -0.597), while interesting, has a simpler explanation.** Hard items that 2024 models now get right and easy items that 2024 models now get wrong could simply reflect regression to the mean combined with genuine capability improvement. Hard items have more room for improvement; easy items are more susceptible to format/prompt sensitivity changes across generations. The paper presents this as evidence that "DIF captures genuine capability change," but the finding is equally consistent with statistical artifacts of comparing populations with different mean abilities on items at different difficulty levels. The matched-ability analysis reduces d from -0.17 to -0.01, but the difficulty-direction interaction analysis is not reported under the matched condition. Severity: minor.

- **(Minor) Some missing related work in psychometric applications to NLP/ML.** The paper does not cite Sedoc & Ungar (2020, "Item Response Theory for Efficient Human Evaluation of Chatbots"), which applies IRT to chatbot evaluation with explicit discussion of DIF-like concepts. More importantly, there is no engagement with Bao et al. (2025, arXiv:2501.xxxxx) on measurement invariance testing for LLM benchmarks, or with the broader psychometric AI literature (e.g., Hernandez-Orallo 2017, "The Measure of All Minds"). The paper cites Burnell et al. (2023) and Chang et al. (2024) as surveys but does not discuss Liao et al. (2024, "Are We Evaluating LLMs Correctly?") which raises closely related questions about temporal validity of benchmarks. Severity: minor, but addressing these would strengthen the positioning.

- **(Minor) The DIF audit protocol (Section 5.4) is underspecified.** Three bullet points recommending "quarterly MH-DIF audits," "C% > 20% triggers item review," and "graduated responses: flag-and-annotate, item rotation, or weighted scoring" is too brief to count as a genuine methodological contribution. These are reasonable recommendations, but they lack the specificity needed for actual implementation (e.g., how to handle items that flip between C and A across audits, how to weight items in a scored version, what "item rotation" means concretely for a static benchmark). This is listed as part of Contribution (d) but reads more like future work. Severity: minor.

- **(Minor) 54 bibliography entries for 8 pages of main text suggests over-citation.** Many references in the Related Work are cited once and never engaged with again. For instance, Muthén (1985), Woods (2009), Raju (1988), Lord (1980), Teresi (2007), Vandenberg & Lance (2000) are cited to establish DIF methodology comprehensiveness but are not actually used in the analysis. The Related Work paragraph on DIF methodology reads more like a literature survey than a focused positioning section. Severity: minor, but trimming would improve readability.

- **(Minor) The paper does not discuss whether the 31% figure is sensitive to the temporal cutoff choice.** The cohorts are defined as "2023 vs. 2024," but models released in December 2023 vs. January 2024 may share nearly identical training data. A sensitivity analysis varying the cutoff date (e.g., 2023-H1 vs. 2024-H1, or quarterly cohorts) would strengthen the claim that this captures meaningful temporal change rather than arbitrary calendar-year effects. Severity: minor.

---

### 4. Questions for Authors

1. Have you computed the difficulty-direction interaction (rho = -0.597) under the ability-matched condition (after nearest-neighbor matching)? If the interaction persists with d approximately -0.01, it would substantially strengthen the claim that this reflects genuine capability change rather than mean-ability confounding.

2. What happens if you define cohorts by training data cutoff date rather than model release date? Many 2024 models may have been trained on pre-2024 data. Is metadata available in METABENCH to test this?

3. The enrichment of approximately 1.0 between DIF flags and web-overlap labels is presented as evidence that the two methods capture "orthogonal signals." But could this also mean that DIF is detecting something that is simply noise -- random item-level variation unrelated to contamination? What evidence distinguishes "genuine differential functioning" from "statistical noise at item level"?

4. The semi-synthetic injection framework flips incorrect-to-correct responses at rate p. This models a very specific contamination mechanism (memorization of correct answers). How would DIF perform under more realistic contamination patterns, e.g., improved reasoning that affects related items heterogeneously?

5. You report that reasoning-RL models are underpowered (N=13). Given the rapid growth of reasoning models (o1, DeepSeek-R1, etc.), do you have any preliminary evidence on whether these models exhibit different DIF patterns?

6. The paper claims "the largest-scale DIF analysis on LLM benchmarks." To your knowledge, has DIF been applied to LLM benchmarks at any scale previously? If not, this is not just the "largest" but the "first," which is a stronger claim.

---

### 5. Soundness: 4/5

The statistical methodology is rigorous within its scope. The MH-DIF procedure is applied correctly, with appropriate controls (random split, ability matching, BH correction, threshold sensitivity, de-duplication). The Simpson's paradox analysis is well-executed. The main soundness concern is the causal ambiguity: the paper sometimes implies more about the causes of DIF than the evidence supports. The semi-synthetic framework validates detection power but does not validate interpretation of observed DIF. The matched-ability analysis (d = -0.17, 2.4pp reduction) is a strong control. The cross-benchmark replication adds confidence. I deduct one point for the interpretive gap between what DIF detects (statistical change) and what the paper sometimes implies it means (contamination-related change).

### 6. Excitement: 3.5/5

The paper applies a standard psychometric method to a new domain without modification. This is explicitly acknowledged. The excitement comes from the empirical findings rather than methodological novelty. The 31% instability finding is striking and practically relevant for anyone using MMLU for cross-temporal model comparison. The Simpson's paradox result is genuinely interesting. The cross-subject matching innovation is useful but narrow. The ground truth meta-critique, while valid, is more of an observation than a breakthrough. The paper makes a solid case that psychometric tools should be part of the benchmark maintenance toolkit, but the insight that "test items can behave differently across populations" is well-known in psychometrics -- the contribution is demonstrating this concretely for LLMs at scale. For EMNLP, this represents a competent application of established methods to a relevant problem with interesting findings, placing it at the borderline between Findings and Conference acceptance.

### 7. Reproducibility: 4/5

METABENCH is publicly available, the MH-DIF procedure is standard, and the paper provides sufficient detail on cohort definitions, matching strategies, and injection protocols to reproduce the core results. The five-seed protocol for semi-synthetic injection is good practice. The paper does not mention code release, which would help. The 99.98% decoder-only architecture finding and the specific numbers (e.g., N = 1,080 reference, 807 focal) are precise enough for replication. The main reproducibility concern is that some results depend on model metadata (release dates, family membership) that may not be fully standardized in METABENCH.

### 8. Overall Assessment: 3.5 (Borderline Conference)

This is a well-executed empirical paper that applies standard psychometric methods to LLM benchmark evaluation and produces genuinely interesting findings. The 31% temporal instability finding, replicated across six benchmarks, is practically relevant and the analysis is thorough. The Simpson's paradox result is compelling. The paper is honest about its contribution type and well-positioned against related work. However, the methodological novelty is limited (MH-DIF is off-the-shelf), the ground truth meta-critique is more observation than contribution, the causal interpretability gap between "items changed" and "why they changed" is not fully addressed, and the DIF audit protocol is underspecified. The paper would benefit from deeper engagement with what DIF means in the LLM context (where the fairness motivation from education does not apply) and from the difficulty-direction analysis under matched conditions. It is above the threshold for Findings and competitive for Conference acceptance, but the limited methodological novelty and interpretive gaps place it at the borderline.

### 9. Confidence: 4/5

I am familiar with both the DIF/psychometrics literature and the LLM evaluation literature. I have read the paper carefully, including the appendix. I am confident in my assessment of the methodological soundness and the related work coverage. My uncertainty is primarily about whether the community will value the "standard method applied to new domain" contribution type highly enough for main conference acceptance at EMNLP -- this is partially a calibration question about reviewer pool preferences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c12c951f-e067-4af5-ab11-d7184ef6734d",
  "isSidechain": true,
  "agentId": "a3c9d662c10f2e121",
  "requestId": "req_011CbFfvhPKJKCdnC6LREyHH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ca0e88c-dadd-47cd-8b30-4de35e8d8740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3UNvFJTjYHktuH5pfNe7S",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 66239,
      "output_tokens": 3592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 823
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3592,
          "cache_read_input_tokens": 66239,
          "cache_creation_input_tokens": 823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 823,
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
