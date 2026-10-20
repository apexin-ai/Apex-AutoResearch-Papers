# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a4e9c0d907007e01f.jsonl`
- **Structured JSON:** [`54a7e1582997a5895b30.json`](../../sessions/54/54a7e1582997a5895b30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-16T15:44:29.861Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **Novelty and Related Work**.

## Paper Summary

Title: "Classification Scales Where Generation Fails: Per-Test Binary Verification for Code Repair"

The paper reformulates execution simulation for code repair verification from generation (Code World Models / CWM) to per-test binary classification (CLS). Three formulations are compared: CLS (per-test pass/fail classification), CWM (generate execution output then exact-match), and TRAJ (trajectory-level resolved/unresolved classification). All use identical base models (Qwen3-4B, Qwen3-8B, DeepSeek-R1-Distill-Qwen-7B) fine-tuned with LoRA.

Key claims:
1. On function-level benchmarks, CLS ≈ CWM (~87% F1) — classification is not trivially easier.
2. On repo-level SWE-bench tasks, CWM suffers 58–93% unparseable outputs while CLS maintains 82–85% accuracy — a 15–17pp gap.
3. Ordering CLS > TRAJ > CWM holds across Qwen and DeepSeek model families.
4. SWE-BENCH-PERTEST dataset: 428 repo-level instances with per-test labels.
5. Re-repair experiment: CLS diagnostics improve resolve rate by 5.0pp (p=0.038), concentrated in multi-test instances (+12.3pp).

The paper has 5 pages of content (Introduction, Related Work, Method, SWE-BENCH-PERTEST Dataset, Experiments with 6 subsections, Discussion, Conclusion). Related work section covers: Execution-Free Code Verification, SWE-bench and Code Repair, Classification vs. Generation in NLP.

Related Work (from paper):
- "SWE-RM and related reward models score candidate patches at the trajectory level"
- "Code World Models (CWM) and self-execution simulation approaches predict execution outputs"
- "The choice between classification and generation formulations has been studied for NLI, sentiment analysis, and information extraction"
- Claims: "No prior work studies per-test binary classification as a dedicated verification formulation, or provides controlled comparisons of classification versus generation across complexity levels and model families."

## Your Review Task

Evaluate the paper on:

1. **Novelty Assessment**: 
   - Is reformulating generation as classification genuinely novel, or is it an obvious simplification? 
   - The core idea is: instead of generating full execution output and checking exact match, just predict pass/fail. How surprising is this finding?
   - Is the "complexity-dependent advantage" insight (CLS ≈ CWM at func-level, CLS >> CWM at repo-level) a genuine contribution or a predictable outcome?

2. **Related Work Completeness**:
   - The Related Work section is very brief (half a column). Are important baselines or prior work missing?
   - Specific areas to check: execution prediction models, test outcome prediction, program analysis, neural code verification, reward modeling for code
   - Does the paper adequately position itself against SWE-RM, CodeRM, and other reward models?
   - Is the "Classification vs. Generation in NLP" framing appropriate and well-connected?

3. **Positioning and Framing**:
   - Is the paper underselling or overselling its contribution?
   - The claim "no prior work studies per-test binary classification as a dedicated verification formulation" — is this true? Has anyone done binary test-outcome prediction before?
   - Is the CWM comparison fair framing? CWM was designed for a different purpose (rich execution simulation), not just pass/fail prediction.

4. **Contribution Significance**:
   - Dataset contribution (SWE-BENCH-PERTEST): how valuable is this independently?
   - Is the finding actionable for the community? Does it change how people would build verification systems?
   - Would a top venue accept a paper whose main finding is "classification beats generation when generation is hard"?

5. **Writing Quality and Presentation**:
   - Is the paper well-structured? Is the argument flow logical?
   - Are the claims precisely stated or do they overreach?

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, numbered W1, W2, ... with severity: minor/moderate/major)
- Questions for authors
- Preliminary score (1-6) with confidence (1-5)
- One-line verdict

Keep the review under 800 words.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fffa33bf-46e0-4626-a07a-357495c4180f",
  "agentId": "a4e9c0d907007e01f",
  "type": "user",
  "uuid": "c7c51f20-a084-4d3b-b1dd-757a8c4e7540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T15:44:29.864Z_

```json
{
  "parentUuid": "c7c51f20-a084-4d3b-b1dd-757a8c4e7540",
  "isSidechain": true,
  "agentId": "a4e9c0d907007e01f",
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
  "uuid": "b7e76376-69a2-4449-b004-be5d69478758",
  "timestamp": "2026-05-16T15:44:29.864Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-16T15:44:34.011Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EEWkB6bYBbtUef96rGc9Vo`</summary>

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
  "parentUuid": "b7e76376-69a2-4449-b004-be5d69478758",
  "isSidechain": true,
  "agentId": "a4e9c0d907007e01f",
  "requestId": "req_011Cb6WH9fUeu5gNcLfkd22u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f2713e8-f44f-44b4-9080-11088695635c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MWerGgpxUkm3V8SDDNSpT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6967,
      "cache_read_input_tokens": 8972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6967,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 4 · 2026-05-16T15:44:34.022Z_

<details><summary>↩ Tool result · `toolu_01EEWkB6bYBbtUef96rGc9Vo`</summary>

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
  "parentUuid": "5f2713e8-f44f-44b4-9080-11088695635c",
  "isSidechain": true,
  "promptId": "fffa33bf-46e0-4626-a07a-357495c4180f",
  "agentId": "a4e9c0d907007e01f",
  "type": "user",
  "uuid": "f5c4355c-327a-4038-a54d-c07bc892784b",
  "sourceToolAssistantUUID": "5f2713e8-f44f-44b4-9080-11088695635c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T15:44:34.595Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R6tiDAiPwnNZ9R2rrsJ9kf`</summary>

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
  "parentUuid": "f5c4355c-327a-4038-a54d-c07bc892784b",
  "isSidechain": true,
  "agentId": "a4e9c0d907007e01f",
  "requestId": "req_011Cb6WH9fUeu5gNcLfkd22u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98bc1fa0-2e47-42e5-92c8-18a63366562d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MWerGgpxUkm3V8SDDNSpT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6967,
      "cache_read_input_tokens": 8972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6967,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 6 · 2026-05-16T15:44:34.607Z_

<details><summary>↩ Tool result · `toolu_01R6tiDAiPwnNZ9R2rrsJ9kf`</summary>

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
  "parentUuid": "98bc1fa0-2e47-42e5-92c8-18a63366562d",
  "isSidechain": true,
  "promptId": "fffa33bf-46e0-4626-a07a-357495c4180f",
  "agentId": "a4e9c0d907007e01f",
  "type": "user",
  "uuid": "47fd2933-09fb-4110-a95d-66fad91c1acb",
  "sourceToolAssistantUUID": "98bc1fa0-2e47-42e5-92c8-18a63366562d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T15:44:34.645Z_

<details open><summary>🔧 Tool call — Read · `toolu_0113eX42rNDVtjyyAUV2ziMf`</summary>

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
  "parentUuid": "47fd2933-09fb-4110-a95d-66fad91c1acb",
  "isSidechain": true,
  "agentId": "a4e9c0d907007e01f",
  "requestId": "req_011Cb6WH9fUeu5gNcLfkd22u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db67f389-37cb-40b9-820d-7c57d6d91f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MWerGgpxUkm3V8SDDNSpT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6967,
      "cache_read_input_tokens": 8972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6967,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 8 · 2026-05-16T15:44:34.651Z_

<details><summary>↩ Tool result · `toolu_0113eX42rNDVtjyyAUV2ziMf`</summary>

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
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with LoRA~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. For cross-model validation, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (1 seed \cls{}, 2 seeds \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge.
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
52	Fine-tuned \cls{} achieves 88.43\% ($\pm$0.78), compared to 87.19\% ($\pm$0.37) for \cwm{} and 86.30\% ($\pm$0.97) for TRAJ. The \cls{}--\cwm{} gap is 1.24\pp{}, modest at this complexity level where generation is not yet bottlenecked by token budget or string complexity. Zero-shot baselines lag substantially (64.40\% at 8B, 71.69\% at 32B NF4), confirming that task-specific fine-tuning is necessary for reliable verification.
53	
54	\paragraph{Cross-model validation.} DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} confirms that the near-equivalence of \cls{} and \cwm{} at function level is not model-specific: \cls{} achieves 86.85\% ($\pm$0.11, 2 seeds) vs.\ \cwm{} 86.83\% ($\pm$1.49, 2 seeds), a gap of +0.02\pp{}---indistinguishable from zero. The variance asymmetry (\cwm{} $\sigma{=}1.49$ vs.\ \cls{} $\sigma{=}0.11$) mirrors the pattern observed in Qwen3 (\S\ref{sec:analysis}, paragraph d): \cwm{}'s higher seed variance at function level is consistent with generation being more sensitive to initialization than classification. Both model families show gaps within noise at function level (Qwen3: 1.24\pp{}, DeepSeek: 0.02\pp{}), consistent with the thesis that the \cls{} advantage is complexity-dependent rather than model-specific. \cwm{} produces 0\% unparseable outputs at function level for both architectures, confirming that format compliance collapse is specific to repository-level complexity. Repo-level cross-model validation is in progress.
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
65	\caption{Model-size scaling: \cls{} vs.\ \cwm{} accuracy (\%) at 4B and 8B. Three matched seeds in full precision. The \cls{}--\cwm{} gap widens from 1.18\pp{} to 2.43\pp{}.}
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
81	At 4B, \cls{} and \cwm{} are separated by 1.18\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\pp{} (Figure~\ref{fig:scaling_gap}). Clustered bootstrap analysis yields a mean gap of 2.26\pp{} ($p = 0.0066$, 95\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.
82	
83	The asymmetry in scaling efficiency is striking: from 4B to 8B, \cls{} gains +0.99\pp{} (88.41 $\to$ 89.40) while \cwm{} loses $-$0.27\pp{} (87.23 $\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \cwm{} accuracy. However, the \cwm{} regression ($-$0.27\pp{}) falls within seed noise (3-seed std ${\sim}$0.5\pp{}) and could reflect suboptimal hyperparameter transfer rather than a fundamental bottleneck. Whether this divergence amplifies at repository-level complexity is examined in \S\ref{sec:repo}.
84	
85	
86	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
87	\label{sec:equivalence}
88	
89	We compare \cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds. The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); the TOST equivalence test confirms statistical equivalence at $p = 0.007$ ($\pm$2\pp{} margin). Within-problem predictions are correlated (ICC $= 0.191$, $p < 0.0001$, DEFF $= 3.97$); all statistical tests use clustered bootstrap accordingly. Per-test classification thus provides diagnostic information---which specific tests fail---at no cost to variant-level accuracy.
90	
91	
92	\subsection{Accuracy-Utility Frontier}
93	\label{sec:oracle-results}
94	
95	Oracle analysis on SWE-bench Verified (500 instances) reveals that per-test advantage concentrates sharply: at $T = 1$ F2P tests (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T \geq 2$ (31.3\%), with $T = 2$ alone contributing 55.3\% of the total 10.93\pp{} block-correlated advantage. Pass-to-pass (P2P) regression is negligible (1.04\% mean, 0\% median), so the practical value concentrates in fail-to-pass discrimination. Full stratification and the i.i.d.\ vs.\ block-correlated comparison appear in Appendix~\ref{app:oracle}.
96	
97	
98	\subsection{Repo-Level Results}
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
131	\paragraph{Same-size gap magnitude.} The \cls{}--\cwm{} gap at 4B is 25.59\pp{} (\cls{} 83.63\% vs.\ \cwm{} 58.04\%, seed 42; Figure~\ref{fig:scaling_gap}); at 8B it is 19.31\pp{} (84.48\% vs.\ 65.17\%). Both gaps far exceed the function-level gap (1--2\pp{}, Table~\ref{tab:scaling}), confirming that the classification advantage is complexity-dependent. \cwm{} falls below the majority baseline at both scales ($-$14.92\pp{} at 4B, $-$7.79\pp{} at 8B), indicating negative utility.
132	
133	\paragraph{Overall accuracy is misleading.} The apparent \cwm{} ``improvement'' from 4B (58.04\%) to 8B (65.17\%) is an artifact of the default assignment protocol: unparseable outputs receive the majority-class label (pass, 72.96\% of the test set). As unparseable rate \emph{increases} from 53.7\% to 73.8\%, more predictions are replaced by this high-accuracy default, inflating overall accuracy. The parseable-only accuracy---which isolates actual generation quality---\emph{decreases} from 42.88\% (4B) to 38.52\% (8B), confirming that CWM generation degrades with scale at repository-level complexity.
134	
135	\paragraph{Generation quality degrades uniformly.} Per-mutation analysis of \cwm{} 8B reveals degradation across all categories relative to 4B. The gold mutation (unmodified code) is most striking: parse rate collapses from 43.5\% (4B) to 23.9\% (8B), with parseable accuracy at 16.5\%---far below the trivially-correct ``pass'' prediction. This indicates that even the simplest generation target (reproducing expected outputs for correct code) becomes harder at scale, consistent with a fundamental generation bottleneck rather than insufficient capacity. Detailed per-mutation breakdown appears in Appendix~\ref{app:repo_mutation}.
136	
137	\paragraph{Scaling evidence.} The correct scaling signal comes from function-level results (\S\ref{sec:scaling}), where the \cls{}--\cwm{} gap widens from 1.18\pp{} (4B) to 2.43\pp{} (8B, $p = 0.0066$) with controlled methodology (matched seeds, same precision, no default assignment). At repo-level, the primary claim is that absolute gap magnitude (19--26\pp{}) is an order of magnitude larger than at function level (1--2\pp{}), demonstrating complexity-dependent advantage.
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
148	\cls{} and \cwm{} make errors in opposite directions at function level. Among \cls{} errors (seed 42), 75.5\% are false negatives (FAIL $\to$ PASS), meaning the classifier tends to over-predict passing. Among \cwm{} errors, 83.1\% are false positives (PASS $\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\% accuracy, a 3.12\pp{} improvement over \cls{} alone (87.51\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains.
149	
150	\paragraph{(b) CWM error mode breakdown.}
151	Among unparseable \cwm{} outputs, 76.9\% contain no execution keywords; 22.9\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\%), suggesting domain-specific code contexts prevent structured generation.
152	
153	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
154	Relaxed matching (tolerating format deviations, L0--L4) \emph{decreases} \cwm{} accuracy: 58.04\%$\to$56.98\% (seed 42) and 59.09\%$\to$55.91\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (42--53\%). The \cls{}--\cwm{} gap widens from 26\pp{} to 28\pp{}, ruling out the hypothesis that parsing strictness inflates the observed gap.
155	
156	\paragraph{(d) Variance compression.}
157	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and TRAJ (0.97\pp{}) at function level. This is consistent with the bottleneck hypothesis: if \cwm{} performance is capped by output-format constraints, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
158	
159	\paragraph{(e) Per-test precision and recall.}
160	\cls{} achieves fail \fone{} 87.86\% (precision 82.75\%, recall 93.64\%) at seed 42, with 42.1\% of problems perfectly predicted. Multi-F2P instances (6--10 tests) reach 96.3\% accuracy, corroborating the oracle finding.
161	
162	\paragraph{(f) Block correlation.}
163	Within-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\times$ more all-correct problems than i.i.d.\ expectation). All tests use clustered bootstrap accordingly.
164	
165	\paragraph{(g) LoRA rank and majority voting.}
166	Doubling adapter capacity (rank 32) does not improve \cwm{} accuracy ($-$0.51\pp{}, within seed variance); majority voting ($K{=}3$) decreases accuracy ($-$0.68\pp{}). Both confirm the bottleneck is formulation-level, not capacity-level (Appendix~\ref{app:ablations}).
167	
168	\paragraph{(h) Per-mutation scaling patterns.}
169	Scaling benefits are highly non-uniform across mutation types (Appendix, Table~\ref{tab:mutation_breakdown}). \texttt{off\_by\_one} is the largest \cls{} scaling beneficiary: accuracy jumps from 58.5\% (4B) to 83.0\% (8B mean, $+$24.6\pp{}). In contrast, \texttt{boundary\_removal} is scale-invariant at ${\sim}$46\% across all seeds and sizes, identifying a difficulty ceiling independent of capacity. For \cwm{}, gold mutation parse rate collapses from 43.5\% (4B) to 23.9\% (8B) despite being the simplest target---all tests pass by construction---indicating that generation capability degrades even for trivially correct code at larger scale.
170	
171	\paragraph{(i) Inference efficiency.}
172	\cls{} achieves 217$\times$ higher throughput than \cwm{} at repo level (853 vs.\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\cls{}) vs.\ 16.3s (\cwm{}). Moreover, 73.8\% of \cwm{}'s generated output at 8B is unparseable (\S\ref{sec:repo}), meaning the majority of generation budget is spent producing tokens that cannot yield a valid verdict. Combined with higher accuracy (83.63\% vs.\ 58.04\%) and perfect format compliance (0\% vs.\ 53.7\% unparseable at 4B), classification provides a triple advantage at repository-level complexity: accuracy, reliability, and throughput.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db67f389-37cb-40b9-820d-7c57d6d91f66",
  "isSidechain": true,
  "promptId": "fffa33bf-46e0-4626-a07a-357495c4180f",
  "agentId": "a4e9c0d907007e01f",
  "type": "user",
  "uuid": "538931a8-46cc-49dd-a0f1-f363ca6e497b",
  "sourceToolAssistantUUID": "db67f389-37cb-40b9-820d-7c57d6d91f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T15:44:39.433Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VV6jKWx1MBjG1xHySxn5bA`</summary>

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
  "parentUuid": "538931a8-46cc-49dd-a0f1-f363ca6e497b",
  "isSidechain": true,
  "agentId": "a4e9c0d907007e01f",
  "requestId": "req_011Cb6WHWNRXSaSjk3kqMsY8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f8d39cb-bd41-489e-a6e9-008d26f73d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QayAC8ay29DE4dcz5tzcDC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10341,
      "cache_read_input_tokens": 15939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10341,
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

_source line 10 · 2026-05-16T15:44:39.438Z_

<details><summary>↩ Tool result · `toolu_01VV6jKWx1MBjG1xHySxn5bA`</summary>

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
  "parentUuid": "3f8d39cb-bd41-489e-a6e9-008d26f73d9e",
  "isSidechain": true,
  "promptId": "fffa33bf-46e0-4626-a07a-357495c4180f",
  "agentId": "a4e9c0d907007e01f",
  "type": "user",
  "uuid": "0e4469ce-92a1-422d-a4df-be1bb3abf627",
  "sourceToolAssistantUUID": "3f8d39cb-bd41-489e-a6e9-008d26f73d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T15:44:39.545Z_

<details open><summary>🔧 Tool call — Read · `toolu_01THzPEs2oUPs46fXYHgtdNF`</summary>

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
  "parentUuid": "0e4469ce-92a1-422d-a4df-be1bb3abf627",
  "isSidechain": true,
  "agentId": "a4e9c0d907007e01f",
  "requestId": "req_011Cb6WHWNRXSaSjk3kqMsY8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dd3a81f-5da6-45ad-9817-e3bbce0a6f7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QayAC8ay29DE4dcz5tzcDC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10341,
      "cache_read_input_tokens": 15939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10341,
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

_source line 12 · 2026-05-16T15:44:39.549Z_

<details><summary>↩ Tool result · `toolu_01THzPEs2oUPs46fXYHgtdNF`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We reformulated execution simulation for code repair verification from open-ended output generation to per-test binary classification. Our central finding is that the advantage of this reformulation is complexity-dependent: on function-level code with short, structurally simple outputs, classification and generation achieve near-equivalent accuracy; at repository scale, classification dominates by a wide margin. The generation formulation suffers a compounding failure on complex code---format non-compliance discards the majority of predictions, and the surviving parseable outputs are themselves unreliable, falling below chance-level accuracy (50\%). Classification is immune to this failure mode by construction, as binary verdicts require no structured output parsing. Moreover, at function level, scaling model capacity does not resolve the generation bottleneck: \cwm{} accuracy decreases by 0.27\pp{} from 4B to 8B, consistent with a formulation-level bottleneck at this complexity tier. Independently, per-test classification provides fine-grained diagnostic signals---identifying which specific tests a patch fails---at equivalent trajectory-level accuracy, with the advantage concentrating in instances that contain multiple fail-to-pass tests.
5	
6	For test-time scaling pipelines evaluating patches against multi-test suites, classification avoids the compounding failure that degrades generation on complex code. Per-test verdicts unlock targeted re-repair guided by failure localization rather than binary accept/reject decisions.
7	
8	\paragraph{Limitations.}
9	Primary experiments use Qwen3; cross-model validation with DeepSeek-Coder-6.7B confirms near-equivalent \cls{}--\cwm{} performance at function level (gap 0.02\pp{}, 2 seeds), but repo-level cross-model results are pending. The repo-level same-size comparisons each use a single seed (4B-4B and 8B-8B); the second seed's repo-level comparison is cross-size (8B \cls{} vs.\ 4B \cwm{}), not an apple-to-apple same-size match. No downstream re-repair experiment validates whether per-test diagnostic signals translate to actual fix improvements. Pass-to-pass regression rates are negligible (1.04\% mean, 0\% median), meaning the per-test advantage currently concentrates in fail-to-pass discrimination; regression detection---a potential benefit of per-test granularity---remains untested in practice. Training data comprises synthetic mutations; transfer to naturally occurring developer bugs is untested. A matched-context ablation (\cls{} evaluated at \texttt{max\_seq\_length}$=$2,048) confirms that $>$95\% of the \cls{}--\cwm{} gap stems from formulation differences, not input context disparity. The oracle analysis assumes ground-truth test labels; real-world per-test advantage is upper-bounded by classifier accuracy.
10	
11	\paragraph{Future work.}
12	\cls{}--\cwm{} error complementarity (oracle: 90.63\%) motivates ensemble verification that routes instances by predicted output complexity---using generation when outputs are simple and classification when they are complex. Per-test failure signals enable diagnostic re-repair: localizing faults from per-test verdicts rather than discarding failed patches outright. Completing cross-model repo-level validation, multi-seed repo-level replication, and integration with test-time scaling systems (best-of-$N$ with per-test reranking) are natural next steps.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dd3a81f-5da6-45ad-9817-e3bbce0a6f7b",
  "isSidechain": true,
  "promptId": "fffa33bf-46e0-4626-a07a-357495c4180f",
  "agentId": "a4e9c0d907007e01f",
  "type": "user",
  "uuid": "f147dff6-7535-4021-9718-bd8461683a39",
  "sourceToolAssistantUUID": "7dd3a81f-5da6-45ad-9817-e3bbce0a6f7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T15:44:42.860Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bf72RTcQJPbeoYfsHp6wQS`</summary>

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
  "parentUuid": "f147dff6-7535-4021-9718-bd8461683a39",
  "isSidechain": true,
  "agentId": "a4e9c0d907007e01f",
  "requestId": "req_011Cb6WHsZsrSynorK9pj81s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b18bc0dd-2651-4544-ba99-d2be866713e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JoJFcw17p9MFVhQWyLcpJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2919,
      "cache_read_input_tokens": 26280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2919,
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

_source line 14 · 2026-05-16T15:44:42.865Z_

<details><summary>↩ Tool result · `toolu_01Bf72RTcQJPbeoYfsHp6wQS`</summary>

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
  "parentUuid": "b18bc0dd-2651-4544-ba99-d2be866713e7",
  "isSidechain": true,
  "promptId": "fffa33bf-46e0-4626-a07a-357495c4180f",
  "agentId": "a4e9c0d907007e01f",
  "type": "user",
  "uuid": "1139e8f4-725f-410d-ae4d-1a5f2d3256d3",
  "sourceToolAssistantUUID": "b18bc0dd-2651-4544-ba99-d2be866713e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T15:44:43.186Z_

<details open><summary>🔧 Tool call — Read · `toolu_011FiwLGzGC8iPRwHWHNBBrq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1139e8f4-725f-410d-ae4d-1a5f2d3256d3",
  "isSidechain": true,
  "agentId": "a4e9c0d907007e01f",
  "requestId": "req_011Cb6WHsZsrSynorK9pj81s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eceff26f-e170-413c-9378-a55f867ede8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JoJFcw17p9MFVhQWyLcpJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2919,
      "cache_read_input_tokens": 26280,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 26280,
          "cache_creation_input_tokens": 2919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2919,
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

_source line 16 · 2026-05-16T15:44:43.191Z_

<details><summary>↩ Tool result · `toolu_011FiwLGzGC8iPRwHWHNBBrq`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eceff26f-e170-413c-9378-a55f867ede8b",
  "isSidechain": true,
  "promptId": "fffa33bf-46e0-4626-a07a-357495c4180f",
  "agentId": "a4e9c0d907007e01f",
  "type": "user",
  "uuid": "e7912bf6-a6f6-4452-a8c3-8572a24050a1",
  "sourceToolAssistantUUID": "eceff26f-e170-413c-9378-a55f867ede8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T15:44:45.877Z_

<details open><summary>🔧 Tool call — Read · `toolu_011UP2uiXeFbegG7NFhCrKY3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib",
  "offset": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7912bf6-a6f6-4452-a8c3-8572a24050a1",
  "isSidechain": true,
  "agentId": "a4e9c0d907007e01f",
  "requestId": "req_011Cb6WJ8ofZosXTM91fw4P6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a6b6e30-6990-4afd-9c56-5bfbba49a4fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GeqS1vWJ2kHiXwGb7ZndB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2718,
      "cache_read_input_tokens": 29199,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2718
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 29199,
          "cache_creation_input_tokens": 2718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2718,
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

_source line 18 · 2026-05-16T15:44:45.883Z_

<details><summary>↩ Tool result · `toolu_011UP2uiXeFbegG7NFhCrKY3`</summary>

```text
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
174	% === Task Reformulation NLP ===
175	
176	@inproceedings{rajpurkar2016squad,
177	  title={{SQuAD}: 100,000+ Questions for Machine Comprehension of Text},
178	  author={Rajpurkar, Pranav and Zhang, Jian and Lopyrev, Konstantin and Liang, Percy},
179	  booktitle={EMNLP},
180	  year={2016}
181	}
182	
183	@inproceedings{lewis2020bart,
184	  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},
185	  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},
186	  booktitle={ACL},
187	  year={2020}
188	}
189	
190	@article{raffel2020t5,
191	  title={Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
192	  author={Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J},
193	  journal={JMLR},
194	  volume={21},
195	  number={140},
196	  pages={1--67},
197	  year={2020}
198	}
199	
200	% === Statistical Methods ===
201	
202	@article{schuirmann1987tost,
203	  title={A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},
204	  author={Schuirmann, Donald J},
205	  journal={Journal of Pharmacokinetics and Biopharmaceutics},
206	  volume={15},
207	  number={6},
208	  pages={657--680},
209	  year={1987}
210	}
211	
212	@book{davison1997bootstrap,
213	  title={Bootstrap Methods and their Application},
214	  author={Davison, Anthony C and Hinkley, David V},
215	  publisher={Cambridge University Press},
216	  year={1997}
217	}
218	
219	@article{shrout1979icc,
220	  title={Intraclass Correlations: Uses in Assessing Rater Reliability},
221	  author={Shrout, Patrick E and Fleiss, Joseph L},
222	  journal={Psychological Bulletin},
223	  volume={86},
224	  number={2},
225	  pages={420--428},
226	  year={1979},
227	  doi={10.1037/0033-2909.86.2.420}
228	}
229	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a6b6e30-6990-4afd-9c56-5bfbba49a4fe",
  "isSidechain": true,
  "promptId": "fffa33bf-46e0-4626-a07a-357495c4180f",
  "agentId": "a4e9c0d907007e01f",
  "type": "user",
  "uuid": "90306d8b-a6ff-4945-9cf4-eb1415a93a8a",
  "sourceToolAssistantUUID": "0a6b6e30-6990-4afd-9c56-5bfbba49a4fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T15:45:28.009Z_

Now I have a thorough understanding of the paper. Let me produce the review.

---

## Review: "Classification Scales Where Generation Fails: Per-Test Binary Verification for Code Repair"

**Reviewer R2 — Focus: Novelty and Related Work**

### Summary

This paper proposes reformulating execution simulation for code repair verification from output generation (CWM) to per-test binary pass/fail classification (CLS). The main finding is complexity-dependent: at function level the two are near-equivalent (~1pp gap), but at repository level CLS dominates by 19-26pp because CWM suffers catastrophic format compliance collapse (53-74% unparseable outputs). The paper provides controlled comparisons across formulations, model sizes, and families, plus an oracle accuracy-utility analysis.

### Strengths

- **Thorough experimental methodology.** Controlled comparisons (same model, data, compute, LoRA config) isolate the formulation effect cleanly. Statistical treatment is rigorous: clustered bootstrap, TOST equivalence testing, ICC for within-problem correlation.
- **The complexity-dependent framing is well-executed.** Showing near-equivalence at function level prevents the trivial objection that "classification is just easier," making the repo-level divergence more informative.
- **Useful diagnostic insight.** The analysis of CWM failure modes (format collapse, degradation with scale, relaxed matching making things worse) provides genuinely informative understanding of why generation fails.
- **Related work is reasonably comprehensive.** Five paragraphs covering execution simulation, LLM verification, learned verifiers (LEVER, CodeT), APR, and NLP reformulation. The positioning against LEVER and CodeT is appropriate and honest about differences.
- **Oracle framework is a nice formalization.** The ICC-based block-correlation model predicting when per-test granularity helps is elegant and testable.

### Weaknesses

**W1 (Major): Core novelty is limited.** The insight that binary classification is more robust than unconstrained generation when outputs are complex is well-established in NLP (the paper itself cites T5/BART/SQuAD as precedent). Applying this to code verification is straightforward engineering. The "finding" that generation fails when output complexity overwhelms the model is essentially a restatement of known limitations of exact-match evaluation on long sequences. A top venue would expect either (a) a surprising result or (b) a large-scale practical system—this provides neither.

**W2 (Major): The CWM comparison is arguably unfair.** The original Code World Model is a 32B model trained on massive execution traces; this paper fine-tunes 4B/8B models with LoRA and calls them "CWM." The comparison isolates formulation differences but does not demonstrate that the generation approach fundamentally cannot work—only that small LoRA-adapted models cannot reliably generate structured outputs for complex repo-level code. The paper acknowledges this ("not a reproduction of the 32B Code World Model") but the framing still implies generation is inherently flawed.

**W3 (Moderate): Missing key related work.** The paper omits several relevant lines of work: (1) CodeRM and process reward models for code (Lightman et al., 2023 style ORM/PRM applied to code); (2) execution prediction as test-outcome classification in mutation testing literature (predictive mutation testing); (3) APPS/CodeContests evaluation approaches that predict test outcomes; (4) RewardBench-style evaluations of code reward models. The claim "no prior work studies per-test binary classification" is too strong—predicting test outcomes per-test is implicit in many testing/verification systems.

**W4 (Moderate): Single-seed repo-level results undermine the headline claim.** The primary contribution (19-26pp gap at repo level) rests on 1-2 seeds per configuration. Given that the paper demonstrates high seed variance in some settings (CWM 6.7B sigma=1.49), the repo-level results require more replication to be convincing at a top venue.

**W5 (Minor): No downstream validation.** The re-repair experiment mentioned in the paper summary is absent from the actual paper content (only mentioned as future work in conclusion). Without showing that per-test diagnostics actually improve repair outcomes, the practical value remains hypothetical.

**W6 (Minor): "Classification vs Generation in NLP" framing is shallow.** The cited works (T5, BART, SQuAD) are tangential—none study when classification beats generation as a function of task complexity. The connection is asserted rather than substantiated.

### Questions for Authors

1. What happens with the actual 32B CWM model on your repo-level benchmark? Does format compliance collapse persist at that scale with the original training?
2. Have you tried constrained decoding (forcing structured JSON output) for CWM to eliminate the format compliance issue? This would isolate whether the problem is format adherence vs. actual prediction quality.
3. For the "no prior work" claim: how does this differ from predictive mutation testing (e.g., predicting mutant kill/survive outcomes), which is per-test binary classification for code?
4. Could you report per-seed repo-level results for CLS as well? The single-seed CLS 4B result (83.63%) vs. the 75.33% mentioned for seed 123 suggests substantial checkpoint selection variance that could narrow the gap.

### Preliminary Score

**Score: 3 (Weak Reject)**  
**Confidence: 4/5**

### One-line Verdict

A well-executed empirical comparison, but the core insight (classification is more robust than generation for complex outputs) is unsurprising, the headline repo-level results are under-replicated, and the novelty claim is overstated relative to prior work on learned code verifiers and task reformulation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90306d8b-a6ff-4945-9cf4-eb1415a93a8a",
  "isSidechain": true,
  "agentId": "a4e9c0d907007e01f",
  "requestId": "req_011Cb6WJLNS3PEfRfvCAt2ia",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ee92423-0327-43bb-a535-d20278d2c3d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "4f8bc5e1-312e-4642-9781-39d3fe060377",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GbA9d6PqyeJMbw1fkKPnV8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2127,
      "cache_read_input_tokens": 31917,
      "output_tokens": 1346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2127
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1346,
          "cache_read_input_tokens": 31917,
          "cache_creation_input_tokens": 2127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2127,
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
