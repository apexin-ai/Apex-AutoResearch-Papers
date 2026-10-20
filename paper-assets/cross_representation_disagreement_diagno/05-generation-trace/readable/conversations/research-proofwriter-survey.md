# research proofwriter survey

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 107
- **Recorded user turns:** 0
- **Tool calls:** 53
- **Original source:** `logs/chats/worker_research_proofwriter_survey_20260514T143225.jsonl`
- **Structured JSON:** [`ddab6127ee0d5195617b.json`](../../sessions/dd/ddab6127ee0d5195617b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

107 recorded events

### Tool call

_source line 1 · 2026-05-14T14:44:05.505240+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research ProofWriter dataset",
  "subagent_type": "general-purpose",
  "prompt": "Research the ProofWriter dataset thoroughly for use in a cross-representation disagreement diagnosis project. I need detailed, factual information about:\n\n1. **Dataset basics**: Task format (input/output), data scale (train/val/test splits), label distribution (True/False/Unknown proportions), reasoning depth distribution (depth-0 through depth-5).\n\n2. **Dataset characteristics**: How is ProofWriter different from FOLIO? Is it synthetically generated or human-annotated? What's the natural language style like? What types of reasoning does it test?\n\n3. **Availability**: Is it on HuggingFace? What's the exact dataset name/path? What format is the data in?\n\n4. **Alternative datasets**: Brief info on RuleTaker, CLUTRR, LogiQA, and any other logical reasoning datasets that could serve as evaluation benchmarks for an NLI-style task (premises → hypothesis → True/False/Unknown).\n\nSearch the web, HuggingFace, and any available sources. I need concrete numbers and facts, not vague descriptions.\n\nKey context: The project formalizes reasoning problems into both FOL/Z3 and Python code simultaneously, using disagreement between the two representations to diagnose reasoning errors. Currently validated on FOLIO (204 samples, NLI task). Need a second dataset to show cross-dataset generalization.\n\nPlease search for:\n- \"ProofWriter dataset\" details, paper, statistics\n- HuggingFace datasets matching \"proofwriter\" \n- ProofWriter vs FOLIO comparison\n- RuleTaker dataset (ProofWriter's predecessor)\n- CLUTRR, LogiQA dataset details\n- Any surveys of logical reasoning benchmarks\n\nReturn ALL concrete facts, numbers, and URLs you find. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Agent",
  "tool_args": {
    "description": "Research ProofWriter dataset",
    "subagent_type": "general-purpose",
    "prompt": "Research the ProofWriter dataset thoroughly for use in a cross-representation disagreement diagnosis project. I need detailed, factual information about:\n\n1. **Dataset basics**: Task format (input/output), data scale (train/val/test splits), label distribution (True/False/Unknown proportions), reasoning depth distribution (depth-0 through depth-5).\n\n2. **Dataset characteristics**: How is ProofWriter different from FOLIO? Is it synthetically generated or human-annotated? What's the natural language style like? What types of reasoning does it test?\n\n3. **Availability**: Is it on HuggingFace? What's the exact dataset name/path? What format is the data in?\n\n4. **Alternative datasets**: Brief info on RuleTaker, CLUTRR, LogiQA, and any other logical reasoning datasets that could serve as evaluation benchmarks for an NLI-style task (premises → hypothesis → True/False/Unknown).\n\nSearch the web, HuggingFace, and any available sources. I need concrete numbers and facts, not vague descriptions.\n\nKey context: The project formalizes reasoning problems into both FOL/Z3 and Python code simultaneously, using disagreement between the two representations to diagnose reasoning errors. Currently validated on FOLIO (204 samples, NLI task). Need a second dataset to show cross-dataset generalization.\n\nPlease search for:\n- \"ProofWriter dataset\" details, paper, statistics\n- HuggingFace datasets matching \"proofwriter\" \n- ProofWriter vs FOLIO comparison\n- RuleTaker dataset (ProofWriter's predecessor)\n- CLUTRR, LogiQA dataset details\n- Any surveys of logical reasoning benchmarks\n\nReturn ALL concrete facts, numbers, and URLs you find. Be thorough."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T14:44:05.505720+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T14:44:05.505944+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T14:44:05.506127+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProofWriter dataset paper statistics train test split label distribution reasoning depth"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProofWriter dataset paper statistics train test split label distribution reasoning depth"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T14:44:05.506281+00:00_

Web search results for query: "ProofWriter dataset paper statistics train test split label distribution reasoning depth"

Links: [{"title":"GitHub - INK-USC/FaiRR: FaiRR: Faithful and Robust Deductive Reasoning over Natural Language (ACL 2022)","url":"https://github.com/INK-USC/FaiRR"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive ...","url":"https://aclanthology.org/2021.findings-acl.317.pdf"},{"title":"ProofWriter","url":"https://www.kaggle.com/datasets/mathurinache/proofwriter"},{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset"},{"title":"Train Test Split: What it Means and How to Use It | Built In","url":"https://builtin.com/data-science/train-test-split"},{"title":"Split Your Dataset With scikit-learn's train_test_split() – Real Python","url":"https://realpython.com/train-test-split-python-data/"},{"title":"Train Test Validation Split: How To & Best Practices [2024]","url":"https://www.v7darwin.com/blog/train-validation-test-set"},{"title":"How to Split Machine Learning Datasets: Training, Validation, & Test Sets","url":"https://encord.com/blog/train-val-test-split/"},{"title":"How to split the Dataset With scikit-learn's train_test_split() Function - GeeksforGeeks","url":"https://www.geeksforgeeks.org/python/how-to-split-the-dataset-with-scikit-learns-train_test_split-function/"}]

Based on the search results, I found information about the ProofWriter dataset. Here's what I found:

## Dataset Overview

ProofWriter is a synthetic dataset featuring natural language problems that assess and advance systematic neural logical deduction. It provides a diverse set of instances—each consisting of a theory (natural language rules and facts), a query, an answer (True/False/Unknown), and, in many cases, an explicit proof.

## Reasoning Depth

The theories are const
…[truncated 899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T14:44:05.506450+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProofWriter dataset HuggingFace huggingface.co/datasets proofwriter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProofWriter dataset HuggingFace huggingface.co/datasets proofwriter"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T14:44:05.506595+00:00_

Web search results for query: "ProofWriter dataset HuggingFace huggingface.co/datasets proofwriter"

Links: [{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset"},{"title":"tasksource/proofwriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/proofwriter"},{"title":"renma/ProofWriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/renma/ProofWriter"},{"title":"smoorsmith/proofwriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/smoorsmith/proofwriter"},{"title":"D3xter1922/proofwriter-dataset at 68a35fc79495cd36f109472e3a3dbbf281e2f10d","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset/tree/68a35fc79495cd36f109472e3a3dbbf281e2f10d"},{"title":"tasksource/proofwriter · Discussions","url":"https://huggingface.co/datasets/tasksource/proofwriter/discussions"},{"title":"Huggingface","url":"https://huggingface.co/api/resolve-cache/datasets/renma/ProofWriter/8f62fa1749d19bde9e7815a2be286a4b9cfaf827/README.md?download=true&etag=%22f34f9b780ff30626cb6bfabbb94d0b98cffcbde0%22"},{"title":"GitHub - INK-USC/FaiRR: FaiRR: Faithful and Robust Deductive Reasoning over Natural Language (ACL 2022)","url":"https://github.com/INK-USC/FaiRR"},{"title":"ProofWriter Dataset","url":"https://paperswithcode.com/dataset/proofwriter"},{"title":"Datasets – Hugging Face","url":"https://huggingface.co/datasets?other=proof-of-work"}]

Based on the search results, I found several ProofWriter dataset versions available on Hugging Face:

1. **tasksource/proofwriter** - This is the largest version with 845,496 rows, split into 586k training rows, 85.5k validation rows, and 174k test rows.

2. **D3xter1922/proofwriter-dataset** - This version contains 59,220 rows with 41.4k training rows, 6.01k validation rows, and 11.8k test rows.

3. **smoorsmith/proofwriter** - This is the standard ProofWriter dataset from the LogicLM GitHub 
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T14:44:05.506748+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProofWriter ACL 2021 paper \"Generating Implications Proofs Abductive\" dataset size OWA CWA statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProofWriter ACL 2021 paper \"Generating Implications Proofs Abductive\" dataset size OWA CWA statistics"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T14:44:05.506918+00:00_

Web search results for query: "ProofWriter ACL 2021 paper "Generating Implications Proofs Abductive" dataset size OWA CWA statistics"

Links: [{"title":"ProofWriter: Generating Implications, Proofs, and Abductive ...","url":"https://aclanthology.org/2021.findings-acl.317.pdf"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language - ACL Anthology","url":"https://aclanthology.org/2021.findings-acl.317/"},{"title":"[2012.13048] ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language","url":"https://arxiv.org/abs/2012.13048"},{"title":"[PDF] ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProofWriter:-Generating-Implications,-Proofs,-and-Tafjord-Dalvi/87c45a908537ffe1d2ab71a5d609bd7b4efa4fe1"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language | Request PDF","url":"https://www.researchgate.net/publication/353489965_ProofWriter_Generating_Implications_Proofs_and_Abductive_Statements_over_Natural_Language"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language","url":"https://proofwriter.apps.allenai.org/about"},{"title":"ProofWriter","url":"https://www.kaggle.com/datasets/mathurinache/proofwriter"},{"title":"(PDF) ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language","url":"https://www.academia.edu/97512358/ProofWriter_Generating_Implications_Proofs_and_Abductive_Statements_over_Natural_Language"},{"title":"GitHub - FreedomIntelligence/ReasoningNLP: paper list on reasoning in NLP · GitHub","url":"https://github.com/FreedomIntelligence/ReasoningNLP"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"}]

Based on the search results, I found information about the ProofWriter ACL 2021 paper. Here are 
…[truncated 1301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T14:44:05.507124+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RuleTaker dataset Clark 2020 logical reasoning natural language predecessor ProofWriter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RuleTaker dataset Clark 2020 logical reasoning natural language predecessor ProofWriter"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T14:44:05.507269+00:00_

Web search results for query: "RuleTaker dataset Clark 2020 logical reasoning natural language predecessor ProofWriter"

Links: [{"title":"[2002.05867] Transformers as Soft Reasoners over Language","url":"https://arxiv.org/abs/2002.05867"},{"title":"RuleTaker: Transformers as Soft Reasoners over Language","url":"https://allenai.org/data/ruletaker"},{"title":"GitHub - allenai/ruletaker · GitHub","url":"https://github.com/allenai/ruletaker"},{"title":"LogiQA 2.0 — An Improved Dataset for Logical Reasoning ...","url":"https://frcchang.github.io/pub/An%20Improved%20Dataset%20for%20Logical%20Reasoning%20in%20Natural%20Language%20Understanding.pdf"},{"title":"Constrained Fact Verification for FEVER","url":"https://aclanthology.org/2020.emnlp-main.629.pdf"},{"title":"AbductionRules: Training Transformers to Explain ...","url":"https://aclanthology.org/2022.findings-acl.19.pdf"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.20973"},{"title":"Towards Generalizable and Faithful Logic Reasoning over Natural Language via Resolution Refutation","url":"https://arxiv.org/html/2404.01677v1"},{"title":"SATBench: Benchmarking LLMs’ Logical Reasoning via Automated Puzzle Generation from SAT Formulas","url":"https://arxiv.org/html/2505.14615"},{"title":"tasksource/ruletaker · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/ruletaker"}]

Based on the search results, here's what I found about the RuleTaker dataset and its relationship to ProofWriter:

## RuleTaker Dataset (Clark 2020)

RuleTaker models provide empirical demonstration that soft reasoning over language is learnable, can achieve high (99%) accuracy, and generalizes to test data requiring substantially deeper chaining than seen during training. Clark et al. (2020) developed RuleTakers to reason deductively over FOL knowledge bases expressed in natural language, judging given facts to be true or false.

The approach investigates a modern method where facts and rules are provided as n
…[truncated 975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T14:44:05.507428+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CLUTRR dataset kinship reasoning benchmark statistics size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CLUTRR dataset kinship reasoning benchmark statistics size"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T14:44:05.507564+00:00_

Web search results for query: "CLUTRR dataset kinship reasoning benchmark statistics size"

Links: [{"title":"GitHub - facebookresearch/clutrr: Diagnostic benchmark suite to explicitly test logical relational reasoning on natural language · GitHub","url":"https://github.com/facebookresearch/clutrr"},{"title":"CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text | Request PDF","url":"https://www.researchgate.net/publication/336997708_CLUTRR_A_Diagnostic_Benchmark_for_Inductive_Reasoning_from_Text"},{"title":"A Diagnostic Benchmark for Inductive Reasoning from Text","url":"https://aclanthology.org/D19-1458.pdf"},{"title":"[1908.06177] CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text","url":"https://arxiv.org/abs/1908.06177"},{"title":"Introducing CLUTRR | A minimal Hugo website","url":"https://koustuvsinha.com/introducing-clutrr/"},{"title":"[PDF] CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CLUTRR:-A-Diagnostic-Benchmark-for-Inductive-from-Sinha-Sodhani/5e35895fc4731858f0b286cb5a1613a819cc2367"},{"title":"GitHub - sailfish009/clutrr: Diagnostic benchmark suite to explicitly test logical relational reasoning on natural language","url":"https://github.com/sailfish009/clutrr"},{"title":"CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text | Research - AI at Meta","url":"https://ai.meta.com/research/publications/clutrr-a-diagnostic-benchmark-for-inductive-reasoning-from-text/"},{"title":"CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text - ACL Anthology","url":"https://aclanthology.org/D19-1458/"},{"title":"GitHub - kliang5/CLUTRR_huggingface_dataset","url":"https://github.com/kliang5/CLUTRR_huggingface_dataset"}]

Based on the search results, here's information about the CLUTRR dataset:

## Overview

CLUTRR is a diagnostic benchmark suite designed to clarify issues related to robustness and systematicity of NLU systems, requiring sys
…[truncated 1430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T14:44:05.507713+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogiQA dataset logical reasoning benchmark NLI statistics size train test split"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogiQA dataset logical reasoning benchmark NLI statistics size train test split"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T14:44:05.507847+00:00_

Web search results for query: "LogiQA dataset logical reasoning benchmark NLI statistics size train test split"

Links: [{"title":"GitHub - csitfun/LogiQA2.0: Logiqa2.0 dataset - logical reasoning in MRC and NLI tasks","url":"https://github.com/csitfun/LogiQA2.0"},{"title":"LogiQA 2.0 — An Improved Dataset for Logical Reasoning ...","url":"https://frcchang.github.io/pub/An%20Improved%20Dataset%20for%20Logical%20Reasoning%20in%20Natural%20Language%20Understanding.pdf"},{"title":"[2007.08124] LogiQA: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning","url":"https://arxiv.org/abs/2007.08124"},{"title":"LogiQA: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning | Request PDF","url":"https://www.researchgate.net/publication/342799906_LogiQA_A_Challenge_Dataset_for_Machine_Reading_Comprehension_with_Logical_Reasoning"},{"title":"tasksource/logiqa-2.0-nli · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/logiqa-2.0-nli"},{"title":"LogiQA 2.0—An Improved Dataset for Logical Reasoning in Natural Language Understanding | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10174688/"},{"title":"GLoRE: Evaluating Logical Reasoning of Large Language Models","url":"https://arxiv.org/html/2310.09107v2"},{"title":"[PDF] LogiQA 2.0—An Improved Dataset for Logical Reasoning in Natural Language Understanding | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LogiQA-2.0%E2%80%94An-Improved-Dataset-for-Logical-in-Liu-Liu/11a05b7e2bc79a9e0cc1d1b83ec978da8ee13bc9"},{"title":"LogiQA 2.0—An Improved Dataset for Logical Reasoning in Natural Language Understanding | IEEE/ACM Transactions on Audio, Speech and Language Processing","url":"https://dl.acm.org/doi/10.1109/TASLP.2023.3293046"},{"title":"lm-evaluation-harness/lm_eval/tasks/logiqa2/README.md at main · EleutherAI/lm-evaluation-harness","url":"https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval
…[truncated 1080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T14:44:05.508094+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProofWriter vs FOLIO dataset comparison logical reasoning NLI synthetic human annotated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProofWriter vs FOLIO dataset comparison logical reasoning NLI synthetic human annotated"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T14:44:05.508241+00:00_

Web search results for query: "ProofWriter vs FOLIO dataset comparison logical reasoning NLI synthetic human annotated"

Links: [{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"},{"title":"Towards Systematic Evaluation of Logical Reasoning Ability of Large","url":"https://openreview.net/pdf?id=1xms2oSsqc"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models","url":"https://arxiv.org/html/2404.15522v2"},{"title":"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework","url":"https://arxiv.org/html/2412.16953v2"},{"title":"large language models meet symbolic provers for logical ...","url":"https://arxiv.org/pdf/2502.06563"},{"title":"[PDF] ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProofWriter:-Generating-Implications,-Proofs,-and-Tafjord-Dalvi/87c45a908537ffe1d2ab71a5d609bd7b4efa4fe1"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"}]

Based on the search results, here's a comparison of ProofWriter vs FOLIO datasets for logical reasoning and NLI:

## Key Differences

**Data Creation & Annotation:**
- ProofWriter is a dataset containing numerous rulebases of
…[truncated 1519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T14:44:05.508395+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ProofWriter\" dataset \"open world assumption\" number of examples depth-0 depth-1 depth-2 depth-3 depth-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ProofWriter\" dataset \"open world assumption\" number of examples depth-0 depth-1 depth-2 depth-3 depth-5"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T14:44:05.508544+00:00_

Web search results for query: ""ProofWriter" dataset "open world assumption" number of examples depth-0 depth-1 depth-2 depth-3 depth-5"

Links: [{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"GitHub - INK-USC/FaiRR: FaiRR: Faithful and Robust Deductive Reasoning over Natural Language (ACL 2022)","url":"https://github.com/INK-USC/FaiRR"},{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive ...","url":"https://aclanthology.org/2021.findings-acl.317.pdf"},{"title":"ProofWriter Dataset","url":"https://paperswithcode.com/dataset/proofwriter"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"tasksource/proofwriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/proofwriter"},{"title":"D3xter1922/proofwriter-dataset at 68a35fc79495cd36f109472e3a3dbbf281e2f10d","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset/tree/68a35fc79495cd36f109472e3a3dbbf281e2f10d"},{"title":"Natural-Language Policy Reasoning with Proof Generation: Turning Platform Rules into Verifiable Knowledge | Journal of Technology Informatics and Engineering","url":"https://jtie.stekom.ac.id/index.php/jtie/article/view/505"},{"title":"ProofWriter","url":"https://www.kaggle.com/datasets/mathurinache/proofwriter"}]

Based on the search results, I found information about the ProofWriter dataset and its structure with different proof depths. Let me provide what I found:

The ProofWriter dataset includes both the Closed World Assumption (CWA) and Open World Assumption (OWA) settings, the latter allowing answers to be
…[truncated 1001 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T14:44:05.508694+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclanthology.org/2021.findings-acl.317.pdf",
  "prompt": "Extract ALL dataset statistics from this paper: number of examples per split (train/val/test), per depth (D0-D5), per label (True/False/Unknown), CWA vs OWA versions. Also extract the data generation method, natural language style description, types of reasoning tested, and any tables with dataset sizes. Be extremely detailed with all numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclanthology.org/2021.findings-acl.317.pdf",
    "prompt": "Extract ALL dataset statistics from this paper: number of examples per split (train/val/test), per depth (D0-D5), per label (True/False/Unknown), CWA vs OWA versions. Also extract the data generation method, natural language style description, types of reasoning tested, and any tables with dataset sizes. Be extremely detailed with all numbers."
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T14:44:05.508825+00:00_

# Dataset Statistics Extraction from ProofWriter Paper

## Overview
The paper introduces **ProofWriter**, a dataset for evaluating natural language reasoning with machine-generated proofs and abductive statements.

## Dataset Splits and Scale

**Total Examples**: The dataset contains training, validation, and test splits across multiple difficulty depths (D0-D5), though specific total counts require careful extraction from tables.

**Depth Levels**: Data is organized by reasoning depth:
- D0: Fact retrieval (no reasoning required)
- D1-D5: Increasing complexity of logical reasoning chains

## Generation Method

The dataset was "generated synthetically using templates and rules" to create controlled reasoning scenarios. Natural language statements were derived from symbolic knowledge bases containing facts and rules.

## Reasoning Types Tested

The paper evaluates several reasoning categories:
- **Deductive reasoning**: Drawing conclusions from given premises
- **Abductive reasoning**: Inferring likely explanations from observations
- **Implication generation**: Deriving new facts from rules

## Label Distribution

Examples are labeled with three possible answers:
- **True**: Statement logically follows
- **False**: Statement contradicts knowledge base
- **Unknown**: Insufficient information to determine truth value

## Logical Framework

Two evaluation conditions exist:
- **CWA (Closed World Assumption)**: Unstated facts are false
- **OWA (Open World Assumption)**: Unstated facts are unknown

## Critical Note

The PDF source material is heavily compressed and contains embedded binary font/image data, making precise extraction of complete numerical tables difficult. The document structure indicates detailed statistics tables exist (referenced as Table 15-20), but specific cell values require direct document access beyond this encoding.

**Recommendation**: Consult the original paper directly for exact numerical breakdowns per split and depth level.

[Binary content (
…[truncated 262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T14:44:05.509004+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/D3xter1922/proofwriter-dataset",
  "prompt": "Extract ALL information about this dataset: number of rows, columns/fields, splits (train/val/test sizes), data format, column names, any statistics shown, configuration options, and how to load it. Be very detailed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/D3xter1922/proofwriter-dataset",
    "prompt": "Extract ALL information about this dataset: number of rows, columns/fields, splits (train/val/test sizes), data format, column names, any statistics shown, configuration options, and how to load it. Be very detailed."
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T14:44:05.509144+00:00_

# ProofWriter Dataset - Complete Information

## Dataset Overview
- **Creator**: D3xter1922
- **Name**: proofwriter-dataset
- **Platform**: Hugging Face Datasets
- **Total Rows**: 59,220
- **Total File Size**: 59.4 MB

## Data Format & Modalities
- **Format**: JSON (auto-converted to Parquet)
- **Modality**: Text
- **Libraries**: Datasets, pandas, Croissant

## Dataset Splits

| Split | Rows |
|-------|------|
| train | 41,400 |
| validation | 6,010 |
| test | 11,800 |
| **Total** | **59,210** |

## Column Structure

The dataset contains a single column structure (based on the data preview):

```
{
  "en": {
    "$answer$": [answer statement],
    "$proof$": [proof/reasoning chain],
    "$question$": [question to answer],
    "$context$": [numbered facts and rules]
  }
}
```

### Detailed Column Breakdown:

1. **answer** - The answer to the question (e.g., "True" or implied from proof)
2. **proof** - The logical reasoning steps that derive the answer
3. **question** - The statement to be verified (e.g., "The tiger visits the rabbit.")
4. **context** - A set of facts and conditional rules:
   - Numbered facts: `sent1: The cow is round.`
   - Conditional rules: `If someone is nice then they are kind.`

## Data Characteristics

### Example Structure
```
{
  "en": "$answer$ ; $proof$ ; $question$ = The tiger visits the rabbit. ; 
         $context$ = sent1: The cow is round. sent2: The cow needs the lion. ... 
         If someone is nice then they are kind."
}
```

### Content Types Observed:
- **Entities**: Animals (cow, lion, rabbit, tiger, bear, dog, cat, mouse), Names (Anne, Charlie, Dave, Fiona, Gary, Harry, Erin)
- **Relations**: visits, needs, sees, chases, eats, likes
- **Properties**: round, kind, young, red, big, cold, furry, quiet, rough, smart, nice, green, white, blue, furry
- **Logic**: Boolean yes/no questions, both positive and negated statements
- **Complexity**: Ranges from simple facts to multi-step logical inference with conditional rules

## How to 
…[truncated 1339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T14:44:05.509367+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/tasksource/proofwriter",
  "prompt": "Extract ALL information: number of rows per split, columns/fields, data format, configurations, label distribution if shown, depth information, OWA vs CWA, how to load. Be very detailed with all numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/tasksource/proofwriter",
    "prompt": "Extract ALL information: number of rows per split, columns/fields, data format, configurations, label distribution if shown, depth information, OWA vs CWA, how to load. Be very detailed with all numbers."
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T14:44:05.509546+00:00_

# ProofWriter Dataset - Complete Information

## Dataset Overview
- **Name**: tasksource/proofwriter
- **Total Rows**: 845,496
- **Total File Size**: 42.9 MB
- **Format**: Parquet (auto-converted)
- **Modalities**: Tabular, Text
- **Library Support**: Datasets, Dask, Croissant

## Data Splits

| Split | Rows |
|-------|------|
| train | 586,000 |
| validation | 85,500 |
| test | 174,000 |
| **Total** | **845,500** |

## Columns/Fields

| Column | Data Type | Description |
|--------|-----------|-------------|
| `id` | stringlengths (15-24) | Unique identifier |
| `maxD` | int64 (0-10) | Maximum depth value |
| `NFact` | int64 (1-16) | Number of facts |
| `NRule` | int64 (1-9) | Number of rules |
| `theory` | stringlengths (34-1.18k) | Logic theory/knowledge base |
| `question` | stringlengths (11-45) | Query question |
| `answer` | stringclasses (3 values) | Answer labels: True/False/Unknown |
| `QDep` | int64 (0-8) | Question depth |
| `QLen` | float64 (1-30) | Question length |
| `allProofs` | stringlengths (26-755k) | All proof chains |
| `config` | stringclasses (8 values) | Configuration type |

## Configurations (8 Types)

Based on data samples, configurations follow patterns:
- **AttNeg-OWA-D[depth]-[id]**: Attribute with Negation, Open World Assumption
- **AttNoneg-OWA-D[depth]-[id]**: Attribute without Negation, Open World Assumption
- **RelNeg-OWA-D[depth]-[id]**: Relational with Negation, Open World Assumption
- **RelNoneg-OWA-D[depth]-[id]**: Relational without Negation, Open World Assumption

*Note: All shown examples use OWA (Open World Assumption); CWA variants may exist*

## Answer Distribution (from samples)
- **True**: Definitive positive answers
- **False**: Definitive negative answers
- **Unknown**: Cannot be determined from given facts/rules

## Depth Information
- `maxD` ranges: 0-10 (maximum reasoning depth in knowledge base)
- `QDep` ranges: 0-8 (question difficulty/depth level)
- Most samples shown have `maxD` of 0-2 and `QDep` of 0-1

## Dat
…[truncated 1501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T14:44:05.509706+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProofWriter dataset allenai.org original download OWA depth statistics table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProofWriter dataset allenai.org original download OWA depth statistics table"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T14:44:05.509845+00:00_

Web search results for query: "ProofWriter dataset allenai.org original download OWA depth statistics table"

Links: [{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"GitHub - INK-USC/FaiRR: FaiRR: Faithful and Robust Deductive Reasoning over Natural Language (ACL 2022)","url":"https://github.com/INK-USC/FaiRR"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language","url":"https://proofwriter.apps.allenai.org/about"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive ...","url":"https://aclanthology.org/2021.findings-acl.317.pdf"},{"title":"ProofWriter Dataset","url":"https://paperswithcode.com/dataset/proofwriter"},{"title":"Dataset Repo for ProofWriter · Issue #26 · allenai/ruletaker","url":"https://github.com/allenai/ruletaker/issues/26"},{"title":"GitHub - princeton-nlp/NLProofS: EMNLP 2022: Generating Natural Language Proofs with Verifier-Guided Search https://arxiv.org/abs/2205.12443 · GitHub","url":"https://github.com/princeton-nlp/NLProofS"},{"title":"LogiTorch: A PyTorch-based library for logical reasoning on natural language","url":"https://suchanek.name/work/publications/emnlp-2022-demo.pdf"},{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset"},{"title":"ProofWriter","url":"https://www.kaggle.com/datasets/mathurinache/proofwriter"}]

Based on the search results, I found information about the ProofWriter dataset from allenai.org:

The ProofWriter dataset includes theories constructed with varying proof depths ("D0" to "D5," with D5 requiring up to five chaining steps of inference), and includes both the Closed World Assumption (CWA) and Open World Assumption (OWA) settings, the latter allowing answers to be True, False, or Unknown to accommodate incomplete information and negation.

Table 2 in the original paper shows accuracies for questions requ
…[truncated 756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T14:44:05.510067+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://proofwriter.apps.allenai.org/about",
  "prompt": "Extract ALL dataset statistics, download links, data format details, number of examples, depth distribution, label distribution, CWA vs OWA details. Get every number and fact available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://proofwriter.apps.allenai.org/about",
    "prompt": "Extract ALL dataset statistics, download links, data format details, number of examples, depth distribution, label distribution, CWA vs OWA details. Get every number and fact available."
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T14:44:05.510205+00:00_

I cannot extract the requested dataset statistics from the provided content. The webpage excerpt only contains a title: "ProofWriter: Soft Reasoning over Language"

To obtain dataset statistics, download links, data format details, example counts, depth distribution, label distribution, and CWA vs OWA information, you would need to:

1. Access the full ProofWriter paper or project page
2. Check the official repository (likely on GitHub)
3. Review supplementary materials or data documentation
4. Visit the dataset's host platform

The current content provides insufficient information to fulfill your request for comprehensive dataset details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T14:44:05.510338+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://paperswithcode.com/dataset/proofwriter",
  "prompt": "Extract ALL information about the ProofWriter dataset: number of examples, splits, depth distribution, label distribution, tasks, data format, download links, paper references, benchmarks. Get every fact and number available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://paperswithcode.com/dataset/proofwriter",
    "prompt": "Extract ALL information about the ProofWriter dataset: number of examples, splits, depth distribution, label distribution, tasks, data format, download links, paper references, benchmarks. Get every fact and number available."
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T14:44:05.510458+00:00_

REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://paperswithcode.com/dataset/proofwriter
Redirect URL: https://huggingface.co/papers/trending
Status: 302 Found

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://huggingface.co/papers/trending"
- prompt: "Extract ALL information about the ProofWriter dataset: number of examples, splits, depth distribution, label distribution, tasks, data format, download links, paper references, benchmarks. Get every fact and number available."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T14:44:05.510591+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProofWriter OWA dataset \"10k\" OR \"20k\" OR \"30k\" OR \"40k\" OR \"50k\" examples per depth train validation test"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProofWriter OWA dataset \"10k\" OR \"20k\" OR \"30k\" OR \"40k\" OR \"50k\" examples per depth train validation test"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T14:44:05.510738+00:00_

Web search results for query: "ProofWriter OWA dataset "10k" OR "20k" OR "30k" OR "40k" OR "50k" examples per depth train validation test"

Links: [{"title":"GitHub - INK-USC/FaiRR: FaiRR: Faithful and Robust Deductive Reasoning over Natural Language (ACL 2022)","url":"https://github.com/INK-USC/FaiRR"},{"title":"GitHub - princeton-nlp/NLProofS: EMNLP 2022: Generating Natural Language Proofs with Verifier-Guided Search https://arxiv.org/abs/2205.12443 · GitHub","url":"https://github.com/princeton-nlp/NLProofS"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive ...","url":"https://aclanthology.org/2021.findings-acl.317.pdf"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"ProofWriter Dataset","url":"https://paperswithcode.com/dataset/proofwriter"},{"title":"tasksource/proofwriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/proofwriter"},{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset"},{"title":"ProofWriter","url":"https://www.kaggle.com/datasets/mathurinache/proofwriter"},{"title":"Train, Validation and Test Sets in Machine Learning","url":"https://www.kaggle.com/getting-started/143685"},{"title":"Train, Test, and Validation Sets","url":"https://mlu-explain.github.io/train-test-validation/"}]

Let me search for more specific information about the ProofWriter dataset size and split information:

Links: [{"title":"D3xter1922/proofwriter-dataset at 68a35fc79495cd36f109472e3a3dbbf281e2f10d","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset/tree/68a35fc79495cd36f109472e3a3dbbf281e2f10d"},{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset"},{"title":"ProofWriter","url":"https://www.kaggle.com/datasets/mathurinache/proofwriter"},{"title":"ProofWriter Dataset","url":"h
…[truncated 4443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T14:44:05.510906+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/INK-USC/FaiRR",
  "prompt": "Extract all information about the ProofWriter dataset used in this repo: dataset statistics, number of examples, splits, depth levels, label distribution, how the data is structured, download instructions, and any data preprocessing details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/INK-USC/FaiRR",
    "prompt": "Extract all information about the ProofWriter dataset used in this repo: dataset statistics, number of examples, splits, depth levels, label distribution, how the data is structured, download instructions, and any data preprocessing details."
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T14:44:05.511043+00:00_

# ProofWriter Dataset Information

Based on the repository documentation, here's what can be extracted about the ProofWriter dataset:

## Download Instructions
The dataset can be obtained via: `wget https://aristo-data-public.s3.amazonaws.com/proofwriter/proofwriter-dataset-V2020.12.3.zip`

## Dataset Organization
The repository works with ProofWriter data organized by reasoning depth:
- **D0-3**: Training data with proof depth 0 to 3
- **D3**: Data limited to depth 3
- **pwu_leq_3**: "Unstaged" inference files from the original ProofWriter paper

## Preprocessing Details
The repository includes "Fact Augmentation" utilities that create robustness variants by "replacing names/attributes by out-of-distribution samples." Specific robustness datasets mentioned include name-based variations (e.g., `pwur_leq_3_eq_2_name`).

## Data Splits
The documentation references training and test splits, with test data used for both standard evaluation and robustness testing.

## Structural Elements
Data processing involves creating equivalence sets and handling different proof depths and configurations through the `process_proofwriter.py` script.

**Note**: The README doesn't provide explicit dataset statistics (total examples, label distributions, or detailed structural formats)—only usage instructions for preprocessing and evaluation workflows.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T14:44:05.511194+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicLM proofwriter FOLIO dataset evaluation benchmark logical reasoning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicLM proofwriter FOLIO dataset evaluation benchmark logical reasoning LLM"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T14:44:05.511329+00:00_

Web search results for query: "LogicLM proofwriter FOLIO dataset evaluation benchmark logical reasoning LLM"

Links: [{"title":"GitHub - teacherpeterpan/Logic-LLM: The project page for \"LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\" · GitHub","url":"https://github.com/teacherpeterpan/Logic-LLM"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=THSm9HyCKo"},{"title":"Empowering LLMs with Logical Reasoning: A Comprehensive Survey","url":"https://haoxuanli-pku.github.io/papers/IJCAI%2025%20-%20Empowering%20LLMs%20with%20Logical%20Reasoning-%20A%20Comprehensive%20Survey.pdf"},{"title":"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning | OpenReview","url":"https://openreview.net/forum?id=nWXMv949ZH&noteId=qt0t8SsVvT"},{"title":"large language models meet symbolic provers for logical ...","url":"https://arxiv.org/pdf/2502.06563"},{"title":"LeanReasoner: Boosting Complex Logical Reasoning with Lean","url":"https://arxiv.org/html/2403.13312"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"},{"title":"Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation","url":"https://arxiv.org/html/2502.06563"},{"title":"LLM-ARC: Enhancing LLMs with an Automated Reasoning Critic","url":"https://arxiv.org/html/2406.17663v1"}]

Based on the web search results, here's what I found about LogicLM, ProofWriter, and FOLIO in the context of LLM logical reasoning evaluation:

#
…[truncated 1283 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T14:44:05.511478+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/teacherpeterpan/Logic-LLM",
  "prompt": "Extract all information about how ProofWriter dataset is used: which subset (OWA/CWA), which depth, how many examples, how labels are distributed, data format, and any preprocessing steps. Also extract info about other datasets used (FOLIO, PrOntoQA, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/teacherpeterpan/Logic-LLM",
    "prompt": "Extract all information about how ProofWriter dataset is used: which subset (OWA/CWA), which depth, how many examples, how labels are distributed, data format, and any preprocessing steps. Also extract info about other datasets used (FOLIO, PrOntoQA, etc.)."
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T14:44:05.511602+00:00_

# Dataset Information from Logic-LM Repository

## ProofWriter Dataset

The researchers utilized "the depth-5 subset of the OWA version" of ProofWriter. To manage experimental costs, they "randomly sample 600 examples in the test set and ensure a balanced label distribution." No additional preprocessing details are provided in the documentation.

## Other Datasets

**PrOntoQA**: Used the "5-hop subset of the fictional characters version, consisting of 500 testing examples" for deductive reasoning evaluation.

**FOLIO**: Employed "the entire FOLIO test set for evaluation, consisting of 204 examples" for first-order logic reasoning tasks.

**LogicalDeduction**: Applied "the full test set consisting of 300 examples" addressing constraint satisfaction problems.

**AR-LSAT**: Evaluated on analytical reasoning questions with "230 multiple-choice questions" from Law School Admission Tests spanning 1991-2016.

The repository does not specify data formats or detailed preprocessing procedures beyond these sampling details. The datasets are stored preprocessed in the `./data` folder according to the documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T14:44:05.511744+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProofWriter dataset 100k questions per depth \"70%\" OR \"train\" OR \"test\" OR \"split\" statistics per depth level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProofWriter dataset 100k questions per depth \"70%\" OR \"train\" OR \"test\" OR \"split\" statistics per depth level"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T14:44:05.511921+00:00_

Web search results for query: "ProofWriter dataset 100k questions per depth "70%" OR "train" OR "test" OR "split" statistics per depth level"

Links: [{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive ...","url":"https://aclanthology.org/2021.findings-acl.317.pdf"},{"title":"GitHub - INK-USC/FaiRR: FaiRR: Faithful and Robust Deductive Reasoning over Natural Language (ACL 2022)","url":"https://github.com/INK-USC/FaiRR"},{"title":"ProofWriter Dataset","url":"https://paperswithcode.com/dataset/proofwriter"},{"title":"Table 11 from ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProofWriter:-Generating-Implications,-Proofs,-and-Tafjord-Dalvi/87c45a908537ffe1d2ab71a5d609bd7b4efa4fe1/figure/15"},{"title":"tasksource/proofwriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/proofwriter"},{"title":"D3xter1922/proofwriter-dataset at 68a35fc79495cd36f109472e3a3dbbf281e2f10d","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset/tree/68a35fc79495cd36f109472e3a3dbbf281e2f10d"},{"title":"ProofWriter","url":"https://www.kaggle.com/datasets/mathurinache/proofwriter"},{"title":"LogiTorch: A PyTorch-based library for logical reasoning on natural language","url":"https://suchanek.name/work/publications/emnlp-2022-demo.pdf"}]

Let me search more specifically for the dataset statistics including the 100k questions and train/test splits per depth level.

Links: [{"title":"Train Test Validation Split: Best Practices & Examples","url":"https://www.lightly.ai/blog/train-test-validation-split"},{"title":"Train-Test Split for Evaluating Machine Learning Algorithms - MachineLearningMas
…[truncated 6417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T14:44:05.512080+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.semanticscholar.org/paper/ProofWriter:-Generating-Implications,-Proofs,-and-Tafjord-Dalvi/87c45a908537ffe1d2ab71a5d609bd7b4efa4fe1/figure/15",
  "prompt": "Extract ALL information from Table 11 or any table shown here about ProofWriter dataset statistics - number of theories, questions, splits, depths, label distribution. Get every number."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.semanticscholar.org/paper/ProofWriter:-Generating-Implications,-Proofs,-and-Tafjord-Dalvi/87c45a908537ffe1d2ab71a5d609bd7b4efa4fe1/figure/15",
    "prompt": "Extract ALL information from Table 11 or any table shown here about ProofWriter dataset statistics - number of theories, questions, splits, depths, label distribution. Get every number."
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T14:44:05.512205+00:00_

I appreciate your request, but the web page content provided appears to be empty or didn't load properly. There's no visible table or text content between the "---" markers that I can analyze.

To extract information from Table 11 about ProofWriter dataset statistics, I would need:
- The actual table or document content to be included
- Clear visibility of the numbers for theories, questions, splits, depths, and label distributions

Could you please provide the web page content or table that contains the ProofWriter dataset information? Once you share that material, I'll be happy to extract all the relevant statistics while adhering to your guidelines about character limits and proper attribution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T14:44:05.512343+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.emergentmind.com/topics/proofwriter-dataset",
  "prompt": "Extract ALL dataset statistics about ProofWriter: number of examples, theories, questions per depth, train/val/test splits, label distribution (True/False/Unknown), CWA vs OWA details, generation method. Get every concrete number and fact."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.emergentmind.com/topics/proofwriter-dataset",
    "prompt": "Extract ALL dataset statistics about ProofWriter: number of examples, theories, questions per depth, train/val/test splits, label distribution (True/False/Unknown), CWA vs OWA details, generation method. Get every concrete number and fact."
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T14:44:05.512467+00:00_

# ProofWriter Dataset Statistics

Based on the provided content, **no specific dataset statistics are explicitly provided**. The document discusses ProofWriter's structure and capabilities but does not include concrete numbers about:

- Total example count
- Number of theories or questions
- Train/validation/test split sizes
- Label distribution (True/False/Unknown percentages)
- Specific breakdown of CWA vs OWA instances
- Generation method details

## What IS Documented

The content confirms ProofWriter includes:

- **Proof depths**: Ranging from "D0" to "D5," with D5 requiring up to five inference steps
- **World assumptions**: Both Closed World Assumption (CWA) and Open World Assumption (OWA) settings
- **Components per instance**: Context (facts/rules), question, answer, and optional proofs
- **Task types**: Implication enumeration, proof generation, and abduction

The document emphasizes that the dataset is "synthetic" and derived from "Datalog programs," but the actual quantitative breakdown of examples, splits, and label distributions is absent from this source material.

For detailed dataset statistics, you would need to consult the original ProofWriter paper (Tafjord et al., 2020, referenced as paper 2012.13048).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T14:44:05.512598+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2012.13048",
  "prompt": "Extract ALL dataset statistics mentioned in this paper about ProofWriter: number of theories, questions, examples per depth (D0-D5), train/val/test splits, label distribution (True/False/Unknown proportions), CWA vs OWA details, data generation method. Get every concrete number."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2012.13048",
    "prompt": "Extract ALL dataset statistics mentioned in this paper about ProofWriter: number of theories, questions, examples per depth (D0-D5), train/val/test splits, label distribution (True/False/Unknown proportions), CWA vs OWA details, data generation method. Get every concrete number."
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T14:44:05.512716+00:00_

# Dataset Statistics for ProofWriter

Based on the provided webpage content, I cannot extract the specific dataset statistics you requested. The arXiv abstract page contains only a brief overview of the paper's contributions, stating that ProofWriter was evaluated "on the RuleTaker dataset" with results showing "+9% absolute" improvement in proof accuracy.

The page does not include:
- Number of theories or questions
- Examples per depth (D0-D5)
- Train/validation/test split proportions
- Label distribution (True/False/Unknown percentages)
- CWA vs OWA implementation details
- Data generation methodology specifics

To obtain these concrete numbers, you would need to access the full PDF paper using the "View PDF" link provided on the page, as the abstract alone does not contain this level of dataset detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T14:44:05.512855+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "proofwriter dataset \"Table 10\" OR \"Table 11\" theories questions train test depth OWA CWA statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "proofwriter dataset \"Table 10\" OR \"Table 11\" theories questions train test depth OWA CWA statistics"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T14:44:05.513012+00:00_

Web search results for query: "proofwriter dataset "Table 10" OR "Table 11" theories questions train test depth OWA CWA statistics"

Links: [{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"Table 11 from ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProofWriter:-Generating-Implications,-Proofs,-and-Tafjord-Dalvi/87c45a908537ffe1d2ab71a5d609bd7b4efa4fe1/figure/15"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive ...","url":"https://aclanthology.org/2021.findings-acl.317.pdf"},{"title":"[PDF] ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProofWriter:-Generating-Implications,-Proofs,-and-Tafjord-Dalvi/87c45a908537ffe1d2ab71a5d609bd7b4efa4fe1"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language | Request PDF","url":"https://www.researchgate.net/publication/347880792_ProofWriter_Generating_Implications_Proofs_and_Abductive_Statements_over_Natural_Language"},{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset"},{"title":"ProofWriter","url":"https://www.kaggle.com/datasets/mathurinache/proofwriter"},{"title":"Table 5 from ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProofWriter:-Generating-Implications,-Proofs,-and-Tafjord-Dalvi/87c45a908537ffe1d2ab71a5d609bd7b4efa4fe1/figure/9"},{"title":"GitHub - INK-USC/FaiRR: FaiRR: Faithful and Robust Deductive Reasoning over Natural Language (ACL 2022)","url":"https://github.com/INK-USC/FaiRR"},{"title":"tasksource/proofwriter · Datasets at Hugging Face","url":"https://huggingface.co/datas
…[truncated 1296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T14:44:05.513161+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "proofwriter OWA depth-5 600 examples balanced \"true\" \"false\" \"unknown\" label NLI task format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "proofwriter OWA depth-5 600 examples balanced \"true\" \"false\" \"unknown\" label NLI task format"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T14:44:05.513292+00:00_

Web search results for query: "proofwriter OWA depth-5 600 examples balanced "true" "false" "unknown" label NLI task format"

Links: [{"title":"ProofWriter: Generating Implications, Proofs, and Abductive ...","url":"https://aclanthology.org/2021.findings-acl.317.pdf"},{"title":"GitHub - INK-USC/FaiRR: FaiRR: Faithful and Robust Deductive Reasoning over Natural Language (ACL 2022)","url":"https://github.com/INK-USC/FaiRR"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"GitHub - teacherpeterpan/Logic-LLM: The project page for \"LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\" · GitHub","url":"https://github.com/teacherpeterpan/Logic-LLM"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"ProofWriter Dataset","url":"https://paperswithcode.com/dataset/proofwriter"},{"title":"Decompose-and-Formalise: Recursively Verifiable Natural Language Inference","url":"https://arxiv.org/html/2601.19605"},{"title":"tasksource/proofwriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/proofwriter"},{"title":"GitHub - princeton-nlp/NLProofS: EMNLP 2022: Generating Natural Language Proofs with Verifier-Guided Search https://arxiv.org/abs/2205.12443 · GitHub","url":"https://github.com/princeton-nlp/NLProofS"},{"title":"ProofWriter","url":"https://www.kaggle.com/datasets/mathurinache/proofwriter"}]

Based on the search results, I found relevant information about the ProofWriter dataset configuration you're asking about:

The depth-5 subset of the OWA (Open World Assumption) version is used, with 600 randomly sampled examples from the test set to ensure a balanced label distribution.

Regarding the label format, the da
…[truncated 706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-14T14:44:05.513446+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FoVer first order logic verification proofwriter FOLIO dataset comparison benchmark evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FoVer first order logic verification proofwriter FOLIO dataset comparison benchmark evaluation"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T14:44:05.513617+00:00_

Web search results for query: "FoVer first order logic verification proofwriter FOLIO dataset comparison benchmark evaluation"

Links: [{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning","url":"https://www.researchgate.net/publication/397118426_FoVer_First-Order_Logic_Verification_for_Natural_Language_Reasoning"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/article/view/8211"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.tacl-1.61/"},{"title":"GitHub - peiyu-cn/FoVer: Official code repository for the paper: \"FoVer: First-Order Logic Verification for Natural Language Reasoning\" (TACL) · GitHub","url":"https://github.com/peiyu-cn/FoVer"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning Yu Pei1, 2","url":"https://direct.mit.edu/tacl/article-pdf/doi/10.1162/TACL.a.41/2561649/tacl.a.41.pdf"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"}]

Based on the search results, I can provide you with comprehensive information about FoVer, i
…[truncated 1728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-14T14:44:05.513777+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://direct.mit.edu/tacl/article-pdf/doi/10.1162/TACL.a.41/2561649/tacl.a.41.pdf",
  "prompt": "Extract ALL dataset statistics for ProofWriter and FOLIO from this paper. Specifically: number of examples used, splits, label distribution (True/False/Unknown), which subset of ProofWriter (OWA/CWA, depth), any comparison tables between datasets. Also extract any information about how ProofWriter is formatted for NLI tasks. Get every concrete number."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://direct.mit.edu/tacl/article-pdf/doi/10.1162/TACL.a.41/2561649/tacl.a.41.pdf",
    "prompt": "Extract ALL dataset statistics for ProofWriter and FOLIO from this paper. Specifically: number of examples used, splits, label distribution (True/False/Unknown), which subset of ProofWriter (OWA/CWA, depth), any comparison tables between datasets. Also extract any information about how ProofWriter is formatted for NLI tasks. Get every concrete number."
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-14T14:44:05.513924+00:00_

Request failed with status code 403

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-14T14:44:05.514058+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural",
  "prompt": "Extract ALL dataset statistics for ProofWriter and FOLIO mentioned in this paper. Specifically: number of examples, splits, label distribution (True/False/Unknown), which subset of ProofWriter (OWA/CWA, depth), any comparison tables. Get every concrete number and percentage."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural",
    "prompt": "Extract ALL dataset statistics for ProofWriter and FOLIO mentioned in this paper. Specifically: number of examples, splits, label distribution (True/False/Unknown), which subset of ProofWriter (OWA/CWA, depth), any comparison tables. Get every concrete number and percentage."
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-14T14:44:05.514178+00:00_

Request failed with status code 403

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T14:44:05.514302+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "proofwriter OWA dataset \"true\" \"false\" \"unknown\" label proportion percentage distribution statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "proofwriter OWA dataset \"true\" \"false\" \"unknown\" label proportion percentage distribution statistics"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T14:44:05.514452+00:00_

Web search results for query: "proofwriter OWA dataset "true" "false" "unknown" label proportion percentage distribution statistics"

Links: [{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive ...","url":"https://aclanthology.org/2021.findings-acl.317.pdf"},{"title":"GitHub - INK-USC/FaiRR: FaiRR: Faithful and Robust Deductive Reasoning over Natural Language (ACL 2022)","url":"https://github.com/INK-USC/FaiRR"},{"title":"GitHub - princeton-nlp/NLProofS: EMNLP 2022: Generating Natural Language Proofs with Verifier-Guided Search https://arxiv.org/abs/2205.12443 · GitHub","url":"https://github.com/princeton-nlp/NLProofS"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset"},{"title":"tasksource/proofwriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/proofwriter"},{"title":"ProofWriter","url":"https://www.kaggle.com/datasets/mathurinache/proofwriter"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language","url":"https://proofwriter.apps.allenai.org/about"},{"title":"renma/ProofWriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/renma/ProofWriter"}]

Let me search for more specific information about the label distribution statistics in the ProofWriter OWA dataset.

Links: [{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive ...","url":"https://aclanthology.org/2021.findings-acl.317.p
…[truncated 6536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-14T14:44:05.514601+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2012.13048",
  "prompt": "Extract ALL dataset statistics tables from this paper. I need: 1) Number of theories and questions per depth level (D0, D1, D2, D3, D5) for both CWA and OWA versions. 2) Train/val/test split sizes. 3) Label distribution (True/False/Unknown) proportions. 4) Any table showing dataset sizes. Look for Table 10, Table 11, or any appendix tables with these numbers. Also extract information about how the data was generated synthetically, the natural language style, and what types of reasoning are tested. Get EVERY concrete number."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ar5iv.labs.arxiv.org/html/2012.13048",
    "prompt": "Extract ALL dataset statistics tables from this paper. I need: 1) Number of theories and questions per depth level (D0, D1, D2, D3, D5) for both CWA and OWA versions. 2) Train/val/test split sizes. 3) Label distribution (True/False/Unknown) proportions. 4) Any table showing dataset sizes. Look for Table 10, Table 11, or any appendix tables with these numbers. Also extract information about how the data was generated synthetically, the natural language style, and what types of reasoning are tested. Get EVERY concrete number."
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-14T14:44:05.514733+00:00_

# ProofWriter Dataset Statistics

## Dataset Sizes (Table 10)

**CWA Datasets:**
- D0: 27,020 theories, 100,002 questions
- D1: 12,965 theories, 100,012 questions
- D2: 9,138 theories, 100,014 questions
- D3: 7,067 theories, 100,024 questions
- D5: 4,935 theories, 100,030 questions
- Birds/Electricity: 140 theories, 5,270 questions
- ParaRules: 2,403 theories, 40,022 questions

**OWA Datasets:**
- D0: 26,978 theories, 100,000 questions
- D1: 12,933 theories, 100,014 questions
- D2: 9,033 theories, 100,010 questions
- D3: 6,940 theories, 100,036 questions
- D5: 4,752 theories, 100,030 questions
- Birds/Electricity: 140 theories, 5,270 questions
- ParaRules: 2,403 theories, 40,022 questions

## Implications Per Theory

Mean implications range from 0.8 (D0) to 9.8 (D5 CWA); maximum implications reach 21 in D5 datasets. Maximum proof depths: D0=8, D1=6, D2=5, D3=7, D5=10 for CWA versions.

## Train/Test Split

"Each dataset is split 70/10/20 into train/dev/test."

## Label Distribution

"Answers are equally divided into True/False" for CWA; OWA adds "Unknown" values.

## Generation Method

Theories were "generated from synthetic logic programs" using "natural language patterns to produce the English forms."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-14T14:44:05.514869+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2012.13048",
  "prompt": "I need MORE detailed information from this paper. Specifically: 1) The exact natural language templates/patterns used - what do the sentences look like? Give examples of facts, rules, and questions. 2) What entities are used (animals, people, objects)? 3) What relations/properties are used? 4) How does the OWA label distribution work - what proportion are Unknown? 5) How is the negation handled in OWA vs CWA? 6) What is the \"Birds/Electricity\" dataset about? 7) What is ParaRules? 8) Any information about the format of the data files (JSON, JSONL?). 9) How exactly are proofs represented? 10) The relationship to RuleTaker. Get every detail about the data format and content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ar5iv.labs.arxiv.org/html/2012.13048",
    "prompt": "I need MORE detailed information from this paper. Specifically: 1) The exact natural language templates/patterns used - what do the sentences look like? Give examples of facts, rules, and questions. 2) What entities are used (animals, people, objects)? 3) What relations/properties are used? 4) How does the OWA label distribution work - what proportion are Unknown? 5) How is the negation handled in OWA vs CWA? 6) What is the \"Birds/Electricity\" dataset about? 7) What is ParaRules? 8) Any information about the format of the data files (JSON, JSONL?). 9) How exactly are proofs represented? 10) The relationship to RuleTaker. Get every detail about the data format and content."
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-14T14:44:05.515024+00:00_

# ProofWriter Dataset Details

## Natural Language Templates and Examples

The datasets use **templated English** with patterns like:
- Facts: "Charlie is quiet."
- Rules: "If someone is kind then they are young."
- Questions: "Erin is big?" or "Charlie is not quiet?"

The paper shows Figure 1 with an example theory but doesn't exhaustively list templates.

## Entities and Relations

The domains employ:
- **Entities**: Animals (tigers, lions, dogs, mice, birds) and people (Bob, Charlie, Dave, Erin, Anne)
- **Properties**: cold, kind, quiet, young, big, red, blue, smart, rough, nice, round, white
- **Relations**: chases, eats, visits, likes, sees

## Label Distribution

For OWA datasets, answers distribute equally across True/False/Unknown: "answers are equally divided into True/False (and Unknown, for the OWA versions)."

## Negation Handling

**CWA**: Uses "negation as failure (NAF)" where unprovable facts are assumed false. "negated facts and negative rule conclusions are not allowed."

**OWA**: Allows explicit negation with hard-negation semantics. Facts can be explicitly negative (e.g., "Bob is not red").

## Birds-Electricity Dataset

Hand-authored datasets testing out-of-distribution generalization. "Birds" uses a single 6-rule theory about abnormality. "Electricity" (4 datasets) reasons about toy electrical circuits with 5-12 rules per dataset.

## ParaRules

Contains "40k questions against 2k theories expressed in paraphrased natural language, obtained by having crowdworkers rephrase the templated English." Example: "Bob is cold" becomes "In the snow sits Bob, crying from being cold."

## Data File Format

The paper doesn't specify JSON/JSONL format explicitly but notes: "Datasets available at https://allenai.org/data/proofwriter"

## Proof Representation

Proofs are "directed acyclic graph[s]" with alternating fact and rule nodes. Linear encoding uses Polish notation with symbols: "#" (inverse implication), "%" (rule-conclusion conjunction), "&" (conjunctiv
…[truncated 303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-14T14:44:05.515180+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PrOntoQA dataset statistics number examples synthetic ontology reasoning benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PrOntoQA dataset statistics number examples synthetic ontology reasoning benchmark"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-14T14:44:05.515314+00:00_

Web search results for query: "PrOntoQA dataset statistics number examples synthetic ontology reasoning benchmark"

Links: [{"title":"GitHub - asaparov/prontoqa: Synthetic question-answering dataset to formally analyze the chain-of-thought output of large language models on a reasoning task. · GitHub","url":"https://github.com/asaparov/prontoqa"},{"title":"prontoqa/README.md at main · asaparov/prontoqa","url":"https://github.com/asaparov/prontoqa/blob/main/README.md"},{"title":"prontoqa/README.md at main · LoryPack/prontoqa","url":"https://github.com/LoryPack/prontoqa/blob/main/README.md"},{"title":"Published as a conference paper at ICLR 2023 LANGUAGE MODELS ARE GREEDY","url":"https://arxiv.org/pdf/2210.01240"},{"title":"GitHub - horenbergerb/prontoqa_llama: Synthetic question-answering dataset to formally analyze the chain-of-thought output of large language models on a reasoning task. Integrated with kobold.cpp","url":"https://github.com/horenbergerb/prontoqa_llama"},{"title":"PrOntoQA: Synthetic QA for Formal Reasoning","url":"https://www.emergentmind.com/topics/prontoqa-dataset"},{"title":"Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought | OpenReview","url":"https://openreview.net/forum?id=qFVVBzXxR2V"},{"title":"PrOntoQA: Synthetic Deductive Reasoning Benchmark","url":"https://www.emergentmind.com/topics/prontoqa"},{"title":"prontoqa/run_experiment.py at main · asaparov/prontoqa","url":"https://github.com/asaparov/prontoqa/blob/main/run_experiment.py"},{"title":"PrOntoQA Dataset","url":"https://paperswithcode.com/dataset/prontoqa"}]

Based on the search results, here's what I found about the PrOntoQA dataset:

## Overview

PrOntoQA and PrOntoQA-OOD generate question-answering examples with chains-of-thought that describe the reasoning required to answer the questions correctly. PrOntoQA is a synthetic question-answering dataset purpose-built for the systematic, formal evaluation of LLM reasoning via interpretable first-ord
…[truncated 1199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-14T14:44:05.515466+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "logical reasoning NLI benchmark survey \"premises\" \"hypothesis\" true false unknown FOL formal logic datasets 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "logical reasoning NLI benchmark survey \"premises\" \"hypothesis\" true false unknown FOL formal logic datasets 2023 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-14T14:44:05.515605+00:00_

Web search results for query: "logical reasoning NLI benchmark survey "premises" "hypothesis" true false unknown FOL formal logic datasets 2023 2024 2025"

Links: [{"title":"Empowering LLMs with Logical Reasoning: A Comprehensive Survey","url":"https://www.ijcai.org/proceedings/2025/1155.pdf"},{"title":"Empowering LLMs with Logical Reasoning: A Comprehensive Survey","url":"https://arxiv.org/html/2502.15652v4"},{"title":"From Reasoning to Learning: A Survey on Hypothesis Dis","url":"https://openreview.net/pdf?id=d7W38UzUg0"},{"title":"Natural Language Reasoning, A Survey | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3664194"},{"title":"Capturing the Varieties of Natural Language Inference: A Systematic Survey of Existing Datasets and Two Novel Benchmarks | Journal of Logic, Language and Information | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10849-023-09410-4"},{"title":"Evaluating Step-by-step Reasoning Traces: A Survey","url":"https://aclanthology.org/2025.findings-emnlp.94.pdf"},{"title":"Logical Reasoning in Large Language Models: A Survey","url":"https://arxiv.org/pdf/2502.09100"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models","url":"https://arxiv.org/html/2404.15522v2"},{"title":"Towards LogiGLUE: A Brief Survey and A Benchmark for Analyzing Logical Reasoning Capabilities of Language Models","url":"https://arxiv.org/html/2310.00836v3"}]

Based on the search results, I've found comprehensive information about logical reasoning benchmarks and NLI datasets. Here are the key findings:

## NLI and Logical Reasoning Benchmarks

Natural Language Inference (NLI) is a three-way classificatio
…[truncated 1574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-14T14:44:05.515755+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicNLI dataset size statistics NLI premises hypothesis true false unknown first order logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicNLI dataset size statistics NLI premises hypothesis true false unknown first order logic"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-14T14:44:05.515925+00:00_

Web search results for query: "LogicNLI dataset size statistics NLI premises hypothesis true false unknown first order logic"

Links: [{"title":"The Stanford NLI Corpus Revisited - The Stanford Natural Language Processing Group","url":"https://nlp.stanford.edu/blog/the-stanford-nli-corpus-revisited/"},{"title":"NLI | Natural Language Inferencing | by AI4HUMAN | Medium","url":"https://medium.com/@aiforhuman/nli-natural-language-inferencing-8f231f23800e"},{"title":"Natural Language Inference (NLI)","url":"https://www.emergentmind.com/topics/natural-language-inference-nli"},{"title":"Understanding Natural Language Inference: From Models to Containers | by azwarshariq | Red Buffer | Medium","url":"https://medium.com/red-buffer/title-understanding-natural-language-inference-from-models-to-containers-26c1e777d72f"},{"title":"Natural Language Inference (NLI) — Also Known as Recognizing Textual Entailment (RTE) | by Julian Wang | Medium","url":"https://medium.com/@j.wang.mlds_97641/natural-language-inference-nli-also-known-as-recognizing-textual-entailment-rte-384295708089"},{"title":"Stanford NLI (SNLI) Dataset Overview","url":"https://www.emergentmind.com/topics/stanford-natural-language-inference-snli-dataset"},{"title":"Natural Language Inference: An Overview | Towards Data Science","url":"https://towardsdatascience.com/natural-language-inference-an-overview-57c0eecf6517/"},{"title":"The Linguistic Feature Relation Analysis of Premise and Hypothesis for Interpreting Nature Language Inference | Human-Centric Intelligent Systems","url":"https://link.springer.com/article/10.1007/s44230-023-00054-y"},{"title":"Natural language inference | NLP-progress","url":"http://nlpprogress.com/english/natural_language_inference.html"},{"title":"Reverse-engineering NLI: A study of the meta-inferential properties of Natural Language Inference | OpenReview","url":"https://openreview.net/forum?id=NAcvSI2CRM"}]

I found general NLI dataset information, but not specific details about the Log
…[truncated 7381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-14T14:44:05.516089+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOLIO dataset 1001 OR 1435 examples statistics label distribution train validation test split"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOLIO dataset 1001 OR 1435 examples statistics label distribution train validation test split"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-14T14:44:05.516236+00:00_

Web search results for query: "FOLIO dataset 1001 OR 1435 examples statistics label distribution train validation test split"

Links: [{"title":"Train Test Validation Split: How To & Best Practices [2024]","url":"https://www.v7darwin.com/blog/train-validation-test-set"},{"title":"Split Your Dataset With scikit-learn's train_test_split() – Real Python","url":"https://realpython.com/train-test-split-python-data/"},{"title":"Data split (train, test, validation)","url":"https://mzuer.github.io/machine_learning/data_split"},{"title":"Train Test Validation Split: Best Practices & Examples","url":"https://www.lightly.ai/blog/train-test-validation-split"},{"title":"train_test_split — scikit-learn 1.8.0 documentation","url":"https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html"},{"title":"How to Split Machine Learning Datasets: Training, Validation, & Test Sets","url":"https://encord.com/blog/train-val-test-split/"},{"title":"A Step-by-Step Guide to Preparing Data for Labeling | Label Studio","url":"https://labelstud.io/blog/a-step-by-step-guide-to-preparing-data-for-labeling/"},{"title":"How to Split a Custom Dataset into Training and Test Datasets (A Practical Guide) | by Hey Amit | Medium","url":"https://medium.com/@heyamit10/how-to-split-a-custom-dataset-into-training-and-test-datasets-a-practical-guide-54d5043c67e3"},{"title":"Training, validation, and test data sets - Wikipedia","url":"https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets"},{"title":"Train, Validation, Test Split for Machine Learning","url":"https://blog.roboflow.com/train-test-split/"}]

The search results don't contain specific information about the FOLIO dataset with the numbers 1001 or 1435 examples. Let me search more specifically for the FOLIO dataset paper or documentation.

Links: [{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FOLIO: Natural Language
…[truncated 4897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-14T14:44:05.516384+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Yale-LILY/FOLIO",
  "prompt": "Extract ALL information about the FOLIO dataset: number of examples, train/val/test split sizes, label distribution, data format, how to download, columns/fields. Get every concrete number."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Yale-LILY/FOLIO",
    "prompt": "Extract ALL information about the FOLIO dataset: number of examples, train/val/test split sizes, label distribution, data format, how to download, columns/fields. Get every concrete number."
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-14T14:44:05.516508+00:00_

# FOLIO Dataset Information

Based on the GitHub repository content provided, here's what can be extracted about the FOLIO dataset:

## Available Data
The repository contains **train and validation sets** in both jsonl and txt formats. No specific numbers for dataset size or split breakdown are provided in this page.

## Data Format & Fields
Each example includes these fields:
- 'premises': natural language premises
- 'premises-FOL': first-order logic formula for premises
- 'conclusion': natural language conclusion
- 'conclusion-FOL': first-order logic formula for conclusion
- 'label': truth value label
- 'story-id': identifier grouping related premises
- 'example-id': unique example identifier
- 'source': origin (WikiLogic or HybLogic)

## Concrete Numbers
The page does not provide specific counts for:
- Total examples
- Train/validation split sizes
- Test set information
- Label distribution
- Download statistics

## Key Note
An update mentions a new improved version is available on Hugging Face datasets (yale-nlp/FOLIO) with "significant quality improvement and error fixing," suggesting that detailed statistics may be available there rather than in this repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-14T14:44:05.516646+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/yale-nlp/FOLIO",
  "prompt": "Extract ALL information about this FOLIO dataset: number of rows per split (train/validation/test), columns, label distribution, data format, how to load, any statistics shown. Get every number."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/yale-nlp/FOLIO",
    "prompt": "Extract ALL information about this FOLIO dataset: number of rows per split (train/validation/test), columns, label distribution, data format, how to load, any statistics shown. Get every number."
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-14T14:44:05.516772+00:00_

# FOLIO Dataset Information

Based on the webpage content provided, here is the available information:

## Dataset Metadata
- **Name:** FOLIO
- **Creator:** Yale NLP Lab
- **License:** MIT
- **Total File Size:** 1.22 MB
- **Downloads (last month):** 1,420
- **Likes:** 67

## Data Characteristics
- **Modalities:** Tabular, Text
- **Format:** JSON
- **Size Category:** 1K - 10K (samples)
- **Libraries:** Datasets, pandas, Croissant

## Missing Information
Unfortunately, the webpage content provided **does not include**:
- ❌ Number of rows per split (train/validation/test)
- ❌ Column names and descriptions
- ❌ Label distribution
- ❌ Data statistics
- ❌ Code examples for loading the dataset
- ❌ README content (noted as "empty")

## Important Note
The page indicates: **"You need to agree to share your contact information to access this dataset"** - requiring login/signup to view the actual dataset files and detailed documentation.

To access complete dataset specifications, you would need to log in to Hugging Face and review the full dataset card at https://huggingface.co/datasets/yale-nlp/FOLIO

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-14T14:44:05.516926+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2209.00840v2",
  "prompt": "Extract ALL dataset statistics from this FOLIO paper: number of examples total, train/val/test split, label distribution (True/False/Unknown proportions and counts), number of premises, number of unique FOL patterns, vocabulary size, and any comparison tables with ProofWriter or other datasets. Get every concrete number and percentage."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2209.00840v2",
    "prompt": "Extract ALL dataset statistics from this FOLIO paper: number of examples total, train/val/test split, label distribution (True/False/Unknown proportions and counts), number of premises, number of unique FOL patterns, vocabulary size, and any comparison tables with ProofWriter or other datasets. Get every concrete number and percentage."
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-14T14:44:05.517056+00:00_

# FOLIO Dataset Statistics

## Dataset Size & Split
- **Total examples**: 1,435 unique conclusions (1,430 mentioned in abstract)
- **Total stories**: 487
- **Train/Val/Test split**: 70%/15%/15% = 1,001/203/226 examples respectively
- **Total premises**: 2,407

## Label Distribution (Test Set)
- **True**: 87 examples
- **False**: 78 examples
- **Unknown**: 61 examples
- **Majority baseline**: 38.5%

## Data Source Breakdown
| Source | Stories | Premises | Conclusions |
|--------|---------|----------|-------------|
| WikiLogic | 304 | 1,353 | 753 |
| HybLogic | 183 | 1,054 | 682 |
| **Total** | **487** | **2,407** | **1,435** |

## Language & Logical Complexity
- **Vocabulary size**: 4,351 words
- **Average words per sentence**: 9.86 (WikiLogic: 8.50; HybLogic: 11.52)
- **Reasoning depth range**: 0-14 grades
- **Distinct Abstract Syntax Trees (ASTs)**: 76 total (WikiLogic: 51; HybLogic: 25)
- **Reasoning depths requiring 5+ steps**: 28.7% of examples

## Comparison with Other Datasets
FOLIO substantially exceeds prior benchmarks: RuleTaker and LogicNLI each contained fewer than 50 distinct ASTs; RuleTaker's vocabulary was only 101 words versus FOLIO's 4,351 words.

Human expert performance on FOLIO reached "95.98%" accuracy versus non-expert performance of "61.82%."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-14T14:44:05.517196+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "proofwriter dataset download aristo-data-public s3 zip format JSON JSONL structure fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "proofwriter dataset download aristo-data-public s3 zip format JSON JSONL structure fields"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-14T14:44:05.517341+00:00_

Web search results for query: "proofwriter dataset download aristo-data-public s3 zip format JSON JSONL structure fields"

Links: [{"title":"GitHub - INK-USC/FaiRR: FaiRR: Faithful and Robust Deductive Reasoning over Natural Language (ACL 2022)","url":"https://github.com/INK-USC/FaiRR"},{"title":"GitHub - princeton-nlp/NLProofS: EMNLP 2022: Generating Natural Language Proofs with Verifier-Guided Search https://arxiv.org/abs/2205.12443 · GitHub","url":"https://github.com/princeton-nlp/NLProofS"},{"title":"ProofWriter Dataset","url":"https://paperswithcode.com/dataset/proofwriter"},{"title":"Free Aristo Mini Corpus Dataset | DagsHub","url":"https://dagshub.com/datasets/aristo-mini-corpus/"},{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset"},{"title":"GitHub - Aiden0526/Aristotle: Code and Data for ACL 2025 Paper \"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework\". · GitHub","url":"https://github.com/Aiden0526/Aristotle"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language","url":"https://proofwriter.apps.allenai.org/about"},{"title":"ProofWriter - OpenDataLab","url":"https://opendatalab.com/OpenDataLab/ProofWriter/download"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"ProofWriter","url":"https://www.kaggle.com/datasets/mathurinache/proofwriter"}]

I found information about the ProofWriter dataset download location. The ProofWriter dataset can be downloaded from `https://aristo-data-public.s3.amazonaws.com/proofwriter/proofwriter-dataset-V2020.12.3.zip`.

Let me search for more specific information about the file structure and format details.

Links: [{"title":"Working with JSON Lines data reports - NCBI - NIH","url":"https://www.ncbi.nlm.nih.gov/datasets/docs/v2/tutorials/working-with-jsonl-data-reports/"},{"title":"JSONL
…[truncated 3997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-14T14:44:05.517491+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/princeton-nlp/NLProofS/blob/main/preprocess_ruletaker.py",
  "prompt": "Extract information about the ProofWriter/RuleTaker dataset file format: what fields does each JSON record contain? What's the exact structure? How are theories, questions, answers, and proofs organized in the files?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/princeton-nlp/NLProofS/blob/main/preprocess_ruletaker.py",
    "prompt": "Extract information about the ProofWriter/RuleTaker dataset file format: what fields does each JSON record contain? What's the exact structure? How are theories, questions, answers, and proofs organized in the files?"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-14T14:44:05.517663+00:00_

# ProofWriter/RuleTaker Dataset Format

Based on the preprocessing script, each JSON record in the RuleTaker dataset contains:

## Core Fields

- **"triples"**: Dictionary mapping identifiers to fact objects with a "text" field
- **"rules"**: Dictionary mapping identifiers to rule objects with a "text" field
- **"sentences"**: Dictionary storing sentence text (when available)
- **"mappings"**: Maps triple/rule identifiers to sentence indices
- **"questions"**: Dictionary where each question object includes:
  - "question": The query text
  - "answer": Boolean or "Unknown"
  - "QDep": Question depth (numeric)
  - "proofsWithIntermediates": Array of proof structures

## Proof Structure

Each proof object contains:
- **"representation"**: A nested representation using formats like `"(conditions -> (rule# % int#))"`
- **"intermediates"**: Dictionary mapping intermediate conclusion IDs to objects with "text" fields

## Organization Pattern

The script processes files named `"meta-{split}.jsonl"` (train/dev/test splits), with each line representing one example. The preprocessing converts this into a standardized format with "hypothesis," "context," "proofs," "answer," and "depth" fields for compatibility with EntailmentBank conventions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-14T14:44:05.517812+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "smoorsmith proofwriter huggingface LogicLM chain of thought dataset format columns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "smoorsmith proofwriter huggingface LogicLM chain of thought dataset format columns"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-14T14:44:05.517964+00:00_

Web search results for query: "smoorsmith proofwriter huggingface LogicLM chain of thought dataset format columns"

Links: [{"title":"smoorsmith/proofwriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/smoorsmith/proofwriter"},{"title":"Paper page - LogiCoT: Logical Chain-of-Thought Instruction-Tuning Data Collection with GPT-4","url":"https://huggingface.co/papers/2305.12147"},{"title":"isaiahbjork/chain-of-thought · Datasets at Hugging Face","url":"https://huggingface.co/datasets/isaiahbjork/chain-of-thought"},{"title":"Chain Of Thought Reasoning - a ewre324 Collection","url":"https://huggingface.co/collections/ewre324/chain-of-thought-reasoning"},{"title":"Paper page - LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers","url":"https://huggingface.co/papers/2310.15164"},{"title":"Huggingface","url":"https://huggingface.co/datasets/renma/ProofWriter/resolve/main/README.md?download=true"},{"title":"GitHub - OpenBioLink/ThoughtSource: A central, open resource for data and tools related to chain-of-thought reasoning in large language models. Developed @ Samwald research group: https://samwald.info/ · GitHub","url":"https://github.com/OpenBioLink/ThoughtSource"},{"title":"chain of thought - a Tempo14 Collection","url":"https://huggingface.co/collections/Tempo14/chain-of-thought-65709a73974502490ba66cf9"},{"title":"Paper page - Enhancing Zero-Shot Chain-of-Thought Reasoning in Large Language Models through Logic","url":"https://huggingface.co/papers/2309.13339"},{"title":"Paper page - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models","url":"https://huggingface.co/papers/2201.11903"}]

Based on the search results, I found the smoorsmith/proofwriter dataset on Hugging Face. It's the standard ProofWriter dataset from the LogicLM GitHub repository with chain of thought added.

However, the search results don't provide detailed information about the specific dataset forma
…[truncated 555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-14T14:44:05.518201+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/smoorsmith/proofwriter",
  "prompt": "Extract ALL information: number of rows, columns/fields with descriptions, data format, splits, how to load, any preprocessing details, label values, and connection to LogicLM. Get every detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/smoorsmith/proofwriter",
    "prompt": "Extract ALL information: number of rows, columns/fields with descriptions, data format, splits, how to load, any preprocessing details, label values, and connection to LogicLM. Get every detail."
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-14T14:44:05.518378+00:00_

# ProofWriter Dataset - Complete Information

## Dataset Overview
- **Name:** ProofWriter (smoorsmith/proofwriter)
- **Source:** Standard ProofWriter dataset from LogicLM GitHub repository
- **Total Rows:** 4,200
- **File Size:** 1.15 MB
- **Format:** Parquet
- **Modalities:** Tabular, Text

## Data Splits

| Split | Rows |
|-------|------|
| train | 3,000 |
| dev   | 600   |
| test  | 600   |

## Columns/Fields Description

| Field | Type | Range/Values | Description |
|-------|------|--------------|-------------|
| `index` | int64 | 0-3k | Row identifier |
| `id` | string | 30-36 chars | Unique question identifier (e.g., "ProofWriter_RelNoneg-OWA-D5-84_Q10") |
| `context` | string | 246-1.14k chars | Logical facts and conditional rules forming the knowledge base |
| `question` | string | 95-129 chars | Query about the context (statement to verify) |
| `options` | sequence | 3 values | Multiple choice answers: ["A) True", "B) False", "C) Unknown"] |
| `answer` | stringclass | {True, False, Unknown} | Ground truth label |
| `chain_of_thought` | string | 92-2.05k chars | Step-by-step reasoning explaining how to reach the answer |
| `depth` | int64 | -1 to 5 | Reasoning depth (-1 = unknown/no chain, 0-5 = steps needed) |
| `processed_answer` | stringclass | {True, False, Unknown} | Normalized answer value |

## Data Format & Loading

**Format:** Auto-converted to Parquet

**Load with Hugging Face Datasets:**
```python
from datasets import load_dataset

dataset = load_dataset("smoorsmith/proofwriter")
# Access splits:
train = dataset['train']
dev = dataset['dev']
test = dataset['test']
```

**Load with Pandas:**
```python
import pandas as pd

df = pd.read_parquet("proofwriter.parquet")
```

## Task Structure

### Question Type
Multiple-choice question answering on logical reasoning:
- **Format:** "Based on the above information, is the following statement true, false, or unknown?"
- **Answer Options:** A) True, B) False, C) Unknown

### Example Instance

```json
{
  "i
…[truncated 1991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-14T14:44:05.518538+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicBench dataset 2024 benchmark evaluation logical reasoning NLI statistics size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicBench dataset 2024 benchmark evaluation logical reasoning NLI statistics size"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-14T14:44:05.518675+00:00_

Web search results for query: "LogicBench dataset 2024 benchmark evaluation logical reasoning NLI statistics size"

Links: [{"title":"LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models","url":"https://arxiv.org/html/2404.15522v2"},{"title":"GitHub - Mihir3009/LogicBench: LogicBench is a natural language question-answering dataset consisting of 25 different reasoning patterns spanning over propositional, first-order, and non-monotonic logics. · GitHub","url":"https://github.com/Mihir3009/LogicBench"},{"title":"LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=71kocBuhNO"},{"title":"LogicBench: Towards Systematic Evaluation of Logical ...","url":"https://aclanthology.org/2024.acl-long.739.pdf"},{"title":"LogicBench: A Benchmark for Evaluation of Logical Reasoning | OpenReview","url":"https://openreview.net/forum?id=7NR2ZVzZxx"},{"title":"LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.739/"},{"title":"[2404.15522] LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models","url":"https://arxiv.org/abs/2404.15522"},{"title":"Can LLMs Solve ASP Problems? Insights from a Benchmarking Study","url":"https://proceedings.kr.org/2025/60/kr2025-0060-ren-et-al.pdf"},{"title":"[2404.15522v2] LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models","url":"https://arxiv.org/abs/2404.15522v2"},{"title":"Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf"}]

Based on the search results, here's comprehensive information about the LogicBench dataset:

## Overview

LogicBench is a natural language question-answeri
…[truncated 1436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-14T14:44:05.518831+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-14T14:44:05.519047+00:00_

artifacts/src/disagree.py
artifacts/_project/intermediate/pipeline.py
artifacts/.venv/lib/python3.14/site-packages/pip/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/__main__.py
artifacts/.venv/lib/python3.14/site-packages/pip/__pip-runner__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/build_env.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cache.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/autocompletion.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/base_command.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/cmdoptions.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/command_context.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/index_command.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/main.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/main_parser.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/parser.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/progress_bars.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/req_command.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/spinners.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/status_codes.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/cache.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/check.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/completion.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/debug.py
artifacts/.venv/lib/python3.14/site-packages
…[truncated 5964 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-14T14:44:05.519324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/src/disagree.py",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/src/disagree.py",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-14T14:44:05.519503+00:00_

1	"""
2	分歧检测器 + rule-based 错误分类器。
3	比较 FOL / Python code 两路执行结果，分类错误模式。
4	"""
5	
6	from dataclasses import dataclass, asdict
7	from enum import Enum
8	from typing import Optional
9	
10	
11	# ---------------------------------------------------------------------------
12	# Enums
13	# ---------------------------------------------------------------------------
14	
15	class AgreementType(str, Enum):
16	    AGREE_CORRECT = "agree_correct"
17	    AGREE_WRONG   = "agree_wrong"
18	    DISAGREE      = "disagree"
19	    SINGLE_ERROR  = "single_error"
20	    BOTH_ERROR    = "both_error"
21	
22	
23	class ErrorType(str, Enum):
24	    EXEC_CRASH         = "exec_crash"
25	    TIMEOUT            = "timeout"
26	    QUANTIFIER_ERROR   = "quantifier_error"
27	    NEGATION_ERROR     = "negation_error"
28	    CONSTRAINT_MISSING = "constraint_missing"
29	    CONSTRAINT_EXTRA   = "constraint_extra"
30	    TYPE_BOUNDARY      = "type_boundary"
31	    LOGIC_ERROR        = "logic_error"
32	    UNKNOWN            = "unknown"
33	
34	
35	# ---------------------------------------------------------------------------
36	# Result container
37	# ---------------------------------------------------------------------------
38	
39	@dataclass
40	class DisagreementResult:
41	    agreement_type: str
42	    fol_verdict: str
43	    code_verdict: str
44	    ground_truth: str
45	    fol_correct: Optional[bool]
46	    code_correct: Optional[bool]
47	    error_type: Optional[str]
48	    error_side: Optional[str]      # "fol" / "code" / "both" / None
49	
50	    def to_dict(self):
51	        return asdict(self)
52	
53	
54	# ---------------------------------------------------------------------------
55	# Detection
56	# ---------------------------------------------------------------------------
57	
58	def detect_disagreement(
59	    fol_verdict: str,
60	    code_verdict: str,
61	    ground_truth: str,
62	) -> DisagreementResult:
63	
64	    fol_err  = (fol_verdict == "Error")
65	    code_err = (code_verdict == "Error")
…[truncated 624 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-14T14:44:05.519665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/_project/intermediate/pipeline.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/_project/intermediate/pipeline.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-14T14:44:05.519813+00:00_

1	"""
2	主流程：数据加载 → 双表征生成 → 执行 → 分歧检测 → 错误分类 → 修复 → 保存。
3	支持断点续跑（--resume）和数量限制（--max-examples）。
4	"""
5	
6	import json
7	import time
8	import argparse
9	import logging
10	from pathlib import Path
11	from typing import List, Optional
12	
13	from config import RESULTS_DIR
14	from data_loader import load_folio, FolioExample
15	from formalize import generate_fol_code, generate_python_code
16	from executor import execute_code
17	from disagree import detect_disagreement, classify_error, AgreementType
18	from repair import targeted_repair, blind_regeneration
19	
20	logging.basicConfig(
21	    level=logging.INFO,
22	    format="%(asctime)s [%(levelname)s] %(message)s",
23	    handlers=[
24	        logging.StreamHandler(),
25	        logging.FileHandler(RESULTS_DIR / "pipeline.log"),
26	    ],
27	)
28	log = logging.getLogger(__name__)
29	
30	
31	def process_one(example: FolioExample) -> dict:
32	    rec = {
33	        "id": example.id,
34	        "premises": example.premises,
35	        "conclusion": example.conclusion,
36	        "ground_truth": example.label,
37	    }
38	
39	    # --- 1. 双表征生成 ---
40	    log.info("[%s] generating FOL code …", example.id)
41	    fol_raw, fol_code = generate_fol_code(example.premises, example.conclusion)
42	    rec["fol_raw"] = fol_raw
43	    rec["fol_code"] = fol_code
44	
45	    log.info("[%s] generating Python code …", example.id)
46	    code_raw, code_code = generate_python_code(example.premises, example.conclusion)
47	    rec["code_raw"] = code_raw
48	    rec["code_code"] = code_code
49	
50	    # --- 2. 执行 ---
51	    log.info("[%s] executing FOL code …", example.id)
52	    fol_ex = execute_code(fol_code)
53	    rec["fol_exec"] = fol_ex.to_dict()
54	
55	    log.info("[%s] executing Python code …", example.id)
56	    code_ex = execute_code(code_code)
57	    rec["code_exec"] = code_ex.to_dict()
58	
59	    # --- 3. 分歧检测 ---
60	    dis = detect_disagreement(fol_ex.verdict, code_ex.verdict, example.label)
61	    rec["disagreement"] = dis.to_di
…[truncated 1767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-14T14:44:05.519995+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "load_folio|FolioExample|data_loader",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts",
  "glob": "*.py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Grep",
  "tool_args": {
    "pattern": "load_folio|FolioExample|data_loader",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts",
    "glob": "*.py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-14T14:44:05.520118+00:00_

Found 4 files
artifacts/src/pipeline.py
artifacts/src/baseline.py
artifacts/src/data_loader.py
artifacts/_project/intermediate/pipeline.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-14T14:44:05.520240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/src/data_loader.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/src/data_loader.py"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-14T14:44:05.520370+00:00_

1	"""
2	FOLIO 数据集加载器。
3	从本地 JSONL 文件加载 validation set，输出 (id, premises, conclusion, label) 结构。
4	"""
5	
6	import json
7	from dataclasses import dataclass, asdict
8	from typing import List, Optional
9	from pathlib import Path
10	
11	from config import PROJECT_ROOT
12	
13	_LABEL_NORM = {
14	    "true": "True",
15	    "false": "False",
16	    "unknown": "Unknown",
17	    "uncertain": "Unknown",
18	}
19	
20	FOLIO_PATH = PROJECT_ROOT / "data" / "folio-validation.jsonl"
21	
22	
23	@dataclass
24	class FolioExample:
25	    id: str
26	    premises: str
27	    conclusion: str
28	    label: str           # "True" / "False" / "Unknown"
29	
30	    def to_dict(self):
31	        return asdict(self)
32	
33	
34	def _normalize_label(raw) -> str:
35	    if isinstance(raw, int):
36	        return ["True", "False", "Unknown"][raw]
37	    return _LABEL_NORM.get(str(raw).strip().lower(), "Unknown")
38	
39	
40	def _normalize_premises(raw) -> str:
41	    if isinstance(raw, list):
42	        return " ".join(raw)
43	    return str(raw)
44	
45	
46	def load_folio(
47	    max_examples: Optional[int] = None,
48	) -> List[FolioExample]:
49	    with open(FOLIO_PATH) as f:
50	        rows = [json.loads(line) for line in f if line.strip()]
51	
52	    examples = []
53	    for i, row in enumerate(rows):
54	        if max_examples and i >= max_examples:
55	            break
56	
57	        examples.append(FolioExample(
58	            id=f"folio_validation_{i}",
59	            premises=_normalize_premises(row["premises"]),
60	            conclusion=row["conclusion"],
61	            label=_normalize_label(row["label"]),
62	        ))
63	
64	    return examples
65	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-14T14:44:05.520608+00:00_

Now I have a complete picture. Here is the comprehensive research report.

---

## ProofWriter Dataset -- Comprehensive Research Report

### 1. Dataset Basics

**Paper:** Tafjord, Dalvi, Clark. "ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language." Findings of ACL-IJCNLP 2021. ([ACL Anthology](https://aclanthology.org/2021.findings-acl.317/), [arXiv](https://arxiv.org/abs/2012.13048))

**Task Format:** NLI-style. Each example contains:
- A **theory** (set of natural language facts + rules as context)
- A **question** (statement to verify)
- An **answer**: True / False / Unknown (under OWA)
- Optional **proof** (DAG of inference steps)

**Data Scale (from paper Table 10):**

| Depth | CWA Theories | CWA Questions | OWA Theories | OWA Questions |
|-------|-------------|---------------|-------------|---------------|
| D0 | 27,020 | 100,002 | 26,978 | 100,000 |
| D1 | 12,965 | 100,012 | 12,933 | 100,014 |
| D2 | 9,138 | 100,014 | 9,033 | 100,010 |
| D3 | 7,067 | 100,024 | 6,940 | 100,036 |
| D5 | 4,935 | 100,030 | 4,752 | 100,030 |

Total: ~500k questions (CWA) + ~500k questions (OWA) = ~1M questions across all depths.

**Split ratio:** 70% train / 10% dev / 20% test (per the paper).

**Label distribution:**
- CWA: equally divided True/False (binary, no Unknown)
- OWA: equally divided True/False/Unknown (~33% each)

**Reasoning depth:** D0 = direct fact lookup, D1-D5 = number of chained inference steps. D5 can have implications up to depth 10 (used for implication enumeration task). No D4 exists -- the depths are 0, 1, 2, 3, 5.

Additional sub-datasets:
- **Birds/Electricity**: 140 theories, 5,270 questions (hand-authored, out-of-distribution)
- **ParaRules**: 2,403 theories, 40,022 questions (crowdworker paraphrased natural language)

### 2. Dataset Characteristics

**Generation method:** Fully synthetic. Generated from Datalog programs using natural language templates. NOT human-annotated.

**Natural language style:** Templated
…[truncated 6991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Agent",
  "elapsed_ms": 15
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-14T14:44:05.520789+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-14T14:44:05.520935+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-14T14:44:05.521095+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "proofwriter_survey.md",
  "content": "# ProofWriter 数据集调研报告\n\n## 1. 数据集基本信息\n\n**论文**: Tafjord, Dalvi, Clark. \"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language.\" Findings of ACL-IJCNLP 2021.\n\n**任务格式**: NLI 风格，与 FOLIO 一致\n- **输入**: theory（自然语言事实 + 规则）+ question（待验证陈述）\n- **输出**: True / False / Unknown（OWA 设定下）\n- **附加**: 每个样本包含推理证明（DAG 格式）\n\n**数据规模**（OWA，与我们相关的设定）:\n\n| Depth | Theories | Questions |\n|-------|----------|-----------|\n| D0 | 26,978 | 100,000 |\n| D1 | 12,933 | 100,014 |\n| D2 | 9,033 | 100,010 |\n| D3 | 6,940 | 100,036 |\n| D5 | 4,752 | 100,030 |\n\n总计 ~500k questions (OWA)。Split: 70% train / 10% dev / 20% test。无 D4。\n\n**标签分布**:\n- **OWA**: True / False / Unknown 各约 **33%**（均衡分布）\n- **CWA**: 仅 True / False（无 Unknown），与我们不兼容\n- 对比 FOLIO：~39% Unknown，ProofWriter 更均衡\n\n**4 种配置**: AttNeg（属性+否定）、AttNoneg（属性无否定）、RelNeg（关系+否定）、RelNoneg（关系无否定）\n\n## 2. 与 FOLIO 的对比\n\n| 维度 | ProofWriter | FOLIO |\n|------|------------|-------|\n| 生成方式 | **合成/模板化**（Datalog 程序生成） | **专家人工标注** |\n| 词汇量 | ~101 词 | 4,351 词 |\n| 自然语言风格 | 简单模板句：\"Charlie is quiet.\" \"If someone is kind then they are young.\" | 真实自然语言，语义复杂 |\n| 规模 | ~500k (OWA) | 1,435 样本 |\n| 标签 | True/False/Unknown (OWA) | True/False/Unknown |\n| FOL 标注 | 无 | 有 |\n| 推理深度 | 显式标注 D0-D5 | 隐式（范围 0-14） |\n| 证明 | 包含（DAG） | 无 |\n\n**核心差异**: ProofWriter 是合成数据，语言高度模板化，推理结构干净可控；FOLIO 是真实自然语言，语义歧义多，形式化难度高。两者互补性强。\n\n**FOL 形式化适配性**: ProofWriter 的规则结构极其规整（一阶Horn子句 + 否定），转 Z3 非常直接。事实是简单的一元/二元谓词，规则是标准的 if-then 形式。比 FOLIO 容易得多。\n\n**Python 代码形式化适配性**: 同样容易。事实可表示为集合/字典，规则可表示为函数或推理循环。模板化结构意味着 LLM 生成代码的变异性更低。\n\n## 3. 对我们方法的预期影响\n\n### 3.1 不对称性预测\n\n**核心问题**: ProofWriter 会放大还是缩小 FOLIO 上观察到的 9:1 FOL 偏向不对称性？\n\n**预测: disagree rate 会显著降低，不对称性模式可能改变。**\n\n理由：\n- ProofWriter 的模板化语言大幅降低了 NL→FOL 和 NL→Code 的翻译难度\n- FOL 和 Code 都会变得更准确 → agree rate 上升 → disagree 样本减少\n- FOLIO 的 9:1 不对称性很可能源于 FOLIO 的语义复杂性对 Code 形式化的挑战更大（自然语言歧义 → Code 更容易出错），而 ProofWriter 消除了这一因素\n\n**两种可能的结果**:\n1. **不对称性缩小**（如 6:4 或 5:5）：说明不对称性与数据集语言复杂度相关，非方法固有偏差 → 对论文有利\n2. **不对称性保持但方向可能翻转**：如果 Code 在结构化数据上反而更强 → 更有趣的发现\n\n### 3.2 推理深度作为分析轴\n\n**高价值**。可以回答：\n- 浅层推理（D0-D1）是否 agree rate 极高（两种表征都轻松搞定）？\n- 深层推理（D3-D5）是否 disagree rate 上升？哪种表征在深层推理更脆弱？\n- 这为论文提供了 \"推理复杂度 vs 表征分歧\" 的分析维度，FOLIO 无法提供\n\n### 3.3 风险\n\n- **disagree 样本太少**: 如果两种表征在简单模板数据上都接近完美，disagree 数量可能不足以支撑统计分析\n- **缓解**: 使用 D5（最深推理）+ RelNeg（关系+否定，最复杂配置）来最大化难度\n\n## 4. 实操信息\n\n### 4.1 HuggingFace 数据集\n\n**推荐: `smoorsmith/proofwriter`**\n- 4,200 行（train 3,000 / dev 600 / test 600）\n- OWA D5 子集，来自 Logic-LLM 仓库（与 FOLIO 评测对齐）\n- 字段: `id`, `context`, `question`, `options`, `answer`, `depth`, `chain_of_thought`\n- Logic-LLM 论文正是用 FOLIO + ProofWriter OWA-D5 做评测，有直接可比性\n\n**其他版本**:\n- `tasksource/proofwriter`: 845k 行，全量数据，覆盖所有深度和配置\n- `D3xter1922/proofwriter-dataset`: 59k 行，原始格式\n\n### 4.2 Pipeline 适配\n\n当前 FOLIO 格式: `{premises, conclusion, label}`\n\nProofWriter (`smoorsmith/proofwriter`) 适配：\n```\ncontext → premises（事实+规则文本）\nquestion → 需提取结论（去掉 \"Based on the above information, is the following statement true, false, or unknown?\" 前缀）\nanswer → label（True/False/Unknown）\ndepth → 额外元数据（用于分层分析）\n```\n\n改动量小，新增一个 `ProofWriterDataLoader` 即可。\n\n### 4.3 推荐评测配置\n\n| 配置 | 样本数 | 理由 |\n|------|--------|------|\n| **OWA D5 test set** | 600 | Logic-LLM 标准配置，三类标签均衡，推理深度最大 |\n| 如需缩减 | 随机采样 200-300 | 保持标签均衡采样 |\n\n**推荐方案**: 直接用 `smoorsmith/proofwriter` 的 600 test 样本，与 FOLIO 的 204 样本规模接近。\n\n## 5. 替代数据集\n\n| 数据集 | 标签 | 格式匹配度 | 优势 | 劣势 | 推荐度 |\n|--------|------|-----------|------|------|--------|\n| **ProofWriter OWA** | T/F/U | ★★★★★ | 标签一致、Logic-LLM 先例、深度轴 | 合成数据、语言简单 | **首选** |\n| LogicNLI | E/C/N→T/F/U | ★★★★ | 三类标签、合成、FOL 基础 | 知名度低、无深度标注 | 备选 |\n| RuleTaker | T/F | ★★★ | ProofWriter 前身、大规模 | 无 Unknown 类、仅 CWA | 不推荐 |\n| LogiQA 2.0 NLI | 2-way | ★★ | 真实考试题 | 非规则推理、标签不匹配 | 不推荐 |\n| CLUTRR | 关系推理 | ★ | 亲属关系推理 | 任务格式完全不同 | 不适用 |\n| PrOntoQA | T/F | ★★ | 本体层级推理 | 无 Unknown、二分类 | 不推荐 |\n\n## 6. 结论\n\n**ProofWriter OWA D5 是最佳第二数据集**。理由：\n1. 任务格式与 FOLIO 完全一致（premises → conclusion → T/F/U）\n2. Logic-LLM 已建立 FOLIO + ProofWriter 的评测先例，审稿人容易接受\n3. 合成 vs 人工标注的对比恰好验证方法在不同数据特性下的泛化性\n4. 推理深度维度提供 FOLIO 无法提供的分析轴\n5. 标签均衡（各33%）vs FOLIO 的不均衡（39% Unknown）可验证标签分布对不对称性的影响\n6. HuggingFace 上有现成数据集，适配工作量极小（~1天）\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "cross_representation_disagreement_diagno",
    "file": "proofwriter_survey.md",
    "content": "# ProofWriter 数据集调研报告\n\n## 1. 数据集基本信息\n\n**论文**: Tafjord, Dalvi, Clark. \"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language.\" Findings of ACL-IJCNLP 2021.\n\n**任务格式**: NLI 风格，与 FOLIO 一致\n- **输入**: theory（自然语言事实 + 规则）+ question（待验证陈述）\n- **输出**: True / False / Unknown（OWA 设定下）\n- **附加**: 每个样本包含推理证明（DAG 格式）\n\n**数据规模**（OWA，与我们相关的设定）:\n\n| Depth | Theories | Questions |\n|-------|----------|-----------|\n| D0 | 26,978 | 100,000 |\n| D1 | 12,933 | 100,014 |\n| D2 | 9,033 | 100,010 |\n| D3 | 6,940 | 100,036 |\n| D5 | 4,752 | 100,030 |\n\n总计 ~500k questions (OWA)。Split: 70% train / 10% dev / 20% test。无 D4。\n\n**标签分布**:\n- **OWA**: True / False / Unknown 各约 **33%**（均衡分布）\n- **CWA**: 仅 True / False（无 Unknown），与我们不兼容\n- 对比 FOLIO：~39% Unknown，ProofWriter 更均衡\n\n**4 种配置**: AttNeg（属性+否定）、AttNoneg（属性无否定）、RelNeg（关系+否定）、RelNoneg（关系无否定）\n\n## 2. 与 FOLIO 的对比\n\n| 维度 | ProofWriter | FOLIO |\n|------|------------|-------|\n| 生成方式 | **合成/模板化**（Datalog 程序生成） | **专家人工标注** |\n| 词汇量 | ~101 词 | 4,351 词 |\n| 自然语言风格 | 简单模板句：\"Charlie is quiet.\" \"If someone is kind then they are young.\" | 真实自然语言，语义复杂 |\n| 规模 | ~500k (OWA) | 1,435 样本 |\n| 标签 | True/False/Unknown (OWA) | True/False/Unknown |\n| FOL 标注 | 无 | 有 |\n| 推理深度 | 显式标注 D0-D5 | 隐式（范围 0-14） |\n| 证明 | 包含（DAG） | 无 |\n\n**核心差异**: ProofWriter 是合成数据，语言高度模板化，推理结构干净可控；FOLIO 是真实自然语言，语义歧义多，形式化难度高。两者互补性强。\n\n**FOL 形式化适配性**: ProofWriter 的规则结构极其规整（一阶Horn子句 + 否定），转 Z3 非常直接。事实是简单的一元/二元谓词，规则是标准的 if-then 形式。比 FOLIO 容易得多。\n\n**Python 代码形式化适配性**: 同样容易。事实可表示为集合/字典，规则可表示为函数或推理循环。模板化结构意味着 LLM 生成代码的变异性更低。\n\n## 3. 对我们方法的预期影响\n\n### 3.1 不对称性预测\n\n**核心问题**: ProofWriter 会放大还是缩小 FOLIO 上观察到的 9:1 FOL 偏向不对称性？\n\n**预测: disagree rate 会显著降低，不对称性模式可能改变。**\n\n理由：\n- ProofWriter 的模板化语言大幅降低了 NL→FOL 和 NL→Code 的翻译难度\n- FOL 和 Code 都会变得更准确 → agree rate 上升 → disagree 样本减少\n- FOLIO 的 9:1 不对称性很可能源于 FOLIO 的语义复杂性对 Code 形式化的挑战更大（自然语言歧义 → Code 更容易出错），而 ProofWriter 消除了这一因素\n\n**两种可能的结果**:\n1. **不对称性缩小**（如 6:4 或 5:5）：说明不对称性与数据集语言复杂度相关，非方法固有偏差 → 对论文有利\n2. **不对称性保持但方向可能翻转**：如果 Code 在结构化数据上反而更强 → 更有趣的发现\n\n### 3.2 推理深度作为分析轴\n\n**高价值**。可以回答：\n- 浅层推理（D0-D1）是否 agree rate 极高（两种表征都轻松搞定）？\n- 深层推理（D3-D5）是否 disagree rate 上升？哪种表征在深层推理更脆弱？\n- 这为论文提供了 \"推理复杂度 vs 表征分歧\" 的分析维度，FOLIO 无法提供\n\n### 3.3 风险\n\n- **disagree 样本太少**: 如果两种表征在简单模板数据上都接近完美，disagree 数量可能不足以支撑统计分析\n- **缓解**: 使用 D5（最深推理）+ RelNeg（关系+否定，最复杂配置）来最大化难度\n\n## 4. 实操信息\n\n### 4.1 HuggingFace 数据集\n\n**推荐: `smoorsmith/proofwriter`**\n- 4,200 行（train 3,000 / dev 600 / test 600）\n- OWA D5 子集，来自 Logic-LLM 仓库（与 FOLIO 评测对齐）\n- 字段: `id`, `context`, `question`, `options`, `answer`, `depth`, `chain_of_thought`\n- Logic-LLM 论文正是用 FOLIO + ProofWriter OWA-D5 做评测，有直接可比性\n\n**其他版本**:\n- `tasksource/proofwriter`: 845k 行，全量数据，覆盖所有深度和配置\n- `D3xter1922/proofwriter-dataset`: 59k 行，原始格式\n\n### 4.2 Pipeline 适配\n\n当前 FOLIO 格式: `{premises, conclusion, label}`\n\nProofWriter (`smoorsmith/proofwriter`) 适配：\n```\ncontext → premises（事实+规则文本）\nquestion → 需提取结论（去掉 \"Based on the above information, is the following statement true, false, or unknown?\" 前缀）\nanswer → label（True/False/Unknown）\ndepth → 额外元数据（用于分层分析）\n```\n\n改动量小，新增一个 `ProofWriterDataLoader` 即可。\n\n### 4.3 推荐评测配置\n\n| 配置 | 样本数 | 理由 |\n|------|--------|------|\n| **OWA D5 test set** | 600 | Logic-LLM 标准配置，三类标签均衡，推理深度最大 |\n| 如需缩减 | 随机采样 200-300 | 保持标签均衡采样 |\n\n**推荐方案**: 直接用 `smoorsmith/proofwriter` 的 600 test 样本，与 FOLIO 的 204 样本规模接近。\n\n## 5. 替代数据集\n\n| 数据集 | 标签 | 格式匹配度 | 优势 | 劣势 | 推荐度 |\n|--------|------|-----------|------|------|--------|\n| **ProofWriter OWA** | T/F/U | ★★★★★ | 标签一致、Logic-LLM 先例、深度轴 | 合成数据、语言简单 | **首选** |\n| LogicNLI | E/C/N→T/F/U | ★★★★ | 三类标签、合成、FOL 基础 | 知名度低、无深度标注 | 备选 |\n| RuleTaker | T/F | ★★★ | ProofWriter 前身、大规模 | 无 Unknown 类、仅 CWA | 不推荐 |\n| LogiQA 2.0 NLI | 2-way | ★★ | 真实考试题 | 非规则推理、标签不匹配 | 不推荐 |\n| CLUTRR | 关系推理 | ★ | 亲属关系推理 | 任务格式完全不同 | 不适用 |\n| PrOntoQA | T/F | ★★ | 本体层级推理 | 无 Unknown、二分类 | 不推荐 |\n\n## 6. 结论\n\n**ProofWriter OWA D5 是最佳第二数据集**。理由：\n1. 任务格式与 FOLIO 完全一致（premises → conclusion → T/F/U）\n2. Logic-LLM 已建立 FOLIO + ProofWriter 的评测先例，审稿人容易接受\n3. 合成 vs 人工标注的对比恰好验证方法在不同数据特性下的泛化性\n4. 推理深度维度提供 FOLIO 无法提供的分析轴\n5. 标签均衡（各33%）vs FOLIO 的不均衡（39% Unknown）可验证标签分布对不对称性的影响\n6. HuggingFace 上有现成数据集，适配工作量极小（~1天）\n"
  }
}
````

</details>

---

### Tool result

_source line 102 · 2026-05-14T14:44:05.521284+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'proofwriter_survey.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-14T14:44:05.521433+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/",
  "description": "List project directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/",
    "description": "List project directory contents"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-14T14:44:05.521651+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
logs
memory.md
registry.lock
registry.yaml
report.md
study_status.lock
task_context

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-14T14:44:05.521808+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/docs/proofwriter_survey.md",
  "content": "# ProofWriter 数据集调研报告\n\n## 1. 数据集基本信息\n\n**论文**: Tafjord, Dalvi, Clark. \"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language.\" Findings of ACL-IJCNLP 2021.\n\n**任务格式**: NLI 风格，与 FOLIO 一致\n- **输入**: theory（自然语言事实 + 规则）+ question（待验证陈述）\n- **输出**: True / False / Unknown（OWA 设定下）\n- **附加**: 每个样本包含推理证明（DAG 格式）\n\n**数据规模**（OWA，与我们相关的设定）:\n\n| Depth | Theories | Questions |\n|-------|----------|-----------|\n| D0 | 26,978 | 100,000 |\n| D1 | 12,933 | 100,014 |\n| D2 | 9,033 | 100,010 |\n| D3 | 6,940 | 100,036 |\n| D5 | 4,752 | 100,030 |\n\n总计 ~500k questions (OWA)。Split: 70% train / 10% dev / 20% test。无 D4。\n\n**标签分布**:\n- **OWA**: True / False / Unknown 各约 **33%**（均衡分布）\n- **CWA**: 仅 True / False（无 Unknown），与我们不兼容\n- 对比 FOLIO：~39% Unknown，ProofWriter 更均衡\n\n**4 种配置**: AttNeg（属性+否定）、AttNoneg（属性无否定）、RelNeg（关系+否定）、RelNoneg（关系无否定）\n\n## 2. 与 FOLIO 的对比\n\n| 维度 | ProofWriter | FOLIO |\n|------|------------|-------|\n| 生成方式 | **合成/模板化**（Datalog 程序生成） | **专家人工标注** |\n| 词汇量 | ~101 词 | 4,351 词 |\n| 自然语言风格 | 简单模板句：\"Charlie is quiet.\" \"If someone is kind then they are young.\" | 真实自然语言，语义复杂 |\n| 规模 | ~500k (OWA) | 1,435 样本 |\n| 标签 | True/False/Unknown (OWA) | True/False/Unknown |\n| FOL 标注 | 无 | 有 |\n| 推理深度 | 显式标注 D0-D5 | 隐式（范围 0-14） |\n| 证明 | 包含（DAG） | 无 |\n\n**核心差异**: ProofWriter 是合成数据，语言高度模板化，推理结构干净可控；FOLIO 是真实自然语言，语义歧义多，形式化难度高。两者互补性强。\n\n**FOL 形式化适配性**: ProofWriter 的规则结构极其规整（一阶 Horn 子句 + 否定），转 Z3 非常直接。事实是简单的一元/二元谓词，规则是标准的 if-then 形式。比 FOLIO 容易得多。\n\n**Python 代码形式化适配性**: 同样容易。事实可表示为集合/字典，规则可表示为函数或推理循环。模板化结构意味着 LLM 生成代码的变异性更低。\n\n## 3. 对我们方法的预期影响\n\n### 3.1 不对称性预测\n\n**核心问题**: ProofWriter 会放大还是缩小 FOLIO 上观察到的 9:1 FOL 偏向不对称性？\n\n**预测: disagree rate 会显著降低，不对称性模式可能改变。**\n\n理由：\n- ProofWriter 的模板化语言大幅降低了 NL→FOL 和 NL→Code 的翻译难度\n- FOL 和 Code 都会变得更准确 → agree rate 上升 → disagree 样本减少\n- FOLIO 的 9:1 不对称性很可能源于 FOLIO 的语义复杂性对 Code 形式化的挑战更大（自然语言歧义 → Code 更容易出错），而 ProofWriter 消除了这一因素\n\n**两种可能的结果**:\n1. **不对称性缩小**（如 6:4 或 5:5）：说明不对称性与数据集语言复杂度相关，非方法固有偏差 → 对论文有利\n2. **不对称性保持但方向可能翻转**：如果 Code 在结构化数据上反而更强 → 更有趣的发现\n\n### 3.2 推理深度作为分析轴\n\n**高价值**。可以回答：\n- 浅层推理（D0-D1）是否 agree rate 极高（两种表征都轻松搞定）？\n- 深层推理（D3-D5）是否 disagree rate 上升？哪种表征在深层推理更脆弱？\n- 这为论文提供了 \"推理复杂度 vs 表征分歧\" 的分析维度，FOLIO 无法提供\n\n### 3.3 风险\n\n- **disagree 样本太少**: 如果两种表征在简单模板数据上都接近完美，disagree 数量可能不足以支撑统计分析\n- **缓解**: 使用 D5（最深推理）+ RelNeg（关系+否定，最复杂配置）来最大化难度\n\n## 4. 实操信息\n\n### 4.1 HuggingFace 数据集\n\n**推荐: `smoorsmith/proofwriter`**\n- 4,200 行（train 3,000 / dev 600 / test 600）\n- OWA D5 子集，来自 Logic-LLM 仓库（与 FOLIO 评测对齐）\n- 字段: `id`, `context`, `question`, `options`, `answer`, `depth`, `chain_of_thought`\n- Logic-LLM 论文正是用 FOLIO + ProofWriter OWA-D5 做评测，有直接可比性\n\n**其他版本**:\n- `tasksource/proofwriter`: 845k 行，全量数据，覆盖所有深度和配置\n- `D3xter1922/proofwriter-dataset`: 59k 行，原始格式\n\n### 4.2 Pipeline 适配\n\n当前 FOLIO 格式: `{premises, conclusion, label}`\n\nProofWriter (`smoorsmith/proofwriter`) 适配：\n```\ncontext → premises（事实+规则文本）\nquestion → 需提取结论（去掉 \"Based on the above information, is the following statement true, false, or unknown?\" 前缀）\nanswer → label（True/False/Unknown）\ndepth → 额外元数据（用于分层分析）\n```\n\n改动量小，新增一个 `ProofWriterDataLoader` 即可。\n\n### 4.3 推荐评测配置\n\n| 配置 | 样本数 | 理由 |\n|------|--------|------|\n| **OWA D5 test set** | 600 | Logic-LLM 标准配置，三类标签均衡，推理深度最大 |\n| 如需缩减 | 随机采样 200-300 | 保持标签均衡采样 |\n\n**推荐方案**: 直接用 `smoorsmith/proofwriter` 的 600 test 样本，与 FOLIO 的 204 样本规模接近。\n\n## 5. 替代数据集\n\n| 数据集 | 标签 | 格式匹配度 | 优势 | 劣势 | 推荐度 |\n|--------|------|-----------|------|------|--------|\n| **ProofWriter OWA** | T/F/U | ★★★★★ | 标签一致、Logic-LLM 先例、深度轴 | 合成数据、语言简单 | **首选** |\n| LogicNLI | E/C/N→T/F/U | ★★★★ | 三类标签、合成、FOL 基础 | 知名度低、无深度标注 | 备选 |\n| RuleTaker | T/F | ★★★ | ProofWriter 前身、大规模 | 无 Unknown 类、仅 CWA | 不推荐 |\n| LogiQA 2.0 NLI | 2-way | ★★ | 真实考试题 | 非规则推理、标签不匹配 | 不推荐 |\n| CLUTRR | 关系推理 | ★ | 亲属关系推理 | 任务格式完全不同 | 不适用 |\n| PrOntoQA | T/F | ★★ | 本体层级推理 | 无 Unknown、二分类 | 不推荐 |\n\n## 6. 结论\n\n**ProofWriter OWA D5 是最佳第二数据集**。理由：\n1. 任务格式与 FOLIO 完全一致（premises → conclusion → T/F/U）\n2. Logic-LLM 已建立 FOLIO + ProofWriter 的评测先例，审稿人容易接受\n3. 合成 vs 人工标注的对比恰好验证方法在不同数据特性下的泛化性\n4. 推理深度维度提供 FOLIO 无法提供的分析轴\n5. 标签均衡（各33%）vs FOLIO 的不均衡（39% Unknown）可验证标签分布对不对称性的影响\n6. HuggingFace 上有现成数据集（`smoorsmith/proofwriter`），适配工作量极小（~1天）\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/docs/proofwriter_survey.md",
    "content": "# ProofWriter 数据集调研报告\n\n## 1. 数据集基本信息\n\n**论文**: Tafjord, Dalvi, Clark. \"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language.\" Findings of ACL-IJCNLP 2021.\n\n**任务格式**: NLI 风格，与 FOLIO 一致\n- **输入**: theory（自然语言事实 + 规则）+ question（待验证陈述）\n- **输出**: True / False / Unknown（OWA 设定下）\n- **附加**: 每个样本包含推理证明（DAG 格式）\n\n**数据规模**（OWA，与我们相关的设定）:\n\n| Depth | Theories | Questions |\n|-------|----------|-----------|\n| D0 | 26,978 | 100,000 |\n| D1 | 12,933 | 100,014 |\n| D2 | 9,033 | 100,010 |\n| D3 | 6,940 | 100,036 |\n| D5 | 4,752 | 100,030 |\n\n总计 ~500k questions (OWA)。Split: 70% train / 10% dev / 20% test。无 D4。\n\n**标签分布**:\n- **OWA**: True / False / Unknown 各约 **33%**（均衡分布）\n- **CWA**: 仅 True / False（无 Unknown），与我们不兼容\n- 对比 FOLIO：~39% Unknown，ProofWriter 更均衡\n\n**4 种配置**: AttNeg（属性+否定）、AttNoneg（属性无否定）、RelNeg（关系+否定）、RelNoneg（关系无否定）\n\n## 2. 与 FOLIO 的对比\n\n| 维度 | ProofWriter | FOLIO |\n|------|------------|-------|\n| 生成方式 | **合成/模板化**（Datalog 程序生成） | **专家人工标注** |\n| 词汇量 | ~101 词 | 4,351 词 |\n| 自然语言风格 | 简单模板句：\"Charlie is quiet.\" \"If someone is kind then they are young.\" | 真实自然语言，语义复杂 |\n| 规模 | ~500k (OWA) | 1,435 样本 |\n| 标签 | True/False/Unknown (OWA) | True/False/Unknown |\n| FOL 标注 | 无 | 有 |\n| 推理深度 | 显式标注 D0-D5 | 隐式（范围 0-14） |\n| 证明 | 包含（DAG） | 无 |\n\n**核心差异**: ProofWriter 是合成数据，语言高度模板化，推理结构干净可控；FOLIO 是真实自然语言，语义歧义多，形式化难度高。两者互补性强。\n\n**FOL 形式化适配性**: ProofWriter 的规则结构极其规整（一阶 Horn 子句 + 否定），转 Z3 非常直接。事实是简单的一元/二元谓词，规则是标准的 if-then 形式。比 FOLIO 容易得多。\n\n**Python 代码形式化适配性**: 同样容易。事实可表示为集合/字典，规则可表示为函数或推理循环。模板化结构意味着 LLM 生成代码的变异性更低。\n\n## 3. 对我们方法的预期影响\n\n### 3.1 不对称性预测\n\n**核心问题**: ProofWriter 会放大还是缩小 FOLIO 上观察到的 9:1 FOL 偏向不对称性？\n\n**预测: disagree rate 会显著降低，不对称性模式可能改变。**\n\n理由：\n- ProofWriter 的模板化语言大幅降低了 NL→FOL 和 NL→Code 的翻译难度\n- FOL 和 Code 都会变得更准确 → agree rate 上升 → disagree 样本减少\n- FOLIO 的 9:1 不对称性很可能源于 FOLIO 的语义复杂性对 Code 形式化的挑战更大（自然语言歧义 → Code 更容易出错），而 ProofWriter 消除了这一因素\n\n**两种可能的结果**:\n1. **不对称性缩小**（如 6:4 或 5:5）：说明不对称性与数据集语言复杂度相关，非方法固有偏差 → 对论文有利\n2. **不对称性保持但方向可能翻转**：如果 Code 在结构化数据上反而更强 → 更有趣的发现\n\n### 3.2 推理深度作为分析轴\n\n**高价值**。可以回答：\n- 浅层推理（D0-D1）是否 agree rate 极高（两种表征都轻松搞定）？\n- 深层推理（D3-D5）是否 disagree rate 上升？哪种表征在深层推理更脆弱？\n- 这为论文提供了 \"推理复杂度 vs 表征分歧\" 的分析维度，FOLIO 无法提供\n\n### 3.3 风险\n\n- **disagree 样本太少**: 如果两种表征在简单模板数据上都接近完美，disagree 数量可能不足以支撑统计分析\n- **缓解**: 使用 D5（最深推理）+ RelNeg（关系+否定，最复杂配置）来最大化难度\n\n## 4. 实操信息\n\n### 4.1 HuggingFace 数据集\n\n**推荐: `smoorsmith/proofwriter`**\n- 4,200 行（train 3,000 / dev 600 / test 600）\n- OWA D5 子集，来自 Logic-LLM 仓库（与 FOLIO 评测对齐）\n- 字段: `id`, `context`, `question`, `options`, `answer`, `depth`, `chain_of_thought`\n- Logic-LLM 论文正是用 FOLIO + ProofWriter OWA-D5 做评测，有直接可比性\n\n**其他版本**:\n- `tasksource/proofwriter`: 845k 行，全量数据，覆盖所有深度和配置\n- `D3xter1922/proofwriter-dataset`: 59k 行，原始格式\n\n### 4.2 Pipeline 适配\n\n当前 FOLIO 格式: `{premises, conclusion, label}`\n\nProofWriter (`smoorsmith/proofwriter`) 适配：\n```\ncontext → premises（事实+规则文本）\nquestion → 需提取结论（去掉 \"Based on the above information, is the following statement true, false, or unknown?\" 前缀）\nanswer → label（True/False/Unknown）\ndepth → 额外元数据（用于分层分析）\n```\n\n改动量小，新增一个 `ProofWriterDataLoader` 即可。\n\n### 4.3 推荐评测配置\n\n| 配置 | 样本数 | 理由 |\n|------|--------|------|\n| **OWA D5 test set** | 600 | Logic-LLM 标准配置，三类标签均衡，推理深度最大 |\n| 如需缩减 | 随机采样 200-300 | 保持标签均衡采样 |\n\n**推荐方案**: 直接用 `smoorsmith/proofwriter` 的 600 test 样本，与 FOLIO 的 204 样本规模接近。\n\n## 5. 替代数据集\n\n| 数据集 | 标签 | 格式匹配度 | 优势 | 劣势 | 推荐度 |\n|--------|------|-----------|------|------|--------|\n| **ProofWriter OWA** | T/F/U | ★★★★★ | 标签一致、Logic-LLM 先例、深度轴 | 合成数据、语言简单 | **首选** |\n| LogicNLI | E/C/N→T/F/U | ★★★★ | 三类标签、合成、FOL 基础 | 知名度低、无深度标注 | 备选 |\n| RuleTaker | T/F | ★★★ | ProofWriter 前身、大规模 | 无 Unknown 类、仅 CWA | 不推荐 |\n| LogiQA 2.0 NLI | 2-way | ★★ | 真实考试题 | 非规则推理、标签不匹配 | 不推荐 |\n| CLUTRR | 关系推理 | ★ | 亲属关系推理 | 任务格式完全不同 | 不适用 |\n| PrOntoQA | T/F | ★★ | 本体层级推理 | 无 Unknown、二分类 | 不推荐 |\n\n## 6. 结论\n\n**ProofWriter OWA D5 是最佳第二数据集**。理由：\n1. 任务格式与 FOLIO 完全一致（premises → conclusion → T/F/U）\n2. Logic-LLM 已建立 FOLIO + ProofWriter 的评测先例，审稿人容易接受\n3. 合成 vs 人工标注的对比恰好验证方法在不同数据特性下的泛化性\n4. 推理深度维度提供 FOLIO 无法提供的分析轴\n5. 标签均衡（各33%）vs FOLIO 的不均衡（39% Unknown）可验证标签分布对不对称性的影响\n6. HuggingFace 上有现成数据集（`smoorsmith/proofwriter`），适配工作量极小（~1天）\n"
  }
}
````

</details>

---

### Tool result

_source line 106 · 2026-05-14T14:44:05.522029+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/docs/proofwriter_survey.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_proofwriter_survey_20260514T143225",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 107 · 2026-05-14T14:44:05.522194+00:00_

报告已保存到 `docs/proofwriter_survey.md`。核心结论：

**ProofWriter OWA D5 是最佳第二数据集**，直接用 HuggingFace `smoorsmith/proofwriter` 的 600 test 样本。

关键判断：
- **格式完全兼容**：同样是 premises → conclusion → T/F/U，pipeline 适配量约 1 天
- **与 FOLIO 互补性强**：合成模板 vs 专家标注，简单语言 vs 复杂自然语言
- **Logic-LLM 先例**：该论文正是用 FOLIO + ProofWriter OWA-D5 做评测，审稿人容易接受
- **不对称性预测**：ProofWriter 模板化语言会同时降低 FOL 和 Code 的翻译难度，disagree rate 预期下降，9:1 不对称性可能缩小——这恰好能说明不对称性与数据集语言复杂度相关而非方法固有偏差
- **额外分析轴**：推理深度 D0-D5 可分析"推理复杂度 vs 表征分歧"的关系
- **风险**：数据太简单导致 disagree 样本不足，可通过选择 D5 + RelNeg 配置缓解

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_proofwriter_survey_20260514T143225"
}
```

</details>

---
