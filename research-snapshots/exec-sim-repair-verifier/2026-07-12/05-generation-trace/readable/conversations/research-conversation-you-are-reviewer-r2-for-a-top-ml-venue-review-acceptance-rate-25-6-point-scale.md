# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-afc382ce2eacaa3da.jsonl`
- **Structured JSON:** [`bbc04f5529c80f4c7c81.json`](../../sessions/bb/bbc04f5529c80f4c7c81.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-17T04:02:10.893Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **novelty, significance, positioning against related work, and writing quality**.

## Paper Summary

Title: "The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study"

The paper compares three formulations for execution-free code verification:
- CLS (per-test binary classification)
- CWM (code world model / generation-based)  
- TRAJ (trajectory-level scoring)

Trained with identical LoRA configs on matched 8B models from Qwen3 and DeepSeek-R1-Qwen3 families, evaluated at function-level and repository-level complexity.

**4 claims:**
1. All formulations achieve equivalent accuracy at function-level (86.8%–90.5%)
2. At repo-level, CWM effectiveness is model-contingent (Qwen3: 53–93% unparseable vs DeepSeek: 13%)
3. Per-test CLS matches TRAJ accuracy with diagnostic granularity at 6–9× lower inference cost
4. CLS diagnostics enable re-repair: +13.3pp resolve rate (p=0.031, McNemar, n=60)

## Introduction Structure

Para 1: LLMs generate patches but verifying without execution is open problem. Three formulations exist (CLS, CWM, TRAJ) with different trade-offs never quantified.
Para 2: Absence of systematic comparison creates practical confusion. CWM only shown on function-level. TRAJ sacrifices localization. CLS not compared to generation under matched conditions.
Para 3: We address this with controlled study: identical LoRA, matched 8B models from 2 families, 2 complexity levels, multiple seeds.
Para 4: Key insight: formulation effectiveness depends on task complexity × model/tokenizer interaction. CWM failure is tokenizer-specific (engineering problem, not formulation weakness).
Para 5: Beyond characterization, CLS diagnostics have downstream value for re-repair (+13.3pp).
Para 6: Contribution list (4 bullets).

## Related Work (3 paragraphs)

1. **Execution-Free Code Verification**: LEVER, CodeT, CWM (CRUXEval), SWE-RewardBench. Claims "first controlled comparison across formulation families."
2. **Process vs. Outcome Supervision**: Lightman et al. (PRM), Uesato et al. Parallel to CLS-vs-TRAJ.
3. **Verification-Guided Code Repair**: CodeRL, AlphaCode, Reflexion. All assume execution availability; this paper uses predicted diagnostics.
4. **Predictive Mutation Testing**: Zhang et al. 2018. Precedent for per-test binary classification.

## References (10 total)
- Chen et al. 2023 (CodeT)
- Gu et al. 2024 (CRUXEval)
- Le et al. 2022 (CodeRL)
- Li et al. 2022 (AlphaCode)
- Lightman et al. 2023 (PRM)
- Ni et al. 2023 (LEVER)
- Shinn et al. 2023 (Reflexion)
- Uesato et al. 2022
- Zhang et al. 2018 (Predictive Mutation Testing)
- Zhang et al. 2025 (SWE-RewardBench)

## Method (Section 3)
Problem formulation (CLS/CWM/TRAJ definitions), experimental design (models, training, complexity levels, evaluation protocol), dataset construction (SWE-bench-PerTest), re-repair protocol (5 conditions).

## Discussion (Section 5)
Practical guidance (4 recommendations), tokenizer engineering implication, limitations (4-8B models, 60-200 instances, CWM may benefit from scale).

## Conclusion
Single paragraph summarizing findings.

## Full Paper Text for Writing Quality Assessment

Abstract (word count ~180):
"Execution-free verification of code repairs can be formulated as per-test binary classification (CLS), execution output generation (CWM), or trajectory-level scoring (TRAJ), yet no controlled comparison exists across these formulations. We present the first systematic study holding model capacity, training data, and compute constant, evaluating two model families (Qwen3 and DeepSeek-R1-Qwen3) at two complexity levels (function-level and repository-level) across multiple seeds. We establish four findings: (1) all three formulations achieve statistically equivalent accuracy at function-level (86.8%–90.5%), making formulation choice irrelevant at low complexity; (2) at repository-level, CWM effectiveness is model-contingent, with Qwen3 exhibiting 53–93% unparseable outputs while DeepSeek maintains only 13%, demonstrating that CWM failure is tokenizer-specific rather than formulation-inherent; (3) per-test CLS matches trajectory-level accuracy while providing diagnostic granularity at 6–9× lower inference cost; and (4) CLS-derived per-test diagnostics enable targeted re-repair, improving resolve rates by 13.3 percentage points over uninformed baselines (p = 0.031, McNemar test, n = 60). Our results provide actionable guidance for practitioners choosing among verification formulations and demonstrate that diagnostic granularity translates to downstream repair utility."

## Your Review Task

Evaluate the following aspects:

1. **Novelty and Significance**: Is "controlled comparison of verification formulations" a genuine contribution? Is this incremental or does it provide new insights? Would this change how people build systems?
2. **Related Work Coverage**: Are key references missing? Is the positioning fair to prior work (especially CWM/CRUXEval)? Only 10 references — is this sufficient?
3. **Framing and Narrative**: Is the story compelling? Does the Introduction motivate the problem well? Is the "design space characterization" framing effective?
4. **Writing Quality**: Check for AI-style markers (excessive dashes, -ing phrases, transition word overuse, etc.). Is the prose clear and concise?
5. **Claim Novelty**: Are the claims genuinely new or could they be predicted from prior work?
6. **Broader Impact and Limitations**: Are limitations honestly stated? Are there unstated ones?
7. **Paper Structure**: Is anything missing that a top venue would expect (e.g., appendix, error analysis, qualitative examples)?

Provide your output as:
```
## R2 Review: Novelty & Related Work

### Summary
[2-3 sentences]

### Strengths
[Bulleted list, 4-6 items]

### Weaknesses
[Bulleted list, 4-8 items, each with specific detail]

### Questions for Authors
[3-5 specific questions]

### Related Work Gaps
[Missing citations or positioning issues]

### Writing Quality Issues
[Specific examples of problematic writing patterns]

### Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "afc382ce2eacaa3da",
  "type": "user",
  "uuid": "fd89546a-d368-4500-be04-1ef505794a71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T04:02:10.897Z_

```json
{
  "parentUuid": "fd89546a-d368-4500-be04-1ef505794a71",
  "isSidechain": true,
  "agentId": "afc382ce2eacaa3da",
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
  "uuid": "c4767d17-c4da-472a-afc9-ea466c8147f3",
  "timestamp": "2026-05-17T04:02:10.897Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-17T04:02:15.626Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ChgtE4DQYn7vn6nHU5XBaZ`</summary>

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
  "parentUuid": "c4767d17-c4da-472a-afc9-ea466c8147f3",
  "isSidechain": true,
  "agentId": "afc382ce2eacaa3da",
  "requestId": "req_011Cb7UXpZDWRadNTu4cU8Sf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eff18dae-b218-4681-840f-d82f5c8aeef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjgD4eeYN1zMXMqiifKwYf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8825,
      "cache_read_input_tokens": 8972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8825,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 4 · 2026-05-17T04:02:15.647Z_

<details><summary>↩ Tool result · `toolu_01ChgtE4DQYn7vn6nHU5XBaZ`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a controlled comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question.
7	
8	We present the first systematic comparison of these three formulations across two model families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our central finding is that \emph{formulation effectiveness is complexity-dependent and model-contingent}: at function-level complexity, all three formulations achieve statistically equivalent accuracy regardless of model family; at repository-level complexity, formulations diverge sharply, with the magnitude and direction of divergence depending on model and tokenizer properties rather than formulation design alone. Figure~\ref{fig:reformulation} illustrates the three formulations.
9	
10	We make the following contributions:
11	
12	\begin{itemize}[leftmargin=*,itemsep=2pt]
13	\item \textbf{Formulation equivalence at low complexity.} On function-level benchmarks, \cls{}, \cwm{}, and \traj{} achieve near-identical accuracy across two model families (Qwen3-4B: 88.4/87.2/86.3\%, 5 seeds; DeepSeek-6.7B: 86.9/86.8\%, 2 seeds). The \cls{}--\cwm{} gap is 0.02--1.24\pp{}, within seed noise in both cases. This null result establishes that classification is not inherently easier than generation when execution outputs are short and structured.
14	
15	\item \textbf{Complexity-dependent divergence.} At repository-level complexity with Qwen3, \cls{} achieves 19--26\pp{} higher accuracy than \cwm{} (4B: 25.59\pp{}; 8B: 19.31\pp{}), driven by format compliance collapse: 54--74\% of \cwm{} outputs are unparseable, and parseable-only accuracy degrades from 42.9\% (4B) to 38.5\% (8B). Whether this divergence generalizes across model families or is tokenizer/model-specific is under investigation (DeepSeek repo-level results pending). Both outcomes are informative: consistency would confirm complexity as the primary moderator; divergence would identify model properties as a critical design variable.
16	
17	\item \textbf{Error complementarity and ensemble potential.} \cls{} and \cwm{} exhibit systematically opposite error patterns at function level: \cls{} over-predicts passing (75.5\% of errors are false negatives) while \cwm{} over-predicts failure (83.1\% false positives). An oracle ensemble achieves 90.63\% (+3.12\pp{} over the best single formulation), suggesting that the formulations capture complementary aspects of code behavior.
18	
19	\item \textbf{Diagnostic granularity at equivalent accuracy.} Per-test classification achieves statistically equivalent variant-level accuracy to trajectory-level scoring (TOST equivalence $p = 0.007$, $\pm$2\pp{} margin) while providing per-test diagnostic signals at 217$\times$ higher throughput than generation (1 output token vs.\ avg 477). This enables failure localization without accuracy or efficiency cost relative to coarser formulations.
20	\end{itemize}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eff18dae-b218-4681-840f-d82f5c8aeef5",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "afc382ce2eacaa3da",
  "type": "user",
  "uuid": "4ac47a90-e881-4d8b-aa52-7823efbc1a59",
  "sourceToolAssistantUUID": "eff18dae-b218-4681-840f-d82f5c8aeef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T04:02:16.123Z_

<details open><summary>🔧 Tool call — Read · `toolu_013V7FaY29NRKSC5eMThBXe4`</summary>

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
  "parentUuid": "4ac47a90-e881-4d8b-aa52-7823efbc1a59",
  "isSidechain": true,
  "agentId": "afc382ce2eacaa3da",
  "requestId": "req_011Cb7UXpZDWRadNTu4cU8Sf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c8db941-2073-40f2-a09e-d17d8e12b4ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjgD4eeYN1zMXMqiifKwYf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8825,
      "cache_read_input_tokens": 8972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8825,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 6 · 2026-05-17T04:02:16.129Z_

<details><summary>↩ Tool result · `toolu_013V7FaY29NRKSC5eMThBXe4`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation for Code.}
5	Code World Models~\cite{meta2025cwm} mid-train a 32B LLM on execution traces to predict output strings, establishing the generation-based paradigm for execution-free verification.
6	Self-Execution~\cite{maimon2026selfexecution} extends this with step-by-step trace prediction.
7	CodeMind~\cite{liu2024codemind} evaluates code reasoning along multiple dimensions including execution prediction.
8	SolidCoder~\cite{lee2026solidcoder} bridges mental simulation and actual execution via concrete feedback.
9	Abdollahi et al.~\cite{abdollahi2025demystifying} identify systematic failure modes in LLM trace prediction, including position-dependent errors.
10	All share a generation formulation whose cost scales with output length. We provide the first controlled comparison of this formulation against classification and trajectory-level alternatives at matched model capacity, revealing that generation reliability is contingent on both code complexity and model/tokenizer properties.
11	
12	\paragraph{LLM-based Verification for Code Repair.}
13	SWE-RM~\cite{shum2025swerm} trains a trajectory-level reward model for patch ranking without execution.
14	Patch Reasoner~\cite{xu2025patchreasoner} uses chain-of-thought reasoning for patch verification.
15	Snell et al.~\cite{snell2024scaling} show that test-time scaling via verification outperforms parameter scaling.
16	S*~\cite{li2025sstar} combines execution-grounded selection with model-based scoring.
17	VG-Search~\cite{chen2025vgsearch} finds that finer-grained verification improves selection efficiency.
18	These works treat verification granularity as a design choice but do not compare the underlying formulation (classification vs.\ generation) at controlled capacity. We provide this comparison, finding that the granularity choice interacts with complexity level.
19	
20	\paragraph{Process vs.\ Outcome Supervision.}
21	Lightman et al.~\cite{lightman2023letsverify} demonstrate that process-based reward models (verifying each reasoning step) outperform outcome-based models (verifying only the final answer) for mathematical reasoning.
22	Uesato et al.~\cite{uesato2022solving} show similar advantages for process feedback in math word problems.
23	Our per-test classification is structurally analogous to process supervision: each test verdict corresponds to an intermediate verification step, while trajectory-level scoring corresponds to outcome supervision. Our finding that per-test and trajectory-level achieve equivalent accuracy (TOST $p = 0.007$) with per-test providing additional diagnostic value parallels the process supervision literature, where step-level verification enables error localization at no accuracy cost.
24	
25	\paragraph{Verification-in-the-Loop Repair.}
26	CodeRL~\cite{le2022coderl} trains a critic model to provide execution feedback for RL-based code generation.
27	AlphaCode~\cite{li2022alphacode} uses massive sampling with test-based filtering for competition programming.
28	Reflexion~\cite{shinn2023reflexion} uses verbal self-reflection on execution results to iteratively improve agent performance.
29	These systems demonstrate that verification quality is a primary bottleneck for iterative repair. Our comparison of verification formulations is complementary: the efficiency and diagnostic granularity of the verifier directly affects the viability of verification-in-the-loop approaches at scale.
30	
31	\paragraph{Learned Code Verifiers.}
32	LEVER~\cite{ni2023lever} trains a classifier to re-rank code candidates by predicting execution correctness.
33	CodeT~\cite{chen2023codet} uses dual execution agreement as a verification signal.
34	Both target execution-free deployment via classification-style training. Unlike candidate-level ranking, we provide per-test diagnostic verdicts and compare classification against generation on the same model, data, and compute budget, isolating the effect of task formulation.
35	
36	\paragraph{Automated Program Repair.}
37	SWE-bench~\cite{jimenez2024swebench} and SWE-bench Verified~\cite{chowdhury2024swebenchverified} provide standard benchmarks for repository-level repair.
38	SWE-agent~\cite{yang2024sweagent} uses tool-augmented agents; Agentless~\cite{xia2024agentless} demonstrates a simpler pipeline.
39	Yang et al.~\cite{yang2025aprsurvey} survey LLM-based repair, identifying verification as a persistent bottleneck.
40	These systems rely on execution-based validation, with cost scaling linearly in candidates. Per-test verification provides failure-localized signals that could support targeted re-repair.
41	
42	\paragraph{Predictive Mutation Testing.}
43	Predicting test outcomes for code mutations without execution has been studied in software engineering~\cite{tufano2019predictive,kim2022predictive}. Our per-test classification formulation shares this problem structure: given a code change (mutation/patch) and a test, predict pass or fail. We extend this line to LLM-based verification at repository scale, comparing it against alternative formulations (generation, trajectory-level) for the first time.
44	
45	\paragraph{Classification vs.\ Generation in NLP.}
46	Task framing affects model performance broadly: T5~\cite{raffel2020t5} and BART~\cite{lewis2020bart} demonstrate generation-classification tradeoffs under controlled capacity, while SQuAD~\cite{rajpurkar2016squad} shows that constraining output space can simplify tasks without sacrificing quality. We extend this lens to code verification, finding that code complexity moderates the tradeoff in a model-contingent manner.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c8db941-2073-40f2-a09e-d17d8e12b4ff",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "afc382ce2eacaa3da",
  "type": "user",
  "uuid": "5e2523ca-7d1b-49ce-99cb-32f20977ea41",
  "sourceToolAssistantUUID": "3c8db941-2073-40f2-a09e-d17d8e12b4ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T04:02:16.430Z_

<details open><summary>🔧 Tool call — Read · `toolu_014TeKews7jVdkbXhJe9CQKY`</summary>

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
  "parentUuid": "5e2523ca-7d1b-49ce-99cb-32f20977ea41",
  "isSidechain": true,
  "agentId": "afc382ce2eacaa3da",
  "requestId": "req_011Cb7UXpZDWRadNTu4cU8Sf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cfe5b3e-baed-4e64-ae21-772accabb6bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjgD4eeYN1zMXMqiifKwYf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8825,
      "cache_read_input_tokens": 8972,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8825
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 239,
          "cache_read_input_tokens": 8972,
          "cache_creation_input_tokens": 8825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8825,
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

_source line 8 · 2026-05-17T04:02:16.435Z_

<details><summary>↩ Tool result · `toolu_014TeKews7jVdkbXhJe9CQKY`</summary>

```text
1	\begin{abstract}
2	Execution-free verification for LLM-based code repair can be formulated in multiple ways, yet no controlled comparison exists across formulations at matched model capacity. We systematically evaluate three formulations: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring, training on identical data with controlled model sizes (4B, 8B).
3	
4	At function level, the three formulations achieve near-equivalent accuracy (\cls{} 88.43\% vs.\ \cwm{} 87.19\% at 4B, 5 seeds; TOST equivalence with trajectory-level at $p{=}0.007$). At repository level, formulation divergence amplifies to 19--26\pp{} (4B: 25.59\pp{}; 8B: 19.31\pp{}), with \cwm{} falling below majority baseline. However, this divergence is partially model-contingent: \cwm{} failures on Qwen3 concentrate in format non-compliance (unparseable rate 53.7\%$\to$73.8\% from 4B to 8B) rather than semantic prediction errors, and generation quality uniformly degrades with scale (parseable-only accuracy 42.9\%$\to$38.5\%). Whether this reflects a fundamental generation bottleneck or model-specific behavior remains open pending cross-model validation.
5	
6	Two findings generalize across conditions. First, per-test classification provides diagnostic granularity (which specific tests fail) at equivalent trajectory-level accuracy, with the advantage concentrating in instances with $\geq$2 failing tests (31\% of instances, 55\% of oracle advantage). Second, formulations exhibit complementary error patterns: an oracle ensemble reaches 90.63\%, motivating complexity-aware routing rather than a single universal formulation.
7	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cfe5b3e-baed-4e64-ae21-772accabb6bd",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "afc382ce2eacaa3da",
  "type": "user",
  "uuid": "0db880c0-dd6c-48bc-bdf5-2c9b32222104",
  "sourceToolAssistantUUID": "6cfe5b3e-baed-4e64-ae21-772accabb6bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T04:02:19.628Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QLmiCuhC7R7oBPT4RDGRvy`</summary>

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
  "parentUuid": "0db880c0-dd6c-48bc-bdf5-2c9b32222104",
  "isSidechain": true,
  "agentId": "afc382ce2eacaa3da",
  "requestId": "req_011Cb7UYEUtRZsuNrLkicEuq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f088cc5-329b-47da-bebd-537a099288e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpWeQHCHY53Vw7nzY1V3K3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4176,
      "cache_read_input_tokens": 17797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4176,
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

_source line 10 · 2026-05-17T04:02:19.640Z_

<details><summary>↩ Tool result · `toolu_01QLmiCuhC7R7oBPT4RDGRvy`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests, providing no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation has characteristic failure modes that differ in their sensitivity to code complexity:
21	
22	\paragraph{Generation failure modes (\cwm{}).} The open-ended output space introduces three failure modes: (1)~\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure due to truncation; (2)~\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; and (3)~\emph{format compliance collapse}, where the model fails to produce structured predictions entirely at high input complexity, even when the generation budget is sufficient. Under optimistic independence, a token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$, making long outputs exponentially harder to predict exactly. We adopt exact string matching following the original \cwm{} evaluation protocol~\citep{meta2025cwm}. Unparseable predictions default to the majority-class label (\textsc{Pass}).
23	
24	\paragraph{Classification failure modes (\cls{}).} The single-token output space eliminates format and truncation failures but constrains the model to encode its reasoning entirely within internal representations, without the intermediate reasoning trace that generation provides. \cls{} errors concentrate in false negatives (predicting \textsc{Pass} for failing tests), consistent with a bias toward the majority class.
25	
26	\paragraph{Trajectory-level failure modes (\traj{}).} By collapsing all per-test information into a single binary verdict, \traj{} discards diagnostic granularity. When a patch fails multiple tests, the trajectory-level formulation cannot identify \emph{which} tests fail. This limits downstream utility (e.g., targeted re-repair) but avoids per-test aggregation errors.
27	
28	\paragraph{Complexity dependence.} These failure modes suggest a complexity-dependent interaction: when execution outputs are short and structured (function-level code), generation modes (1)--(2) are rarely triggered, and all formulations should perform comparably. As output length and structural complexity increase (repository-level code), generation-specific failures may compound, creating divergence. Whether this divergence reflects a fundamental property of the generation formulation or is contingent on model/tokenizer properties is an empirical question we investigate in \S\ref{sec:experiments}.
29	
30	\subsection{Oracle Accuracy-Utility Framework}
31	\label{sec:oracle}
32	
33	Per-test granularity is valuable only when per-test predictions are sufficiently accurate and multiple tests provide partially independent signals. Consider a buggy patch with $k = |T_{\text{f2p}}|$ fail-to-pass tests. A per-test verifier with recall $r$ detects the bug if it identifies at least one failing test:
34	%
35	\begin{equation}
36	  P_{\text{detect}}(k) = 1 - (1 - r)^{k_{\text{eff}}}
37	  \label{eq:pdetect}
38	\end{equation}
39	%
40	where $k_{\text{eff}}$ is the effective number of independent tests. Let $a_h$ denote the trajectory-level detection accuracy; it is independent of $k$.
41	
42	\paragraph{Block-correlation model.} Per-test predictions within the same patch are correlated. We model this via the intraclass correlation coefficient $\rho$ \citep[ICC;][]{shrout1979icc}:
43	%
44	\begin{equation}
45	  k_{\text{eff}} = \frac{k}{1 + (k - 1)\rho}
46	  \label{eq:keff}
47	\end{equation}
48	%
49	When $\rho = 0$, $k_{\text{eff}} = k$ (full independence); when $\rho = 1$, $k_{\text{eff}} = 1$ (per-test collapses to trajectory-level). The per-test advantage relative to a trajectory-level baseline is $\Delta(k) = P_{\text{detect}}(k) - a_h$, and the expected population advantage is:
50	%
51	\begin{equation}
52	  \mathbb{E}[\Delta] = \sum_{k=1}^{K} P(|T_{\text{f2p}}| = k) \cdot \Delta(k)
53	  \label{eq:expected-advantage}
54	\end{equation}
55	
56	\paragraph{Testable predictions.} This yields three predictions validated in \S\ref{sec:experiments}: (1)~at $k = 1$, $\Delta \approx 0$; (2)~$\Delta(k)$ increases with $k$, dampened by $\rho > 0$; (3)~$\mathbb{E}[\Delta]$ concentrates in multi-F2P-test instances.
57	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f088cc5-329b-47da-bebd-537a099288e1",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "afc382ce2eacaa3da",
  "type": "user",
  "uuid": "c34f81bc-4665-4aca-a08d-ea73ff4c3410",
  "sourceToolAssistantUUID": "3f088cc5-329b-47da-bebd-537a099288e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T04:02:20.188Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VuePLXnKH9mr6P8Jsg1AXM`</summary>

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
  "parentUuid": "c34f81bc-4665-4aca-a08d-ea73ff4c3410",
  "isSidechain": true,
  "agentId": "afc382ce2eacaa3da",
  "requestId": "req_011Cb7UYEUtRZsuNrLkicEuq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adf980a5-773b-4829-afe7-b91a13e1042a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpWeQHCHY53Vw7nzY1V3K3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4176,
      "cache_read_input_tokens": 17797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4176,
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

_source line 12 · 2026-05-17T04:02:20.193Z_

<details><summary>↩ Tool result · `toolu_01VuePLXnKH9mr6P8Jsg1AXM`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two model families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench}.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with LoRA~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. For cross-model validation, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge.
15	
16	\paragraph{Statistics.}
17	Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); per-test vs.\ trajectory-level comparison uses TOST~\cite{schuirmann1987tost} ($\pm$2\pp{} margin). ICC~\cite{shrout1979icc} quantifies within-problem correlation. Oracle analysis uses SWE-bench Verified (500 instances).
18	
19	
20	\subsection{Function-Level: Formulation Equivalence}
21	\label{sec:func_results}
22	
23	Table~\ref{tab:main_results} reports function-level results across formulations and model families.
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
36	\multicolumn{4}{l}{\emph{Qwen3 (primary)}} \\
37	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
38	\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\pm$ 0.37 \\
39	TRAJ (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
40	\midrule
41	\multicolumn{4}{l}{\emph{DeepSeek-Coder (cross-model validation)}} \\
42	\cls{} (fine-tuned) & 6.7B & 2 & 86.85 $\pm$ 0.11 \\
43	\cwm{} (fine-tuned) & 6.7B & 2 & 86.83 $\pm$ 1.49 \\
44	\midrule
45	\multicolumn{4}{l}{\emph{Zero-shot baselines}} \\
46	ZS LLM-as-judge & 8B & 1 & 64.40 \\
47	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	All three formulations achieve comparable accuracy on Qwen3-4B: \cls{} 88.43\% ($\pm$0.78), \cwm{} 87.19\% ($\pm$0.37), \traj{} 86.30\% ($\pm$0.97). The \cls{}--\cwm{} gap of 1.24\pp{} is modest, within 1.6$\times$ of the seed standard deviation for \cls{}. DeepSeek-Coder-6.7B confirms this equivalence: \cls{} 86.85\% ($\pm$0.11) vs.\ \cwm{} 86.83\% ($\pm$1.49), a gap of 0.02\pp{} indistinguishable from zero. At this complexity level, execution outputs are short and structured, generation-specific failure modes (truncation, format compliance) are not triggered, and formulation choice does not meaningfully affect accuracy. Zero-shot baselines lag substantially (64.40\% at 8B, 71.69\% at 32B NF4), confirming that task-specific fine-tuning is necessary regardless of formulation. \cwm{} produces 0\% unparseable outputs at function level for both model families.
53	
54	\paragraph{Variance asymmetry.} \cwm{}'s higher seed variance on DeepSeek ($\sigma{=}1.49$ vs.\ \cls{} $\sigma{=}0.11$) mirrors the Qwen3 pattern (\S\ref{sec:analysis}, paragraph d): generation is more sensitive to initialization than classification, consistent with the output space being less constrained.
55	
56	
57	\subsection{Scaling Behavior}
58	\label{sec:scaling}
59	
60	Table~\ref{tab:scaling} compares \cls{} and \cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.
61	
62	\begin{table}[t]
63	\centering
64	\small
65	\caption{Model-size scaling: \cls{} vs.\ \cwm{} accuracy (\%) at 4B and 8B (Qwen3). Three matched seeds in full precision. The \cls{}--\cwm{} gap widens from 1.18\pp{} to 2.43\pp{}.}
66	\label{tab:scaling}
67	\setlength{\tabcolsep}{4pt}
68	\begin{tabular}{llccccc}
69	\toprule
70	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{s456} & \textbf{Mean} & \textbf{Gap} \\
71	\midrule
72	\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \multirow{2}{*}{1.18} \\
73	\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\
74	\midrule
75	\cls{} & 8B & \textbf{90.48} & 89.40 & 88.31 & \textbf{89.40} & \multirow{2}{*}{\textbf{2.43}} \\
76	\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\
77	\bottomrule
78	\end{tabular}
79	\end{table}
80	
81	At 4B, \cls{} and \cwm{} are separated by 1.18\pp{} on the matched three-seed subset. At 8B, the gap widens to 2.43\pp{} (Figure~\ref{fig:scaling_gap}). Clustered bootstrap yields a mean gap of 2.26\pp{} ($p = 0.0066$, 95\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.
82	
83	The two formulations scale differently: from 4B to 8B, \cls{} gains +0.99\pp{} (88.41 $\to$ 89.40) while \cwm{} loses $-$0.27\pp{} (87.23 $\to$ 86.96). Additional capacity benefits classification but provides no measurable improvement for generation, consistent with the hypothesis that string prediction, not model capacity, constrains \cwm{} at this complexity level. However, the \cwm{} regression ($-$0.27\pp{}) falls within seed noise (3-seed std ${\sim}$0.5\pp{}) and could reflect suboptimal hyperparameter transfer rather than a fundamental bottleneck. This scaling pattern is observed within Qwen3 only; whether it generalizes across model families at function level is not yet tested. At repository-level complexity, the interaction between formulation and scale is examined in \S\ref{sec:repo}.
84	
85	
86	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
87	\label{sec:equivalence}
88	
89	We compare \cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds. The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); the TOST equivalence test confirms statistical equivalence at $p = 0.007$ ($\pm$2\pp{} margin). Within-problem predictions are correlated (ICC $= 0.191$, $p < 0.0001$, DEFF $= 3.97$); all statistical tests use clustered bootstrap accordingly. Per-test classification provides diagnostic information (which specific tests fail) at no cost to variant-level accuracy, paralleling the finding in process supervision~\cite{lightman2023letsverify} that step-level verification enables error localization without degrading outcome-level performance.
90	
91	
92	\subsection{Accuracy-Utility Frontier}
93	\label{sec:oracle-results}
94	
95	Oracle analysis on SWE-bench Verified (500 instances) reveals that per-test advantage concentrates sharply: at $T = 1$ F2P tests (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T \geq 2$ (31.3\%), with $T = 2$ alone contributing 55.3\% of the total 10.93\pp{} block-correlated advantage. Pass-to-pass (P2P) regression is negligible (1.04\% mean, 0\% median), so the practical value concentrates in fail-to-pass discrimination. Full stratification and the i.i.d.\ vs.\ block-correlated comparison appear in Appendix~\ref{app:oracle}.
96	
97	
98	\subsection{Repo-Level: Complexity-Dependent Divergence}
99	\label{sec:repo}
100	
101	Table~\ref{tab:repo_level} compares \cls{} and \cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy; the test set ($n{=}9{,}784$) has zero problem overlap with validation. We report both overall accuracy (where unparseable outputs default to the majority class, pass) and parseable-only accuracy to disentangle generation quality from default assignment effects.
102	
103	\begin{table}[t]
104	\centering
105	\small
106	\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Parse Acc: accuracy computed only on parseable outputs. Unparseable \cwm{} outputs default to pass (majority class, 72.96\%).}
107	\label{tab:repo_level}
108	\resizebox{\columnwidth}{!}{%
109	\setlength{\tabcolsep}{3pt}
110	\begin{tabular}{llcccccc}
111	\toprule
112	\textbf{Method} & \textbf{Size} & \textbf{Seed} & \textbf{Acc (\%)} & \textbf{Macro \fone{}} & \textbf{Unparse (\%)} & \textbf{Parse Acc (\%)} & \textbf{vs Maj.\ (\pp{})} \\
113	\midrule
114	\cls{} & 4B & 42 & \textbf{83.63} & 75.63 & 0.0 & --- & +10.67 \\
115	\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & 42.88 & $-$14.92 \\
116	\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & 42.68 & $-$13.87 \\
117	\midrule
118	\cls{} & 8B & 42 & 84.48 & 78.17 & 0.0 & --- & +11.52 \\
119	\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & --- & +12.64 \\
120	\cwm{} & 8B & 42 & 65.17 & --- & 73.8 & 38.52 & $-$7.79 \\
121	\midrule
122	\multicolumn{8}{l}{\emph{DeepSeek-Coder (cross-model, in progress)}} \\
123	\cls{} & 6.7B & --- & --- & --- & --- & --- & --- \\
124	\cwm{} & 6.7B & --- & --- & --- & --- & --- & --- \\
125	\midrule
126	Majority & --- & --- & 72.96 & --- & --- & --- & --- \\
127	\bottomrule
128	\end{tabular}}
129	\end{table}
130	
131	\paragraph{Formulation divergence.} At repository-level complexity, \cls{} and \cwm{} diverge sharply on Qwen3: the gap is 25.59\pp{} at 4B (\cls{} 83.63\% vs.\ \cwm{} 58.04\%, seed 42; Figure~\ref{fig:scaling_gap}) and 19.31\pp{} at 8B (84.48\% vs.\ 65.17\%). Both gaps are an order of magnitude larger than at function level (1--2\pp{}, Table~\ref{tab:scaling}), confirming that formulation effectiveness is complexity-dependent. \cwm{} falls below the majority baseline at both scales ($-$14.92\pp{} at 4B, $-$7.79\pp{} at 8B), indicating negative utility for this model/formulation combination. DeepSeek-Coder repo-level results (in progress) will determine whether this divergence is consistent across model families or specific to Qwen3's tokenizer and generation properties.
132	
133	\paragraph{Default assignment artifact.} The apparent \cwm{} ``improvement'' from 4B (58.04\%) to 8B (65.17\%) is an artifact of the default assignment protocol: unparseable outputs receive the majority-class label (pass, 72.96\% of the test set). As unparseable rate \emph{increases} from 53.7\% to 73.8\%, more predictions are replaced by this high-accuracy default, inflating overall accuracy. Parseable-only accuracy \emph{decreases} from 42.88\% (4B) to 38.52\% (8B), indicating that the generation model's actual predictive quality degrades with scale at this complexity level.
134	
135	\paragraph{Generation quality analysis.} Per-mutation analysis of \cwm{} 8B reveals degradation across all categories relative to 4B. The gold mutation (unmodified code) is most striking: parse rate collapses from 43.5\% (4B) to 23.9\% (8B), with parseable accuracy at 16.5\%. Even the simplest generation target (reproducing expected outputs for correct code) becomes harder at scale, consistent with a model-specific generation bottleneck. Whether this reflects a property of the Qwen3 tokenizer, the training regime, or the generation formulation itself will be informed by cross-model results. Detailed per-mutation breakdown appears in Appendix~\ref{app:repo_mutation}.
136	
137	\paragraph{Complexity as moderator.} The function-level \cls{}--\cwm{} gap widens from 1.18\pp{} (4B) to 2.43\pp{} (8B, $p = 0.0066$) with controlled methodology (matched seeds, same precision, no default assignment). At repo level, absolute gap magnitude (19--26\pp{}) is an order of magnitude larger than at function level (1--2\pp{}). This confirms complexity as the primary moderator of formulation divergence, though the repo-level data is from Qwen3 only.
138	
139	\paragraph{Sequence length.} A matched-context ablation confirms input context disparity explains $<$3\% of the \cls{}--\cwm{} gap: \cls{} 8B evaluated at \texttt{max\_seq\_length}$=$2,048 yields a matched-context gap of 25.00\pp{}, representing 98\% of the same-size 25.59\pp{} gap (Appendix~\ref{app:ablations}).
140	
141	\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline), indicating that val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \cwm{} 8B comparison is also single-seed. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches; the synthetic-to-real transfer gap remains untested.
142	
143	
144	\subsection{Analysis}
145	\label{sec:analysis}
146	
147	\paragraph{(a) Error complementarity.}
148	\cls{} and \cwm{} make errors in opposite directions at function level. Among \cls{} errors (seed 42), 75.5\% are false negatives (FAIL $\to$ PASS), meaning the classifier over-predicts passing. Among \cwm{} errors, 83.1\% are false positives (PASS $\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination achieves 90.63\% accuracy, +3.12\pp{} over the best single formulation (87.51\%). This systematic complementarity indicates that the formulations capture different aspects of code behavior: classification encodes discriminative features directly, while generation must additionally model output structure, leading to orthogonal failure patterns. Ensemble approaches combining both signals are a natural direction.
149	
150	\paragraph{(b) CWM error mode breakdown.}
151	Among unparseable \cwm{} outputs (Qwen3, repo-level), 76.9\% contain no execution keywords; 22.9\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\%), suggesting that repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-inherent one.
152	
153	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
154	Relaxed matching (tolerating format deviations, L0--L4) \emph{decreases} \cwm{} accuracy: 58.04\%$\to$56.98\% (seed 42) and 59.09\%$\to$55.91\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (42--53\%). The divergence widens from 26\pp{} to 28\pp{} under relaxed matching, ruling out the hypothesis that parsing strictness inflates the observed gap.
155	
156	\paragraph{(d) Variance compression.}
157	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and TRAJ (0.97\pp{}) at function level. If \cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
158	
159	\paragraph{(e) Per-test precision and recall.}
160	\cls{} achieves fail \fone{} 87.86\% (precision 82.75\%, recall 93.64\%) at seed 42, with 42.1\% of problems perfectly predicted. Multi-F2P instances (6--10 tests) reach 96.3\% accuracy, corroborating the oracle finding that per-test granularity is most valuable for complex instances.
161	
162	\paragraph{(f) Block correlation.}
163	Within-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\times$ more all-correct problems than i.i.d.\ expectation). All statistical tests use clustered bootstrap accordingly.
164	
165	\paragraph{(g) LoRA rank and majority voting.}
166	Doubling adapter capacity (rank 32) does not improve \cwm{} accuracy ($-$0.51\pp{}, within seed variance); majority voting ($K{=}3$) decreases accuracy ($-$0.68\pp{}). Both interventions fail to resolve the generation bottleneck on Qwen3, consistent with the failure being formulation-level or model-specific rather than capacity-limited (Appendix~\ref{app:ablations}).
167	
168	\paragraph{(h) Per-mutation scaling patterns.}
169	Scaling benefits are highly non-uniform across mutation types (Appendix, Table~\ref{tab:mutation_breakdown}). \texttt{off\_by\_one} shows the largest \cls{} scaling gain: 58.5\% (4B) to 83.0\% (8B mean, $+$24.6\pp{}). In contrast, \texttt{boundary\_removal} is scale-invariant at ${\sim}$46\% across all seeds and sizes, identifying an intrinsic difficulty ceiling. For \cwm{}, gold mutation parse rate collapses from 43.5\% (4B) to 23.9\% (8B) despite being the simplest target, indicating that generation capability degrades even for trivially correct code at larger scale within Qwen3.
170	
171	\paragraph{(i) Inference efficiency.}
172	\cls{} achieves 217$\times$ higher throughput than \cwm{} at repo level (853 vs.\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\cls{}) vs.\ 16.3s (\cwm{}). At the observed unparseable rate of 73.8\% (8B), the majority of \cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This efficiency gap is an inherent property of the formulation difference (1 vs.\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.
173	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adf980a5-773b-4829-afe7-b91a13e1042a",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "afc382ce2eacaa3da",
  "type": "user",
  "uuid": "fece7105-7571-4795-a543-3c773b30b86b",
  "sourceToolAssistantUUID": "adf980a5-773b-4829-afe7-b91a13e1042a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T04:02:20.453Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JULXWbvAiQLXRRBrs9MFYv`</summary>

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
  "parentUuid": "fece7105-7571-4795-a543-3c773b30b86b",
  "isSidechain": true,
  "agentId": "afc382ce2eacaa3da",
  "requestId": "req_011Cb7UYEUtRZsuNrLkicEuq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b79977e-32e9-4ab4-b611-4a711f9b6803",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpWeQHCHY53Vw7nzY1V3K3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4176,
      "cache_read_input_tokens": 17797,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 17797,
          "cache_creation_input_tokens": 4176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4176,
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

_source line 14 · 2026-05-17T04:02:20.458Z_

<details><summary>↩ Tool result · `toolu_01JULXWbvAiQLXRRBrs9MFYv`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first controlled comparison of three formulations for execution-free code repair verification: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level scoring. Our central finding is that no single formulation dominates across all conditions; formulation effectiveness is complexity-dependent and, at repository scale, model-contingent.
5	
6	At function level, \cls{} and \cwm{} achieve near-equivalent accuracy (gap 1.24\pp{} at 4B, TOST equivalence $p{=}0.007$), suggesting that the formulation choice matters less than model capacity and training data at this complexity tier. At repository level, formulation divergence amplifies dramatically (4B: 25.59\pp{}; 8B: 19.31\pp{}), but the source of this divergence requires careful attribution: \cwm{} failures on Qwen3 concentrate in format non-compliance (unparseable rates 53.7--73.8\%) rather than semantic prediction errors. Whether this reflects a fundamental generation bottleneck or a model-specific tokenizer interaction remains an open empirical question pending cross-model validation.
7	
8	Two formulation-level properties generalize independent of model choice. First, per-test classification provides diagnostic granularity at equivalent trajectory-level accuracy, identifying which specific tests a patch fails. This advantage concentrates in instances with $\geq$2 fail-to-pass tests (31\% of instances, contributing 55\% of total oracle advantage). Second, the 1-token classification formulation yields a 217$\times$ throughput advantage over variable-length generation, an inherent property of the output-length asymmetry.
9	
10	Error complementarity between formulations (oracle ensemble: 90.63\%) suggests that the practitioner's choice need not be exclusive. Classification and generation exhibit complementary failure patterns, motivating routing strategies that select formulations based on predicted instance complexity.
11	
12	\paragraph{Limitations.}
13	Primary repo-level experiments use a single model family (Qwen3); cross-model validation with DeepSeek-Coder confirms near-equivalent function-level performance (gap 0.02\pp{}, 2 seeds), but repo-level cross-model results are pending. The repo-level same-size comparisons each use a single seed (4B-4B and 8B-8B). No downstream re-repair experiment validates whether per-test diagnostic signals translate to actual fix improvements. Pass-to-pass regression rates are negligible (1.04\% mean, 0\% median), meaning the per-test advantage currently concentrates in fail-to-pass discrimination; regression detection remains untested in practice. Training data comprises synthetic mutations; transfer to naturally occurring developer bugs is untested. The oracle analysis assumes ground-truth test labels; real-world per-test advantage is upper-bounded by classifier accuracy.
14	
15	\paragraph{Future work.}
16	Cross-model repo-level validation is the most critical next step: if DeepSeek-Coder replicates the Qwen3 divergence pattern, the generation bottleneck can be attributed to the formulation rather than the model. Multi-seed repo-level replication would strengthen statistical claims at this complexity tier. Error complementarity motivates complexity-aware routing that selects formulations per-instance. Per-test failure signals enable diagnostic re-repair: localizing faults from per-test verdicts rather than discarding failed patches outright. Integration with test-time scaling systems (best-of-$N$ with per-test reranking) is a natural application of the diagnostic granularity finding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b79977e-32e9-4ab4-b611-4a711f9b6803",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "afc382ce2eacaa3da",
  "type": "user",
  "uuid": "2e315b1e-ef76-458c-8dcf-14f9557b536a",
  "sourceToolAssistantUUID": "7b79977e-32e9-4ab4-b611-4a711f9b6803",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T04:02:24.950Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F7AKkhwGcKXKQ8U5bzL5aY`</summary>

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
  "parentUuid": "2e315b1e-ef76-458c-8dcf-14f9557b536a",
  "isSidechain": true,
  "agentId": "afc382ce2eacaa3da",
  "requestId": "req_011Cb7UYXd1wgvoM9n1A1FFT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b92a9ae-756e-4422-acb3-f295cbd6670e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Z86BduG1gV5vdd7w7aWhS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9565,
      "cache_read_input_tokens": 21973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9565,
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

_source line 16 · 2026-05-17T04:02:25.007Z_

<details><summary>↩ Tool result · `toolu_01F7AKkhwGcKXKQ8U5bzL5aY`</summary>

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
151	@article{guo2024deepseekcoder,
152	  title={{DeepSeek-Coder}: When the Large Language Model Meets Programming -- The Rise of Code Intelligence},
153	  author={Guo, Daya and Zhu, Qihao and Yang, Dejian and Xie, Zhenda and Dong, Kai and Zhang, Wentao and Chen, Guanting and Bi, Xiao and Wu, Y. and Li, Y.K. and Luo, Fuli and Xiong, Yun and Liang, Wenfeng},
154	  journal={arXiv preprint arXiv:2401.14196},
155	  year={2024}
156	}
157	
158	% === Code Verification ===
159	
160	@inproceedings{ni2023lever,
161	  title={{LEVER}: Learning to Verify Language-to-Code Generation with Execution},
162	  author={Ni, Ansong and Iyer, Srini and Radev, Dragomir and Stoyanov, Veselin and Yih, Wen-tau and Wang, Sida I. and Lin, Xi Victoria},
163	  booktitle={ICML},
164	  year={2023}
165	}
166	
167	@inproceedings{chen2023codet,
168	  title={{CodeT}: Code Generation with Generated Tests},
169	  author={Chen, Bei and Zhang, Fengji and Nguyen, Anh and Zan, Daoguang and Lin, Zeqi and Lou, Jian-Guang and Chen, Weizhu},
170	  booktitle={ICLR},
171	  year={2023}
172	}
173	
174	% === Process vs Outcome Supervision ===
175	
176	@article{lightman2023letsverify,
177	  title={Let's Verify Step by Step},
178	  author={Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
179	  journal={arXiv preprint arXiv:2305.20050},
180	  year={2023}
181	}
182	
183	@article{uesato2022solving,
184	  title={Solving Math Word Problems with Process- and Outcome-Based Feedback},
185	  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},
186	  journal={arXiv preprint arXiv:2211.14275},
187	  year={2022}
188	}
189	
190	% === Verification-in-the-Loop ===
191	
192	@inproceedings{le2022coderl,
193	  title={{CodeRL}: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning},
194	  author={Le, Hung and Wang, Yue and Gotmare, Akhilesh Deepak and Savarese, Silvio and Hoi, Steven C.H.},
195	  booktitle={NeurIPS},
196	  year={2022}
197	}
198	
199	@article{li2022alphacode,
200	  title={Competition-Level Code Generation with {AlphaCode}},
201	  author={Li, Yujia and Choi, David and Chung, Junyoung and Kushman, Nate and Schrittwieser, Julian and others},
202	  journal={Science},
203	  volume={378},
204	  number={6624},
205	  pages={1092--1097},
206	  year={2022}
207	}
208	
209	@article{shinn2023reflexion,
210	  title={Reflexion: Language Agents with Verbal Reinforcement Learning},
211	  author={Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
212	  journal={NeurIPS},
213	  year={2023}
214	}
215	
216	% === Predictive Mutation Testing ===
217	
218	@inproceedings{tufano2019predictive,
219	  title={Learning How to Mutate Source Code from Bug-Fixes},
220	  author={Tufano, Michele and Watson, Cody and Bavota, Gabriele and Di Penta, Massimiliano and White, Martin and Poshyvanyk, Denys},
221	  booktitle={ISSTA},
222	  year={2019}
223	}
224	
225	@article{kim2022predictive,
226	  title={Predictive Mutation Testing via Natural Language Channel},
227	  author={Kim, Jinhan and Ju, Juyoung and Tao, Robert and Hu, Nhat-Tan and Baik, Shin Yoo Juyeon},
228	  journal={IEEE TSE},
229	  year={2022}
230	}
231	
232	% === Task Reformulation NLP ===
233	
234	@inproceedings{rajpurkar2016squad,
235	  title={{SQuAD}: 100,000+ Questions for Machine Comprehension of Text},
236	  author={Rajpurkar, Pranav and Zhang, Jian and Lopyrev, Konstantin and Liang, Percy},
237	  booktitle={EMNLP},
238	  year={2016}
239	}
240	
241	@inproceedings{lewis2020bart,
242	  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},
243	  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},
244	  booktitle={ACL},
245	  year={2020}
246	}
247	
248	@article{raffel2020t5,
249	  title={Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
250	  author={Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J},
251	  journal={JMLR},
252	  volume={21},
253	  number={140},
254	  pages={1--67},
255	  year={2020}
256	}
257	
258	% === Statistical Methods ===
259	
260	@article{schuirmann1987tost,
261	  title={A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},
262	  author={Schuirmann, Donald J},
263	  journal={Journal of Pharmacokinetics and Biopharmaceutics},
264	  volume={15},
265	  number={6},
266	  pages={657--680},
267	  year={1987}
268	}
269	
270	@book{davison1997bootstrap,
271	  title={Bootstrap Methods and their Application},
272	  author={Davison, Anthony C and Hinkley, David V},
273	  publisher={Cambridge University Press},
274	  year={1997}
275	}
276	
277	@article{shrout1979icc,
278	  title={Intraclass Correlations: Uses in Assessing Rater Reliability},
279	  author={Shrout, Patrick E and Fleiss, Joseph L},
280	  journal={Psychological Bulletin},
281	  volume={86},
282	  number={2},
283	  pages={420--428},
284	  year={1979},
285	  doi={10.1037/0033-2909.86.2.420}
286	}
287	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b92a9ae-756e-4422-acb3-f295cbd6670e",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "afc382ce2eacaa3da",
  "type": "user",
  "uuid": "86d074a8-ec97-4af1-87c1-bdbf072d69a8",
  "sourceToolAssistantUUID": "9b92a9ae-756e-4422-acb3-f295cbd6670e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T04:02:25.303Z_

<details open><summary>🔧 Tool call — Read · `toolu_013sy7nNW79ri4Mtaz7bnoeC`</summary>

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
  "parentUuid": "86d074a8-ec97-4af1-87c1-bdbf072d69a8",
  "isSidechain": true,
  "agentId": "afc382ce2eacaa3da",
  "requestId": "req_011Cb7UYXd1wgvoM9n1A1FFT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0dd464f-01ec-48cd-9d1c-4ad1af3b3052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Z86BduG1gV5vdd7w7aWhS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9565,
      "cache_read_input_tokens": 21973,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9565
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 21973,
          "cache_creation_input_tokens": 9565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9565,
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

_source line 18 · 2026-05-17T04:02:25.317Z_

<details><summary>↩ Tool result · `toolu_013sy7nNW79ri4Mtaz7bnoeC`</summary>

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
  "parentUuid": "c0dd464f-01ec-48cd-9d1c-4ad1af3b3052",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "afc382ce2eacaa3da",
  "type": "user",
  "uuid": "53808efb-5a84-4e17-bf02-eed6559a88fd",
  "sourceToolAssistantUUID": "c0dd464f-01ec-48cd-9d1c-4ad1af3b3052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-17T04:03:40.254Z_

Now I have a thorough understanding of the full paper. Let me provide my review.

## R2 Review: Novelty & Related Work

### Summary
This paper presents a controlled empirical comparison of three formulations (per-test classification, execution output generation, trajectory-level scoring) for execution-free code verification. The main findings are that formulations are equivalent at function-level complexity, diverge sharply at repository-level (though this is observed only on one model family), and that classification provides diagnostic granularity at lower cost. The work is methodologically careful but has limited novelty and incomplete experiments that weaken core claims.

### Strengths

- **Rigorous experimental control.** Holding LoRA config, training data, compute, and seeds constant is the right methodology. The use of TOST equivalence testing, clustered bootstrap, and ICC for within-problem correlation shows statistical sophistication uncommon in empirical ML papers.
- **Honest limitations.** The paper acknowledges single-seed repo-level comparisons, pending cross-model validation, and the fact that core findings (CWM failure) may be model-specific. This is refreshingly transparent.
- **Useful practical insight.** The 217x throughput advantage of CLS and the observation that unparseable CWM outputs default to majority class (creating an accuracy inflation artifact) are genuinely useful for practitioners.
- **Well-structured related work.** The related work section covers relevant threads (execution simulation, process/outcome supervision, verification-in-the-loop, predictive mutation testing) and positions the paper clearly. The paragraph on "Classification vs. Generation in NLP" provides useful conceptual grounding.
- **Oracle accuracy-utility framework.** The block-correlation model (Equations 1-3) provides a principled theoretical lens for understanding when per-test granularity matters, going beyond pure empiricism.

### Weaknesses

- **Incomplete core experiments undermine the central claims.** The paper's most interesting claim (CWM failure is model-contingent at repo-level) is unsubstantiated: DeepSeek repo-level results are listed as "in progress" with empty table cells. The paper repeatedly hedges ("remains open pending cross-model validation"), which is appropriate, but submitting a comparison paper whose pivotal comparison is missing is premature. A reviewer must evaluate what is shown, not what is promised.

- **Limited novelty of established findings.** That classification is cheaper than generation (1 token vs. many) is trivially obvious from the formulation definitions. That generation is harder when outputs are long (exponential decay argument in Section 3.2) is well-known from NLP sequence modeling. The function-level equivalence null result, while useful, is predictable: short outputs with simple structure make generation nearly degenerate to classification. The genuinely novel finding (model-contingent CWM failure) is the one that lacks cross-model validation.

- **Narrow model/scale exploration.** All fine-tuned models are 4B-8B LoRA variants. The CWM literature uses 32B+ models (the original Code World Model is 32B). Comparing LoRA-finetuned 4-8B CWM against a 32B mid-trained CWM is not possible with this setup, but the paper should more prominently acknowledge that its CWM results characterize "small-model LoRA CWM" rather than "CWM as a formulation." The brief footnote acknowledging this is insufficient given how central the CWM failure is to the paper's narrative.

- **Re-repair claim (Claim 4 from the brief) is absent from the paper.** The paper summary mentions "+13.3pp resolve rate from re-repair (p=0.031, McNemar, n=60)" but the actual paper text contains no re-repair experiment. The Conclusion explicitly states "No downstream re-repair experiment validates whether per-test diagnostic signals translate to actual fix improvements." This is a missing validation of the paper's motivating application.

- **Only 10 references in the brief vs. 30+ in the actual bib.** The actual reference list is adequate (~30 entries), but coverage of reward modeling for code (SWE-RewardBench, CodeRM) and recent execution-free verification papers from 2025-2026 could be deeper. The paper cites SWE-RM but not the SWE-RewardBench evaluation paper separately; it also misses ICE-Score (Zhuo 2024) and other execution-prediction benchmarks.

- **Single-family repo-level results.** The entire repo-level story (the most interesting part) rests on Qwen3 alone with 1-2 seeds per configuration. The CLS advantage could be an artifact of Qwen3's tokenizer interacting poorly with generation rather than a generalizable formulation-level property. The paper acknowledges this but still frames it as a "finding" rather than a "preliminary observation."

- **Abstract inconsistency with paper content.** The paper has two abstracts that differ substantially. The main.tex abstract discusses error complementarity and oracle ensembles, while the brief mentions re-repair results. Neither matches the other cleanly. The actual abstract is 199 words (acceptable length) but tries to compress too many findings, making it read like a results dump rather than a story.

- **Missing qualitative error analysis.** The paper discusses error modes quantitatively (false negative rates, unparseable rates) but provides no concrete examples of what CWM generates when it fails, what CLS misclassifies, or what the unparseable outputs look like. For a paper whose core contribution is characterizing formulation behavior, this absence is notable.

### Questions for Authors

1. **Can you provide any preliminary DeepSeek repo-level numbers?** Even partial results (e.g., unparseable rate alone) would dramatically change the paper's contribution. If DeepSeek also shows 50%+ unparseable at repo-level, the finding is formulation-level; if not, the paper's most prominent finding (the 19-26pp gap) is essentially a Qwen3 bug report.

2. **Why not evaluate CWM with a larger base model (16B+) or with the original 32B CWM checkpoint?** The claim that "LoRA rank 32 doesn't help" demonstrates rank is not the bottleneck, but raw model capacity/pretraining (the 32B CWM was mid-trained on execution traces) could be. Without this, the CWM failure could be attributed to insufficient pretraining rather than formulation design.

3. **What do unparseable CWM outputs actually contain?** The paper mentions "76.9% contain no execution keywords" but does not show examples. Are these hallucinated code? Explanations? Empty strings? The character of the failure matters for interpreting whether this is fixable with better prompting/formatting instructions.

4. **The re-repair experiment appears in the brief but not the paper. Is this a planned addition or a removed contribution?** If removed, the paper loses its strongest application-level motivation.

5. **How sensitive is the function-level equivalence result to the specific mutation operators used?** HumanEval/MBPP mutations may produce very short, structured outputs that trivialize generation. Would equivalence hold on more naturalistic function-level bugs with longer/more complex expected outputs?

### Related Work Gaps

- **SWE-RewardBench (Zhang et al. 2025)**: Cited but could be discussed more as a direct evaluation framework for the same problem.
- **ICE-Score (Zhuo, EACL 2024)**: Execution-free code evaluation via LLM scoring, relevant to trajectory-level formulation.
- **CodeScore (Dong et al. 2023)**: Unified code evaluation without execution, relevant positioning.
- **Recent reward model work for code**: RLCF (Liu et al. 2025), CodeRM papers from 2025 that train reward models for code generation.
- **CRUXEval (Gu et al. 2024)**: Listed in the brief summary but the actual paper cites the Meta CWM paper instead. CRUXEval is the benchmark; it should be cited distinctly if function-level evaluation uses similar paradigms.
- **Test-time compute scaling**: Only Snell et al. cited; the broader best-of-N literature (Wang et al. 2023 self-consistency, etc.) provides more context for why verification matters.

### Writing Quality Issues

- **Introduction paragraph 1**: "driving demand for execution-free alternatives" followed by listing three formulations in bold is acceptable, but the sentence beginning "Each makes different tradeoffs..." is vague. What tradeoffs specifically?
- **Dash usage**: The paper generally avoids em-dashes (good), but uses en-dashes in ranges appropriately. No major AI-style markers detected in this regard.
- **-ing phrases**: "driving demand for execution-free alternatives" (line 4 of intro), "making formulation choice irrelevant" (contribution 1 implicit), "indicating negative utility" (repo section). These are borderline but not egregious.
- **Hedging density**: The paper over-hedges at repo level: "Whether this divergence generalizes..." / "remains an open empirical question" / "pending cross-model validation" / "Whether this reflects a fundamental generation bottleneck or..." appears 4+ times. Once is transparent; four times signals the authors know the experiment is incomplete.
- **Abstract structure**: The abstract in abstract.tex reads more like a technical summary than a compelling pitch. It opens with formulation definitions rather than the problem/motivation. The first sentence should establish why execution-free verification matters before naming formulations.
- **Contribution list wording**: "Error complementarity and ensemble potential" (contribution 3 in intro) uses "potential" which signals speculation rather than demonstrated contribution. Either demonstrate the ensemble or remove it from contributions.
- **"in progress" in a submitted paper**: Table 3 contains "---" entries with the label "in progress." This is unacceptable for a submission; either include results or remove the rows and discuss as future work.

### Score: 3/6
### Confidence: 4/5

The paper demonstrates solid experimental methodology and statistical rigor, but it is submitting an incomplete study. The most novel potential finding (model-contingent CWM failure at repo-level) lacks cross-model validation, the re-repair application is unvalidated, and the findings that are complete (function-level equivalence, CLS efficiency) are either predictable or incremental. The "design space characterization" framing is appropriate but the space is incompletely explored: one model family at repo-level, no models above 8B, no re-repair demonstration. This reads as a solid workshop paper or a strong draft that needs one more round of experiments (DeepSeek repo-level, re-repair validation, qualitative examples) before it is ready for a top venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53808efb-5a84-4e17-bf02-eed6559a88fd",
  "isSidechain": true,
  "agentId": "afc382ce2eacaa3da",
  "requestId": "req_011Cb7UYtab9vVmktiMpANh6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb085d35-5624-4fb5-ad32-8030dfea3b95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dakk3B96ffUoDuKGNRJWLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9401,
      "cache_read_input_tokens": 31538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9401,
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
