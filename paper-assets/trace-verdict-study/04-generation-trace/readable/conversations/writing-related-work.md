# writing related work

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_writing_related-work_20260515T094528.jsonl`
- **Structured JSON:** [`646207b98e8986d44d84.json`](../../sessions/64/646207b98e8986d44d84.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-15T09:47:56.796819+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if paper output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260515T094528",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check if paper output directory exists"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T09:47:56.797698+00:00_

DIR_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260515T094528",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T09:47:56.797944+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/",
  "description": "Create paper output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260515T094528",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/",
    "description": "Create paper output directory"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T09:47:56.798580+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260515T094528",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T09:47:56.798965+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/related_work.tex",
  "content": "\\section{Related Work}\n\n\\subsection{Execution Traces for Code LLMs}\n\nExecution traces have been increasingly explored as supplementary signals for code language models, but existing work focuses almost exclusively on generation tasks such as code repair and synthesis.\n\\cite{placeholder_WangEMNLP2025} provide the most comprehensive study to date, showing that execution trace SFT yields limited improvements for code generation across multiple settings---a finding we complement by demonstrating that traces become highly effective when the downstream task shifts from generation to classification.\n\\cite{placeholder_NiICML2024} use self-training on execution traces as chain-of-thought rationales, improving MBPP fix rates by 26.1\\%, while \\cite{placeholder_JungEMNLP2025} extract step-by-step traces via the Python debugger Snoop to construct CoT supervision.\nBoth treat traces as intermediate reasoning scaffolds for producing code, leaving the question of trace utility for binary judgments entirely unexamined.\n\nA parallel line of work investigates what trace content to retain.\n\\cite{placeholder_FerrandoArXiv2025} show that compact scratchpads recording only changed values match or exceed full-state scratchpads, providing early evidence that value-level information is largely redundant.\n\\cite{placeholder_DemystifyingArXiv2025} corroborate this from the model capability side, finding that LLMs are substantially weaker at value tracking than at structural understanding.\nTraceCoder \\cite{placeholder_TraceCoderICSE2026} demonstrates that selective variable probing outperforms full traces by 34.43\\% on Pass@1, and TraceRepair \\cite{placeholder_TraceRepairArXiv2026} uses critical variable snapshots to repair 392 defects.\nND-Slicer \\cite{placeholder_YadavallyFSE2024} proposes execution-aware pretraining to learn dynamic dependencies, and \\cite{placeholder_PredSlicingFSE2024} introduces assertion-point slicing conceptually close to our snapshot design.\n\\cite{placeholder_HaqueACL2025} observe that trace benefits diminish as program complexity increases, while ET-CoT \\cite{placeholder_ETCoTICML2025} pushes granularity to the sub-line level on CRUXEval.\n\nThese compression strategies all optimize traces for generation fluency.\nOur work departs from this paradigm: for a classification objective with $O(1)$ output entropy, the optimal representation is not a compressed execution narrative but a decision-relevant event summary---a principle that yields 99.2\\% verdict accuracy where full traces reach only 81.8\\%.\n\n\\subsection{Fine-Tuning LLMs for Classification}\n\nAdapting generative LLMs to classification raises distinct design questions around input representation and training objective.\n\\cite{placeholder_YousefiArXiv2025} compare embedding-based and instruction-based SFT for text classification, finding task-dependent trade-offs between the two paradigms.\nFisherSFT \\cite{placeholder_FisherSFTICML2025} leverages Fisher information to select maximally informative training subsets, improving sample efficiency for classification fine-tuning.\n\\cite{placeholder_BucherArXiv2024} show that fine-tuned small models consistently outperform zero-shot GPT-4 on classification benchmarks, reinforcing that SFT remains the dominant approach for binary prediction tasks.\n\nNone of these studies consider structured program execution data as input, nor do they examine how input granularity interacts with classification accuracy.\nOur work bridges this gap by treating the trace format itself as a first-class design variable: when the task is binary verdict prediction, the choice of trace abstraction has a larger effect on accuracy (+24.1 points) than the choice of whether to include traces at all (+6.7 points).\n\n\\subsection{Code Correctness Prediction}\n\nPredicting whether code is correct constitutes the task most directly related to ours, yet prior approaches rely on static representations.\nAPPT \\cite{placeholder_APPTTSE2024} combines BERT embeddings with LSTM sequence modeling for automated patch correctness classification, reaching 79.7\\% accuracy---the closest prior baseline to our verdict task setting.\n\\cite{placeholder_SpiessICSE2025} show that code generation models are poorly calibrated when repurposed for correctness judgments, motivating dedicated classification architectures over repurposed generators.\nAt industry scale, \\cite{placeholder_FosterFSE2025} build a mutation equivalence detector at Meta achieving 0.95 precision, demonstrating that binary code judgments can reach high reliability through domain-specific design.\n\nNo prior code correctness predictor incorporates execution traces as input.\nVOTA closes this gap by pairing trace abstraction with verdict-specific compression: reducing full execution traces to exception-type events raises accuracy from 75.1\\% (no trace) past 81.8\\% (full trace) to 99.2\\%, with the exception-only variant reaching 99.83\\%---indicating that for pass/fail judgments, knowing \\emph{what went wrong} matters far more than knowing \\emph{what happened}.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260515T094528",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/related_work.tex",
    "content": "\\section{Related Work}\n\n\\subsection{Execution Traces for Code LLMs}\n\nExecution traces have been increasingly explored as supplementary signals for code language models, but existing work focuses almost exclusively on generation tasks such as code repair and synthesis.\n\\cite{placeholder_WangEMNLP2025} provide the most comprehensive study to date, showing that execution trace SFT yields limited improvements for code generation across multiple settings---a finding we complement by demonstrating that traces become highly effective when the downstream task shifts from generation to classification.\n\\cite{placeholder_NiICML2024} use self-training on execution traces as chain-of-thought rationales, improving MBPP fix rates by 26.1\\%, while \\cite{placeholder_JungEMNLP2025} extract step-by-step traces via the Python debugger Snoop to construct CoT supervision.\nBoth treat traces as intermediate reasoning scaffolds for producing code, leaving the question of trace utility for binary judgments entirely unexamined.\n\nA parallel line of work investigates what trace content to retain.\n\\cite{placeholder_FerrandoArXiv2025} show that compact scratchpads recording only changed values match or exceed full-state scratchpads, providing early evidence that value-level information is largely redundant.\n\\cite{placeholder_DemystifyingArXiv2025} corroborate this from the model capability side, finding that LLMs are substantially weaker at value tracking than at structural understanding.\nTraceCoder \\cite{placeholder_TraceCoderICSE2026} demonstrates that selective variable probing outperforms full traces by 34.43\\% on Pass@1, and TraceRepair \\cite{placeholder_TraceRepairArXiv2026} uses critical variable snapshots to repair 392 defects.\nND-Slicer \\cite{placeholder_YadavallyFSE2024} proposes execution-aware pretraining to learn dynamic dependencies, and \\cite{placeholder_PredSlicingFSE2024} introduces assertion-point slicing conceptually close to our snapshot design.\n\\cite{placeholder_HaqueACL2025} observe that trace benefits diminish as program complexity increases, while ET-CoT \\cite{placeholder_ETCoTICML2025} pushes granularity to the sub-line level on CRUXEval.\n\nThese compression strategies all optimize traces for generation fluency.\nOur work departs from this paradigm: for a classification objective with $O(1)$ output entropy, the optimal representation is not a compressed execution narrative but a decision-relevant event summary---a principle that yields 99.2\\% verdict accuracy where full traces reach only 81.8\\%.\n\n\\subsection{Fine-Tuning LLMs for Classification}\n\nAdapting generative LLMs to classification raises distinct design questions around input representation and training objective.\n\\cite{placeholder_YousefiArXiv2025} compare embedding-based and instruction-based SFT for text classification, finding task-dependent trade-offs between the two paradigms.\nFisherSFT \\cite{placeholder_FisherSFTICML2025} leverages Fisher information to select maximally informative training subsets, improving sample efficiency for classification fine-tuning.\n\\cite{placeholder_BucherArXiv2024} show that fine-tuned small models consistently outperform zero-shot GPT-4 on classification benchmarks, reinforcing that SFT remains the dominant approach for binary prediction tasks.\n\nNone of these studies consider structured program execution data as input, nor do they examine how input granularity interacts with classification accuracy.\nOur work bridges this gap by treating the trace format itself as a first-class design variable: when the task is binary verdict prediction, the choice of trace abstraction has a larger effect on accuracy (+24.1 points) than the choice of whether to include traces at all (+6.7 points).\n\n\\subsection{Code Correctness Prediction}\n\nPredicting whether code is correct constitutes the task most directly related to ours, yet prior approaches rely on static representations.\nAPPT \\cite{placeholder_APPTTSE2024} combines BERT embeddings with LSTM sequence modeling for automated patch correctness classification, reaching 79.7\\% accuracy---the closest prior baseline to our verdict task setting.\n\\cite{placeholder_SpiessICSE2025} show that code generation models are poorly calibrated when repurposed for correctness judgments, motivating dedicated classification architectures over repurposed generators.\nAt industry scale, \\cite{placeholder_FosterFSE2025} build a mutation equivalence detector at Meta achieving 0.95 precision, demonstrating that binary code judgments can reach high reliability through domain-specific design.\n\nNo prior code correctness predictor incorporates execution traces as input.\nVOTA closes this gap by pairing trace abstraction with verdict-specific compression: reducing full execution traces to exception-type events raises accuracy from 75.1\\% (no trace) past 81.8\\% (full trace) to 99.2\\%, with the exception-only variant reaching 99.83\\%---indicating that for pass/fail judgments, knowing \\emph{what went wrong} matters far more than knowing \\emph{what happened}.\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T09:47:56.799303+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260515T094528",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T09:47:56.799637+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/related_work.tex",
  "description": "Count words in related work draft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260515T094528",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/related_work.tex",
    "description": "Count words in related work draft"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T09:47:56.800314+00:00_

598 /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260515T094528",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-15T09:47:56.800998+00:00_

草稿已写入。

```json
{
  "section": "Related Work",
  "word_count": 598,
  "subsections": [
    "Execution Traces for Code LLMs (11 papers)",
    "Fine-Tuning LLMs for Classification (3 papers)",
    "Code Correctness Prediction (3 papers)"
  ],
  "citations_needed": [
    "placeholder_WangEMNLP2025 → Wang et al. EMNLP Findings 2025 (DCSH)",
    "placeholder_NiICML2024 → Ni et al. ICML 2024 (NExT)",
    "placeholder_JungEMNLP2025 → Jung et al. EMNLP 2025 (Snoop trace)",
    "placeholder_FerrandoArXiv2025 → Ferrando et al. arXiv 2503.05703",
    "placeholder_DemystifyingArXiv2025 → arXiv 2512.00215",
    "placeholder_TraceCoderICSE2026 → TraceCoder ICSE 2026",
    "placeholder_TraceRepairArXiv2026 → TraceRepair arXiv 2604.02647",
    "placeholder_YadavallyFSE2024 → ND-Slicer FSE 2024",
    "placeholder_PredSlicingFSE2024 → Predictive Program Slicing FSE 2024",
    "placeholder_HaqueACL2025 → Haque et al. KnowledgeNLP@ACL 2025",
    "placeholder_ETCoTICML2025 → ET-CoT ICML 2025 Workshop",
    "placeholder_YousefiArXiv2025 → Yousefiramandi & Cooney arXiv 2512.12677",
    "placeholder_FisherSFTICML2025 → FisherSFT ICML 2025",
    "placeholder_BucherArXiv2024 → Bucher & Martini arXiv 2406.08660",
    "placeholder_APPTTSE2024 → APPT TSE 2024",
    "placeholder_SpiessICSE2025 → Spiess et al. ICSE 2025",
    "placeholder_FosterFSE2025 → Foster et al. FSE 2025 Industry"
  ],
  "notes": [
    "17 citations all from provided literature map, no fabricated references",
    "Structure: traces (distant) → classification SFT (middle) → code correctness (closest)",
    "Each subsection ends with explicit contrast to VOTA",
    "~598 words ≈ 0.8 EMNLP pages, within 1-1.5 page budget",
    "All placeholder cite keys need replacement with actual bib entries"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_related-work_20260515T094528"
}
```

</details>

---
