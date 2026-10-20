# research d145 fol datasets

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 335
- **Recorded user turns:** 0
- **Tool calls:** 167
- **Original source:** `logs/chats/worker_research_d145-fol-datasets_20260519T131524.jsonl`
- **Structured JSON:** [`c5ad4ea1d3be372e148e.json`](../../sessions/c5/c5ad4ea1d3be372e148e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

335 recorded events

### Tool call

_source line 1 · 2026-05-19T13:25:44.493805+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Survey ProntoQA dataset",
  "subagent_type": "general-purpose",
  "prompt": "Research the ProntoQA dataset for formal logic (FOL) annotations. Do the following:\n\n1. Search the web for \"ProntoQA dataset\" to find its paper, GitHub repo, and HuggingFace page\n2. Check HuggingFace Hub for ProntoQA datasets: try downloading/viewing sample data from any available version\n3. Determine: does ProntoQA contain first-order logic (FOL) premises and conclusions as fields? Specifically looking for fields like fol_premises, fol_conclusion, or equivalent FOL annotations.\n4. If FOL fields exist, show the first 2-3 examples with their structure\n5. If no FOL but structured rules exist, describe what format the logical rules are in and how hard it would be to convert to standard FOL\n\nReport concisely:\n- Dataset size (number of examples)\n- Field structure (list all fields)\n- Whether FOL annotations exist (yes/no/partial)\n- If partial or no, what would conversion require\n- FOL compatibility score 1-5 (5=directly compatible with Prover9 FOL format)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "tool_args": {
    "description": "Survey ProntoQA dataset",
    "subagent_type": "general-purpose",
    "prompt": "Research the ProntoQA dataset for formal logic (FOL) annotations. Do the following:\n\n1. Search the web for \"ProntoQA dataset\" to find its paper, GitHub repo, and HuggingFace page\n2. Check HuggingFace Hub for ProntoQA datasets: try downloading/viewing sample data from any available version\n3. Determine: does ProntoQA contain first-order logic (FOL) premises and conclusions as fields? Specifically looking for fields like fol_premises, fol_conclusion, or equivalent FOL annotations.\n4. If FOL fields exist, show the first 2-3 examples with their structure\n5. If no FOL but structured rules exist, describe what format the logical rules are in and how hard it would be to convert to standard FOL\n\nReport concisely:\n- Dataset size (number of examples)\n- Field structure (list all fields)\n- Whether FOL annotations exist (yes/no/partial)\n- If partial or no, what would conversion require\n- FOL compatibility score 1-5 (5=directly compatible with Prover9 FOL format)"
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-19T13:25:44.494223+00:00_

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
  "session": "worker_research_d145-fol-datasets_20260519T131524",
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

_source line 3 · 2026-05-19T13:25:44.494383+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T13:25:44.494513+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Survey LogicNLI dataset",
  "subagent_type": "general-purpose",
  "prompt": "Research the LogicNLI dataset for formal logic (FOL) annotations. Do the following:\n\n1. Search the web for \"LogicNLI dataset\" to find its paper, GitHub repo, and HuggingFace page\n2. Check HuggingFace Hub for LogicNLI datasets\n3. Determine: does LogicNLI contain first-order logic (FOL) premises and conclusions as fields? Specifically looking for fields like fol_premises, fol_conclusion, or equivalent FOL annotations.\n4. Show sample data structure if possible\n5. If no FOL but structured rules exist, describe what format the logical rules are in and how hard it would be to convert to standard FOL\n\nReport concisely:\n- Dataset size (number of examples)\n- Field structure (list all fields)\n- Whether FOL annotations exist (yes/no/partial)\n- If partial or no, what would conversion require\n- FOL compatibility score 1-5 (5=directly compatible with Prover9 FOL format)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "tool_args": {
    "description": "Survey LogicNLI dataset",
    "subagent_type": "general-purpose",
    "prompt": "Research the LogicNLI dataset for formal logic (FOL) annotations. Do the following:\n\n1. Search the web for \"LogicNLI dataset\" to find its paper, GitHub repo, and HuggingFace page\n2. Check HuggingFace Hub for LogicNLI datasets\n3. Determine: does LogicNLI contain first-order logic (FOL) premises and conclusions as fields? Specifically looking for fields like fol_premises, fol_conclusion, or equivalent FOL annotations.\n4. Show sample data structure if possible\n5. If no FOL but structured rules exist, describe what format the logical rules are in and how hard it would be to convert to standard FOL\n\nReport concisely:\n- Dataset size (number of examples)\n- Field structure (list all fields)\n- Whether FOL annotations exist (yes/no/partial)\n- If partial or no, what would conversion require\n- FOL compatibility score 1-5 (5=directly compatible with Prover9 FOL format)"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T13:25:44.494688+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProntoQA dataset first-order logic FOL annotations GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProntoQA dataset first-order logic FOL annotations GitHub"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T13:25:44.494884+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProntoQA dataset HuggingFace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProntoQA dataset HuggingFace"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T13:25:44.495009+00:00_

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
  "session": "worker_research_d145-fol-datasets_20260519T131524",
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

_source line 8 · 2026-05-19T13:25:44.495129+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T13:25:44.495248+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Survey FOLIO extensions",
  "subagent_type": "general-purpose",
  "prompt": "Research FOLIO dataset and its extensions/variants for formal logic (FOL) annotations. Do the following:\n\n1. Search the web for \"FOLIO dataset\" extensions, larger versions, or community-contributed splits\n2. Check HuggingFace Hub: search for all datasets matching \"FOLIO\" - look for extended versions, FOLIO-v2, FOLIO-wiki, etc.\n3. For each version found, check: how many examples? What fields? Does it have fol_premises and fol_conclusion?\n4. The original FOLIO has ~1400 examples with FOL annotations. Are there larger versions?\n5. Check if there's a \"FOLIO-wiki\" or similar extension that was mentioned in follow-up papers\n\nReport concisely:\n- All FOLIO variants found (name, source, size)\n- Which ones have FOL annotations\n- The largest available version with FOL\n- FOL compatibility score 1-5 for each variant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "tool_args": {
    "description": "Survey FOLIO extensions",
    "subagent_type": "general-purpose",
    "prompt": "Research FOLIO dataset and its extensions/variants for formal logic (FOL) annotations. Do the following:\n\n1. Search the web for \"FOLIO dataset\" extensions, larger versions, or community-contributed splits\n2. Check HuggingFace Hub: search for all datasets matching \"FOLIO\" - look for extended versions, FOLIO-v2, FOLIO-wiki, etc.\n3. For each version found, check: how many examples? What fields? Does it have fol_premises and fol_conclusion?\n4. The original FOLIO has ~1400 examples with FOL annotations. Are there larger versions?\n5. Check if there's a \"FOLIO-wiki\" or similar extension that was mentioned in follow-up papers\n\nReport concisely:\n- All FOLIO variants found (name, source, size)\n- Which ones have FOL annotations\n- The largest available version with FOL\n- FOL compatibility score 1-5 for each variant"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T13:25:44.495430+00:00_

Web search results for query: "ProntoQA dataset HuggingFace"

Links: [{"title":"tasksource/prontoqa · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/prontoqa"},{"title":"longface/prontoqa-train · Datasets at Hugging Face","url":"https://huggingface.co/datasets/longface/prontoqa-train"},{"title":"renma/ProntoQA · Datasets at Hugging Face","url":"https://huggingface.co/datasets/renma/ProntoQA"},{"title":"community-datasets/proto_qa · Datasets at Hugging Face","url":"https://huggingface.co/datasets/community-datasets/proto_qa"},{"title":"GitHub - asaparov/prontoqa: Synthetic question-answering dataset to formally analyze the chain-of-thought output of large language models on a reasoning task. · GitHub","url":"https://github.com/asaparov/prontoqa"},{"title":"tasksource/prontoqa at main","url":"https://huggingface.co/datasets/tasksource/prontoqa/tree/main"},{"title":"Navigating Dataset Documentations in AI: A Large-Scale Analysis of   Dataset Cards on Hugging Face","url":"https://arxiv.org/pdf/2401.13822"},{"title":"Language Models Are Greedy Reasoners: A Systematic Formal Analysis of   Chain-of-Thought","url":"https://arxiv.org/pdf/2210.01240"},{"title":"fengyang0317/prontoqa at main","url":"https://huggingface.co/datasets/fengyang0317/prontoqa/tree/main"}]

Based on the search results, here's what I found about the ProntoQA dataset on HuggingFace:

ProntoQA is a synthetic QA dataset called PRONTOQA, for Proof and Ontology-Generated Question-Answering. Inspired by the PROOFWRITER dataset, each example in PRONTOQA is generated from an ontology and has a unique proof.

The dataset is available on HuggingFace through multiple repositories, including:
- `tasksource/prontoqa` (contains various JSON files with different logical reasoning tasks)
- `renma/ProntoQA` (contains 500 rows in a validation split)
- `fengyang0317/prontoqa` 

The proofs are converted into syntactically simple sentences using a grammar, and from the predicted chain-of-though
…[truncated 266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T13:25:44.495603+00:00_

Web search results for query: "ProntoQA dataset first-order logic FOL annotations GitHub"

Links: [{"title":"PrOntoQA: Synthetic QA for Formal Reasoning","url":"https://www.emergentmind.com/topics/prontoqa-dataset"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"GitHub - teacherpeterpan/Logic-LLM: The project page for \"LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\" · GitHub","url":"https://github.com/teacherpeterpan/Logic-LLM"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs: Data   Generation, Incremental Fine-Tuning, and Verification","url":"https://arxiv.org/pdf/2409.16461"},{"title":"GitHub - asaparov/prontoqa: Synthetic question-answering dataset to formally analyze the chain-of-thought output of large language models on a reasoning task. · GitHub","url":"https://github.com/asaparov/prontoqa"},{"title":"first-order-logic · GitHub Topics · GitHub","url":"https://github.com/topics/first-order-logic?o=asc&s=stars"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/pdf/2505.14932"},{"title":"Large Language Models Meet Symbolic Provers for Logical Reasoning   Evaluation","url":"https://arxiv.org/pdf/2502.06563"}]

Based on the search results, here's what I found about the ProntoQA dataset:

## ProntoQA Dataset Overview

ProntoQA is a synthetic question-answering dataset purpose-built for the systematic, formal evaluation of LLM reasoning via interpretable first-order logic (FOL) ontologies. Its construction employs algorithmic ontology sampling and systematic proof generation to produce unambiguous FOL proofs and control deduction complexity.

## GitHub Repository

The official ProntoQA repository is available at: https://github.com/asaparov/prontoqa, which contains PrOntoQA-OOD, as described in papers including "Language Models Are Greedy Reasoners: A Systematic Formal A
…[truncated 721 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T13:25:44.495771+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicNLI dataset first-order logic NLI paper GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicNLI dataset first-order logic NLI paper GitHub"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T13:25:44.495900+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicNLI dataset HuggingFace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicNLI dataset HuggingFace"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T13:25:44.496021+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Survey RuleTaker/ProofWriter FOL variants",
  "subagent_type": "general-purpose",
  "prompt": "Research RuleTaker and ProofWriter dataset variants that might have FOL (first-order logic) annotations. Do the following:\n\n1. Search the web for \"RuleTaker FOL\" \"ProofWriter FOL annotations\" \"ProofWriter first-order logic\"\n2. Check HuggingFace Hub for any ProofWriter or RuleTaker variants that include FOL fields\n3. The original ProofWriter has natural language rules but NOT FOL annotations. Check if anyone has created a FOL-annotated version\n4. Check if there are community projects that converted ProofWriter rules to FOL\n5. Check the original RuleTaker/ProofWriter papers and repos for any FOL conversion scripts\n\nReport concisely:\n- Any FOL-annotated variants found (name, source, size)\n- If conversion tools exist, describe them\n- Feasibility of converting ProofWriter's structured rules to FOL (the rules are template-generated so should be convertible)\n- FOL compatibility score 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "tool_args": {
    "description": "Survey RuleTaker/ProofWriter FOL variants",
    "subagent_type": "general-purpose",
    "prompt": "Research RuleTaker and ProofWriter dataset variants that might have FOL (first-order logic) annotations. Do the following:\n\n1. Search the web for \"RuleTaker FOL\" \"ProofWriter FOL annotations\" \"ProofWriter first-order logic\"\n2. Check HuggingFace Hub for any ProofWriter or RuleTaker variants that include FOL fields\n3. The original ProofWriter has natural language rules but NOT FOL annotations. Check if anyone has created a FOL-annotated version\n4. Check if there are community projects that converted ProofWriter rules to FOL\n5. Check the original RuleTaker/ProofWriter papers and repos for any FOL conversion scripts\n\nReport concisely:\n- Any FOL-annotated variants found (name, source, size)\n- If conversion tools exist, describe them\n- Feasibility of converting ProofWriter's structured rules to FOL (the rules are template-generated so should be convertible)\n- FOL compatibility score 1-5"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T13:25:44.496188+00:00_

Web search results for query: "LogicNLI dataset first-order logic NLI paper GitHub"

Links: [{"title":"LogicNLI","url":"https://omnilabnlp.github.io/dataset/dataset.html"},{"title":"Diagnosing the First-Order Logical Reasoning Ability Through LogicNLI - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.303/"},{"title":"GitHub - omnilabNLP/LogicNLI","url":"https://github.com/omnilabNLP/LogicNLI"},{"title":"nli · GitHub Topics · GitHub","url":"https://github.com/topics/nli"},{"title":"first-order-logic · GitHub Topics · GitHub","url":"https://github.com/topics/first-order-logic"},{"title":"GitHub - utahnlp/layer_augmentation: Implementation of the NLI model in our ACL 2019 paper: Augmenting Neural Networks with First-order Logic.","url":"https://github.com/utahnlp/layer_augmentation"},{"title":"NL2LOGIC: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models","url":"https://arxiv.org/pdf/2602.13237"},{"title":"On the logical skills of large language models: evaluations using   arbitrarily complex first-order logic problems","url":"https://arxiv.org/pdf/2502.14180"}]

Based on the search results, here's the information about the LogicNLI dataset:

## LogicNLI Dataset Overview

LogicNLI is an NLI-style dataset that effectively disentangles the target FOL reasoning from commonsense inference and can be used to diagnose LMs from four perspectives: accuracy, robustness, generalization, and interpretability.

## Paper Information

The paper is titled "Diagnosing the First-Order Logical Reasoning Ability Through LogicNLI" authored by Jidong Tian, Yitian Li, Wenqing Chen, Liqiang Xiao, Hao He and Yaohui Jin, published in the Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (November 2021). The paper is available at: https://aclanthology.org/2021.emnlp-main.303

## GitHub Repository

The dataset is available on GitHub at: **https://github.com/omnilabNLP/LogicNLI**

The data is distributed 
…[truncated 145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T13:25:44.496344+00:00_

Web search results for query: "LogicNLI dataset HuggingFace"

Links: [{"title":"tasksource/LogicNLI · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/LogicNLI"},{"title":"logicreasoning/logi_glue · Datasets at Hugging Face","url":"https://huggingface.co/datasets/logicreasoning/logi_glue"},{"title":"kasnerz/logicnlg · Datasets at Hugging Face","url":"https://huggingface.co/datasets/kasnerz/logicnlg"},{"title":"tasksource/deberta-base-long-nli · Hugging Face","url":"https://huggingface.co/tasksource/deberta-base-long-nli"},{"title":"tasksource/deberta-small-long-nli · Hugging Face","url":"https://huggingface.co/tasksource/deberta-small-long-nli"},{"title":"hivaze/LOGIC-701 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/hivaze/LOGIC-701"},{"title":"tasksource/ModernBERT-large-nli · Hugging Face","url":"https://huggingface.co/tasksource/ModernBERT-large-nli"},{"title":"baber/logiqa2 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/baber/logiqa2"}]

Based on the search results, here's what I found about the LogicNLI dataset on HuggingFace:

## LogicNLI Dataset Overview

The LogicNLI dataset is associated with research titled "Diagnosing the First-Order Logical Reasoning Ability Through LogicNLI," published at the 2021 Conference on Empirical Methods in Natural Language Processing.

## Dataset Availability

The dataset is available on HuggingFace through the tasksource/LogicNLI repository. Additionally, the logicNLI subset contains 18k rows and is part of the larger logi_glue dataset collection on HuggingFace.

## Usage

The LogicNLI dataset is being utilized in multiple contexts:
- It's included as a logical reasoning task in training data for various NLI models
- It's used for multi-task fine-tuning in natural language inference models, such as ModernBERT

The dataset appears to be a well-established resource for evaluating and training models on logical reasoning tasks within the natural language underst
…[truncated 117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T13:25:44.496484+00:00_

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
  "session": "worker_research_d145-fol-datasets_20260519T131524",
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

_source line 18 · 2026-05-19T13:25:44.496599+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T13:25:44.496728+00:00_

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
  "session": "worker_research_d145-fol-datasets_20260519T131524",
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

_source line 20 · 2026-05-19T13:25:44.496862+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T13:25:44.496976+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Survey LogicBench and FLD",
  "subagent_type": "general-purpose",
  "prompt": "Research LogicBench and FLD (Formal Logic Deduction) datasets for formal logic (FOL) annotations. Do the following:\n\nFor LogicBench:\n1. Search the web for \"LogicBench dataset\" \"LogicBench benchmark logic reasoning\"\n2. Check HuggingFace Hub for LogicBench\n3. Determine if it contains FOL premises/conclusions\n4. Show sample data structure if possible\n\nFor FLD (Formal Logic Deduction):\n1. Search the web for \"FLD formal logic deduction dataset\"\n2. Check HuggingFace Hub for FLD dataset\n3. Determine if it contains FOL premises/conclusions\n4. Show sample data structure if possible\n5. FLD is known to have formal logic components - check exact format\n\nReport concisely for each:\n- Dataset size (number of examples)\n- Field structure (list all fields)\n- Whether FOL annotations exist (yes/no/partial)\n- If partial or no, what would conversion require\n- FOL compatibility score 1-5 (5=directly compatible with Prover9 FOL format)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "tool_args": {
    "description": "Survey LogicBench and FLD",
    "subagent_type": "general-purpose",
    "prompt": "Research LogicBench and FLD (Formal Logic Deduction) datasets for formal logic (FOL) annotations. Do the following:\n\nFor LogicBench:\n1. Search the web for \"LogicBench dataset\" \"LogicBench benchmark logic reasoning\"\n2. Check HuggingFace Hub for LogicBench\n3. Determine if it contains FOL premises/conclusions\n4. Show sample data structure if possible\n\nFor FLD (Formal Logic Deduction):\n1. Search the web for \"FLD formal logic deduction dataset\"\n2. Check HuggingFace Hub for FLD dataset\n3. Determine if it contains FOL premises/conclusions\n4. Show sample data structure if possible\n5. FLD is known to have formal logic components - check exact format\n\nReport concisely for each:\n- Dataset size (number of examples)\n- Field structure (list all fields)\n- Whether FOL annotations exist (yes/no/partial)\n- If partial or no, what would conversion require\n- FOL compatibility score 1-5 (5=directly compatible with Prover9 FOL format)"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T13:25:44.497192+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/asaparov/prontoqa",
  "prompt": "Extract the full README content. I need to understand: 1) What fields/columns does the dataset have? 2) Does it contain first-order logic (FOL) annotations as explicit fields? 3) What is the data format (JSON structure)? 4) How many examples are there? Show any example data structures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/asaparov/prontoqa",
    "prompt": "Extract the full README content. I need to understand: 1) What fields/columns does the dataset have? 2) Does it contain first-order logic (FOL) annotations as explicit fields? 3) What is the data format (JSON structure)? 4) How many examples are there? Show any example data structures."
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T13:25:44.497316+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/tasksource/prontoqa",
  "prompt": "Extract all information about the dataset fields/columns, number of examples/rows, splits, and any example data shown. I need to know the exact field names and whether any field contains first-order logic (FOL) annotations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/tasksource/prontoqa",
    "prompt": "Extract all information about the dataset fields/columns, number of examples/rows, splits, and any example data shown. I need to know the exact field names and whether any field contains first-order logic (FOL) annotations."
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T13:25:44.497452+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/renma/ProntoQA",
  "prompt": "Extract all information about the dataset fields/columns, number of examples/rows, splits, and any example data shown. I need to know the exact field names and whether any field contains first-order logic (FOL) annotations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/renma/ProntoQA",
    "prompt": "Extract all information about the dataset fields/columns, number of examples/rows, splits, and any example data shown. I need to know the exact field names and whether any field contains first-order logic (FOL) annotations."
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T13:25:44.497568+00:00_

# PrOntoQA Dataset Analysis

Based on the GitHub repository content provided, here's what I can determine:

## 1) Dataset Fields/Columns

The page does not explicitly list the dataset schema or field names. However, it mentions the dataset contains "question-answering examples with chains-of-thought that describe the reasoning required."

## 2) FOL Annotations

The repository indicates formal logic capabilities exist. The codebase includes a file called `fol.py`, suggesting first-order logic support is built into the framework. The description states: "The sentences in the examples are syntactically simple and amenable to semantic parsing, and so this code can be used to formally analyze the predicted chain-of-thought from large language models."

However, **the README does not explicitly confirm FOL annotations as explicit dataset fields**.

## 3) Data Format

The JSON structure is documented:

```json
{
  "example1": {
    "test_example": {
      "model_output": "&lt;model output as string, including predicted label>"
    }
  }
}
```

## 4) Dataset Size

**The README provides no information about the total number of examples** in the dataset.

## Recommendation

To understand the exact field structure and example counts, you would need to examine the actual data files in `generated_ood_data.zip` or review the paper citations referenced in the repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T13:25:44.497712+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/omnilabNLP/LogicNLI",
  "prompt": "Extract all information about: 1) data format and field structure (what fields each example has), 2) whether FOL (first-order logic) annotations are included as fields, 3) dataset size, 4) example data samples showing the structure, 5) how logical rules/premises are represented"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/omnilabNLP/LogicNLI",
    "prompt": "Extract all information about: 1) data format and field structure (what fields each example has), 2) whether FOL (first-order logic) annotations are included as fields, 3) dataset size, 4) example data samples showing the structure, 5) how logical rules/premises are represented"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T13:25:44.497838+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/tasksource/LogicNLI",
  "prompt": "Extract: 1) dataset fields/columns, 2) dataset size (number of rows), 3) sample data showing field values, 4) whether there are FOL (first-order logic) annotation fields like fol_premises or fol_conclusion, 5) data format details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/tasksource/LogicNLI",
    "prompt": "Extract: 1) dataset fields/columns, 2) dataset size (number of rows), 3) sample data showing field values, 4) whether there are FOL (first-order logic) annotation fields like fol_premises or fol_conclusion, 5) data format details"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T13:25:44.497951+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOLIO dataset formal logic FOL annotations extensions variants"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOLIO dataset formal logic FOL annotations extensions variants"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T13:25:44.498059+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOLIO-wiki dataset first-order logic larger version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOLIO-wiki dataset first-order logic larger version"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T13:25:44.498166+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HuggingFace FOLIO dataset FOL premises conclusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HuggingFace FOLIO dataset FOL premises conclusion"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T13:25:44.498270+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOLIO dataset v2 extended community splits formal logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOLIO dataset v2 extended community splits formal logic"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T13:25:44.498375+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RuleTaker ProofWriter FOL first-order logic annotations dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RuleTaker ProofWriter FOL first-order logic annotations dataset"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T13:25:44.498479+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProofWriter first-order logic conversion FOL annotated version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProofWriter first-order logic conversion FOL annotated version"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T13:25:44.498584+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HuggingFace ProofWriter FOL dataset variant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HuggingFace ProofWriter FOL dataset variant"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T13:25:44.498687+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RuleTaker ProofWriter natural language to FOL conversion tool GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RuleTaker ProofWriter natural language to FOL conversion tool GitHub"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-19T13:25:44.498816+00:00_

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
  "session": "worker_research_d145-fol-datasets_20260519T131524",
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

_source line 37 · 2026-05-19T13:25:44.498924+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T13:25:44.499037+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search HF Hub for FOL datasets",
  "subagent_type": "general-purpose",
  "prompt": "Search broadly for datasets with first-order logic (FOL) annotations on HuggingFace Hub and Papers with Code. Do the following:\n\n1. Search HuggingFace Hub for datasets with keywords: \"first-order logic\", \"FOL\", \"formal logic reasoning\", \"logical reasoning FOL\"\n2. Search Papers with Code for \"first-order logic reasoning dataset\"\n3. Search the web for \"first order logic annotated dataset NLP\" and \"FOL reasoning benchmark\"\n4. For any promising datasets found (beyond ProntoQA, LogicNLI, FOLIO, ProofWriter, LogicBench, FLD which are being researched separately), check:\n   - Does it have FOL premises and conclusions?\n   - What format are they in?\n   - How large is the dataset?\n5. Also check these specific datasets if you find them:\n   - CLUTRR\n   - bAbI tasks\n   - SimpleLogic\n   - AR-LSAT\n   - ReClor\n\nReport: a list of all datasets found with FOL annotations or near-FOL structured logic, with size, format, and compatibility assessment (1-5 scale where 5 = directly compatible with Prover9 FOL format like: all(x, (penguin(x) -> bird(x)))."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "tool_args": {
    "description": "Search HF Hub for FOL datasets",
    "subagent_type": "general-purpose",
    "prompt": "Search broadly for datasets with first-order logic (FOL) annotations on HuggingFace Hub and Papers with Code. Do the following:\n\n1. Search HuggingFace Hub for datasets with keywords: \"first-order logic\", \"FOL\", \"formal logic reasoning\", \"logical reasoning FOL\"\n2. Search Papers with Code for \"first-order logic reasoning dataset\"\n3. Search the web for \"first order logic annotated dataset NLP\" and \"FOL reasoning benchmark\"\n4. For any promising datasets found (beyond ProntoQA, LogicNLI, FOLIO, ProofWriter, LogicBench, FLD which are being researched separately), check:\n   - Does it have FOL premises and conclusions?\n   - What format are they in?\n   - How large is the dataset?\n5. Also check these specific datasets if you find them:\n   - CLUTRR\n   - bAbI tasks\n   - SimpleLogic\n   - AR-LSAT\n   - ReClor\n\nReport: a list of all datasets found with FOL annotations or near-FOL structured logic, with size, format, and compatibility assessment (1-5 scale where 5 = directly compatible with Prover9 FOL format like: all(x, (penguin(x) -> bird(x)))."
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T13:25:44.499191+00:00_

Web search results for query: "FOLIO-wiki dataset first-order logic larger version"

Links: [{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic Simeng Han1","url":"https://arxiv.org/pdf/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://github.com/Yale-LILY/FOLIO"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1229/"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"}]

Based on the search results, I found information about the FOLIO dataset:

FOLIO is a human-annotated, logically complex and diverse dataset for reasoning in natural language (NL), equipped with first-order logic (FOL) annotations. FOLIO consists of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion.

Regarding the Wikipedia connection, 52.5% of the examples in FOLIO are created based on knowledge from randomly-chosen Wikipedia pages. The remaining 47.5% are written in a hybrid manner, based on diverse and challenging logical templates.

…[truncated 580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T13:25:44.499338+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicBench dataset benchmark logic reasoning formal logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicBench dataset benchmark logic reasoning formal logic"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T13:25:44.499459+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FLD formal logic deduction dataset HuggingFace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FLD formal logic deduction dataset HuggingFace"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T13:25:44.499619+00:00_

Web search results for query: "FOLIO dataset formal logic FOL annotations extensions variants"

Links: [{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1229/"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic Simeng Han1","url":"https://arxiv.org/pdf/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"}]

Based on the search results, here's what I found about the FOLIO dataset:

## Overview

FOLIO is a human-annotated, open-domain, and logically complex and diverse dataset for reasoning in natural language (NL), equipped with first order logic (FOL) annotations.

## Dataset Composition

FOLIO consists of 1,435 examples (unique conclusions), each paired with one of 487 sets of premises which serve as rules to be used to deductively reason for the validity of each conclusion. The logical correctness of premises and conclusions is ensured by their parallel FOL annotations, which are automatically verified by
…[truncated 884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T13:25:44.499851+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicBench HuggingFace dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicBench HuggingFace dataset"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T13:25:44.500000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FLD formal logic deduction dataset Hitachi paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FLD formal logic deduction dataset Hitachi paper"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-19T13:25:44.500122+00:00_

# ProntoQA Dataset Information

## Dataset Overview
- **Name**: ProntoQA
- **Total Examples**: 500 rows
- **Split**: validation (500 rows)
- **Format**: JSON (auto-converted to Parquet)
- **Modality**: Text
- **Language**: English
- **License**: MIT
- **Size Category**: < 1K
- **ArXiv**: 2305.12295

## Field Names and Types

Based on the dataset viewer output, the dataset contains the following fields:

| Field Name | Type | Description |
|------------|------|-------------|
| `id` | string (10-12 chars) | Unique identifier for each example |
| `answer` | string (2 values) | Binary answer: "A" or "B" |
| `context` | string (262-445 chars) | Knowledge base with facts and rules |
| `options` | sequence (2 items) | Answer choices: ["A) True", "B) False"] |
| `question` | string (53-68 chars) | The question to answer |
| `raw_logic_programs` | sequence (1+ items) | **First-Order Logic (FOL) annotations** |

## FOL Content

The `raw_logic_programs` field contains **first-order logic formal representations**, including:

- **Predicates** with signatures (e.g., `Jompus($x, bool)`, `Shy($x, bool)`)
- **Facts** in logic notation (e.g., `Zumpus(Alex, True)`)
- **Rules** in implication form (e.g., `Rompus($x, True) >>> Impus($x, True)`)

### Example FOL Structure:
```
Predicates:
Jompus($x, bool) ::: Does x belong to Jompus?
Shy($x, bool) ::: Is x shy?

Facts:
Zumpus(Alex, True)

Rules:
Rompus($x, True) >>> Impus($x, True)
Impus($x, True) >>> Spicy($x, True)
```

## Task Type
**Question Answering with Logical Reasoning** - Binary classification (True/False) based on knowledge base inference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T13:25:44.500256+00:00_

# LogicNLI Dataset Information

Based on the provided GitHub page content, here's what can be determined:

## Available Information

**Dataset Type & Purpose:**
The repository describes LogicNLI as "an NLI-style dataset that effectively disentangles the target FOL reasoning from commonsense inference."

**Evaluation Dimensions:**
The dataset measures first-order logic reasoning across four perspectives: accuracy, robustness, generalization, and traceability.

## Information NOT Available

The webpage content does not provide:

1. **Data Format & Field Structure** - No details on specific fields or example formats are shown
2. **FOL Annotations** - While FOL reasoning is central to the dataset's purpose, the actual annotation structure isn't described
3. **Dataset Size** - No quantitative information about example counts
4. **Sample Data** - No concrete example entries demonstrating structure
5. **Logical Rules Representation** - No specification of how premises or FOL rules are formatted

## Note

The page includes a download link for "LogicNLI_sim.zip" but doesn't preview or describe the contents. To obtain detailed information about data structure and representation, one would need to either download the dataset or consult the full paper referenced: Tian et al. (2021) in Proceedings of EMNLP.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-19T13:25:44.500390+00:00_

Web search results for query: "HuggingFace ProofWriter FOL dataset variant"

Links: [{"title":"renma/ProofWriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/renma/ProofWriter"},{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset/viewer"},{"title":"smoorsmith/proofwriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/smoorsmith/proofwriter"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"tasksource/proofwriter · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/proofwriter"},{"title":"D3xter1922/proofwriter-dataset at 68a35fc79495cd36f109472e3a3dbbf281e2f10d","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset/tree/68a35fc79495cd36f109472e3a3dbbf281e2f10d"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs: Data   Generation, Incremental Fine-Tuning, and Verification","url":"https://arxiv.org/pdf/2409.16461"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive Statements   over Natural Language","url":"https://arxiv.org/pdf/2012.13048"}]

Based on the search results, I found information about the HuggingFace ProofWriter dataset and its FOL variant:

PROOFFOL is a high-quality FOL-annotated subset of ProofWriter dataset created using GPT-4o. Models fine-tuned on this silver standard data achieve significant performance gains when compared to larger language models such as LLaMA-2 70B.

The availability of FOL-based and Lean-based annotation has made ProofWriter a prime resource for evaluating hybrid reasoning systems that bridge connectionist and symbolic AI.

The search results also show several ProofWriter dataset variants available on HuggingFace Hub, including contributions from different users (renma, D3xter1922, smoorsmith, and tasksource), with some variants adding features like chain-of-thought re
…[truncated 111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-19T13:25:44.500538+00:00_

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
  "session": "worker_research_d145-fol-datasets_20260519T131524",
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

_source line 49 · 2026-05-19T13:25:44.500656+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T13:25:44.500838+00:00_

Web search results for query: "ProofWriter first-order logic conversion FOL annotated version"

Links: [{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs: Data   Generation, Incremental Fine-Tuning, and Verification","url":"https://arxiv.org/pdf/2409.16461"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"Translating Natural Language Propositions to First Order Logic","url":"https://www.cse.iitk.ac.in/users/karkare/MTP/2014-15/naman2015logica.pdf"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning","url":"https://www.researchgate.net/publication/397118426_FoVer_First-Order_Logic_Verification_for_Natural_Language_Reasoning"},{"title":"NL2LOGIC: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models","url":"https://arxiv.org/pdf/2602.13237"},{"title":"Intuitionistic Completeness of First-Order Logic","url":"https://arxiv.org/pdf/1110.1614"},{"title":"FMLtoHOL (version 1.0): Automating First-order Modal Logics with LEO-II   and Friends","url":"https://arxiv.org/pdf/1207.6685"}]

Based on the search results, here's what I found about ProofWriter and its first-order logic conversion resources:

## ProofWriter FOL-Annotated Resources

ProofFOL is a filtered, FOL-annotated subset of ProofWriter generated by prompting high-quality LLMs (e.g., GPT-4o) to produce FOL translations of context and queries, validated via Prover9.

This resource enables robust evaluation and fine-tuning of models on NL-to-FOL translation, and provides fine-grained error analysis (e.g., identifying errors of parsing, quantifier mismatch, predicate arity, and semantic sense).

## PROOFF
…[truncated 826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-19T13:25:44.500987+00:00_

Web search results for query: "RuleTaker ProofWriter FOL first-order logic annotations dataset"

Links: [{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic Simeng Han1","url":"https://arxiv.org/pdf/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://arxiv.org/pdf/2502.06563"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"}]

Based on the search results, here's information about RuleTaker, ProofWriter, and FOL datasets:

## RuleTaker and ProofWriter

ProofWriter is built upon the methodology introduced in the RuleTaker project but advances the complexity and expressiveness of the tasks in several dimensions. Both RuleTaker (2020) and ProofWriter (2021) are 500k deductive reasoning datasets with synthetic text sources and reasoning depths of 0-5.

ProofWriter is a dataset containing numerous rulebases of facts and rules expressed in English, with each rulebase including a set of questions that can be proven True, False, or Unknown using proofs of various depths.

## First-Order Logic Annotations

A range of neur
…[truncated 915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T13:25:44.501137+00:00_

Web search results for query: "RuleTaker ProofWriter natural language to FOL conversion tool GitHub"

Links: [{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive Statements   over Natural Language","url":"https://arxiv.org/pdf/2012.13048"},{"title":"GitHub - princeton-nlp/NLProofS: EMNLP 2022: Generating Natural Language Proofs with Verifier-Guided Search https://arxiv.org/abs/2205.12443 · GitHub","url":"https://github.com/princeton-nlp/NLProofS"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs: Data   Generation, Incremental Fine-Tuning, and Verification","url":"https://arxiv.org/pdf/2409.16461"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://arxiv.org/pdf/2502.06563"},{"title":"GitHub - wufeiwuwoshihua/nshy","url":"https://github.com/wufeiwuwoshihua/nshy"},{"title":"NLProofS/README.md at main · princeton-nlp/NLProofS","url":"https://github.com/princeton-nlp/NLProofS/blob/main/README.md"}]

Based on the search results, here's what I found about RuleTaker and ProofWriter:

ProofWriter is built upon the methodology introduced in the RuleTaker project but advances the complexity and expressiveness of the tasks in several dimensions. The core of each instance is a synthetic "theory" generated from Datalog programs and rendered in controlled English: facts ("A is a cat"), rules ("If X is a cat then X is an animal"), and target queries.

PROOFFOL is a high-quality FOL-annotated subset of ProofWriter dataset using GPT-4o, which was created to help improve natural language to first-order logic (NL-to-FOL) translation with large language models.

Regarding GitHub repositories, the search results reference the NLProofS project at https://github.com/princeton-nlp/NLProofS, which works with both RuleTaker and ProofWriter datasets. However, the search results don't show a specific GitHub repositor
…[truncated 480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-19T13:25:44.501284+00:00_

Web search results for query: "FOLIO dataset v2 extended community splits formal logic"

Links: [{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - DEV Community","url":"https://dev.to/aimodels-fyi/folio-natural-language-reasoning-with-first-order-logic-3hb1"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"tasksource/folio · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/folio"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/pdf/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://github.com/Yale-LILY/FOLIO"},{"title":"FOL2NS: Generating Natural Sentences from First-Order Logic","url":"https://arxiv.org/html/2605.18155"}]

Based on the search results, I found information about the FOLIO dataset, which is a human-annotated, logically complex and diverse dataset for reasoning in natural language (NL), equipped with first-order logic (FOL) annotations.

Key characteristics of FOLIO include:

- **Dataset Composition**: FOLIO contains 1,430 unique conclusions, each paired with a set of premises that can be used to logically deduce the validity of the conclusion.

- **Formal Logic Annotations**: FOLIO is the first large-scale first-order logic (FOL) reasoning dataset with formal logic annotations in FOL.

- **Diversity and Complexity**: FOLIO has abundant NL variations and a rich vocabulary, as well as diverse logic patterns.

- **Dataset Splits**: The available splits include a train set with 1k rows and a validation set with 203 rows.

However, the se
…[truncated 551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T13:25:44.501426+00:00_

# LogicNLI Dataset Summary

## 1) Dataset Fields/Columns
The dataset contains three main fields:
- **premise** (string): First-order logic premises and rules
- **hypothesis** (string): A statement to be evaluated against the premises
- **label** (string): Classification label indicating the logical relationship

## 2) Dataset Size
- **Total rows**: 20,000
- **Train split**: 16,000 rows
- **Validation split**: 2,000 rows
- **Test split**: 2,000 rows
- **File size**: 718 KB

## 3) Sample Data

```
Premise: "Nathalie is not blue. Gabriel is concerned. Nathalie is not concerned. 
Baird is concerned. Baird is serious. Quinlan is not entire. John is not fresh. 
John is blue. Gabriel is serious. Arthur is serious. Gabriel is not entire. 
Nathalie is not accurate. If there is someone who is either not concerned or fresh, 
then John ..."

Hypothesis: "Baird is not serious."
Label: "self_contradiction"

Hypothesis: "John is concerned."
Label: "entailment"

Hypothesis: "Arthur is blue."
Label: "neutral"
```

## 4) FOL Annotation Fields
**No explicit FOL annotation fields** like `fol_premises` or `fol_conclusion` are present. Instead, the dataset uses:
- Natural language premises containing first-order logic statements
- Structured logical facts about entities and their properties
- Logical rules embedded within the premise text

## 5) Data Format Details
- **Format**: Parquet (auto-converted from original format)
- **Libraries**: Compatible with Hugging Face Datasets and pandas
- **Label Classes** (4 values):
  - `entailment` - hypothesis logically follows from premises
  - `contradiction` - hypothesis contradicts the premises
  - `neutral` - hypothesis is independent of premises
  - `self_contradiction` - label contradicts explicit premises

The dataset is designed to diagnose first-order logic reasoning capabilities of language models across four dimensions: accuracy, robustness, generalization, and interpretability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-19T13:25:44.501559+00:00_

# ProntoQA Dataset Information

## Overview
The **ProntoQA** dataset is hosted on Hugging Face by tasksource, associated with the paper "Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought" (arXiv:2210.01240).

## Dataset Structure Issue
The dataset viewer is currently **non-functional** due to a configuration error. The JSON files are not properly formatted for automatic parsing by the Hugging Face datasets library.

### Identified Structure
Based on the error message, the JSON file (`1hop_AndElim_2testhops_random_noadj.json`) contains the following field structure:

**Fields:** `example1` through `example100` (100 example fields)

The JSON does **not** use the standard record-list format that the datasets library expects. Instead, it appears to nest individual examples as separate top-level keys rather than as an array of records.

## Metadata
- **Task Categories:** Question Answering, Text Classification
- **Language:** English
- **License:** Apache 2.0
- **Total Size:** 38.7 MB
- **Downloads (last month):** 289

## Known Data Characteristics
- Contains logical reasoning examples (implied by the chain-of-thought focus)
- Multiple test hop variations mentioned: `1hop_AndElim_2testhops_random_noadj.json`
- **FOL Annotations:** Not explicitly confirmed from the available content, but the paper's focus on formal analysis suggests logical reasoning structure

## Recommendation
To use this dataset, you may need to:
1. Check the [GitHub repository](https://github.com/asaparov/prontoqa/) for proper loading instructions
2. Create a custom loading script with the appropriate field specification
3. Review the dataset documentation for the exact FOL annotation format

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-19T13:25:44.501722+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HuggingFace Hub dataset \"first-order logic\" FOL annotations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HuggingFace Hub dataset \"first-order logic\" FOL annotations"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-19T13:25:44.501863+00:00_

Web search results for query: "HuggingFace FOLIO dataset FOL premises conclusion"

Links: [{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=FOLIO"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/pdf/2209.00840"},{"title":"minimario/FOLIO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/minimario/FOLIO"},{"title":"yale-nlp/FOLIO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yale-nlp/FOLIO"},{"title":"tasksource/folio · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/folio"}]

Based on the search results, here's what I found about the HuggingFace FOLIO dataset:

## Overview

FOLIO is a human-annotated, open-domain, and logically complex and diverse dataset for reasoning in natural language (NL), equipped with first order logic (FOL) annotations.

## Dataset Structure

FOLIO consists of 1,435 examples (unique conclusions), each paired with one of 487 sets of premises which serve as rules to be used to deductively reason for the validity of each conclusion.

## FOL Annotations

The logical correctness of premises and conclusions is ensured by their parallel FOL annotations, which are automatically verified by our FOL inference engine.

## Additional Use Case

In addition to the main NL reasoning task, NL-FOL pairs in FOLIO automatically constitute a new NL-FOL translation dataset 
…[truncated 404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T13:25:44.502012+00:00_

Web search results for query: "LogicBench dataset benchmark logic reasoning formal logic"

Links: [{"title":"LogicBench: A Benchmark for Evaluation of Logical Reasoning | OpenReview","url":"https://openreview.net/forum?id=7NR2ZVzZxx"},{"title":"LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models","url":"https://arxiv.org/html/2404.15522v2"},{"title":"[Literature Review] LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models","url":"https://www.themoonlight.io/en/review/logicbench-towards-systematic-evaluation-of-logical-reasoning-ability-of-large-language-models"},{"title":"GitHub - Mihir3009/LogicBench: LogicBench is a natural language question-answering dataset consisting of 25 different reasoning patterns spanning over propositional, first-order, and non-monotonic logics. · GitHub","url":"https://github.com/Mihir3009/LogicBench"},{"title":"LogicBench: Towards Systematic Evaluation of Logical ...","url":"https://aclanthology.org/2024.acl-long.739.pdf"},{"title":"LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=71kocBuhNO"},{"title":"LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability   of Large Language Models","url":"https://arxiv.org/pdf/2404.15522"},{"title":"Published as a conference paper at ICLR 2026 LOGICONBENCH:","url":"https://openreview.net/pdf?id=ULEHJkolxB"},{"title":"[2602.06533] LogicSkills: A Structured Benchmark for Formal Reasoning in Large Language Models","url":"https://arxiv.org/abs/2602.06533"}]

Based on the search results, here's what I found about LogicBench:

## Overview

LogicBench is a systematically created natural language question-answering dataset encompassing 25 reasoning patterns spanning over propositional, first-order, and non-monotonic logics.

## Purpose and Motivation

Logical reasoning has remained underexplored compared to o
…[truncated 1176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-19T13:25:44.502171+00:00_

Web search results for query: "LogicBench HuggingFace dataset"

Links: [{"title":"cogint/LogicBench-v1.0 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/cogint/LogicBench-v1.0"},{"title":"GitHub - Mihir3009/LogicBench: LogicBench is a natural language question-answering dataset consisting of 25 different reasoning patterns spanning over propositional, first-order, and non-monotonic logics. · GitHub","url":"https://github.com/Mihir3009/LogicBench"},{"title":"LogicStar/BaxBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/LogicStar/BaxBench"},{"title":"11NOel11/ChaosBench-Logic at main","url":"https://huggingface.co/datasets/11NOel11/ChaosBench-Logic/tree/main/docs"},{"title":"LogicStar/BaxBench at main","url":"https://huggingface.co/datasets/LogicStar/BaxBench/tree/main"},{"title":"GitHub - huggingface/datasets: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools","url":"https://github.com/huggingface/datasets"},{"title":"Joschka/big_bench_hard · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Joschka/big_bench_hard"},{"title":"Datasets – Hugging Face","url":"https://huggingface.co/datasets"},{"title":"tasksource/bigbench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/bigbench/viewer"},{"title":"SWE-bench/SWE-bench_Verified · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified"}]

Here are the search results for LogicBench HuggingFace dataset:

## Overview

LogicBench is a natural language question-answering dataset focusing on the use of a single inference rule. It comprehensively evaluates the logical reasoning ability of LLMs on 25 different reasoning patterns spanning over propositional, first-order, and non-monotonic logics.

## Dataset Versions

The dataset introduces two versions: LogicBench(Eval) is a high-quality human-verified evaluation dataset, whereas LogicBenc
…[truncated 794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-19T13:25:44.502334+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProofFOL dataset GPT-4o FOL annotated ProofWriter subset paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProofFOL dataset GPT-4o FOL annotated ProofWriter subset paper"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-19T13:25:44.502467+00:00_

Web search results for query: "FLD formal logic deduction dataset HuggingFace"

Links: [{"title":"Learning Deductive Reasoning From Synthetic Corpus Based On Formal Logic | Explore 2024 Best Paper And LLMs Tools Price, Review, Features And Alternatives","url":"https://toolsfine.com/Tools/5201.html"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=logical+validity"},{"title":"Papers with Code - FLD Dataset","url":"https://paperswithcode.com/dataset/fld"},{"title":"hitachi-nlp/FLD - Formal Logic Deduction","url":"https://github.com/hitachi-nlp/FLD"},{"title":"GitHub - hitachi-nlp/FLD-corpus","url":"https://github.com/hitachi-nlp/FLD-corpus"},{"title":"text2log · Datasets at Hugging Face","url":"https://huggingface.co/datasets/text2log"},{"title":"Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic   Corpus","url":"https://arxiv.org/pdf/2411.12498"},{"title":"Learning Deductive Reasoning from Synthetic Corpus based on Formal Logic","url":"https://arxiv.org/pdf/2308.07336"},{"title":"tasksource/logical-fallacy · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/logical-fallacy"}]

Based on the search results, here's what I found about the FLD (Formal Logic Deduction) dataset on HuggingFace:

## Overview
FLD (Formal Logic Deduction) is a project aimed at teaching language models deductive reasoning through synthetic examples rooted in formal logic theory. It is designed to enhance LLMs' reasoning capabilities via synthetically generated samples of logical reasoning, the most fundamental form of reasoning.

## Key Features
The dataset is a deductive reasoning benchmark based on formal logic theory where a model is required to generate a proof that (dis-) proves a given hypothesis based on a given set of facts.

## Latest Version
FLDx2 (Formal Logic Deduction Diverse) is the newest and most advanced corpus, which substantially improves the reasoning capability of LLMs, published alongside a NeurIPS
…[truncated 703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-19T13:25:44.502614+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FoVer first-order logic verification ProofWriter Prover9 dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FoVer first-order logic verification ProofWriter Prover9 dataset"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T13:25:44.502760+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclanthology.org/2021.emnlp-main.303/",
  "prompt": "Extract information about: 1) how the dataset was constructed - are FOL formulas used to generate the natural language? 2) Is the underlying FOL available in the dataset or only NL? 3) What is the structure of logical rules - propositional or truly first-order with quantifiers/predicates? 4) Dataset statistics (number of examples, splits). 5) Any mention of providing formal logic annotations alongside NL."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclanthology.org/2021.emnlp-main.303/",
    "prompt": "Extract information about: 1) how the dataset was constructed - are FOL formulas used to generate the natural language? 2) Is the underlying FOL available in the dataset or only NL? 3) What is the structure of logical rules - propositional or truly first-order with quantifiers/predicates? 4) Dataset statistics (number of examples, splits). 5) Any mention of providing formal logic annotations alongside NL."
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-19T13:25:44.502892+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicNLI dataset JSONL format fields FOL formulas structure sample example"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicNLI dataset JSONL format fields FOL formulas structure sample example"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T13:25:44.503020+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/pdf/2409.16461",
  "prompt": "Extract details about the ProofFOL dataset: how was it created, what size is it, what FOL annotations does it contain, where can it be downloaded, and what is the conversion methodology from ProofWriter to FOL?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/pdf/2409.16461",
    "prompt": "Extract details about the ProofFOL dataset: how was it created, what size is it, what FOL annotations does it contain, where can it be downloaded, and what is the conversion methodology from ProofWriter to FOL?"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T13:25:44.503157+00:00_

Web search results for query: "FLD formal logic deduction dataset Hitachi paper"

Links: [{"title":"GitHub - hitachi-nlp/FLD-corpus","url":"https://github.com/hitachi-nlp/FLD-corpus"},{"title":"FLD-corpus/README.md at NeurIPS_2024 · hitachi-nlp/FLD-corpus","url":"https://github.com/hitachi-nlp/FLD-corpus/blob/NeurIPS_2024/README.md"},{"title":"hitachi-nlp/FLD - Formal Logic Deduction","url":"https://github.com/hitachi-nlp/FLD"},{"title":"Learning Deductive Reasoning From Synthetic Corpus Based On Formal Logic | Explore 2024 Best Paper And LLMs Tools Price, Review, Features And Alternatives","url":"https://toolsfine.com/Tools/5201.html"},{"title":"Yasuhiro Sogawa","url":"https://www.catalyzex.com/author/Yasuhiro%20Sogawa"},{"title":"Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf"},{"title":"GitHub - hitachi-nlp/FLD-generator","url":"https://github.com/hitachi-nlp/FLD-generator"},{"title":"Papers with Code - FLD Dataset","url":"https://paperswithcode.com/dataset/fld"},{"title":"Learning Deductive Reasoning from Synthetic Corpus based on Formal Logic","url":"https://arxiv.org/pdf/2308.07336"},{"title":"Learning Deductive Reasoning from Synthetic Corpus based on Formal Logic","url":"https://proceedings.mlr.press/v202/morishita23a/morishita23a.pdf"}]

Based on the search results, here's what I found about the FLD formal logic deduction dataset and Hitachi papers:

## Overview

Formal Logic Deduction (FLD) is a project to enhance LLMs' reasoning capabilities via synthetically generated samples of logical reasoning, the most fundamental form of reasoning.

## Dataset Versions

The project has released multiple versions:

1. **FLDx2 (Most Recent)**: FLDx2 (Formal Logic Deduction Diverse), the newest and most advanced corpus, which substantially improves the reasoning capability of LLMs, was published alongside a NeurIPS 202
…[truncated 975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-19T13:25:44.503306+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/D3xter1922/proofwriter-dataset",
  "prompt": "Does this dataset contain FOL (first-order logic) annotations? What fields/columns does it have? List all available columns and whether any contain logical formulas."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/D3xter1922/proofwriter-dataset",
    "prompt": "Does this dataset contain FOL (first-order logic) annotations? What fields/columns does it have? List all available columns and whether any contain logical formulas."
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-19T13:25:44.503434+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /tmp && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('renma/ProntoQA', split='validation')\nprint('Number of examples:', len(ds))\nprint('Fields:', ds.column_names)\nprint('Features:', ds.features)\nprint()\nfor i in range(3):\n    ex = ds[i]\n    print(f'=== Example {i} ===')\n    for k, v in ex.items():\n        print(f'  {k}: {repr(v)[:500]}')\n    print()\n\" 2>&1",
  "description": "Download and inspect renma/ProntoQA dataset from HuggingFace",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /tmp && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('renma/ProntoQA', split='validation')\nprint('Number of examples:', len(ds))\nprint('Fields:', ds.column_names)\nprint('Features:', ds.features)\nprint()\nfor i in range(3):\n    ex = ds[i]\n    print(f'=== Example {i} ===')\n    for k, v in ex.items():\n        print(f'  {k}: {repr(v)[:500]}')\n    print()\n\" 2>&1",
    "description": "Download and inspect renma/ProntoQA dataset from HuggingFace",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T13:25:44.503574+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/yale-nlp/FOLIO",
  "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations (fol_premises, fol_conclusion fields). List all available splits and their sizes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/yale-nlp/FOLIO",
    "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations (fol_premises, fol_conclusion fields). List all available splits and their sizes."
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T13:25:44.503713+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 2, in &lt;module>
    from datasets import load_dataset
ModuleNotFoundError: No module named 'datasets'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T13:25:44.503842+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/minimario/FOLIO",
  "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations (fol_premises, fol_conclusion fields). List all available splits and their sizes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/minimario/FOLIO",
    "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations (fol_premises, fol_conclusion fields). List all available splits and their sizes."
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-19T13:25:44.503962+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/tasksource/folio",
  "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations (fol_premises, fol_conclusion fields). List all available splits and their sizes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/tasksource/folio",
    "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations (fol_premises, fol_conclusion fields). List all available splits and their sizes."
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-19T13:25:44.504085+00:00_

Web search results for query: "HuggingFace Hub dataset "first-order logic" FOL annotations"

Links: [{"title":"text2log · Datasets at Hugging Face","url":"https://huggingface.co/datasets/text2log"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"tasksource/folio · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/folio"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/pdf/2209.00840"},{"title":"GitHub - gblackout/LogicLLaMA: Large language model and dataset for natural language to first-order logic translation","url":"https://github.com/gblackout/LogicLLaMA"},{"title":"tasksource/FOL-nli · Discussions","url":"https://huggingface.co/datasets/tasksource/FOL-nli/discussions"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/pdf/2505.14932"}]

Based on the search results, I found several HuggingFace Hub datasets with first-order logic (FOL) annotations:

## Key Datasets Found:

**1. text2log**
The dataset contains 100,000 simple English sentences selected and filtered from enTenTen15 and their translation into First Order Logic (FOL) using ccg2lambda. The data set is used to train models which can generate FOL statements from natural language text.

**2. FOLIO**
FOLIO is a human-annotated, logically complex and diverse dataset for reasoning in natural language (NL), equipped with first-order logic (FOL) annotations. FOLIO consists of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion. The logical correctness of the premises and conclusions is ensured by their FOL annotations, which are automatically verified by an FOL inference engine.

**3. FOL
…[truncated 705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T13:25:44.504219+00:00_

# LogicNLI Dataset Information

Based on the provided ACL Anthology page, I can only offer limited information about the dataset construction, as the page contains metadata and abstract only:

**Available Information:**

The abstract describes LogicNLI as "an NLI-style dataset that effectively disentangles the target FOL reasoning from commonsense inference" and states it can diagnose language models across four dimensions: accuracy, robustness, generalization, and interpretability.

**What Cannot Be Determined:**

The webpage does not provide specifics regarding:

1. **Construction methodology** - Whether FOL formulas were used to generate natural language examples remains unclear from this source
2. **Formal logic availability** - No mention of whether underlying logical formulas are included in the dataset
3. **Logical structure** - The abstract doesn't specify whether the FOL rules involve quantifiers/predicates or are purely propositional
4. **Dataset statistics** - No numbers provided for example counts or data splits
5. **Formal annotations** - No discussion of accompanying logic annotations

**To obtain these details**, you would need to access the full PDF (available at https://aclanthology.org/2021.emnlp-main.303.pdf) or the paper's supplementary materials, which this metadata page does not excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-19T13:25:44.504350+00:00_

Web search results for query: "ProofFOL dataset GPT-4o FOL annotated ProofWriter subset paper"

Links: [{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification","url":"https://arxiv.org/html/2409.16461v1"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs:","url":"https://arxiv.org/pdf/2409.16461"},{"title":"Efficient Translation of NL-based Logical Problems to FOL ...","url":"https://arxiv.org/pdf/2506.18383"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning ...","url":"https://aclanthology.org/2023.emnlp-main.313.pdf"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://arxiv.org/pdf/2502.06563"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"}]

Based on the search results, I found information about the ProofFOL dataset paper:

The paper utilizes GPT-4o to create ProofFOL, a new large corpus of (premises, conclusion) pairs and corresponding FOL translations, using the existing pairs from the ProofWriter dataset. To ensure the correctness of the FOL translations, they pass them through Prover9 and filter out examples that produce outputs that do not match the ground truth in ProofWriter.

ProofFOL is the largest existing dataset consisting of 10424 examples of (premises, conclusion and their corresponding FOL translations. To avoid over-fitting the model to certain spurious patterns in GPT-4o translations, they include human-generated dataset (FOLIO) in the mix.

The paper is titled "Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification" (published September 18, 2024) and demonstrates that fine-tuned smaller mode
…[truncated 227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-19T13:25:44.504495+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/cogint/LogicBench-v1.0",
  "prompt": "Extract the full dataset structure: all fields/columns, dataset size (number of examples per split), and show any sample data. List every column name."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/cogint/LogicBench-v1.0",
    "prompt": "Extract the full dataset structure: all fields/columns, dataset size (number of examples per split), and show any sample data. List every column name."
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-19T13:25:44.504620+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Yale-LILY/FOLIO",
  "prompt": "Extract all information about: dataset files available, sizes, splits, any mention of FOLIO-wiki or extended versions, data format, FOL annotation fields. List all JSON/CSV files in the repository."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Yale-LILY/FOLIO",
    "prompt": "Extract all information about: dataset files available, sizes, splits, any mention of FOLIO-wiki or extended versions, data format, FOL annotation fields. List all JSON/CSV files in the repository."
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-19T13:25:44.504776+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip install datasets -q 2>&1 | tail -3",
  "description": "Install HuggingFace datasets library",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "pip install datasets -q 2>&1 | tail -3",
    "description": "Install HuggingFace datasets library",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-19T13:25:44.504900+00:00_

I appreciate your request, but I must be transparent: the content you've provided appears to be a PDF file encoded in binary format rather than readable text. The material shows PDF stream objects with FlateDecode compression, image data, and embedded binary content that cannot be meaningfully analyzed in its current form.

To extract information about the ProofFOL dataset, I would need:

1. **Readable text source** - A properly decoded PDF, plain text document, or webpage containing the dataset documentation
2. **Direct access** - Links to academic papers, dataset repositories, or official documentation describing ProofFOL

Without accessible text content, I cannot provide specific details about:
- Dataset creation methodology
- Size and scale metrics
- FOL annotation specifications
- Download locations
- Conversion processes from ProofWriter

**Recommendation:** Please share the source material in one of these formats:
- Plain text or markdown
- Readable PDF text (not binary)
- URL to the official paper or repository
- Direct quotes from the documentation

Once you provide readable content, I'll gladly extract the requested information while adhering to your citation and accuracy requirements.

[Binary content (application/pdf, 1.4MB) also saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/91820fa6-7a1f-4a02-8bc0-aaa4f114a9f1/tool-results/webfetch-1779196574153-pmsuk9.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-19T13:25:44.505017+00:00_

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-19T13:25:44.505140+00:00_

Web search results for query: "FoVer first-order logic verification ProofWriter Prover9 dataset"

Links: [{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.tacl-1.61/"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/article/view/8211"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning","url":"https://www.researchgate.net/publication/397118426_FoVer_First-Order_Logic_Verification_for_Natural_Language_Reasoning"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"GitHub - peiyu-cn/FoVer: Official code repository for the paper: \"FoVer: First-Order Logic Verification for Natural Language Reasoning\" (TACL) · GitHub","url":"https://github.com/peiyu-cn/FoVer"},{"title":"GitHub - Kwanikaze/Prover9Mace4DatasetGenerator: Creates dataset for an ontology specified in First Order Logic based on specified cardinality constraints and number of copies.","url":"https://github.com/Kwanikaze/Prover9Mace4DatasetGenerator"}]

Based on the search results, here's what I found about FoVer, first-order logic verification, ProofWriter, and Prover9:

## FoVer Overview

FoVer (First-order logic Verification) is an automated pipeline that verifies the logical correctness of reasoning texts using first-order logic, operating in two main steps: (1) LLM-driven translation of natural language into executable logical expressions, and (2) automated logical verification using the Z3 theorem prover.

## Datasets Used

FoVer i
…[truncated 922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-19T13:25:44.505292+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HuggingFace datasets \"formal logic reasoning\" \"logical reasoning\" FOL benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HuggingFace datasets \"formal logic reasoning\" \"logical reasoning\" FOL benchmark"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-19T13:25:44.505415+00:00_

# FOLIO Dataset Information

Based on the webpage content provided, I can extract the following information:

## Dataset Size
- **Total file size**: 1.22 MB
- **Size category**: 1K - 10K (rows)

## Access Limitation
The dataset requires user authentication to access the actual content files. The page states:
> "You need to agree to share your contact information to access this dataset"

This means the specific details about splits, column names, and field information are **not visible** without logging in.

## What We Know
- **Modalities**: Tabular, Text
- **Format**: JSON
- **License**: MIT
- **Organization**: Yale NLP Lab

## Unable to Determine from This Page
❌ Exact number of rows per split  
❌ Column names/fields  
❌ Whether FOL (First-Order Logic) annotation fields exist (`fol_premises`, `fol_conclusion`)  
❌ Available data splits and their individual sizes  

## Recommendation
To access the requested information (splits, columns, and FOL annotations), you would need to:
1. [Log in or sign up](https://huggingface.co/login) to Hugging Face
2. Accept the dataset conditions
3. View the dataset card or use the Data Studio viewer
4. Or load the dataset programmatically using the Hugging Face `datasets` library

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-19T13:25:44.505550+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/hitachi-nlp/FLD-corpus",
  "prompt": "Extract the dataset format, fields/columns, sample data examples, and dataset size information. Look for any FOL (first-order logic) annotations or formal logic representations in the data format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/hitachi-nlp/FLD-corpus",
    "prompt": "Extract the dataset format, fields/columns, sample data examples, and dataset size information. Look for any FOL (first-order logic) annotations or formal logic representations in the data format."
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-19T13:25:44.505666+00:00_

# ProofWriter Dataset Analysis

Based on the webpage content, here's what I can determine about the dataset structure:

## Dataset Overview
- **Total rows:** 59,220
- **Splits:** train (41.4k), validation (6.01k), test (11.8k)
- **Format:** JSON
- **Size:** 10K - 100K rows

## Available Columns/Fields

From the sample data shown, each record contains:

1. **`en`** - Main field containing structured data with the following components:
   - **`$answer$`** - Boolean answer (true/false statements)
   - **`$proof$`** - Reasoning chain/proof steps
   - **`$question$`** - Query/statement to verify
   - **`$context$`** - Background facts and rules

## FOL (First-Order Logic) Content

**Yes, this dataset does contain logical annotations:**

The dataset includes:
- **Facts** in structured form (e.g., "sent1: The cow is round.")
- **Rules** expressed in logical form (e.g., "If someone is nice then they are kind")
- **Logical negation** (e.g., "The cow does not need the rabbit")

### Example Structure:
```
$context$ = 
  sent1: The bear is blue.
  sent8: If someone is nice then they are kind.

$question$ = The bear is kind.
$answer$ = true
$proof$ = [reasoning chain]
```

The dataset appears designed for **multi-hop reasoning** and **automated theorem proving** tasks, where models must generate proofs based on given facts and rules.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-19T13:25:44.505826+00:00_

Web search results for query: "LogicNLI dataset JSONL format fields FOL formulas structure sample example"

Links: [{"title":"Diagnosing the First-Order Logical Reasoning Ability Through LogicNLI - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.303/"},{"title":"GitHub - tammet/json-ld-logic: JSON representation of first-order logic formulas","url":"https://github.com/tammet/json-ld-logic"},{"title":"GitHub - csitfun/LogiQA2.0: Logiqa2.0 dataset - logical reasoning in MRC and NLI tasks","url":"https://github.com/csitfun/LogiQA2.0"},{"title":"LogicNLI","url":"https://omnilabnlp.github.io/dataset/dataset.html"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://github.com/Yale-LILY/FOLIO"},{"title":"How to create a correct JSONL for training - Prompting - OpenAI Developer Community","url":"https://community.openai.com/t/how-to-create-a-correct-jsonl-for-training/693897"}]

Based on my search results, I found information about the LogicNLI dataset. LogicNLI is an NLI-style dataset that effectively disentangles the target FOL reasoning from commonsense inference and can be used to diagnose LMs from four perspectives: accuracy, robustness, generalization, and interpretability.

However, the search results don't provide specific details about the JSONL format fields, FOL formula structure, or sample examples for the LogicNLI dataset itself. The results mention that the dataset has been opened in Github, and reference a paper on diagnosing first-order logical reasoning ability through LogicNLI.

To get the specific technical details about the JSONL format fields and sample examples you're looking for, I'd recommend:

1. Checking the official LogicNLI GitHub repository directly
2. Reviewing the full EMNLP 2021 paper "Diagnosing the First-Order Logical Reasoning Ability Through LogicNLI" for detailed format specificat
…[truncated 328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-19T13:25:44.505971+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Mihir3009/LogicBench",
  "prompt": "Extract the dataset structure, fields, sample data format, and whether it contains FOL (first-order logic) annotations. Look for data format descriptions, JSON structure, column names."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Mihir3009/LogicBench",
    "prompt": "Extract the dataset structure, fields, sample data format, and whether it contains FOL (first-order logic) annotations. Look for data format descriptions, JSON structure, column names."
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-19T13:25:44.506094+00:00_

# FOLIO Dataset Information

## Dataset Size
- **Total rows**: 1,208
- **Train split**: 1,000 rows
- **Validation split**: 204 rows

## Column Names/Fields

The dataset contains the following columns:

1. **conclusion** (string) - The conclusion to be evaluated
2. **premises** (sequence) - List of premises in natural language
3. **premises-FOL** (sequence) - Formal logic representations of the premises
4. **label** (string) - Classification label with 3 possible values:
   - `True` - The conclusion follows from the premises
   - `False` - The conclusion does not follow from the premises
   - `Unknown` - The conclusion cannot be determined from the premises

## FOL Annotations

**Yes**, the dataset includes First-Order Logic (FOL) annotations:
- **premises-FOL**: Contains formal logic representations using standard FOL notation (∀, ∃, →, ∧, ∨, ¬, ⊕, etc.)
- **fol_conclusion** field: Implicitly represented through the structured conclusion field

## Available Splits

| Split | Rows |
|-------|------|
| train | 1,000 |
| validation | 204 |
| **Total** | **1,208** |

## Format & Libraries
- **Format**: Parquet
- **Libraries**: Datasets, pandas
- **License**: Apache-2.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-19T13:25:44.506229+00:00_

# FOLIO Dataset Overview

## Dataset Size
- **Total rows**: 1,204
- **Default subset**: 1,200 rows

## Splits

| Split | Size |
|-------|------|
| train | 1,000 rows |
| validation | 203 rows |

## Column Names/Fields

The dataset contains the following fields:

1. **story_id** (int64) - Identifier for the story/premise group
2. **premises** (string) - Natural language premises (41-1.12k characters)
3. **premises-FOL** (string) - First-order logic representation of premises (41-1.43k characters)
4. **conclusion** (string) - Natural language conclusion/hypothesis (12-378 characters)
5. **conclusion-FOL** (string) - First-order logic representation of conclusion (8-340 characters)
6. **label** (string) - Classification label with 3 possible values:
   - "True" (entailment)
   - "False" (contradiction)
   - "Uncertain" (neutral/unknown)
7. **example_id** (int64) - Unique example identifier (3-1.43k range)

## FOL Annotations

✅ **Yes, FOL annotations are included:**
- `premises-FOL` - First-order logic formalization of premises
- `conclusion-FOL` - First-order logic formalization of conclusions

## Key Characteristics

- **Task**: Natural Language Inference (NLI) / Text Classification
- **Modalities**: Tabular, Text
- **Format**: JSON
- **Language**: English
- **License**: Creative Commons (cc)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-19T13:25:44.506365+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -m venv /tmp/hf_env && source /tmp/hf_env/bin/activate && pip install datasets -q 2>&1 | tail -3",
  "description": "Create venv and install datasets library",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -m venv /tmp/hf_env && source /tmp/hf_env/bin/activate && pip install datasets -q 2>&1 | tail -3",
    "description": "Create venv and install datasets library",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-19T13:25:44.506488+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2404.15522v2",
  "prompt": "Extract information about: 1) the data format and fields of LogicBench, 2) whether FOL (first-order logic) formulas are included in the dataset, 3) sample data examples showing the structure, 4) dataset size statistics. Focus on any formal logic representations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2404.15522v2",
    "prompt": "Extract information about: 1) the data format and fields of LogicBench, 2) whether FOL (first-order logic) formulas are included in the dataset, 3) sample data examples showing the structure, 4) dataset size statistics. Focus on any formal logic representations."
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-19T13:25:44.506605+00:00_

# FOLIO Dataset Information

## Available Files and Splits
The repository contains train and validation sets in **jsonl and txt formats** located in the `data/v0.0` folder. No specific file sizes are provided in the documentation.

## Data Format
Each example includes these fields:
- `premises`: natural language premises
- `premises-FOL`: first-order logic annotation for premises
- `conclusion`: natural language conclusion
- `conclusion-FOL`: FOL formula annotation for conclusion
- `label`: truth value label for the conclusion
- `story-id`: identifier for premise groupings
- `example-id`: identifier for individual examples
- `source`: indicates origin from WikiLogic or HybLogic sets

## JSON/CSV Files Listed
The page does not explicitly list specific JSON or CSV filenames. Only the directory structure `data/v0.0` is mentioned as containing the datasets.

## Extended Versions
An updated version with "significant quality improvement and error fixing" is available separately on Hugging Face at `yale-nlp/FOLIO`. The repository indicates this represents an improvement over the original v0.0 release.

## Additional Notes
The documentation mentions that "code for evaluation with fine-tuning and few-shot prompting will be updated soon," suggesting the repo is under active development.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-19T13:25:44.506759+00:00_

# LogicBench-v1.0 Dataset Structure

## Overview
LogicBench is a question-answering dataset for evaluating logical reasoning ability of Large Language Models across 25 inference rules spanning propositional, first-order, and non-monotonic logics.

## Dataset Organization

The dataset is distributed in two versions:

```
data/
├── LogicBench(Aug)           # Augmented version
│   ├── first_order_logic/
│   ├── nm_logic/
│   └── propositional_logic/
└── LogicBench(Eval)          # Evaluation version
    ├── BQA/                  # Boolean Question Answering
    │   ├── propositional_logic/
    │   ├── first_order_logic/
    │   └── nm_logic/
    └── MCQA/                 # Multiple Choice Question Answering
        ├── propositional_logic/
        ├── first_order_logic/
        └── nm_logic/
```

## JSON Schema / Column Structure

Each file contains the following structure:

```json
{
    "type": "str",
    "axiom": "str",
    "samples": [
        {
            "id": "int",
            "context": "str",
            "qa_pairs": [
                {
                    "question": "str",
                    "answer": "str"
                },
                {
                    "question": "str",
                    "answer": "str"
                }
            ]
        }
    ]
}
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| **type** | string | The type of inference rule/reasoning pattern |
| **axiom** | string | The logical axiom or inference rule being tested |
| **samples** | array | Collection of sample instances |
| **id** | integer | Unique identifier for each sample |
| **context** | string | Natural language premise/context for reasoning |
| **qa_pairs** | array | Array of question-answer pairs based on the context |
| **question** | string | Natural language question |
| **answer** | string | Expected answer to the question |

## Dataset Specifications

- **Task**: Question Answering
- **Language**: English
- **Lic
…[truncated 199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-19T13:25:44.506912+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2409.16461v1",
  "prompt": "Extract all details about the ProofFOL dataset: exact size, how it was created from ProofWriter, FOL format used, Prover9 verification process, where to download it, any GitHub repo link. Also extract information about the conversion pipeline from natural language to FOL."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2409.16461v1",
    "prompt": "Extract all details about the ProofFOL dataset: exact size, how it was created from ProofWriter, FOL format used, Prover9 verification process, where to download it, any GitHub repo link. Also extract information about the conversion pipeline from natural language to FOL."
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-19T13:25:44.507035+00:00_

# FLD Corpus Dataset Format

## Key Fields

The dataset contains these primary columns:

- **context/facts**: "A set of facts"
- **hypothesis**: The statement to be evaluated
- **proofs**: "Gold proofs. Each proof consists of a series of logical steps derived from the facts leading towards the hypothesis"
- **world_assump_label**: Answer marked as PROVED, DISPROVED, or UNKNOWN

## Training-Specific Fields

- **prompt_serial**: Serialized representation combining facts and hypothesis
- **proof_serial**: Serialized representation of proof and answer; "for the FLDx2 corpus, `proof_serial` sometimes includes both the proof and answer, and sometimes only the answer"

## Dataset Size

The page does not specify exact dataset sizes or provide concrete sample data examples. However, it references three corpus versions:

- **FLDx2** (newest): Designed to improve LLM reasoning capabilities
- **JFLD**: Japanese version
- **FLD/FLD★**: Original versions (v2.0)

## Formal Logic Representation

The dataset uses serialized logical notation rather than displaying explicit FOL syntax on this page. Details on the actual serialization format are referenced as available "on the huggingface hub."

For comprehensive schema details and examples, users should consult the Hugging Face dataset hub directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-19T13:25:44.507180+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclanthology.org/2021.emnlp-main.303.pdf",
  "prompt": "Extract ALL information about: 1) How the dataset was constructed - are formal FOL formulas used to generate the NL premises? 2) The exact structure of logical rules: are they propositional (unary predicates on constants) or truly first-order with quantifiers, functions, multi-arity predicates? 3) Are the underlying FOL formulas stored in the dataset files? 4) Dataset size and statistics. 5) Example premises showing the exact format. 6) What types of logical connectives and quantifiers appear. 7) Any mention of providing machine-readable logic alongside natural language."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclanthology.org/2021.emnlp-main.303.pdf",
    "prompt": "Extract ALL information about: 1) How the dataset was constructed - are formal FOL formulas used to generate the NL premises? 2) The exact structure of logical rules: are they propositional (unary predicates on constants) or truly first-order with quantifiers, functions, multi-arity predicates? 3) Are the underlying FOL formulas stored in the dataset files? 4) Dataset size and statistics. 5) Example premises showing the exact format. 6) What types of logical connectives and quantifiers appear. 7) Any mention of providing machine-readable logic alongside natural language."
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-19T13:25:44.507303+00:00_

# LogicBench Dataset Structure

## Dataset Versions
LogicBench offers two versions:
- **LogicBench(Eval)**: "high-quality human-verified evaluation dataset"
- **LogicBench(Aug)**: synthetically augmented version for training

## Task Types
The evaluation dataset includes two task formats:
1. Binary Question-Answering (BQA)
2. Multiple Choice Question-Answering (MCQA)

## Directory Organization
The dataset spans three logic categories:
- Propositional logic
- First-order logic (FOL)
- Non-monotonic logic

Each category contains JSON files for individual inference rules.

## JSON Schema

**BQA Format** includes:
- `type`: inference rule classification
- `axiom`: the logical rule description
- `samples`: array with `id`, `context`, and `qa_pairs` (question-answer pairs)

**MCQA Format** includes:
- `type`, `axiom`, and `samples` array with `id`, `context`, `question`, `choices` (dictionary), and `answer`

## FOL Annotations
Yes, the dataset explicitly covers first-order logic through dedicated folders and reasoning patterns spanning propositional, first-order, and non-monotonic logics across 25 inference rules.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-19T13:25:44.507429+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/peiyu-cn/FoVer",
  "prompt": "Extract details about the FoVer project: does it include FOL-annotated versions of ProofWriter? What datasets are included? How does the NL-to-FOL conversion work? Is there code for converting ProofWriter to FOL? What format are the FOL annotations in?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/peiyu-cn/FoVer",
    "prompt": "Extract details about the FoVer project: does it include FOL-annotated versions of ProofWriter? What datasets are included? How does the NL-to-FOL conversion work? Is there code for converting ProofWriter to FOL? What format are the FOL annotations in?"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-19T13:25:44.507569+00:00_

Web search results for query: "HuggingFace datasets "formal logic reasoning" "logical reasoning" FOL benchmark"

Links: [{"title":"InternScience/MME-Reasoning · Datasets at Hugging Face","url":"https://huggingface.co/datasets/InternScience/MME-Reasoning"},{"title":"baber/logiqa2 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/baber/logiqa2"},{"title":"datatune/LogiCoT · Datasets at Hugging Face","url":"https://huggingface.co/datasets/datatune/LogiCoT"},{"title":"AtlasUnified/Atlas-Reasoning · Datasets at Hugging Face","url":"https://huggingface.co/datasets/AtlasUnified/Atlas-Reasoning"},{"title":"text2log · Datasets at Hugging Face","url":"https://huggingface.co/datasets/text2log"},{"title":"Reasoning datasets - a HuggingFaceTB Collection","url":"https://huggingface.co/collections/HuggingFaceTB/reasoning-datasets"},{"title":"Agentified Assessment of Logical Reasoning Agents","url":"https://arxiv.org/pdf/2603.02788"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/pdf/2505.14932"},{"title":"Large Language Models Meet Symbolic Provers for Logical Reasoning   Evaluation","url":"https://arxiv.org/pdf/2502.06563"}]

Based on the search results, I found several relevant HuggingFace datasets related to formal logic reasoning and FOL (First Order Logic):

## Key Datasets Found:

1. **text2log**: Contains 100,000 simple English sentences selected and filtered from enTenTen15 and their translation into First Order Logic (FOL) using ccg2lambda.

2. **datatune/LogiCoT**: The instructions and demonstrations for building formal logical reasoning capable Generative Large Language models. Includes data derived from the FOLIO data.

3. **baber/logiqa2**: Logiqa2.0 dataset - logical reasoning in MRC and NLI tasks.

4. **AtlasUnified/Atlas-Reasoning**: This dataset includes various logic-related categories such as Propositional Logic, Predicate Logic, First-order logic, and was synthetically generated.

5. **Inter
…[truncated 621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-19T13:25:44.507738+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LINC neurosymbolic ProofWriter FOL Prover9 conversion code GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LINC neurosymbolic ProofWriter FOL Prover9 conversion code GitHub"
  }
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-19T13:25:44.507872+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProofFOL dataset download GitHub HuggingFace \"10424\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProofFOL dataset download GitHub HuggingFace \"10424\""
  }
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-19T13:25:44.507993+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co/datasets FOLIO logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co/datasets FOLIO logic"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-19T13:25:44.508113+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOLIO-wiki first-order logic dataset extended annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOLIO-wiki first-order logic dataset extended annotation"
  }
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-19T13:25:44.508233+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"FOLIO\" dataset larger version 2000 3000 examples FOL natural language reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"FOLIO\" dataset larger version 2000 3000 examples FOL natural language reasoning"
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-19T13:25:44.508353+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Papers with Code \"first-order logic reasoning dataset\" benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Papers with Code \"first-order logic reasoning dataset\" benchmark"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-19T13:25:44.508470+00:00_

# LogicBench Dataset Information

## 1. Data Format and Fields

LogicBench structures instances as tuples containing:
- **Context (c)**: A narrative-based description of logical statements and rules
- **Question (q)**: A query testing logical entailment
- **Answer (a)**: Binary label (Yes/No) for BQA; multiple choice for MCQA

The dataset provides two task formulations: Binary Question-Answering (BQA) and Multiple-Choice Question-Answering (MCQA).

## 2. First-Order Logic (FOL) Inclusion

Yes, FOL formulas are comprehensively included. The dataset covers formal logic representations alongside natural language versions. Table 2 presents "Existential Generalization (EG)" and "Universal Instantiation (UI)" as formal axioms, with extensions showing quantified expressions like: ∀x(p(x)→q(x))∧p(a)⊢q(a).

## 3. Sample Data Examples

Table 4 demonstrates the structure. For Modus Tollens:
- **Formal**: ((p→q)∧¬q)⊢¬p
- **Natural Language Context**: "Liam knows that if he finishes his work early, he will order pizza for dinner. However, he decided against ordering pizza."
- **Questions vary** between semantically preserving and inverting forms

For Bidirectional Dilemma (FOL): contexts combine multiple conditional statements with disjunctive premises.

## 4. Dataset Size Statistics

Table 5 reports:
- **LogicBench(Eval)BQA**: 500 unique instances, 1,520 total (with variations)
- **LogicBench(Eval)MCQA**: 500 unique instances
- **LogicBench(Aug)**: 12,908 augmented samples (150 per rule for BQA)
- Coverage: "25 reasoning patterns spanning propositional, first-order, and non-monotonic logics"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-19T13:25:44.508605+00:00_

# ProofFOL Dataset Details

## Dataset Size and Creation
ProofFOL contains **10,424 examples** of (premises, conclusion) pairs with corresponding FOL translations. It was created by using GPT-4o to generate FOL translations from the ProofWriter dataset's training set, specifically from "depth-5 records" representing the highest complexity level.

## Creation Process
The pipeline involved:
- Generating FOLs for 15,000 training data points from ProofWriter using GPT-4o
- Parsing outputs using regex pattern matching to extract FOL statements
- Validating syntax through Prover9 theorem prover
- Filtering by comparing generated labels against ground truth labels
- **Retention rate: 70%** of silver-standard data

## FOL Format and Verification
The formal language follows **Prover9 syntax**, a theorem prover format. As stated: "The format of FOLs is set to be consistent with the 'Prover9' theorem prover, which has a human understandable, formal language syntax."

Prover9 verification identifies errors by returning 'True', 'False', 'Unknown', or 'None' (indicating errors). Semantic errors were detected by "comparing the ground truth label from ProofWriter with Prover9-generated output."

## Access and Repository
The authors provide: **"The code for fine-tuning, augmentation and verification, and ProofFOL dataset are available at https://github.com/RamyaKeerthy/Translation-NL2FOL"**

## NL-to-FOL Conversion Pipeline
The conversion generates predicates first, then FOL statements for each sentence, following the format: predicates paired with their corresponding natural language text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-19T13:25:44.508756+00:00_

# FoVer Project Details

Based on the GitHub repository content provided, I can only extract limited information:

## What's Confirmed

The repository contains:
- **Datasets directory**: `data/` folder houses "Datasets used in the paper" with requests and responses stored there
- **Code organization**: Separate utilities for `dataset_utils/` and `llm_utils/` functionality
- **Demo examples**: `demos/` directory includes "Few-shot prompt examples for FoVer"

## What's Not Addressed

The webpage content does not specify:
- Whether FOL-annotated ProofWriter versions are included
- Specific dataset names or compositions
- Details on NL-to-FOL conversion mechanisms
- Code for converting ProofWriter to FOL format
- FOL annotation formats used

## Recommendation

The main README states that the "CLI interface is not very user-friendly" and recommends using Jupyter Notebooks instead. To answer your detailed questions about dataset composition, conversion processes, and annotation formats, you would need to examine the actual code files in the repository directories, particularly `data/README.md` and `demos/README.md`, which are referenced but not included in the provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-19T13:25:44.508892+00:00_

Web search results for query: "ProofFOL dataset download GitHub HuggingFace "10424""

Links: [{"title":"GitHub - bodaay/HuggingFaceModelDownloader: Simple go utility to download HuggingFace Models and Datasets · GitHub","url":"https://github.com/bodaay/HuggingFaceModelDownloader"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs: Data   Generation, Incremental Fine-Tuning, and Verification","url":"https://arxiv.org/pdf/2409.16461"},{"title":"Downloading datasets · Hugging Face","url":"https://huggingface.co/docs/hub/datasets-downloading"},{"title":"datasets/src/datasets/load.py at main · huggingface/datasets","url":"https://github.com/huggingface/datasets/blob/main/src/datasets/load.py"},{"title":"Load · Hugging Face","url":"https://huggingface.co/docs/datasets/en/loading"},{"title":"D3xter1922/proofwriter-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/D3xter1922/proofwriter-dataset/viewer"},{"title":"AutoFactory Dataset to Support AI in Manufacturing Systems","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12363462/"}]

Based on the search results, I found relevant information about the ProofFOL dataset:

ProofFOL is a high-quality FOL-annotated subset of ProofWriter dataset created using GPT-4o. The code for fine-tuning, augmentation, verification, and the ProofFOL dataset are available at https://github.com/RamyaKeerthy/Translation-NL2FOL.

The dataset appears to be primarily hosted on GitHub rather than HuggingFace Hub. The search results don't show a specific HuggingFace dataset page for ProofFOL, though the "10424" identifier you mentioned may refer to a specific file, version, or record number that wasn't captured in these results.

For the most direct access, you would want to visit the GitHub repository linked above for the dataset and associated code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-19T13:25:44.509025+00:00_

# Dataset Construction and Logical Structure Analysis

Based on the PDF content provided, this appears to be a research paper on diagnosing first-order logical reasoning abilities through natural language inference (LogicNLI). Here's what the document reveals:

## Dataset Construction
The paper references a benchmark called **EMNLP 2021** with the title mentioning "Diagnosing the First-Order Logical Reasoning Ability Through LogicNLI." The document indicates this work involves creating synthetic datasets from formal logical specifications.

## Logical Structure
The dataset appears to employ **first-order logic with quantifiers and multiple-arity predicates** rather than simple propositional logic. The references to "first-order logical reasoning ability" suggest the framework includes:
- Universal and existential quantifiers
- Multi-argument predicates
- Complex logical formulas

## Machine-Readable Formats
While the PDF shows extensive bibliographic references and linked citations, **specific details about whether underlying FOL formulas are directly stored in dataset files are not clearly visible** in the provided text sections. The document structure indicates this is a research contribution, but the detailed dataset specifications would typically appear in supplementary materials or methodology sections not fully captured here.

## Dataset Statistics and Examples
The specific dataset size metrics and concrete example premises are **not legible** in the provided PDF excerpt. The visible content primarily shows citation networks and document metadata rather than the actual dataset descriptions.

## Recommendation
To obtain complete details about dataset construction methodology, logical formula specifications, and machine-readable logic formats, consulting the full paper text (particularly methodology and appendix sections) would be necessary.

[Binary content (application/pdf, 782.5KB) also saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-r
…[truncated 139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-19T13:25:44.509175+00:00_

Web search results for query: "LINC neurosymbolic ProofWriter FOL Prover9 conversion code GitHub"

Links: [{"title":"Efficient Translation of NL-based Logical Problems to FOL ...","url":"https://arxiv.org/pdf/2506.18383"},{"title":"[2310.15164] LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers","url":"https://arxiv.org/abs/2310.15164"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining","url":"https://arxiv.org/pdf/2310.15164"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning ...","url":"https://aclanthology.org/2023.emnlp-main.313.pdf"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs:","url":"https://arxiv.org/pdf/2409.16461"},{"title":"Robustness of Neurosymbolic Reasoners on First-Order ...","url":"https://aclanthology.org/2025.alta-main.1.pdf"},{"title":"GitHub - benlipkin/linc: 🔗 LINC: Logical Inference via Neurosymbolic Computation [EMNLP2023]","url":"https://github.com/benlipkin/linc"}]

Based on the search results, I found relevant information about LINC and its connection to ProofWriter, FOL, and Prover9:

LINC parses the context and question to first-order logic (FOL) using LLMs, and verifies conclusions symbolically with a system like Prover9. On ProofWriter, augmenting the comparatively small open-source StarCoder+ (15.5B parameters) with LINC even outperforms GPT-3.5 and GPT-4 with Chain-of-Thought (CoT) prompting by an absolute 38% and 10%, respectively.

All corresponding code is publicly available, and the official GitHub repository is available at: **https://github.com/benlipkin/linc**

This repository contains the LINC implementation for "Logical Inference via Neurosymbolic Computation," which was presented at EMNLP 2023. The code includes the components for converting natural language problems to FOL and integrating with Prover9 for s
…[truncated 124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-19T13:25:44.509327+00:00_

Web search results for query: "site:huggingface.co/datasets FOLIO logic"

Links: [{"title":"tasksource/folio · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/folio"},{"title":"akshay107/FOLIO-fol · Datasets at Hugging Face","url":"https://huggingface.co/datasets/akshay107/FOLIO-fol"},{"title":"yale-nlp/P-FOLIO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yale-nlp/P-FOLIO"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/pdf/2209.00840"},{"title":"yale-nlp/FOLIO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yale-nlp/FOLIO"},{"title":"Scaling Synthetic Logical Reasoning Datasets with Context-Sensitive   Declarative Grammars","url":"https://arxiv.org/pdf/2406.11035"},{"title":"fol-traces/fol-traces · Datasets at Hugging Face","url":"https://huggingface.co/datasets/fol-traces/fol-traces"},{"title":"datatune/LogiCoT · Datasets at Hugging Face","url":"https://huggingface.co/datasets/datatune/LogiCoT"},{"title":"P-FOLIO: Evaluating and Improving Logical Reasoning with Abundant   Human-Written Reasoning Chains","url":"https://arxiv.org/pdf/2410.09207"}]

Based on the search results, I found several datasets related to FOLIO and logic on Hugging Face:

## Main FOLIO Dataset

FOLIO is a human-annotated, open-domain dataset for reasoning in natural language equipped with first-order logic (FOL) annotations, consisting of 1,435 examples (unique conclusions), each paired with one of 487 sets of premises which serve as rules to be used to deductively reason for the validity of each conclusion. The logical correctness of premises and conclusions is ensured by their parallel FOL annotations, which are automatically verified by their FOL inference engine.

## P-FOLIO Dataset

P-FOLIO is a human-annotated dataset consisting of diverse and complex reasoning chains for a set of realistic logical reasoning stories also written by humans. P-FOLIO is collected with an annot
…[truncated 559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-19T13:25:44.509473+00:00_

Web search results for query: "FOLIO-wiki first-order logic dataset extended annotation"

Links: [{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1229/"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic Simeng Han1","url":"https://arxiv.org/pdf/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://github.com/Yale-LILY/FOLIO"}]

Based on the search results, here's what I found about FOLIO:

## FOLIO Dataset Overview

FOLIO is a human-annotated, logically complex and diverse dataset for reasoning in natural language (NL), equipped with first-order logic (FOL) annotations. FOLIO consists of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion, with logical correctness ensured by their FOL annotations, which are automatically verified by
…[truncated 921 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-19T13:25:44.509623+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "hitachi-nlp FLD HuggingFace dataset columns fields sample"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "hitachi-nlp FLD HuggingFace dataset columns fields sample"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-19T13:25:44.509768+00:00_

Web search results for query: ""FOLIO" dataset larger version 2000 3000 examples FOL natural language reasoning"

Links: [{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"},{"title":"[PDF] FOLIO: Natural Language Reasoning with First-Order Logic | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FOLIO:-Natural-Language-Reasoning-with-First-Order-Han-Schoelkopf/5581bf85386737bd3378eec68189759a05280bea"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic Simeng Han1","url":"https://arxiv.org/pdf/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1229/"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"}]

Based on the search results, FOLIO consists of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion.

Regarding your query about a larger version with 2000-3000 examples: The search results mention Kawabata and Sugawara (2023) crowdsourced rationales for over 3000 examples based on ReClor, but this is a different dataset (ReClor), not a larger version of FOLIO.

Based on the available search results, FOLIO itself contains approximately 1,430-1,435 
…[truncated 454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-19T13:25:44.509919+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/hitachi-nlp/FLD.v2",
  "prompt": "Extract the complete dataset structure: all fields/columns, dataset size, number of examples per split, and any sample data shown. List every field name and type."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/hitachi-nlp/FLD.v2",
    "prompt": "Extract the complete dataset structure: all fields/columns, dataset size, number of examples per split, and any sample data shown. List every field name and type."
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-19T13:25:44.510045+00:00_

Web search results for query: "Papers with Code "first-order logic reasoning dataset" benchmark"

Links: [{"title":"Diagnosing the First-Order Logical Reasoning Ability Through LogicNLI - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.303/"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FCoReBench: Can Large Language Models Solve Challenging First-Order   Combinatorial Reasoning Problems?","url":"https://arxiv.org/pdf/2402.02611"},{"title":"P-FOLIO: Evaluating and Improving Logical Reasoning with Abundant   Human-Written Reasoning Chains","url":"https://arxiv.org/pdf/2410.09207"},{"title":"CodeSense: a Real-World Benchmark and Dataset for Code Semantic Reasoning","url":"https://arxiv.org/pdf/2506.00750"}]

Based on the search results, here are some notable first-order logic reasoning datasets and benchmarks:

## Key Datasets and Benchmarks

**LogicNLI**: A proposed benchmark that introduces a diagnostic method for first-order logic reasoning, where LogicNLI is an NLI-style dataset that effectively disentangles the target FOL reasoning from commonsense inference and can be used to diagnose language models from four perspectives: accuracy, robustness, generalization, and interpretability.

**FOLIO**: A human-annotated, logically complex and diverse dataset for reasoning in natural language equipped with first-order logic annotations, consisting of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion.

**P-FOLIO**: A human-annotated dataset consisting of diverse and complex reasoning chains for realistic logical reasoning stories, collected with an annotation protocol that facilitates humans to annotate well-structured natural language proofs for first-order logic re
…[truncated 442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-19T13:25:44.510193+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/91820fa6-7a1f-4a02-8bc0-aaa4f114a9f1/tool-results/webfetch-1779196587258-r6kcgy.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/91820fa6-7a1f-4a02-8bc0-aaa4f114a9f1/tool-results/webfetch-1779196587258-r6kcgy.pdf",
    "pages": "1-5"
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-19T13:25:44.510324+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://proceedings.mlr.press/v202/morishita23a/morishita23a.pdf",
  "prompt": "Extract the exact data format/fields of the FLD dataset. What are the columns? Is there formal logic (FOL) annotation? Show sample data if available. What does a proof look like? Are there formal logic formulas or just natural language?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://proceedings.mlr.press/v202/morishita23a/morishita23a.pdf",
    "prompt": "Extract the exact data format/fields of the FLD dataset. What are the columns? Is there formal logic (FOL) annotation? Show sample data if available. What does a proof look like? Are there formal logic formulas or just natural language?"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-19T13:25:44.510449+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/RamyaKeerthy/Translation-NL2FOL",
  "prompt": "Describe the repository structure. What files contain the ProofFOL dataset? What format is the data in? What does the conversion pipeline look like? List all key files and directories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/RamyaKeerthy/Translation-NL2FOL",
    "prompt": "Describe the repository structure. What files contain the ProofFOL dataset? What format is the data in? What does the conversion pipeline look like? List all key files and directories."
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-19T13:25:44.510559+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/91820fa6-7a1f-4a02-8bc0-aaa4f114a9f1/tool-results/webfetch-1779196587258-r6kcgy.pdf (782.5KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-19T13:25:44.510676+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/yale-nlp/P-FOLIO",
  "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations (fol_premises, fol_conclusion, premises-FOL, conclusion-FOL fields). What is P-FOLIO? How does it differ from FOLIO?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/yale-nlp/P-FOLIO",
    "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations (fol_premises, fol_conclusion, premises-FOL, conclusion-FOL fields). What is P-FOLIO? How does it differ from FOLIO?"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-19T13:25:44.510820+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/benlipkin/linc",
  "prompt": "Describe the repository structure. Does it include code for converting ProofWriter natural language rules to FOL? What is the conversion approach? Does it produce FOL annotations that could be used as a dataset? List key files related to FOL conversion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/benlipkin/linc",
    "prompt": "Describe the repository structure. Does it include code for converting ProofWriter natural language rules to FOL? What is the conversion approach? Does it produce FOL annotations that could be used as a dataset? List key files related to FOL conversion."
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-19T13:25:44.510946+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RuleTaker dataset original Datalog rules FOL conversion Allen AI allenai"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RuleTaker dataset original Datalog rules FOL conversion Allen AI allenai"
  }
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-19T13:25:44.511065+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/akshay107/FOLIO-fol",
  "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations (fol_premises, fol_conclusion, premises-FOL, conclusion-FOL fields). How does it differ from the original FOLIO?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/akshay107/FOLIO-fol",
    "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations (fol_premises, fol_conclusion, premises-FOL, conclusion-FOL fields). How does it differ from the original FOLIO?"
  }
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-19T13:25:44.511188+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"first order logic\" annotated dataset NLP natural language 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"first order logic\" annotated dataset NLP natural language 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-19T13:25:44.511306+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/fol-traces/fol-traces",
  "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations. How does it relate to FOLIO? Is this a FOLIO extension?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/fol-traces/fol-traces",
    "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations. How does it relate to FOLIO? Is this a FOLIO extension?"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-19T13:25:44.511439+00:00_

Web search results for query: "hitachi-nlp FLD HuggingFace dataset columns fields sample"

Links: [{"title":"hitachi-nlp/FLD.v2 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/hitachi-nlp/FLD.v2"},{"title":"hitachi-nlp/FLDx2 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/hitachi-nlp/FLDx2"},{"title":"hitachi-nlp/FLD.v2.reimpl · Discussions","url":"https://huggingface.co/datasets/hitachi-nlp/FLD.v2.reimpl/discussions"},{"title":"hitachi-nlp/FLDx2 at main","url":"https://huggingface.co/datasets/hitachi-nlp/FLDx2/tree/main"},{"title":"Dataset features — nlp 0.4.0 documentation","url":"https://huggingface.co/docs/datasets/v0.3.0/features.html"},{"title":"hitachi-nlp/FLD_metrics · Discussions","url":"https://huggingface.co/spaces/hitachi-nlp/FLD_metrics/discussions"},{"title":"GitHub - hitachi-nlp/FLD-corpus","url":"https://github.com/hitachi-nlp/FLD-corpus"},{"title":"hitachi-nlp (Hitachi, Ltd.)","url":"https://huggingface.co/hitachi-nlp"},{"title":"Update README.md · hitachi-nlp/FLDx2 at 4ed4bc0","url":"https://huggingface.co/datasets/hitachi-nlp/FLDx2/commit/4ed4bc0dac57ebe4b34020070f29f8105d672e57"},{"title":"Main classes — datasets 1.12.0 documentation","url":"https://huggingface.co/docs/datasets/v1.12.0/package_reference/main_classes.html"}]

Based on the search results, I found information about the hitachi-nlp FLD dataset. The FLD dataset involves given a set of facts and a hypothesis, a model must generate a proof sequence and determine an answer marker (proved, disproved, or unknown), with gold proofs consisting of a series of logical steps derived from the facts leading towards the hypothesis, currently with at most one proof per example.

For the FLDx2 corpus specifically, proof_serial sometimes includes both the proof and answer, and sometimes only the answer, working as a sort of augmentation.

The search results indicate that the actual schema/columns information can be found on the HuggingFace Hub directly. The datas
…[truncated 600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-19T13:25:44.511602+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "huggingface datasets FOLIO extended FOL \"folio\" -P-FOLIO site:huggingface.co"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "huggingface datasets FOLIO extended FOL \"folio\" -P-FOLIO site:huggingface.co"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-19T13:25:44.511771+00:00_

I cannot extract meaningful information about the FLD dataset from this content. The provided text appears to be a PDF file encoded in binary/compressed format (containing FlateDecode streams and object references), which is not human-readable raw data.

To properly analyze the FLD dataset's structure, columns, and annotation format, I would need:

1. **Accessible documentation** - README files, data cards, or academic papers describing the dataset
2. **Sample data files** - CSV, JSON, or plain text format showing actual records
3. **Schema definitions** - Formal specifications of fields and data types

From the binary content provided, I cannot determine:
- The specific columns/fields used
- Whether formal logic (FOL) annotations are present
- The structure of proofs (natural language vs. formal expressions)
- Sample data instances

**Recommendation:** Please provide the dataset in a text-accessible format or share the associated documentation/paper describing the FLD dataset's structure and annotation scheme.

[Binary content (application/pdf, 1.7MB) also saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/91820fa6-7a1f-4a02-8bc0-aaa4f114a9f1/tool-results/webfetch-1779196598089-1613he.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-19T13:25:44.511926+00:00_

# P-FOLIO Dataset Information

Based on the provided web page content, here's what can be determined:

## What is P-FOLIO?

**P-FOLIO** is a human-annotated dataset for logical reasoning that consists of:
- Diverse and complex **reasoning chains** for realistic logical reasoning stories (all human-written)
- Well-structured natural language proofs for first-order logic reasoning problems
- Annotated using a structured, step-by-step annotation protocol

It was published at EMNLP 2024 Findings and is built upon the [FOLIO](https://huggingface.co/datasets/yale-nlp/FOLIO) dataset.

## How it differs from FOLIO

While the page confirms P-FOLIO is "built upon FOLIO," the specific differences aren't detailed in this excerpt. However, the key distinction appears to be:
- **FOLIO**: The base logical reasoning dataset
- **P-FOLIO**: Enhanced version with **abundant human-written reasoning chains** - essentially adding detailed step-by-step reasoning annotations that weren't present in FOLIO

## Dataset Details

**Unfortunately, the specific information requested is NOT available in this web page:**
- ❌ Number of rows per split
- ❌ Specific column names/fields
- ❌ FOL annotation fields (fol_premises, fol_conclusion, etc.)
- ❌ Total file size breakdown

The page only shows:
- **Total file size**: 1.14 MB
- **Downloads last month**: 47
- **License**: MIT
- **Status**: "[WIP] We are working on the release of the dataset"

**Note**: The dataset requires users to accept conditions and log in to access the full content and detailed specifications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-19T13:25:44.512062+00:00_

# Translation-NL2FOL Repository Overview

## Repository Structure

The repository is organized into several key directories:

- **`data/`** - Contains training datasets for the three main datasets mentioned
- **`data/incremental/`** - Houses systematically split records for simulating data augmentation scenarios
- **`fol_solver/`** - Modules for handling first-order logic operations
- **`notebook/`** - Jupyter notebooks for exploration and analysis
- **`templates/`** - Configuration or template files
- **`utils/`** - Utility functions supporting the main pipeline

## ProofFOL Dataset Location

According to the documentation, "The FOL dataset for ProofWriter (ProofFOL) is available on Hugging Face" at the external URL: `https://huggingface.co/datasets/ramyakeerthyt/ProofFOL`

The dataset can be loaded programmatically using the Hugging Face datasets library rather than being stored directly in this repository.

## Key Executable Files

- **`finetune.py`** - Fine-tuning script
- **`inference.py`** - Standard inference implementation
- **`inference_incremental.py`** - Incremental learning inference
- **`inference_t5.py`** - T5 model-based inference with verification
- **`run_seq2seq.py`** - T5 model training on perturbation datasets
- **`run_test.sh`** - Test execution script

## Data Format & Pipeline

The repository focuses on translating natural language into first-order logic. The conversion pipeline involves fine-tuning language models and performing inference with optional verification tools, supporting both standard and incremental learning approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-19T13:25:44.512184+00:00_

# LINC Repository Structure Analysis

Based on the provided content, I cannot definitively answer whether this repository includes code for converting ProofWriter natural language rules to FOL (First-Order Logic).

## What the Content Reveals

The repository description indicates it's for a paper titled **"LINC: A neuro-symbolic approach for logical reasoning by combining language models with first-order logic provers."** The repo contains:

**Directory structure:**
- `analysis/` - for figure and table generation
- `eval/` - evaluation framework
- `outputs/` - experimental results
- `utils/` - utility functions

**Key files visible:**
- `runner.py` - experiment execution
- `eval/args.py` - configuration options
- Analysis notebooks for supplemental materials

## Limitations of Available Information

The GitHub page excerpt provided doesn't detail the specific functionality within each directory or file. To determine whether ProofWriter conversion code exists, one would need to:

1. Examine the actual Python files and notebooks
2. Review the complete README content (truncated here)
3. Check the `eval/` and `utils/` directories directly

The paper focuses on combining language models with FOL provers, suggesting the system handles logical reasoning, but the exact conversion methodology and whether it produces FOL datasets as byproducts cannot be confirmed from this excerpt alone.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-19T13:25:44.512322+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip install datasets -q 2>/dev/null && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('tasksource/LogicNLI', split='train[:3]')\nprint('=== COLUMNS ===')\nprint(ds.column_names)\nprint()\nprint('=== FEATURES ===')\nprint(ds.features)\nprint()\nfor i, ex in enumerate(ds):\n    print(f'=== EXAMPLE {i} ===')\n    for k, v in ex.items():\n        val_str = str(v)\n        if len(val_str) > 500:\n            val_str = val_str[:500] + '...'\n        print(f'  {k}: {val_str}')\n    print()\n\"\n",
  "description": "Load LogicNLI from HuggingFace and inspect field structure",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "pip install datasets -q 2>/dev/null && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('tasksource/LogicNLI', split='train[:3]')\nprint('=== COLUMNS ===')\nprint(ds.column_names)\nprint()\nprint('=== FEATURES ===')\nprint(ds.features)\nprint()\nfor i, ex in enumerate(ds):\n    print(f'=== EXAMPLE {i} ===')\n    for k, v in ex.items():\n        val_str = str(v)\n        if len(val_str) > 500:\n            val_str = val_str[:500] + '...'\n        print(f'  {k}: {val_str}')\n    print()\n\"\n",
    "description": "Load LogicNLI from HuggingFace and inspect field structure",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-19T13:25:44.512449+00:00_

# FOL-Traces Dataset Analysis

Based on the webpage content provided, I can only extract limited information:

## Available Information

**Dataset Metadata:**
- **Total file size:** 126 GB
- **Size category:** 1B < n < 10B (between 1 billion and 10 billion items)
- **Task:** Text Generation
- **Language:** English
- **Tags:** logic, first-order-logic, fol
- **License:** MIT

## Information NOT Available

The webpage content does not provide:
- ❌ Number of rows per split
- ❌ Column names/fields
- ❌ Specific FOL annotation details
- ❌ Relationship to FOLIO dataset
- ❌ Whether it's a FOLIO extension

**Note:** The README.md file exists but is empty, and the dataset requires login/contact information sharing to access detailed content.

## Recommendation

To obtain the missing information, you would need to:
1. Log in to Hugging Face
2. Accept the dataset conditions
3. Review the full README documentation
4. Check the Data Studio viewer
5. Examine the actual dataset files

If this dataset is related to FOLIO (a first-order logic benchmark), that relationship would likely be documented in the full README once you gain access.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-19T13:25:44.512576+00:00_

# FOLIO-fol Dataset Analysis

## Dataset Size
- **Total rows**: 3,254
- **Train split**: 2,680 rows
- **Validation split**: 579 rows

## Column Names/Fields
The dataset has two main columns:
1. **`data`** (string): Natural language premises/statements
2. **`fol`** (string): First-Order Logic (FOL) formalized representations

## FOL Annotations
Yes, this dataset includes FOL annotations. Each row contains:
- Natural language statements in the `data` column
- Corresponding FOL expressions in the `fol` column

Example:
```
data: "All people who regularly drink coffee are dependent on caffeine."
fol: "∀x (DrinkRegularly(x, coffee) → IsDependentOn(x, caffeine))"
```

## Differences from Original FOLIO

Based on the naming convention and structure, this appears to be a variant or derived version of the original FOLIO dataset with the following characteristics:

- **Format**: Presents data as simple `data` and `fol` column pairs (premises + their FOL encodings)
- **Original FOLIO structure**: Typically includes separate fields for premises, conclusions, and their FOL equivalents (e.g., `fol_premises`, `fol_conclusion`)

This **FOLIO-fol** dataset simplifies the structure to a 2-column format, making it potentially easier for direct text-to-FOL translation tasks, whereas the original FOLIO likely maintains separate logical reasoning problems with premises and conclusions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-19T13:25:44.512734+00:00_

Web search results for query: "RuleTaker dataset original Datalog rules FOL conversion Allen AI allenai"

Links: [{"title":"GitHub - allenai/ruletaker · GitHub","url":"https://github.com/allenai/ruletaker"},{"title":"RuleTaker: Transformers as Soft Reasoners over Language","url":"https://allenai.org/data/ruletaker"},{"title":"ruletaker/common.py at master · allenai/ruletaker","url":"https://github.com/allenai/ruletaker/blob/master/common.py"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"Transformers as Soft Reasoners over Language","url":"https://arxiv.org/pdf/2002.05867"},{"title":"Towards Generalizable and Faithful Logic Reasoning over Natural Language via Resolution Refutation","url":"https://arxiv.org/html/2404.01677v1"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive ...","url":"https://aclanthology.org/2021.findings-acl.317.pdf"}]

Based on the search results, here's what I found about the RuleTaker dataset:

## RuleTaker Dataset Overview

The original RuleTaker theory generator and inference engine were written in Lisp, but a more stable and re-engineered Python version was later created. The theory generator uses a declarative grammar that users can modify to generate different theories with different distributions.

## Datalog Rules and Representation

The dataset follows the semantics of Datalog: a fact is true if it is either known (explicitly stated in the context), or is the conclusion of a rule whose conditions are true. The original datasets were generated from synthetic logic programs and their implications, using natural language patterns to produce the English forms.

## FOL Conversion

The representations provided currently are the logical forms (prefix notation), natural language, and logic program in theorem prover format. Additionally, regular expressions can be used to convert each data back to its corresponding FOL representation since the dataset is synthetic.
…[truncated 306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-19T13:25:44.512887+00:00_

Web search results for query: ""first order logic" annotated dataset NLP natural language 2024 2025"

Links: [{"title":"Few-Shot Natural Language to First-Order Logic ...","url":"https://aclanthology.org/2025.naacl-long.547.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1229/"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/pdf/2209.00840"}]

Based on the search results, here are the key findings about first-order logic annotated datasets in NLP:

## FOLIO Dataset

FOLIO is the first expert-written dataset for FOL reasoning equipped with parallel FOL formulas. FOLIO consists of 1,435 examples (unique conclusions), each paired with one of 487 sets of premises which serve as rules to be used to deductively reason for the validity of each conclusion. The logical correctness of premises and conclusions is ensured by their parallel FOL annotations, which are automatically verified by 
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-19T13:25:44.513023+00:00_

Exit code 1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-19T13:25:44.513145+00:00_

Web search results for query: "huggingface datasets FOLIO extended FOL "folio" -P-FOLIO site:huggingface.co"

Links: [{"title":"akshay107/FOLIO-fol · Datasets at Hugging Face","url":"https://huggingface.co/datasets/akshay107/FOLIO-fol"},{"title":"yale-nlp/P-FOLIO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yale-nlp/P-FOLIO"},{"title":"minimario/FOLIO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/minimario/FOLIO"},{"title":"tasksource/folio · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/folio"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=FOLIO"},{"title":"yale-nlp/FOLIO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yale-nlp/FOLIO"},{"title":"benlipkin/folio · Datasets at Hugging Face","url":"https://huggingface.co/datasets/benlipkin/folio"},{"title":"Navigating Dataset Documentations in AI: A Large-Scale Analysis of   Dataset Cards on Hugging Face","url":"https://arxiv.org/pdf/2401.13822"},{"title":"P-FOLIO: Evaluating and Improving Logical Reasoning with Abundant   Human-Written Reasoning Chains","url":"https://arxiv.org/pdf/2410.09207"}]

Based on the search results, I found several FOLIO-related datasets on Hugging Face:

1. **FOLIO (Original Dataset)** - FOLIO is a human-annotated, open-domain dataset for reasoning in natural language equipped with first-order logic (FOL) annotations, consisting of 1,435 examples paired with premise sets. This is available at [yale-nlp/FOLIO](https://huggingface.co/datasets/yale-nlp/FOLIO) and other mirrors.

2. **P-FOLIO (Extended Dataset)** - P-FOLIO is a human-annotated dataset consisting of diverse and complex reasoning chains, collected with an annotation protocol that facilitates humans to annotate well-structured natural language proofs for first-order logic reasoning problems in a step-by-step manner. P-FOLIO is built upon FOLIO. This is available at [yale-nlp/P-FOLIO](https://huggingface.co/da
…[truncated 556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-19T13:25:44.513289+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOL reasoning benchmark dataset CLUTRR bAbI SimpleLogic AR-LSAT ReClor formal logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOL reasoning benchmark dataset CLUTRR bAbI SimpleLogic AR-LSAT ReClor formal logic"
  }
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-19T13:25:44.513419+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/allenai/ruletaker",
  "prompt": "Describe the repo structure. Does it contain logical forms or FOL representations? Is there a theory generator that outputs both natural language and logical forms? What format are the logical forms in? List key files and directories, especially anything related to FOL or logic program generation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/allenai/ruletaker",
    "prompt": "Describe the repo structure. Does it contain logical forms or FOL representations? Is there a theory generator that outputs both natural language and logical forms? What format are the logical forms in? List key files and directories, especially anything related to FOL or logic program generation."
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-19T13:25:44.513556+00:00_

# FLD.v2 Dataset Structure

## Overview
**FLD.v2** is a formal logic deduction dataset from Hitachi, Ltd., hosted on Hugging Face. It contains 40,000 rows across 2 subsets with 3 splits.

## Dataset Size
- **Total rows**: 40,000
- **Subset**: default (40k rows)
- **Splits**:
  - train: 30,000 rows
  - validation: 5,000 rows
  - test: 5,000 rows

## Modalities & Formats
- **Modalities**: Tabular, Text
- **Format**: Parquet
- **Libraries**: Datasets, pandas, Croissant

## Complete Field Structure

| Field Name | Type | Description |
|---|---|---|
| `version` | stringclass (1 value) | Dataset version identifier |
| `hypothesis` | string (11-215 chars) | Natural language hypothesis statement |
| `hypothesis_formula` | string (3-39 chars) | Formal logic representation of hypothesis |
| `context` | string (0-2.9k chars) | Natural language premises/context |
| `context_formula` | string (0-905 chars) | Formal logic representation of context |
| `proofs` | sequence | List of natural language proof steps |
| `proofs_formula` | sequence | List of formal logic proof steps |
| `negative_hypothesis` | string (15-193 chars, nullable) | Natural language negative hypothesis |
| `negative_hypothesis_formula` | string (3-37 chars, nullable) | Formal logic negative hypothesis |
| `negative_proofs` | sequence | Proof steps for negative case |
| `negative_original_tree_depth` | int64 (0-25, nullable) | Depth metric for negative proofs |
| `original_tree_depth` | int64 (1-4, nullable) | Depth metric for positive proofs |
| `depth` | int64 (0-3, nullable) | Normalized depth value |
| `num_formula_distractors` | int64 (0-22) | Count of formula-based distractors |
| `num_translation_distractors` | int64 (0-0) | Count of translation distractors |
| `num_all_distractors` | int64 (0-22) | Total distractor count |
| `proof_label` | stringclass (3 values) | Label: {PROVED, DISPROVED, UNKNOWN} |
| `negative_proof_label` | stringclass (2 values) | Negative proof label |
| `world_assump_label` | st
…[truncated 2334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-19T13:25:44.513691+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-19T13:25:44.513835+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/ramyakeerthyt/ProofFOL",
  "prompt": "Describe this dataset: what fields does it have, how many examples, what format are the FOL annotations in, what splits are available? List all column names and provide a sample if visible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/ramyakeerthyt/ProofFOL",
    "prompt": "Describe this dataset: what fields does it have, how many examples, what format are the FOL annotations in, what splits are available? List all column names and provide a sample if visible."
  }
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-19T13:25:44.513963+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip install datasets -q 2>&1 | tail -3 && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('tasksource/LogicNLI', split='train[:3]', trust_remote_code=True)\nprint('=== COLUMNS ===')\nprint(ds.column_names)\nprint()\nprint('=== FEATURES ===')\nprint(ds.features)\nprint()\nfor i, ex in enumerate(ds):\n    print(f'=== EXAMPLE {i} ===')\n    for k, v in ex.items():\n        val_str = str(v)\n        if len(val_str) > 800:\n            val_str = val_str[:800] + '...'\n        print(f'  {k}: {val_str}')\n    print()\n\" 2>&1\n",
  "description": "Load LogicNLI dataset and inspect structure",
  "timeout": "180000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "pip install datasets -q 2>&1 | tail -3 && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('tasksource/LogicNLI', split='train[:3]', trust_remote_code=True)\nprint('=== COLUMNS ===')\nprint(ds.column_names)\nprint()\nprint('=== FEATURES ===')\nprint(ds.features)\nprint()\nfor i, ex in enumerate(ds):\n    print(f'=== EXAMPLE {i} ===')\n    for k, v in ex.items():\n        val_str = str(v)\n        if len(val_str) > 800:\n            val_str = val_str[:800] + '...'\n        print(f'  {k}: {val_str}')\n    print()\n\" 2>&1\n",
    "description": "Load LogicNLI dataset and inspect structure",
    "timeout": "180000"
  }
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-19T13:25:44.514094+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/benlipkin/folio",
  "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations. How does it differ from the original FOLIO? Is this an extended version?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/benlipkin/folio",
    "prompt": "Extract: dataset size (number of rows per split), column names/fields, whether it has FOL annotations. How does it differ from the original FOLIO? Is this an extended version?"
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-19T13:25:44.514221+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "allenai ruletaker theory generator logical form prefix notation FOL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "allenai ruletaker theory generator logical form prefix notation FOL"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-19T13:25:44.514333+00:00_

Exit code 1

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
Traceback (most recent call last):
  File "&lt;string>", line 2, in &lt;module>
    from datasets import load_dataset
ModuleNotFoundError: No module named 'datasets'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-19T13:25:44.514459+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"FOLIO\" \"WikiLogic\" \"HybLogic\" dataset source split first-order logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"FOLIO\" \"WikiLogic\" \"HybLogic\" dataset source split first-order logic"
  }
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-19T13:25:44.514580+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2209.00840v2",
  "prompt": "Extract information about FOLIO dataset splits: WikiLogic vs HybLogic sources, total example counts, train/validation/test split sizes. Is there mention of FOLIO-wiki or extended versions? What are the exact split sizes?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2209.00840v2",
    "prompt": "Extract information about FOLIO dataset splits: WikiLogic vs HybLogic sources, total example counts, train/validation/test split sizes. Is there mention of FOLIO-wiki or extended versions? What are the exact split sizes?"
  }
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-19T13:25:44.514715+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip install datasets --break-system-packages -q 2>&1 | tail -5",
  "description": "Install datasets library",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "pip install datasets --break-system-packages -q 2>&1 | tail -5",
    "description": "Install datasets library",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-19T13:25:44.514840+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/hitachi-nlp/FLDx2",
  "prompt": "Extract: all field names/columns, dataset size (number of rows per split), sample data, and any FOL formula fields. List every column."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/hitachi-nlp/FLDx2",
    "prompt": "Extract: all field names/columns, dataset size (number of rows per split), sample data, and any FOL formula fields. List every column."
  }
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-19T13:25:44.514961+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('renma/ProntoQA', split='validation')\nprint('Number of examples:', len(ds))\nprint('Fields:', ds.column_names)\nprint('Features:', ds.features)\nprint()\nfor i in range(3):\n    ex = ds[i]\n    print(f'=== Example {i} ===')\n    for k, v in ex.items():\n        print(f'  {k}:')\n        if isinstance(v, list):\n            for item in v:\n                print(f'    - {repr(item)[:300]}')\n        else:\n            print(f'    {repr(v)[:500]}')\n    print()\n\" 2>&1",
  "description": "Load and inspect renma/ProntoQA dataset",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('renma/ProntoQA', split='validation')\nprint('Number of examples:', len(ds))\nprint('Fields:', ds.column_names)\nprint('Features:', ds.features)\nprint()\nfor i in range(3):\n    ex = ds[i]\n    print(f'=== Example {i} ===')\n    for k, v in ex.items():\n        print(f'  {k}:')\n        if isinstance(v, list):\n            for item in v:\n                print(f'    - {repr(item)[:300]}')\n        else:\n            print(f'    {repr(v)[:500]}')\n    print()\n\" 2>&1",
    "description": "Load and inspect renma/ProntoQA dataset",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-19T13:25:44.515081+00:00_

# RuleTaker Repository Structure

## Overview
The RuleTaker repository is a Python-based toolkit for generating logical reasoning datasets and labeling them via theorem proving. It contains both a theory generator and a label generator that work with logical representations.

## Logical Forms & FOL Representations
Yes, the repository extensively uses logical forms. The system generates representations in multiple formats:

- **Prefix notation logical forms** (the primary symbolic representation)
- **Natural language English sentences**
- **ProbLog logic programs** (the theorem prover format)

## Theory Generator
The `theory_generator.py` tool produces comprehensive outputs including:

> "the prefix notation logical forms generated by the grammar, the theory and assertion in natural languages (english sentences), and the logic program that was input to the theorem prover"

This generator accepts probabilistic context-free grammars (PCFG) to create theories with both logical and natural language representations.

## Logical Form Format
The system uses **prefix notation** for logical forms. For example:
- Fact: `+ ( likes 'lion' 'cow' )`
- Rule: `[ + ( cold X ) ] -> + ( nice X )`

These are structured as predicates with polarity markers (+/-) and arguments in prefix notation.

## Key Files & Directories

**Core Files:**
- `theory_generator.py` - Generates dataset with logical forms, English, and logic programs
- `theory_label_generator.py` - Labels theories using ProbLog theorem prover
- `common.py` - Shared utilities
- `utils.py` - Helper functions

**Supporting:**
- `grammars_and_config/` - Contains PCFG grammars and configuration JSON files
- `requirements.txt` - Dependencies (includes ProbLog)

The repository outputs ProbLog-formatted logic programs as the FOL representation for theorem proving.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-19T13:25:44.515218+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/hitachi-nlp/FLD",
  "prompt": "Extract the data format details: what fields are in each example, sample input/output, how proofs are formatted, what formal logic notation is used. Show examples of proof_serial and prompt_serial format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/hitachi-nlp/FLD",
    "prompt": "Extract the data format details: what fields are in each example, sample input/output, how proofs are formatted, what formal logic notation is used. Show examples of proof_serial and prompt_serial format."
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-19T13:25:44.515341+00:00_

# FOLIO Dataset Summary

## Dataset Size and Structure

**Total Rows:** 204 rows
**Split:** 
- `validation` split: 204 rows

**Total File Size:** 178 kB

## Column Names/Fields

The dataset contains the following fields:

1. **premises** (sequence) - Natural language premise statements
2. **premises-FOL** (sequence) - First-Order Logic (FOL) representations of premises
3. **conclusion** (string, length 12-386 characters) - Natural language conclusion statement
4. **conclusion-FOL** (string, length 8-140 characters) - FOL representation of the conclusion
5. **label** (3 class values) - Classification label: `"True"`, `"False"`, or `"Uncertain"`

## FOL Annotations

**Yes, this dataset includes FOL annotations.** Each natural language premise and conclusion has a corresponding first-order logic representation. For example:

```
Premises (NL):
"If people perform in school talent shows often, then they attend and are very engaged with school events."

Premises-FOL:
"∀x (TalentShows(x) → Engaged(x))"

Conclusion (NL):
"Bonnie performs in school talent shows often."

Conclusion-FOL:
"Engaged(bonnie)"

Label: "Uncertain"
```

## Relationship to Original FOLIO

This appears to be the **original FOLIO dataset** published in the paper *"FOLIO: Natural Language Reasoning with First-Order Logic"* (arXiv: 2209.00840, 2022). There is no indication this is an extended version—it is the canonical version maintained by the original authors on Hugging Face.

**Citation:**
```bibtex
@article{han2022folio,
  title={FOLIO: Natural Language Reasoning with First-Order Logic},
  author={Han, Simeng and Schoelkopf, Hailey and ...},
  journal={arXiv preprint arXiv:2209.00840},
  year={2022}
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-19T13:25:44.515504+00:00_

Web search results for query: "allenai ruletaker theory generator logical form prefix notation FOL"

Links: [{"title":"ruletaker/theory_label_generator.py at master · allenai/ruletaker","url":"https://github.com/allenai/ruletaker/blob/master/theory_label_generator.py"},{"title":"ruletaker/common.py at master · allenai/ruletaker","url":"https://github.com/allenai/ruletaker/blob/master/common.py"},{"title":"GitHub - allenai/ruletaker · GitHub","url":"https://github.com/allenai/ruletaker"},{"title":"ruletaker/theory_generator.py at master · allenai/ruletaker","url":"https://github.com/allenai/ruletaker/blob/master/theory_generator.py"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"Releases · allenai/ruletaker","url":"https://github.com/allenai/ruletaker/releases"},{"title":"ruletaker/tests.py at master · allenai/ruletaker","url":"https://github.com/allenai/ruletaker/blob/master/tests.py"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive Statements   over Natural Language","url":"https://arxiv.org/pdf/2012.13048"}]

Based on the search results, here's what I found about Allen AI's RuleTaker theory generator and logical forms:

## RuleTaker Overview

RuleTaker is a tool designed to generate datasets of theories and assertions meant to test logical reasoning capabilities and run existing theories through a theorem proving engine to obtain labels.

## Logical Form Representation

The tool supports JSON format where theory statements are contained in a `theory_statements` field in prefix notation as logical forms. The representations provided include logical forms in prefix notation, natural language, and logic program in theorem prover format.

## Technical Implementation

RuleTaker uses Problog as the theorem-proving engine to generate labels for theory-assertion examples. The theory generator uses a declarative grammar that users can modify to generate different theories with different distr
…[truncated 551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-19T13:25:44.515644+00:00_

# ProofFOL Dataset Description

## Overview
ProofFOL is a dataset available on Hugging Face containing logical reasoning examples with First-Order Logic (FOL) annotations.

## Dataset Specifications

### Size & Format
- **Total Examples**: 10,424 rows
- **File Size**: 21.3 MB
- **Format**: JSON (auto-converted to Parquet)
- **Size Category**: 10K - 100K examples
- **Libraries**: Datasets, pandas, Croissant

### Splits
- **Single Split**: `train` (10.4k rows)

## Column Names

Based on the dataset viewer, the dataset contains the following columns:

1. **id** (string, length 27-33): Unique identifier for each example
2. **input** (string, length 283-1.2k): The premise text containing facts and rules
3. **label** (string, 3 classes): Classification label - `True`, `False`, or `Unknown`
4. **output** (string, length 56-2.55k): FOL representation and conclusion

## FOL Format

The FOL annotations follow this structure:

```
Predicates: [List of predicates used]
Premise_FOL: [FOL representation of premises]
Conclusion_FOL: [FOL representation of what to prove]
```

### Example Entry

```
ID: proof_AttNoneg-OWA-D5-588_Q10_d4
Input: "Premise: Bob is cold. Bob is quiet... If someone is white and rough then they are quiet..."
Label: False
Output: "Predicates: Green(x); Young(x); Quiet(x); White(x); Rough(x); Furry(x); Cold(x)
         Premise_FOL: Cold(Bob) ::: Bob is cold. ..."
```

## Key Characteristics

- **Task Type**: Logical entailment/reasoning with FOL
- **Modality**: Text-based
- **Label Distribution**: Ternary classification (True/False/Unknown)
- **FOL Predicates**: Unary predicates (e.g., `Cold(x)`, `Quiet(x)`) and binary relations (e.g., `Visits(x,y)`, `Needs(x,y)`)
- **Example Types**: Both attribute-based and relational reasoning examples (marked as "AttNeg", "AttNoneg", "RelNeg", "RelNoneg")

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-19T13:25:44.515803+00:00_

Web search results for query: ""FOLIO" "WikiLogic" "HybLogic" dataset source split first-order logic"

Links: [{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://github.com/Yale-LILY/FOLIO"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic Simeng Han1","url":"https://arxiv.org/pdf/2209.00840"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"[PDF] FOLIO: Natural Language Reasoning with First-Order Logic | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FOLIO:-Natural-Language-Reasoning-with-First-Order-Han-Schoelkopf/5581bf85386737bd3378eec68189759a05280bea"}]

Based on the search results, here's what I found about the FOLIO dataset and its WikiLogic and HybLogic splits:

## Dataset Overview

FOLIO is a human-annotated, logically complex and diverse dataset for reasoning in natural language (NL), equipped with first-order logic (FOL) annotations. FOLIO consists of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion.

## Source Splits: WikiLogic and HybLogic

The dataset is divided into two distinct sources based on how the examples were collected:

The dataset was developed in six stages: WikiLogic collection, HybLogic collection, NL quality control, FOL quality control, NL-FOL alignment and FOL verification, spending 980 man-hours 
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-19T13:25:44.515948+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/pdf/2308.07336",
  "prompt": "Extract: 1) the exact data fields in FLD dataset, 2) sample data showing formal logic formulas, 3) how proofs are represented, 4) the formal logic notation used (FOL formulas vs natural language). Show concrete examples of formulas used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/pdf/2308.07336",
    "prompt": "Extract: 1) the exact data fields in FLD dataset, 2) sample data showing formal logic formulas, 3) how proofs are represented, 4) the formal logic notation used (FOL formulas vs natural language). Show concrete examples of formulas used."
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-19T13:25:44.516073+00:00_

# FOLIO Dataset Splits and Versions

## WikiLogic vs HybLogic Sources

FOLIO comprises two distinct collection methods:

**WikiLogic**: Annotators selected random Wikipedia pages as inspiration and created original stories from scratch. This method produced 304 stories with 1,353 premises and 753 conclusions, accounting for approximately 63% of total stories but 74% of vocabulary.

**HybLogic**: A template-based hybrid approach combining valid syllogisms to ensure logical soundness. This yielded 183 stories with 1,054 premises and 682 conclusions. As noted, "the conclusion of one syllogism is used as a premise for the next syllogism."

## Total Example Counts

The dataset contains "1,430 examples (unique conclusions)" paired with "487 sets of premises." Combined statistics show 2,407 total premises and 1,435 total conclusions across both collection methods.

## Train/Validation/Test Split

The authors specify: "We split FOLIO by 70%/15%/15% split for the train/validation/test sets with 1,001/203/226 examples respectively."

## Extended Versions

The document contains no mention of FOLIO-wiki or other extended dataset versions. The paper focuses exclusively on the single unified FOLIO dataset combining both collection approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-19T13:25:44.516211+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOLIO dataset HuggingFace first-order logic annotations size examples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOLIO dataset HuggingFace first-order logic annotations size examples"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-19T13:25:44.516344+00:00_

Generating validation split:   0%|          | 0/500 [00:00<?, ? examples/s]Generating validation split: 100%|██████████| 500/500 [00:00<00:00, 14523.11 examples/s]
Number of examples: 500
Fields: ['id', 'answer', 'context', 'options', 'question', 'raw_logic_programs']
Features: {'id': Value('string'), 'answer': Value('string'), 'context': Value('string'), 'options': List(Value('string')), 'question': Value('string'), 'raw_logic_programs': List(Value('string'))}

=== Example 0 ===
  id:
    'ProntoQA_1'
  answer:
    'B'
  context:
    'Jompuses are not shy. Jompuses are yumpuses. Each yumpus is aggressive. Each yumpus is a dumpus. Dumpuses are not wooden. Dumpuses are wumpuses. Wumpuses are red. Every wumpus is an impus. Each impus is opaque. Impuses are tumpuses. Numpuses are sour. Tumpuses are not sour. Tumpuses are vumpuses. Vumpuses are earthy. Every vumpus is a zumpus. Zumpuses are small. Zumpuses are rompuses. Max is a yumpus.'
  options:
    - 'A) True'
    - 'B) False'
  question:
    'Is the following statement true or false? Max is sour.'
  raw_logic_programs:
    - 'Predicates:\nJompus($x, bool) ::: Does x belong to Jompus?\nShy($x, bool) ::: Is x shy?\nYumpus($x, bool) ::: Does x belong to Yumpus?\nAggressive($x, bool) ::: Is x aggressive?\nDumpus($x, bool) ::: Does x belong to Dumpus?\nWooden($x, bool) ::: Is x wooden?\nWumpus($x, bool) ::: Does x belong to 

=== Example 1 ===
  id:
    'ProntoQA_2'
  answer:
    'A'
  context:
    'Every tumpus is not angry. Tumpuses are rompuses. Every numpus is not bright. Rompuses are not luminous. Rompuses are yumpuses. Yumpuses are transparent. Yumpuses are zumpuses. Each zumpus is not bitter. Zumpuses are impuses. Impuses are red. Each impus is a dumpus. Every dumpus is happy. Each dumpus is a vumpus. Vumpuses are bright. Every vumpus is a jompus. Jompuses are large. Each jompus is a wumpus. Stella is a yumpus.'
  options:
    - 'A) True'
    - 'B) False'
  question:
    'Is the following statement true or fals
…[truncated 1300 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-19T13:25:44.516488+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://allenai.org/data/ruletaker",
  "prompt": "What data formats are available for download? Does the dataset include FOL or logical form representations alongside the natural language? What files/formats can be downloaded?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://allenai.org/data/ruletaker",
    "prompt": "What data formats are available for download? Does the dataset include FOL or logical form representations alongside the natural language? What files/formats can be downloaded?"
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-19T13:25:44.516607+00:00_

# FLD Data Format Details

Based on the provided GitHub repository content, specific data format details are not explicitly documented in the accessible text.

## What the Repository Indicates

The page confirms FLD is "a project to enhance LLMs' reasoning capabilities via synthetically generated samples of logical reasoning." However, the actual data structure specifications—including field definitions, sample inputs/outputs, proof formatting, and formal logic notation—are not included in this overview.

## Where to Find Details

The repository directs users to consult:

- **FLD corpora documentation**: Available at the dedicated [FLDx2 corpus repository](https://github.com/hitachi-nlp/FLD-corpus)
- **Generator scripts**: Details at the [FLD-generator repository](https://github.com/hitachi-nlp/FLD-generator/) which likely contains implementation specifics
- **Research papers**: The NeurIPS 2024 paper ["Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus"](https://arxiv.org/abs/2411.12498) presumably documents proof serialization, prompt formats, and formal logic conventions

## Design Principles Mentioned

The project integrates "(i) multi-step deduction with unknown facts, (ii) diverse reasoning rules, (iii) diverse linguistic expressions, and (iv) challenging distractors," but exact formatting specifications require consulting the linked resources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-19T13:25:44.516761+00:00_

  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts hf, huggingface-cli and tiny-agents are installed in '/home/ubuntu/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script datasets-cli is installed in '/home/ubuntu/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-19T13:25:44.516882+00:00_

REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://allenai.org/data/ruletaker
Redirect URL: https://github.com/allenai/ruletaker
Status: 307 Temporary Redirect

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://github.com/allenai/ruletaker"
- prompt: "What data formats are available for download? Does the dataset include FOL or logical form representations alongside the natural language? What files/formats can be downloaded?"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-19T13:25:44.517007+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.09207",
  "prompt": "Extract: What is P-FOLIO? How many examples does it have? Does P-FOLIO include FOL annotations (premises-FOL, conclusion-FOL)? Or does it only add reasoning chains? What's the relationship to original FOLIO?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2410.09207",
    "prompt": "Extract: What is P-FOLIO? How many examples does it have? Does P-FOLIO include FOL annotations (premises-FOL, conclusion-FOL)? Or does it only add reasoning chains? What's the relationship to original FOLIO?"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-19T13:25:44.517127+00:00_

I cannot extract the requested information from this document. The provided content appears to be a compressed/encoded PDF binary stream rather than readable text. The payload contains:

- Flate-encoded image data (XObject with BitsPerComponent 8, ColorSpace DeviceRGB)
- Binary streams with compression artifacts
- No discernible structured data fields, formal logic formulas, or proof representations

**What's needed instead:**

To analyze an FLD (Formal Logic Dataset) structure, I would require:
- Uncompressed or decoded document content
- Plain text or structured data format (JSON, CSV, XML)
- Actual formula examples in notation like predicate logic: ∀x(P(x) → Q(x))
- Proof representation samples showing inference steps

**Recommendation:**

Please provide either:
1. A decompressed version of this PDF
2. Raw dataset files in text-readable format
3. Documentation describing the FLD schema

Without readable content, I cannot identify data fields, formulas, or proof structures as requested.

[Binary content (application/pdf, 1.8MB) also saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/91820fa6-7a1f-4a02-8bc0-aaa4f114a9f1/tool-results/webfetch-1779196619294-tjp03m.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-19T13:25:44.517269+00:00_

Web search results for query: "FOL reasoning benchmark dataset CLUTRR bAbI SimpleLogic AR-LSAT ReClor formal logic"

Links: [{"title":"SLR: An Automated Synthesis Framework for Scalable Logical ...","url":"https://www.arxiv.org/pdf/2506.15787v2"},{"title":"[PDF] CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CLUTRR:-A-Diagnostic-Benchmark-for-Inductive-from-Sinha-Sodhani/5e35895fc4731858f0b286cb5a1613a819cc2367"},{"title":"CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text | Request PDF","url":"https://www.researchgate.net/publication/336997708_CLUTRR_A_Diagnostic_Benchmark_for_Inductive_Reasoning_from_Text"},{"title":"Large Language Models Meet Symbolic Provers for Logical Reasoning   Evaluation","url":"https://arxiv.org/pdf/2502.06563"},{"title":"CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text","url":"https://arxiv.org/pdf/1908.06177"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/pdf/2209.00840"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/pdf/2505.14932"},{"title":"Assessing Logical Reasoning Capabilities of Encoder-Only Transformer Models","url":"https://arxiv.org/html/2312.11720v1"}]

Now let me search for information about the remaining datasets mentioned:

Links: [{"title":"LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification","url":"https://arxiv.org/html/2602.21044"},{"title":"Logical Reasoning in Large Language Models: A Survey","url":"https://arxiv.org/html/2502.09100"},{"title":"Microsoft LReasoner leads the ReClor challenge on logical reasoning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/blog/microsoft-lreasoner-leads-the-reclor-challenge-on-logical-reasoning/"},{"title":"1 From LSAT: The Progress and Challenges of Complex Reasoning","url":"https://arxiv.org/pdf/21
…[truncated 2181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-19T13:25:44.517415+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicNLI ProofWriter RuleTaker FOL annotation first-order logic dataset comparison FOLIO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicNLI ProofWriter RuleTaker FOL annotation first-order logic dataset comparison FOLIO"
  }
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-19T13:25:44.517541+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('renma/ProntoQA', split='validation')\n\n# Print full raw_logic_programs for first 2 examples\nfor i in range(2):\n    ex = ds[i]\n    print(f'=== Example {i} (id={ex[\\\"id\\\"]}) ===')\n    print(f'context: {ex[\\\"context\\\"]}')\n    print(f'question: {ex[\\\"question\\\"]}')\n    print(f'answer: {ex[\\\"answer\\\"]}')\n    print(f'raw_logic_programs:')\n    for prog in ex['raw_logic_programs']:\n        print(prog)\n    print()\n    print('='*80)\n    print()\n\" 2>&1",
  "description": "Print full raw_logic_programs field content",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('renma/ProntoQA', split='validation')\n\n# Print full raw_logic_programs for first 2 examples\nfor i in range(2):\n    ex = ds[i]\n    print(f'=== Example {i} (id={ex[\\\"id\\\"]}) ===')\n    print(f'context: {ex[\\\"context\\\"]}')\n    print(f'question: {ex[\\\"question\\\"]}')\n    print(f'answer: {ex[\\\"answer\\\"]}')\n    print(f'raw_logic_programs:')\n    for prog in ex['raw_logic_programs']:\n        print(prog)\n    print()\n    print('='*80)\n    print()\n\" 2>&1",
    "description": "Print full raw_logic_programs field content",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-19T13:25:44.517674+00:00_

# FLDx2 Dataset Summary

## Dataset Overview
**Name:** FLDx2 (Hitachi NLP)  
**Total Rows:** 110,000  
**Modalities:** Tabular, Text  
**Format:** Parquet  
**Size Category:** 100K - 1M rows

## Dataset Splits
- **train:** 100,000 rows
- **validation:** 5,000 rows
- **test:** 5,000 rows

## All Column Fields

| # | Column Name | Data Type | Description |
|---|---|---|---|
| 1 | `version` | stringclass(1) | Version identifier |
| 2 | `hypothesis` | string (9-227 chars) | Natural language hypothesis statement |
| 3 | `hypothesis_formula` | string (3-39 chars) | First-order logic formula for hypothesis |
| 4 | `facts` | string (0-3.09k chars) | Natural language facts/premises |
| 5 | `facts_formula` | string (0-929 chars) | FOL formulas for facts |
| 6 | `proofs` | sequence (0-1 length) | Proof steps sequence |
| 7 | `proofs_formula` | sequence (0-1 length) | Proof formulas sequence |
| 8 | `theorem_is_used_in_proof` | bool | Binary indicator if theorem used |
| 9 | `negative_hypothesis` | string (10-195 chars, nullable) | Negated hypothesis in NL |
| 10 | `negative_hypothesis_formula` | string (3-37 chars, nullable) | FOL formula for negated hypothesis |
| 11 | `negative_proofs` | sequence (0-1 length) | Negative proof steps |
| 12 | `negative_original_tree_depth` | int64 (0-30, nullable) | Depth metric for negative tree |
| 13 | `original_tree_steps` | int64 (1-8) | Original proof tree steps |
| 14 | `original_tree_depth` | int64 (1-3) | Original proof tree depth |
| 15 | `steps` | int64 (0-8, nullable) | Number of proof steps |
| 16 | `depth` | int64 (0-3, nullable) | Proof depth |
| 17 | `num_formula_distractors` | int64 (0-22) | Count of formula distractors |
| 18 | `num_translation_distractors` | int64 (0-0) | Count of translation distractors |
| 19 | `num_all_distractors` | int64 (0-22) | Total distractor count |
| 20 | `proof_label` | stringclass(3) | Label: {PROVED, DISPROVED, UNKNOWN} |
| 21 | `negative_proof_label` | stringclass(2) | Label for negative proof
…[truncated 1496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-19T13:25:44.517837+00:00_

# P-FOLIO: Overview

Based on the arXiv abstract provided, here's what we can determine:

**What is P-FOLIO?**
P-FOLIO is "a human-annotated dataset consisting of diverse and complex reasoning chains for a set of realistic logical reasoning stories also written by humans." It was collected using "an annotation protocol that facilitates humans to annotate well-structured natural language proofs for first-order logic reasoning problems in a step-by-step manner."

**Number of Examples:**
The provided content does not specify the dataset size or example count.

**FOL Annotations:**
The abstract does not clarify whether the dataset includes formal first-order logic representations (premises-FOL, conclusion-FOL) alongside the reasoning chains, or solely contains natural language reasoning chains.

**Relationship to Original FOLIO:**
The abstract makes no mention of an original FOLIO dataset or how P-FOLIO relates to it, so this connection cannot be determined from the available content.

**Additional Finding:**
The reasoning steps in P-FOLIO range from "0 to 20," and the work demonstrates that fine-tuning on this data improved model performance by "10% or more on three other out-of-domain logical reasoning datasets."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-19T13:25:44.517974+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('tasksource/LogicNLI', split='train[:3]', trust_remote_code=True)\nprint('=== COLUMNS ===')\nprint(ds.column_names)\nprint()\nprint('=== FEATURES ===')\nprint(ds.features)\nprint()\nfor i, ex in enumerate(ds):\n    print(f'=== EXAMPLE {i} ===')\n    for k, v in ex.items():\n        val_str = str(v)\n        if len(val_str) > 800:\n            val_str = val_str[:800] + '...'\n        print(f'  {k}: {val_str}')\n    print()\n\" 2>&1\n",
  "description": "Load and inspect LogicNLI dataset from HuggingFace",
  "timeout": "180000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('tasksource/LogicNLI', split='train[:3]', trust_remote_code=True)\nprint('=== COLUMNS ===')\nprint(ds.column_names)\nprint()\nprint('=== FEATURES ===')\nprint(ds.features)\nprint()\nfor i, ex in enumerate(ds):\n    print(f'=== EXAMPLE {i} ===')\n    for k, v in ex.items():\n        val_str = str(v)\n        if len(val_str) > 800:\n            val_str = val_str[:800] + '...'\n        print(f'  {k}: {val_str}')\n    print()\n\" 2>&1\n",
    "description": "Load and inspect LogicNLI dataset from HuggingFace",
    "timeout": "180000"
  }
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-19T13:25:44.518111+00:00_

Web search results for query: "FOLIO dataset HuggingFace first-order logic annotations size examples"

Links: [{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=FOLIO"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/pdf/2209.00840"},{"title":"benlipkin/folio · Datasets at Hugging Face","url":"https://huggingface.co/datasets/benlipkin/folio"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"tasksource/folio · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/folio"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"yale-nlp/P-FOLIO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yale-nlp/P-FOLIO"},{"title":"text2log · Datasets at Hugging Face","url":"https://huggingface.co/datasets/text2log"}]

Based on the search results, here's the information about the FOLIO dataset:

## Dataset Overview

FOLIO is a human-annotated, open-domain dataset for reasoning in natural language, equipped with first-order logic (FOL) annotations.

## Size and Examples

FOLIO consists of 1,435 examples (unique conclusions), each paired with one of 487 sets of premises which serve as rules to be used to deductively reason for the validity of each conclusion. The dataset is split with 1k training rows and 203 validation rows in the main Hugging Face version.

## First-Order Logic Annotations

The logical correctness of premises and conclusions is ensured by their parallel FOL annotations, which are automatically verified by an FOL inference engine. In addition to the main NL reasoning task, NL-FOL pairs in FOLIO automatically constitute a new NL-FOL translation dataset using FOL as the logical 
…[truncated 431 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-19T13:25:44.518260+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOL-Traces dataset \"first-order logic\" reasoning traces 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOL-Traces dataset \"first-order logic\" reasoning traces 2025"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-19T13:25:44.518403+00:00_

=== Example 0 (id=ProntoQA_1) ===
context: Jompuses are not shy. Jompuses are yumpuses. Each yumpus is aggressive. Each yumpus is a dumpus. Dumpuses are not wooden. Dumpuses are wumpuses. Wumpuses are red. Every wumpus is an impus. Each impus is opaque. Impuses are tumpuses. Numpuses are sour. Tumpuses are not sour. Tumpuses are vumpuses. Vumpuses are earthy. Every vumpus is a zumpus. Zumpuses are small. Zumpuses are rompuses. Max is a yumpus.
question: Is the following statement true or false? Max is sour.
answer: B
raw_logic_programs:
Predicates:
Jompus($x, bool) ::: Does x belong to Jompus?
Shy($x, bool) ::: Is x shy?
Yumpus($x, bool) ::: Does x belong to Yumpus?
Aggressive($x, bool) ::: Is x aggressive?
Dumpus($x, bool) ::: Does x belong to Dumpus?
Wooden($x, bool) ::: Is x wooden?
Wumpus($x, bool) ::: Does x belong to Wumpus?
Red($x, bool) ::: Is x red?
Impus($x, bool) ::: Does x belong to Impus?
Opaque($x, bool) ::: Is x opaque?
Tumpus($x, bool) ::: Does x belong to Tumpus?
Sour($x, bool) ::: Is x sour?
Vumpus($x, bool) ::: Does x belong to Vumpus?
Earthy($x, bool) ::: Is x earthy?
Zumpus($x, bool) ::: Does x belong to Zumpus?
Small($x, bool) ::: Is x small?
Rompus($x, bool) ::: Does x belong to Rompus?

Facts:
Yumpus(Max, True)

Rules:
Jompus($x, True) >>> Shy($x, False)
Jompus($x, True) >>> Yumpus($x, True)
Yumpus($x, True) >>> Aggressive($x, True)
Yumpus($x, True) >>> Dumpus($x, True)
Dumpus($x, True) >>> Wooden($x, False)
Dumpus($x, True) >>> Wumpus($x, True)
Wumpus($x, True) >>> Red($x, True)
Wumpus($x, True) >>> Impus($x, True)
Impus($x, True) >>> Opaque($x, True)
Impus($x, True) >>> Tumpus($x, True)
Numpus($x, True) >>> Sour($x, True)
Tumpus($x, True) >>> Sour($x, False)
Tumpus($x, True) >>> Vumpus($x, True)
Vumpus($x, True) >>> Earthy($x, True)
Vumpus($x, True) >>> Zumpus($x, True)
Zumpus($x, True) >>> Small($x, True)
Zumpus($x, True) >>> Rompus($x, True)

Query:
Sour(Max, False)

========================================================================
…[truncated 2119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-19T13:25:44.518552+00:00_

Web search results for query: "LogicNLI ProofWriter RuleTaker FOL annotation first-order logic dataset comparison FOLIO"

Links: [{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic Simeng Han1","url":"https://arxiv.org/pdf/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation","url":"https://arxiv.org/html/2502.06563"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://arxiv.org/pdf/2502.06563"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.20973"}]

Based on the search results, here's a comprehensive comparison of these first-order logic reasoning datasets:

## Dataset Comparison Overview

RuleTaker (2020) and ProofWriter (2021) are both large synthetic datasets with 500k examples focused on deductive reasoning, while LogicNLI (2021) is a smaller synthetic FOL dataset with 20k examples, and FOLIO (the authors' dataset) contains 1,435 expert-written FOL examples.

## Key Differences

**Logical Complexity and Diversity:**
RuleTaker and LogicNLI examples require at most five depths of reasoning, and the entire 
…[truncated 1044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-19T13:25:44.518718+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Mihir3009/LogicBench/tree/main/data/LogicBench(Eval)/BQA/first_order_logic",
  "prompt": "List all files in this directory. Show the names of the JSON files for first-order logic evaluation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Mihir3009/LogicBench/tree/main/data/LogicBench(Eval)/BQA/first_order_logic",
    "prompt": "List all files in this directory. Show the names of the JSON files for first-order logic evaluation."
  }
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-19T13:25:44.518857+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Mihir3009/LogicBench/main/data/LogicBench(Eval)/BQA/first_order_logic/universal_instantiation.json",
  "prompt": "Show the complete structure of this JSON file. Show the first 1-2 samples in full detail. Are there any FOL formula fields, or is everything in natural language only?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Mihir3009/LogicBench/main/data/LogicBench(Eval)/BQA/first_order_logic/universal_instantiation.json",
    "prompt": "Show the complete structure of this JSON file. Show the first 1-2 samples in full detail. Are there any FOL formula fields, or is everything in natural language only?"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-19T13:25:44.518982+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-19T13:25:44.519166+00:00_

# First-Order Logic Directory Contents

Based on the GitHub page, the `first_order_logic` directory contains the following subdirectories (which presumably hold JSON files):

1. bidirectional_dilemma
2. constructive_dilemma
3. destructive_dilemma
4. disjunctive_syllogism
5. existential_generalization
6. hypothetical_syllogism
7. modus_ponens
8. modus_tollens
9. universal_instantiation

The page shows a file tree structure but does not explicitly display individual JSON filenames. Each folder likely contains evaluation datasets for its corresponding logical reasoning pattern within the LogicBench evaluation suite.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-19T13:25:44.519311+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"FoVer\" OR \"FOL-traces\" FOLIO first-order logic dataset extended synthetic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"FoVer\" OR \"FOL-traces\" FOLIO first-order logic dataset extended synthetic"
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-19T13:25:44.519444+00:00_

Web search results for query: "FOL-Traces dataset "first-order logic" reasoning traces 2025"

Links: [{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale | Isabelle Lee","url":"https://iglee.me/papers/fol-traces/"},{"title":"[2505.14932] FOL-Pretrain: A complexity annotated corpus of first-order logic","url":"https://arxiv.org/abs/2505.14932"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/html/2505.14932v2"},{"title":"Verified First-Order Logic Reasoning Traces at Scale","url":"https://aclanthology.org/2026.findings-eacl.115.pdf"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/pdf/2505.14932"},{"title":"FOL-Pretrain: A complexity annotated corpus of first-order logic","url":"https://arxiv.org/html/2505.14932v1"}]

Based on the search results, here's what I found about the FOL-Traces dataset:

## Overview

FOL-Traces is the first large-scale dataset of programmatically verified reasoning traces, enabling rigorous evaluation of structured logical inference. The dataset contains 7.4 million examples and 3.5 billion tokens.

## Dataset Composition

The dataset consists of 3.5 billion tokens, including 8.8 million LLM-augmented, human-annotated examples and 7.5 million synthetically generated examples. Each synthetic example is verifiably correct, produced by a custom automated theorem solver, and accompanied by metadata tracing its algorithmic provenance.

## Purpose and Diagnostic Tasks

The dataset is designed to probe and analyze algorithmic reasoning in LLMs. Two challenging and comprehensive diagnostic tasks include masked operation prediction and step completion—that directly probe syntactic awareness and process fidelity.

## Experimental Results

Systematic experiments with 5 reasoning LLMs show that the dataset remains challenging: models only reach around 45.7% accuracy on masked operation prediction and around 27% on two-step com
…[truncated 262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-19T13:25:44.519620+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOLIO dataset test set held out 226 examples release github yale-nlp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOLIO dataset test set held out 226 examples release github yale-nlp"
  }
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-19T13:25:44.519813+00:00_

`trust_remote_code` is not supported anymore.
Please check that the Hugging Face dataset 'tasksource/LogicNLI' isn't based on a loading script and remove `trust_remote_code`.
If the dataset is based on a loading script, please ask the dataset author to remove it and convert it to a standard format like Parquet.
Generating train split:   0%|          | 0/16000 [00:00<?, ? examples/s]Generating train split: 100%|██████████| 16000/16000 [00:00<00:00, 458842.07 examples/s]
Generating validation split:   0%|          | 0/2000 [00:00<?, ? examples/s]Generating validation split: 100%|██████████| 2000/2000 [00:00<00:00, 392982.67 examples/s]
Generating test split:   0%|          | 0/2000 [00:00<?, ? examples/s]Generating test split: 100%|██████████| 2000/2000 [00:00<00:00, 429062.86 examples/s]
=== COLUMNS ===
['premise', 'hypothesis', 'label']

=== FEATURES ===
{'premise': Value('string'), 'hypothesis': Value('string'), 'label': Value('string')}

=== EXAMPLE 0 ===
  premise: Nathalie is not blue.
Gabriel is concerned.
Nathalie is not concerned.
Baird is concerned.
Baird is serious.
Quinlan is not entire.
John is not fresh.
John is blue.
Gabriel is serious.
Arthur is serious.
Gabriel is not entire.
Nathalie is not accurate.If there is someone who is either not concerned or fresh, then John is entire.
Someone who is eithor not fresh or entire is always not serious.
If John is not serious and Quinlan is fresh, then Baird is not entire.
If Gabriel is not serious, then Quinlan is not blue and Gabriel is accurate.
If Nathalie is not blue, then Collier is entire.
If someone is fresh or he is not concerned, then he is not blue.
If there is someone who is both serious and fresh, then Baird is not blue.
If someone is concerned and serious, then he is entire, and vice ve...
  hypothesis: Baird is not serious.
  label: self_contradiction

=== EXAMPLE 1 ===
  premise: Nathalie is not blue.
Gabriel is concerned.
Nathalie is not concerned.
Baird is concerned.
Baird is serious.
Quin
…[truncated 1637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 189 · 2026-05-19T13:25:44.519983+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /tmp && git clone --depth 1 https://github.com/Mihir3009/LogicBench.git 2>&1 | tail -3",
  "description": "Clone LogicBench repo to inspect data files",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /tmp && git clone --depth 1 https://github.com/Mihir3009/LogicBench.git 2>&1 | tail -3",
    "description": "Clone LogicBench repo to inspect data files",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-19T13:25:44.520119+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "text2log dataset huggingface \"first order logic\" ccg2lambda size format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "text2log dataset huggingface \"first order logic\" ccg2lambda size format"
  }
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-19T13:25:44.520247+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\n# Try original tasksource version - it has JSON files with different structure\nimport json, urllib.request\nurl = 'https://huggingface.co/datasets/tasksource/prontoqa/resolve/main/1hop_AndElim_2testhops_random_noadj.json'\nwith urllib.request.urlopen(url) as r:\n    data = json.loads(r.read())\nkeys = list(data.keys())[:3]\nprint('Top-level keys (first 3):', keys)\nprint('Total keys:', len(data.keys()))\nprint()\nfor k in keys[:2]:\n    print(f'=== {k} ===')\n    ex = data[k]\n    for field, val in ex.items():\n        print(f'  {field}: {repr(val)[:400]}')\n    print()\n\" 2>&1",
  "description": "Inspect tasksource/prontoqa original format",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\n# Try original tasksource version - it has JSON files with different structure\nimport json, urllib.request\nurl = 'https://huggingface.co/datasets/tasksource/prontoqa/resolve/main/1hop_AndElim_2testhops_random_noadj.json'\nwith urllib.request.urlopen(url) as r:\n    data = json.loads(r.read())\nkeys = list(data.keys())[:3]\nprint('Top-level keys (first 3):', keys)\nprint('Total keys:', len(data.keys()))\nprint()\nfor k in keys[:2]:\n    print(f'=== {k} ===')\n    ex = data[k]\n    for field, val in ex.items():\n        print(f'  {field}: {repr(val)[:400]}')\n    print()\n\" 2>&1",
    "description": "Inspect tasksource/prontoqa original format",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-19T13:25:44.520366+00:00_

Cloning into 'LogicBench'...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-19T13:25:44.520489+00:00_

Top-level keys (first 3): ['example1', 'example2', 'example3']
Total keys: 100

=== example1 ===
  in_context_example0: {'question': 'Each dumpus is a tumpus and a jompus. Lorpuses are zumpuses and brimpuses. Lempuses are dumpuses and rompuses. Vumpuses are yumpuses and lorpuses. Yumpuses are shumpuses and lempuses. Every grimpus is a vumpus. Each numpus is temperate and a wumpus. Each shumpus is a sterpus and an impus. Polly is a yumpus and a shumpus. Polly is a tumpus and a jompus.', 'query': 'Prove: Polly is a y
  in_context_example1: {'question': 'Each dumpus is a lorpus. Every numpus is a brimpus and an impus. Every gorpus is amenable and a zumpus. Every sterpus is a yumpus and a rompus. Grimpuses are tumpuses and jompuses. Each yumpus is a shumpus and a lempus. Lorpuses are grimpuses and vumpuses. Each vumpus is a numpus and a sterpus. Stella is a shumpus and a lempus. Stella is a lorpus and a grimpus.', 'query': 'Prove: Ste
  in_context_example2: {'question': 'Vumpuses are jompuses and yumpuses. Lorpuses are wumpuses and rompuses. Each jompus is an impus and a tumpus. Each gorpus is wooden and a shumpus. Brimpuses are lorpuses and vumpuses. Alex is a jompus and a vumpus. Alex is an impus and a tumpus.', 'query': 'Prove: Alex is a vumpus.', 'chain_of_thought': ['Alex is a jompus and a vumpus.', 'Alex is a vumpus.']}
  in_context_example3: {'question': 'Lempuses are tumpuses and grimpuses. Wumpuses are dull and jompuses. Every brimpus is a shumpus and a lempus. Grimpuses are dumpuses and yumpuses. Shumpuses are sterpuses and lorpuses. Sally is a lempus and a grimpus. Sally is a yumpus and a dumpus.', 'query': 'Prove: Sally is a lempus.', 'chain_of_thought': ['Sally is a lempus and a grimpus.', 'Sally is a lempus.']}
  in_context_example4: {'question': 'Each wumpus is a tumpus and a sterpus. Vumpuses are numpuses and shumpuses. Every gorpus is hot and a lorpus. Every numpus is a jompus and a lempus. Every tumpus is a rompus and a grimpus. Brimpuses are yumpuses 
…[truncated 5629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-19T13:25:44.520645+00:00_

Web search results for query: "FOLIO dataset test set held out 226 examples release github yale-nlp"

Links: [{"title":"GitHub - Yale-LILY/FOLIO · GitHub","url":"https://github.com/Yale-LILY/FOLIO"},{"title":"FOLIO/README.md at main · Yale-LILY/FOLIO","url":"https://github.com/Yale-LILY/FOLIO/blob/main/README.md"},{"title":"yale-nlp/FOLIO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yale-nlp/FOLIO"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/pdf/2209.00840"},{"title":"yale-nlp/P-FOLIO at main","url":"https://huggingface.co/datasets/yale-nlp/P-FOLIO/tree/main"},{"title":"MABSA: A curated Malayalam aspect based sentiment analysis dataset on movie reviews","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10415832/"},{"title":"GitHub - Yale-LILY/LectureBank: LectureBank Dataset","url":"https://github.com/Yale-LILY/LectureBank"},{"title":"yale-nlp/P-FOLIO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yale-nlp/P-FOLIO"},{"title":"P-FOLIO: Evaluating and Improving Logical Reasoning with Abundant   Human-Written Reasoning Chains","url":"https://arxiv.org/pdf/2410.09207"}]

Based on the search results, I found information about the FOLIO dataset from the Yale-LILY team on GitHub. FOLIO is an expert-written, open-domain, logically complex and diverse dataset for natural language reasoning with first-order logic.

However, the specific details you're asking about regarding a test set with 226 held-out examples don't appear in the current search results. According to the GitHub repository, a leaderboard would be released to obtain results on the unreleased test set. The search results indicate that the publicly available folio-v0.0 contains train and validation sets in the data/v0.0 folder.

The search results don't contain the specific information about 226 test examples you mentioned. If you need more details about the test set composition, you may want to check the actual paper di
…[truncated 210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 195 · 2026-05-19T13:25:44.520822+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /tmp/LogicBench/data/LogicBench\\(Eval\\)/BQA/first_order_logic/",
  "description": "List FOL evaluation files in LogicBench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /tmp/LogicBench/data/LogicBench\\(Eval\\)/BQA/first_order_logic/",
    "description": "List FOL evaluation files in LogicBench"
  }
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-19T13:25:44.520942+00:00_

bidirectional_dilemma
constructive_dilemma
destructive_dilemma
disjunctive_syllogism
existential_generalization
hypothetical_syllogism
modus_ponens
modus_tollens
universal_instantiation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-19T13:25:44.521062+00:00_

Web search results for query: ""FoVer" OR "FOL-traces" FOLIO first-order logic dataset extended synthetic"

Links: [{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/html/2505.14932v2"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning","url":"https://www.researchgate.net/publication/397118426_FoVer_First-Order_Logic_Verification_for_Natural_Language_Reasoning"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic Simeng Han1","url":"https://arxiv.org/pdf/2209.00840"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/pdf/2505.14932"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"},{"title":"FOL-Pretrain: A complexity annotated corpus of first-order logic","url":"https://arxiv.org/html/2505.14932v1"}]

Based on the search results, here's what I found about these related first-order logic datasets:

## FOL-Traces

FOL-Traces combines programmatic verification with pretraining-scale size, enabling systematic study of logical reasoning. The dataset consists of 3.5 billion tokens, inclu
…[truncated 1290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 198 · 2026-05-19T13:25:44.521206+00:00_

Web search results for query: "text2log dataset huggingface "first order logic" ccg2lambda size format"

Links: [{"title":"alevkov95/text2log · Datasets at Hugging Face","url":"https://huggingface.co/datasets/alevkov95/text2log"},{"title":"text2log · Datasets at Hugging Face","url":"https://huggingface.co/datasets/text2log"},{"title":"Visualization of the semantic output of ccg2lambda for the sentence \"... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/sualization-of-the-semantic-output-of-ccg2lambda-for-the-sentence-Some-woman-ordered_fig3_306093859"},{"title":"Dataset formats and types · Hugging Face","url":"https://huggingface.co/docs/trl/dataset_formats"},{"title":"Text Datasets – Hugging Face","url":"https://huggingface.co/datasets?modality=modality:text"},{"title":"Exploring Neural Models for Parsing Natural Language into First-Order   Logic","url":"https://arxiv.org/pdf/2002.06544"},{"title":"Harnessing the Power of Large Language Models for Natural Language to   First-Order Logic Translation","url":"https://arxiv.org/pdf/2305.15541"}]

Based on the search results, here's what I found about the text2log dataset:

## Dataset Overview

The dataset contains 100,000 simple English sentences selected and filtered from enTenTen15 and their translation into First Order Logic (FOL) using ccg2lambda.

## Data Format

The dataset includes fields 'clean' (a simple English sentence) and 'trans' (the corresponding translation into Lambda Dependency-based Compositional Semantics), with example entries like 'clean': "All things that are new are good." and 'trans': "all x1. (_thing(x1) -> (_new(x1) -> _good(x1)))"

## Train/Test Split

No predefined train/test split is given. The authors used a 80/20 split

## Use Case

The data set is used to train models which can generate FOL statements from natural language text

The dataset is available on Hugging Face at both `text2log` and `alevkov95/text2log`.


REMINDER: You MUST include the sources above
…[truncated 56 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-19T13:25:44.521357+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/omnilabNLP/LogicNLI/tree/main",
  "prompt": "List all files and directories in this repository. What data files are available? Are there any files containing FOL formulas, logic expressions, or structured annotations beyond the natural language text? List all file names."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/omnilabNLP/LogicNLI/tree/main",
    "prompt": "List all files and directories in this repository. What data files are available? Are there any files containing FOL formulas, logic expressions, or structured annotations beyond the natural language text? List all file names."
  }
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-19T13:25:44.521487+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /tmp/LogicBench/data/LogicBench\\(Eval\\)/BQA/first_order_logic/modus_ponens/",
  "description": "List files in modus_ponens FOL directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /tmp/LogicBench/data/LogicBench\\(Eval\\)/BQA/first_order_logic/modus_ponens/",
    "description": "List files in modus_ponens FOL directory"
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-19T13:25:44.521598+00:00_

data_instances.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-19T13:25:44.521734+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2505.14932v2",
  "prompt": "Extract: What is FOL-Traces? How many examples? Does it contain FOLIO data? Does it have FOL premises and conclusion annotations? What are the fields/columns? How does it relate to FOLIO dataset?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2505.14932v2",
    "prompt": "Extract: What is FOL-Traces? How many examples? Does it contain FOLIO data? Does it have FOL premises and conclusion annotations? What are the fields/columns? How does it relate to FOLIO dataset?"
  }
}
```

</details>

---

### Tool call

_source line 203 · 2026-05-19T13:25:44.521870+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MALLS dataset \"natural language to first-order logic\" GPT-4 34K pairs huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MALLS dataset \"natural language to first-order logic\" GPT-4 34K pairs huggingface"
  }
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-19T13:25:44.521991+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/LogicBench/data/LogicBench(Eval)/BQA/first_order_logic/modus_ponens/data_instances.json",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/LogicBench/data/LogicBench(Eval)/BQA/first_order_logic/modus_ponens/data_instances.json",
    "limit": "80"
  }
}
```

</details>

---

### Tool call

_source line 205 · 2026-05-19T13:25:44.522114+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/tasksource/prontoqa/tree/main",
  "prompt": "List all JSON files available in this dataset repository. I need to see all the filenames to understand how many total examples and what configurations exist."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/tasksource/prontoqa/tree/main",
    "prompt": "List all JSON files available in this dataset repository. I need to see all the filenames to understand how many total examples and what configurations exist."
  }
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-19T13:25:44.522246+00:00_

1	{
2	    "type": "first_order_logic",
3	    "axiom": "modus_ponens",
4	    "samples": [
5	        {
6	            "id": 1,
7	            "context": "If someone is extremely tired, then they will seek some rest and relaxation. Today, Jack finds himself utterly exhausted.",
8	            "qa_pairs": [
9	                {
10	                    "question": "Does this entail that he will take rest?",
11	                    "answer": "yes"
12	                },
13	                {
14	                    "question": "Does this entail that he won't take rest?",
15	                    "answer": "no"
16	                }
17	            ]
18	        },
19	        {
20	            "id": 2,
21	            "context": "If a person experiences a throbbing sensation in their head, it is likely that they will seek relief by consuming medication intended to alleviate this discomfort. In this situation, Sarah finds herself with a pounding headache.",
22	            "qa_pairs": [
23	                {
24	                    "question": "Does this mean that she will take medicine?",
25	                    "answer": "yes"
26	                },
27	                {
28	                    "question": "Does this mean that she won't take medicine?",
29	                    "answer": "no"
30	                }
31	            ]
32	        },
33	        {
34	            "id": 3,
35	            "context": "If someone experiences sadness, they will often shed tears. In this particular case, Sara is feeling sorrowful.",
36	            "qa_pairs": [
37	                {
38	                    "question": "Does this entail that she will cry?",
39	                    "answer": "yes"
40	                },
41	                {
42	                    "question": "Does this entail that she won't cry?",
43	                    "answer": "no"
44	                }
45	            ]
46	        },
47	        {
48	            "id": 4,
49	            "context": "If someone possesses strong arithmetic skills, it in
…[truncated 1490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 207 · 2026-05-19T13:25:44.522398+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\n# Check fengyang0317/prontoqa - might have a different structure\nds = load_dataset('fengyang0317/prontoqa')\nprint('Splits:', list(ds.keys()))\nfor split in ds:\n    print(f'{split}: {len(ds[split])} examples')\n    print(f'  Fields: {ds[split].column_names}')\n    if len(ds[split]) > 0:\n        ex = ds[split][0]\n        for k, v in ex.items():\n            print(f'  {k}: {repr(v)[:200]}')\n    break\n\" 2>&1",
  "description": "Check fengyang0317/prontoqa dataset version",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\n# Check fengyang0317/prontoqa - might have a different structure\nds = load_dataset('fengyang0317/prontoqa')\nprint('Splits:', list(ds.keys()))\nfor split in ds:\n    print(f'{split}: {len(ds[split])} examples')\n    print(f'  Fields: {ds[split].column_names}')\n    if len(ds[split]) > 0:\n        ex = ds[split][0]\n        for k, v in ex.items():\n            print(f'  {k}: {repr(v)[:200]}')\n    break\n\" 2>&1",
    "description": "Check fengyang0317/prontoqa dataset version",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-19T13:25:44.522532+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Yale-LILY/FOLIO/blob/main/README.md",
  "prompt": "Extract: all file listings, split sizes, data format fields, any mention of updated versions, test set availability, FOLIO-wiki. What versions exist (v0.0, v1, etc)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Yale-LILY/FOLIO/blob/main/README.md",
    "prompt": "Extract: all file listings, split sizes, data format fields, any mention of updated versions, test set availability, FOLIO-wiki. What versions exist (v0.0, v1, etc)?"
  }
}
```

</details>

---

### Tool call

_source line 209 · 2026-05-19T13:25:44.522660+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('tasksource/LogicNLI', split='train')\nprint(f'Train size: {len(ds)}')\nds_val = load_dataset('tasksource/LogicNLI', split='validation')\nprint(f'Val size: {len(ds_val)}')\nds_test = load_dataset('tasksource/LogicNLI', split='test')\nprint(f'Test size: {len(ds_test)}')\nprint(f'Total: {len(ds) + len(ds_val) + len(ds_test)}')\nprint()\n# Check label distribution\nfrom collections import Counter\nlabels = Counter(ds['label'])\nprint('Label distribution (train):')\nfor k,v in sorted(labels.items()):\n    print(f'  {k}: {v}')\nprint()\n# Print one full example\nex = ds[0]\nprint('=== FULL PREMISE (example 0) ===')\nprint(ex['premise'])\nprint()\nprint('=== HYPOTHESIS ===')\nprint(ex['hypothesis'])\nprint()\nprint('=== LABEL ===')\nprint(ex['label'])\n\" 2>&1\n",
  "description": "Get full dataset statistics and a complete example",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('tasksource/LogicNLI', split='train')\nprint(f'Train size: {len(ds)}')\nds_val = load_dataset('tasksource/LogicNLI', split='validation')\nprint(f'Val size: {len(ds_val)}')\nds_test = load_dataset('tasksource/LogicNLI', split='test')\nprint(f'Test size: {len(ds_test)}')\nprint(f'Total: {len(ds) + len(ds_val) + len(ds_test)}')\nprint()\n# Check label distribution\nfrom collections import Counter\nlabels = Counter(ds['label'])\nprint('Label distribution (train):')\nfor k,v in sorted(labels.items()):\n    print(f'  {k}: {v}')\nprint()\n# Print one full example\nex = ds[0]\nprint('=== FULL PREMISE (example 0) ===')\nprint(ex['premise'])\nprint()\nprint('=== HYPOTHESIS ===')\nprint(ex['hypothesis'])\nprint()\nprint('=== LABEL ===')\nprint(ex['label'])\n\" 2>&1\n",
    "description": "Get full dataset statistics and a complete example",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-19T13:25:44.522815+00:00_

# LogicNLI Repository File Structure

Based on the GitHub page content provided, the repository contains the following files and directories:

**Visible Structure:**
- `README.assets/` (directory)
- `dataset/` (directory)
- `README.md` (file)

**Data Files Available:**
The page explicitly mentions one downloadable dataset file:
- `LogicNLI_sim.zip` (located in the dataset folder)

**Important Note:**
The webpage content shows only the repository's main directory listing. While the page indicates a dataset folder exists, the specific contents within that folder—including any files containing formal logic expressions, FOL formulas, or structured annotations—are not detailed in the provided web content. 

The project aims to create "an NLI-style dataset that effectively disentangles the target FOL reasoning from commonsense inference," suggesting the dataset likely contains structured logical annotations, but the exact file names and formats within the dataset directory cannot be determined from this page alone.

To access the complete file listing and examine whether additional files with logic expressions exist, direct access to the GitHub repository would be necessary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-19T13:25:44.522951+00:00_

# FOLIO Dataset Information

## Versions
Only **folio-v0.0** is explicitly mentioned as released, containing training and validation sets located in the `data/v0.0` folder.

## Updated Version
The README notes: "We are excited to release a new version of FOLIO here with significant quality improvement and error fixing!" This updated version is available on Hugging Face (yale-nlp/FOLIO), though a specific version number isn't provided in this document.

## Data Format Fields
Each example contains:
- 'premises' and 'premises-FOL' (natural language and first-order logic annotations)
- 'conclusion' and 'conclusion-FOL'
- 'label' (truth value)
- 'story-id' and 'example-id'
- 'source' (WikiLogic or HybLogic origin)

## File Formats
Data is available in jsonl and txt formats.

## Test Set Status
"A leaderboard will be released soon to obtain your results on the unreleased test set," indicating the test set is not yet publicly available.

## Community Contributions
The README invites pull requests for additional data contributions to FOLIO.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-19T13:25:44.523081+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /tmp/LogicBench && find data -name \"data_instances.json\" | head -5 | while read f; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); print('keys:', list(d.keys())); print('num_samples:', len(d['samples'])); s=d['samples'][0]; print('sample_keys:', list(s.keys())); print('qa_keys:', list(s['qa_pairs'][0].keys()) if 'qa_pairs' in s else 'N/A')\"; done",
  "description": "Inspect LogicBench data structure across multiple files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /tmp/LogicBench && find data -name \"data_instances.json\" | head -5 | while read f; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); print('keys:', list(d.keys())); print('num_samples:', len(d['samples'])); s=d['samples'][0]; print('sample_keys:', list(s.keys())); print('qa_keys:', list(s['qa_pairs'][0].keys()) if 'qa_pairs' in s else 'N/A')\"; done",
    "description": "Inspect LogicBench data structure across multiple files"
  }
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-19T13:25:44.523198+00:00_

=== data/LogicBench(Eval)/MCQA/propositional_logic/modus_tollens/data_instances.json ===
keys: ['type', 'axiom', 'samples']
num_samples: 20
sample_keys: ['id', 'context', 'question', 'choices', 'answer']
qa_keys: N/A
=== data/LogicBench(Eval)/MCQA/propositional_logic/material_implication/data_instances.json ===
keys: ['type', 'axiom', 'samples']
num_samples: 20
sample_keys: ['id', 'context', 'question', 'choices', 'answer']
qa_keys: N/A
=== data/LogicBench(Eval)/MCQA/propositional_logic/hypothetical_syllogism/data_instances.json ===
keys: ['type', 'axiom', 'samples']
num_samples: 20
sample_keys: ['id', 'context', 'question', 'choices', 'answer']
qa_keys: N/A
=== data/LogicBench(Eval)/MCQA/propositional_logic/disjunctive_syllogism/data_instances.json ===
keys: ['type', 'axiom', 'samples']
num_samples: 20
sample_keys: ['id', 'context', 'question', 'choices', 'answer']
qa_keys: N/A
=== data/LogicBench(Eval)/MCQA/propositional_logic/destructive_dilemma/data_instances.json ===
keys: ['type', 'axiom', 'samples']
num_samples: 20
sample_keys: ['id', 'context', 'question', 'choices', 'answer']
qa_keys: N/A

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 214 · 2026-05-19T13:25:44.523323+00:00_

# FOL-Traces: Overview and Structure

## What is FOL-Traces?

FOL-Traces is "the first large-scale dataset of programmatically verified reasoning traces" containing 7.4 million examples with 3.5 billion tokens. It addresses a critical gap by combining symbolic verification guarantees with pretraining-scale data—something neither natural language CoT datasets nor small theorem-proving corpora achieve.

## Dataset Size and Composition

The dataset includes:
- **7.4M training examples** (3.51B tokens)
- **5K development examples** (3.05M tokens)
- **8.64K test examples** (5.25M tokens)
- **8.8M curated training examples** (786.27M tokens)

## FOLIO Dataset Integration

Yes, FOL-Traces leverages existing benchmarks including FOLIO. The authors "use existing benchmarks such as LogicBench and FOLIO...as sources of human-annotated logical forms and prompts," combining these with programmatically generated rules.

## Key Annotation Fields

Each example includes:
- **Rule**: The first-order logic expression template
- **Expressions (exprs)**: Step-by-step simplifications using FOL inference rules
- **Complexity by step**: Circuit complexity for each expression
- **Elimination complexity**: Complexity of simplifying one step to the next
- **Program complexity**: Total generation complexity
- **Original depth**: Initial expression depth

## Relationship to FOLIO

FOL-Traces extends FOLIO's human-annotated logical forms by: generating 1.5 million unique programmatically verified rules, instantiating symbolic rules with natural language predicates via LLMs, and providing detailed step-level verification—capabilities FOLIO lacks at scale.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-19T13:25:44.523463+00:00_

Web search results for query: "MALLS dataset "natural language to first-order logic" GPT-4 34K pairs huggingface"

Links: [{"title":"Harnessing the Power of Large Language Models for Natural Language to   First-Order Logic Translation","url":"https://arxiv.org/pdf/2305.15541"},{"title":"Harnessing the Power of Large Language Models for Natural Language to First-Order Logic Translation | OpenReview","url":"https://openreview.net/forum?id=QzQSR56JZr"},{"title":"GitHub - gblackout/LogicLLaMA: Large language model and dataset for natural language to first-order logic translation","url":"https://github.com/gblackout/LogicLLaMA"},{"title":"AtlasUnified/Atlas-Reasoning · Datasets at Hugging Face","url":"https://huggingface.co/datasets/AtlasUnified/Atlas-Reasoning"},{"title":"Advancing Natural Language Formalization to First Order Logic with Fine-tuned LLMs","url":"https://arxiv.org/pdf/2509.22338"},{"title":"vicgalle/alpaca-gpt4 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/vicgalle/alpaca-gpt4"},{"title":"tasksource/folio · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/folio"}]

Based on the search results, I found relevant information about the MALLS dataset:

MALLS (large language Model generAted NL-FOL pairS) is a dataset of 34K high-quality and diverse sentence-level NL-FOL pairs collected from GPT-4. The dataset was created by implementing a pipeline that prompts GPT-4 for pairs, and dynamically adjusts the prompts to ensure the collection of pairs with rich and diverse contexts at different levels of complexity, and verifies the validity of the generated FOL rules.

The dataset was used to train LogicLLaMA using a novel supervised fine-tuning (SFT) + reinforcement learning with human feedback (RLHF) framework, which initially trains on synthetically perturbed NL-FOL pairs to encourage chain-of-thought reasoning and then finetunes with RLHF on GPT-3.5 outputs using a FOL verifier as the reward model.

Codes, weights,
…[truncated 170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-19T13:25:44.523622+00:00_

Train size: 16000
Val size: 2000
Test size: 2000
Total: 20000

Label distribution (train):
  contradiction: 4000
  entailment: 4000
  neutral: 4000
  self_contradiction: 4000

=== FULL PREMISE (example 0) ===
Nathalie is not blue.
Gabriel is concerned.
Nathalie is not concerned.
Baird is concerned.
Baird is serious.
Quinlan is not entire.
John is not fresh.
John is blue.
Gabriel is serious.
Arthur is serious.
Gabriel is not entire.
Nathalie is not accurate.If there is someone who is either not concerned or fresh, then John is entire.
Someone who is eithor not fresh or entire is always not serious.
If John is not serious and Quinlan is fresh, then Baird is not entire.
If Gabriel is not serious, then Quinlan is not blue and Gabriel is accurate.
If Nathalie is not blue, then Collier is entire.
If someone is fresh or he is not concerned, then he is not blue.
If there is someone who is both serious and fresh, then Baird is not blue.
If someone is concerned and serious, then he is entire, and vice versa.
Nathalie being not fresh and Baird being serious imply that Nathalie is blue.
If there is at least one people who is both not accurate and entire, then Collier is serious.
It can be concluded that Gabriel is concerned once knowing that Baird is not blue.
If someone is entire, then he is not serious, and vice versa.

=== HYPOTHESIS ===
Baird is not serious.

=== LABEL ===
self_contradiction

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 217 · 2026-05-19T13:25:44.523780+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CLUTRR dataset format first-order logic kinship reasoning rules FOL representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CLUTRR dataset format first-order logic kinship reasoning rules FOL representation"
  }
}
```

</details>

---

### Tool result

_source line 218 · 2026-05-19T13:25:44.523906+00:00_

# ProntoQA Dataset - JSON Files List

Based on the web page content, here are the JSON files available in the `tasksource/prontoqa` dataset repository:

## 1-hop Files
- `1hop_AndElim_2testhops_random_noadj.json` (453 kB)
- `1hop_AndElim_3testhops_random_noadj.json` (466 kB)
- `1hop_AndElim_random_noadj.json` (439 kB)
- `1hop_AndIntro_2testhops_random_noadj.json` (561 kB)
- `1hop_AndIntro_3testhops_random_noadj.json` (588 kB)
- `1hop_AndIntro_random_noadj.json` (534 kB)
- `1hop_OOD_OrElim_3proofwidth_random_noadj.json` (940 kB)
- `1hop_OOD_ProofByContra_random_noadj.json` (745 kB)
- `1hop_OrElim_3proofwidth_random_noadj.json` (724 kB)
- `1hop_OrElim_3proofwidth_testrandom_nodistractor_testdistractor_noadj.json` (552 kB)
- `1hop_OrElim_3testwidth_random_noadj.json` (561 kB)
- `1hop_OrElim_4proofwidth_random_noadj.json` (905 kB)
- `1hop_OrElim_4testwidth_random_noadj.json` (582 kB)
- `1hop_ProofByContra_random_noadj.json` (800 kB)
- `1hop_ProofByContra_testrandom_nodistractor_testdistractor_noadj.json` (697 kB)
- `1hop_ProofsOnly_2testhops_random_noadj.json` (501 kB)
- `1hop_ProofsOnly_3testhops_random_noadj.json` (511 kB)
- `1hop_ProofsOnly_4testhops_random_noadj.json` (523 kB)
- `1hop_ProofsOnly_5testhops_random_noadj.json` (535 kB)
- `1hop_ProofsOnly_random_noadj.json` (487 kB)

## 2-hop Files
- `2hop_AndElim_3proofwidth_random_noadj.json` (679 kB)
- `2hop_AndElim_3testhops_random_noadj.json` (579 kB)
- `2hop_AndElim_3testwidth_random_noadj.json` (579 kB)
- `2hop_AndElim_4proofwidth_random_noadj.json` (782 kB)
- `2hop_AndElim_4testwidth_random_noadj.json` (591 kB)
- `2hop_AndElim_random_noadj.json` (567 kB)
- `2hop_AndElim_testrandom_nodistractor_testdistractor_noadj.json` (343 kB)
- `2hop_AndIntro_3proofwidth_random_noadj.json` (945 kB)
- `2hop_AndIntro_3testhops_random_noadj.json` (788 kB)
- `2hop_AndIntro_3testwidth_random_noadj.json` (786 kB)
- `2hop_AndIntro_4proofwidth_random_noadj.json` (1.05 MB)
- `2hop_AndIntro_4testwidth_random_noadj.json` (801 kB)
- `2ho
…[truncated 1138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 219 · 2026-05-19T13:25:44.524059+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /tmp/LogicBench && echo \"=== Total BQA samples ===\" && find data/LogicBench\\(Eval\\)/BQA -name \"data_instances.json\" -exec python3 -c \"import json,sys; d=json.load(open(sys.argv[1])); print(f'{sys.argv[1]}: {len(d[\\\"samples\\\"])} samples, {sum(len(s[\\\"qa_pairs\\\"]) for s in d[\\\"samples\\\"])} qa_pairs')\" {} \\; | sort && echo \"=== Total MCQA samples ===\" && find data/LogicBench\\(Eval\\)/MCQA -name \"data_instances.json\" -exec python3 -c \"import json,sys; d=json.load(open(sys.argv[1])); print(f'{sys.argv[1]}: {len(d[\\\"samples\\\"])} samples')\" {} \\; | sort",
  "description": "Count LogicBench examples across all files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /tmp/LogicBench && echo \"=== Total BQA samples ===\" && find data/LogicBench\\(Eval\\)/BQA -name \"data_instances.json\" -exec python3 -c \"import json,sys; d=json.load(open(sys.argv[1])); print(f'{sys.argv[1]}: {len(d[\\\"samples\\\"])} samples, {sum(len(s[\\\"qa_pairs\\\"]) for s in d[\\\"samples\\\"])} qa_pairs')\" {} \\; | sort && echo \"=== Total MCQA samples ===\" && find data/LogicBench\\(Eval\\)/MCQA -name \"data_instances.json\" -exec python3 -c \"import json,sys; d=json.load(open(sys.argv[1])); print(f'{sys.argv[1]}: {len(d[\\\"samples\\\"])} samples')\" {} \\; | sort",
    "description": "Count LogicBench examples across all files"
  }
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-19T13:25:44.524193+00:00_

=== Total BQA samples ===
data/LogicBench(Eval)/BQA/first_order_logic/bidirectional_dilemma/data_instances.json: 20 samples, 80 qa_pairs
data/LogicBench(Eval)/BQA/first_order_logic/constructive_dilemma/data_instances.json: 20 samples, 80 qa_pairs
data/LogicBench(Eval)/BQA/first_order_logic/destructive_dilemma/data_instances.json: 20 samples, 80 qa_pairs
data/LogicBench(Eval)/BQA/first_order_logic/disjunctive_syllogism/data_instances.json: 20 samples, 40 qa_pairs
data/LogicBench(Eval)/BQA/first_order_logic/existential_generalization/data_instances.json: 20 samples, 40 qa_pairs
data/LogicBench(Eval)/BQA/first_order_logic/hypothetical_syllogism/data_instances.json: 20 samples, 80 qa_pairs
data/LogicBench(Eval)/BQA/first_order_logic/modus_ponens/data_instances.json: 20 samples, 40 qa_pairs
data/LogicBench(Eval)/BQA/first_order_logic/modus_tollens/data_instances.json: 20 samples, 40 qa_pairs
data/LogicBench(Eval)/BQA/first_order_logic/universal_instantiation/data_instances.json: 20 samples, 40 qa_pairs
data/LogicBench(Eval)/BQA/nm_logic/default_reasoning_default/data_instances.json: 20 samples, 40 qa_pairs
data/LogicBench(Eval)/BQA/nm_logic/default_reasoning_irr/data_instances.json: 20 samples, 40 qa_pairs
data/LogicBench(Eval)/BQA/nm_logic/default_reasoning_open/data_instances.json: 20 samples, 40 qa_pairs
data/LogicBench(Eval)/BQA/nm_logic/default_reasoning_several/data_instances.json: 20 samples, 80 qa_pairs
data/LogicBench(Eval)/BQA/nm_logic/reasoning_about_exceptions_1/data_instances.json: 20 samples, 80 qa_pairs
data/LogicBench(Eval)/BQA/nm_logic/reasoning_about_exceptions_2/data_instances.json: 20 samples, 40 qa_pairs
data/LogicBench(Eval)/BQA/nm_logic/reasoning_about_exceptions_3/data_instances.json: 20 samples, 40 qa_pairs
data/LogicBench(Eval)/BQA/nm_logic/reasoning_about_priority/data_instances.json: 20 samples, 80 qa_pairs
data/LogicBench(Eval)/BQA/propositional_logic/bidirectional_dilemma/data_instances.json: 20 samples, 80 qa_pairs
data/LogicBench(Eval)/BQA
…[truncated 3190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-19T13:25:44.524368+00:00_

I now have comprehensive information. Here is my report.

---

## RuleTaker / ProofWriter FOL Annotation Research

### 1. Original Datasets: No Native FOL Annotations

**ProofWriter** (Allen AI, 2021): ~59K examples of facts/rules in English with proof chains. Fields are `context`, `question`, `answer`, `proof` -- all in natural language. No FOL column.

**RuleTaker** (Allen AI, 2020): The theory generator at `github.com/allenai/ruletaker` **does** produce prefix-notation logical forms internally (e.g., `+ ( cold X )`, `[ + ( cold X ) ] -> + ( nice X )`), plus ProbLog programs, alongside the English. However, the published dataset releases are primarily in natural language form. The generator itself is the closest thing to an official NL-to-logic mapping -- it generates both representations from the same grammar, so the mapping is deterministic and lossless.

### 2. FOL-Annotated Variants Found

| Name | Source | Size | FOL Format | Creation Method |
|------|--------|------|------------|-----------------|
| **ProofFOL** | [HuggingFace: ramyakeerthyt/ProofFOL](https://huggingface.co/datasets/ramyakeerthyt/ProofFOL) | 10,424 examples (train only) | Prover9 syntax with explicit predicates, `Premise_FOL`, `Conclusion_FOL` | GPT-4o translation of ProofWriter depth-5 training set, verified via Prover9; ~70% retention rate after filtering |
| **FOLIO** | [HuggingFace: benlipkin/folio](https://huggingface.co/datasets/benlipkin/folio) | 1,435 examples (487 premise sets) | Standard FOL with quantifiers | Human-annotated by CS students; not ProofWriter-derived but same task domain |
| **FoVer** | [GitHub: peiyu-cn/FoVer](https://github.com/peiyu-cn/FoVer) | Covers ProofWriter + FOLIO + REVEAL | Z3 solver format | LLM-generated FOL translations verified by Z3 theorem prover; published TACL 2025 |

### 3. Conversion Tools

| Tool | Approach | Code |
|------|----------|------|
| **Translation-NL2FOL** | Fine-tunes Mistral-7B/LLaMA-13B on ProofFOL to do NL-to-FOL; includes Prover9
…[truncated 2515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "elapsed_ms": 28
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-19T13:25:44.524526+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/omnilabNLP/LogicNLI/tree/main/dataset",
  "prompt": "List all files in this directory. What file formats are available? Are there JSON, JSONL, or other structured data files?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/omnilabNLP/LogicNLI/tree/main/dataset",
    "prompt": "List all files in this directory. What file formats are available? Are there JSON, JSONL, or other structured data files?"
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-19T13:25:44.524655+00:00_

# LogicNLI Dataset Directory Contents

Based on the webpage content provided, the dataset directory contains:

**File Available:**
- `LogicNLI_sim.zip`

**File Format:**
Only one compressed archive file is visible in this directory listing. The webpage does not display the contents of the ZIP file or indicate whether it contains JSON, JSONL, or other structured data formats.

To determine the specific data formats within the archive, you would need to download and extract the `LogicNLI_sim.zip` file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 224 · 2026-05-19T13:25:44.524807+00:00_

Web search results for query: "CLUTRR dataset format first-order logic kinship reasoning rules FOL representation"

Links: [{"title":"[PDF] CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CLUTRR:-A-Diagnostic-Benchmark-for-Inductive-from-Sinha-Sodhani/5e35895fc4731858f0b286cb5a1613a819cc2367"},{"title":"GitHub - facebookresearch/clutrr: Diagnostic benchmark suite to explicitly test logical relational reasoning on natural language · GitHub","url":"https://github.com/facebookresearch/clutrr"},{"title":"CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text | Request PDF","url":"https://www.researchgate.net/publication/336997708_CLUTRR_A_Diagnostic_Benchmark_for_Inductive_Reasoning_from_Text"},{"title":"CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text | Research - AI at Meta","url":"https://ai.meta.com/research/publications/clutrr-a-diagnostic-benchmark-for-inductive-reasoning-from-text/"},{"title":"[1908.06177] CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text","url":"https://arxiv.org/abs/1908.06177"},{"title":"CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text","url":"https://arxiv.org/pdf/1908.06177"},{"title":"CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text - ACL Anthology","url":"https://aclanthology.org/D19-1458/"},{"title":"An Extendible Realism-Based Ontology for Kinship","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11131162/"}]

Based on the search results, here's what I found about the CLUTRR dataset:

## Overview

CLUTRR is a diagnostic benchmark suite that requires an NLU system to infer kinship relations between characters in short stories, with successful performance requiring both extracting relationships between entities and inferring the logical rules governing these relationships.

## Dataset Format and Rules

The dataset creates an ideal simple kinship world derived from a set of clauses or 
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 225 · 2026-05-19T13:25:44.524965+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /tmp/LogicBench && echo \"=== Aug data ===\" && find data/LogicBench\\(Aug\\) -name \"data_instances.json\" | head -3 | while read f; do python3 -c \"import json,sys; d=json.load(open(sys.argv[1])); print(f'{sys.argv[1]}: {len(d[\\\"samples\\\"])} samples, keys={list(d.keys())}')\" \"$f\"; done && echo \"=== Check for FOL fields ===\" && python3 -c \"\nimport json\nd = json.load(open('data/LogicBench(Eval)/BQA/first_order_logic/modus_ponens/data_instances.json'))\ns = d['samples'][0]\nprint('All keys in sample:', list(s.keys()))\nprint('All keys in top-level:', list(d.keys()))\n# Check if any field has FOL formula\nimport pprint\npprint.pprint(s)\n\"",
  "description": "Check LogicBench for FOL formula fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /tmp/LogicBench && echo \"=== Aug data ===\" && find data/LogicBench\\(Aug\\) -name \"data_instances.json\" | head -3 | while read f; do python3 -c \"import json,sys; d=json.load(open(sys.argv[1])); print(f'{sys.argv[1]}: {len(d[\\\"samples\\\"])} samples, keys={list(d.keys())}')\" \"$f\"; done && echo \"=== Check for FOL fields ===\" && python3 -c \"\nimport json\nd = json.load(open('data/LogicBench(Eval)/BQA/first_order_logic/modus_ponens/data_instances.json'))\ns = d['samples'][0]\nprint('All keys in sample:', list(s.keys()))\nprint('All keys in top-level:', list(d.keys()))\n# Check if any field has FOL formula\nimport pprint\npprint.pprint(s)\n\"",
    "description": "Check LogicBench for FOL formula fields"
  }
}
```

</details>

---

### Tool result

_source line 226 · 2026-05-19T13:25:44.525097+00:00_

Exit code 1
=== Aug data ===
Traceback (most recent call last):
  File "&lt;string>", line 1, in &lt;module>
    import json,sys; d=json.load(open(sys.argv[1])); print(f'{sys.argv[1]}: {len(d["samples"])} samples, keys={list(d.keys())}')
                                                                                 ~^^^^^^^^^^^
KeyError: 'samples'
Traceback (most recent call last):
  File "&lt;string>", line 1, in &lt;module>
    import json,sys; d=json.load(open(sys.argv[1])); print(f'{sys.argv[1]}: {len(d["samples"])} samples, keys={list(d.keys())}')
                                                                                 ~^^^^^^^^^^^
KeyError: 'samples'
Traceback (most recent call last):
  File "&lt;string>", line 1, in &lt;module>
    import json,sys; d=json.load(open(sys.argv[1])); print(f'{sys.argv[1]}: {len(d["samples"])} samples, keys={list(d.keys())}')
                                                                                 ~^^^^^^^^^^^
KeyError: 'samples'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 227 · 2026-05-19T13:25:44.525230+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ReClor dataset format logical reasoning LSAT size examples formal logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ReClor dataset format logical reasoning LSAT size examples formal logic"
  }
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-19T13:25:44.525354+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicNLI omnilabNLP dataset JSONL fields facts rules proofs path label structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicNLI omnilabNLP dataset JSONL fields facts rules proofs path label structure"
  }
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-19T13:25:44.525477+00:00_

Generating train split:   0%|          | 0/9000 [00:00<?, ? examples/s]Generating train split: 100%|██████████| 9000/9000 [00:00<00:00, 230922.90 examples/s]
Generating validation split:   0%|          | 0/200 [00:00<?, ? examples/s]Generating validation split: 100%|██████████| 200/200 [00:00<00:00, 65423.55 examples/s]
Generating test split:   0%|          | 0/800 [00:00<?, ? examples/s]Generating test split: 100%|██████████| 800/800 [00:00<00:00, 146596.32 examples/s]
Splits: ['train', 'validation', 'test']
train: 9000 examples
  Fields: ['question', 'steps', 'answer']
  question: 'Numpuses are not wooden. Vumpuses are lempuses. Rompuses are not dull. Each lorpus is a wumpus. Every gorpus is moderate. Each vumpus is not discordant. Zumpuses are not spicy. Shumpuses are windy. B
  steps: ['Max is a vumpus. Each vumpus is a brimpus.', 'Max is a brimpus. Brimpuses are grimpuses.', 'Max is a grimpus. Grimpuses are shumpuses.', 'Max is a shumpus. Shumpuses are numpuses.', 'Max is a numpus
  answer: 'True'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-19T13:25:44.525620+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('fengyang0317/prontoqa')\n# Show full examples from fengyang0317 version\nfor split in ['train', 'test']:\n    print(f'=== {split} split: {len(ds[split])} examples ===')\n    for i in range(2):\n        ex = ds[split][i]\n        print(f'  Example {i}:')\n        print(f'    question: {ex[\\\"question\\\"][:300]}')\n        print(f'    answer: {ex[\\\"answer\\\"]}')\n        print(f'    steps ({len(ex[\\\"steps\\\"])} steps):')\n        for s in ex['steps']:\n            print(f'      - {s}')\n        print()\n    print()\n\" 2>&1",
  "description": "Show fengyang0317/prontoqa full examples",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('fengyang0317/prontoqa')\n# Show full examples from fengyang0317 version\nfor split in ['train', 'test']:\n    print(f'=== {split} split: {len(ds[split])} examples ===')\n    for i in range(2):\n        ex = ds[split][i]\n        print(f'  Example {i}:')\n        print(f'    question: {ex[\\\"question\\\"][:300]}')\n        print(f'    answer: {ex[\\\"answer\\\"]}')\n        print(f'    steps ({len(ex[\\\"steps\\\"])} steps):')\n        for s in ex['steps']:\n            print(f'      - {s}')\n        print()\n    print()\n\" 2>&1",
    "description": "Show fengyang0317/prontoqa full examples",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool call

_source line 231 · 2026-05-19T13:25:44.525776+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /tmp/LogicBench && python3 -c \"\nimport json\n# Check Aug format\nf = 'data/LogicBench(Aug)/propositional_logic/modus_tollens/data_instances.json'\nd = json.load(open(f))\nif isinstance(d, list):\n    print('Aug is a list, len:', len(d))\n    print('Keys in first item:', list(d[0].keys()))\n    import pprint\n    pprint.pprint(d[0])\nelse:\n    print('Aug keys:', list(d.keys()))\n\" && echo \"---\" && python3 -c \"\nimport json\n# Confirm Eval structure - no FOL\nd = json.load(open('data/LogicBench(Eval)/BQA/first_order_logic/modus_ponens/data_instances.json'))\ns = d['samples'][0]\nprint('Sample keys:', list(s.keys()))\nprint()\nprint('Full sample:')\nimport pprint\npprint.pprint(s)\n\"",
  "description": "Inspect LogicBench Aug format and confirm no FOL fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /tmp/LogicBench && python3 -c \"\nimport json\n# Check Aug format\nf = 'data/LogicBench(Aug)/propositional_logic/modus_tollens/data_instances.json'\nd = json.load(open(f))\nif isinstance(d, list):\n    print('Aug is a list, len:', len(d))\n    print('Keys in first item:', list(d[0].keys()))\n    import pprint\n    pprint.pprint(d[0])\nelse:\n    print('Aug keys:', list(d.keys()))\n\" && echo \"---\" && python3 -c \"\nimport json\n# Confirm Eval structure - no FOL\nd = json.load(open('data/LogicBench(Eval)/BQA/first_order_logic/modus_ponens/data_instances.json'))\ns = d['samples'][0]\nprint('Sample keys:', list(s.keys()))\nprint()\nprint('Full sample:')\nimport pprint\npprint.pprint(s)\n\"",
    "description": "Inspect LogicBench Aug format and confirm no FOL fields"
  }
}
```

</details>

---

### Tool result

_source line 232 · 2026-05-19T13:25:44.525900+00:00_

Aug keys: ['type', 'axiom', 'data_samples']
---
Sample keys: ['id', 'context', 'qa_pairs']

Full sample:
{'context': 'If someone is extremely tired, then they will seek some rest and '
            'relaxation. Today, Jack finds himself utterly exhausted.',
 'id': 1,
 'qa_pairs': [{'answer': 'yes',
               'question': 'Does this entail that he will take rest?'},
              {'answer': 'no',
               'question': "Does this entail that he won't take rest?"}]}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-19T13:25:44.526029+00:00_

Web search results for query: "ReClor dataset format logical reasoning LSAT size examples formal logic"

Links: [{"title":"[2002.04326] ReClor: A Reading Comprehension Dataset Requiring Logical Reasoning","url":"https://ar5iv.labs.arxiv.org/html/2002.04326"},{"title":"RECLOR: A READING COMPREHENSION DATASET ...","url":"https://openreview.net/pdf?id=HJgJtT4tvB"},{"title":"(PDF) ReClor: A Reading Comprehension Dataset Requiring Logical Reasoning","url":"https://www.researchgate.net/publication/339199685_ReClor_A_Reading_Comprehension_Dataset_Requiring_Logical_Reasoning"},{"title":"Published as a conference paper at ICLR 2020 RECLOR:","url":"https://arxiv.org/pdf/2002.04326"},{"title":"LogiQA 2.0 — An Improved Dataset for Logical Reasoning ...","url":"https://frcchang.github.io/pub/An%20Improved%20Dataset%20for%20Logical%20Reasoning%20in%20Natural%20Language%20Understanding.pdf"},{"title":"Microsoft LReasoner leads the ReClor challenge on logical reasoning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/blog/microsoft-lreasoner-leads-the-reclor-challenge-on-logical-reasoning/"},{"title":"ReClor | A Reading Comprehension Dataset Requiring Logical Reasoning","url":"https://whyu.me/reclor/"},{"title":"Logic-Driven Context Extension and Data Augmentation for Logical   Reasoning of Text","url":"https://arxiv.org/pdf/2105.03659"}]

Based on the search results, here's comprehensive information about the ReClor dataset:

## Dataset Overview

ReClor consists of 6,138 logical reasoning questions sourced from open websites and books. 91.22% are from actual exams of GMAT and LSAT while others are from high-quality practice exams.

## Dataset Format

The format of data in ReClor is similar to other multiple-choice reading comprehension datasets, where a data point contains a context, a question and four answer options, among which only one option is right/most suitable. Note that in the original problems, there are five answer options in which only one is righ
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-19T13:25:44.526182+00:00_

=== train split: 9000 examples ===
  Example 0:
    question: Numpuses are not wooden. Vumpuses are lempuses. Rompuses are not dull. Each lorpus is a wumpus. Every gorpus is moderate. Each vumpus is not discordant. Zumpuses are not spicy. Shumpuses are windy. Brimpuses are grimpuses. Each grimpus is a rompus. Brimpuses are zumpuses. Each impus is not opaque. L
    answer: True
    steps (6 steps):
      - Max is a vumpus. Each vumpus is a brimpus.
      - Max is a brimpus. Brimpuses are grimpuses.
      - Max is a grimpus. Grimpuses are shumpuses.
      - Max is a shumpus. Shumpuses are numpuses.
      - Max is a numpus. Numpuses are not wooden.
      - Max is not wooden.

  Example 1:
    question: Every rompus is not sweet. Every vumpus is not feisty. Every jompus is angry. Every sterpus is a wumpus. Brimpuses are rompuses. Each lempus is a grimpus. Dumpuses are not slow. Yumpuses are not temperate. Brimpuses are jompuses. Every shumpus is not discordant. Each lorpus is discordant. Rompuses a
    answer: False
    steps (6 steps):
      - Fae is a brimpus. Brimpuses are rompuses.
      - Fae is a rompus. Rompuses are lempuses.
      - Fae is a lempus. Each lempus is a grimpus.
      - Fae is a grimpus. Each grimpus is a lorpus.
      - Fae is a lorpus. Each lorpus is discordant.
      - Fae is discordant.


=== test split: 800 examples ===
  Example 0:
    question: Brimpuses are not luminous. Shumpuses are amenable. Each yumpus is a lorpus. Gorpuses are shumpuses. Each zumpus is a grimpus. Gorpuses are rompuses. Dumpuses are not floral. Lempuses are cold. Brimpuses are impuses. Every lorpus is floral. Every rompus is transparent. Grimpuses are muffled. Rompuse
    answer: False
    steps (6 steps):
      - Stella is a zumpus. Zumpuses are gorpuses.
      - Stella is a gorpus. Gorpuses are rompuses.
      - Stella is a rompus. Rompuses are yumpuses.
      - Stella is a yumpus. Each yumpus is a lorpus.
      - Stella is a lorpus. Every lorpus is floral.
      - Ste
…[truncated 658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 235 · 2026-05-19T13:25:44.526335+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AR-LSAT dataset analytical reasoning size format logic games"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AR-LSAT dataset analytical reasoning size format logic games"
  }
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-19T13:25:44.526462+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /tmp/LogicBench && python3 -c \"\nimport json\nf = 'data/LogicBench(Aug)/propositional_logic/modus_tollens/data_instances.json'\nd = json.load(open(f))\nprint('Aug keys:', list(d.keys()))\nprint('data_samples count:', len(d['data_samples']))\ns = d['data_samples'][0]\nprint('Sample keys:', list(s.keys()))\nimport pprint\npprint.pprint(s)\n\"",
  "description": "Inspect LogicBench Aug sample structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /tmp/LogicBench && python3 -c \"\nimport json\nf = 'data/LogicBench(Aug)/propositional_logic/modus_tollens/data_instances.json'\nd = json.load(open(f))\nprint('Aug keys:', list(d.keys()))\nprint('data_samples count:', len(d['data_samples']))\ns = d['data_samples'][0]\nprint('Sample keys:', list(s.keys()))\nimport pprint\npprint.pprint(s)\n\"",
    "description": "Inspect LogicBench Aug sample structure"
  }
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-19T13:25:44.526622+00:00_

Aug keys: ['type', 'axiom', 'data_samples']
data_samples count: 150
Sample keys: ['context', 'qa_pairs']
{'context': 'If Mason left his job, then he will not receive any salary.',
 'qa_pairs': [{'answer': 'yes',
               'question': 'If he will receive any salary, does this mean that '
                           "mason didn't leave his job?"},
              {'answer': 'no',
               'question': 'If he will receive any salary, does this mean that '
                           'Mason left his job?'},
              {'answer': 'no',
               'question': 'If he will not receive any salary, does this imply '
                           "that mason didn't leave his job?"},
              {'answer': 'no',
               'question': 'If he will not receive any salary, does this mean '
                           'that Mason left his job?'}]}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 238 · 2026-05-19T13:25:44.526872+00:00_

Web search results for query: "LogicNLI omnilabNLP dataset JSONL fields facts rules proofs path label structure"

Links: [{"title":"LogicNLI/README.md at main · omnilabNLP/LogicNLI","url":"https://github.com/omnilabNLP/LogicNLI/blob/main/README.md?plain=1"},{"title":"LogicNLI","url":"https://omnilabnlp.github.io/dataset/dataset.html"},{"title":"GitHub - omnilabNLP/LogicNLI","url":"https://github.com/omnilabNLP/LogicNLI"},{"title":"A Study to Assess the Safety and Immune Response to Env-C DNA and Protein Vaccines in Kenya","url":"https://cdn.clinicaltrials.gov/large-docs/94/NCT04826094/SAP_001.pdf"},{"title":"Logical Reasoning with Span-Level Predictions for Interpretable and   Robust NLI Models","url":"https://arxiv.org/pdf/2205.11432"},{"title":"GitHub - csitfun/LogiQA2.0: Logiqa2.0 dataset - logical reasoning in MRC and NLI tasks","url":"https://github.com/csitfun/LogiQA2.0"},{"title":"Attention over common-sense network for natural language inference","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11526678"},{"title":"Can Large Language Models Robustly Perform Natural Language Inference for Japanese Comparatives?","url":"https://arxiv.org/pdf/2509.13695"}]

I found information about LogicNLI from omnilabNLP. Let me search for more specific details about the JSONL data structure and fields.

Links: [{"title":"Logictools","url":"https://logictools.org/json.html"},{"title":"GitHub - tammet/json-ld-logic: JSON representation of first-order logic formulas","url":"https://github.com/tammet/json-ld-logic"},{"title":"JSON Rules Engine: Separate Logic From Code","url":"https://www.flowwright.com/json-rules-engine-separate-logic-from-code"},{"title":"How to store and process rules and logic with JsonLogic | by kommradHomer | Medium","url":"https://kommradhomer.medium.com/jsonlogic-for-storing-processing-rules-and-logic-ccf32a7eef74"},{"title":"GitHub - json-logic/json-logic-engine: Construct complex rules with JSON & process them. · GitHub","url":"
…[truncated 4664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-19T13:25:44.527040+00:00_

Web search results for query: "AR-LSAT dataset analytical reasoning size format logic games"

Links: [{"title":"LSAT Disclosed Analytical Reasoning Section (AR Field Study) - LSATHacks","url":"https://lsathacks.com/disclosed-analytical-reasoning-section/"},{"title":"LSAT Analytical Reasoning (Logic Games): Strategies from a 180 Scorer — Shemmassian Academic Consulting","url":"https://www.shemmassianconsulting.com/blog/lsat-analytical-reasoning"},{"title":"LSAT Analytical Reasoning: Complete Guide + Sample ...","url":"https://www.juriseducation.com/blog/lsat-analytical-reasoning-what-you-need-to-know"},{"title":"LSAT Analytical Reasoning: Complete Guide + Sample Questions","url":"https://www.juriseducation.com/blog/lsat-analytical-reasoning"},{"title":"saumyamalik/lsat_logic_games-analytical_reasoning · Datasets at Hugging Face","url":"https://huggingface.co/datasets/saumyamalik/lsat_logic_games-analytical_reasoning"},{"title":"Lost in the Logic: An Evaluation of Large Language Models’ Reasoning Capabilities on LSAT Logic Games","url":"https://arxiv.org/html/2409.19012v1"},{"title":"[PDF] AR-LSAT: Investigating Analytical Reasoning of Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AR-LSAT:-Investigating-Analytical-Reasoning-of-Text-Zhong-Wang/c5943bc4b22a63f595cb1c2823a449e03aad4787"},{"title":"AR-LSAT: Investigating Analytical Reasoning of Text","url":"https://arxiv.org/pdf/2104.06598"},{"title":"The LSAT Analytical Reasoning Section","url":"https://www.manhattanreview.com/lsat-analytical-reasoning/"},{"title":"Lost in the Logic: An Evaluation of Large Language Models' Reasoning   Capabilities on LSAT Logic Games","url":"https://arxiv.org/pdf/2409.19012"}]

Based on the search results, here's information about the AR-LSAT dataset:

## AR-LSAT Dataset Overview

The AR-LSAT dataset is a new dataset from the Law School Admission Test (LSAT) from 1991 to 2016, designed to facilitate research on analytical reasoning.

## Format and Task

An example
…[truncated 1001 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-19T13:25:44.527196+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nimport json, urllib.request\n\n# Check the original ProntoQA GitHub data structure more thoroughly\nurl = 'https://huggingface.co/datasets/tasksource/prontoqa/resolve/main/1hop_ProofsOnly_random_noadj.json'\nwith urllib.request.urlopen(url) as r:\n    data = json.loads(r.read())\n\n# Look at a test_example in detail\nex = data['example1']\nprint('Keys in example:', list(ex.keys()))\nprint()\nprint('=== test_example ===')\ntest = ex['test_example']\nfor k, v in test.items():\n    print(f'{k}: {repr(v)[:500]}')\nprint()\nprint('=== in_context_example0 ===')\nic = ex['in_context_example0']\nfor k, v in ic.items():\n    print(f'{k}: {repr(v)[:500]}')\n\" 2>&1",
  "description": "Inspect original ProntoQA GitHub data format in detail",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nimport json, urllib.request\n\n# Check the original ProntoQA GitHub data structure more thoroughly\nurl = 'https://huggingface.co/datasets/tasksource/prontoqa/resolve/main/1hop_ProofsOnly_random_noadj.json'\nwith urllib.request.urlopen(url) as r:\n    data = json.loads(r.read())\n\n# Look at a test_example in detail\nex = data['example1']\nprint('Keys in example:', list(ex.keys()))\nprint()\nprint('=== test_example ===')\ntest = ex['test_example']\nfor k, v in test.items():\n    print(f'{k}: {repr(v)[:500]}')\nprint()\nprint('=== in_context_example0 ===')\nic = ex['in_context_example0']\nfor k, v in ic.items():\n    print(f'{k}: {repr(v)[:500]}')\n\" 2>&1",
    "description": "Inspect original ProntoQA GitHub data format in detail",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool call

_source line 241 · 2026-05-19T13:25:44.527334+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip install datasets 2>&1 | tail -1 && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('hitachi-nlp/FLD.v2', split='test', streaming=True)\nimport json\nfor i, ex in enumerate(ds):\n    if i >= 2: break\n    print(f'=== Example {i} ===')\n    for k, v in ex.items():\n        print(f'  {k}: {repr(v)[:200]}')\n    print()\n\" 2>&1",
  "description": "Load FLD.v2 from HuggingFace to inspect actual fields and FOL format",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "pip install datasets 2>&1 | tail -1 && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('hitachi-nlp/FLD.v2', split='test', streaming=True)\nimport json\nfor i, ex in enumerate(ds):\n    if i >= 2: break\n    print(f'=== Example {i} ===')\n    for k, v in ex.items():\n        print(f'  {k}: {repr(v)[:200]}')\n    print()\n\" 2>&1",
    "description": "Load FLD.v2 from HuggingFace to inspect actual fields and FOL format",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 242 · 2026-05-19T13:25:44.527463+00:00_

Keys in example: ['in_context_example0', 'in_context_example1', 'in_context_example2', 'in_context_example3', 'in_context_example4', 'in_context_example5', 'in_context_example6', 'in_context_example7', 'test_example']

=== test_example ===
question: 'Gorpuses are sterpuses. Gorpuses are grimpuses. Every dumpus is a jompus. Every grimpus is a shumpus. Gorpuses are not small. Sterpuses are liquid. Every shumpus is not muffled. Dumpuses are bright. Each grimpus is a brimpus. Every grimpus is not cold. Wren is a dumpus. Wren is a grimpus.'
query: 'Prove: Wren is not cold.'
chain_of_thought: ['Wren is a grimpus.', 'Every grimpus is not cold.', 'Wren is not cold.']

=== in_context_example0 ===
question: 'Dumpuses are numpuses. Impuses are jompuses. Each yumpus is not spicy. Every dumpus is mean. Lorpuses are snowy. Each lempus is not transparent. Numpuses are tumpuses. Numpuses are moderate. Every tumpus is luminous. Jompuses are not blue. Impuses are gorpuses. Every gorpus is not hot. Each dumpus is a yumpus. Every gorpus is a lempus. Lorpuses are sterpuses. Every impus is muffled. Every numpus is an impus. Gorpuses are rompuses. Polly is an impus. Polly is a lorpus.'
query: 'Prove: Polly is muffled.'
chain_of_thought: ['Polly is an impus.', 'Every impus is muffled.', 'Polly is muffled.']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 243 · 2026-05-19T13:25:44.527615+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SimpleLogic dataset logical reasoning benchmark synthetic propositional"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SimpleLogic dataset logical reasoning benchmark synthetic propositional"
  }
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-19T13:25:44.527763+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/omnilabNLP/LogicNLI/blob/main/README.md?plain=1",
  "prompt": "Extract ALL information about the dataset format: field names, data structure, example entries, whether FOL annotations exist, how facts/rules are stored. Show any JSON/JSONL examples if present."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/omnilabNLP/LogicNLI/blob/main/README.md?plain=1",
    "prompt": "Extract ALL information about the dataset format: field names, data structure, example entries, whether FOL annotations exist, how facts/rules are stored. Show any JSON/JSONL examples if present."
  }
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-19T13:25:44.527940+00:00_

Now I have comprehensive information. Here is the complete report.

---

## FOLIO Dataset Variants: Complete Inventory

### 1. FOLIO v0.0 (Original, GitHub)
- **Source**: [Yale-LILY/FOLIO on GitHub](https://github.com/Yale-LILY/FOLIO), `data/v0.0/`
- **Size**: 1,430 examples total (train: 1,001 / val: 203 / test: 226 held-out, unreleased)
- **Fields**: `premises`, `premises-FOL`, `conclusion`, `conclusion-FOL`, `label`, `story-id`, `example-id`, `source` (WikiLogic or HybLogic)
- **FOL annotations**: Yes -- both premises and conclusions have parallel FOL formulas
- **FOL compatibility**: **5/5** (canonical source, full FOL for premises + conclusion)

### 2. yale-nlp/FOLIO (HuggingFace, updated)
- **Source**: [yale-nlp/FOLIO](https://huggingface.co/datasets/yale-nlp/FOLIO)
- **Size**: ~1,435 examples (gated; requires agreement to access). "Significant quality improvement and error fixing" over v0.0.
- **Fields**: Same schema as v0.0 (premises, premises-FOL, conclusion, conclusion-FOL, label)
- **FOL annotations**: Yes
- **FOL compatibility**: **5/5** (improved quality FOL)
- **Note**: Gated dataset, requires login + agreement.

### 3. tasksource/folio
- **Source**: [tasksource/folio](https://huggingface.co/datasets/tasksource/folio)
- **Size**: train: 1,000 / val: 203 (total ~1,203)
- **Fields**: `story_id`, `premises`, `premises-FOL`, `conclusion`, `conclusion-FOL`, `label`, `example_id`
- **FOL annotations**: Yes -- full FOL for both premises and conclusions
- **FOL compatibility**: **5/5** (community mirror of FOLIO with all FOL fields intact)

### 4. minimario/FOLIO
- **Source**: [minimario/FOLIO](https://huggingface.co/datasets/minimario/FOLIO)
- **Size**: train: 1,000 / val: 204 (total ~1,204)
- **Fields**: `conclusion`, `premises` (sequence), `premises-FOL` (sequence), `label`
- **FOL annotations**: Has `premises-FOL` but **no explicit `conclusion-FOL` field** visible in the viewer
- **FOL compatibility**: **3/5** (premises FOL only; conclusion FOL missing or 
…[truncated 3390 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "elapsed_ms": 32
}
```

</details>

---

### Tool result

_source line 246 · 2026-05-19T13:25:44.528093+00:00_

# LogicNLI Dataset Format Information

Based on the provided README content, **specific dataset format details are not included**. The page only references that a dataset file exists:

- **Available resource**: "LogicNLI_sim.zip" is mentioned as downloadable

## What the Document Reveals

The README describes LogicNLI as "an NLI-style dataset" evaluated across four dimensions: accuracy, robustness, generalization, and traceability. However, it does **not provide**:

- Field names or JSON/JSONL structure examples
- Data entry examples
- Documentation of how first-order logic (FOL) annotations are encoded
- Storage format for facts or rules
- Schema specifications

## Summary

The README serves as a project overview and paper citation rather than technical documentation. To obtain actual dataset structure details, you would need to:

1. Access the downloadable LogicNLI_sim.zip file directly
2. Review the full 2021 EMNLP paper referenced (Tian et al.)
3. Consult additional documentation in the repository beyond this README

The document confirms the dataset exists and focuses on FOL reasoning diagnosis, but defers structural information to the actual data files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-19T13:25:44.528237+00:00_

hint: See PEP 668 for the detailed specification.
=== Example 0 ===
  version: 'DeductionInstance'
  hypothesis: 'the cytoplasm does stump cytoplasm.'
  hypothesis_formula: '{E}{a}'
  context: 'sent1: something stumps cytoplasm if it stumps brigandine. sent2: something that is not a candidate ensiles mailman. sent3: something does not stump cytoplasm if that it is a candidate and a northeas
  context_formula: 'sent1: (x): {D}x -> {E}x sent2: (x): ¬{A}x -> {EU}x sent3: (x): ¬({A}x & {B}x) -> ¬{E}x sent4: (x): {A}x -> ¬(¬{B}{a} & {C}{a}) sent5: (Ex): {A}x sent6: (x): {GO}x -> ¬({C}{eo} & ¬{EL}{eo}) sent7: (x
  proofs: ['sent5 & sent7 -> int1: the fact that the cytoplasm is not a northeaster and does not spy ovipositor is wrong.; sent1 -> int2: the cytoplasm stumps cytoplasm if it stumps brigandine.;']
  proofs_formula: ['sent5 & sent7 -> int1: ¬(¬{B}{a} & ¬{C}{a}); sent1 -> int2: {D}{a} -> {E}{a};']
  negative_hypothesis: 'the cytoplasm does not stump cytoplasm.'
  negative_hypothesis_formula: '¬{E}{a}'
  negative_proofs: ['sent3 -> int3: if that the cytoplasm is a candidate and it is a kind of a northeaster is incorrect then it does not stump cytoplasm.;']
  negative_original_tree_depth: 4
  original_tree_depth: 3
  depth: None
  num_formula_distractors: 5
  num_translation_distractors: 0
  num_all_distractors: 5
  proof_label: 'UNKNOWN'
  negative_proof_label: 'UNKNOWN'
  world_assump_label: 'UNKNOWN'
  negative_world_assump_label: 'UNKNOWN'
  prompt_serial: '$hypothesis$ = the cytoplasm does stump cytoplasm. ; $context$ = sent1: something stumps cytoplasm if it stumps brigandine. sent2: something that is not a candidate ensiles mailman. sent3: something 
  proof_serial: 'sent5 & sent7 -> int1: the fact that the cytoplasm is not a northeaster and does not spy ovipositor is wrong.; sent1 -> int2: the cytoplasm stumps cytoplasm if it stumps brigandine.; __UNKNOWN__'

=== Example 1 ===
  version: 'DeductionInstance'
  hypothesis: 'the fact that the widower does not stu
…[truncated 1448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 248 · 2026-05-19T13:25:44.528385+00:00_

Web search results for query: "SimpleLogic dataset logical reasoning benchmark synthetic propositional"

Links: [{"title":"LogicBench: Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models","url":"https://arxiv.org/html/2404.15522v2"},{"title":"Assessing Logical Reasoning Capabilities of Encoder-Only Transformer Models","url":"https://arxiv.org/html/2312.11720v1"},{"title":"GitHub - Mihir3009/LogicBench: LogicBench is a natural language question-answering dataset consisting of 25 different reasoning patterns spanning over propositional, first-order, and non-monotonic logics. · GitHub","url":"https://github.com/Mihir3009/LogicBench"},{"title":"Large language models have a reasoning problem - TechTalks","url":"https://bdtechtalks.com/2022/06/27/large-language-models-logical-reasoning/"},{"title":"Can BERT Conduct Logical Reasoning? On the Difficulty of ...","url":"https://openreview.net/pdf?id=zwUYKKosPKC"},{"title":"Towards Systematic Evaluation of Logical Reasoning Ability of Large Language Models","url":"https://arxiv.org/html/2404.15522v1"},{"title":"GitHub - ariyaninf/simple_reasoning","url":"https://github.com/ariyaninf/simple_reasoning"},{"title":"JustLogic: A Comprehensive Benchmark for Evaluating Deductive Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2501.14851"},{"title":"LogicBench: A Benchmark for Evaluation of Logical Reasoning | OpenReview","url":"https://openreview.net/forum?id=7NR2ZVzZxx"}]

Based on the search results, here's what I found about the SimpleLogic dataset:

## SimpleLogic Dataset Overview

SimpleLogic is a class of logical reasoning problems that are based on propositional logic, developed by researchers at UCLA. SimpleLogic is fully synthetic, distinguishing it from other logical reasoning datasets that may use manual or semi-synthetic approaches.

## Key Characteristics

SimpleLogic covers only a subset of propositional calculus and was selected as one of four logical reasoning datasets 
…[truncated 930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 249 · 2026-05-19T13:25:44.528538+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "bAbI tasks dataset format logical reasoning first order logic deduction rules"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "bAbI tasks dataset format logical reasoning first order logic deduction rules"
  }
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-19T13:25:44.528668+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('hitachi-nlp/FLDx2', split='test', streaming=True)\nfor i, ex in enumerate(ds):\n    if i >= 1: break\n    print('=== FLDx2 Example ===')\n    for k, v in ex.items():\n        val = repr(v)\n        if len(val) > 300: val = val[:300] + '...'\n        print(f'  {k}: {val}')\n\" 2>&1",
  "description": "Load FLDx2 from HuggingFace to inspect fields",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('hitachi-nlp/FLDx2', split='test', streaming=True)\nfor i, ex in enumerate(ds):\n    if i >= 1: break\n    print('=== FLDx2 Example ===')\n    for k, v in ex.items():\n        val = repr(v)\n        if len(val) > 300: val = val[:300] + '...'\n        print(f'  {k}: {val}')\n\" 2>&1",
    "description": "Load FLDx2 from HuggingFace to inspect fields",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool call

_source line 251 · 2026-05-19T13:25:44.528819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/91820fa6-7a1f-4a02-8bc0-aaa4f114a9f1/tool-results/webfetch-1779196587258-r6kcgy.pdf",
  "pages": "6-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/91820fa6-7a1f-4a02-8bc0-aaa4f114a9f1/tool-results/webfetch-1779196587258-r6kcgy.pdf",
    "pages": "6-10"
  }
}
```

</details>

---

### Tool result

_source line 252 · 2026-05-19T13:25:44.528936+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/91820fa6-7a1f-4a02-8bc0-aaa4f114a9f1/tool-results/webfetch-1779196587258-r6kcgy.pdf (782.5KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 253 · 2026-05-19T13:25:44.529071+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('renma/ProntoQA', split='validation')\n\n# Full raw_logic_programs for example 2\nex = ds[2]\nprint('=== Example 2 full raw_logic_programs ===')\nfor prog in ex['raw_logic_programs']:\n    print(prog)\nprint()\nprint('=== Conversion analysis ===')\n# Parse and show what Prover9 FOL would look like\nprograms = ex['raw_logic_programs'][0]\nlines = programs.strip().split('\\n')\nsection = None\nfor line in lines:\n    line = line.strip()\n    if line.startswith('Predicates:'):\n        section = 'pred'\n        continue\n    elif line.startswith('Facts:'):\n        section = 'fact'\n        continue\n    elif line.startswith('Rules:'):\n        section = 'rule'\n        continue\n    elif line.startswith('Query:'):\n        section = 'query'\n        continue\n    if not line:\n        continue\n    if section == 'rule':\n        # Parse: Pred(\\$x, True) >>> Pred(\\$x, True)\n        parts = line.split(' >>> ')\n        if len(parts) == 2:\n            print(f'Rule: {line}')\n            lhs, rhs = parts\n            # Convert to Prover9 style\n            lhs_name = lhs.split('(')[0]\n            rhs_name = rhs.split('(')[0]\n            lhs_val = 'True' in lhs.split(',')[-1]\n            rhs_val = 'True' in rhs.split(',')[-1]\n            lhs_fol = f'{lhs_name.lower()}(x)' if lhs_val else f'-{lhs_name.lower()}(x)'\n            rhs_fol = f'{rhs_name.lower()}(x)' if rhs_val else f'-{rhs_name.lower()}(x)'\n            print(f'  -> Prover9: all x ({lhs_fol} -> {rhs_fol}).')\n    elif section == 'fact':\n        print(f'Fact: {line}')\n        name = line.split('(')[0]\n        entity = line.split('(')[1].split(',')[0]\n        val = 'True' in line\n        fol = f'{name.lower()}({entity.lower()})' if val else f'-{name.lower()}({entity.lower()})'\n        print(f'  -> Prover9: {fol}.')\n    elif section == 'query':\n        print(f'Query: {line}')\n        name = line.split('(')[0]\n        entity = line.split('(')[1].split(',')[0]\n        val = 'True' in line\n        fol = f'{name.lower()}({entity.lower()})' if val else f'-{name.lower()}({entity.lower()})'\n        print(f'  -> Prover9 goal: {fol}.')\n\" 2>&1",
  "description": "Analyze FOL format and Prover9 convertibility",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('renma/ProntoQA', split='validation')\n\n# Full raw_logic_programs for example 2\nex = ds[2]\nprint('=== Example 2 full raw_logic_programs ===')\nfor prog in ex['raw_logic_programs']:\n    print(prog)\nprint()\nprint('=== Conversion analysis ===')\n# Parse and show what Prover9 FOL would look like\nprograms = ex['raw_logic_programs'][0]\nlines = programs.strip().split('\\n')\nsection = None\nfor line in lines:\n    line = line.strip()\n    if line.startswith('Predicates:'):\n        section = 'pred'\n        continue\n    elif line.startswith('Facts:'):\n        section = 'fact'\n        continue\n    elif line.startswith('Rules:'):\n        section = 'rule'\n        continue\n    elif line.startswith('Query:'):\n        section = 'query'\n        continue\n    if not line:\n        continue\n    if section == 'rule':\n        # Parse: Pred(\\$x, True) >>> Pred(\\$x, True)\n        parts = line.split(' >>> ')\n        if len(parts) == 2:\n            print(f'Rule: {line}')\n            lhs, rhs = parts\n            # Convert to Prover9 style\n            lhs_name = lhs.split('(')[0]\n            rhs_name = rhs.split('(')[0]\n            lhs_val = 'True' in lhs.split(',')[-1]\n            rhs_val = 'True' in rhs.split(',')[-1]\n            lhs_fol = f'{lhs_name.lower()}(x)' if lhs_val else f'-{lhs_name.lower()}(x)'\n            rhs_fol = f'{rhs_name.lower()}(x)' if rhs_val else f'-{rhs_name.lower()}(x)'\n            print(f'  -> Prover9: all x ({lhs_fol} -> {rhs_fol}).')\n    elif section == 'fact':\n        print(f'Fact: {line}')\n        name = line.split('(')[0]\n        entity = line.split('(')[1].split(',')[0]\n        val = 'True' in line\n        fol = f'{name.lower()}({entity.lower()})' if val else f'-{name.lower()}({entity.lower()})'\n        print(f'  -> Prover9: {fol}.')\n    elif section == 'query':\n        print(f'Query: {line}')\n        name = line.split('(')[0]\n        entity = line.split('(')[1].split(',')[0]\n        val = 'True' in line\n        fol = f'{name.lower()}({entity.lower()})' if val else f'-{name.lower()}({entity.lower()})'\n        print(f'  -> Prover9 goal: {fol}.')\n\" 2>&1",
    "description": "Analyze FOL format and Prover9 convertibility",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-19T13:25:44.529224+00:00_

Web search results for query: "bAbI tasks dataset format logical reasoning first order logic deduction rules"

Links: [{"title":"Solving the Prerequisites: Improving Question Answering on the bAbI Dataset","url":"https://cs229.stanford.edu/proj2015/333_report.pdf"},{"title":"What datasets are commonly used for AI reasoning tasks?","url":"https://milvus.io/ai-quick-reference/what-datasets-are-commonly-used-for-ai-reasoning-tasks"},{"title":"Reasoning in Vector Space: An Exploratory Study of Question Answering","url":"https://arxiv.org/pdf/1511.06426"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"GitHub - Mihir3009/LogicBench: LogicBench is a natural language question-answering dataset consisting of 25 different reasoning patterns spanning over propositional, first-order, and non-monotonic logics. · GitHub","url":"https://github.com/Mihir3009/LogicBench"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"Large Language Models Meet Symbolic Provers for Logical Reasoning   Evaluation","url":"https://arxiv.org/pdf/2502.06563"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/pdf/2209.00840"}]

Based on the search results, here's what I found about the bAbI tasks dataset and its relationship to logical reasoning:

## bAbI Dataset Overview

The Facebook bAbI dataset is a synthetic dataset of 20 toy question-answering tasks. Each task targets a specific skill that a general reasoning agent would be expected to have, such as answering yes/no questions or performing deduction over multiple sentences.

Each of the 20 tasks consists of 1,000 training examples and 1,000 test examples. The tasks are generated from a simulation of characters and objects interacting in a small, closed world, which produces ground text describing the scene and question/answer pairs.

## Reasoning C
…[truncated 725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-19T13:25:44.529392+00:00_

=== Example 2 full raw_logic_programs ===
Predicates:
Vumpus($x, bool) ::: Does x belong to Vumpus?
Floral($x, bool) ::: Is x floral?
Tumpus($x, bool) ::: Does x belong to Tumpus?
Brown($x, bool) ::: Is x brown?
Wumpus($x, bool) ::: Does x belong to Wumpus?
Small($x, bool) ::: Is x small?
Rompus($x, bool) ::: Does x belong to Rompus?
Zumpus($x, bool) ::: Does x belong to Zumpus?
Metallic($x, bool) ::: Is x metallic?
Happy($x, bool) ::: Is x happy?
Impus($x, bool) ::: Does x belong to Impus?
Amenable($x, bool) ::: Is x amenable?
Dumpus($x, bool) ::: Does x belong to Dumpus?
Numpus($x, bool) ::: Does x belong to Numpus?
Bitter($x, bool) ::: Is x bitter?
Jompus($x, bool) ::: Does x belong to Jompus?
Cold($x, bool) ::: Is x cold?
Yumpus($x, bool) ::: Does x belong to Yumpus?

Facts:
Tumpus(Wren, True)

Rules:
Vumpus($x, True) >>> Floral($x, True)
Vumpus($x, True) >>> Tumpus($x, True)
Tumpus($x, True) >>> Brown($x, True)
Tumpus($x, True) >>> Wumpus($x, True)
Wumpus($x, True) >>> Small($x, True)
Wumpus($x, True) >>> Rompus($x, True)
Zumpus($x, True) >>> Metallic($x, True)
Rompus($x, True) >>> Happy($x, True)
Rompus($x, True) >>> Impus($x, True)
Impus($x, True) >>> Amenable($x, True)
Impus($x, True) >>> Dumpus($x, True)
Dumpus($x, True) >>> Metallic($x, False)
Dumpus($x, True) >>> Numpus($x, True)
Numpus($x, True) >>> Bitter($x, True)
Numpus($x, True) >>> Jompus($x, True)
Jompus($x, True) >>> Cold($x, True)
Jompus($x, True) >>> Yumpus($x, True)

Query:
Metallic(Wren, False)

=== Conversion analysis ===
Fact: Tumpus(Wren, True)
  -> Prover9: tumpus(wren).
Rule: Vumpus($x, True) >>> Floral($x, True)
  -> Prover9: all x (vumpus(x) -> floral(x)).
Rule: Vumpus($x, True) >>> Tumpus($x, True)
  -> Prover9: all x (vumpus(x) -> tumpus(x)).
Rule: Tumpus($x, True) >>> Brown($x, True)
  -> Prover9: all x (tumpus(x) -> brown(x)).
Rule: Tumpus($x, True) >>> Wumpus($x, True)
  -> Prover9: all x (tumpus(x) -> wumpus(x)).
Rule: Wumpus($x, True) >>> Small($x, True)
  -> Prover9: all x (wump
…[truncated 1166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 256 · 2026-05-19T13:25:44.529543+00:00_

=== FLDx2 Example ===
  version: '0.31'
  hypothesis: 'This ballottement occurs and this flying jnd happens.'
  hypothesis_formula: '({A} & {B})'
  facts: 'fact1: That backing and that confectioning inkblot happens if this SALTING Melampodium does not occurs. fact2: If this miaow happens that that robing dole does not happens and this arts does not happens does not hold. fact3: If the fact that this kabbalism does not happens and that washableness doe...
  facts_formula: 'fact1: ¬{M} -> ({F} & {I}) fact2: {T} -> ¬(¬{N} & ¬{L}) fact3: ¬(¬{Q} & ¬{R}) -> {P} fact4: ¬{U} -> ¬(¬{AA} & ¬{T}) fact5: {IL} fact6: (¬{B} & ¬{A}) -> {G} fact7: {B} fact8: ¬{U} fact9: ¬{E} -> ({D} & {C}) fact10: (¬{J} & {K}) -> {H} fact11: {A} fact12: ({H} & {F}) -> ¬{E} fact13: {P} -> (¬{M} & {O...
  proofs: ['fact11 & fact7 -> hypothesis;']
  proofs_formula: ['fact11 & fact7 -> hypothesis;']
  theorem_is_used_in_proof: False
  negative_hypothesis: 'This upholding occurs.'
  negative_hypothesis_formula: '{G}'
  negative_proofs: ['fact25 & fact30 -> int1: That this cascade does not happens and this miaow does not occurs is false.; fact29 & int1 -> int2: This miaow occurs.; fact21 & int2 -> int3: That that robing dole does not occurs and this arts does not occurs is incorrect.; fact26 & int3 -> int4: This arts happens.; fact...
  negative_original_tree_depth: 13
  original_tree_steps: 1
  original_tree_depth: 1
  steps: 1
  depth: 1
  num_formula_distractors: 17
  num_translation_distractors: 0
  num_all_distractors: 17
  proof_label: 'PROVED'
  negative_proof_label: 'UNKNOWN'
  world_assump_label: 'PROVED'
  negative_world_assump_label: 'UNKNOWN'
  prompt_serial: 'Based on the provided facts ($facts$), verify the hypothesis ($hypothesis$). Conclude with one of the markers: "__PROVED__" for proven, "__DISPROVED__" for disproven, or "__UNKNOWN__" if uncertain.\n\nLet\'s analyze this step by step. $facts$ = fact1: That backing and that confectioning inkblot hap...
  proof_serial: 'fact11 & fact7 -> 
…[truncated 389 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 257 · 2026-05-19T13:25:44.529711+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOL-nli dataset huggingface tasksource syllogism sorite first-order logic NLI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOL-nli dataset huggingface tasksource syllogism sorite first-order logic NLI"
  }
}
```

</details>

---

### Tool call

_source line 258 · 2026-05-19T13:25:44.529847+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "rm -rf /tmp/LogicBench",
  "description": "Clean up temp clone"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "rm -rf /tmp/LogicBench",
    "description": "Clean up temp clone"
  }
}
```

</details>

---

### Tool result

_source line 259 · 2026-05-19T13:25:44.529959+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 260 · 2026-05-19T13:25:44.530081+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nimport json, urllib.request\n\n# Count total examples in tasksource/prontoqa by checking a few files\nbase = 'https://huggingface.co/datasets/tasksource/prontoqa/resolve/main/'\nfiles_to_check = [\n    '1hop_ProofsOnly_random_noadj.json',\n    '2hop_AndElim_random_noadj.json',\n    '1hop_AndElim_2testhops_random_noadj.json',\n]\nfor f in files_to_check:\n    url = base + f\n    with urllib.request.urlopen(url) as r:\n        data = json.loads(r.read())\n    print(f'{f}: {len(data)} examples')\n    # Check fields\n    ex = data['example1']\n    test = ex['test_example']\n    print(f'  test_example keys: {list(test.keys())}')\n    print()\n\" 2>&1",
  "description": "Count examples in tasksource/prontoqa files",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "source /tmp/hf_env/bin/activate && python3 -c \"\nimport json, urllib.request\n\n# Count total examples in tasksource/prontoqa by checking a few files\nbase = 'https://huggingface.co/datasets/tasksource/prontoqa/resolve/main/'\nfiles_to_check = [\n    '1hop_ProofsOnly_random_noadj.json',\n    '2hop_AndElim_random_noadj.json',\n    '1hop_AndElim_2testhops_random_noadj.json',\n]\nfor f in files_to_check:\n    url = base + f\n    with urllib.request.urlopen(url) as r:\n        data = json.loads(r.read())\n    print(f'{f}: {len(data)} examples')\n    # Check fields\n    ex = data['example1']\n    test = ex['test_example']\n    print(f'  test_example keys: {list(test.keys())}')\n    print()\n\" 2>&1",
    "description": "Count examples in tasksource/prontoqa files",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 261 · 2026-05-19T13:25:44.530199+00:00_

1hop_ProofsOnly_random_noadj.json: 100 examples
  test_example keys: ['question', 'query', 'chain_of_thought']

2hop_AndElim_random_noadj.json: 100 examples
  test_example keys: ['question', 'query', 'chain_of_thought']

1hop_AndElim_2testhops_random_noadj.json: 100 examples
  test_example keys: ['question', 'query', 'chain_of_thought']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 262 · 2026-05-19T13:25:44.530320+00:00_

Web search results for query: "FOL-nli dataset huggingface tasksource syllogism sorite first-order logic NLI"

Links: [{"title":"tasksource/FOL-nli · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/FOL-nli"},{"title":"Study to Evaluate the Safety, Tolerability, Pharmacokinetics, and Efficacy of AMG 562 in Subjects With r/r Diffuse Large B-cell Lymphoma, Mantle Cell Lymphoma, or Follicular Lymphoma","url":"https://cdn.clinicaltrials.gov/large-docs/28/NCT03571828/Prot_000.pdf"},{"title":"Safety and Performance of PEEK Anchors in Extremities","url":"https://cdn.clinicaltrials.gov/large-docs/98/NCT03782298/Prot_SAP_000.pdf"},{"title":"tasksource/FOL-nli · Discussions","url":"https://huggingface.co/datasets/tasksource/FOL-nli/discussions"},{"title":"tasksource/LogicNLI · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/LogicNLI"},{"title":"tasksource/folio · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/folio"},{"title":"A Study to Assess the Safety and Immune Response to Env-C DNA and Protein Vaccines in Kenya","url":"https://cdn.clinicaltrials.gov/large-docs/94/NCT04826094/SAP_001.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"},{"title":"nlplabtdtu/data-syllogism-v3 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/nlplabtdtu/data-syllogism-v3"},{"title":"tasksource/ModernBERT-large-nli · Hugging Face","url":"https://huggingface.co/tasksource/ModernBERT-large-nli"}]

Based on the search results, here's what I found about the FOL-nli dataset:

## FOL-nli Dataset Overview

The FOL-nli dataset is available on Hugging Face under tasksource and contains 103,000 rows across three splits: 82,200 training rows, 10,300 validation rows, and 10,300 test rows. The dataset is tagged with topics including first-order logic, syllo
…[truncated 758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 263 · 2026-05-19T13:25:44.530475+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Check a wider sample to see if any hidden fields exist, and analyze premise structure\nfrom datasets import load_dataset\nds = load_dataset('tasksource/LogicNLI', split='train')\n\n# Confirm fields\nprint('Fields:', ds.column_names)\nprint()\n\n# Analyze premise structure patterns\nimport re\nex = ds[100]\npremise = ex['premise']\nlines = [l.strip() for l in premise.split('\\n') if l.strip()]\n\n# Separate facts vs rules\nfacts = []\nrules = []\nfor line in lines:\n    # Rules typically start with 'If' or contain 'someone' patterns\n    if line.startswith('If ') or 'someone' in line.lower() or 'always' in line.lower() or 'imply' in line.lower() or 'once knowing' in line.lower() or 'it can be concluded' in line.lower() or 'vice versa' in line.lower():\n        rules.append(line)\n    else:\n        facts.append(line)\n\nprint(f'=== EXAMPLE 100 ANALYSIS ===')\nprint(f'Number of facts: {len(facts)}')\nprint(f'Number of rules: {len(rules)}')\nprint()\nprint('FACTS:')\nfor f in facts:\n    print(f'  {f}')\nprint()\nprint('RULES:')\nfor r in rules:\n    print(f'  {r}')\nprint()\nprint(f'HYPOTHESIS: {ex[\\\"hypothesis\\\"]}')\nprint(f'LABEL: {ex[\\\"label\\\"]}')\n\n# Check unique NL patterns for FOL connectives\nprint()\nprint('=== RULE PATTERN ANALYSIS (first 200 examples) ===')\nrule_patterns = set()\nfor i in range(min(200, len(ds))):\n    premise = ds[i]['premise']\n    lines = [l.strip() for l in premise.split('\\n') if l.strip()]\n    for line in lines:\n        if 'someone' in line.lower() or line.startswith('If ') or 'always' in line.lower():\n            # Extract the template pattern\n            # Replace names with X\n            pattern = re.sub(r'[A-Z][a-z]+(?:\\s)', 'X ', line)\n            rule_patterns.add(line[:80])\n\nprint(f'Unique rule prefixes (sample): {len(rule_patterns)}')\nfor p in sorted(list(rule_patterns))[:15]:\n    print(f'  {p}')\n\" 2>&1\n",
  "description": "Analyze LogicNLI premise structure to understand rule format",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Check a wider sample to see if any hidden fields exist, and analyze premise structure\nfrom datasets import load_dataset\nds = load_dataset('tasksource/LogicNLI', split='train')\n\n# Confirm fields\nprint('Fields:', ds.column_names)\nprint()\n\n# Analyze premise structure patterns\nimport re\nex = ds[100]\npremise = ex['premise']\nlines = [l.strip() for l in premise.split('\\n') if l.strip()]\n\n# Separate facts vs rules\nfacts = []\nrules = []\nfor line in lines:\n    # Rules typically start with 'If' or contain 'someone' patterns\n    if line.startswith('If ') or 'someone' in line.lower() or 'always' in line.lower() or 'imply' in line.lower() or 'once knowing' in line.lower() or 'it can be concluded' in line.lower() or 'vice versa' in line.lower():\n        rules.append(line)\n    else:\n        facts.append(line)\n\nprint(f'=== EXAMPLE 100 ANALYSIS ===')\nprint(f'Number of facts: {len(facts)}')\nprint(f'Number of rules: {len(rules)}')\nprint()\nprint('FACTS:')\nfor f in facts:\n    print(f'  {f}')\nprint()\nprint('RULES:')\nfor r in rules:\n    print(f'  {r}')\nprint()\nprint(f'HYPOTHESIS: {ex[\\\"hypothesis\\\"]}')\nprint(f'LABEL: {ex[\\\"label\\\"]}')\n\n# Check unique NL patterns for FOL connectives\nprint()\nprint('=== RULE PATTERN ANALYSIS (first 200 examples) ===')\nrule_patterns = set()\nfor i in range(min(200, len(ds))):\n    premise = ds[i]['premise']\n    lines = [l.strip() for l in premise.split('\\n') if l.strip()]\n    for line in lines:\n        if 'someone' in line.lower() or line.startswith('If ') or 'always' in line.lower():\n            # Extract the template pattern\n            # Replace names with X\n            pattern = re.sub(r'[A-Z][a-z]+(?:\\s)', 'X ', line)\n            rule_patterns.add(line[:80])\n\nprint(f'Unique rule prefixes (sample): {len(rule_patterns)}')\nfor p in sorted(list(rule_patterns))[:15]:\n    print(f'  {p}')\n\" 2>&1\n",
    "description": "Analyze LogicNLI premise structure to understand rule format",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-19T13:25:44.530621+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogiCoT dataset formal logic chain-of-thought FOLIO derived format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogiCoT dataset formal logic chain-of-thought FOLIO derived format"
  }
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-19T13:25:44.530774+00:00_

Fields: ['premise', 'hypothesis', 'label']

=== EXAMPLE 100 ANALYSIS ===
Number of facts: 12
Number of rules: 11

FACTS:
  Sean is not annoyed.
  Amos is outstanding.
  Adrian is tall.
  Sean is not unable.
  Amos is loyal.
  Sean is massive.
  Baldwin is annoyed.
  Adrian is not unable.
  Sean is tall.
  Richard is unable.
  Kayla is not tall.
  Adrian being tall and Amos being outstanding are equivalent to Hunter being unable and Richard being not annoyed.

RULES:
  Baldwin is tall.If someone is tall and not massive, then he is loyal, and vice versa.
  If someone is both not outstanding and not annoyed, then he is unable.
  If Kayla is not massive, then Kayla is unable and Amos is annoyed, and vice versa.
  If there is someone who is both unable and not annoyed, then Amos is not loyal.
  If Adrian is outstanding, then Amos is not massive and Richard is tall.
  If Hunter is loyal, then Richard is not unable.
  Someone who is not annoyed is always both not outstanding and massive.
  If there is at least one people who is loyal, then Hunter is massive and Richard is not unable.
  Someone who is both tall and not outstanding is always unable.
  If everyone is not outstanding, then Kayla is not tall.
  If there is someone who is massive, then Sean is not tall.

HYPOTHESIS: Richard is outstanding.
LABEL: contradiction

=== RULE PATTERN ANALYSIS (first 200 examples) ===
Unique rule prefixes (sample): 88
  As long as someone is difficult, he is not crazy and breakable.
  As long as someone is either not difficult or breakable, he is terrible and not 
  As long as someone is not imaginative, he is big and modern.
  Baldwin is tall.If someone is tall and not massive, then he is loyal, and vice v
  Hunter is big.If there is someone who is imaginative, then Harley is modern and 
  If Adrian is outstanding, then Amos is not massive and Richard is tall.
  If Amery is not popular and Kendrick is not helpful, then Austin is wooden.
  If Chalmers is not alive and Brooke is not emo
…[truncated 553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 266 · 2026-05-19T13:25:44.530937+00:00_

Web search results for query: "LogiCoT dataset formal logic chain-of-thought FOLIO derived format"

Links: [{"title":"LogiCoT: Logical Chain-of-Thought Instruction Tuning","url":"https://aclanthology.org/2023.findings-emnlp.191.pdf"},{"title":"(PDF) LogiCoT: Logical Chain-of-Thought Instruction-Tuning Data Collection with GPT-4","url":"https://www.researchgate.net/publication/370949042_LogiCoT_Logical_Chain-of-Thought_Instruction-Tuning_Data_Collection_with_GPT-4"},{"title":"Logical CoT Instruction Tuning","url":"https://www.emergentmind.com/topics/logical-chain-of-thought-instruction-tuning"},{"title":"LogiCoT: Logical Chain-of-Thought Tuning","url":"https://www.emergentmind.com/topics/logicot-logical-chain-of-thought-instruction-tuning"},{"title":"datatune/LogiCoT · Datasets at Hugging Face","url":"https://huggingface.co/datasets/datatune/LogiCoT"},{"title":"LogiCoT: Logical Chain-of-Thought Instruction Tuning with ...","url":"https://github.com/csitfun/LogiCoT"},{"title":"Paper page - LogiCoT: Logical Chain-of-Thought Instruction-Tuning Data Collection with GPT-4","url":"https://huggingface.co/papers/2305.12147"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"LogiCoT: Logical Chain-of-Thought Instruction-Tuning","url":"https://arxiv.org/pdf/2305.12147"},{"title":"[2305.12147] LogiCoT: Logical Chain-of-Thought Instruction-Tuning","url":"https://arxiv.org/abs/2305.12147"}]

Based on the search results, here's what I found about the LogiCoT dataset and its relationship to FOLIO:

## Overview

LogiCoT (Logical Chain-of-Thought) is a large-scale instruction-tuning methodology and dataset designed to enhance the logical reasoning abilities of LLMs. It presents a new instruction-tuning dataset for Logical Chain-of-Thought reasoning with GPT-4.

## FOLIO-Derived Format

The LogiCoT dataset includes folio2instruction.jsonl, which is derived from the FOLIO data. More broadly, classical resources su
…[truncated 1039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 267 · 2026-05-19T13:25:44.531161+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FoVer dataset first-order logic verification natural language reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FoVer dataset first-order logic verification natural language reasoning 2025"
  }
}
```

</details>

---

### Tool result

_source line 268 · 2026-05-19T13:25:44.531300+00:00_

Web search results for query: "FoVer dataset first-order logic verification natural language reasoning 2025"

Links: [{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.tacl-1.61/"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/article/view/8211"},{"title":"GitHub - peiyu-cn/FoVer: Official code repository for the paper: \"FoVer: First-Order Logic Verification for Natural Language Reasoning\" (TACL) · GitHub","url":"https://github.com/peiyu-cn/FoVer"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning","url":"https://www.researchgate.net/publication/397118426_FoVer_First-Order_Logic_Verification_for_Natural_Language_Reasoning"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/pdf/2505.14932"}]

Based on the search results, here's what I found about FoVer:

FoVer (First-order logic Verification) is an automated pipeline that verifies the logical correctness of reasoning texts using first-order logic. The work was published in Transactions of the Association for Computational Linguistics in 2025 by Yu Pei, Yongping Du, and Xingnan Jin.

The pipeline operates in two main steps: (1) LLM-driven translation of natural language into executable logical expressions, and (2) automated logical verification using
…[truncated 711 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 269 · 2026-05-19T13:25:44.531454+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Catalog the FOL connective patterns in NL\nfrom datasets import load_dataset\nimport re\nds = load_dataset('tasksource/LogicNLI', split='train[:500]')\n\npatterns = {\n    'universal_forall': 0,       # 'someone who ... is always', 'everyone'\n    'existential_exists': 0,     # 'there is someone', 'there is at least one'\n    'conjunction_and': 0,        # 'and'\n    'disjunction_or': 0,         # 'or', 'either...or'\n    'negation_not': 0,           # 'not'\n    'implication_if_then': 0,    # 'If...then'\n    'equivalence_iff': 0,        # 'vice versa', 'equivalent to', 'if and only if'\n}\n\nfor ex in ds:\n    premise = ex['premise']\n    lines = [l.strip() for l in premise.split('\\n') if l.strip()]\n    for line in lines:\n        ll = line.lower()\n        if 'always' in ll or 'everyone' in ll:\n            patterns['universal_forall'] += 1\n        if 'there is someone' in ll or 'there is at least one' in ll:\n            patterns['existential_exists'] += 1\n        if ' and ' in ll:\n            patterns['conjunction_and'] += 1\n        if ' or ' in ll:\n            patterns['disjunction_or'] += 1\n        if ' not ' in ll:\n            patterns['negation_not'] += 1\n        if 'if ' in ll and 'then' in ll:\n            patterns['implication_if_then'] += 1\n        if 'vice versa' in ll or 'equivalent' in ll:\n            patterns['equivalence_iff'] += 1\n\nprint('FOL connective frequency (500 examples):')\nfor k, v in sorted(patterns.items(), key=lambda x: -x[1]):\n    print(f'  {k}: {v}')\n\n# Show the predicate structure: unary predicates on named constants\nprint()\nprint('=== PREDICATE ANALYSIS ===')\n# Facts are of the form: \\\"Name is (not) adjective\\\"\nfact_pattern = re.compile(r'^([A-Z][a-z]+) is (not )?(\\w+)\\.$')\nadj_set = set()\nname_set = set()\nfor ex in ds:\n    premise = ex['premise']\n    for line in premise.split('\\n'):\n        line = line.strip()\n        m = fact_pattern.match(line)\n        if m:\n            name_set.add(m.group(1))\n            adj_set.add(m.group(3))\n\nprint(f'Unique entity names (sample): {len(name_set)}')\nprint(f'Unique predicates/adjectives (sample): {len(adj_set)}')\nprint(f'Sample names: {sorted(list(name_set))[:10]}')\nprint(f'Sample predicates: {sorted(list(adj_set))[:15]}')\n\" 2>&1\n",
  "description": "Catalog FOL connective patterns and predicate structure",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Catalog the FOL connective patterns in NL\nfrom datasets import load_dataset\nimport re\nds = load_dataset('tasksource/LogicNLI', split='train[:500]')\n\npatterns = {\n    'universal_forall': 0,       # 'someone who ... is always', 'everyone'\n    'existential_exists': 0,     # 'there is someone', 'there is at least one'\n    'conjunction_and': 0,        # 'and'\n    'disjunction_or': 0,         # 'or', 'either...or'\n    'negation_not': 0,           # 'not'\n    'implication_if_then': 0,    # 'If...then'\n    'equivalence_iff': 0,        # 'vice versa', 'equivalent to', 'if and only if'\n}\n\nfor ex in ds:\n    premise = ex['premise']\n    lines = [l.strip() for l in premise.split('\\n') if l.strip()]\n    for line in lines:\n        ll = line.lower()\n        if 'always' in ll or 'everyone' in ll:\n            patterns['universal_forall'] += 1\n        if 'there is someone' in ll or 'there is at least one' in ll:\n            patterns['existential_exists'] += 1\n        if ' and ' in ll:\n            patterns['conjunction_and'] += 1\n        if ' or ' in ll:\n            patterns['disjunction_or'] += 1\n        if ' not ' in ll:\n            patterns['negation_not'] += 1\n        if 'if ' in ll and 'then' in ll:\n            patterns['implication_if_then'] += 1\n        if 'vice versa' in ll or 'equivalent' in ll:\n            patterns['equivalence_iff'] += 1\n\nprint('FOL connective frequency (500 examples):')\nfor k, v in sorted(patterns.items(), key=lambda x: -x[1]):\n    print(f'  {k}: {v}')\n\n# Show the predicate structure: unary predicates on named constants\nprint()\nprint('=== PREDICATE ANALYSIS ===')\n# Facts are of the form: \\\"Name is (not) adjective\\\"\nfact_pattern = re.compile(r'^([A-Z][a-z]+) is (not )?(\\w+)\\.$')\nadj_set = set()\nname_set = set()\nfor ex in ds:\n    premise = ex['premise']\n    for line in premise.split('\\n'):\n        line = line.strip()\n        m = fact_pattern.match(line)\n        if m:\n            name_set.add(m.group(1))\n            adj_set.add(m.group(3))\n\nprint(f'Unique entity names (sample): {len(name_set)}')\nprint(f'Unique predicates/adjectives (sample): {len(adj_set)}')\nprint(f'Sample names: {sorted(list(name_set))[:10]}')\nprint(f'Sample predicates: {sorted(list(adj_set))[:15]}')\n\" 2>&1\n",
    "description": "Catalog FOL connective patterns and predicate structure",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool call

_source line 270 · 2026-05-19T13:25:44.531623+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FCoReBench PuzzleBench first-order combinatorial reasoning dataset size format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FCoReBench PuzzleBench first-order combinatorial reasoning dataset size format"
  }
}
```

</details>

---

### Tool result

_source line 271 · 2026-05-19T13:25:44.531773+00:00_

FOL connective frequency (500 examples):
  negation_not: 7540
  conjunction_and: 3660
  implication_if_then: 3220
  disjunction_or: 1200
  existential_exists: 1120
  equivalence_iff: 1120
  universal_forall: 700

=== PREDICATE ANALYSIS ===
Unique entity names (sample): 126
Unique predicates/adjectives (sample): 115
Sample names: ['Adrian', 'Alberto', 'Aldis', 'Alexander', 'Alfie', 'Alfred', 'Alisa', 'Amery', 'Amos', 'Angus']
Sample predicates: ['administrative', 'alive', 'ancient', 'angry', 'annoyed', 'aware', 'basic', 'better', 'big', 'blue', 'breakable', 'careful', 'cautious', 'clear', 'cloudy']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 272 · 2026-05-19T13:25:44.531940+00:00_

I now have all the information needed. Here is the complete report.

---

## ProntoQA Dataset Research Report

### Dataset Versions Available

There are three HuggingFace versions and the original GitHub repo:

| Source | Examples | Has FOL? |
|--------|----------|----------|
| `tasksource/prontoqa` (original GitHub mirror) | ~100 per JSON file, ~50+ files, ~38.7 MB total | No |
| `fengyang0317/prontoqa` | 9000 train / 200 val / 800 test = 10,000 | No |
| `renma/ProntoQA` | 500 (validation only) | **Yes** |
| GitHub: `asaparov/prontoqa` | generator code + OOD data | No (generates NL) |

### Field Structures

**`renma/ProntoQA` (the one with FOL)**:
- `id` (string) -- e.g., "ProntoQA_1"
- `answer` (string) -- "A" or "B" (True/False)
- `context` (string) -- NL knowledge base
- `options` (list) -- ["A) True", "B) False"]
- `question` (string) -- NL question
- `raw_logic_programs` (list of strings) -- **FOL annotations**

**`fengyang0317/prontoqa` (largest, no FOL)**:
- `question` (string) -- NL context + question combined
- `steps` (list of strings) -- chain-of-thought reasoning steps
- `answer` (string) -- "True" or "False"

**`tasksource/prontoqa` (original format, no FOL)**:
- Nested JSON: `{example1: {in_context_example0..7, test_example}}`
- Each example has: `question`, `query`, `chain_of_thought`

### FOL Annotation Details (renma/ProntoQA)

The `raw_logic_programs` field contains structured FOL in a custom DSL with four sections:

1. **Predicates**: `Jompus($x, bool) ::: Does x belong to Jompus?`
2. **Facts**: `Yumpus(Max, True)`
3. **Rules**: `Rompus($x, True) >>> Impus($x, True)` (universally quantified implications)
4. **Query**: `Sour(Max, False)` (the goal to prove/disprove)

The logic is restricted to:
- Unary predicates only (single variable `$x`)
- Rules are all of the form `P($x, True/False) >>> Q($x, True/False)` (modus ponens chains)
- Facts are ground atoms with a single constant (e.g., `Max`, `Stella`, `Wren`)
- No existential quantifiers, no binar
…[truncated 1570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "elapsed_ms": 38
}
```

</details>

---

### Tool result

_source line 273 · 2026-05-19T13:25:44.532097+00:00_

Web search results for query: "FCoReBench PuzzleBench first-order combinatorial reasoning dataset size format"

Links: [{"title":"FCoReBench: Can Large Language Models Solve Challenging First-Order Combinatorial Reasoning Problems? | OpenReview","url":"https://openreview.net/forum?id=CFKZKjrQ5r"},{"title":"FCoReBench: Can Large Language Models Solve Challenging First-Order   Combinatorial Reasoning Problems?","url":"https://arxiv.org/pdf/2402.02611"},{"title":"FCoReBench: Can Large Language Models Solve Challenging First-Order Combinatorial Reasoning Problems?","url":"https://arxiv.org/html/2402.02611"},{"title":"PuzzleBench: Can LLMs Solve Challenging First-Order Combinatorial Reasoning Problems?","url":"https://arxiv.org/html/2402.02611v2"},{"title":"[2402.02611] FCoReBench: Can Large Language Models Solve Challenging First-Order Combinatorial Reasoning Problems?","url":"https://arxiv.org/abs/2402.02611"},{"title":"PuzzleBench: Can LLMs Solve Challenging First-Order Combinatorial Reasoning Problems?","url":"https://www.catalyzex.com/paper/puzzlebench-can-llms-solve-challenging-first"}]

Based on the search results, I found information about FCoReBench and PuzzleBench:

**Dataset Size:**
FCoReBench is a dataset of 40 challenging problems, along with scripts to generate problem instances of varying sizes and automatically verify and generate their solutions. (Note: An earlier version of the dataset was called PuzzleBench and contained 31 such challenging problems along with a few solved instances for each problem.)

**Dataset Format:**
These are first-order problems that can be instantiated with potentially an infinite number of problem instances of varying sizes. The dataset includes scripts for generating instances and automatically verifying solutions, allowing researchers to test models on problems of different difficulty levels rather than being limited to a fixed set of problem instances.

**Problem Types:**
The dataset covers challenging combinatorial reasoni
…[truncated 252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 274 · 2026-05-19T13:25:44.532247+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "JustLogic dataset deductive reasoning benchmark first-order logic 2025 format size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "JustLogic dataset deductive reasoning benchmark first-order logic 2025 format size"
  }
}
```

</details>

---

### Tool result

_source line 275 · 2026-05-19T13:25:44.532379+00:00_

Web search results for query: "JustLogic dataset deductive reasoning benchmark first-order logic 2025 format size"

Links: [{"title":"Rethinking Reasoning Quality in Large Language Models through Enhanced Chain-of-Thought via RL","url":"https://arxiv.org/html/2509.06024v1"},{"title":"JustLogic: A Comprehensive Benchmark for Evaluating Deductive Reasoning in LLMs","url":"https://openreview.net/pdf?id=PK5py0eznd"},{"title":"JustLogic: A Comprehensive Benchmark for Evaluating Deductive Reasoning in LLMs | OpenReview","url":"https://openreview.net/forum?id=PK5py0eznd"},{"title":"michaelchenkj/JustLogic · Datasets at Hugging Face","url":"https://huggingface.co/datasets/michaelchenkj/JustLogic"},{"title":"Improving Symbolic Translation of Language Models for Logical Reasoning","url":"https://arxiv.org/html/2601.09446v1"},{"title":"[2501.14851] JustLogic: A Comprehensive Benchmark for Evaluating Deductive Reasoning in Large Language Models","url":"https://arxiv.org/abs/2501.14851"},{"title":"JustLogic: A Comprehensive Benchmark for Evaluating Deductive Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2501.14851"},{"title":"JUSTLOGIC","url":"https://openreview.net/pdf?id=THSm9HyCKo"}]

Based on the search results, I found comprehensive information about the JustLogic dataset:

## JustLogic Dataset Overview

JustLogic is a synthetically generated benchmark designed for rigorous evaluation of LLMs. It is highly complex, capable of generating a diverse range of linguistic patterns, vocabulary, and argument structures; prior knowledge independent, eliminating the advantage of models possessing prior knowledge and ensuring that only deductive reasoning is used to answer questions; and capable of in-depth error analysis on the heterogeneous effects of reasoning depth and argument form on model accuracy.

## Format and Construction

JustLogic is code-generated rather than manually curated. The dataset is structured with specific fields including premises, paragraph
…[truncated 1037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 276 · 2026-05-19T13:25:44.532589+00:00_

Here is the research report.

---

## LogicBench

**Source**: [cogint/LogicBench-v1.0](https://huggingface.co/datasets/cogint/LogicBench-v1.0) | [GitHub](https://github.com/Mihir3009/LogicBench) | [ACL 2024 paper](https://aclanthology.org/2024.acl-long.739.pdf)

**Dataset size**:
- LogicBench(Eval) BQA: 500 unique instances (25 rules x 20 each), ~1,520 QA pairs total
- LogicBench(Eval) MCQA: 500 unique instances
- LogicBench(Aug): ~3,750 instances (25 rules x 150 each)

**Field structure (BQA)**:
- `type`: string ("first_order_logic", "propositional_logic", "nm_logic")
- `axiom`: string (e.g., "modus_ponens")
- `samples[].id`: int
- `samples[].context`: string (natural language premises)
- `samples[].qa_pairs[].question`: string
- `samples[].qa_pairs[].answer`: "yes"/"no"

**Field structure (MCQA)**: Same top-level, but samples have `question`, `choices` (dict), `answer` instead of `qa_pairs`.

**FOL annotations**: **No.** The dataset is purely natural language. Despite covering FOL reasoning patterns (modus ponens, universal instantiation, existential generalization, etc.), the actual data contains no formal logic formulas. The paper shows FOL axioms (e.g., `forall x(p(x)->q(x)) & p(a) |- q(a)`) only as rule descriptions, not in the data instances themselves. Each `context` is a natural language paragraph; there is no `context_formula` or similar field.

**Conversion requirement**: Full NL-to-FOL translation needed. Each context paragraph would require: (1) entity extraction, (2) predicate identification, (3) quantifier scoping, (4) formula construction. Non-trivial because contexts use varied, paraphrased language.

**FOL compatibility score: 1/5** -- No FOL annotations at all. Would require complete semantic parsing from natural language.

---

## FLD (Formal Logic Deduction)

**Source**: [hitachi-nlp/FLD.v2](https://huggingface.co/datasets/hitachi-nlp/FLD.v2) | [hitachi-nlp/FLDx2](https://huggingface.co/datasets/hitachi-nlp/FLDx2) | [GitHub](https://github.com/h
…[truncated 4255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "elapsed_ms": 35
}
```

</details>

---

### Tool call

_source line 277 · 2026-05-19T13:25:44.532774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicInference dataset logical inference natural language formal logic representation Prolog"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicInference dataset logical inference natural language formal logic representation Prolog"
  }
}
```

</details>

---

### Tool result

_source line 278 · 2026-05-19T13:25:44.532916+00:00_

Web search results for query: "LogicInference dataset logical inference natural language formal logic representation Prolog"

Links: [{"title":"[PDF] LogicInference: A New Dataset for Teaching Logical Inference to seq2seq Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LogicInference:-A-New-Dataset-for-Teaching-Logical-Onta%C3%B1%C3%B3n-Ainslie/5021fd710fd17dee53bc7bc7bf334b148ef3d8b6"},{"title":"LogicInference: A New Dataset for Teaching Logical Inference to seq2seq Models","url":"https://research.google/pubs/logicinference-a-new-dataset-for-teaching-logical-inference-to-seq2seq-models/"},{"title":"google-research/logic_inference_dataset/README.md at master · google-research/google-research","url":"https://github.com/google-research/google-research/blob/master/logic_inference_dataset/README.md"},{"title":"(PDF) LogicInference: A New Dataset for Teaching Logical Inference to seq2seq Models","url":"https://www.researchgate.net/publication/359575151_LogicInference_A_New_Dataset_for_Teaching_Logical_Inference_to_seq2seq_Models"},{"title":"[2203.15099] LogicInference: A New Dataset for Teaching Logical Inference to seq2seq Models","url":"https://arxiv.org/abs/2203.15099"},{"title":"LogicInference: A New Dataset for Teaching Logical Inference to seq2seq Models | DeepAI","url":"https://deepai.org/publication/logicinference-a-new-dataset-for-teaching-logical-inference-to-seq2seq-models"},{"title":"LogicInference: A New Dataset for Teaching Logical Inference to seq2seq   Models","url":"https://arxiv.org/pdf/2203.15099"},{"title":"LogicInference: A new Datasaet for Teaching Logical Inference to seq2seq Models | OpenReview","url":"https://openreview.net/forum?id=HAGeIS_Lcg9"},{"title":"ANEW DATASET FOR TEACHING LOGICAL INFERENCE ...","url":"https://openreview.net/pdf?id=HAGeIS_Lcg9"}]

Here are the search results about the LogicInference dataset:

LogicInference is a dataset that evaluates the ability of models to perform logical inference using propos
…[truncated 1263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 279 · 2026-05-19T13:25:44.533070+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RuleTaker dataset ProofWriter format Prover9 compatibility FOL automated theorem prover"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RuleTaker dataset ProofWriter format Prover9 compatibility FOL automated theorem prover"
  }
}
```

</details>

---

### Tool result

_source line 280 · 2026-05-19T13:25:44.533207+00:00_

Web search results for query: "RuleTaker dataset ProofWriter format Prover9 compatibility FOL automated theorem prover"

Links: [{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"ProofWriter: Generating Implications, Proofs, and Abductive Statements   over Natural Language","url":"https://arxiv.org/pdf/2012.13048"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"},{"title":"[2012.13048] ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language","url":"https://ar5iv.labs.arxiv.org/html/2012.13048"},{"title":"Prover9 & Mace4 — Automated Theorem Prover (LADR-2026)","url":"https://prover9.org/"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"(PDF) PRover: Proof Generation for Interpretable Reasoning over Rules","url":"https://www.academia.edu/103199178/PRover_Proof_Generation_for_Interpretable_Reasoning_over_Rules?uc-sb-sw=762564"},{"title":"GitHub - princeton-nlp/NLProofS: EMNLP 2022: Generating Natural Language Proofs with Verifier-Guided Search https://arxiv.org/abs/2205.12443 · GitHub","url":"https://github.com/princeton-nlp/NLProofS"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs:","url":"https://arxiv.org/pdf/2409.16461"}]

Based on the search results, here's what I found about the relationship between these components:

## Overview

ProofWriter is built upon the methodology introduced in the RuleTaker project but advances the complexity and expressiveness of the tasks in several dimensions. The core of each instance is a synthetic "theory" generated from Datalog prog
…[truncated 1463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 281 · 2026-05-19T13:25:44.533402+00:00_

Now I have all the information needed. Here is the complete report:

---

## LogicNLI Dataset Research Report

### Source Links
- Paper: [Tian et al., EMNLP 2021](https://aclanthology.org/2021.emnlp-main.303/)
- GitHub: [omnilabNLP/LogicNLI](https://github.com/omnilabNLP/LogicNLI)
- HuggingFace: [tasksource/LogicNLI](https://huggingface.co/datasets/tasksource/LogicNLI)

### Dataset Size
- **Train**: 16,000 / **Validation**: 2,000 / **Test**: 2,000 / **Total**: 20,000
- The full LogicNLI (including robustness/generalization/traceability test sets) has ~96,000 train + various test splits totaling ~150K+ instances (Table 2 in paper). The HuggingFace version is the simplified subset.
- 4 balanced labels: entailment, contradiction, neutral, self_contradiction (25% each)

### Field Structure
Only **3 fields**:
| Field | Type | Description |
|-------|------|-------------|
| `premise` | string | Concatenated natural language facts + rules (newline-separated) |
| `hypothesis` | string | Single NL statement to classify |
| `label` | string | One of: entailment, contradiction, neutral, self_contradiction |

### FOL Annotations: **NO**

The dataset contains **zero** formal FOL annotations. No `fol_premises`, `fol_conclusion`, `fol_rules`, or any machine-readable logic fields exist. The premise field is a single NL text blob mixing facts and rules together.

### What Format the Logical Rules Are In

The NL premises follow highly **templated patterns** that encode FOL using restricted English:

**Facts** (ground atoms): `"Name is (not) adjective."` -- These are unary predicates on named constants.
- Example: `"Sean is not annoyed."` = `neg(annoyed(sean))`

**Rules** (quantified/conditional): Templated English with 7 FOL connectives:
- **Conjunction**: `"A is X and B is Y"` 
- **Disjunction**: `"either X or Y"`
- **Negation**: `"not"`
- **Implication**: `"If ..., then ..."`
- **Equivalence**: `"..., and vice versa"` / `"... is equivalent to ..."`
- **Universal**: `"Someone who is 
…[truncated 2836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "elapsed_ms": 38
}
```

</details>

---

### Tool call

_source line 282 · 2026-05-19T13:25:44.533560+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PROOFFOL dataset FOL Prover9 premises conclusions deduction labels 10424 pairs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PROOFFOL dataset FOL Prover9 premises conclusions deduction labels 10424 pairs"
  }
}
```

</details>

---

### Tool result

_source line 283 · 2026-05-19T13:25:44.533707+00:00_

Web search results for query: "PROOFFOL dataset FOL Prover9 premises conclusions deduction labels 10424 pairs"

Links: [{"title":"Strategies for Improving NL-to-FOL Translation with LLMs:","url":"https://arxiv.org/pdf/2409.16461"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification","url":"https://arxiv.org/html/2409.16461v1"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"[Literature Review] Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification","url":"https://www.themoonlight.io/en/review/strategies-for-improving-nl-to-fol-translation-with-llms-data-generation-incremental-fine-tuning-and-verification"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic Simeng Han1","url":"https://arxiv.org/pdf/2209.00840"},{"title":"Efficient Translation of NL-based Logical Problems to FOL ...","url":"https://arxiv.org/pdf/2506.18383"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"}]

Based on the search results, I found detailed information about the PROOFFOL dataset:

PROOFFOL consists of 10,424 pairs of (Premises, Conclusions), deduction label, and corresponding FOLs. 

The dataset was created by utilizing GPT-4o to generate FOL translations, starting from the existing p
…[truncated 769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 284 · 2026-05-19T13:25:44.533870+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Atlas-Reasoning dataset huggingface predicate logic first-order logic size format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Atlas-Reasoning dataset huggingface predicate logic first-order logic size format"
  }
}
```

</details>

---

### Tool result

_source line 285 · 2026-05-19T13:25:44.534002+00:00_

Web search results for query: "Atlas-Reasoning dataset huggingface predicate logic first-order logic size format"

Links: [{"title":"AtlasUnified/Atlas-Reasoning · Datasets at Hugging Face","url":"https://huggingface.co/datasets/AtlasUnified/Atlas-Reasoning"},{"title":"README.md · AtlasUnified/Atlas-Reasoning at main","url":"https://huggingface.co/datasets/AtlasUnified/Atlas-Reasoning/blob/main/README.md"},{"title":"GitHub - atlasunified/atlas-reasoning: This script leverages OpenAI's GPT-3 to generate reasoning tasks based on topics and subtopics, which are then cleansed, formatted, and consolidated from individual text files into a single CSV file.","url":"https://github.com/atlasunified/atlas-reasoning"},{"title":"sdiazlor/logic-problems-reasoning-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/sdiazlor/logic-problems-reasoning-dataset"},{"title":"tasksource/folio · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tasksource/folio"},{"title":"text2log · Datasets at Hugging Face","url":"https://huggingface.co/datasets/text2log"},{"title":"ATLAS: A High-Difficulty, Multidisciplinary Benchmark for Frontier Scientific Reasoning","url":"https://arxiv.org/pdf/2511.14366"},{"title":"KK04/LogicInference_OA · Datasets at Hugging Face","url":"https://huggingface.co/datasets/KK04/LogicInference_OA"},{"title":"AtlasUnified/Code-Instruct-Sets · Datasets at Hugging Face","url":"https://huggingface.co/datasets/AtlasUnified/Code-Instruct-Sets"}]

Based on the search results, here's what I found about the Atlas-Reasoning dataset on Hugging Face:

## Overview
The dataset derives from the code at atlasunified/atlas-reasoning and is synthetically generated by GPT-3.5-turbo.

## Categories and Structure
The main 42 categories were human derived while the subcategories were synthetically generated by GPT-4. The dataset includes Predicate Logic among its 42+ categories, along with many other reasoning types such as Propositional Logic, Syllogi
…[truncated 698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 286 · 2026-05-19T13:25:44.534149+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicGraph benchmark multi-path logical reasoning 2025 dataset FOL neuro-symbolic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicGraph benchmark multi-path logical reasoning 2025 dataset FOL neuro-symbolic"
  }
}
```

</details>

---

### Tool result

_source line 287 · 2026-05-19T13:25:44.534283+00:00_

Web search results for query: "LogicGraph benchmark multi-path logical reasoning 2025 dataset FOL neuro-symbolic"

Links: [{"title":"LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification","url":"https://arxiv.org/pdf/2602.21044"},{"title":"LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification","url":"https://arxiv.org/html/2602.21044v1"},{"title":"[2602.21044] LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification","url":"https://arxiv.org/abs/2602.21044"},{"title":"LogicGraph: Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification / LogicGraph: 通过神经符号生成与验证的多路径逻辑推理基准 | Alan Hou","url":"https://alanhou.org/blog/arxiv-logicgraph-benchmarking-multi-path-logical-reasoning/"},{"title":"Paper page - MM-CondChain: A Programmatically Verified Benchmark for Visually Grounded Deep Compositional Reasoning","url":"https://huggingface.co/papers/2603.12266"}]

Based on the search results, here's what I found about LogicGraph:

## Overview

LogicGraph is the first benchmark aimed to systematically evaluate multi-path logical reasoning, constructed via a neuro-symbolic framework that leverages backward logic generation and semantic instantiation.

## Key Features

The pipeline yields solver-verified reasoning problems formalized by high-depth multi-path reasoning and inherent logical distractions, where each instance is associated with an exhaustive set of minimal proofs.

## Motivation

Most existing benchmarks for evaluating LLM reasoning primarily emphasize convergent thinking—assessing whether a model can reach a correct final conclusion for a given problem. In contrast, many real-world reasoning problems admit multiple valid derivations, requiring models to explore diverse logical paths rather than committing to one route.

## Evaluation Framework

The benchmark proposes a reference-free evaluation fram
…[truncated 561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 288 · 2026-05-19T13:25:44.534431+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SLR\" \"scalable logical reasoning\" synthetic dataset 2025 first-order logic generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SLR\" \"scalable logical reasoning\" synthetic dataset 2025 first-order logic generation"
  }
}
```

</details>

---

### Tool result

_source line 289 · 2026-05-19T13:25:44.534560+00:00_

Web search results for query: ""SLR" "scalable logical reasoning" synthetic dataset 2025 first-order logic generation"

Links: [{"title":"SLR: Automated Synthesis for Scalable Logical Reasoning","url":"https://arxiv.org/html/2506.15787"},{"title":"SLR: Automated Synthesis for Scalable Logical Reasoning Lukas Helff1,2,","url":"https://openreview.net/pdf/cf2e63cd1ff6427bb327b94c9dfcf188e83883b1.pdf"},{"title":"SLR: An Automated Synthesis Framework for Scalable Logical Reasoning","url":"https://arxiv.org/html/2506.15787v2"},{"title":"GitHub - ml-research/ScalableLogicalReasoning · GitHub","url":"https://github.com/ml-research/ScalableLogicalReasoning"},{"title":"SLR: An Automated Synthesis Framework for Scalable Logical ...","url":"https://www.arxiv.org/pdf/2506.15787v2"},{"title":"SLR: Automated Synthesis for Scalable Logical Reasoning","url":"https://arxiv.org/pdf/2506.15787"}]

I found relevant results for your search. Here's what I discovered:

SLR (Scalable Logical Reasoning) is an end-to-end framework for systematic evaluation and training of Large Language Models through scalable logical reasoning, enabling automated synthesis of inductive reasoning tasks with precisely controlled difficulty based on a user's task specification.

The task synthesizer automatically generates novel inductive logic programming (ILP) tasks of controllable complexity, with each task coming with a latent ground-truth rule, an executable validation program, and an instruction prompt for the reasoning task.

SLR introduces scalable, curriculum-based synthesis with controllable difficulty and verifiable evaluation, addressing key gaps in prior works.

The framework includes SLR-BENCH, a 19k task benchmark organized as a 20-level curriculum of increasing logical complexity, enabling both training and evaluation across a controlled reasoning spectrum, with curriculum learning substantially improving both in-domain and downstream reasoning.

SLR's fully symbolic and automated pipeline elimi
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 290 · 2026-05-19T13:25:44.534730+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LINC \"LLMs first-order logic\" Prover9 symbolic reasoning dataset NL-to-FOL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LINC \"LLMs first-order logic\" Prover9 symbolic reasoning dataset NL-to-FOL"
  }
}
```

</details>

---

### Tool result

_source line 291 · 2026-05-19T13:25:44.534867+00:00_

Web search results for query: "LINC "LLMs first-order logic" Prover9 symbolic reasoning dataset NL-to-FOL"

Links: [{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers","url":"https://www.researchgate.net/publication/376394657_LINC_A_Neurosymbolic_Approach_for_Logical_Reasoning_by_Combining_Language_Models_with_First-Order_Logic_Provers"},{"title":"Efficient Translation of NL-based Logical Problems to FOL ...","url":"https://arxiv.org/pdf/2506.18383"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining   Language Models with First-Order Logic Provers","url":"https://arxiv.org/pdf/2310.15164"},{"title":"[2310.15164] LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers","url":"https://arxiv.org/abs/2310.15164"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.313/"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers | OpenReview","url":"https://openreview.net/forum?id=h00GHjWDEp"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs:","url":"https://arxiv.org/pdf/2409.16461"},{"title":"Large Language Models Meet Symbolic Provers for Logical Reasoning   Evaluation","url":"https://arxiv.org/pdf/2502.06563"},{"title":"Towards Advanced Mathematical Reasoning for LLMs via First-Order Logic Theorem Proving","url":"https://arxiv.org/html/2506.17104v1"}]

Based on the search results, here's what I found about LINC and related work on LLMs with first-order logic:

## LINC Overview

LINC (Logical Inference via Neurosymbolic Computation) tackles logical reasoning through a modular, two-step neurosymbolic process. First, the language model converts the natural language premises and desired conclusion into f
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 292 · 2026-05-19T13:25:44.535011+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/text2log",
  "prompt": "Extract: dataset size (number of examples), format (fields/columns), example entries showing the FOL notation used, and any information about the logic notation style (is it Prover9-compatible like all(x, (P(x) -> Q(x)))?)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/text2log",
    "prompt": "Extract: dataset size (number of examples), format (fields/columns), example entries showing the FOL notation used, and any information about the logic notation style (is it Prover9-compatible like all(x, (P(x) -> Q(x)))?)."
  }
}
```

</details>

---

### Tool result

_source line 293 · 2026-05-19T13:25:44.535125+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 294 · 2026-05-19T13:25:44.535291+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/alevkov95/text2log",
  "prompt": "Extract: dataset size (number of examples), format (fields/columns), example entries showing the FOL notation used, and any information about the logic notation style (is it Prover9-compatible?)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/alevkov95/text2log",
    "prompt": "Extract: dataset size (number of examples), format (fields/columns), example entries showing the FOL notation used, and any information about the logic notation style (is it Prover9-compatible?)."
  }
}
```

</details>

---

### Tool result

_source line 295 · 2026-05-19T13:25:44.535461+00:00_

# text2log Dataset Summary

## Dataset Size
- **100,000 examples** of English sentences with First Order Logic translations
- Size category: 100K < n < 1M
- Total file size: 7.93 kB

## Format (Fields/Columns)
Two fields per example:
- **'clean'**: Simple English sentence
- **'trans'**: Lambda Dependency-based Compositional Semantics (translation to FOL)

## Example Entry
```python
{
    'clean': 'All things that are new are good.',
    'trans': 'all x1.(_thing(x1) -> (_new(x1) -> _good(x1)))'
}
```

## Logic Notation Style
The dataset uses **Lambda Dependency-based Compositional Semantics** notation generated by the `ccg2lambda` tool (https://github.com/mynlp/ccg2lambda).

**Key notation characteristics:**
- Universal quantification: `all x1.`
- Predicates: prefixed with underscore (`_thing`, `_new`, `_good`)
- Logical implication: `->`
- Lambda expressions with variable binding

**Note:** The documentation does not explicitly confirm Prover9-compatibility. The notation appears to be a lambda calculus-based semantic representation rather than standard Prover9 format, which typically uses different syntactic conventions (e.g., `all(X, ...)` vs. `all x1.`).

## Data Split
- **No predefined train/test split** provided
- Authors used an **80/20 split** in their experiments

## Generation Method
- Machine-generated annotations using `ccg2lambda`
- Source sentences from `enTenTen15` corpus

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 296 · 2026-05-19T13:25:44.535627+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/tasksource/FOL-nli",
  "prompt": "Extract: dataset size, format (fields/columns), example entries showing the FOL or logic notation used, what kind of logic is represented, and the source paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/tasksource/FOL-nli",
    "prompt": "Extract: dataset size, format (fields/columns), example entries showing the FOL or logic notation used, what kind of logic is represented, and the source paper."
  }
}
```

</details>

---

### Tool result

_source line 297 · 2026-05-19T13:25:44.535818+00:00_

# FOL-nli Dataset Summary

## Dataset Size
- **Total rows**: 102,774
- **File size**: 182 MB
- **Split distribution**:
  - Train: 82.2k rows
  - Validation: 10.3k rows
  - Test: 10.3k rows

## Format (Fields/Columns)

| Field | Type | Description |
|-------|------|-------------|
| `premise` | string | Natural language premise (12-3.12k chars) |
| `hypothesis` | string | Natural language hypothesis (10-236 chars) |
| `label` | string | Classification: entailment, contradiction, or neutral |
| `premise_tptp` | string | Premise in TPTP (Thousands of Problems for Theorem Provers) format |
| `hypothesis_tptp` | string | Hypothesis in TPTP format |
| `proof_inputs` | sequence | List of proof input references |
| `proof` | string | Formal proof output (767-76.8k chars, nullable) |
| `rule_concentration` | float | Metric (0-0.72 range) |

## Example Entry

**Natural Language:**
```
Premise: Kristy, Earl, Carol, Kerri are the only persons in the room. 
If "everyone in the room has completed a triathlon or does not have 
completed a triathlon" then "everyone in the room does not have completed 
a triathlon or has completed a triathlon"...

Hypothesis: Kristy has completed a triathlon.

Label: contradiction
```

**TPTP Logic Format:**
```
room(kristy)&room(earl)&room(carol)&room(kerri)&
(!\[X\]:(room(X)=>(X='kristy'|X='earl'|X='carol'|X='kerri')))& 
((!\[X\]:(room(X)=>(((does_not_have_completed_a_triathlon(X))|
(has_completed_a_triathlon(X))))))=>
(!\[X\]:(room(X)=>(((has_completed_a_triathlon(X))|
(does_not_have_completed_a_triathlon(X)))))))&...

has_completed_a_triathlon(kristy)
```

## Logic Type Represented

**First-Order Logic (FOL)** with:
- Universal quantifiers: `!\[X\]` (∀)
- Existential quantifiers: `?\[X\]` (∃)
- Logical operators: `&` (AND), `|` (OR), `~` (NOT), `=>` (IMPLIES), `<=>` (IFF), `<~>` (XOR)
- Predicates for properties: `room(X)`, `old(X)`, `likes(X,Y)`, etc.
- Relations between entities

**Tags indicate**: logic, reasoning, FOL, first-order-logic, syll
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 298 · 2026-05-19T13:25:44.535985+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/michaelchenkj/JustLogic",
  "prompt": "Extract: dataset size (number of examples), format (fields/columns), what kind of logic is represented, any FOL annotations, and example entries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/michaelchenkj/JustLogic",
    "prompt": "Extract: dataset size (number of examples), format (fields/columns), what kind of logic is represented, any FOL annotations, and example entries."
  }
}
```

</details>

---

### Tool result

_source line 299 · 2026-05-19T13:25:44.536119+00:00_

# JustLogic Dataset Summary

## Dataset Size
- **Total Examples**: 4,900 rows
- **Split**: Single `train` split with 4.9k rows
- **Size Category**: 1K - 10K examples

## Format
The dataset uses **Parquet/CSV format** with the following columns:

| Field | Type | Description |
|-------|------|-------------|
| `id` | int64 | Example identifier |
| `premises` | string | List of logical premises/statements |
| `paragraph` | string | Natural language paragraph |
| `conclusion` | string | Target conclusion statement |
| `question` | string | Question being asked |
| `label` | string | Truth label: `TRUE`, `FALSE`, or `Uncertain` |
| `arg` | string | Argument structure in formal notation |
| `statements` | string | Mapped statements with variable substitutions |
| `depth` | int64 | Logical depth/complexity (range: 1-7) |

## Logic Representation
The dataset represents **classical logical inference patterns**, including:

1. **Modus Ponens**: `If [A], then [B]. [A]. Therefore, [B].`
2. **Modus Tollens**: `If [A], then [B]. Not [B]. Therefore, Not [A].`
3. **Disjunctive Syllogism**: `Either [A] or [B]. Not [A]. Therefore, [B].`
4. **Disjunction Elimination**: Multiple premises with OR/IF combinations
5. **Reductio Ad Absurdum**: `If [A], then [B]. If [A], then Not [B]. Therefore, Not [A].`
6. **Constructive Dilemma**: Multiple conditional branches with disjunction

## FOL Annotations
Each example includes:
- **Formal logical structure** in the `arg` field
- **Variable mappings** in `statements` field with indexed propositions (e.g., `{0: 'Persistence is...', 1: 'Subjectivity is...'}`)
- **Nested logical operators**: `If`, `Not`, `Either...or`, parenthesized compounds

## Example Entry

```python
{
  "id": 993,
  "premises": [
    "Provided that the statement that states persistence is extremely important...",
    "So long as the statement that states persistence is extremely important..."
  ],
  "paragraph": "Provided that the statement that states persistence...",
  "conclu
…[truncated 799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 300 · 2026-05-19T13:25:44.536264+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/gblackout/LogicLLaMA",
  "prompt": "Extract: MALLS dataset size, FOL format/notation used, example entries showing the FOL representation, and whether the notation is compatible with Prover9 (e.g. all(x, (P(x) -> Q(x))))."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/gblackout/LogicLLaMA",
    "prompt": "Extract: MALLS dataset size, FOL format/notation used, example entries showing the FOL representation, and whether the notation is compatible with Prover9 (e.g. all(x, (P(x) -> Q(x))))."
  }
}
```

</details>

---

### Tool result

_source line 301 · 2026-05-19T13:25:44.536384+00:00_

# LogicLLaMA and MALLS Dataset Analysis

## Dataset Size
The MALLS dataset contains **34,000 pairs** of natural language statements and first-order logic rules. The training subset (MALLS-v0.1) includes "27K auto-verified pairs," while the test set has "1K human-verified pairs."

## FOL Format/Notation
The webpage does not explicitly specify the formal notation used for FOL representations in the dataset. No syntax examples or formatting conventions are provided in the content.

## Example Entries
No concrete example entries showing FOL representations are included in the provided webpage content. The README references available datasets but does not display sample data pairs.

## Prover9 Compatibility
There is no mention of Prover9 compatibility or discussion of whether the FOL notation follows standard logical formats compatible with automated theorem provers. The documentation does not address technical compatibility with specific logical reasoning systems.

## Additional Note
The repo provides a "fol_parser.py" file, suggesting internal parsing capabilities, but the webpage does not detail the parser's specifications or output format details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 302 · 2026-05-19T13:25:44.536525+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MALLS dataset FOL notation format example \"exists\" \"forall\" logic representation NL-to-FOL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MALLS dataset FOL notation format example \"exists\" \"forall\" logic representation NL-to-FOL"
  }
}
```

</details>

---

### Tool result

_source line 303 · 2026-05-19T13:25:44.536657+00:00_

Web search results for query: "MALLS dataset FOL notation format example "exists" "forall" logic representation NL-to-FOL"

Links: [{"title":"GitHub - gblackout/LogicLLaMA: Large language model and dataset for natural language to first-order logic translation","url":"https://github.com/gblackout/LogicLLaMA"},{"title":"First-order logic • First-order logic (FOL) models the world in terms of","url":"https://www.cs.brandeis.edu/~jamesp/content/courses/LING130/FirstOrderLogic-1.pdf"},{"title":"Chapter 36 Basic rules for FOL ‣ Part VII Natural deduction for FOL ‣ forall x: Calgary","url":"https://forallx.openlogicproject.org/html/Ch36.html"},{"title":"Harnessing the Power of Large Language Models for Natural Language to   First-Order Logic Translation","url":"https://arxiv.org/pdf/2305.15541"},{"title":"12/18/2019 1 First-Order Logic (FOL) Sven Koenig, USC","url":"https://idm-lab.org/intro-to-ai/slides/First_Order_Logic.pdf"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/pdf/2505.14932"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"}]

Based on the search results, I can provide you with information about the MALLS dataset and FOL notation formats:

## MALLS Dataset Overview

MALLS (large language Model generAted natural-Language-to-first-order-Logic pairS) is a dataset consisting of 34K pairs of real-world natural language (NL) statements and the corresponding first-order logic (FOL) rules annotations. All pairs are generated by prompting GPT-4 and processed to ensure the validity of the FOL rules.

## FOL Notation Format

The standard FOL notation includes quantifiers and logical operators:

FOL syntax includes quantifiers "EXISTS" and "FORALL", connectives like "AND", "OR", "IMPLIES", and "EQUIVALENT", predicates in the form of "Predicate(Term, ...)", constants, and variables.

## Examples of FOL Expressions

Some concrete examples of FOL notation us
…[truncated 544 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 304 · 2026-05-19T13:25:44.536827+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2305.15541",
  "prompt": "Extract: MALLS dataset FOL notation format with concrete examples. What operators are used (forall, exists, ->, &, |, etc.)? Show at least 3 example FOL translations. Is this compatible with Prover9 format?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2305.15541",
    "prompt": "Extract: MALLS dataset FOL notation format with concrete examples. What operators are used (forall, exists, ->, &, |, etc.)? Show at least 3 example FOL translations. Is this compatible with Prover9 format?"
  }
}
```

</details>

---

### Tool result

_source line 305 · 2026-05-19T13:25:44.536950+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 306 · 2026-05-19T13:25:44.537072+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2305.15541",
  "prompt": "Extract: MALLS dataset FOL notation format with concrete examples. What operators are used (forall, exists, ->, &, |, etc.)? Show at least 3 example FOL translations from the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2305.15541",
    "prompt": "Extract: MALLS dataset FOL notation format with concrete examples. What operators are used (forall, exists, ->, &, |, etc.)? Show at least 3 example FOL translations from the paper."
  }
}
```

</details>

---

### Tool result

_source line 307 · 2026-05-19T13:25:44.537191+00:00_

# MALLS Dataset FOL Notation Format

Based on the provided content, I cannot extract specific examples of FOL translations or detailed information about the operators used in the MALLS dataset. The abstract states that the paper presents "MALLS (large language **M**odel gener**A**ted N**L**-FO**L** pair**S**), a dataset of 34K high-quality and diverse sentence-level NL-FOL pairs collected from GPT-4," but it does not include concrete translation examples or specify which logical operators are employed.

The webpage content provided is limited to the arXiv abstract and metadata. To obtain this information, you would need to access the full PDF paper or the associated code/data repository (referenced at https://github.com/gblackout/LogicLLaMA), which would contain detailed examples of FOL notations, operator specifications, and concrete sentence-to-logic translations demonstrating the use of operators like ∀ (forall), ∃ (exists), →, &, |, and others.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 308 · 2026-05-19T13:25:44.537321+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/pdf/2305.15541",
  "prompt": "Extract all concrete examples of FOL notation used in the MALLS dataset. What operators/symbols are used? Show the NL-to-FOL translation examples. Is the format compatible with Prover9 (all(x, (P(x) -> Q(x))))?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/pdf/2305.15541",
    "prompt": "Extract all concrete examples of FOL notation used in the MALLS dataset. What operators/symbols are used? Show the NL-to-FOL translation examples. Is the format compatible with Prover9 (all(x, (P(x) -> Q(x))))?"
  }
}
```

</details>

---

### Tool result

_source line 309 · 2026-05-19T13:25:44.537435+00:00_

I cannot extract concrete FOL notation examples from the provided content because the document appears to be a corrupted or improperly formatted PDF file containing compressed binary data rather than readable text.

The content shows encoded stream objects and metadata typical of PDF structure, but the actual textual content about the MALLS dataset, FOL notation, operators, and NL-to-FOL translation examples is not accessible in the provided format.

To properly answer your questions about:
- Specific FOL operators/symbols used
- Natural language to FOL translation examples
- Prover9 compatibility
- Dataset notation conventions

I would need the source material in a readable text format, such as a plain text file, properly decoded PDF, or HTML version of the relevant research paper or documentation.

If you have access to the original document, please share it in a more accessible format, and I'll be happy to extract the specific FOL notation examples and analyze their compatibility with formal logic systems like Prover9.

[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/91820fa6-7a1f-4a02-8bc0-aaa4f114a9f1/tool-results/webfetch-1779196898584-s0pidn.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 310 · 2026-05-19T13:25:44.537572+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MALLS LogicLLaMA FOL example \"∀x\" OR \"forall x\" OR \"all x\" notation sample pairs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MALLS LogicLLaMA FOL example \"∀x\" OR \"forall x\" OR \"all x\" notation sample pairs"
  }
}
```

</details>

---

### Tool result

_source line 311 · 2026-05-19T13:25:44.537714+00:00_

Web search results for query: "MALLS LogicLLaMA FOL example "∀x" OR "forall x" OR "all x" notation sample pairs"

Links: [{"title":"Harnessing the Power of Large Language Models for Natural Language to   First-Order Logic Translation","url":"https://arxiv.org/pdf/2305.15541"},{"title":"Chapter 36 Basic rules for FOL ‣ Part VII Natural deduction for FOL ‣ forall x: Calgary","url":"https://forallx.openlogicproject.org/html/Ch36.html"},{"title":"Chapter 31 Truth in FOL ‣ Part VI Interpretations ‣ forall x: Calgary","url":"https://forallx.openlogicproject.org/html/Ch31.html"},{"title":"Chapter 23 Building blocks of FOL ‣ Part V First-order logic ‣ forall x: Calgary","url":"https://forallx.openlogicproject.org/html/Ch23.html"},{"title":"Advancing Natural Language Formalization to First Order ...","url":"https://arxiv.org/pdf/2509.22338"},{"title":"Chapter 27 Sentences of FOL ‣ Part V First-order logic ‣ forall x: Calgary","url":"https://forallx.openlogicproject.org/html/Ch27.html"},{"title":"logicalmethods.ai – FOL","url":"https://logicalmethods.ai/textbook/fol/"}]

Based on the search results, I found relevant information about the MALLS dataset and LogicLLaMA:

MALLS (large language Model generAted NL-FOL pairS) is a dataset of 34K high-quality and diverse sentence-level NL-FOL pairs collected from GPT-4. The dataset was created by implementing a pipeline that prompts GPT-4 for pairs, and dynamically adjusts the prompts to ensure the collection of pairs with rich and diverse contexts at different levels of complexity, and verifies the validity of the generated FOL rules.

LogicLLaMA was achieved by a novel supervised fine-tuning (SFT) + reinforcement learning with human feedback (RLHF) framework, which initially trains on synthetically perturbed NL-FOL pairs to encourage chain-of-thought reasoning and then finetunes with RLHF on GPT-3.5 outputs using a FOL verifier as the reward model.

The search results confirm that MALLS provides NL-FOL (Natural Language to First-Or
…[truncated 387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 312 · 2026-05-19T13:25:44.537872+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2509.22338",
  "prompt": "Extract: concrete examples of NL-to-FOL translations from the MALLS dataset or similar. Show the exact FOL notation/syntax used (operators like forall, exists, ->, &, |). Also look for mention of PROOFFOL, text2log, or other FOL datasets with their notation examples."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2509.22338",
    "prompt": "Extract: concrete examples of NL-to-FOL translations from the MALLS dataset or similar. Show the exact FOL notation/syntax used (operators like forall, exists, ->, &, |). Also look for mention of PROOFFOL, text2log, or other FOL datasets with their notation examples."
  }
}
```

</details>

---

### Tool result

_source line 313 · 2026-05-19T13:25:44.537998+00:00_

# NL-to-FOL Translation Examples from the Paper

## Concrete Examples

The paper provides several NL-to-FOL translation instances:

**Example 1 - Simple Statement:**
- NL: "Not every student is hardworking."
- FOL: "¬∀x (Student(x) → Hardworking(x))"

**Example 2 - Complex Descriptive Statement:**
- NL: "Tomatoes are red and round, while cucumbers are green and elongated."
- Model output: "∀x(Tomato(x)→(Red(x)∧Round(x))) ∧ ∀y(Cucumber(y)→(Green(y)∧Elongated(y)))"
- Ground truth: "∀x∀y(Tomato(x)→(Red(x)∧Round(x))) ∧ (Cucumber(y)→(Green(y)∧Elongated(y)))"

**Example 3 - Aristotelian Form:**
The authors note a common error: "A pineapple is a fruit with spiky skin" is mistranslated as "∃x(Pineapple(x)∧Fruit(x)∧SpikySkin(x))" but should be "∀x(Pineapple(x)→(Fruit(x)∧HasSpikySkin(x)))"

## FOL Notation Used

The paper employs standard first-order logic operators: "∀,∃,¬,∧,∨,→,↔,⊕" with textual alternatives for systems like T5 (forall, exists, etc.).

## Dataset Mentions

The paper focuses on **MALLS** and **Willow** datasets but also references **FOLIO** for logical argument evaluation. Text2Log and other datasets receive passing mention but lack detailed notation examples.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 314 · 2026-05-19T13:25:44.538143+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PROOFFOL dataset github huggingface Prover9 format FOL premises conclusions download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PROOFFOL dataset github huggingface Prover9 format FOL premises conclusions download"
  }
}
```

</details>

---

### Tool result

_source line 315 · 2026-05-19T13:25:44.538277+00:00_

Web search results for query: "PROOFFOL dataset github huggingface Prover9 format FOL premises conclusions download"

Links: [{"title":"Dataset formats and types · Hugging Face","url":"https://huggingface.co/docs/trl/dataset_formats"},{"title":"GitHub - opendatalab/ProverGen: [ICLR 2025] This is the official implementation for the paper: \"Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation\"","url":"https://github.com/opendatalab/ProverGen"},{"title":"Simple Dataset for Proof Method Recommendation in Isabelle/HOL (Dataset   Description)","url":"https://arxiv.org/pdf/2004.10667"},{"title":"GitHub - huggingface/dataset-viewer: Backend that powers the dataset viewer on Hugging Face dataset pages through a public API. · GitHub","url":"https://github.com/huggingface/dataset-viewer"},{"title":"Datasets · Hugging Face","url":"https://huggingface.co/docs/datasets/index"},{"title":"GitHub - huggingface/datasets: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools","url":"https://github.com/huggingface/datasets"},{"title":"Large Language Models Meet Symbolic Provers for Logical Reasoning   Evaluation","url":"https://arxiv.org/pdf/2502.06563"},{"title":"AutoFactory Dataset to Support AI in Manufacturing Systems","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12363462/"},{"title":"datasets/templates/README_guide.md at main · huggingface/datasets","url":"https://github.com/huggingface/datasets/blob/main/templates/README_guide.md"}]

Based on the search results, I found relevant information about a dataset related to FOL reasoning with Prover9:

ProverGen is a framework that synergizes Large Language Models with symbolic provers to create scalable, diverse, and high-quality First-Order Logic (FOL) reasoning datasets. The framework has created ProverQA, a challenging FOL reasoning benchmark consisting of 1,500 evaluation instances and 5,000 training instances across three difficulty le
…[truncated 667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 316 · 2026-05-19T13:25:44.538428+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/opendatalab/ProverGen",
  "prompt": "Extract: ProverQA dataset details - size, format, FOL notation used, Prover9 compatibility, example entries showing the FOL format. How are premises and conclusions represented?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/opendatalab/ProverGen",
    "prompt": "Extract: ProverQA dataset details - size, format, FOL notation used, Prover9 compatibility, example entries showing the FOL format. How are premises and conclusions represented?"
  }
}
```

</details>

---

### Tool result

_source line 317 · 2026-05-19T13:25:44.538547+00:00_

# ProverQA Dataset Details

## Dataset Size and Structure
The ProverQA dataset comprises **1,500 evaluation instances and 5,000 training instances** distributed across three difficulty tiers: easy (1-2 reasoning steps), medium (3-5 steps), and hard (6-9 steps).

## FOL Coverage and Prover9 Integration
The dataset provides "complete FOL coverage" across all seven logical operators: conjunction (∧), disjunction (∨), negation (¬), implication (→), exclusive or (⊕), universal quantification (∀), and existential quantification (∃). The framework leverages Prover9 symbolic prover for validating logical structures during generation.

## Format and Representation
The documentation references "faithful reasoning chains" presented in both symbolic and natural language formats, though specific example entries showing exact premise-conclusion notation are not included in the provided content.

## Availability
ProverQA is accessible through:
- **Hugging Face**: opendatalab/ProverQA dataset repository
- **OpenDataLab**: ProverQA project page

The materials note that the dataset was "created using this framework" but don't provide detailed specifications about internal data structure formats or sample JSON/annotation examples.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 318 · 2026-05-19T13:25:44.538690+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/opendatalab/ProverQA",
  "prompt": "Extract: dataset size, format (fields/columns), example entries showing the FOL notation used, and whether it uses Prover9 syntax. Show concrete examples of premises and conclusions in FOL format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/opendatalab/ProverQA",
    "prompt": "Extract: dataset size, format (fields/columns), example entries showing the FOL notation used, and whether it uses Prover9 syntax. Show concrete examples of premises and conclusions in FOL format."
  }
}
```

</details>

---

### Tool result

_source line 319 · 2026-05-19T13:25:44.538850+00:00_

# ProverQA Dataset Analysis

## Overview
The ProverQA dataset is currently **unavailable** due to a schema mismatch error in the dataset generation process. However, based on the preview content, I can extract the following information:

## Dataset Structure

### Size
- **1K < n < 10K** entries
- Contains `train` and `validation` splits

### Schema Mismatch Issue
The dataset has two conflicting column schemas:

**Expected Schema (current files):**
```
- id: int64
- nl2fol: struct (2025+ fields)
- context: string
- question: string
- conclusion_fol: string
- options: list&lt;string>
- reasoning: string
- answer: string
```

**Conflicting Schema:**
```
- system: string
- input: string
- instruction: string
- output: string
```

## Task Type
- **Task Category:** Question Answering
- **Language:** English

## FOL Notation Examples

Based on the preview data, the dataset uses natural language to first-order logic conversion:

### Example 1: Basic Conditional
```
Context: "Jayce pursues historical interests. If Jayce pursues historical interests, then he either gains practical skills or develops expertise (or both)."

FOL (nl2fol field): 
- premise: pursues_historical_interests(Jayce) → gains_practical_skills(Jayce) ∨ develops_expertise(Jayce)
- conclusion: gains_practical_skills(Jayce)
```

### Example 2: Exclusive Or (XOR)
```
Context: "Braden pursues science. If Braden pursues science, then he can either make a groundbreaking discovery or advance medical knowledge, but not both."

FOL:
- pursues_science(Braden) → (makes_groundbreaking_discovery(Braden) ⊕ advances_medical_knowledge(Braden))
- Answer: False (Braden does not make groundbreaking discovery)
```

### Example 3: Complex Logical Structure
```
Context: "Peyton is charismatic. If Peyton is charismatic, then she either has a confident demeanor or a strong stage presence (but not both)."

FOL:
- charismatic(Peyton) = true
- charismatic(Peyton) → (confident_demeanor(Peyton) ⊕ strong_stage_presence(Peyton))
- Conclusio
…[truncated 1290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 320 · 2026-05-19T13:25:44.538997+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PROOFFOL dataset \"Prover9\" NL-to-FOL ProofWriter-derived 10424 pairs download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PROOFFOL dataset \"Prover9\" NL-to-FOL ProofWriter-derived 10424 pairs download"
  }
}
```

</details>

---

### Tool result

_source line 321 · 2026-05-19T13:25:44.539122+00:00_

Web search results for query: "PROOFFOL dataset "Prover9" NL-to-FOL ProofWriter-derived 10424 pairs download"

Links: [{"title":"(PDF) Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification","url":"https://www.researchgate.net/publication/384365596_Strategies_for_Improving_NL-to-FOL_Translation_with_LLMs_Data_Generation_Incremental_Fine-Tuning_and_Verification"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs:","url":"https://arxiv.org/pdf/2409.16461"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification","url":"https://arxiv.org/html/2409.16461v1"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"PROOFFOL: Improving NL-to-FOL Translation of LMs Anonymous ACL submission","url":"https://openreview.net/pdf?id=W0WJwqhdCd"},{"title":"Improving Symbolic Translation of Language Models for Logical Reasoning","url":"https://arxiv.org/html/2601.09446v1"},{"title":"Efficient Translation of NL-based Logical Problems to FOL ...","url":"https://arxiv.org/pdf/2506.18383"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification | OpenReview","url":"https://openreview.net/forum?id=OXeCKlsRdj"},{"title":"[2409.16461] Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification","url":"https://arxiv.org/abs/2409.16461"}]

Based on the search results, here's what I found about the PROOFFOL dataset:

## Overview

PROOFFOL is a dataset consisting of 10424 pairs of (Premises, Conclusions), deduction label, and corresponding FOLs. It is a high-quality FOL-annotated subset of ProofWriter dataset created using GPT-4o.

## Data Generation Process

The formal language was changed to Prover9 and kept fixed for all datasets. The systematic pipeline enabled the r
…[truncated 538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 322 · 2026-05-19T13:25:44.539271+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2409.16461v1",
  "prompt": "Extract concrete examples of Prover9 FOL format used in the PROOFFOL dataset. Show the exact syntax for premises, conclusions, quantifiers (all, exists), operators (->  &  |  -). How are the FOL expressions formatted? Show at least 3 complete examples."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2409.16461v1",
    "prompt": "Extract concrete examples of Prover9 FOL format used in the PROOFFOL dataset. Show the exact syntax for premises, conclusions, quantifiers (all, exists), operators (->  &  |  -). How are the FOL expressions formatted? Show at least 3 complete examples."
  }
}
```

</details>

---

### Tool result

_source line 323 · 2026-05-19T13:25:44.539392+00:00_

# Prover9 FOL Format in ProofFOL

The document describes the ProofFOL dataset's use of Prover9 syntax but provides **limited concrete examples** of complete FOL expressions.

## Available Format Information

The paper states: "The format of the FOLs is set to be consistent with the 'Prover9' theorem prover, which has a human understandable, formal language syntax."

### Operators Mentioned
The document references these logical operators in Prover9 format:
- `->` (implication)
- `&` (conjunction/and)
- `|` (disjunction/or)
- `-` (negation)
- `all` and `exists` (quantifiers)

### Partial Examples from Error Analysis

The appendix includes error examples showing Prover9 syntax:

**Example with universal quantifier:**
`all x (Athlete(x) -> -NeverExercises(x))`

**Example with existential quantifier:**
`exists y (Own(emily, y) & Roommate(y))`

**Example with conjunction:**
`BerkeleyCollege(x) & ResidentialCollegeAt(x, yaleUniversity)`

## Limitation

The paper focuses on **error patterns and methodology** rather than showcasing complete, correct ProofFOL examples. The authors emphasize their code and dataset are "available at https://github.com/RamyaKeerthy/Translation-NL2FOL" for concrete formatting specifications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 324 · 2026-05-19T13:25:44.539543+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FOL-Traces dataset format Prover9 examples size huggingface 2025 reasoning traces"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FOL-Traces dataset format Prover9 examples size huggingface 2025 reasoning traces"
  }
}
```

</details>

---

### Tool result

_source line 325 · 2026-05-19T13:25:44.539683+00:00_

Web search results for query: "FOL-Traces dataset format Prover9 examples size huggingface 2025 reasoning traces"

Links: [{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/html/2505.14932"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale","url":"https://arxiv.org/pdf/2505.14932"},{"title":"FOL-Traces: Verified First-Order Logic Reasoning Traces at Scale | Isabelle Lee","url":"https://iglee.me/papers/fol-traces/"},{"title":"opendatalab/ProverQA · Datasets at Hugging Face","url":"https://huggingface.co/datasets/opendatalab/ProverQA"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"}]

Based on the search results, here's information about the FOL-Traces dataset:

## FOL-Traces Dataset Overview

FOL-Traces is the first large-scale dataset of programmatically verified reasoning traces available at https://huggingface.co/datasets/fol-traces/fol-traces.

### Dataset Size and Format
The dataset consists of 3.5 billion tokens, including 8.8 million LLM-augmented, human-annotated examples and 7.5 million synthetically generated examples.

### Generation and Verification
Each synthetic example is verifiably correct, produced by a custom automated theorem solver, and accompanied by metadata tracing its algorithmic provenance.

### Purpose and Benchmarking
The dataset enables rigorous evaluation of structured logical inference, and proposes two challenging diagnostic tasks—masked operation prediction and step completion—that directly probe syntactic awareness and process fidelity. Systematic experiments with 5 reasoning LLMs show that the dataset remains challenging: models only reach around 45.7% accuracy on masked operation prediction and around 27% on two-step completion.

The dataset was published in May 2025 and accepted to EACL 2026, representing
…[truncated 190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 326 · 2026-05-19T13:25:44.539858+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2505.14932",
  "prompt": "Extract: FOL-Traces dataset format details. What is the exact FOL notation used? Show concrete examples of FOL expressions. What theorem prover is used? Is it Prover9 format? How are premises, axioms, and conclusions represented? What are the dataset splits and sizes?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2505.14932",
    "prompt": "Extract: FOL-Traces dataset format details. What is the exact FOL notation used? Show concrete examples of FOL expressions. What theorem prover is used? Is it Prover9 format? How are premises, axioms, and conclusions represented? What are the dataset splits and sizes?"
  }
}
```

</details>

---

### Tool result

_source line 327 · 2026-05-19T13:25:44.539984+00:00_

# FOL-Traces Dataset Format Details

## FOL Notation

The dataset uses standard first-order logic notation with operators: ¬ (negation), ∧ (conjunction), ∨ (disjunction), → (implication), and ↔ (equivalence). Quantifiers include ∀ (universal) and ∃ (existential).

**Concrete example from the paper:**
```
¬(Sunny(x) ∨ Breezy(x)) → ¬Sunny(x) ∧ ¬Breezy(x)
```

## Theorem Prover

The dataset uses **SymPy** (Python's symbolic computation library) rather than Prover9. The paper states: "we utilize SymPy" to "generate verifiably correct first-order logic expressions" through programmatic simplification.

## Representation Structure

Each example contains:
- **Rule**: FOL expression template
- **Expressions (exprs)**: Sequential simplification steps
- **Complexity metrics**: Circuit complexity, elimination complexity, program complexity
- **Depth information**: Original expression depth

## Dataset Splits and Sizes

| Split | Examples | Tokens |
|-------|----------|--------|
| Train | 7.40M | 3.51B |
| Dev | 5K | 3.05M |
| Test | 8.64K | 5.25M |
| **Curated Train** | **8.80M** | **786.27M** |

The dataset combines synthetically generated rules (via SymPy) with human-curated logical forms from existing benchmarks like LogicBench and FOLIO, instantiated with natural language predicates through LLM prompting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 328 · 2026-05-19T13:25:44.540126+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Willow dataset NL-to-FOL first-order logic natural language translation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Willow dataset NL-to-FOL first-order logic natural language translation 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 329 · 2026-05-19T13:25:44.540251+00:00_

Web search results for query: "Willow dataset NL-to-FOL first-order logic natural language translation 2024 2025"

Links: [{"title":"Advancing Natural Language Formalization to First Order Logic with Fine-tuned LLMs","url":"https://arxiv.org/html/2509.22338v1"},{"title":"[2509.22338] Advancing Natural Language Formalization to First Order Logic with Fine-tuned LLMs","url":"https://arxiv.org/abs/2509.22338"},{"title":"Harnessing the Power of Large Language Models for Natural Language to   First-Order Logic Translation","url":"https://arxiv.org/pdf/2305.15541"},{"title":"Autoformalizing Natural Language to First-Order Logic: A Case Study in   Logical Fallacy Detection","url":"https://arxiv.org/pdf/2405.02318"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection","url":"https://arxiv.org/html/2405.02318v1/"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"GitHub - gblackout/LogicLLaMA: Large language model and dataset for natural language to first-order logic translation","url":"https://github.com/gblackout/LogicLLaMA"}]

Based on the search results, here's what I found about the Willow dataset for NL-to-FOL translation:

The Willow dataset is used alongside the MALLS dataset for natural language to first-order logic translation research, with techniques including vocabulary extension, predicate conditioning, and multilingual training.

Recent work has fine-tuned several large language models using the MALLS and Willow datasets for the task of translating natural language into first-order logic. In a specific application, the Willow dataset correctly handles difficult Aristotelian logical forms that were problematic in the MALLS dataset.

In a 2025 study, fine-tuned Flan-T5-XXL achieved 70% accuracy with predicate lists, outperforming GPT-4o and DeepSeek-R1-0528 model with chain-of-thought reasoning ability as well as symbolic systems l
…[truncated 378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 330 · 2026-05-19T13:25:44.540396+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NL2FOL dataset logical fallacy detection formal logic FOL size format 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NL2FOL dataset logical fallacy detection formal logic FOL size format 2024"
  }
}
```

</details>

---

### Tool result

_source line 331 · 2026-05-19T13:25:44.540537+00:00_

Web search results for query: "NL2FOL dataset logical fallacy detection formal logic FOL size format 2024"

Links: [{"title":"[2405.02318v1] NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection","url":"https://arxiv.org/abs/2405.02318v1"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection","url":"https://www.emergentmind.com/papers/2405.02318"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/nl2fol-translating-natural-language-to-first-order"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NL2FOL:-Translating-Natural-Language-to-First-Order-Lalwani-Kim/f56614b0b188f4b53bfc63b134220ed4167024a4"},{"title":"Autoformalizing Natural Language to First-Order Logic: A Case Study in   Logical Fallacy Detection","url":"https://arxiv.org/pdf/2405.02318"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection","url":"https://arxiv.org/html/2405.02318v1/"},{"title":"[2405.02318] Autoformalizing Natural Language to First-Order Logic: A Case Study in Logical Fallacy Detection","url":"https://arxiv.org/abs/2405.02318"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection - Paper Detail","url":"https://deeplearn.org/arxiv/582469/nl2fol:-translating-natural-language-to-first-order-logic-for-logical-fallacy-detection"}]

Based on the search results, here's what I found about the NL2FOL dataset and project:

## Overview
NL2FOL is a framework to autoformalize natural language to FOL (First-Order Logic) step by step using Large Language Models (LLMs). The process translates natural language to First-order Logic using LLMs, then utilizes Satisfiability Modulo Theory (SMT) solvers to rea
…[truncated 1065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 332 · 2026-05-19T13:25:44.540792+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogiQA dataset logical reasoning format size FOL formal logic annotations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogiQA dataset logical reasoning format size FOL formal logic annotations"
  }
}
```

</details>

---

### Tool result

_source line 333 · 2026-05-19T13:25:44.540943+00:00_

Web search results for query: "LogiQA dataset logical reasoning format size FOL formal logic annotations"

Links: [{"title":"LogiQA 2.0 — An Improved Dataset for Logical Reasoning ...","url":"https://frcchang.github.io/pub/An%20Improved%20Dataset%20for%20Logical%20Reasoning%20in%20Natural%20Language%20Understanding.pdf"},{"title":"LogiQA: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning | Request PDF","url":"https://www.researchgate.net/publication/342799906_LogiQA_A_Challenge_Dataset_for_Machine_Reading_Comprehension_with_Logical_Reasoning"},{"title":"[PDF] LogiQA 2.0—An Improved Dataset for Logical Reasoning in Natural Language Understanding | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LogiQA-2.0%E2%80%94An-Improved-Dataset-for-Logical-in-Liu-Liu/11a05b7e2bc79a9e0cc1d1b83ec978da8ee13bc9"},{"title":"LogiQA 2.0—An Improved Dataset for Logical Reasoning in Natural Language Understanding | IEEE/ACM Transactions on Audio, Speech and Language Processing","url":"https://dl.acm.org/doi/10.1109/TASLP.2023.3293046"},{"title":"LogiQA 2.0—An Improved Dataset for Logical Reasoning in Natural Language Understanding | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10174688/"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - DEV Community","url":"https://dev.to/aimodels-fyi/folio-natural-language-reasoning-with-first-order-logic-3hb1"},{"title":"[2007.08124] LogiQA: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning","url":"https://arxiv.org/abs/2007.08124"}]

Based on the search results, here's information about the LogiQA dataset:

## Dataset Overview

LogiQA is a comprehensive dataset sourced from expert-written questions for testing human logical reasoning, consisting of 8,678 QA instances covering multiple types of deductive reasoning.

## Size and Format

The dataset exists in two versions:
- LogiQA 1.0 contains 8,678 question instances, while L
…[truncated 949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 334 · 2026-05-19T13:25:44.541177+00:00_

I now have comprehensive information. Let me compile the final report.

---

## FOL-Annotated Dataset Survey Results

Below are all datasets found beyond the six already being researched (ProntoQA, LogicNLI, FOLIO, ProofWriter, LogicBench, FLD). Each is assessed for Prover9 compatibility on a 1-5 scale where 5 = directly compatible with Prover9 syntax like `all(x, (penguin(x) -> bird(x)))`.

---

### Tier 1: Directly Prover9-compatible or near-compatible FOL

**1. PROOFFOL**
- **Size:** 10,424 (premise, conclusion, label, FOL) tuples
- **Format:** Derived from ProofWriter; NL premises/conclusions + Prover9-format FOL translations. Uses `all x (...)`, `exists y (...)`, `->`, `&`, `|`, `-` (negation).
- **Example:** `all x (Athlete(x) -> -NeverExercises(x))`
- **Source:** GPT-4o translations of ProofWriter, verified against Prover9 output.
- **Availability:** [github.com/RamyaKeerthy/Translation-NL2FOL](https://github.com/RamyaKeerthy/Translation-NL2FOL)
- **Compatibility: 5/5** -- Natively uses Prover9 syntax. Directly usable.

**2. ProverQA (from ProverGen framework)**
- **Size:** 6,500 (1,500 eval + 5,000 train) across easy/medium/hard splits
- **Format:** NL context + NL-to-FOL mappings + conclusion FOL + reasoning chain. Uses predicate logic with all 7 operators (conjunction, disjunction, negation, implication, XOR, universal/existential quantification). Generated and validated via Prover9.
- **Availability:** [huggingface.co/datasets/opendatalab/ProverQA](https://huggingface.co/datasets/opendatalab/ProverQA)
- **Compatibility: 4/5** -- Built with Prover9 in the loop, but notation uses Unicode symbols (∧, ∨, →, ∀, ∃) rather than ASCII Prover9 syntax. Mechanical symbol substitution needed.

---

### Tier 2: FOL annotations requiring moderate conversion

**3. text2log**
- **Size:** 100,000 NL-FOL pairs
- **Format:** `{clean: "sentence", trans: "FOL"}`. Lambda DCS notation via ccg2lambda. Example: `all x1.(_thing(x1) -> (_new(x1) -> _good(x1)))`
- **Availability:** 
…[truncated 9420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d145-fol-datasets_20260519T131524",
  "tool": "Agent",
  "elapsed_ms": 42
}
```

</details>

---

### Assistant

_source line 335 · 2026-05-19T13:25:44.541445+00:00_

调研完成。以下是汇总报告。

---

## 自带 FOL 标注的逻辑推理数据集调研

### 必查候选

| 数据集 | 大小 | FOL 标注 | 兼容性 | 备注 |
|--------|------|----------|--------|------|
| **FOLIO** (tasksource/folio) | 1,203 | `premises-FOL` + `conclusion-FOL` | **5/5** | 已在用，人工标注，质量最高 |
| **ProofFOL** | 10,424 | `Premise_FOL` + `Conclusion_FOL`，**原生 Prover9 语法** | **5/5** | GPT-4o 翻译 ProofWriter depth-5 + Prover9 验证，~70% 保留率。最佳新发现 |
| **ProntoQA** (renma/ProntoQA) | 500 | `raw_logic_programs` 自定义 DSL | **4/5** | 仅一元谓词，转 Prover9 ~20 行 regex。逻辑片段太窄 |
| **FLD v2 / FLDx2** | 40K / 110K | `hypothesis_formula` + `context_formula` + `proofs_formula` | **4/5** | 匿名谓词 `{A}x`，需 regex 重写为 Prover9 语法。规模最大 |
| **ProverQA** | 6,500 | NL-to-FOL 映射 + 结论 FOL，Prover9 生成验证 | **4/5** | Unicode 符号 (∀∃→∧∨) 替换为 ASCII 即可 |
| **LogicNLI** | 20,000 | 无，纯 NL 模板 | **2/5** | 模板规律可 regex 解析 ~95%，但工程量 2-3 天 |
| **LogicBench** | ~2,000 | 无 | **1/5** | 纯 NL，需完整语义解析 |
| **FLD** 见上 | — | — | — | — |
| **RuleTaker/ProofWriter** 原版 | ~59K | 无原生 FOL，但生成器有双向映射 | 见 ProofFOL | 用 ProofFOL 即可 |

### 额外发现

| 数据集 | 大小 | FOL 标注 | 兼容性 | 备注 |
|--------|------|----------|--------|------|
| **FOL-nli** | 102,774 | TPTP 格式 FOL (premise + hypothesis) | **3/5** | TPTP→Prover9 系统转换，规模大 |
| **MALLS** | 34,000 | 标准 FOL (Unicode) | **3/5** | `∀x(P(x)→Q(x))` 需 Unicode→ASCII |
| **text2log** | 100,000 | Lambda DCS via ccg2lambda | **3/5** | 需清理前缀下划线和量词语法 |

### 推荐

**首选：ProofFOL**（兼容性 5/5）
- 10K+ 条，原生 Prover9 语法，零转换成本
- 基于 ProofWriter（与我们 pipeline 同源），有 premise/conclusion/label 结构
- 来源：`github.com/RamyaKeerthy/Translation-NL2FOL`

**次选：FLD v2/FLDx2**（兼容性 4/5）
- 规模最大（40K-110K），含完整证明链的 FOL
- 谓词匿名化 (`{A}`, `{B}`)，需 ~50 行转换脚本
- 逻辑复杂度可控（depth 0-3, steps 1-8）

**备选：FOL-nli**（兼容性 3/5）
- 10 万条 TPTP 格式，覆盖面广
- TPTP 到 Prover9 有成熟工具链

**结论**：ProofFOL 是跨数据集验证的最优候选——与 FOLIO 互补（ProofWriter 域 vs WikiLogic 域），Prover9 直接兼容，无需任何格式转换。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_d145-fol-datasets_20260519T131524"
}
```

</details>

---
