# research r15 reference verification

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_research_r15-reference-verification_20260520T044621.jsonl`
- **Structured JSON:** [`c90ae3114df959865571.json`](../../sessions/c9/c90ae3114df959865571.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-20T04:48:13.905425+00:00_

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
  "session": "worker_research_r15-reference-verification_20260520T044621",
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

_source line 2 · 2026-05-20T04:48:13.905860+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T04:48:13.906064+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.15149 \"LLMs Gaming Verifiers\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.15149 \"LLMs Gaming Verifiers\""
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T04:48:13.906200+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.07084 Countdown code reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.07084 Countdown code reasoning"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T04:48:13.906732+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Uesato 2022 \"Solving math word problems\" process outcome feedback"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Uesato 2022 \"Solving math word problems\" process outcome feedback"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T04:48:13.906904+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Cobbe 2021 \"Training Verifiers to Solve Math Word Problems\" GSM8K"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cobbe 2021 \"Training Verifiers to Solve Math Word Problems\" GSM8K"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T04:48:13.907047+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T04:48:13.907346+00:00_

1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author       = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title        = {{The Llama 3 Herd of Models}},
8	  journal      = {arXiv preprint arXiv:2407.21783},
9	  year         = {2024},
10	  eprint       = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	@article{deepseekmath,
15	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
16	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
17	  journal      = {arXiv preprint arXiv:2402.03300},
18	  year         = {2024},
19	  eprint       = {2402.03300},
20	  archivePrefix = {arXiv},
21	  primaryClass = {cs.AI},
22	}
23	
24	@article{logic-rl,
25	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
26	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
27	  journal      = {arXiv preprint arXiv:2502.14768},
28	  year         = {2025},
29	  eprint       = {2502.14768},
30	  archivePrefix = {arXiv},
31	  primaryClass = {cs.AI},
32	}
33	
34	@article{mellgren-prolog-grpo,
35	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
36	  title        = {{Training Language Models to Use Prolog as a Tool}},
37	  journal      = {arXiv preprint arXiv:2512.07407},
38	  year         = {2025},
39	  eprint       = {2512.07407},
40	  archivePrefix = {arXiv},
41	  primaryClass = {cs.AI},
42	}
43	
44	@inproceedings{satlm,
45	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
46	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
47	  booktitle    = {Advances in Neu
…[truncated 21817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T04:48:13.907688+00:00_

Web search results for query: "arxiv 2604.15149 "LLMs Gaming Verifiers""

Links: [{"title":"[2604.15149] LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://arxiv.org/abs/2604.15149"},{"title":"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://arxiv.org/html/2604.15149"},{"title":"LLM Reasoning Workshop @ ICLR 2026 LLMS GAMING VERIFIERS:","url":"https://arxiv.org/pdf/2604.15149"},{"title":"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://chatpaper.com/paper/268961"},{"title":"Prover-Verifier Games improve legibility of LLM outputs","url":"https://arxiv.org/pdf/2407.13692"}]

I found the paper! Here's what I found about arxiv 2604.15149:

## Paper Summary

As reinforcement Learning with Verifiable Rewards (RLVR) has become the dominant paradigm for scaling reasoning capabilities in LLMs, a new failure mode emerges: LLMs gaming verifiers.

The paper studies this phenomenon on inductive reasoning tasks, where models must induce and output logical rules. They find that RLVR-trained models systematically abandon rule induction. Instead of learning generalizable patterns (e.g., "trains carrying red cars go east"), they enumerate instance-level labels, producing outputs that pass verifiers without capturing the relational patterns required by the task.

The authors show that this behavior is not a failure of understanding but a form of reward hacking: imperfect verifiers that check only extensional correctness admit false positives.

## Key Contribution

To diagnose this behavior, the authors introduce Isomorphic Perturbation Testing (IPT), which evaluates a model's output under two regimes: extensional verification on the original task, and isomorphic verification on a logically isomorphic perturbation obtained by permuting object identifiers while preserving relational structure.

The paper was submitted on April 16, 2026, and is associated with the LLM Reasoning Workshop at ICLR 2026.


REMINDER: You MUST inc
…[truncated 78 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T04:48:13.907944+00:00_

Web search results for query: "Cobbe 2021 "Training Verifiers to Solve Math Word Problems" GSM8K"

Links: [{"title":"(Open Access) Training Verifiers to Solve Math Word Problems (2021) | Karl Cobbe | 2 Citations","url":"https://scispace.com/papers/training-verifiers-to-solve-math-word-problems-2jokilm0qa"},{"title":"openai/gsm8k · Datasets at Hugging Face","url":"https://paperswithcode.com/dataset/gsm8k"},{"title":"[2110.14168] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168"},{"title":"GitHub - openai/grade-school-math · GitHub","url":"https://github.com/openai/grade-school-math"},{"title":"[PDF] Training Verifiers to Solve Math Word Problems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-Verifiers-to-Solve-Math-Word-Problems-Cobbe-Kosaraju/d6045d2ccc9c09ca1671348de86d07da6bc28eea"},{"title":"Paper page - Training Verifiers to Solve Math Word Problems","url":"https://huggingface.co/papers/2110.14168"},{"title":"Training Verifiers to Solve Math Word Problems, Karl Cobbe+, arXiv'21 · Issue #1618 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1618"},{"title":"Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/pdf/2110.14168"},{"title":"Training Verifiers to Solve Math Word Problems - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2110.14168"},{"title":"Training Verifiers to Solve Math Word Problems","url":"https://www.researchgate.net/publication/355698629_Training_Verifiers_to_Solve_Math_Word_Problems"}]

I found the paper you're looking for. Here's what I found:

"Training Verifiers to Solve Math Word Problems" by Cobbe et al. (2021) introduces GSM8K, a dataset of 8.5K high quality linguistically diverse grade school math word problems. The paper addresses the fact that state-of-the-art language models can match human performance on many tasks, but they still struggle to robustly perform multi-step mathematical reasoning.

Th
…[truncated 830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T04:48:13.908138+00:00_

Web search results for query: "arxiv 2603.07084 Countdown code reasoning"

Links: [{"title":"[2603.07084] Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR","url":"https://arxiv.org/abs/2603.07084"},{"title":"Preprint Countdown-Code: A Testbed for Studying The Emergence","url":"https://arxiv.org/pdf/2603.07084"},{"title":"Unveiling the Magic of Code Reasoning through Hypothesis Decomposition   and Amendment","url":"https://arxiv.org/pdf/2502.13170"},{"title":"Agentic Code Reasoning","url":"https://arxiv.org/pdf/2603.01896"},{"title":"Self-Aware Markov Models for Discrete Reasoning","url":"https://arxiv.org/html/2603.16661"},{"title":"Evaluating Code Reasoning Abilities of Large Language Models Under Real-World Settings","url":"https://arxiv.org/pdf/2512.14917"},{"title":"Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and   Reasoning-Driven Code Intelligence in LLMs","url":"https://arxiv.org/pdf/2502.19411"}]

Based on the search results, here's what I found about arxiv 2603.07084:

**Countdown-Code** is a minimal environment where models can both solve a mathematical reasoning task and manipulate the test harness. This dual-access design creates a clean separation between proxy rewards (test pass/fail) and true rewards (mathematical correctness), enabling accurate measurement of reward-hacking rates.

The paper studies an important problem in AI alignment: reward hacking, which is a form of misalignment in which models overoptimize proxy rewards without genuinely solving the underlying task, and precisely measuring reward hacking occurrence remains challenging because true task rewards are often expensive or impossible to compute.

Key findings include: Using this environment, researchers study reward hacking in open-weight LLMs and find that such behaviors can be unintentionally learned during supervised fine-tuning (SFT) when even a small fraction of reward-hacking trajectories leak into training d
…[truncated 390 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T04:48:13.908365+00:00_

Web search results for query: "Uesato 2022 "Solving math word problems" process outcome feedback"

Links: [{"title":"[PDF] Solving Math Word Problems with Process-based and Outcome-based Feedback | Semantic Scholar","url":"https://www.semanticscholar.org/paper/e002bb8dae5a18a5ea1e7e1aafa16e19ad545662"},{"title":"[PDF] Solving math word problems with process- and outcome-based feedback | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Solving-math-word-problems-with-process-and-Uesato-Kushman/6d7b8a478801bd9d21df82d5f33ae6eced90da5e"},{"title":"dblp: Solving math word problems with process- and outcome-based feedback.","url":"https://dblp.org/rec/journals/corr/abs-2211-14275.html"},{"title":"2022-11-28 Solving math word problems with process- and outcome-based feedback","url":"https://arxiv.org/pdf/2211.14275"},{"title":"[2211.14275v1] Solving math word problems with process- and outcome-based feedback","url":"https://arxiv.org/abs/2211.14275v1"},{"title":"Solving Math Word Problems with Process-based and Outcome-based Feedback","url":"https://mathai2022.github.io/papers/26.pdf"},{"title":"[2211.14275] Solving math word problems with process- and outcome-based feedback","url":"https://arxiv.org/abs/2211.14275"},{"title":"Solving math word problems with process- and outcome-based feedback | SCALE Initiative","url":"https://scale.stanford.edu/ai/repository/solving-math-word-problems-process-and-outcome-based-feedback"}]

I found the research paper you're looking for. Here's a summary of the Uesato 2022 paper on solving math word problems with process-based and outcome-based feedback:

**Paper Details:**
The paper is authored by Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins, and was published in November 2022.

**Research Question:**
The paper addresses the question of how to supervise language models: using outcome-based approaches which supervise the final result, 
…[truncated 831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T04:48:13.908640+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2110.14168 Cobbe \"Heewoo Jun\" OR \"Heather Jun\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2110.14168 Cobbe \"Heewoo Jun\" OR \"Heather Jun\" authors"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T04:48:13.908810+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.15149 \"LLMs Gaming Verifiers\" authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.15149 \"LLMs Gaming Verifiers\" authors full list"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:48:13.908941+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "gaming-verifiers|countdown-code|2604\\.15149|2603\\.07084",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "Grep",
  "tool_args": {
    "pattern": "gaming-verifiers|countdown-code|2604\\.15149|2603\\.07084",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T04:48:13.909066+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T04:48:13.909211+00:00_

Web search results for query: "arxiv 2110.14168 Cobbe "Heewoo Jun" OR "Heather Jun" authors"

Links: [{"title":"Paper page - Training Verifiers to Solve Math Word Problems","url":"https://huggingface.co/papers/2110.14168"},{"title":"[2110.14168] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168"},{"title":"[2110.14168v2] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168v2"},{"title":"Machine Learning authors/titles Oct 2021 (1300 skipped)","url":"https://arxiv.org/list/cs.LG/2110?skip=1300&show=100"},{"title":"Training Verifiers to Solve Math Word Problems, Karl Cobbe+, arXiv'21 · Issue #1618 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1618"},{"title":"[PDF] Training Verifiers to Solve Math Word Problems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-Verifiers-to-Solve-Math-Word-Problems-Cobbe-Kosaraju/d6045d2ccc9c09ca1671348de86d07da6bc28eea"},{"title":"dblp: Heewoo Jun","url":"https://dblp.org/pid/200/8045.html"},{"title":"CoBeL-RL: A neuroscience-oriented simulation framework for complex behavior and learning","url":"https://www.biorxiv.org/content/10.1101/2022.12.27.521997.full.pdf"}]

Based on the search results, arxiv paper 2110.14168 titled "Training Verifiers to Solve Math Word Problems" has the following authors: Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman.

The paper includes "Heewoo Jun" as one of the authors. There is no author named "Heather Jun" on this paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T04:48:13.909428+00:00_

Web search results for query: "arxiv 2604.15149 "LLMs Gaming Verifiers" authors full list"

Links: [{"title":"[2604.15149] LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://arxiv.org/abs/2604.15149"},{"title":"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://arxiv.org/html/2604.15149"},{"title":"Prover-Verifier Games improve legibility of LLM outputs","url":"https://arxiv.org/pdf/2407.13692"},{"title":"GAMEBoT: Transparent Assessment of LLM Reasoning in Games","url":"https://arxiv.org/pdf/2412.13602"},{"title":"Evaluating Large Language Models with Grid-Based Game Competitions: An   Extensible LLM Benchmark and Leaderboard","url":"https://arxiv.org/pdf/2407.07796"},{"title":"Truth or Deceit? A Bayesian Decoding Game Enhances Consistency and   Reliability","url":"https://arxiv.org/pdf/2410.01064"}]

Based on the search results, the full list of authors for the paper "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking" (arxiv 2604.15149) is: Lukas Helff, Quentin Delfosse, David Steinmann, Ruben Härle, Hikaru Shindo, Patrick Schramowski, Wolfgang Stammer, Kristian Kersting, and Felix Friedrich.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T04:48:13.909682+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Gaming Verifiers|Countdown.Code|gaming|countdown",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Gaming Verifiers|Countdown.Code|gaming|countdown",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T04:48:13.909978+00:00_

paper/related_work.tex:9:\citet{kim-game-formalization} study whether GPT-5 and DeepSeek-R1 game Lean~4 formalization at \emph{inference} time. Using axiom diffing and LLM-judge classification on 303 FOL problems, they find no systematic gaming in unified generation but identify two unfaithfulness modes: axiom fabrication during proof (56\% are conclusion-as-axiom) and premise mistranslation during formalization.
paper/related_work.tex:11:First, we study \emph{training-time} gaming under GRPO, where the optimizer actively reshapes the output distribution, producing qualitatively different failures from one-shot inference.
paper/related_work.tex:13:Third, we observe universal gaming under RL (all GRPO conditions show ${\geq}80\%$ hacking), whereas Kim et al.\ report that models prefer failure over forcing proofs at inference time.
paper/related_work.tex:23:Goodhart's Law~\citep{goodhart-1975} is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward} and empirically in RLHF~\citep{amodei2016concrete, gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization, metr-reward-hacking, spurious-rewards}, text generation~\citep{paulus2018deep}, and deep RL~\citep{langosco2022goal, krakovna2020specification}.
paper/related_work.tex:26:Our setting differs from prior work in that ISR is deterministic and solver-derived, gaming emerges during training rather than at inference~\citep{geirhos2020shortcut, kim-game-formalization}, and the diagnostic itself becomes the optimization target.
paper/experiments.tex:126:Under ISR reward, 3/3 seeds reach $0\%$ non-hacking through three distinct mechanisms (TS tautology, classifier-evading pseudo-Prolog, query-as-fact gaming), with one seed evading the strict classifier entirely (Appendix Table~\ref{tab:prolog-detailed}).
paper/experiments.tex:127:Complete collapse across all seeds suggests Prolog's simpler operational semantics provides a broader gaming
…[truncated 6711 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T04:48:13.910160+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "helff|khalifa2026|countdown",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "Grep",
  "tool_args": {
    "pattern": "helff|khalifa2026|countdown",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T04:48:13.910298+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r15-reference-verification_20260520T044621",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T04:48:13.910531+00:00_

验证完成。以下是结果：

---

## [1] LLMs Gaming Verifiers — arXiv:2604.15149

- **完整标题**: LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking
- **作者**: Lukas Helff, Quentin Delfosse, David Steinmann, Ruben Härle, Hikaru Shindo, Patrick Schramowski, Wolfgang Stammer, Kristian Kersting, Felix Friedrich
- **年份**: 2026
- **Venue**: arXiv preprint / LLM Reasoning Workshop @ ICLR 2026
- **验证状态**: ✅ 论文存在，信息正确
- **Bib 状态**: ❌ 不在 references.bib 中，也未在任何 .tex 文件中引用
- **BibTeX entry**:
```bibtex
@article{helff2026gaming,
  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},
  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},
  journal      = {arXiv preprint arXiv:2604.15149},
  year         = {2026},
  eprint       = {2604.15149},
  archivePrefix = {arXiv},
}
```

---

## [2] Countdown-Code — arXiv:2603.07084

- **完整标题**: Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR
- **作者**: Muhammad Khalifa, Zohaib Khan, Omer Tafveez, Hao Peng, Lu Wang
- **年份**: 2026
- **Venue**: arXiv preprint
- **验证状态**: ✅ 论文存在，信息正确
- **Bib 状态**: ❌ 不在 references.bib 中，也未在任何 .tex 文件中引用
- **BibTeX entry**:
```bibtex
@article{khalifa2026countdown,
  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},
  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},
  journal      = {arXiv preprint arXiv:2603.07084},
  year         = {2026},
  eprint       = {2603.07084},
  archivePrefix = {arXiv},
}
```

---

## [3] Uesato et al. (2022) — arXiv:2211.14275

- **完整标题**: Solving math word problems with process- and outcome-based feedback
- **作者**: Jonathan Uesato, Nate Kushman, **Ramana** Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, Irina Higgins
- **年份**: 2022
- **Venue**: NeurIPS 2022 Workshop on MATH-AI
- **验证状态**: ⚠️ 需修正 — bib 中作者写成 **"Ramesh"** Kumar，应为 **"Ramana"** Kumar
- **Bib 状态**: 已有 (`uesato2022solving`, L396-401)，需修正作者名
- **修正**:
```diff
- author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramesh and ...}
+ author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and ...}
```

---

## [4] Cobbe et al. (2021) — arXiv:2110.14168

- **完整标题**: Training Verifiers to Solve Math Word Problems
- **作者**: Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, **Heewoo** Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, John Schulman
- **年份**: 2021
- **Venue**: arXiv preprint (未正式发表于会议)
- **验证状态**: ⚠️ 需修正 — bib 中作者写成 **"Heather Jun"**，应为 **"Heewoo Jun"**
- **Bib 状态**: 已有 (`cobbe2021training`, L509-514)，需修正作者名
- **修正**:
```diff
- author={... and Heather Jun and ...}
+ author={... and Heewoo Jun and ...}
```

---

## 汇总

| # | 论文 | 存在性 | Bib 状态 | 需修正 |
|---|------|--------|----------|--------|
| 1 | LLMs Gaming Verifiers | ✅ | ❌ 缺失 | 需添加 entry |
| 2 | Countdown-Code | ✅ | ❌ 缺失 | 需添加 entry |
| 3 | Uesato 2022 | ✅ | ⚠️ 有 | Kumar, Ramesh → Ramana |
| 4 | Cobbe 2021 | ✅ | ⚠️ 有 | Heather Jun → Heewoo Jun |

Sources:
- [arXiv:2604.15149](https://arxiv.org/abs/2604.15149)
- [arXiv:2603.07084](https://arxiv.org/abs/2603.07084)
- [arXiv:2211.14275](https://arxiv.org/abs/2211.14275)
- [arXiv:2110.14168](https://arxiv.org/abs/2110.14168)
- [DBLP: Heewoo Jun](https://dblp.org/pid/200/8045.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_r15-reference-verification_20260520T044621"
}
```

</details>

---
