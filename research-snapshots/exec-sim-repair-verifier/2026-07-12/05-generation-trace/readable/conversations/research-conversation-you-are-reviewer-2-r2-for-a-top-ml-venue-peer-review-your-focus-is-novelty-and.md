# Research conversation: You are Reviewer 2 (R2) for a top ML venue peer review. Your focus is **novelty and related work**. Review the paper des

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-acd05d89cc17cecdb.jsonl`
- **Structured JSON:** [`7d9e123b894584b8d9fd.json`](../../sessions/7d/7d9e123b894584b8d9fd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-16T08:24:11.402Z_

You are Reviewer 2 (R2) for a top ML venue peer review. Your focus is **novelty and related work**. Review the paper described below independently. Use a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

**Title**: "Per-Test Classification for Code Execution Simulation: Classification Works Where Generation Fails"

**Core idea**: For execution-free verification of code patches, instead of trajectory-level scoring (binary resolved/unresolved) or Code World Models (CWM, predicting execution outputs token-by-token), propose per-test binary classification (CLS) that predicts pass/fail for each (code, test) pair independently.

**Three claims**:
1. **Complexity-dependent formulation advantage**: CLS ≈ CWM at function-level (both 87.51% at 4B), CLS scales better with model size (8B: +2.43pp), CLS works at repo-level (82–85%) where CWM catastrophically fails (50–93% unparseable).
2. **Diagnostic granularity at equivalent accuracy**: Per-test CLS ≈ trajectory-level (TOST p=0.007, ±2pp margin).
3. **Per-test advantage concentrates in T≥2 instances** (31.3% of SWE-bench Verified).

## Method

- **Models**: Qwen3-4B, Qwen3-8B (LoRA rank 16, α=32), DeepSeek-Coder-6.7B-Instruct
- **CLS**: Binary cross-entropy on pass/fail per (code, test) pair
- **CWM**: Next-token prediction on execution output strings, then string matching
- **Trajectory-level**: Single binary resolved/unresolved prediction
- **Data**: Function-level mutant detection; repo-level SWE-bench-PerTest (435 instances, ~68K per-test labels)

## Related Work Section (from paper, Section 4)

The paper has a very brief Related Work section with 4 short paragraphs:

1. **Code World Models**: Cites Gu et al. [1] (CRUXEval, ICML 2024) for execution simulation via output generation. Claims their work shows CWM faces "fundamental scaling challenges on complex code" where classification is more robust.

2. **Execution-Free Verification**: Mentions SWE-RM and related reward models that predict trajectory-level correctness. Claims per-test formulation preserves granularity lost by these approaches.

3. **LLM-as-Judge for Code**: Notes zero-shot LLM judges show bias toward predicting failure; fine-tuning is necessary.

4. **Test-Time Scaling**: Brief mention of test-time compute scaling for code generation; per-test classification enables targeted re-repair.

**Only 1 reference** is cited: [1] Gu et al. (2024) CRUXEval, ICML 2024.

## Key Experiments and Results

- Function-level: CLS = CWM at 4B (87.51%), CLS +2.43pp at 8B
- Repo-level: CLS 82–86%, CWM 50–93% unparseable
- TOST equivalence: per-test ≈ trajectory within ±2pp (p=0.007)
- Oracle F2P analysis: per-test advantage in T≥2 (31.3% of SWE-bench)
- Error complementarity: oracle ensemble 90.63%
- DeepSeek: CLS–CWM gap reverses (CWM +0.7pp better)
- Zero-shot baselines: fine-tuned 4B >> zero-shot 32B
- Re-repair pilot: +4.1pp (p=0.11, n=120), not significant
- Majority voting: hurts by 0.69pp
- P2P regression: negative finding (empirical rate ~1%, breakeven at 10%)
- SWE-bench-PerTest dataset: 435 instances, ~68K labels

## Limitations (from paper)
1. CWM repo-level failure may partly reflect max_new_tokens and output format choices
2. Re-repair experiment underpowered (n=120)
3. Cross-architecture results are mixed
4. Trace-then-judge ablation failed
5. Seeds 789 and 0 used 4-bit quantization in TOST

## Your Task

Evaluate the **novelty and related work** rigorously:

1. **Technical novelty**: How novel is the per-test binary classification formulation? Is this a genuinely new idea or a straightforward baseline that should have been compared in prior work?
2. **Related work coverage**: Is the related work section comprehensive? What major related work is missing?
3. **Positioning**: How well does the paper position itself relative to existing work? Does it fairly represent prior approaches?
4. **Contribution significance**: Even if the idea is simple, is the empirical contribution significant enough for a top venue?
5. **Narrative honesty**: Does the paper fairly present its mixed results (DeepSeek gap reversal, non-significant re-repair, failed ablation)?

Key questions to consider:
- SWE-RM, SWE-Judge, and other execution-free verifiers are not cited beyond a vague mention. Are these critical omissions?
- The CWM comparison relies on a single citation (CRUXEval). Are there other CWM-style approaches?
- Is per-test classification genuinely novel, or is it the obvious first thing anyone would try?
- The paper has only 1 reference. For a top venue, is this acceptable?

Provide your review in this exact format:

```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentence summary]

### Strengths
- S1: ...
- S2: ...
[etc.]

### Weaknesses
- W1: ...
- W2: ...
[etc.]

### Missing Related Work
- [List specific papers/approaches that should be discussed]

### Questions for Authors
- Q1: ...
- Q2: ...
[etc.]

### Minor Issues
- ...

### Overall Assessment
[1-2 paragraph assessment]

### Scores
- Novelty: X/5
- Related Work Completeness: X/5
- Significance: X/5
- Overall Recommendation: X/6 (label)
- Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "56caabaf-ab9c-4b84-b3a0-6c8eb12d6fab",
  "agentId": "acd05d89cc17cecdb",
  "type": "user",
  "uuid": "021c4d65-6201-48b2-ac96-200211932997",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T08:24:11.406Z_

```json
{
  "parentUuid": "021c4d65-6201-48b2-ac96-200211932997",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
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
  "uuid": "9bdea739-a71b-4d6f-ae0d-6727f0b030fc",
  "timestamp": "2026-05-16T08:24:11.406Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-16T08:24:14.844Z_



I'll review the paper thoroughly by first examining the actual paper files to understand the full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bdea739-a71b-4d6f-ae0d-6727f0b030fc",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5vhjRCpUmmqq3MtW3Ru",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a71b8c6a-9840-421e-8a91-dc624af81327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKz6DhdMFoGbrYQ9UMJzoW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7411,
      "cache_read_input_tokens": 8950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7411,
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

_source line 4 · 2026-05-16T08:24:16.736Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013oAvUBnsp3E3QxB4D18mim`</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a71b8c6a-9840-421e-8a91-dc624af81327",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5vhjRCpUmmqq3MtW3Ru",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1eb2210-5eba-4b01-b0c0-a88c0e24ece5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKz6DhdMFoGbrYQ9UMJzoW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7411,
      "cache_read_input_tokens": 8950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7411,
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

_source line 5 · 2026-05-16T08:24:16.765Z_

<details><summary>↩ Tool result · `toolu_013oAvUBnsp3E3QxB4D18mim`</summary>

```text
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/abstract.tex
docs/paper/appendix.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1eb2210-5eba-4b01-b0c0-a88c0e24ece5",
  "isSidechain": true,
  "promptId": "56caabaf-ab9c-4b84-b3a0-6c8eb12d6fab",
  "agentId": "acd05d89cc17cecdb",
  "type": "user",
  "uuid": "4fbf1b1f-6c89-4103-b8c8-1b3c5baeb70d",
  "sourceToolAssistantUUID": "f1eb2210-5eba-4b01-b0c0-a88c0e24ece5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T08:24:16.906Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WURi35PZgqNkTDHWSAjT9x`</summary>

```json
{
  "pattern": "docs/paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fbf1b1f-6c89-4103-b8c8-1b3c5baeb70d",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5vhjRCpUmmqq3MtW3Ru",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dff2e3a9-ea23-4db1-8411-e94492af8f84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKz6DhdMFoGbrYQ9UMJzoW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7411,
      "cache_read_input_tokens": 8950,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 209,
          "cache_read_input_tokens": 8950,
          "cache_creation_input_tokens": 7411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7411,
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

_source line 7 · 2026-05-16T08:24:16.935Z_

<details><summary>↩ Tool result · `toolu_01WURi35PZgqNkTDHWSAjT9x`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dff2e3a9-ea23-4db1-8411-e94492af8f84",
  "isSidechain": true,
  "promptId": "56caabaf-ab9c-4b84-b3a0-6c8eb12d6fab",
  "agentId": "acd05d89cc17cecdb",
  "type": "user",
  "uuid": "497cf467-3337-4678-8d38-7c47292d30b9",
  "sourceToolAssistantUUID": "dff2e3a9-ea23-4db1-8411-e94492af8f84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T08:24:19.827Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y4tXChr1KGCkkyHcoLDLGF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "497cf467-3337-4678-8d38-7c47292d30b9",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5vi98U9Q2jjGMRkFaSX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f7ba37e-fd07-4ea5-ade3-20818fe00d07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkFCQ7Rc86vUxstjJP115c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 16361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1183,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
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

_source line 9 · 2026-05-16T08:24:19.834Z_

<details><summary>↩ Tool result · `toolu_01Y4tXChr1KGCkkyHcoLDLGF`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation for Code.}
5	Code World Models~\cite{meta2025cwm} mid-train a 32B LLM on execution traces to predict output strings, establishing the generation-based paradigm for execution-free code verification.
6	Self-Execution~\cite{maimon2026selfexecution} extends this with step-by-step trace prediction, demonstrating that simulation-based self-verification can improve code generation without external execution.
7	CodeMind~\cite{liu2024codemind} evaluates code reasoning along multiple dimensions including independent and dependent execution reasoning.
8	SolidCoder~\cite{lee2026solidcoder} bridges mental simulation and actual execution via concrete execution feedback.
9	Abdollahi et al.~\cite{abdollahi2025demystifying} identify systematic failure modes in LLM trace prediction, including position-dependent and cascading errors.
10	All share a generation formulation whose cost scales with output length and whose reliability degrades when outputs are complex---at repository-level complexity, we observe format compliance collapse (53--67\% unparseable outputs; \S\ref{sec:experiments}). We reformulate as per-test classification and show the advantage is complexity-dependent: negligible at function level but critical at repository scale.
11	
12	\paragraph{LLM-based Verification for Code Repair.}
13	SWE-RM~\cite{shum2025swerm} trains a 30B MoE reward model for trajectory-level execution-free patch ranking, achieving strong results on SWE-bench without test execution.
14	Patch Reasoner~\cite{xu2025patchreasoner} uses chain-of-thought reasoning for patch verification.
15	Snell et al.~\cite{snell2024scaling} show that test-time compute scaling via verification can outperform parameter scaling, establishing verification quality as a key lever for code generation improvement.
16	S*~\cite{li2025sstar} combines execution-grounded selection with model-based scoring for efficient test-time scaling.
17	VG-Search~\cite{chen2025vgsearch} studies how verification granularity affects compute-efficient scaling, finding that finer-grained verification can improve selection efficiency.
18	These works treat verification granularity as a design choice but do not compare the underlying \emph{formulation}---classification vs.\ generation---at controlled capacity. We formally compare per-test and trajectory-level granularity, showing statistical equivalence (TOST $p = 0.007$) with additional per-test diagnostic signals.
19	
20	\paragraph{Learned Code Verifiers.}
21	LEVER~\cite{ni2023lever} trains a classifier to re-rank code candidates by predicting execution correctness, learning verification from execution feedback.
22	CodeT~\cite{chen2023codet} generates auxiliary test cases and uses dual execution agreement---consensus between generated code and generated tests---as a verification signal.
23	Both methods leverage execution signals during training but target execution-free deployment, a goal shared by our classification formulation. Unlike LEVER's candidate-level ranking and CodeT's agreement-based filtering, we provide \emph{per-test} diagnostic verdicts that identify which specific tests fail, and systematically compare classification against generation on the same model, data, and compute budget, isolating the effect of task formulation.
24	
25	\paragraph{Automated Program Repair.}
26	SWE-bench~\cite{jimenez2024swebench} and SWE-bench Verified~\cite{chowdhury2024swebenchverified} provide standard benchmarks for repository-level repair, driving rapid progress in LLM-based program repair.
27	SWE-agent~\cite{yang2024sweagent} uses tool-augmented agents while Agentless~\cite{xia2024agentless} demonstrates a simpler localize--repair--validate pipeline that achieves competitive results.
28	Yang et al.~\cite{yang2025aprsurvey} survey the broader landscape of LLM-based program repair, identifying verification as a persistent bottleneck across approaches.
29	These systems rely on execution-based validation as the final filter, with verification cost scaling linearly in the number of candidates. Per-test classification provides failure-localized signals that could inform targeted re-repair---re-generating only the code responsible for a specific failing test---a capability absent from trajectory-level verifiers.
30	
31	\paragraph{Classification vs.\ Generation in NLP.}
32	Task framing affects model performance across NLP: T5~\cite{raffel2020t5} and BART~\cite{lewis2020bart} show generation--classification tradeoffs under controlled capacity, while SQuAD~\cite{rajpurkar2016squad} demonstrates that constraining output space (span extraction vs.\ generation) can simplify tasks without sacrificing quality. We extend this lens to code verification, identifying code complexity as the key moderator of the classification--generation tradeoff.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f7ba37e-fd07-4ea5-ade3-20818fe00d07",
  "isSidechain": true,
  "promptId": "56caabaf-ab9c-4b84-b3a0-6c8eb12d6fab",
  "agentId": "acd05d89cc17cecdb",
  "type": "user",
  "uuid": "205a3c3c-ad0a-4069-8d2c-ae2a61ca5858",
  "sourceToolAssistantUUID": "5f7ba37e-fd07-4ea5-ade3-20818fe00d07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T08:24:20.816Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qnj5qnjXM4vSsCPJiguj6V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "205a3c3c-ad0a-4069-8d2c-ae2a61ca5858",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5vi98U9Q2jjGMRkFaSX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf380a72-8020-4c57-bd1f-39583b852422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkFCQ7Rc86vUxstjJP115c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 16361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1183,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
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

_source line 11 · 2026-05-16T08:24:20.821Z_

<details><summary>↩ Tool result · `toolu_01Qnj5qnjXM4vSsCPJiguj6V`</summary>

```text
1	% === Execution Simulation ===
2	
3	@article{maimon2026selfexecution,
4	  title={Self-Execution Simulation Improves Coding Models},
5	  author={Maimon, Gallil and Yoran, Ori and Kreuk, Felix and Hassid, Michael and Cohen, Gal and Chambon, Pierre and Adi, Yossi},
6	  journal={arXiv preprint arXiv:2604.03253},
7	  year={2026}
8	}
9	
10	@article{meta2025cwm,
11	  title={{CWM}: An Open-Weights {LLM} for Research on Code Generation with World Models},
12	  author={{FAIR CodeGen team} and Copet, Jade and Carbonneaux, Quentin and Cohen, Gal and Gehring, Jonas and Kahn, Jacob and Kossen, Jannik and Kreuk, Felix and McMilin, Emily and Meyer, Michel and Wei, Yuxiang and Zhang, David and Zheng, Kunhao and others},
13	  journal={arXiv preprint arXiv:2510.02387},
14	  year={2025}
15	}
16	
17	@article{liu2024codemind,
18	  title={{CodeMind}: A Framework to Challenge Large Language Models for Code Reasoning},
19	  author={Liu, Changshu and Zhang, Shizhuo Dylan and Ibrahimzada, Ali Reza and Jabbarvand, Reyhaneh},
20	  journal={arXiv preprint arXiv:2402.09664},
21	  year={2024}
22	}
23	
24	@article{abdollahi2025demystifying,
25	  title={Demystifying Errors in {LLM} Reasoning Traces: An Empirical Study of Code Execution Simulation},
26	  author={Abdollahi, Mohammad and Tasnia, Khandaker Rifah and Saha, Soumit Kanti and Yang, Jinqiu and Wang, Song and Hemmati, Hadi},
27	  journal={arXiv preprint arXiv:2512.00215},
28	  year={2025}
29	}
30	
31	@article{lee2026solidcoder,
32	  title={{SolidCoder}: Bridging the Mental-Reality Gap in {LLM} Code Generation through Concrete Execution},
33	  author={Lee, Woojin and Huang, Jin-Xia},
34	  journal={arXiv preprint arXiv:2604.19825},
35	  year={2026}
36	}
37	
38	% === LLM Verification for Code ===
39	
40	@article{shum2025swerm,
41	  title={{SWE-RM}: Execution-free Feedback for Software Engineering Agents},
42	  author={Shum, KaShun and Hui, Binyuan and Chen, Jiawei and Zhang, Lei and Yang, Jiaxi and Huang, Yuzhen and Lin, Junyang and He, Junxian},
43	  journal={arXiv preprint arXiv:2512.21919},
44	  year={2025}
45	}
46	
47	@article{xu2025patchreasoner,
48	  title={Scalable Supervising Software Agents with Patch Reasoner},
49	  author={Xu, Junjielong and Tan, Boyin and Liu, Xiaoyuan and Peng, Chao and Gao, Pengfei and He, Pinjia},
50	  journal={arXiv preprint arXiv:2510.22775},
51	  year={2025}
52	}
53	
54	@inproceedings{chen2025vgsearch,
55	  title={Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling},
56	  author={Chen, Hao Mark and Lu, Guanxi and Okoshi, Yasuyuki and Mo, Zhiwen and Motomura, Masato and Fan, Hongxiang},
57	  booktitle={NeurIPS},
58	  year={2025}
59	}
60	
61	@inproceedings{snell2024scaling,
62	  title={Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
63	  author={Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
64	  booktitle={ICLR},
65	  year={2025},
66	  note={Oral}
67	}
68	
69	@inproceedings{li2025sstar,
70	  title={S*: Test Time Scaling for Code Generation},
71	  author={Li, Dacheng and Cao, Shiyi and Cao, Chengkun and Li, Xiuyu and Tan, Shangyin and Keutzer, Kurt and Xing, Jiarong and Gonzalez, Joseph E. and Stoica, Ion},
72	  booktitle={Findings of EMNLP},
73	  year={2025}
74	}
75	
76	% === APR and SWE-bench ===
77	
78	@inproceedings{jimenez2024swebench,
79	  title={{SWE-bench}: Can Language Models Resolve Real-world {GitHub} Issues?},
80	  author={Jimenez, Carlos E and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik},
81	  booktitle={ICLR},
82	  year={2024}
83	}
84	
85	@misc{chowdhury2024swebenchverified,
86	  title={Introducing {SWE-bench} Verified},
87	  author={Chowdhury, Neil and Aung, James and Shern, Chan Jun and Jaffe, Oliver and Sherburn, Dane and Starace, Giulio and Mays, Evan and Dias, Rachel and Aljubeh, Marwan and Glaese, Mia and Jimenez, Carlos E. and Yang, John and Ho, Leyton and Patwardhan, Tejal and Liu, Kevin and Madry, Aleksander},
88	  year={2024},
89	  url={https://openai.com/index/introducing-swe-bench-verified/}
90	}
91	
92	@inproceedings{yang2024sweagent,
93	  title={{SWE-agent}: Agent-Computer Interfaces Enable Automated Software Engineering},
94	  author={Yang, John and Jimenez, Carlos E and Wettig, Alexander and Lieret, Kilian and Yao, Shunyu and Narasimhan, Karthik and Press, Ofir},
95	  booktitle={NeurIPS},
96	  year={2024}
97	}
98	
99	@inproceedings{xia2024agentless,
100	  title={Agentless: Demystifying {LLM}-based Software Engineering Agents},
101	  author={Xia, Chunqiu Steven and Deng, Yinlin and Dunn, Soren and Zhang, Lingming},
102	  booktitle={FSE},
103	  year={2025},
104	  note={Distinguished Paper}
105	}
106	
107	@article{yang2025aprsurvey,
108	  title={A Survey of {LLM}-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications},
109	  author={Yang, Boyang and Cai, Zijian and Liu, Fengling and Le, Bach and Zhang, Lingming and Bissyand{\'e}, Tegawend{\'e} F. and Liu, Yang and Tian, Haoye},
110	  journal={arXiv preprint arXiv:2506.23749},
111	  year={2025}
112	}
113	
114	% === Code LLMs and Benchmarks ===
115	
116	@article{qwen2025qwen3,
117	  title={{Qwen3} Technical Report},
118	  author={Yang, An and Li, Anfeng and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and others},
119	  journal={arXiv preprint arXiv:2505.09388},
120	  year={2025}
121	}
122	
123	@article{chen2021humaneval,
124	  title={Evaluating Large Language Models Trained on Code},
125	  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and others},
126	  journal={arXiv preprint arXiv:2107.03374},
127	  year={2021}
128	}
129	
130	@article{austin2021mbpp,
131	  title={Program Synthesis with Large Language Models},
132	  author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and others},
133	  journal={arXiv preprint arXiv:2108.07732},
134	  year={2021}
135	}
136	
137	@inproceedings{hu2022lora,
138	  title={{LoRA}: Low-Rank Adaptation of Large Language Models},
139	  author={Hu, Edward J and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
140	  booktitle={ICLR},
141	  year={2022}
142	}
143	
144	@inproceedings{dettmers2024qlora,
145	  title={{QLoRA}: Efficient Finetuning of Quantized {LLMs}},
146	  author={Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
147	  booktitle={NeurIPS},
148	  year={2023}
149	}
150	
151	% === Code Verification ===
152	
153	@inproceedings{ni2023lever,
154	  title={{LEVER}: Learning to Verify Language-to-Code Generation with Execution},
155	  author={Ni, Ansong and Iyer, Srini and Radev, Dragomir and Stoyanov, Veselin and Yih, Wen-tau and Wang, Sida I. and Lin, Xi Victoria},
156	  booktitle={ICML},
157	  year={2023}
158	}
159	
160	@inproceedings{chen2023codet,
161	  title={{CodeT}: Code Generation with Generated Tests},
162	  author={Chen, Bei and Zhang, Fengji and Nguyen, Anh and Zan, Daoguang and Lin, Zeqi and Lou, Jian-Guang and Chen, Weizhu},
163	  booktitle={ICLR},
164	  year={2023}
165	}
166	
167	% === Task Reformulation NLP ===
168	
169	@inproceedings{rajpurkar2016squad,
170	  title={{SQuAD}: 100,000+ Questions for Machine Comprehension of Text},
171	  author={Rajpurkar, Pranav and Zhang, Jian and Lopyrev, Konstantin and Liang, Percy},
172	  booktitle={EMNLP},
173	  year={2016}
174	}
175	
176	@inproceedings{lewis2020bart,
177	  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},
178	  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},
179	  booktitle={ACL},
180	  year={2020}
181	}
182	
183	@article{raffel2020t5,
184	  title={Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
185	  author={Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J},
186	  journal={JMLR},
187	  volume={21},
188	  number={140},
189	  pages={1--67},
190	  year={2020}
191	}
192	
193	% === Statistical Methods ===
194	
195	@article{schuirmann1987tost,
196	  title={A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},
197	  author={Schuirmann, Donald J},
198	  journal={Journal of Pharmacokinetics and Biopharmaceutics},
199	  volume={15},
200	  number={6},
201	  pages={657--680},
202	  year={1987}
203	}
204	
205	@book{davison1997bootstrap,
206	  title={Bootstrap Methods and their Application},
207	  author={Davison, Anthony C and Hinkley, David V},
208	  publisher={Cambridge University Press},
209	  year={1997}
210	}
211	
212	@article{shrout1979icc,
213	  title={Intraclass Correlations: Uses in Assessing Rater Reliability},
214	  author={Shrout, Patrick E and Fleiss, Joseph L},
215	  journal={Psychological Bulletin},
216	  volume={86},
217	  number={2},
218	  pages={420--428},
219	  year={1979},
220	  doi={10.1037/0033-2909.86.2.420}
221	}
222	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf380a72-8020-4c57-bd1f-39583b852422",
  "isSidechain": true,
  "promptId": "56caabaf-ab9c-4b84-b3a0-6c8eb12d6fab",
  "agentId": "acd05d89cc17cecdb",
  "type": "user",
  "uuid": "de8370f5-a256-47b3-87dc-5646959cd4dc",
  "sourceToolAssistantUUID": "cf380a72-8020-4c57-bd1f-39583b852422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T08:24:20.933Z_

<details open><summary>🔧 Tool call — Read · `toolu_018PYUzjg9xWdTb9tepv99LA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de8370f5-a256-47b3-87dc-5646959cd4dc",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5vi98U9Q2jjGMRkFaSX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b3de163-464d-42de-a703-38cfa151d181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkFCQ7Rc86vUxstjJP115c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 16361,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1183
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 16361,
          "cache_creation_input_tokens": 1183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1183,
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

_source line 13 · 2026-05-16T08:24:20.943Z_

<details><summary>↩ Tool result · `toolu_018PYUzjg9xWdTb9tepv99LA`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair has advanced rapidly on real-world software tasks. Agent-based systems such as SWE-agent~\cite{yang2024sweagent} and pipeline approaches like Agentless~\cite{xia2024agentless} resolve substantial fractions of SWE-bench~\cite{jimenez2024swebench} issues through candidate patch generation and validation. The prevailing strategy for improving resolve rates is test-time compute scaling~\cite{snell2024scaling}: generating $K$ candidate patches and selecting the best via a verifier. This verification step is critical---without it, the additional compute invested in diverse patch generation yields diminishing returns, because correct patches are diluted among incorrect ones. Full execution verification---running the repository's test suite against each candidate---is reliable but expensive, costing \$1--3 and several minutes per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}, making it prohibitive for large $K$. The resulting demand for fast, execution-free verification has driven work on learned verifiers~\cite{ni2023lever,shum2025swerm} and execution simulators~\cite{meta2025cwm,maimon2026selfexecution}, but the choice of \emph{how} to formulate the verification task---what the model predicts and in what format---has received surprisingly little systematic study.
5	
6	Two dominant paradigms have emerged. \textbf{Generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test, deriving verdicts by exact match. This suffers three failure modes at scale: (1)~\emph{token-budget exhaustion} truncates long outputs; (2)~\emph{string-value errors} reject semantically correct outputs differing in surface form; (3)~\emph{format compliance collapse} renders the majority of predictions unparseable at repository-level complexity, with parseable accuracy dropping below chance (38--43\% across model sizes).
7	
8	\textbf{Trajectory-level scoring}~\cite{shum2025swerm} predicts patch-level correctness directly, bypassing generation. This is robust---no outputs to truncate or parse---but discards per-test diagnostic signals needed for targeted re-repair~\cite{yang2024sweagent,xia2024agentless}. The apparent trade-off: generation preserves per-test granularity at the cost of reliability, while trajectory-level scoring provides reliability at the cost of granularity.
9	
10	We argue this trade-off is an artifact of the formulation. Per-test binary classification---predicting a single \textsc{Pass}/\textsc{Fail} token---eliminates all three failure modes by construction: a single-token output cannot be truncated, needs no string matching, and is always parseable, while preserving the per-test diagnostics that trajectory-level scoring discards. Prior learned verifiers (LEVER~\cite{ni2023lever}, CodeT~\cite{chen2023codet}) leverage execution signals but target candidate-level ranking rather than per-test diagnostic classification. No prior work compares classification and generation formulations at controlled model sizes across complexity levels.
11	
12	Crucially, the advantage is complexity-dependent. At function level, both formulations achieve near-equivalent accuracy (\mbox{1.24\pp{}} gap, 5 seeds, 4B). The gap emerges only when \cwm{} failure modes dominate: at repository level, it widens to \mbox{25.59\pp{}}. We formalize this via an oracle accuracy-utility framework (\S\ref{sec:oracle}) that predicts when per-test granularity provides value given test distribution and prediction correlation.
13	
14	We validate these predictions through controlled experiments comparing the three formulations on function-level benchmarks (HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp}) and repository-level tasks (SWE-bench Verified~\cite{chowdhury2024swebenchverified}), using Qwen3~\cite{qwen2025qwen3} models at 4B and 8B parameters with matched training data and compute. Figure~\ref{fig:reformulation} illustrates the three formulations. We make the following contributions:
15	
16	\begin{itemize}[leftmargin=*,itemsep=2pt]
17	\item \textbf{Complexity-dependent reformulation advantage.} The \cls{}--\cwm{} gap grows with complexity: near-null at function level (\mbox{1.18\pp{}}, 4B), widening to 2.26\pp{} at 8B (bootstrap mean, $p = 0.0066$; both 3 seeds), and 19--26\pp{} at repository level (8B-8B: 19.31\pp{}; 4B-4B: 25.59\pp{}, seed~42)---an order of magnitude larger than function-level. \cwm{} generation quality uniformly degrades with scale: parseable-only accuracy decreases from 42.9\% (4B) to 38.5\% (8B) while unparseable rate increases from 53.7\% to 73.8\%. Function-level scaling provides converging evidence: \cls{} gains \mbox{+0.99\pp{}} (4B$\to$8B) while \cwm{} loses \mbox{$-$0.27\pp{}}, consistent with a generation bottleneck rather than a capacity limitation.
18	
19	\item \textbf{Diagnostic granularity at equivalent accuracy.} Per-test classification achieves statistically equivalent variant-level accuracy to trajectory-level scoring (TOST equivalence test $p = 0.007$, $\pm$2\pp{} margin) while providing per-test diagnostic signals---which specific tests fail---at no accuracy cost. This enables downstream applications such as targeted re-repair that trajectory-level verifiers cannot support.
20	
21	\item \textbf{Accuracy-utility frontier characterization.} Oracle analysis on SWE-bench Verified~\cite{chowdhury2024swebenchverified} shows that the per-test advantage concentrates in instances with $T \geq 2$ FAIL\_TO\_PASS tests (31\% of instances, contributing 55\% of total advantage), while instances with $T = 1$ (69\%) gain nothing from per-test granularity. This provides a practical decision framework for when per-test verification is worth deploying.
22	\end{itemize}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b3de163-464d-42de-a703-38cfa151d181",
  "isSidechain": true,
  "promptId": "56caabaf-ab9c-4b84-b3a0-6c8eb12d6fab",
  "agentId": "acd05d89cc17cecdb",
  "type": "user",
  "uuid": "9e6144f1-57a0-4945-bac4-242b04d96e8f",
  "sourceToolAssistantUUID": "2b3de163-464d-42de-a703-38cfa151d181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T08:24:25.777Z_

<details open><summary>🔧 Tool call — Read · `toolu_012CAXPw32YmrWPxpA9hHABz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e6144f1-57a0-4945-bac4-242b04d96e8f",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5viSNoMTDgYYuQxqC7X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "668e7c16-1f2b-48a8-ab3c-6c4c24f91d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XMnaPkPC9vfKrmGCZ5nNX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6783,
      "cache_read_input_tokens": 17544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6783,
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

_source line 15 · 2026-05-16T08:24:25.782Z_

<details><summary>↩ Tool result · `toolu_012CAXPw32YmrWPxpA9hHABz`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate \cls{}, \cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench}.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with LoRA~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. Our \cwm{} baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge.
15	
16	\paragraph{Statistics.}
17	Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); per-test vs.\ trajectory-level comparison uses TOST~\cite{schuirmann1987tost} ($\pm$2\pp{} margin). ICC~\cite{shrout1979icc} quantifies within-problem correlation. Oracle analysis uses SWE-bench Verified (500 instances).
18	
19	
20	\subsection{Function-Level Results}
21	\label{sec:func_results}
22	
23	Table~\ref{tab:main_results} reports function-level results across formulations.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \cls{}: per-test binary classification; \cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\pm$ std over seeds reported where applicable.}
29	\label{tab:main_results}
30	\resizebox{\columnwidth}{!}{%
31	\setlength{\tabcolsep}{4pt}
32	\begin{tabular}{llcc}
33	\toprule
34	\textbf{Method} & \textbf{Model} & \textbf{Seeds} & \textbf{Accuracy (\%)} \\
35	\midrule
36	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
37	\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\pm$ 0.37 \\
38	TRAJ (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
39	\midrule
40	ZS LLM-as-judge & 8B & 1 & 64.40 \\
41	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
42	\bottomrule
43	\end{tabular}}
44	\end{table}
45	
46	Fine-tuned \cls{} achieves 88.43\% ($\pm$0.78), compared to 87.19\% ($\pm$0.37) for \cwm{} and 86.30\% ($\pm$0.97) for TRAJ. The \cls{}--\cwm{} gap is 1.24\pp{}, modest at this complexity level where generation is not yet bottlenecked by token budget or string complexity. Zero-shot baselines lag substantially (64.40\% at 8B, 71.69\% at 32B NF4), confirming that task-specific fine-tuning is necessary for reliable verification.
47	
48	
49	\subsection{Scaling Behavior}
50	\label{sec:scaling}
51	
52	Table~\ref{tab:scaling} compares \cls{} and \cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.
53	
54	\begin{table}[t]
55	\centering
56	\small
57	\caption{Model-size scaling: \cls{} vs.\ \cwm{} accuracy (\%) at 4B and 8B. Three matched seeds in full precision. The \cls{}--\cwm{} gap widens from 1.18\pp{} to 2.43\pp{}.}
58	\label{tab:scaling}
59	\setlength{\tabcolsep}{4pt}
60	\begin{tabular}{llccccc}
61	\toprule
62	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{s456} & \textbf{Mean} & \textbf{Gap} \\
63	\midrule
64	\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \multirow{2}{*}{1.18} \\
65	\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\
66	\midrule
67	\cls{} & 8B & \textbf{90.48} & 89.40 & 88.31 & \textbf{89.40} & \multirow{2}{*}{\textbf{2.43}} \\
68	\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\
69	\bottomrule
70	\end{tabular}
71	\end{table}
72	
73	At 4B, \cls{} and \cwm{} are separated by 1.18\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\pp{} (Figure~\ref{fig:scaling_gap}). Clustered bootstrap analysis yields a mean gap of 2.26\pp{} ($p = 0.0066$, 95\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.
74	
75	The asymmetry in scaling efficiency is striking: from 4B to 8B, \cls{} gains +0.99\pp{} (88.41 $\to$ 89.40) while \cwm{} loses $-$0.27\pp{} (87.23 $\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \cwm{} accuracy. However, the \cwm{} regression ($-$0.27\pp{}) falls within seed noise (3-seed std ${\sim}$0.5\pp{}) and could reflect suboptimal hyperparameter transfer rather than a fundamental bottleneck. Whether this divergence amplifies at repository-level complexity is examined in \S\ref{sec:repo}.
76	
77	
78	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
79	\label{sec:equivalence}
80	
81	We compare \cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds. The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); the TOST equivalence test confirms statistical equivalence at $p = 0.007$ ($\pm$2\pp{} margin). Within-problem predictions are correlated (ICC $= 0.191$, $p < 0.0001$, DEFF $= 3.97$); all statistical tests use clustered bootstrap accordingly. Per-test classification thus provides diagnostic information---which specific tests fail---at no cost to variant-level accuracy.
82	
83	
84	\subsection{Accuracy-Utility Frontier}
85	\label{sec:oracle-results}
86	
87	Oracle analysis on SWE-bench Verified (500 instances) reveals that per-test advantage concentrates sharply: at $T = 1$ F2P tests (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T \geq 2$ (31.3\%), with $T = 2$ alone contributing 55.3\% of the total 10.93\pp{} block-correlated advantage. Pass-to-pass (P2P) regression is negligible (1.04\% mean, 0\% median), so the practical value concentrates in fail-to-pass discrimination. Full stratification and the i.i.d.\ vs.\ block-correlated comparison appear in Appendix~\ref{app:oracle}.
88	
89	
90	\subsection{Repo-Level Results}
91	\label{sec:repo}
92	
93	Table~\ref{tab:repo_level} compares \cls{} and \cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy; the test set ($n{=}9{,}784$) has zero problem overlap with validation. We report both overall accuracy (where unparseable outputs default to the majority class, pass) and parseable-only accuracy to disentangle generation quality from default assignment effects.
94	
95	\begin{table}[t]
96	\centering
97	\small
98	\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Parse Acc: accuracy computed only on parseable outputs. Unparseable \cwm{} outputs default to pass (majority class, 72.96\%).}
99	\label{tab:repo_level}
100	\resizebox{\columnwidth}{!}{%
101	\setlength{\tabcolsep}{3pt}
102	\begin{tabular}{llcccccc}
103	\toprule
104	\textbf{Method} & \textbf{Size} & \textbf{Seed} & \textbf{Acc (\%)} & \textbf{Macro \fone{}} & \textbf{Unparse (\%)} & \textbf{Parse Acc (\%)} & \textbf{vs Maj.\ (\pp{})} \\
105	\midrule
106	\cls{} & 4B & 42 & \textbf{83.63} & 75.63 & 0.0 & --- & +10.67 \\
107	\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & 42.88 & $-$14.92 \\
108	\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & 42.68 & $-$13.87 \\
109	\midrule
110	\cls{} & 8B & 42 & 84.48 & 78.17 & 0.0 & --- & +11.52 \\
111	\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & --- & +12.64 \\
112	\cwm{} & 8B & 42 & 65.17 & --- & 73.8 & 38.52 & $-$7.79 \\
113	\midrule
114	Majority & --- & --- & 72.96 & --- & --- & --- & --- \\
115	\bottomrule
116	\end{tabular}}
117	\end{table}
118	
119	\paragraph{Same-size gap magnitude.} The \cls{}--\cwm{} gap at 4B is 25.59\pp{} (\cls{} 83.63\% vs.\ \cwm{} 58.04\%, seed 42; Figure~\ref{fig:scaling_gap}); at 8B it is 19.31\pp{} (84.48\% vs.\ 65.17\%). Both gaps far exceed the function-level gap (1--2\pp{}, Table~\ref{tab:scaling}), confirming that the classification advantage is complexity-dependent. \cwm{} falls below the majority baseline at both scales ($-$14.92\pp{} at 4B, $-$7.79\pp{} at 8B), indicating negative utility.
120	
121	\paragraph{Overall accuracy is misleading.} The apparent \cwm{} ``improvement'' from 4B (58.04\%) to 8B (65.17\%) is an artifact of the default assignment protocol: unparseable outputs receive the majority-class label (pass, 72.96\% of the test set). As unparseable rate \emph{increases} from 53.7\% to 73.8\%, more predictions are replaced by this high-accuracy default, inflating overall accuracy. The parseable-only accuracy---which isolates actual generation quality---\emph{decreases} from 42.88\% (4B) to 38.52\% (8B), confirming that CWM generation degrades with scale at repository-level complexity.
122	
123	\paragraph{Generation quality degrades uniformly.} Per-mutation analysis of \cwm{} 8B reveals degradation across all categories relative to 4B. The gold mutation (unmodified code) is most striking: parse rate collapses from 43.5\% (4B) to 23.9\% (8B), with parseable accuracy at 16.5\%---far below the trivially-correct ``pass'' prediction. This indicates that even the simplest generation target (reproducing expected outputs for correct code) becomes harder at scale, consistent with a fundamental generation bottleneck rather than insufficient capacity. Detailed per-mutation breakdown appears in Appendix~\ref{app:repo_mutation}.
124	
125	\paragraph{Scaling evidence.} The correct scaling signal comes from function-level results (\S\ref{sec:scaling}), where the \cls{}--\cwm{} gap widens from 1.18\pp{} (4B) to 2.43\pp{} (8B, $p = 0.0066$) with controlled methodology (matched seeds, same precision, no default assignment). At repo-level, the primary claim is that absolute gap magnitude (19--26\pp{}) is an order of magnitude larger than at function level (1--2\pp{}), demonstrating complexity-dependent advantage.
126	
127	\paragraph{Sequence length.} A matched-context ablation confirms input context disparity explains $<$3\% of the \cls{}--\cwm{} gap: \cls{} 8B evaluated at \texttt{max\_seq\_length}$=$2,048 yields a matched-context gap of 25.00\pp{}, representing 98\% of the same-size 25.59\pp{} gap (Appendix~\ref{app:ablations}).
128	
129	\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline), indicating that val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \cwm{} 8B comparison is also single-seed. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches; the synthetic-to-real transfer gap remains untested.
130	
131	
132	\subsection{Analysis}
133	\label{sec:analysis}
134	
135	\paragraph{(a) Error complementarity.}
136	\cls{} and \cwm{} make errors in opposite directions at function level. Among \cls{} errors (seed 42), 75.5\% are false negatives (FAIL $\to$ PASS), meaning the classifier tends to over-predict passing. Among \cwm{} errors, 83.1\% are false positives (PASS $\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\% accuracy, a 3.12\pp{} improvement over \cls{} alone (87.51\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains.
137	
138	\paragraph{(b) CWM error mode breakdown.}
139	Among unparseable \cwm{} outputs, 76.9\% contain no execution keywords; 22.9\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\%), suggesting domain-specific code contexts prevent structured generation.
140	
141	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
142	Relaxed matching (tolerating format deviations, L0--L4) \emph{decreases} \cwm{} accuracy: 58.04\%$\to$56.98\% (seed 42) and 59.09\%$\to$55.91\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (42--53\%). The \cls{}--\cwm{} gap widens from 26\pp{} to 28\pp{}, ruling out the hypothesis that parsing strictness inflates the observed gap.
143	
144	\paragraph{(d) Variance compression.}
145	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and TRAJ (0.97\pp{}) at function level. This is consistent with the bottleneck hypothesis: if \cwm{} performance is capped by output-format constraints, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
146	
147	\paragraph{(e) Per-test precision and recall.}
148	\cls{} achieves fail \fone{} 87.86\% (precision 82.75\%, recall 93.64\%) at seed 42, with 42.1\% of problems perfectly predicted. Multi-F2P instances (6--10 tests) reach 96.3\% accuracy, corroborating the oracle finding.
149	
150	\paragraph{(f) Block correlation.}
151	Within-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\times$ more all-correct problems than i.i.d.\ expectation). All tests use clustered bootstrap accordingly.
152	
153	\paragraph{(g) LoRA rank and majority voting.}
154	Doubling adapter capacity (rank 32) does not improve \cwm{} accuracy ($-$0.51\pp{}, within seed variance); majority voting ($K{=}3$) decreases accuracy ($-$0.68\pp{}). Both confirm the bottleneck is formulation-level, not capacity-level (Appendix~\ref{app:ablations}).
155	
156	\paragraph{(h) Per-mutation scaling patterns.}
157	Scaling benefits are highly non-uniform across mutation types (Appendix, Table~\ref{tab:mutation_breakdown}). \texttt{off\_by\_one} is the largest \cls{} scaling beneficiary: accuracy jumps from 58.5\% (4B) to 83.0\% (8B mean, $+$24.6\pp{}). In contrast, \texttt{boundary\_removal} is scale-invariant at ${\sim}$46\% across all seeds and sizes, identifying a difficulty ceiling independent of capacity. For \cwm{}, gold mutation parse rate collapses from 43.5\% (4B) to 23.9\% (8B) despite being the simplest target---all tests pass by construction---indicating that generation capability degrades even for trivially correct code at larger scale.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "668e7c16-1f2b-48a8-ab3c-6c4c24f91d5f",
  "isSidechain": true,
  "promptId": "56caabaf-ab9c-4b84-b3a0-6c8eb12d6fab",
  "agentId": "acd05d89cc17cecdb",
  "type": "user",
  "uuid": "3f3cf9ff-609e-4d5e-a256-8e07a1f7fc12",
  "sourceToolAssistantUUID": "668e7c16-1f2b-48a8-ab3c-6c4c24f91d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T08:24:26.135Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QA5L8XgMBgth2qBhuTjSNo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f3cf9ff-609e-4d5e-a256-8e07a1f7fc12",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5viSNoMTDgYYuQxqC7X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8ec023f-9637-4d4d-91dd-6775f01e2697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XMnaPkPC9vfKrmGCZ5nNX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6783,
      "cache_read_input_tokens": 17544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6783,
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

_source line 17 · 2026-05-16T08:24:26.141Z_

<details><summary>↩ Tool result · `toolu_01QA5L8XgMBgth2qBhuTjSNo`</summary>

```text
1	% Method section — EMNLP 2026 ARR submission
2	% Classification Succeeds Where Generation Stalls:
3	% Reformulating Execution Simulation for Code Repair Verification
4	
5	\section{Method}
6	\label{sec:method}
7	
8	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
9	
10	\subsection{Verification Formulations}
11	\label{sec:formulations}
12	
13	Let $c_p$ denote the code context (unified diff) of patch $p$.
14	
15	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Cost: one token per test.
16	
17	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Cost: $\sum_i |\hat{o}_i|$ tokens.
18	
19	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests, providing no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences reflect per-test decomposition value.
20	
21	\subsection{\cwm{} Failure Modes}
22	\label{sec:failure-modes}
23	
24	The generation formulation introduces three systematic failure modes absent in classification: (1)~\emph{token-budget exhaustion}---when $|o_i^*| > B$, truncation guarantees exact-match failure; (2)~\emph{string-value prediction errors}---semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; even under optimistic independence assumptions, a sequence of $L$ tokens each with accuracy $q$ yields correct-sequence probability $q^L$, making long outputs exponentially harder; (3)~\emph{format compliance collapse}---at repository-level complexity, the model fails to produce structured predictions entirely, even when the generation budget is sufficient. We hypothesize that the increased input complexity and multi-file context at repository level overwhelm the model's ability to maintain format adherence across the generation; per-repository unparseable rates support this (\S\ref{sec:analysis}). We adopt exact string matching following the original \cwm{} evaluation protocol \citep{meta2025cwm}. This is conservative but does not disadvantage \cwm{}: the dominant failure at repository scale is format non-compliance, where outputs are structurally unparseable regardless of matching strategy. Unparseable \cwm{} predictions---those that cannot be parsed into a structured verdict---default to the majority-class label (\textsc{Pass}), equivalent to the majority baseline prediction. This favors \cwm{} by assigning the statistically most likely label rather than penalizing format failures.
25	
26	\cls{} bypasses all three by construction: its single-token output cannot be truncated, requires no string matching, and is always parseable. Classification reduces the output space from $\Sigma^*$ to $\{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$---strictly lower output complexity, though the underlying reasoning need not be simpler. We hypothesize a \emph{complexity-dependent advantage}: both formulations perform comparably on simple code, but \cls{} gains as output complexity triggers \cwm{} failure modes.
27	
28	\subsection{Oracle Accuracy-Utility Framework}
29	\label{sec:oracle}
30	
31	Per-test granularity is valuable only when per-test predictions are sufficiently accurate and multiple tests provide partially independent signals. Consider a buggy patch with $k = |T_{\text{f2p}}|$ fail-to-pass tests. A per-test verifier with recall $r$ detects the bug if it identifies at least one failing test:
32	%
33	\begin{equation}
34	  P_{\text{detect}}(k) = 1 - (1 - r)^{k_{\text{eff}}}
35	  \label{eq:pdetect}
36	\end{equation}
37	%
38	where $k_{\text{eff}}$ is the effective number of independent tests. Let $a_h$ denote the trajectory-level detection accuracy; it is independent of $k$.
39	
40	\paragraph{Block-correlation model.} Per-test predictions within the same patch are correlated. We model this via the intraclass correlation coefficient $\rho$ \citep[ICC;][]{shrout1979icc}:
41	%
42	\begin{equation}
43	  k_{\text{eff}} = \frac{k}{1 + (k - 1)\rho}
44	  \label{eq:keff}
45	\end{equation}
46	%
47	When $\rho = 0$, $k_{\text{eff}} = k$ (full independence); when $\rho = 1$, $k_{\text{eff}} = 1$ (per-test collapses to trajectory-level). The per-test advantage relative to a trajectory-level baseline is $\Delta(k) = P_{\text{detect}}(k) - a_h$, and the expected population advantage is:
48	%
49	\begin{equation}
50	  \mathbb{E}[\Delta] = \sum_{k=1}^{K} P(|T_{\text{f2p}}| = k) \cdot \Delta(k)
51	  \label{eq:expected-advantage}
52	\end{equation}
53	
54	\paragraph{Testable predictions.} This yields three predictions validated in \S\ref{sec:experiments}: (1)~at $k = 1$, $\Delta \approx 0$; (2)~$\Delta(k)$ increases with $k$, dampened by $\rho > 0$; (3)~$\mathbb{E}[\Delta]$ concentrates in multi-F2P-test instances.
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8ec023f-9637-4d4d-91dd-6775f01e2697",
  "isSidechain": true,
  "promptId": "56caabaf-ab9c-4b84-b3a0-6c8eb12d6fab",
  "agentId": "acd05d89cc17cecdb",
  "type": "user",
  "uuid": "10eeaa7d-29d3-4db7-89c9-1bc643f0b5a2",
  "sourceToolAssistantUUID": "f8ec023f-9637-4d4d-91dd-6775f01e2697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T08:24:26.380Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LWuVEuh6GXux3nj9fJ9coG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10eeaa7d-29d3-4db7-89c9-1bc643f0b5a2",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5viSNoMTDgYYuQxqC7X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96dcf75c-a613-4145-9b53-9fe5ea2ce729",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XMnaPkPC9vfKrmGCZ5nNX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6783,
      "cache_read_input_tokens": 17544,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6783
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 17544,
          "cache_creation_input_tokens": 6783,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6783,
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

_source line 19 · 2026-05-16T08:24:26.384Z_

<details><summary>↩ Tool result · `toolu_01LWuVEuh6GXux3nj9fJ9coG`</summary>

```text
1	\begin{abstract}
2	Execution-free verification for LLM-based code repair faces a granularity--accuracy tradeoff: generation-based approaches (Code World Models) predict execution output strings but suffer from token-budget exhaustion, string-value prediction errors, and format compliance collapse as code complexity grows, while trajectory-level verifiers provide binary patch verdicts but discard per-test diagnostic information.
3	%
4	We reformulate execution simulation from open-ended output generation to per-test binary pass/fail classification, and systematically compare classification (\cls{}), generation (\cwm{}), and trajectory-level formulations at controlled model sizes.
5	%
6	On function-level benchmarks, \cls{} and \cwm{} achieve near-equivalent accuracy at 4B parameters (88.43\% vs.\ 87.19\%, 5 seeds, gap 1.24\pp{}). At 8B the gap widens to 2.43\pp{} (bootstrap mean 2.26\pp{}, $p{=}0.0066$, 3 seeds), with \cwm{} failing to benefit from scaling (\cls{} +0.99\pp{} vs.\ \cwm{} $-$0.27\pp{}, 4B$\to$8B). Per-test \cls{} matches trajectory-level accuracy (TOST equivalence $p{=}0.007$, $\pm$2\pp{} margin) while providing free diagnostic granularity---which specific tests fail. Oracle analysis on SWE-bench Verified shows this advantage concentrates in instances with $\geq$2 failing tests (31\% of instances, 55\% of total advantage); an oracle ensemble reaches 90.63\%. At repository level, the gap amplifies to 19--26\pp{} (4B: 25.59\pp{}; 8B: 19.31\pp{})---an order of magnitude above function level---with \cwm{} below majority baseline at both scales. The apparent gap narrowing from 4B to 8B is a default-assignment artifact: \cwm{} generation quality uniformly degrades with scale (parseable-only accuracy 42.9\%$\to$38.5\%; unparseable rate 53.7\%$\to$73.8\%), while inflated overall accuracy reflects more predictions defaulting to the majority class. \cls{} remains robust with 0\% unparseable.
7	%
8	These results support classification as a promising alternative to generation-based execution simulation, with an advantage that grows with code complexity---from modest at function level to critical at repository level.
9	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96dcf75c-a613-4145-9b53-9fe5ea2ce729",
  "isSidechain": true,
  "promptId": "56caabaf-ab9c-4b84-b3a0-6c8eb12d6fab",
  "agentId": "acd05d89cc17cecdb",
  "type": "user",
  "uuid": "84f7a979-fda6-414a-88da-99ef72a84f61",
  "sourceToolAssistantUUID": "96dcf75c-a613-4145-9b53-9fe5ea2ce729",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T08:24:31.094Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C4hTSSZgrHJzaHKa3LF5Gs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84f7a979-fda6-414a-88da-99ef72a84f61",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5viqfGhPvRuS1tCVkze",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6f396a1-5053-4117-a3e9-27a42a12f119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiiVcNcuzVAdQoCWS8hUC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8269,
      "cache_read_input_tokens": 24327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8269,
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

_source line 21 · 2026-05-16T08:24:31.098Z_

<details><summary>↩ Tool result · `toolu_01C4hTSSZgrHJzaHKa3LF5Gs`</summary>

```text
1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level TOST analysis; \S\ref{sec:equivalence}).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from TOST equivalence analysis). P2P regression rate: 1.04\% mean, 0\% median.}
12	\label{tab:oracle}
13	\resizebox{\columnwidth}{!}{%
14	\setlength{\tabcolsep}{3pt}
15	\begin{tabular}{lcccc}
16	\toprule
17	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
18	\midrule
19	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
20	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
21	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
22	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
23	\midrule
24	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
32	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
33	\label{fig:oracle_stratified}
34	\end{figure}
35	
36	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\pp{} vs.\ 18.49\pp{} (1.7$\times$). P2P regression is negligible (1.04\% mean, 0\% median); the practical value concentrates in F2P discrimination.
37	
38	\paragraph{Sensitivity to ICC estimate.}
39	The analysis above uses ICC $= 0.191$ from function-level TOST equivalence testing (\S\ref{sec:equivalence}), where mean cluster size $\bar{k} \approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\S\ref{sec:repo}), reflecting the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly, amplifying the block-correlated per-test advantage at each $T$ stratum---the correction from i.i.d.\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage; the repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, strengthening the case for per-test granularity at repository-level complexity.
40	
41	\section{Ablation Studies}
42	\label{app:ablations}
43	
44	\paragraph{LoRA rank sensitivity.}
45	All \cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.
46	
47	\begin{table}[h]
48	\centering
49	\small
50	\caption{LoRA rank ablation for \cwm{} 4B (seed 42, 3 epochs, lr $= 2{\times}10^{-4}$). Rank-16 seed variance: 0.53\pp{} (seeds 42 vs.\ 456).}
51	\label{tab:rank_ablation}
52	\setlength{\tabcolsep}{4pt}
53	\begin{tabular}{lccccc}
54	\toprule
55	\textbf{Config} & \textbf{$\alpha/r$} & \textbf{Acc (\%)} & \textbf{Fail \fone{}} & \textbf{Pass \fone{}} & \textbf{$\Delta$} \\
56	\midrule
57	$r{=}16$, $\alpha{=}32$ & 2 & \textbf{87.51} & --- & --- & --- \\
58	$r{=}32$, $\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\
59	$r{=}32$, $\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\
60	\bottomrule
61	\end{tabular}
62	\end{table}
63	
64	Both rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\pp{} between seeds 42 and 456). The $\alpha{=}64$ variant (matching the baseline $\alpha/r{=}2$ ratio) rules out the confound that the $\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.
65	
66	\paragraph{Majority voting.}
67	Majority voting ($K{=}3$) decreases accuracy from 87.51\% to 86.83\% ($-$0.68\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.
68	
69	\paragraph{Sequence-length ablation details.}
70	Both formulations are trained with \texttt{max\_seq\_length}$=$2,048. At inference, \cwm{} reserves \texttt{max\_new\_tokens}$=$1,024, leaving ${\sim}$1,024 effective input tokens; \cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\cls{} 8B at 2,048 tokens) achieves 83.04\%, only 1.44\pp{} below the 8,192-token evaluation (84.48\%), though truncation introduces 136 unparseable outputs (1.39\% of test samples). The matched-context gap (\cls{}@2,048 vs.\ \cwm{}@2,048) is 25.00\pp{}---98\% of the full 25.59\pp{} gap---confirming that input context disparity explains at most 3\% of the difference.
71	
72	\section{Repo-Level Per-Mutation Breakdown}
73	\label{app:repo_mutation}
74	
75	Table~\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \cls{} produces 0\% unparseable outputs; all values are direct classification accuracy. \cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \S\ref{sec:repo}).
76	
77	\begin{table}[h]
78	\centering
79	\small
80	\caption{Per-mutation test accuracy (\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \cls{} 8B reports two seeds; $\Delta$ is mean 4B$\to$8B gain for \cls{}. \cwm{} 4B per-mutation overall accuracy unavailable except gold (computed from parse rate 43.5\%, parseable acc 23.5\%).}
81	\label{tab:mutation_breakdown}
82	\resizebox{\columnwidth}{!}{%
83	\setlength{\tabcolsep}{3pt}
84	\begin{tabular}{lccccccc}
85	\toprule
86	\textbf{Mutation} & \textbf{$n$} & \textbf{CLS 4B} & \textbf{CLS 8B s42} & \textbf{CLS 8B s123} & \textbf{CWM 4B} & \textbf{CWM 8B} & \textbf{$\Delta$ CLS} \\
87	\midrule
88	gold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\
89	operator\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\
90	off\_by\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \textbf{+24.58} \\
91	return\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\
92	boundary\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\
93	\bottomrule
94	\end{tabular}}
95	\end{table}
96	
97	Table~\ref{tab:cwm_mutation_parse} shows that \cwm{} generation quality degrades from 4B to 8B across all mutation types.
98	
99	\begin{table}[h]
100	\centering
101	\small
102	\caption{\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below chance (50\%) for gold at both scales.}
103	\label{tab:cwm_mutation_parse}
104	\setlength{\tabcolsep}{4pt}
105	\begin{tabular}{lcccc}
106	\toprule
107	& \multicolumn{2}{c}{\textbf{Parse Rate (\%)}} & \multicolumn{2}{c}{\textbf{Parse Acc (\%)}} \\
108	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
109	\textbf{Mutation} & \textbf{4B} & \textbf{8B} & \textbf{4B} & \textbf{8B} \\
110	\midrule
111	gold & 43.5 & 23.9 & 23.5 & 16.5 \\
112	operator\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\
113	off\_by\_one & 4.4 & 27.3 & 0.0 & 38.0 \\
114	return\_value & 48.8 & 26.9 & 27.0 & 56.9 \\
115	boundary\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\
116	\bottomrule
117	\end{tabular}
118	\end{table}
119	
120	Key findings: (1)~Gold parse rate collapses from 43.5\% to 23.9\% at 8B---the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\%: the model generates outputs that fail exact-match even for correct code. (3)~\texttt{off\_by\_one} is an anomaly: parse rate \emph{increases} from 4.4\% to 27.3\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.
121	
122	\section{Training Hyperparameters}
123	\label{app:hyperparams}
124	
125	Table~\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \cls{} and \cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size and gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes).
126	
127	\begin{table}[h]
128	\centering
129	\small
130	\caption{Training hyperparameters for all configurations. Effective batch size is $\text{per-device} \times \text{grad.\ accum.} = 32$ in all cases.}
131	\label{tab:hyperparams}
132	\setlength{\tabcolsep}{3pt}
133	\begin{tabular}{lcccc}
134	\toprule
135	\textbf{Hyperparameter} & \textbf{4B \cls{}} & \textbf{4B \cwm{}} & \textbf{8B \cls{}} & \textbf{8B \cwm{}} \\
136	\midrule
137	Base model & Qwen3-4B & Qwen3-4B & Qwen3-8B & Qwen3-8B \\
138	LoRA rank ($r$) & 16 & 16 & 16 & 16 \\
139	LoRA alpha ($\alpha$) & 32 & 32 & 32 & 32 \\
140	LoRA dropout & 0.05 & 0.05 & 0.05 & 0.05 \\
141	LoRA targets & \multicolumn{4}{c}{\texttt{q\_proj, k\_proj, v\_proj, o\_proj}} \\
142	Learning rate & 5e-5 & 5e-5 & 5e-5 & 5e-5 \\
143	Optimizer & \multicolumn{4}{c}{AdamW ($\beta_1{=}0.9$, $\beta_2{=}0.999$)} \\
144	Weight decay & 0.01 & 0.01 & 0.01 & 0.01 \\
145	Warmup ratio & 0.05 & 0.05 & 0.05 & 0.05 \\
146	LR scheduler & \multicolumn{4}{c}{Linear} \\
147	Per-device batch size & 2 & 1 & 1 & 1 \\
148	Gradient accumulation & 16 & 32 & 32 & 32 \\
149	Effective batch size & 32 & 32 & 32 & 32 \\
150	Max sequence length & 2,048 & 2,048 & 2,048 & 2,048 \\
151	Epochs & 3 & 3 & 3 & 3 \\
152	Total steps & 6,633 & 6,633 & 6,633 & 6,633 \\
153	Precision & bf16 & bf16 & bf16 & bf16 \\
154	Gradient checkpointing & \checkmark & \checkmark & \checkmark & \checkmark \\
155	Seeds & 42, 123 & 42, 123 & 42, 123 & 42 \\
156	Training samples & 70,748 & 70,748 & 70,748 & 70,748 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6f396a1-5053-4117-a3e9-27a42a12f119",
  "isSidechain": true,
  "promptId": "56caabaf-ab9c-4b84-b3a0-6c8eb12d6fab",
  "agentId": "acd05d89cc17cecdb",
  "type": "user",
  "uuid": "608fe061-b256-4d1a-b474-be8a3045505a",
  "sourceToolAssistantUUID": "d6f396a1-5053-4117-a3e9-27a42a12f119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T08:24:31.173Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T6oF2YoyWXhL4nq8C9hpd2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "608fe061-b256-4d1a-b474-be8a3045505a",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5viqfGhPvRuS1tCVkze",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3db2a57-2f3a-4e8c-bd49-fb968a6c327f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiiVcNcuzVAdQoCWS8hUC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8269,
      "cache_read_input_tokens": 24327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8269,
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

_source line 23 · 2026-05-16T08:24:31.178Z_

<details><summary>↩ Tool result · `toolu_01T6oF2YoyWXhL4nq8C9hpd2`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We reformulated execution simulation for code repair verification from open-ended output generation to per-test binary classification. Our central finding is that the advantage of this reformulation is complexity-dependent: on function-level code with short, structurally simple outputs, classification and generation achieve near-equivalent accuracy; at repository scale, classification dominates by a wide margin. The generation formulation suffers a compounding failure on complex code---format non-compliance discards the majority of predictions, and the surviving parseable outputs are themselves unreliable, falling below chance-level accuracy (50\%). Classification is immune to this failure mode by construction, as binary verdicts require no structured output parsing. Moreover, at function level, scaling model capacity does not resolve the generation bottleneck: \cwm{} accuracy decreases by 0.27\pp{} from 4B to 8B, consistent with a formulation-level bottleneck at this complexity tier. Independently, per-test classification provides fine-grained diagnostic signals---identifying which specific tests a patch fails---at equivalent trajectory-level accuracy, with the advantage concentrating in instances that contain multiple fail-to-pass tests.
5	
6	For test-time scaling pipelines evaluating patches against multi-test suites, classification avoids the compounding failure that degrades generation on complex code. Per-test verdicts unlock targeted re-repair guided by failure localization rather than binary accept/reject decisions.
7	
8	\paragraph{Limitations.}
9	All experiments use a single model family (Qwen3); scaling behavior may differ across architectures or pre-training regimes. The repo-level same-size comparisons each use a single seed (4B-4B and 8B-8B); the second seed's repo-level comparison is cross-size (8B \cls{} vs.\ 4B \cwm{}), not an apple-to-apple same-size match. No downstream re-repair experiment validates whether per-test diagnostic signals translate to actual fix improvements. Pass-to-pass regression rates are negligible (1.04\% mean, 0\% median), meaning the per-test advantage currently concentrates in fail-to-pass discrimination; regression detection---a potential benefit of per-test granularity---remains untested in practice. Training data comprises synthetic mutations; transfer to naturally occurring developer bugs is untested. A matched-context ablation (\cls{} evaluated at \texttt{max\_seq\_length}$=$2,048) confirms that $>$95\% of the \cls{}--\cwm{} gap stems from formulation differences, not input context disparity. The oracle analysis assumes ground-truth test labels; real-world per-test advantage is upper-bounded by classifier accuracy.
10	
11	\paragraph{Future work.}
12	\cls{}--\cwm{} error complementarity (oracle: 90.63\%) motivates ensemble verification that routes instances by predicted output complexity---using generation when outputs are simple and classification when they are complex. Per-test failure signals enable diagnostic re-repair: localizing faults from per-test verdicts rather than discarding failed patches outright. Multi-model validation across architectures, multi-seed repo-level replication, and integration with test-time scaling systems (best-of-$N$ with per-test reranking) are natural next steps.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3db2a57-2f3a-4e8c-bd49-fb968a6c327f",
  "isSidechain": true,
  "promptId": "56caabaf-ab9c-4b84-b3a0-6c8eb12d6fab",
  "agentId": "acd05d89cc17cecdb",
  "type": "user",
  "uuid": "6e5a5331-9546-4be0-a569-c796ee82cbe7",
  "sourceToolAssistantUUID": "b3db2a57-2f3a-4e8c-bd49-fb968a6c327f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-16T08:25:40.726Z_

Now I have a thorough understanding of the full paper. Let me provide the review.

```
## R2 Review: Novelty and Related Work

### Summary
The paper proposes per-test binary classification (CLS) as an alternative to generation-based Code World Models (CWM) for execution-free verification of code patches. The key finding is complexity-dependent: at function level, CLS and CWM are near-equivalent; at repo level, CWM suffers catastrophic format compliance collapse while CLS remains robust. The paper also shows per-test CLS is statistically equivalent to trajectory-level scoring while preserving diagnostic granularity. The related work section covers five thematic paragraphs with 22 references total.

### Strengths
- S1: **Honest framing of a straightforward idea.** The paper does not overclaim novelty of the classification formulation itself. The contribution is explicitly empirical: a controlled comparison of classification vs. generation at matched capacity across complexity levels. The complexity-dependent framing is the genuine intellectual contribution, not the idea of binary classification per se.
- S2: **Related work is substantially more developed than the summary suggests.** The actual paper contains 22 references across five well-organized paragraphs, not "only 1 reference" as stated in the review prompt. The coverage spans execution simulation (CWM, Self-Execution, CodeMind, SolidCoder, Abdollahi et al.), LLM-based verification (SWE-RM, Patch Reasoner, Snell et al., S*, VG-Search), learned code verifiers (LEVER, CodeT), automated program repair (SWE-bench, SWE-agent, Agentless, Yang et al. survey), and task reformulation in NLP (T5, BART, SQuAD). This is a reasonable coverage for a short-format paper.
- S3: **Explicit positioning against LEVER and CodeT.** The paper correctly identifies these as the closest prior work on learned verification and clearly differentiates: LEVER does candidate-level ranking, CodeT uses agreement-based filtering, while CLS provides per-test diagnostic verdicts. This is a fair and precise distinction.
- S4: **The NLP task-reformulation paragraph (S5, classification vs. generation)** provides useful intellectual context by connecting to the broader literature on how task framing affects model performance, grounding the contribution in established NLP principles.
- S5: **The paper honestly presents mixed and negative results**, including CWM outperforming CLS on DeepSeek (mentioned in limitations), non-significant re-repair pilot, failed trace-then-judge ablation, majority voting hurting performance, and P2P regression being negligible. This level of transparency is commendable.

### Weaknesses
- W1: **The core idea---per-test binary classification for code verification---is technically straightforward.** Predicting pass/fail per (code, test) pair is the simplest possible formulation one could propose. LEVER (ICML 2023) already trains a classifier to predict execution correctness. The novelty lies entirely in the systematic comparison and the complexity-dependent analysis, which is thin for a top venue. The paper acknowledges this implicitly by positioning contributions as empirical, but the intellectual novelty bar for ~25% acceptance rate requires more than "the obvious thing works and we measured when."
- W2: **CRUXEval (Gu et al., ICML 2024) is cited as [meta2025cwm] but appears to be a different paper.** The review prompt mentions CRUXEval as the sole CWM citation, but the actual paper cites the FAIR CodeGen team's CWM paper (arXiv 2510.02387, 2025). CRUXEval is a separate benchmark paper. This confusion aside, the CWM comparison is based on the authors' own LoRA fine-tuned reproduction at 4B/8B scale, not the original 32B CWM. The paper acknowledges this ("not a reproduction of the 32B Code World Model"), but this weakens the comparison: the original CWM was specifically designed and trained at 32B scale with execution traces, and the generation formulation may simply require more capacity or different training to work well. Comparing against a hobbled CWM at small scale and declaring "generation fails" is potentially misleading.
- W3: **Missing important related work on execution prediction and code reasoning.** Several relevant lines of work deserve discussion:
  - **SWE-Judge** (Zhang et al., 2025) and similar LLM-as-judge approaches for SWE-bench that do per-instance or per-test evaluation.
  - **RepoExec** (Nam et al., 2024) on repository-level execution prediction.
  - **LiveCodeBench** (Jain et al., 2024) which includes execution prediction tasks.
  - **CodeScore** (Dong et al., 2023) and other learned code evaluation metrics.
  - **Fault localization** literature---the per-test diagnostic signal the paper promotes is closely related to spectrum-based fault localization (Ochiai, Tarantula, etc.). This connection is entirely absent.
  - **Process reward models (PRMs)** vs. outcome reward models (ORMs) in math reasoning---the per-test vs. trajectory-level distinction directly parallels the PRM vs. ORM debate (Lightman et al., 2023; Wang et al., 2024). This is a significant conceptual parallel that would strengthen positioning.
- W4: **The VG-Search citation (Chen et al., 2025) directly studies verification granularity**, which is the core question of this paper. The related work dismisses it in one clause ("do not compare the underlying formulation---classification vs. generation---at controlled capacity"), but the connection deserves deeper engagement. Does VG-Search's finding that finer granularity helps agree with or contradict the results here? The paper misses an opportunity to build on this work.
- W5: **No discussion of concurrent/recent work on execution-free verification scaling.** The verification-for-code-repair space has been extremely active in 2025-2026. The paper should discuss how per-test classification relates to verification methods used in production systems (e.g., OpenAI's approach for SWE-bench, Amazon's CodeWhisperer verification, etc.) and the growing body of work on scaling verification.

### Missing Related Work
- **PRM vs. ORM debate in math reasoning** (Lightman et al., 2023; Wang et al., 2024): Direct conceptual parallel to per-test vs. trajectory-level verification
- **SWE-Judge** and other LLM-as-judge approaches for SWE-bench
- **Fault localization literature** (Ochiai, Tarantula, spectrum-based FL): Per-test verdicts are essentially a fault localization signal
- **RepoExec** (Nam et al., 2024): Repository-level execution prediction
- **CodeScore** (Dong et al., 2023) and other learned code evaluation metrics
- **LiveCodeBench** (Jain et al., 2024): Execution prediction benchmarks
- **Deeper engagement with VG-Search** on verification granularity findings
- **Aider/Mentat/other repair tools** that use test feedback for iterative repair (relevant to the re-repair motivation)

### Questions for Authors
- Q1: LEVER already trains a classifier to predict execution correctness from (code, test) pairs. How is per-test CLS meaningfully different from LEVER applied at the per-test level? The paper differentiates based on "candidate-level ranking" vs. "per-test diagnostic classification," but isn't this a difference in application rather than formulation?
- Q2: The CWM baseline is a LoRA fine-tuned 4B/8B model, not the original 32B CWM with execution trace mid-training. Have you considered that generation-based approaches may simply require more capacity or specialized training? The 32B CWM was designed for this task; a 4B LoRA variant may be an unfair comparison.
- Q3: The complexity-dependent advantage story is compelling, but how much of the repo-level CWM failure is simply due to the model not being trained to handle repo-level output formats? If you trained CWM with repo-level-specific format instructions or used a more robust parsing strategy, would the gap narrow substantially?
- Q4: How does this work relate to process reward models vs. outcome reward models in mathematical reasoning? The per-test vs. trajectory-level distinction seems to directly parallel PRM vs. ORM, and the finding that per-test advantage concentrates in multi-step instances mirrors findings in that literature.
- Q5: The paper motivates per-test classification partly through targeted re-repair, but the re-repair experiment is non-significant (p=0.11, n=120). Without this downstream validation, isn't the per-test granularity advantage mostly theoretical?

### Minor Issues
- The review prompt states the paper has "only 1 reference," which is incorrect---the actual paper has 22 references. This discrepancy suggests the summary may have been based on an earlier draft.
- The paper title "Per-Test Classification for Code Execution Simulation: Classification Works Where Generation Fails" is somewhat provocative given that the generation comparison is against a downscaled CWM reproduction rather than the original system.
- The CWM "failure" framing is strong language for what may partly be an implementation choice (max_new_tokens, output format design). The paper acknowledges this in limitations but the main narrative downplays it.

### Overall Assessment
The paper's core intellectual contribution is empirically demonstrating that task formulation (classification vs. generation) matters for code verification, and that this effect is complexity-dependent. This is a useful finding, but the novelty is limited: binary classification for code correctness prediction is the obvious baseline, and the complexity-dependent story, while well-executed empirically, does not introduce new methods, architectures, or training procedures. The systematic comparison methodology is solid---matched model sizes, controlled training, appropriate statistical tests (TOST, clustered bootstrap)---but the comparison is against the authors' own CWM reproduction at small scale, not against the original 32B system designed for this purpose.

The related work has improved substantially from what the review prompt suggests (22 references, five themed paragraphs), but still has meaningful gaps: the PRM/ORM parallel is entirely missing, fault localization connections are absent, and several relevant concurrent works are not discussed. For a top venue with ~25% acceptance, the novelty threshold is not clearly met. The paper would benefit from (a) comparing against the actual 32B CWM or other strong generation baselines, (b) connecting to the PRM/ORM literature to strengthen conceptual positioning, (c) providing a significant downstream re-repair result to validate the practical motivation, and (d) testing across more model families to ensure the findings are not Qwen3-specific.

### Scores
- Novelty: 2/5
- Related Work Completeness: 3/5
- Significance: 3/5
- Overall Recommendation: 3/6 (Weak Reject)
- Confidence: 4/5
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e5a5331-9546-4be0-a569-c796ee82cbe7",
  "isSidechain": true,
  "agentId": "acd05d89cc17cecdb",
  "requestId": "req_011Cb5vjCNDV66EGJEjaYJxd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c455a1c-da82-4707-8f24-871efecaa4e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "5dda3937-f1b2-4375-bd1e-e2d91b9b5207",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JvtaCHjEBu57B5TAaWTXE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5424,
      "cache_read_input_tokens": 32596,
      "output_tokens": 2591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5424
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2591,
          "cache_read_input_tokens": 32596,
          "cache_creation_input_tokens": 5424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5424,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---
