# research literature vota

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_research_literature-vota_20260514T215130.jsonl`
- **Structured JSON:** [`8d09ff34044b3887c541.json`](../../sessions/8d/8d09ff34044b3887c541.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-14T21:57:16.493316+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T21:57:16.493786+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T21:57:16.493995+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "execution trace LLM code debugging understanding 2024 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "execution trace LLM code debugging understanding 2024 2025 paper"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T21:57:16.494137+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM code verdict pass fail classification mutation testing 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM code verdict pass fail classification mutation testing 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T21:57:16.494291+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "execution trace compression abstraction summarization program 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "execution trace compression abstraction summarization program 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T21:57:16.494410+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SFT fine-tuning LLM classification task 2024 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SFT fine-tuning LLM classification task 2024 2025 paper"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T21:57:16.494566+00:00_

Web search results for query: "execution trace compression abstraction summarization program 2024 2025"

Links: [{"title":"Interactive Performance Visualization and Analysis of Execution Traces for Pattern-Based Parallel Programming | International Journal of Parallel Programming | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10766-025-00805-3"},{"title":"Do Code Semantics Help? A Comprehensive Study on ...","url":"https://aclanthology.org/2025.findings-emnlp.548.pdf"},{"title":"Tracezip: Efficient Distributed Tracing via Trace Compression","url":"https://arxiv.org/html/2502.06318v1"},{"title":"Compressing Microcontroller Execution Traces to Assist System Analysis | Springer Nature Link (formerly SpringerLink)","url":"https://link.springer.com/chapter/10.1007/978-3-642-38853-8_13"},{"title":"Unified extractive-abstractive summarization: a hybrid approach utilizing BERT and transformer models for enhanced document summarization [PeerJ]","url":"https://peerj.com/articles/cs-2424/"},{"title":"A Novel Framework for Evaluating Application Performance in Distributed Systems","url":"https://www.mdpi.com/2076-3417/15/23/12837"},{"title":"Tracezip: Efficient Distributed Tracing via Trace Compression | Request PDF","url":"https://www.researchgate.net/publication/392914397_Tracezip_Efficient_Distributed_Tracing_via_Trace_Compression"},{"title":"Energy Considerations of Large Language Model ...","url":"https://aclanthology.org/2025.acl-long.1563.pdf"},{"title":"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/html/2505.04441v1"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"}]

Based on the search results, here are some recent findings on execution trace compression, abstraction, and summarization in programs (2024-2025):

## Key Research Areas

**Performance Visualization and E
…[truncated 1505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T21:57:16.494755+00:00_

Web search results for query: "execution trace LLM code debugging understanding 2024 2025 paper"

Links: [{"title":"LADYBUG: an LLM Agent DeBUGger for data-driven applications Joel Rorseth","url":"https://openproceedings.org/2025/conf/edbt/paper-313.pdf"},{"title":"Towards Effectively Leveraging Execution Traces for ...","url":"https://aclanthology.org/2025.knowledgenlp-1.17.pdf"},{"title":"Do Code Semantics Help? A Comprehensive Study on ...","url":"https://aclanthology.org/2025.findings-emnlp.548.pdf"},{"title":"Published as a conference paper at ICLR 2024 TEACHING LARGE LANGUAGE MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf"},{"title":"Paper Review — Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step (ACL 2024) | by Riley Learning | Medium","url":"https://rileylearning.medium.com/paper-review-debug-like-a-human-a-large-language-model-debugger-via-verifying-runtime-execution-3872e931cf40"},{"title":"Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation","url":"https://arxiv.org/html/2512.00215v1"},{"title":"DebugBench: Evaluating Debugging Capability of Large ...","url":"https://aclanthology.org/2024.findings-acl.247.pdf"},{"title":"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/html/2505.04441v1"},{"title":"Making LLMs Program Interpreters via Execution Trace Chain of Thought","url":"https://openreview.net/pdf?id=pFyBdPyOCQ"},{"title":"trace: Evaluating Execution Efficiency of LLM-Based Code Translation","url":"https://arxiv.org/html/2603.16479"}]

I found several relevant papers on execution traces for LLM code debugging and understanding from 2024-2025. Here's a summary of the key papers:

## Recent Papers on Execution Traces and LLM Debugging

**1. Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs (2025)**
T
…[truncated 2086 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T21:57:16.494945+00:00_

Web search results for query: "LLM code verdict pass fail classification mutation testing 2024 2025"

Links: [{"title":"LLMs Are the Key to Mutation Testing and Better Compliance - Engineering at Meta","url":"https://engineering.fb.com/2025/09/30/security/llms-are-the-key-to-mutation-testing-and-better-compliance/"},{"title":"Mutation-Guided LLM-based Test Generation at Meta","url":"https://arxiv.org/html/2501.12862v1"},{"title":"Mutation-Guided LLM-based Test Generation at Meta Christopher Foster","url":"https://arxiv.org/pdf/2501.12862"},{"title":"Mutation-Guided LLM-based Test Generation at Meta (FSE 2025 - Industry Papers) - FSE 2025","url":"https://conf.researchr.org/details/fse-2025/fse-2025-industry-papers/16/Mutation-Guided-LLM-based-Test-Generation-at-Meta"},{"title":"Meta Applies Mutation Testing with LLM to Improve Compliance Coverage - InfoQ","url":"https://www.infoq.com/news/2026/01/meta-llm-mutation-testing/"},{"title":"Evaluating LLM Generated Detection Rules in Cybersecurity","url":"https://arxiv.org/html/2509.16749v1"},{"title":"LLM Testing Tools and Frameworks in 2026: The Engineering Guide","url":"https://contextqa.com/blog/llm-testing-tools-frameworks-2026/"},{"title":"[2501.12862] Mutation-Guided LLM-based Test Generation at Meta","url":"https://arxiv.org/abs/2501.12862"},{"title":"LLM-Powered Test Case Generation for Detecting Bugs in ...","url":"https://aclanthology.org/2025.acl-long.20.pdf"},{"title":"Utilising LLM-as-a-Judge to Evaluate LLM-Generated Code by cbarkinozer | Softtech","url":"https://medium.com/softtechas/utilising-llm-as-a-judge-to-evaluate-llm-generated-code-451e9631c713"}]

Based on the search results, here's what I found related to LLM code verdict pass/fail classification and mutation testing in 2024-2025:

## Key Research and Developments

**Meta's ACH System (Automated Compliance Hardening):**

Meta developed an LLM-based Equivalence Detector agent that is capable of judging whether a mutant is equivalent to the original 
…[truncated 1377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T21:57:16.495128+00:00_

Web search results for query: "SFT fine-tuning LLM classification task 2024 2025 paper"

Links: [{"title":"The Best Instruction-Tuning Data are Those That Fit | OpenReview","url":"https://openreview.net/forum?id=4jFSekBaDT"},{"title":"ICML Poster FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain","url":"https://icml.cc/virtual/2025/poster/44605"},{"title":"Massive Supervised Fine-tuning Experiments Reveal How Data, Layer, and Training Factors Shape LLM Alignment Quality","url":"https://arxiv.org/html/2506.14681v2"},{"title":"Original Paper Fine-Tuning Methods for Large Language Models in Clinical","url":"https://www.jmir.org/2025/1/e76048/PDF"},{"title":"Journal of Medical Internet Research - Fine-Tuning Methods for Large Language Models in Clinical Medicine by Supervised Fine-Tuning and Direct Preference Optimization: Comparative Evaluation","url":"https://www.jmir.org/2025/1/e76048"},{"title":"preserving diversity in supervised fine-tuning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf"},{"title":"Fine-tuning large language models for domain adaptation: exploration of training strategies, scaling, model merging and synergistic capabilities | npj Computational Materials","url":"https://www.nature.com/articles/s41524-025-01564-y"},{"title":"Hands on with SFT - AI Engineering Academy","url":"https://aiengineering.academy/LLM/HandsOnWithFinetuning/SFT/SFT/"},{"title":"[2506.14681] Massive Supervised Fine-tuning Experiments Reveal How Data, Layer, and Training Factors Shape LLM Alignment Quality","url":"https://arxiv.org/abs/2506.14681"},{"title":"Fine-tuning large language models (LLMs) in 2026 | SuperAnnotate","url":"https://www.superannotate.com/blog/llm-fine-tuning"}]

I found several recent papers and resources related to SFT (Supervised Fine-Tuning) for LLMs with classification tasks from 2024-2025. Here are the key findings:

## Recent Papers on SFT Fi
…[truncated 2123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T21:57:16.495325+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Teaching Large Language Models to Self-Debug\" ICLR 2024 execution trace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Teaching Large Language Models to Self-Debug\" ICLR 2024 execution trace"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T21:57:16.495453+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Do Code Semantics Help\" execution trace fine-tuning EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Do Code Semantics Help\" execution trace fine-tuning EMNLP 2025"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T21:57:16.495568+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM code correctness prediction test outcome classification 2024 2025 ICSE FSE ASE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM code correctness prediction test outcome classification 2024 2025 ICSE FSE ASE"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T21:57:16.495680+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"execution trace chain of thought\" LLM program interpreter 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"execution trace chain of thought\" LLM program interpreter 2025"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T21:57:16.495825+00:00_

Web search results for query: ""Teaching Large Language Models to Self-Debug" ICLR 2024 execution trace"

Links: [{"title":"TEACHING LARGE LANGUAGE MODELS TO SELF- DEBUG","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf"},{"title":"[2304.05128] Teaching Large Language Models to Self-Debug","url":"https://arxiv.org/abs/2304.05128"},{"title":"Teaching Large Language Models to Self-Debug | OpenReview","url":"https://openreview.net/forum?id=KuPixIqPiq"},{"title":"TEACHING LARGE LANGUAGE MODELS TO SELF- DEBUG","url":"https://openreview.net/attachment?id=KuPixIqPiq&name=supplementary_material"},{"title":"[PDF] Teaching Large Language Models to Self-Debug | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Teaching-Large-Language-Models-to-Self-Debug-Chen-Lin/9e3c493fb09dcd61bb05e8c5659f23327b7b6340"},{"title":"TEACHING LARGE LANGUAGE MODELS TO SELF- DEBUG Xinyun Chen1 Maxwell Lin2","url":"https://arxiv.org/pdf/2304.05128"},{"title":"GitHub - teacherpeterpan/self-correction-llm-papers: This is a collection of research papers for Self-Correcting Large Language Models with Automated Feedback. · GitHub","url":"https://github.com/teacherpeterpan/self-correction-llm-papers"},{"title":"Teaching Large Language Models to Self-Debug | by Stay Hard | Medium","url":"https://medium.com/@instein98/teaching-large-language-models-to-self-debug-1f6bf4b2f994"},{"title":"Revisit Self-Debugging with Self-Generated Tests for Code ...","url":"https://aclanthology.org/2025.acl-long.881.pdf"},{"title":"[2404.14662] NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://arxiv.org/abs/2404.14662"}]

I found comprehensive information about the paper "Teaching Large Language Models to Self-Debug" from ICLR 2024. Here are the key findings:

## Overview

This work proposes Self-Debugging, which teaches a large language model to debug its predicted program via few-shot demonstrations.

## The S
…[truncated 1415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T21:57:16.496003+00:00_

Web search results for query: "LLM code correctness prediction test outcome classification 2024 2025 ICSE FSE ASE"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Calibration and Correctness of Language Models for Code Claudio Spiess∗","url":"https://www.software-lab.org/publications/icse2025_calibration.pdf"},{"title":"CORE: Benchmarking LLMs' Code Reasoning Capabilities ...","url":"https://openreview.net/pdf?id=WJIDorHiuZ"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"Do LLMs Generate Useful Test Oracles? An Empirical ...","url":"https://www.lucadigrazia.com/papers/ase2025.pdf"},{"title":"A Systematic Literature Review on Large Language Models","url":"https://arxiv.org/pdf/2405.01466"},{"title":"GitHub - xinyi-hou/LLM4SE_SLR: Large Language Models for Software Engineering: A Systematic Literature Review · GitHub","url":"https://github.com/xinyi-hou/LLM4SE_SLR"},{"title":"How well LLM-based test generation techniques perform with newer LLM versions?","url":"https://arxiv.org/pdf/2601.09695"},{"title":"Blended Analysis for Predictive Execution","url":"https://aashishyadavally.github.io/assets/pdf/pub-fse2025-(2).pdf"},{"title":"Unprecedented Code Change Automation: The Fusion of","url":"https://danny.cs.colorado.edu/papers/PyCraft_FSE2024.pdf"}]

Based on the web search results, here's what I found regarding LLM code correctness prediction and test outcome classification in recent conferences (2024-2025):

## Key Research Areas

Recent work on LLMs for software engineering includes studies on fine-tuning large language models of code for automated program repair, code security vulnerability repair, and program repair using reinforcement learni
…[truncated 1209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T21:57:16.496166+00:00_

Web search results for query: ""Do Code Semantics Help" execution trace fine-tuning EMNLP 2025"

Links: [{"title":"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.548/"},{"title":"Do Code Semantics Help? A Comprehensive Study on ...","url":"https://aclanthology.org/2025.findings-emnlp.548.pdf"},{"title":"[2509.11686] Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/abs/2509.11686"},{"title":"Do Code Semantics Help? A Comprehensive Study on Execution","url":"https://arxiv.org/pdf/2509.11686"},{"title":"[2509.11686v3] Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/abs/2509.11686v3"},{"title":"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models","url":"https://arxiv.org/html/2509.11686v3"},{"title":"Code Execution as Grounded Supervision for LLM ...","url":"https://aclanthology.org/2025.emnlp-main.1260.pdf"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"Systematically and Automatically Testing Instruction-Tuned ...","url":"https://www.doc.ic.ac.uk/~afd/papers/2025/ICST-Turbulence.pdf"},{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/html/2510.18471"}]

Based on the search results, I found the paper you're looking for:

"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models" was published in the Findings of the Association for Computational Linguistics: EMNLP 2025.

The paper was authored by Jian Jornbowrl Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, and Yi Li.

**Key findings:**

The researchers in
…[truncated 812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T21:57:16.496355+00:00_

Web search results for query: ""execution trace chain of thought" LLM program interpreter 2025"

Links: [{"title":"Making LLMs Program Interpreters via Execution Trace Chain of Thought | OpenReview","url":"https://openreview.net/forum?id=pFyBdPyOCQ"},{"title":"Making LLMs Program Interpreters via Execution Trace Chain of Thought","url":"https://openreview.net/pdf?id=pFyBdPyOCQ"},{"title":"Code Execution as Grounded Supervision for LLM ...","url":"https://aclanthology.org/2025.emnlp-main.1260.pdf"},{"title":"Generating Verifiable Chain of Thoughts from Exection-Traces","url":"https://arxiv.org/pdf/2512.00127"},{"title":"Towards Effectively Leveraging Execution Traces for ...","url":"https://aclanthology.org/2025.knowledgenlp-1.17.pdf"},{"title":"COTTONTAIL: Large Language Model-Driven Concolic Execution for","url":"https://mboehme.github.io/paper/SP26-cottontail.pdf"},{"title":"trace: Evaluating Execution Efficiency of LLM-Based Code Translation","url":"https://arxiv.org/html/2603.16479"},{"title":"Chain-of-Thought Component in LLMs","url":"https://www.emergentmind.com/topics/chain-of-thought-cot-component"},{"title":"Do Code Semantics Help? A Comprehensive Study on ...","url":"https://aclanthology.org/2025.findings-emnlp.548.pdf"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"}]

Based on the web search results, here are the key findings about execution trace chain of thought for LLM program interpreters in 2025:

## ET-CoT: Making LLMs Program Interpreters

ET-CoT (Execution Trace Chain of Thought) is an approach where LLMs learn to generate a detailed and systematic program execution trace as a chain of thought to predict program outcomes.

### Key Approach

The approach has LLMs generate detailed and systematic program execution traces as a chain of thought to predict program outcomes, with a program-execution trace format inspired by 
…[truncated 1058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T21:57:16.496522+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NExT \"Teaching Large Language Models to Reason about Code Execution\" 2024 trace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NExT \"Teaching Large Language Models to Reason about Code Execution\" 2024 trace"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T21:57:16.496648+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "APPT patch correctness prediction fine-tuning pre-trained models TSE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "APPT patch correctness prediction fine-tuning pre-trained models TSE 2024"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T21:57:16.496762+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Calibration and Correctness of Language Models for Code\" ICSE 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Calibration and Correctness of Language Models for Code\" ICSE 2025"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T21:57:16.496874+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "supervised fine-tuning LLM binary classification sequence classification 2024 2025 NeurIPS ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "supervised fine-tuning LLM binary classification sequence classification 2024 2025 NeurIPS ICML"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T21:57:16.497016+00:00_

Web search results for query: "NExT "Teaching Large Language Models to Reason about Code Execution" 2024 trace"

Links: [{"title":"[2404.14662] NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://arxiv.org/abs/2404.14662"},{"title":"[PDF] NExT: Teaching Large Language Models to Reason about Code Execution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NExT:-Teaching-Large-Language-Models-to-Reason-Code-Ni-Allamanis/49306aa1fde2a21fadc77dbc8ec7e487fac72c5b"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://proceedings.mlr.press/v235/ni24a.html"},{"title":"[2404.14662v1] NExT: Teaching Large Language Models to Reason about Code Execution","url":"https://arxiv.org/abs/2404.14662v1"},{"title":"Decoding Code Execution: How DeepMind’s NExT Empowers AI Reasoning | Synced","url":"https://syncedreview.com/2024/04/24/decoding-code-execution-how-deepminds-next-empowers-ai-reasoning/"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/next-teaching-large-language-models-to-reason"},{"title":"NExT: Teaching Large Language Models to Reason about ...","url":"https://www.emergentmind.com/papers/2404.14662"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution · Miltos Allamanis","url":"https://miltos.allamanis.com/publications/2024next/"},{"title":"NExT: Teaching Large Language Models to Reason about Code Execution | OpenReview","url":"https://openreview.net/forum?id=B1W712hMBi"},{"title":"NExT: Teaching Large Language Models to Reason about ...","url":"https://arxiv.org/pdf/2404.14662"}]

Based on the web search results, I found comprehensive information about the NExT paper:

## NExT: Teaching Large Language Models to Reason about Code Execution

NExT is a method to teach LLMs to inspect the execution traces of programs (variable states of executed lines) and re
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T21:57:16.497181+00:00_

Web search results for query: "APPT patch correctness prediction fine-tuning pre-trained models TSE 2024"

Links: [{"title":"GitHub - iSEngLab/APPT: [TSE 2024] APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models · GitHub","url":"https://github.com/iSEngLab/APPT"},{"title":"[2301.12453] APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models","url":"https://arxiv.org/abs/2301.12453"},{"title":"Actions · iSEngLab/APPT","url":"https://github.com/iSEngLab/APPT/actions"},{"title":"APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10402095/;jsessionid=5922708BFC9F37FBEE6DF1C5986009E3"},{"title":"GitHub - xinyi-hou/LLM4SE_SLR: Large Language Models for Software Engineering: A Systematic Literature Review · GitHub","url":"https://github.com/xinyi-hou/LLM4SE_SLR"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Contrastive Learning for Automated Patch Correctness ...","url":"https://arxiv.org/pdf/2602.07561"},{"title":"APPT Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models","url":"https://www.scribd.com/document/874799956/APPT-Boosting-Automated-Patch-Correctness-Prediction-via-Fine-tuning-Pre-trained-Models"},{"title":"APPT: Boosting Automated Patch Correctness Prediction ...","url":"https://arxiv.org/pdf/2301.12453"},{"title":"(PDF) Boosting Automated Patch Correctness Prediction via Pre-trained Language Model","url":"https://www.researchgate.net/publication/367558621_Boosting_Automated_Patch_Correctness_Prediction_via_Pre-trained_Language_Model"}]

Based on the search results, here's what I found about APPT:

## APPT: Automated Patch Correctness Prediction

APPT is a TSE 2024 paper titled "Boosting Automated Patch
…[truncated 1090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T21:57:16.497377+00:00_

Web search results for query: "supervised fine-tuning LLM binary classification sequence classification 2024 2025 NeurIPS ICML"

Links: [{"title":"NeurIPS Entropic Distribution Matching for Supervised Fine-tuning of LLMs: Less Overfitting and Better Diversity","url":"https://neurips.cc/virtual/2024/101683"},{"title":"preserving diversity in supervised fine-tuning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf"},{"title":"ICML Poster FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain","url":"https://icml.cc/virtual/2025/poster/44605"},{"title":"NeurIPS Poster Coevolving with the Other You: Fine-Tuning LLM with Sequential Cooperative Multi-Agent Reinforcement Learning","url":"https://neurips.cc/virtual/2024/poster/95347"},{"title":"Fine-Tuning in Modern Machine Learning: Principles and Scalability","url":"https://neurips.cc/virtual/2024/workshop/84742"},{"title":"ICML Poster RoSTE: An Efficient Quantization-Aware Supervised Fine-Tuning Approach for Large Language Models","url":"https://icml.cc/virtual/2025/poster/44438"},{"title":"Massive Supervised Fine-tuning Experiments Reveal How Data, Layer, and Training Factors Shape LLM Alignment Quality","url":"https://arxiv.org/html/2506.14681v2"},{"title":"Preserving Diversity in Supervised Fine-Tuning of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=NQEe7B7bSw"},{"title":"LoFiT: Localized Fine-tuning on LLM Representations","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/122ea6470232ee5e79a2649243348005-Abstract-Conference.html"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"}]

Based on the search results, I found several recent papers on supervised fine-tuning of LLMs presented at NeurIPS 2024 and ICML 2025:

## NeurIPS 2024 Papers

Large language models rely on Supervised Fine-Tuning (SFT) to specialize in downstream tasks, with Cross E
…[truncated 1257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T21:57:16.497555+00:00_

Web search results for query: ""Calibration and Correctness of Language Models for Code" ICSE 2025"

Links: [{"title":"Calibration and Correctness of Language Models for Code (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/8/Calibration-and-Correctness-of-Language-Models-for-Code"},{"title":"Calibration and Correctness of Language Models for Code | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00040"},{"title":"Calibration and Correctness of Language Models for Code Claudio Spiess∗","url":"https://www.software-lab.org/publications/icse2025_calibration.pdf"},{"title":"Calibration and Correctness of Language Models for Code","url":"https://www.computer.org/csdl/proceedings-article/icse/2025/056900a495/215aWTgzWr6"},{"title":"[PDF] Calibration and Correctness of Language Models for Code | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Calibration-and-Correctness-of-Language-Models-for-Spiess-Gros/65b59f4ffae4f5b9e5d63fc1d11bf9ca7f7df34d"},{"title":"[2402.02047] Calibration and Correctness of Language Models for Code","url":"https://arxiv.org/abs/2402.02047"},{"title":"dblp: ICSE 2025","url":"https://dblp.org/db/conf/icse/icse2025.html"},{"title":"Calibration and Correctness of Language Models for Code ICSE Artifact","url":"https://explore.openaire.eu/search/result?pid=10.5281/zenodo.14744842"},{"title":"Calibration of Large Language Models on Code Summarization | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3729400"},{"title":"Calibration and Correctness of Language Models for Code ICSE Artifact","url":"https://zenodo.org/records/14744842"}]

Based on the search results, here's information about the paper "Calibration and Correctness of Language Models for Code" accepted at ICSE 2025:

## Paper Overview

The paper is authored by Claudio Spiess, David Gros
…[truncated 1196 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T21:57:16.497714+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Code Execution as Grounded Supervision\" EMNLP 2025 LLM reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Code Execution as Grounded Supervision\" EMNLP 2025 LLM reasoning"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T21:57:16.497833+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM fine-tuning text classification vs generation format 2024 2025 paper comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM fine-tuning text classification vs generation format 2024 2025 paper comparison"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T21:57:16.497947+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CRUXEval code execution prediction LLM benchmark 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CRUXEval code execution prediction LLM benchmark 2024"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T21:57:16.498086+00:00_

Web search results for query: "CRUXEval code execution prediction LLM benchmark 2024"

Links: [{"title":"CRUXEval: Code Reasoning, Understanding, and Execution Evaluation","url":"https://crux-eval.github.io/"},{"title":"CruxEval-O Leaderboard","url":"https://llm-stats.com/benchmarks/cruxeval-o"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf/e4619cf824fc3a958f2d274337715f6c670e7240.pdf"},{"title":"GitHub - facebookresearch/cruxeval: CRUXEval: Code Reasoning, Understanding, and Execution Evaluation · GitHub","url":"https://github.com/facebookresearch/cruxeval"},{"title":"Evaluating Code Reasoning Abilities of Large Language Models Under Real-World Settings","url":"https://arxiv.org/html/2512.14917v1"},{"title":"LiveCodeBench: Holistic and Contamination Free Evaluation of","url":"https://arxiv.org/pdf/2403.07974"},{"title":"A Benchmark for Code Reasoning, Understanding and ...","url":"https://crux-eval.github.io/paper/cruxeval.pdf"},{"title":"[2401.03065] CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution","url":"https://arxiv.org/abs/2401.03065"},{"title":"CRUXEval: a benchmark for code reasoning ...","url":"https://dl.acm.org/doi/10.5555/3692070.3692729"},{"title":"Do Code Semantics Help? A Comprehensive Study on ...","url":"https://aclanthology.org/2025.findings-emnlp.548.pdf"}]

Based on the web search results, here's what I found about CRUXEval:

## Overview

CRUXEval (Code Reasoning, Understanding, and eXecution Evaluation) is a benchmark of 800 Python functions and input-output pairs consisting of two tasks: CRUXEval-I (input prediction) and CRUXEval-O (output prediction).

## Benchmark Details

The benchmark consists of 800 Python functions (3-13 lines), with each function coming with an input-output pair, leading to two natural tasks: input prediction and output prediction.

The benchmark tests fundamental code execution reasoning abilities and goes beyond simple code generation to assess deeper un
…[truncated 641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T21:57:16.498307+00:00_

Web search results for query: ""Code Execution as Grounded Supervision" EMNLP 2025 LLM reasoning"

Links: [{"title":"GitHub - luka-group/Execution-Grounded-Reasoning: [EMNLP 2025] Code Execution as Grounded Supervision for LLM Reasoning","url":"https://github.com/luka-group/Execution-Grounded-Reasoning"},{"title":"Code Execution as Grounded Supervision for LLM Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1260/"},{"title":"[2506.10343] Code Execution as Grounded Supervision for LLM Reasoning","url":"https://arxiv.org/abs/2506.10343"},{"title":"Code Execution as Grounded Supervision for LLM ...","url":"https://aclanthology.org/2025.emnlp-main.1260.pdf"},{"title":"Code Execution as Grounded Supervision for LLM Reasoning","url":"https://arxiv.org/html/2506.10343"},{"title":"[Literature Review] Code Execution as Grounded Supervision for LLM Reasoning","url":"https://www.themoonlight.io/en/review/code-execution-as-grounded-supervision-for-llm-reasoning"},{"title":"A Multi-Agent LLM Framework for Transforming Ambiguous ...","url":"https://aclanthology.org/2025.emnlp-industry.163.pdf"},{"title":"A Survey on Code-Enhanced Reasoning and ...","url":"https://aclanthology.org/2025.emnlp-main.130.pdf"},{"title":"Do Code Semantics Help? A Comprehensive Study on ...","url":"https://aclanthology.org/2025.findings-emnlp.548.pdf"},{"title":"RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=PzSG5nKe1q"}]

I found comprehensive information about "Code Execution as Grounded Supervision for LLM Reasoning" from EMNLP 2025. Here are the key findings:

## Overview

This is an EMNLP 2025 paper that proposes a scalable method for generating verifiable CoT data to supervise the reasoning process of LLM by leveraging the determinism of program execution.

## Problem and Solution

Unlike existing reasoning dataset generation methods that rely on costly human annotations or error-prone LLM-
…[truncated 1234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T21:57:16.498528+00:00_

Web search results for query: "LLM fine-tuning text classification vs generation format 2024 2025 paper comparison"

Links: [{"title":"Open-source LLMs for text annotation: a practical guide for model setting and fine-tuning | Journal of Computational Social Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s42001-024-00345-9"},{"title":"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches","url":"https://arxiv.org/html/2512.12677v1"},{"title":"Large Language Models for Text Classification: From Zero-Shot Learning to Instruction-Tuning - Youngjin Chae, Thomas Davidson, 2026","url":"https://journals.sagepub.com/doi/10.1177/00491241251325243"},{"title":"Advancing Single and Multi-task Text Classification through Large Language Model Fine-tuning","url":"https://arxiv.org/html/2412.08587v2"},{"title":"Pushing The Limit of LLM Capacity for Text Classification | Companion Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3701716.3715528"},{"title":"A Comparative Analysis of Instruction Fine-Tuning Large Language Models for Financial Text Classification | ACM Transactions on Management Information Systems","url":"https://dl.acm.org/doi/10.1145/3706119"},{"title":"Fine-Tuned ‘Small’ LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification","url":"https://arxiv.org/html/2406.08660v1"},{"title":"A Study on Text Classification in the Age of Large Language Models","url":"https://www.mdpi.com/2504-4990/6/4/129"},{"title":"Text Classification in the LLM Era - Where do we stand?","url":"https://arxiv.org/html/2502.11830v1"},{"title":"Parameter-efficient fine-tuning of large language models using semantic knowledge tuning | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-75599-4"}]

I found several relevant recent papers (2024-2025) comparing LLM fine-tuning approaches for text classification and generation tasks. He
…[truncated 1741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T21:57:16.498733+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "program execution trace reduction slicing abstraction debugging 2024 2025 ICSE ASE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "program execution trace reduction slicing abstraction debugging 2024 2025 ICSE ASE"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T21:57:16.498861+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Towards Effectively Leveraging Execution Traces for Program Repair\" 2025 authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Towards Effectively Leveraging Execution Traces for Program Repair\" 2025 authors venue"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T21:57:16.498995+00:00_

Web search results for query: ""Towards Effectively Leveraging Execution Traces for Program Repair" 2025 authors venue"

Links: [{"title":"[2505.04441] Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/abs/2505.04441"},{"title":"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/html/2505.04441v1"},{"title":"Debugging Code World Models","url":"https://arxiv.org/html/2602.07672v2"},{"title":"Towards Effectively Leveraging Execution Traces for ...","url":"https://aclanthology.org/2025.knowledgenlp-1.17.pdf"},{"title":"Towards Effectively Leveraging Execution Traces","url":"https://arxiv.org/pdf/2505.04441"},{"title":"Bug Fixing with Broader Context: Enhancing LLM-Based Program Repair via Layered Knowledge Injection","url":"https://arxiv.org/html/2506.24015v1"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Petr Babkin's research works | Palo Alto Research Center and other places","url":"https://www.researchgate.net/scientific-contributions/Petr-Babkin-2224003926"},{"title":"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate","url":"https://arxiv.org/html/2604.02647"}]

Based on the search results, here is the information about the paper "Towards Effectively Leveraging Execution Traces for Program Repair":

**Authors:** Mirazul Haque, Petr Babkin, Farima Farmahinifarahani, and Manuela Veloso from J. P. Morgan AI Research

**Venue:** The 4th International Workshop on Knowledge-Augmented Methods for Natural Language Processing (in Albuquerque, New Mexico, USA, published by Association for Computational Linguistics, May 2025)

**Year:** 2025

The paper explores strategies for in
…[truncated 221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T21:57:16.499164+00:00_

Web search results for query: "program execution trace reduction slicing abstraction debugging 2024 2025 ICSE ASE"

Links: [{"title":"International Automated Program Repair Workshop 2025 ...","url":"https://program-repair.org/workshop-2025/"},{"title":"2025 IEEE/ACM 47th International Conference on Software ...","url":"https://www.computer.org/csdl/proceedings/icse/2025/215aVCUIQmY"},{"title":"Software Engineering Aug 2024","url":"https://arxiv.org/list/cs.SE/2024-08?show=2000&skip=175"},{"title":"dblp: ICSE 2024","url":"https://dblp.org/db/conf/icse/icse2024.html"},{"title":"Program - ICSE 2024","url":"https://conf.researchr.org/program/icse-2024/program-icse-2024/"},{"title":"On the Effects of Program Slicing for Vulnerability Detection during Code Inspection: Extended Abstract (ICSE 2024 - Posters) - ICSE 2024","url":"https://conf.researchr.org/details/icse-2024/icse-2024-posters/52/On-the-Effects-of-Program-Slicing-for-Vulnerability-Detection-during-Code-Inspection-"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"On the effects of program slicing for vulnerability detection during code inspection - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11972194/"},{"title":"2024 IEEE/ACM 46th International Conference on Software ...","url":"https://www.computer.org/csdl/proceedings/icse/2024/1RLIVDkr2xO"},{"title":"dblp: ICSE 2024","url":"https://dblp.uni-trier.de/db/conf/icse/icse2024.html"}]

Based on the search results, I found relevant information about program slicing, debugging, and related research presented at ICSE and ASE conferences:

## Key Findings:

**Program Slicing Research (2024):**
Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning was published at FSE'24, and A Learning-Based Approach to Static Program Slicing appeared at OOPSLA'24. 
…[truncated 1236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T21:57:16.499364+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Predictive Program Slicing via Execution Knowledge\" FSE 2024 dynamic dependence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Predictive Program Slicing via Execution Knowledge\" FSE 2024 dynamic dependence"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T21:57:16.499489+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "trace abstraction loop summarization program analysis verification 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "trace abstraction loop summarization program analysis verification 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T21:57:16.499602+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Fine-Tuning Causal LLMs for Text Classification Embedding-Based Instruction-Based\" 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Fine-Tuning Causal LLMs for Text Classification Embedding-Based Instruction-Based\" 2025 authors"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T21:57:16.499733+00:00_

Web search results for query: ""Fine-Tuning Causal LLMs for Text Classification Embedding-Based Instruction-Based" 2025 authors"

Links: [{"title":"[2512.12677] Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches","url":"https://arxiv.org/abs/2512.12677"},{"title":"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches","url":"https://arxiv.org/html/2512.12677v1"},{"title":"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches","url":"https://www.emergentmind.com/papers/2512.12677"},{"title":"A Comparative Analysis of Instruction Fine-Tuning Large Language Models for Financial Text Classification | ACM Transactions on Management Information Systems","url":"https://dl.acm.org/doi/10.1145/3706119"},{"title":"A Comparative Analysis of Instruction Fine-Tuning Large Language Models for Financial Text Classification | Request PDF","url":"https://www.researchgate.net/publication/386435246_A_Comparative_Analysis_of_Instruction_Fine-Tuning_Large_Language_Models_for_Financial_Text_Classification"},{"title":"A Comparative Analysis of Instruction Fine-Tuning LLMs for Financial Text","url":"https://arxiv.org/pdf/2411.02476"},{"title":"Large Language Models for Text Classification: From Zero-Shot Learning to Instruction-Tuning - Youngjin Chae, Thomas Davidson, 2026","url":"https://journals.sagepub.com/doi/10.1177/00491241251325243"},{"title":"KaLM-Embedding-V2: Superior Training Techniques and ...","url":"https://arxiv.org/pdf/2506.20923v1"},{"title":"It is all in the [MASK]: Simple instruction-tuning enables BERT-like masked language models as generative classifiers - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2949719125000263"},{"title":"Towards Locally Deployable Fine-Tuned Causal Large Language Models for Mode Choice Behaviour","url":"https://arxiv.org/html/2507.21432v1"}]

Based on the search results, I found the p
…[truncated 721 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T21:57:16.499903+00:00_

Web search results for query: ""Predictive Program Slicing via Execution Knowledge" FSE 2024 dynamic dependence"

Links: [{"title":"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning (FSE 2024 - Posters) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-posters/26/Predictive-Program-Slicing-via-Execution-Knowledge-Guided-Dynamic-Dependence-Learning"},{"title":"Predictive Program Slicing via Execution Knowledge-Guided","url":"https://aashishyadavally.github.io/assets/pdf/pub-fse2024.pdf"},{"title":"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3643739"},{"title":"Awards - FSE 2024","url":"https://2024.esec-fse.org/info/awards"},{"title":"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/yadavally2024predictive/"},{"title":"One paper accepted at FSE 2024. | Aashish Yadavally","url":"https://aashishyadavally.github.io/news/announcement_26/"},{"title":"Aashish Yadavally Assistant Professor Department of Computer Science","url":"https://aashishyadavally.github.io/assets/pdf/cv.pdf"},{"title":"Predictive Program Slicing via Execution Knowledge- ...","url":"https://dl.acm.org/doi/pdf/10.1145/3643739"},{"title":"Blended Analysis for Predictive Execution | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3729402"},{"title":"A Survey of Program Slicing Techniques. | Guide books","url":"https://dl.acm.org/doi/abs/10.5555/869354"}]

Based on the search results, I found comprehensive information about "Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning" from FSE 2024.

## Overview

ND-Slicer is a predictive slicing methodology that caters to specific executions based on a particular input, overcoming the nee
…[truncated 1361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T21:57:16.500069+00:00_

Web search results for query: "trace abstraction loop summarization program analysis verification 2024 2025"

Links: [{"title":"Loop Summarization Using Abstract Transformers | Proceedings of the 6th International Symposium on Automated Technology for Verification and Analysis","url":"https://dl.acm.org/doi/10.1007/978-3-540-88387-6_10"},{"title":"Loop summarization | Formal Verification and Security Lab","url":"https://verify.inf.usi.ch/content/loop-summarization"},{"title":"Trace Abstraction-Based Verification for Uninterpreted Programs","url":"https://dl.acm.org/doi/10.1007/978-3-030-90870-6_29"},{"title":"Structural Abstraction and Refinement for Probabilistic ...","url":"https://dl.acm.org/doi/pdf/10.1145/3763115"},{"title":"Abstract Interpretation Framework","url":"https://www.emergentmind.com/topics/abstract-interpretation"},{"title":"Trace Abstraction-Based Verification for Uninterpreted Programs | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-030-90870-6_29"},{"title":"Noname manuscript No. (will be inserted by the editor) Loop Summarization using","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/main-29.pdf"},{"title":"1 Trace Abstraction Modulo Probability","url":"https://arxiv.org/pdf/1810.12396"},{"title":"Loop Summarization using Abstract Transformers | Formal Verification and Security Lab","url":"https://verify.inf.usi.ch/publications/2008/loop-summarization-using-abstract-transformers"},{"title":"Loop Summarization Using Abstract Transformers | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-540-88387-6_10"}]

Based on the search results, here's what I found regarding trace abstraction, loop summarization, and program analysis/verification in the 2024-2025 timeframe:

## Key Recent Work (2024-2025)

A paper on "Structural Abstraction and Refinement for Probabilistic Programs" was published in October 2025, which advances techniques for program verification. This wor
…[truncated 1258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T21:57:16.500262+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Making LLMs Program Interpreters\" ET-CoT authors PyTracify 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Making LLMs Program Interpreters\" ET-CoT authors PyTracify 2025"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T21:57:16.500391+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FisherSFT data-efficient supervised fine-tuning Fisher information ICML 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FisherSFT data-efficient supervised fine-tuning Fisher information ICML 2025 authors"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T21:57:16.500528+00:00_

Web search results for query: "FisherSFT data-efficient supervised fine-tuning Fisher information ICML 2025 authors"

Links: [{"title":"ICML Poster FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain","url":"https://icml.cc/virtual/2025/poster/44605"},{"title":"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain | OpenReview","url":"https://openreview.net/forum?id=e02oLEbehE&noteId=1WMosCnZ5a"},{"title":"[2505.14826] FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain","url":"https://arxiv.org/abs/2505.14826"},{"title":"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain","url":"https://proceedings.mlr.press/v267/deb25a.html"},{"title":"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain","url":"https://arxiv.org/html/2505.14826v1"},{"title":"FisherSFT: Data-Efficient Supervised Fine-Tuning of ...","url":"https://www.arxiv.org/pdf/2505.14826"},{"title":"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using","url":"https://openreview.net/attachment?id=e02oLEbehE&name=pdf"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=1425&show=250"},{"title":"ICML Poster Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models","url":"https://icml.cc/virtual/2025/poster/46652"},{"title":"GitHub - zituitui/DiffusionFisher: [ICML 2025] Official implementation of \"Efficiently Access Diffusion Fisher: Within the Outer Product Span Space\".","url":"https://github.com/zituitui/DiffusionFisher"}]

Based on the search results, here's the information about the FisherSFT paper at ICML 2025:

## Paper Overview

FisherSFT improves the efficiency of supervised fine-tuning (SFT) by selecting an informative subset of training examples. For a fixed budget of training examples, the method selects those that maximize informat
…[truncated 793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T21:57:16.500692+00:00_

Web search results for query: ""Making LLMs Program Interpreters" ET-CoT authors PyTracify 2025"

Links: [{"title":"Making LLMs Program Interpreters via Execution Trace Chain of Thought","url":"https://openreview.net/pdf?id=pFyBdPyOCQ"},{"title":"Making LLMs Program Interpreters via Execution Trace Chain of Thought | OpenReview","url":"https://openreview.net/forum?id=pFyBdPyOCQ"},{"title":"Transforming Language Models into Program Interpreters ...","url":"https://openreview.net/pdf?id=pOg7iub4Pz"},{"title":"What Are Program-Aided Language Models? | Coursera","url":"https://www.coursera.org/articles/program-aided-language-models"},{"title":"Build Your Own Code Interpreter - Dynamic Tool Generation and Execution With o3-mini","url":"https://cookbook.openai.com/examples/object_oriented_agentic_approach/secure_code_interpreter_tool_for_llm_agents"},{"title":"Together Code Interpreter: execute LLM-generated code seamlessly with a simple API call","url":"https://www.together.ai/blog/code-interpreter"},{"title":"GitHub - NavneelSinghal/LLMInterpreter: Can an LLM learn to run a program? This repository explores the state-tracking and simulation capabilities of language models on a custom esoteric programming language.","url":"https://github.com/NavneelSinghal/LLMInterpreter"},{"title":"CoRE: LLM as Interpreter for Natural Language Programming, Pseudo-Code Programming, and Flow Programming of AI Agents","url":"https://arxiv.org/html/2405.06907v1"},{"title":"LLMs as Interpreters: The Probabilistic Runtime for English Programs","url":"https://responseawareness.substack.com/p/llms-as-interpreters-the-probabilistic"},{"title":"Code Interpreter: Traditional vs. LLM Use Cases & Top 5 Tools | Obot AI","url":"https://obot.ai/resources/learning-center/code-interpreter/"}]

Based on the search results, I found the paper you're looking for:

## "Making LLMs Program Interpreters via Execution Trace Chain of Thought"

This work introduces ET-CoT (Execution Trace Chain of Thought), an app
…[truncated 1116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T21:57:16.500914+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Fine-tuned Small LLMs Still Significantly Outperform Zero-Shot\" text classification 2024 authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Fine-tuned Small LLMs Still Significantly Outperform Zero-Shot\" text classification 2024 authors venue"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T21:57:16.501093+00:00_

Web search results for query: ""Fine-tuned Small LLMs Still Significantly Outperform Zero-Shot" text classification 2024 authors venue"

Links: [{"title":"GitHub - mnbucher/text-cls-llms: Code for \"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\", arXiv 2024 · GitHub","url":"https://github.com/mnbucher/text-cls-llms"},{"title":"[2406.08660] Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification","url":"https://arxiv.org/abs/2406.08660"},{"title":"Fine-Tuned ‘Small’ LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification","url":"https://arxiv.org/html/2406.08660v1"},{"title":"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240608660J/abstract"},{"title":"[Literature Review] Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification","url":"https://www.themoonlight.io/en/review/fine-tuned-small-llms-still-significantly-outperform-zero-shot-generative-ai-models-in-text-classification"},{"title":"Bridging Zero-Shot and Fine-Tuned Performance in Text Classification through Retrieval-Augmented Prompting | American Scientific Research Journal for Engineering, Technology, and Sciences","url":"https://asrjetsjournal.org/American_Scientific_Journal/article/view/12048"},{"title":"(PDF) Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification","url":"https://www.researchgate.net/publication/381404182_Fine-Tuned_'Small'_LLMs_Still_Significantly_Outperform_Zero-Shot_Generative_AI_Models_in_Text_Classification"},{"title":"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/f
…[truncated 1572 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T21:57:16.501356+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "literature_map.yaml",
  "content": "categories:\n  execution-trace-llm:\n    description: \"Execution trace 辅助 LLM 代码理解/调试/推理\"\n    papers:\n      - title: \"NExT: Teaching Large Language Models to Reason about Code Execution\"\n        authors: \"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\"\n        year: 2024\n        venue: \"ICML 2024\"\n        role: method-component\n        key_finding: \"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\"\n        metrics:\n          mbpp_fix_rate_improvement: \"+26.1%\"\n          humaneval_fix_rate_improvement: \"+14.3%\"\n\n      - title: \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\"\n        authors: \"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\"\n        year: 2025\n        venue: \"Findings of EMNLP 2025\"\n        role: direct-competitor\n        key_finding: \"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\"\n        metrics: {}\n\n      - title: \"Code Execution as Grounded Supervision for LLM Reasoning\"\n        authors: \"Dongwon Jung, Wenxuan Zhou, Muhao Chen\"\n        year: 2025\n        venue: \"EMNLP 2025\"\n        role: method-component\n        key_finding: \"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\"\n        metrics: {}\n\n  code-verdict:\n    description: \"LLM 判断代码 pass/fail、正确性分类、mutation testing\"\n    papers:\n      - title: \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\"\n        authors: \"iSEngLab (Nanjing University)\"\n        year: 2024\n        venue: \"IEEE TSE 2024\"\n        role: direct-competitor\n        key_finding: \"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\"\n        metrics:\n          accuracy: \"79.7%\"\n          recall: \"83.2%\"\n          f1_improvement_from_finetuning: \"+10.22%\"\n\n      - title: \"Calibration and Correctness of Language Models for Code\"\n        authors: \"Claudio Spiess, David Gros, et al.\"\n        year: 2025\n        venue: \"ICSE 2025\"\n        role: evaluation\n        key_finding: \"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\"\n        metrics: {}\n\n      - title: \"Mutation-Guided LLM-based Test Generation at Meta\"\n        authors: \"Christopher Foster et al. (Meta)\"\n        year: 2025\n        venue: \"FSE 2025 (Industry)\"\n        role: evaluation\n        key_finding: \"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\"\n        metrics:\n          precision: \"0.95\"\n          recall: \"0.96\"\n          classes_evaluated: \"10795\"\n          test_acceptance_rate: \"73%\"\n\n  trace-compression:\n    description: \"Execution trace 的压缩、摘要、抽象方法\"\n    papers:\n      - title: \"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\"\n        authors: \"Aashish Yadavally, Yi Li, Tien Nguyen\"\n        year: 2024\n        venue: \"FSE 2024\"\n        role: method-component\n        key_finding: \"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\"\n        metrics:\n          exact_match: \"81.31%\"\n          rouge_lcs: \"0.954\"\n          fault_localization_accuracy: \"63.88%\"\n\n      - title: \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\"\n        authors: \"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\"\n        year: 2025\n        venue: \"KnowledgeNLP Workshop @ ACL 2025\"\n        role: background\n        key_finding: \"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\"\n        metrics: {}\n\n      - title: \"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\"\n        authors: \"OpenReview submission (ICML 2025 Workshop PRAL)\"\n        year: 2025\n        venue: \"ICML 2025 Workshop\"\n        role: method-component\n        key_finding: \"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\"\n        metrics:\n          cruxeval_o: \"70.0%\"\n          livecodebench_execution: \"88.3%\"\n\n  sft-classification:\n    description: \"用 SFT 做分类任务的方法论和 findings\"\n    papers:\n      - title: \"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\"\n        authors: \"Amirhossein Yousefiramandi, Ciaran Cooney\"\n        year: 2025\n        venue: \"arXiv 2512.12677\"\n        role: method-component\n        key_finding: \"对比 embedding-based（加分类头）vs instruction-based（prompt→response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\"\n        metrics: {}\n\n      - title: \"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\"\n        authors: \"Rohan Deb, Kiran Koshy Thekumparampil, et al.\"\n        year: 2025\n        venue: \"ICML 2025\"\n        role: background\n        key_finding: \"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\"\n        metrics: {}\n\n      - title: \"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\"\n        authors: \"Martin Juan José Bucher, Marco Martini\"\n        year: 2024\n        venue: \"arXiv 2406.08660\"\n        role: background\n        key_finding: \"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\"\n        metrics: {}\n\nmeta:\n  last_updated: \"2026-05-14\"\n  total_papers: 12\n  search_scope: \"2024-2026, top ML/NLP/SE venues\"\n  key_gaps:\n    - \"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\"\n    - \"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\"\n    - \"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "trace-verdict-study",
    "file": "literature_map.yaml",
    "content": "categories:\n  execution-trace-llm:\n    description: \"Execution trace 辅助 LLM 代码理解/调试/推理\"\n    papers:\n      - title: \"NExT: Teaching Large Language Models to Reason about Code Execution\"\n        authors: \"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\"\n        year: 2024\n        venue: \"ICML 2024\"\n        role: method-component\n        key_finding: \"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\"\n        metrics:\n          mbpp_fix_rate_improvement: \"+26.1%\"\n          humaneval_fix_rate_improvement: \"+14.3%\"\n\n      - title: \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\"\n        authors: \"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\"\n        year: 2025\n        venue: \"Findings of EMNLP 2025\"\n        role: direct-competitor\n        key_finding: \"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\"\n        metrics: {}\n\n      - title: \"Code Execution as Grounded Supervision for LLM Reasoning\"\n        authors: \"Dongwon Jung, Wenxuan Zhou, Muhao Chen\"\n        year: 2025\n        venue: \"EMNLP 2025\"\n        role: method-component\n        key_finding: \"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\"\n        metrics: {}\n\n  code-verdict:\n    description: \"LLM 判断代码 pass/fail、正确性分类、mutation testing\"\n    papers:\n      - title: \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\"\n        authors: \"iSEngLab (Nanjing University)\"\n        year: 2024\n        venue: \"IEEE TSE 2024\"\n        role: direct-competitor\n        key_finding: \"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\"\n        metrics:\n          accuracy: \"79.7%\"\n          recall: \"83.2%\"\n          f1_improvement_from_finetuning: \"+10.22%\"\n\n      - title: \"Calibration and Correctness of Language Models for Code\"\n        authors: \"Claudio Spiess, David Gros, et al.\"\n        year: 2025\n        venue: \"ICSE 2025\"\n        role: evaluation\n        key_finding: \"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\"\n        metrics: {}\n\n      - title: \"Mutation-Guided LLM-based Test Generation at Meta\"\n        authors: \"Christopher Foster et al. (Meta)\"\n        year: 2025\n        venue: \"FSE 2025 (Industry)\"\n        role: evaluation\n        key_finding: \"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\"\n        metrics:\n          precision: \"0.95\"\n          recall: \"0.96\"\n          classes_evaluated: \"10795\"\n          test_acceptance_rate: \"73%\"\n\n  trace-compression:\n    description: \"Execution trace 的压缩、摘要、抽象方法\"\n    papers:\n      - title: \"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\"\n        authors: \"Aashish Yadavally, Yi Li, Tien Nguyen\"\n        year: 2024\n        venue: \"FSE 2024\"\n        role: method-component\n        key_finding: \"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\"\n        metrics:\n          exact_match: \"81.31%\"\n          rouge_lcs: \"0.954\"\n          fault_localization_accuracy: \"63.88%\"\n\n      - title: \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\"\n        authors: \"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\"\n        year: 2025\n        venue: \"KnowledgeNLP Workshop @ ACL 2025\"\n        role: background\n        key_finding: \"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\"\n        metrics: {}\n\n      - title: \"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\"\n        authors: \"OpenReview submission (ICML 2025 Workshop PRAL)\"\n        year: 2025\n        venue: \"ICML 2025 Workshop\"\n        role: method-component\n        key_finding: \"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\"\n        metrics:\n          cruxeval_o: \"70.0%\"\n          livecodebench_execution: \"88.3%\"\n\n  sft-classification:\n    description: \"用 SFT 做分类任务的方法论和 findings\"\n    papers:\n      - title: \"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\"\n        authors: \"Amirhossein Yousefiramandi, Ciaran Cooney\"\n        year: 2025\n        venue: \"arXiv 2512.12677\"\n        role: method-component\n        key_finding: \"对比 embedding-based（加分类头）vs instruction-based（prompt→response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\"\n        metrics: {}\n\n      - title: \"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\"\n        authors: \"Rohan Deb, Kiran Koshy Thekumparampil, et al.\"\n        year: 2025\n        venue: \"ICML 2025\"\n        role: background\n        key_finding: \"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\"\n        metrics: {}\n\n      - title: \"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\"\n        authors: \"Martin Juan José Bucher, Marco Martini\"\n        year: 2024\n        venue: \"arXiv 2406.08660\"\n        role: background\n        key_finding: \"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\"\n        metrics: {}\n\nmeta:\n  last_updated: \"2026-05-14\"\n  total_papers: 12\n  search_scope: \"2024-2026, top ML/NLP/SE venues\"\n  key_gaps:\n    - \"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\"\n    - \"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\"\n    - \"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\"\n"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T21:57:16.501689+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T21:57:16.501919+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T21:57:16.502094+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T21:57:16.502374+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_map.yaml",
  "content": "categories:\n  execution-trace-llm:\n    description: \"Execution trace 辅助 LLM 代码理解/调试/推理\"\n    papers:\n      - title: \"NExT: Teaching Large Language Models to Reason about Code Execution\"\n        authors: \"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\"\n        year: 2024\n        venue: \"ICML 2024\"\n        role: method-component\n        key_finding: \"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\"\n        metrics:\n          mbpp_fix_rate_improvement: \"+26.1%\"\n          humaneval_fix_rate_improvement: \"+14.3%\"\n\n      - title: \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\"\n        authors: \"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\"\n        year: 2025\n        venue: \"Findings of EMNLP 2025\"\n        role: direct-competitor\n        key_finding: \"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\"\n        metrics: {}\n\n      - title: \"Code Execution as Grounded Supervision for LLM Reasoning\"\n        authors: \"Dongwon Jung, Wenxuan Zhou, Muhao Chen\"\n        year: 2025\n        venue: \"EMNLP 2025\"\n        role: method-component\n        key_finding: \"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\"\n        metrics: {}\n\n  code-verdict:\n    description: \"LLM 判断代码 pass/fail、正确性分类、mutation testing\"\n    papers:\n      - title: \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\"\n        authors: \"iSEngLab (Nanjing University)\"\n        year: 2024\n        venue: \"IEEE TSE 2024\"\n        role: direct-competitor\n        key_finding: \"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\"\n        metrics:\n          accuracy: \"79.7%\"\n          recall: \"83.2%\"\n          f1_improvement_from_finetuning: \"+10.22%\"\n\n      - title: \"Calibration and Correctness of Language Models for Code\"\n        authors: \"Claudio Spiess, David Gros, et al.\"\n        year: 2025\n        venue: \"ICSE 2025\"\n        role: evaluation\n        key_finding: \"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\"\n        metrics: {}\n\n      - title: \"Mutation-Guided LLM-based Test Generation at Meta\"\n        authors: \"Christopher Foster et al. (Meta)\"\n        year: 2025\n        venue: \"FSE 2025 (Industry)\"\n        role: evaluation\n        key_finding: \"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\"\n        metrics:\n          precision: \"0.95\"\n          recall: \"0.96\"\n          classes_evaluated: \"10795\"\n          test_acceptance_rate: \"73%\"\n\n  trace-compression:\n    description: \"Execution trace 的压缩、摘要、抽象方法\"\n    papers:\n      - title: \"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\"\n        authors: \"Aashish Yadavally, Yi Li, Tien Nguyen\"\n        year: 2024\n        venue: \"FSE 2024\"\n        role: method-component\n        key_finding: \"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\"\n        metrics:\n          exact_match: \"81.31%\"\n          rouge_lcs: \"0.954\"\n          fault_localization_accuracy: \"63.88%\"\n\n      - title: \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\"\n        authors: \"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\"\n        year: 2025\n        venue: \"KnowledgeNLP Workshop @ ACL 2025\"\n        role: background\n        key_finding: \"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\"\n        metrics: {}\n\n      - title: \"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\"\n        authors: \"ICML 2025 Workshop PRAL\"\n        year: 2025\n        venue: \"ICML 2025 Workshop\"\n        role: method-component\n        key_finding: \"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\"\n        metrics:\n          cruxeval_o: \"70.0%\"\n          livecodebench_execution: \"88.3%\"\n\n  sft-classification:\n    description: \"用 SFT 做分类任务的方法论和 findings\"\n    papers:\n      - title: \"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\"\n        authors: \"Amirhossein Yousefiramandi, Ciaran Cooney\"\n        year: 2025\n        venue: \"arXiv 2512.12677\"\n        role: method-component\n        key_finding: \"对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\"\n        metrics: {}\n\n      - title: \"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\"\n        authors: \"Rohan Deb, Kiran Koshy Thekumparampil, et al.\"\n        year: 2025\n        venue: \"ICML 2025\"\n        role: background\n        key_finding: \"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\"\n        metrics: {}\n\n      - title: \"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\"\n        authors: \"Martin Juan Jose Bucher, Marco Martini\"\n        year: 2024\n        venue: \"arXiv 2406.08660\"\n        role: background\n        key_finding: \"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\"\n        metrics: {}\n\nmeta:\n  last_updated: \"2026-05-14\"\n  total_papers: 12\n  search_scope: \"2024-2026, top ML/NLP/SE venues\"\n  key_gaps:\n    - \"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\"\n    - \"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\"\n    - \"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_map.yaml",
    "content": "categories:\n  execution-trace-llm:\n    description: \"Execution trace 辅助 LLM 代码理解/调试/推理\"\n    papers:\n      - title: \"NExT: Teaching Large Language Models to Reason about Code Execution\"\n        authors: \"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\"\n        year: 2024\n        venue: \"ICML 2024\"\n        role: method-component\n        key_finding: \"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\"\n        metrics:\n          mbpp_fix_rate_improvement: \"+26.1%\"\n          humaneval_fix_rate_improvement: \"+14.3%\"\n\n      - title: \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\"\n        authors: \"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\"\n        year: 2025\n        venue: \"Findings of EMNLP 2025\"\n        role: direct-competitor\n        key_finding: \"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\"\n        metrics: {}\n\n      - title: \"Code Execution as Grounded Supervision for LLM Reasoning\"\n        authors: \"Dongwon Jung, Wenxuan Zhou, Muhao Chen\"\n        year: 2025\n        venue: \"EMNLP 2025\"\n        role: method-component\n        key_finding: \"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\"\n        metrics: {}\n\n  code-verdict:\n    description: \"LLM 判断代码 pass/fail、正确性分类、mutation testing\"\n    papers:\n      - title: \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\"\n        authors: \"iSEngLab (Nanjing University)\"\n        year: 2024\n        venue: \"IEEE TSE 2024\"\n        role: direct-competitor\n        key_finding: \"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\"\n        metrics:\n          accuracy: \"79.7%\"\n          recall: \"83.2%\"\n          f1_improvement_from_finetuning: \"+10.22%\"\n\n      - title: \"Calibration and Correctness of Language Models for Code\"\n        authors: \"Claudio Spiess, David Gros, et al.\"\n        year: 2025\n        venue: \"ICSE 2025\"\n        role: evaluation\n        key_finding: \"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\"\n        metrics: {}\n\n      - title: \"Mutation-Guided LLM-based Test Generation at Meta\"\n        authors: \"Christopher Foster et al. (Meta)\"\n        year: 2025\n        venue: \"FSE 2025 (Industry)\"\n        role: evaluation\n        key_finding: \"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\"\n        metrics:\n          precision: \"0.95\"\n          recall: \"0.96\"\n          classes_evaluated: \"10795\"\n          test_acceptance_rate: \"73%\"\n\n  trace-compression:\n    description: \"Execution trace 的压缩、摘要、抽象方法\"\n    papers:\n      - title: \"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\"\n        authors: \"Aashish Yadavally, Yi Li, Tien Nguyen\"\n        year: 2024\n        venue: \"FSE 2024\"\n        role: method-component\n        key_finding: \"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\"\n        metrics:\n          exact_match: \"81.31%\"\n          rouge_lcs: \"0.954\"\n          fault_localization_accuracy: \"63.88%\"\n\n      - title: \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\"\n        authors: \"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\"\n        year: 2025\n        venue: \"KnowledgeNLP Workshop @ ACL 2025\"\n        role: background\n        key_finding: \"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\"\n        metrics: {}\n\n      - title: \"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\"\n        authors: \"ICML 2025 Workshop PRAL\"\n        year: 2025\n        venue: \"ICML 2025 Workshop\"\n        role: method-component\n        key_finding: \"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\"\n        metrics:\n          cruxeval_o: \"70.0%\"\n          livecodebench_execution: \"88.3%\"\n\n  sft-classification:\n    description: \"用 SFT 做分类任务的方法论和 findings\"\n    papers:\n      - title: \"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\"\n        authors: \"Amirhossein Yousefiramandi, Ciaran Cooney\"\n        year: 2025\n        venue: \"arXiv 2512.12677\"\n        role: method-component\n        key_finding: \"对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\"\n        metrics: {}\n\n      - title: \"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\"\n        authors: \"Rohan Deb, Kiran Koshy Thekumparampil, et al.\"\n        year: 2025\n        venue: \"ICML 2025\"\n        role: background\n        key_finding: \"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\"\n        metrics: {}\n\n      - title: \"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\"\n        authors: \"Martin Juan Jose Bucher, Marco Martini\"\n        year: 2024\n        venue: \"arXiv 2406.08660\"\n        role: background\n        key_finding: \"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\"\n        metrics: {}\n\nmeta:\n  last_updated: \"2026-05-14\"\n  total_papers: 12\n  search_scope: \"2024-2026, top ML/NLP/SE venues\"\n  key_gaps:\n    - \"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\"\n    - \"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\"\n    - \"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\"\n"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T21:57:16.502714+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-vota_20260514T215130",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-14T21:57:16.502946+00:00_

已写入 `artifacts/literature_map.yaml`，12 篇论文覆盖 4 个方向。

关键发现：

- **最重要的负面结果**：Wang et al. (EMNLP 2025 Findings) 发现原始 execution trace 对 SFT 帮助有限——这恰好支持 VOTA 的核心动机：需要针对性的 trace 压缩/抽象，而非直接喂原始 trace
- **最接近的 competitor**：APPT (TSE 2024) 做 patch 正确性二分类达 79.7% accuracy，但用 BERT 而非 decoder LLM，且不用 trace 信息
- **文献空白**：没有工作将 compressed execution trace + SFT 用于 binary verdict 分类——这正是 VOTA 的差异化定位

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_literature-vota_20260514T215130"
}
```

</details>

---
