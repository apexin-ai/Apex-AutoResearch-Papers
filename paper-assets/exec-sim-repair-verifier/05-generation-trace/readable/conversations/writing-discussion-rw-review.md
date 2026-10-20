# writing discussion rw review

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_writing_discussion-rw-review_20260521T192137.jsonl`
- **Structured JSON:** [`a0186df2567e0a60b0a7.json`](../../sessions/a0/a0186df2567e0a60b0a7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-21T19:26:28.625946+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T19:26:28.626332+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. Verification formulations span trajectory-level reward~\cite{shum2025swerm,zhu2026codescaler}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. Our \cls{} provides per-test (process) supervision while \traj{} provides outcome-level; the PRM literature compares supervision granularity given a fixed output format, while we additionally vary the output format (\cwm{} generation vs.\ \cls{} classification).
9	
10	\paragraph{Repair, Mutation Testing, and Task Framing.}
11	CodeRL~\cite{le2022coderl}, AlphaCode~\cite{li2022alphacode,alphacode2023team}, and Reflexion~\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\cite{jimenez2024swebench,chowdhury2024swebenchverified} provides benchmarks; SWE-agent~\cite{yang2
…[truncated 895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T19:26:28.626532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T19:26:28.626706+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} reaches parity on Qwen3 but not DeepSeek-Coder (2.69\pp{}). Per-test classification achieves 217$\times$ higher throughput while providing diagnostic signal whose downstream utility remains unconfirmed ($n{=}44$, $p{=}0.42$). Complementary errors (oracle: 90.63\%/95.83\%; single-seed) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA fine-tuning, a significant interaction ($z{=}-23.7$) confirms divergence (19--26\pp{}, single-seed variant-level), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). Variant-level analysis reveals three distinct failure modes (format collapse, decision collapse, aggregation penalty) consistent across model families. At function level, formulation choice is immaterial; at repository level under ${\leq}$8B LoRA, \cls{} is recommended for both accuracy and throughput. Behavior at larger scale remains open~\cite{meta2025cwm}.
5	
6	\section*{Limitations}
7	
8	Most repo-level comparisons use limited seeds; the gap (19--26\pp{}) exceeds any single assessed confound (\S\ref{sec:threats}), but correlated confounds mean definitive causal attribution requires multi-seed replication. Our \cwm{} baseline uses ${\leq}$8B LoRA fine-tuning, not the original 32B CWM with execution trace mid-training~\cite{meta2025cwm}; at larger scale, the generation bottleneck may diminish. Training data comprises synthetic mutations~\cite{andrews2005mutation,just2014mutants}; the synthetic-to-real transfer gap for absolute accuracy remains untested, though the coupling effect supports relative ranking validity (Appendix~\ref{app:limitations}). Model coverage is limited to 6--8B code-specia
…[truncated 147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T19:26:28.626924+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T19:26:28.627213+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss due to length-mismatched sequences, which defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Mo
…[truncated 18912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T19:26:28.627445+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T19:26:28.627594+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T19:26:28.627724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T19:26:28.628010+00:00_

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
31	@article{venkatkrishna2026aletheia,
32	  title={Aletheia: What Makes {RLVR} For Code Verifiers Tick?},
33	  author={Venkatkrishna, Vatsal and Paul, Indraneil and Gurevych, Iryna},
34	  journal={arXiv preprint arXiv:2601.12186},
35	  year={2026}
36	}
37	
38	@article{lee2026solidcoder,
39	  title={{SolidCoder}: Bridging the Mental-Reality Gap in {LLM} Code Generation through Concrete Execution},
40	  author={Lee, Woojin and Huang, Jin-Xia},
41	  journal={arXiv preprint arXiv:2604.19825},
42	  year={2026}
43	}
44	
45	@article{nye2021scratchpad,
46
…[truncated 18395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T19:26:28.628204+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "execution-free code verification LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "execution-free code verification LLM 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T19:26:28.628334+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM code repair verification reward model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM code repair verification reward model 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T19:26:28.628458+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "code verifier formulation classification generation comparison 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "code verifier formulation classification generation comparison 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T19:26:28.628621+00:00_

Web search results for query: "execution-free code verification LLM 2025 2026"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"[2507.13290] Towards Formal Verification of LLM-Generated Code from Natural Language Prompts","url":"https://arxiv.org/abs/2507.13290"},{"title":"Best LLMs for coding in 2026","url":"https://www.builder.io/blog/best-llms-for-coding"},{"title":"StackPilot: Autonomous Function Agents for Scalable and Environment-Free Code Execution","url":"https://arxiv.org/pdf/2508.11665"},{"title":"[2026] Best LLMs for Coding Ranked: Free, Local, Open Models","url":"https://nutstudio.imyfone.com/llm-tips/best-llm-for-coding/"},{"title":"6 Best LLMs for Coding To Try in 2026 [Comparison List]","url":"https://zencoder.ai/blog/best-llm-for-coding"},{"title":"Chain of Targeted Verification Questions to Improve the Reliability of   Code Generated by LLMs","url":"https://arxiv.org/pdf/2405.13932"}]

Based on the search results, here are the key findings related to execution-free code verification and LLMs in 2025-2026:

## Execution-Free Code Verification

REDO is a notable work on "Execution-Free Runtime Error Detection for COding Agents" from 2024, representing recent advances in this area.

Astrogator is a formal verification system for LLM-generated code that implements ideas for verifying code against formal specifications, implemented for the Ansible programming language used in system administration. The verifier is able to verify correct code in 83% of cases and identify incorrect code in 92% on a benchmark suite of 21 code-generation tasks.

## Current Verification Challenges

Current verification approaches primarily rely on automated compilation and unit testing against benchmark datasets, which enables large-scale evaluation by checking syntactic validity and functional correctness through test cases, but has
…[truncated 546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T19:26:28.628833+00:00_

Web search results for query: "LLM code repair verification reward model 2025 2026"

Links: [{"title":"RLVR: Verifiable Rewards for Reliable Enterprise LLMs | Appen","url":"https://www.appen.com/blog/rlvr"},{"title":"5 Open-Source Coding LLMs You Can Run Locally in 2026","url":"https://www.labellerr.com/blog/best-coding-llms/"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"RLVR Beyond Math and Code: The Verifier Problem Nobody Has Solved | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/rlvr-beyond-math-code/"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"},{"title":"Chain of Targeted Verification Questions to Improve the Reliability of   Code Generated by LLMs","url":"https://arxiv.org/pdf/2405.13932"},{"title":"Detect Repair Verify for Securing LLM Generated Code: A Multi-Language Empirical Study","url":"https://arxiv.org/pdf/2603.00897"}]

Here are the search results for "LLM code repair verification reward model 2025 2026":

## Key Findings

**Reinforcement Learning with Verifiable Rewards (RLVR)**

RLVR trains a model to earn a reward only when its output passes programmatic checks, and the system samples multiple candidates, runs them through verifiers, and updates the policy toward behaviors that pass. RLVR optimizes for objective correctness and format compliance by rewarding outputs that satisfy automated verifiers.

**Applications to Code Tasks**

Evidence from recent training efforts highlights that large models trained with rule-based, accuracy-oriented rewards show substantia
…[truncated 1076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T19:26:28.629016+00:00_

Web search results for query: "code verifier formulation classification generation comparison 2025 2026"

Links: [{"title":"Preprint. Accepted at the ICLR 2026 LIT Workshop","url":"https://arxiv.org/pdf/2602.09924"},{"title":"CVeDRL: An Efficient Code Verifier via Difficulty-aware Reinforcement Learning","url":"https://arxiv.org/pdf/2601.22803"},{"title":"Aletheia: What Makes RLVR For Code Verifiers Tick?","url":"https://arxiv.org/pdf/2601.12186"},{"title":"On the Query Complexity of Verifier-Assisted Language Generation","url":"https://arxiv.org/pdf/2502.12123"},{"title":"Pareto Optimal Code Generation","url":"https://arxiv.org/pdf/2506.10056"},{"title":"Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning","url":"https://arxiv.org/pdf/2502.13820"},{"title":"Scaling Agentic Verifier for Competitive Coding","url":"https://arxiv.org/pdf/2602.04254"}]

Based on the search results, here's what I found about code verifier formulation, classification, generation, and comparison for 2025-2026:

## Code Verifier Approaches

Code verifiers take the problem description and candidate code solution as input and leverage LLMs to generate unit tests, which consist of reasonable input and corresponding output pairs. By executing candidate code solutions and their unit tests, the execution outcomes are examined to identify the optimal code solutions among all candidates.

## Key Verification Methods

Recent research distinguishes several approaches:

1. **Synthetic Verifiers**: New benchmarks (HE-R, HE-R+, MBPP-R, and MBPP-R+) analyzed synthetic verification methods with standard, reasoning-based, and reward-based LLMs, showing that reasoning can significantly improve test case generation and that scaling the number of test cases enhances verification accuracy.

2. **Surrogate Code-Execution Verifiers**: Surrogate code-execution verifiers are models trained to score code snippets based on execution outcomes without actually executing them.

3. **Verifier-Ass
…[truncated 1083 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T19:26:28.629198+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CVeDRL code verifier difficulty-aware reinforcement learning 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CVeDRL code verifier difficulty-aware reinforcement learning 2026 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T19:26:28.629325+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Scoring Verifiers\" synthetic verification code reasoning 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Scoring Verifiers\" synthetic verification code reasoning 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T19:26:28.629473+00:00_

Web search results for query: "CVeDRL code verifier difficulty-aware reinforcement learning 2026 arxiv"

Links: [{"title":"[2601.22803] CVeDRL: An Efficient Code Verifier via Difficulty-aware Reinforcement Learning","url":"https://arxiv.org/abs/2601.22803"},{"title":"CVeDRL: An Efficient Code Verifier via Difficulty-aware Reinforcement Learning","url":"https://arxiv.org/pdf/2601.22803"},{"title":"CVeDRL: An Efficient Code Verifier via Difficulty-aware Reinforcement Learning","url":"https://arxiv.org/html/2601.22803"},{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/pdf/2510.00915"},{"title":"EvolveCoder: Evolving Test Cases via Adversarial Verification for Code Reinforcement Learning","url":"https://arxiv.org/pdf/2603.12698"}]

I found the paper! Here's what I discovered:

**CVeDRL: An Efficient Code Verifier via Difficulty-aware Reinforcement Learning** is a paper by Ji Shi, Peiming Guo, Meishan Zhang, and others from Harbin Institute of Technology, submitted on January 30, 2026 to arXiv.

**Overview:**
The paper addresses how code verifiers play a critical role in post-verification for LLM-based code generation, yet existing supervised fine-tuning methods suffer from data scarcity, high failure rates, and poor inference efficiency.

**Key Approach:**
While reinforcement learning offers a promising alternative through execution-driven rewards without labeled supervision, naive RL fails to generate effective unit tests for difficult branches. The authors theoretically show that branch coverage, sample difficulty, syntactic and functional correctness can be jointly modeled as RL rewards, and design syntax- and functionality-aware rewards alongside branch- and sample-difficulty-aware RL using exponential reward shaping and static analysis metrics.

**Results:**
CVeDRL achieves state-of-the-art performance with only 0.6B parameters, yielding up to 28.97% higher pass rate and 15.08% higher branch cove
…[truncated 262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T19:26:28.629653+00:00_

Web search results for query: ""Scoring Verifiers" synthetic verification code reasoning 2025 arxiv"

Links: [{"title":"[Literature Review] Scoring Verifiers: Evaluating Synthetic Verification in Code and Reasoning","url":"https://www.themoonlight.io/en/review/scoring-verifiers-evaluating-synthetic-verification-in-code-and-reasoning"},{"title":"[2502.13820] Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning","url":"https://arxiv.org/abs/2502.13820"},{"title":"[2502.13820v3] Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning","url":"https://arxiv.org/abs/2502.13820v3"},{"title":"Scoring Verifiers: Evaluating Synthetic Verification in Code and Reasoning","url":"https://arxiv.org/html/2502.13820v1"},{"title":"Scoring Verifiers: Evaluating Synthetic Verification in Code and Reasoning","url":"https://www.arxiv.org/pdf/2502.13820v1"},{"title":"(PDF) Scoring Verifiers: Evaluating Synthetic Verification in Code and Reasoning","url":"https://www.researchgate.net/publication/389167994_Scoring_Verifiers_Evaluating_Synthetic_Verification_in_Code_and_Reasoning"},{"title":"Software Engineering Feb 2025","url":"https://www.arxiv.org/list/cs.SE/2025-02?skip=325&show=250"},{"title":"Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning","url":"https://arxiv.org/html/2502.13820v3"},{"title":"Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning","url":"https://arxiv.org/pdf/2502.13820"},{"title":"Computer Science Feb 2025","url":"https://www.arxiv.org/list/cs/2025-02?skip=6975&show=50"}]

I found comprehensive information about the "Scoring Verifiers" paper on arXiv. Here's what the search revealed:

## Overview

The paper "Scoring Verifiers: Evaluating Synthetic Verification in Code and Reasoning" is authored by Aleksander Ficek, Somshubra Majumdar, Vahid Noroozi, and Boris Ginsburg and presents a comprehensive approach to evaluating the effectiveness of synthetic verification methods for v
…[truncated 1117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T19:26:28.629845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T19:26:28.630006+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\graphicspath{{../../artifacts/}}
21	
22	% Lists
23	\usepackage{enumitem}
24	
25	% Custom commands
26	\newcommand{\cls}{\textsc{Cls}}
27	\newcommand{\cwm}{\textsc{Cwm}}
28	\newcommand{\traj}{\textsc{Traj}}
29	\newcommand{\fone}{F\textsubscript{1}}
30	\newcommand{\pp}{\,\text{pp}}
31	\newcommand{\tbd}{\textsc{tbd}}
32	
33	\title{The Formulation Design Space for Execution-Free Code Verification:\\A Systematic Empirical Study}
34	\author{Anonymous}
35	
36	\begin{document}
37	\maketitle
38	
39	\input{abstract}
40	
41	\input{introduction}
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
46	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
47	\label{fig:reformulation}
48	\end{figure*}
49	
50	\input{method}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T19:26:28.630157+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T19:26:28.630315+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimenta
…[truncated 2614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T19:26:28.630615+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "old_string": "confirming the bottleneck is semantic rather than syntactic (Appendix~\\ref{app:extended_analysis}(c)).",
  "new_string": "confirming the bottleneck is semantic rather than syntactic (Appendix~\\ref{app:extended_analysis}(c)). This extends the formulation-dependent accuracy tradeoffs documented for NLP tasks~\\cite{raffel2020t5} to a regime where output complexity causes format compliance itself to become a dominant failure mode."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "old_string": "confirming the bottleneck is semantic rather than syntactic (Appendix~\\ref{app:extended_analysis}(c)).",
    "new_string": "confirming the bottleneck is semantic rather than syntactic (Appendix~\\ref{app:extended_analysis}(c)). This extends the formulation-dependent accuracy tradeoffs documented for NLP tasks~\\cite{raffel2020t5} to a regime where output complexity causes format compliance itself to become a dominant failure mode."
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T19:26:28.630864+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T19:26:28.631013+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
  "old_string": "At function level, formulation choice is immaterial; at repository level under ${\\leq}$8B LoRA, \\cls{} is recommended for both accuracy and throughput. Behavior at larger scale remains open~\\cite{meta2025cwm}.\n\n\\section*{Limitations}",
  "new_string": "At function level, formulation choice is immaterial; at repository level under ${\\leq}$8B LoRA, \\cls{} is recommended for both accuracy and throughput.\n\nThree directions follow. First, oracle gains (90.63\\%/95.83\\%) motivate complexity-aware routing among formulations; the failure mode taxonomy (\\S\\ref{sec:repo}) provides candidate routing features. Second, the generation bottleneck is semantic---four syntactic interventions fail (Appendix~\\ref{app:extended_analysis}(g))---suggesting that closing the gap requires capacity scaling or execution trace pretraining~\\cite{meta2025cwm}; testing at 32B+ scale would resolve the primary open question. Third, larger-scale evaluation of per-test diagnostics for downstream repair ($n{=}44$ in our pilot) would test whether the 217$\\times$ throughput advantage of \\cls{} extends beyond verification to repair pipelines.\n\n\\section*{Limitations}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
    "old_string": "At function level, formulation choice is immaterial; at repository level under ${\\leq}$8B LoRA, \\cls{} is recommended for both accuracy and throughput. Behavior at larger scale remains open~\\cite{meta2025cwm}.\n\n\\section*{Limitations}",
    "new_string": "At function level, formulation choice is immaterial; at repository level under ${\\leq}$8B LoRA, \\cls{} is recommended for both accuracy and throughput.\n\nThree directions follow. First, oracle gains (90.63\\%/95.83\\%) motivate complexity-aware routing among formulations; the failure mode taxonomy (\\S\\ref{sec:repo}) provides candidate routing features. Second, the generation bottleneck is semantic---four syntactic interventions fail (Appendix~\\ref{app:extended_analysis}(g))---suggesting that closing the gap requires capacity scaling or execution trace pretraining~\\cite{meta2025cwm}; testing at 32B+ scale would resolve the primary open question. Third, larger-scale evaluation of per-test diagnostics for downstream repair ($n{=}44$ in our pilot) would test whether the 217$\\times$ throughput advantage of \\cls{} extends beyond verification to repair pipelines.\n\n\\section*{Limitations}"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T19:26:28.631183+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T19:26:28.631338+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -20",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T19:26:28.631503+00:00_

ic/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/u
crr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (21 pages, 411816 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T19:26:28.631662+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"Warning\" main.log && grep \"Warning\" main.log | grep -v \"Font\" | grep -v \"microtype\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"Warning\" main.log && grep \"Warning\" main.log | grep -v \"Font\" | grep -v \"microtype\" | head -10"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T19:26:28.631812+00:00_

11
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T19:26:28.631954+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T19:26:28.632096+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} reaches parity on Qwen3 but not DeepSeek-Coder (2.69\pp{}). Per-test classification achieves 217$\times$ higher throughput while providing diagnostic signal whose downstream utility remains unconfirmed ($n{=}44$, $p{=}0.42$). Complementary errors (oracle: 90.63\%/95.83\%; single-seed) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA fine-tuning, a significant interaction ($z{=}-23.7$) confirms divergence (19--26\pp{}, single-seed variant-level), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). Variant-level analysis reveals three distinct failure modes (format collapse, decision collapse, aggregation penalty) consistent across model families. At function level, formulation choice is immaterial; at repository level under ${\leq}$8B LoRA, \cls{} is recommended for both accuracy and throughput.
5	
6	Three directions follow. First, oracle gains (90.63\%/95.83\%) motivate complexity-aware routing among formulations; the failure mode taxonomy (\S\ref{sec:repo}) provides candidate routing features. Second, the generation bottleneck is semantic---four syntactic interventions fail (Appendix~\ref{app:extended_analysis}(g))---suggesting that closing the gap requires capacity scaling or execution trace pretraining~\cite{meta2025cwm}; testing at 32B+ scale would resolve the primary open question. Third, larger-scale evaluation of per-test diagnostics for downstream repair ($n{=}44$ in our pilot) would test whether the 217$\times$ throughput advantage of \cls{} extends beyond verification to repair pipelines.
7	
8	\section*{Limitations}
9	
10	Most repo-level comparisons use limited seeds; the gap (
…[truncated 808 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T19:26:28.632241+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "offset": "170",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "offset": "170",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T19:26:28.632387+00:00_

170	\paragraph{Aggregation penalty.} Under the all-pass rule, a single false negative flips the variant verdict. The penalty ranges from 1.36\pp{} (DeepSeek s42) to 19\pp{} (Qwen3-4B), depending on fail recall and test count (Appendix Table~\ref{tab:variant_level}). Val-based checkpoint selection biases toward per-test accuracy at the expense of fail recall, which amplifies the penalty. \traj{} avoids this by predicting variant outcomes directly (72.91--77.08\%). The penalty is predictable from test count: function-level variants ($\bar{T} \approx 2.3$) incur negligible penalty, while repo-level variants ($\bar{T} \gg 10$) incur substantial penalty, both the \emph{advantage} and \emph{cost} of per-test granularity concentrate at high $T$ (Appendix~\ref{app:extended_analysis}(a)).
171	
172	\paragraph{Why does generation degrade at repo level?} Output space complexity increases nonlinearly: function-level outputs are short strings (integers, booleans); repo-level outputs are unconstrained execution traces (mean ${\sim}$477 tokens) where errors compound multiplicatively, and cause format collapse (53--74\% unparseable). Even among parseable outputs, accuracy (38--43\%) is below majority baseline; forced parsing that rescues 90.6\% of unparseable outputs achieves only 49.4\% accuracy, confirming the bottleneck is semantic rather than syntactic (Appendix~\ref{app:extended_analysis}(c)). This extends the formulation-dependent accuracy tradeoffs documented for NLP tasks~\cite{raffel2020t5} to a regime where output complexity causes format compliance itself to become a dominant failure mode.
173	
174	\cls{} achieves 217$\times$ higher throughput than \cwm{} (1 output token vs.\ avg 477), consistent across both model families.
175	
176	\paragraph{Error complementarity.} At function level, \cls{} and \cwm{} exhibit partial complementarity: both are FP-dominant (over-predict failure), but at different rates (\cls{} 56.5\%, \cwm{} 70.3\%; Appendix~\ref{app:extended_analysis}(a)
…[truncated 904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_discussion-rw-review_20260521T192137",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-21T19:26:28.632587+00:00_

Both edits applied cleanly. Compilation passes with no errors.

---

## Summary

### Audit findings per file

**Related Work** (`related_work.tex`):
- Coverage is comprehensive across all relevant axes (execution simulation, PRM/ORM, repair/mutation, task framing)
- 2025-2026 literature well-represented (12+ recent papers cited)
- No critical missing papers: CVeDRL (2026) and Scoring Verifiers (2025) were the closest candidates but both are tangential (test-case generation, not formulation comparison)
- Differentiation from existing work is clear; no changes needed

**Analysis** (`experiments.tex` §5.5):
- "Why does generation degrade" lacked a callback to the formulation literature in Related Work
- Re-repair null result was reported but without deeper analytical framing (left as-is since the small sample is acknowledged and adding speculation would weaken the paper)

**Conclusion** (`conclusion.tex`):
- No future work directions existed -- significant gap for EMNLP
- Ended weakly on "Behavior at larger scale remains open"
- Did answer the research question but implicitly

### Modifications made

1. **`experiments.tex` line 172** -- Added one sentence in "Why does generation degrade" connecting the format collapse finding back to the T5 formulation literature (Raffel et al., 2020), establishing that this paper extends known formulation-dependent tradeoffs to a new severity regime. Creates the Related Work callback the section was missing.

2. **`conclusion.tex` lines 5-6** -- Added a future work paragraph with three concrete directions: (a) complexity-aware routing motivated by oracle gains, with the failure mode taxonomy as routing features; (b) 32B+ scale testing to determine whether the semantic generation bottleneck persists, since syntactic interventions fail; (c) larger-scale re-repair evaluation to test whether CLS's throughput advantage extends to downstream repair pipelines. Removed the weak closing sentence.

### WebSearch results
No critical missing references found. The paper's 2025-2026 citation coverage is thorough.

### Compilation
Passes cleanly. 21 pages, no errors, only standard float placement warnings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_discussion-rw-review_20260521T192137"
}
```

</details>

---
