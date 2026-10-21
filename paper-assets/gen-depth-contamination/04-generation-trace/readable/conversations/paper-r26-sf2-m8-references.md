# paper r26 sf2 m8 references

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_paper_r26_sf2_m8_references_20260522T082246.jsonl`
- **Structured JSON:** [`36cf69776667a4f34dff.json`](../../sessions/36/36cf69776667a4f34dff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-22T08:27:16.766139+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T08:27:16.766587+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T08:27:16.766808+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2603.11228 Geng Markovian Generation Chains Large Language Models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2603.11228 Geng Markovian Generation Chains Large Language Models"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T08:27:16.766972+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2512.05311 Shahriar Erosion LLM Signatures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2512.05311 Shahriar Erosion LLM Signatures"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T08:27:16.767104+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T08:27:16.767240+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/related_work.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/related_work.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T08:27:16.767390+00:00_

Web search results for query: "arXiv 2603.11228 Geng Markovian Generation Chains Large Language Models"

Links: [{"title":"[2603.11228] Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/abs/2603.11228"},{"title":"Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/html/2603.11228"},{"title":"Markovian Generation Chains in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nTDn4OMiym"},{"title":"Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/pdf/2603.11228"},{"title":"[2410.02724v1] Large Language Models as Markov Chains","url":"https://arxiv.org/abs/2410.02724v1"},{"title":"[2410.02724] Large Language Models as Markov Chains","url":"https://arxiv.org/abs/2410.02724"}]

I found the paper! Here are the key details about arXiv paper 2603.11228:

**Title:** Markovian Generation Chains in Large Language Models

**Authors:** Mingmeng Geng, Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, and Thierry Poibeau

**Main Contribution:** The paper addresses the question of how texts evolve when they are repeatedly processed by LLMs, defining this iterative inference process as Markovian generation chains, where each step takes a specific prompt template and the previous output as input, without including any prior memory.

**Key Findings:** In iterative rephrasing and round-trip translation experiments, the output either converges to a small recurrent set or continues to produce novel sentences over a finite horizon. Additionally, the iterative process can either increase or reduce sentence diversity depending on factors such as the temperature parameter and the initial input sentence.

**Publication Date:** March 11, 2026

The paper was posted to arXiv and is also available through OpenReview, offering insights into the dynamics of iterative LLM inference systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T08:27:16.767551+00:00_

Web search results for query: "arXiv 2512.05311 Shahriar Erosion LLM Signatures"

Links: [{"title":"[2512.05311] The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?","url":"https://arxiv.org/abs/2512.05311"},{"title":"The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?","url":"https://arxiv.org/html/2512.05311"},{"title":"The Erosion of LLM Signatures: Can We Still Distinguish Human and","url":"https://www.arxiv.org/pdf/2512.05311"},{"title":"Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure","url":"https://arxiv.org/pdf/2601.10566"},{"title":"Beyond Next Token Probabilities: Learnable, Fast Detection of Hallucinations and Data Contamination on LLM Output Distributions","url":"https://arxiv.org/pdf/2503.14043"},{"title":"The Statistical Signature of LLMs","url":"https://arxiv.org/pdf/2602.18152"},{"title":"[2512.05331] Exposing Pink Slime Journalism: Linguistic Signatures and Robust Detection Against LLM-Generated Threats","url":"https://arxiv.org/abs/2512.05331"}]

I found the paper for you. Here's what I found:

arXiv 2512.05311 is titled "The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?" by Sadat Shahriar and 2 other authors.

**Key findings:**

- The paper addresses distinguishing human vs LLM-generated scientific ideas, which remains an unexplored area.

- The researchers systematically evaluate state-of-the-art machine learning models to differentiate between human and LLM-generated ideas, particularly after successive paraphrasing stages.

- Detection performance declined by an average of 25.4% after five consecutive paraphrasing stages.

- Incorporating the research problem as contextual information improved detection performance by up to 2.97%.

The paper was submitted on Decem
…[truncated 179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T08:27:16.767834+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"% === References for gen-depth-contamination ===\\n% Source: literature_map.yaml — verified 2026-05-15\\n\\n% === Must-Cite ===\\n\\n@inproceedings{drayson2025,\\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\\n  booktitle={Proceedings of EMNLP},\\n  year={2025},\\n  url={https://arxiv.org/abs/2502.15654}\\n}\\n\\n@inproceedings{schaeffer2025position,\\n  title={Position: Model Collapse Does Not Mean What You Think},\\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\\n  booktitle={Proceedings of ICML},\\n  year={2025},\\n  url={https://arxiv.org/abs/2503.03150}\\n}\\n\\n@inproceedings{kazdan2025collapse,\\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\\n  booktitle={Proceedings of ICML},\\n  year={2025},\\n  url={https://arxiv.org/abs/2410.16713}\\n}\\n\\n@inproceedings{mitchell2023detectgpt,\\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\\n  booktitle={Proceedings of ICML},\\n  year={2023},\\n  url={https://arxiv.org/abs/2301.11305}\\n}\\n\\n% === Should-Cite ===\\n\\n@article{basani2026diveye,\\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\\n  author={Basani, Advik Raj and Chen, Pin-Yu},\\n  journal={Transactions on Machine Learning Research},\\n  issn={2835-8856},\\n  year={2026},\\n  url={https://arxiv.org/abs/2509.18880}\\n}\\n\\n@inproceedings{zawalski2026codec,\\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\\n  author={Zawalski, Micha{\\\\l} and 
…[truncated 6612 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T08:27:16.768048+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Related Work}\\n\\\\label{sec:related_work}\\n\\n\\\\paragraph{Model collapse and recursive degradation.}\\nIterative training on model outputs causes tail-distribution degradation~\\\\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong, fu2025theoretical}, diversity contraction~\\\\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\\\\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, wang2025unveiling}.\\nSuresh et al.~\\\\cite{suresh2024rate} derive precise collapse rates for discrete distributions under recursive MLE training, complementing the theoretical conditions established by Fu et al.~\\\\cite{fu2025theoretical}.\\nOur prompt-chain operates in the replace regime~\\\\cite{kazdan2025collapse}, making $\\\\Kempirical = 2$ a conservative lower bound.\\nThis literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.\\n\\n\\\\paragraph{Beyond binary detection.}\\nBinary detectors~\\\\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.\\nRecent work extends beyond binary labels to collaboration degree~\\\\cite{cheng2025beyond}, contamination hierarchies~\\\\cite{mehta2025beyond}, and multigenerator benchmarks~\\\\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\\\\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\\\\cite{hao2025rewrite}; CoDeC~\\\\cite{zawalski2026codec} addresses contamination via membership inference.\\nNone estimates recursive generation depth.\\n\\n\\\\paragraph{Data selection and curation.}\\nDSIR~\\\\cite{xie2023dsir}, D4~\\\\cite{tirumala2023d4}, and DoReMi~\\\\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\\\\cite{drayson2025} combined binary det
…[truncated 450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T08:27:16.768255+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2512.05311 \"The Erosion of LLM Signatures\" full author list Shahriar"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2512.05311 \"The Erosion of LLM Signatures\" full author list Shahriar"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T08:27:16.768392+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"doremi\\|bao2024\\|hans2024\\|cheng2025\\|mehta2025\\|alain2017\\|belinkov\\|frank2001\\|dohmatob2025\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -n \"doremi\\|bao2024\\|hans2024\\|cheng2025\\|mehta2025\\|alain2017\\|belinkov\\|frank2001\\|dohmatob2025\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T08:27:16.768535+00:00_

Web search results for query: "arxiv 2512.05311 "The Erosion of LLM Signatures" full author list Shahriar"

Links: [{"title":"[2512.05311] The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?","url":"https://arxiv.org/abs/2512.05311"},{"title":"The Erosion of LLM Signatures: Can We Still Distinguish Human and","url":"https://www.arxiv.org/pdf/2512.05311"},{"title":"The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?","url":"https://arxiv.org/html/2512.05311v1"},{"title":"Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure","url":"https://arxiv.org/pdf/2601.10566"},{"title":"[2512.05331] Exposing Pink Slime Journalism: Linguistic Signatures and Robust Detection Against LLM-Generated Threats","url":"https://arxiv.org/abs/2512.05331"},{"title":"The Statistical Signature of LLMs","url":"https://arxiv.org/pdf/2602.18152"},{"title":"Exposing Pink Slime Journalism: Linguistic Signatures and Robust Detection Against LLM-Generated Threats","url":"https://arxiv.org/html/2512.05331"}]

Based on the search results, the full author list for arxiv paper 2512.05311 "The Erosion of LLM Signatures" is: Sadat Shahriar, Navid Ayoobi, and Arjun Mukherjee.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T08:27:16.768685+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T08:27:16.768847+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n -E \"doremi|bao2024|hans2024|cheng2025|mehta2025|alain2017|belinkov|frank2001|dohmatob2025\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -n -E \"doremi|bao2024|hans2024|cheng2025|mehta2025|alain2017|belinkov|frank2001|dohmatob2025\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T08:27:16.768978+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T08:27:16.769112+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "wc -l /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "wc -l /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T08:27:16.769235+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"296 /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T08:27:16.769353+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -180 /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -180 /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T08:27:16.769537+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\\n  booktitle={Proceedings of ICML},\\n  year={2024},\\n  url={https://arxiv.org/abs/2401.12070}\\n}\\n\\n% === Probing Classifiers ===\\n\\n@inproceedings{alain2017understanding,\\n  title={Understanding Intermediate Layers Using Linear Classifier Probes},\\n  author={Alain, Guillaume and Bengio, Yoshua},\\n  booktitle={ICLR Workshop},\\n  year={2017},\\n  url={https://arxiv.org/abs/1610.01644}\\n}\\n\\n@article{belinkov2022probing,\\n  title={Probing Classifiers: Promises, Shortcomings, and Advances},\\n  author={Belinkov, Yonatan},\\n  journal={Computational Linguistics},\\n  volume={48},\\n  number={1},\\n  pages={207--219},\\n  year={2022},\\n  url={https://doi.org/10.1162/coli_a_00422}\\n}\\n\\n% === Model Collapse Avoidability ===\\n\\n@inproceedings{bao2024fast,\\n  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},\\n  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\\n  booktitle={Proceedings of ICLR},\\n  year={2024},\\n  url={https://arxiv.org/abs/2310.05130}\\n}\\n\\n@inproceedings{frank2001ordinal,\\n  title={A Simple Approach to Ordinal Classification},\\n  author={Frank, Eibe and Hall, Mark},\\n  booktitle={Proceedings of ECML},\\n  pages={145--156},\\n  year={2001},\\n  url={https://doi.org/10.1007/3-540-44795-4_13}\\n}\\n\\n% === Beyond-Binary Detection ===\\n\\n@inproceedings{cheng2025beyond,\\n  title={Beyond Binary: Towards Fine-Grained {LLM}-Generated Text Detection via Role Recognition and Involvement Measurement},\\n  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\\n  booktitle={Proceedings of the ACM Web Conference (WWW)},\\n  year={2025},\\n  url={https://arxiv.org/ab
…[truncated 5498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T08:27:16.769732+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -140 /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -140 /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T08:27:16.769970+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"% === References for gen-depth-contamination ===\\n% Source: literature_map.yaml — verified 2026-05-15\\n\\n% === Must-Cite ===\\n\\n@inproceedings{drayson2025,\\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\\n  booktitle={Proceedings of EMNLP},\\n  year={2025},\\n  url={https://arxiv.org/abs/2502.15654}\\n}\\n\\n@inproceedings{schaeffer2025position,\\n  title={Position: Model Collapse Does Not Mean What You Think},\\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\\n  booktitle={Proceedings of ICML},\\n  year={2025},\\n  url={https://arxiv.org/abs/2503.03150}\\n}\\n\\n@inproceedings{kazdan2025collapse,\\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\\n  booktitle={Proceedings of ICML},\\n  year={2025},\\n  url={https://arxiv.org/abs/2410.16713}\\n}\\n\\n@inproceedings{mitchell2023detectgpt,\\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\\n  booktitle={Proceedings of ICML},\\n  year={2023},\\n  url={https://arxiv.org/abs/2301.11305}\\n}\\n\\n% === Should-Cite ===\\n\\n@article{basani2026diveye,\\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\\n  author={Basani, Advik Raj and Chen, Pin-Yu},\\n  journal={Transactions on Machine Learning Research},\\n  issn={2835-8856},\\n  year={2026},\\n  url={https://arxiv.org/abs/2509.18880}\\n}\\n\\n@inproceedings{zawalski2026codec,\\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\\n  author={Zawalski, Micha{\\\\l} and 
…[truncated 3649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T08:27:16.770177+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" published venue ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" published venue ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T08:27:16.770312+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Briesch \"Large Language Models Suffer From Their Own Output\" published venue 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Briesch \"Large Language Models Suffer From Their Own Output\" published venue 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T08:27:16.770453+00:00_

Web search results for query: "Briesch "Large Language Models Suffer From Their Own Output" published venue 2024 2025"

Links: [{"title":"[2311.16822v2] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822v2"},{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822"},{"title":"[PDF] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Suffer-From-Their-Own-Output:-Briesch-Sobania/c24ed03689adc2a075004c6619f43f7f6230fe4b"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the   Self-Consuming Training Loop","url":"https://arxiv.org/pdf/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | OpenReview","url":"https://openreview.net/forum?id=SaOxhcDCM3"}]

Based on the search results, I found the paper you're looking for:

The paper "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop" is authored by Martin Briesch, Dominik Sobania, and Franz Rothlauf from Johannes Gutenberg University, Mainz, Germany.

**Publishing Venue and Timeline:**
The paper was originally posted on arXiv in 2023 (with identifier 2311.16822). It investigates how Large Language Models are used to generate content for online platforms, and how LLM-generated content is then used to train the next generation of LLMs, creating a self-consuming training loop. The paper also appears on OpenReview with a timestamp of October 4, 2024, indicating it was under review or accepted at a conference around that time.

**Key Findings:**
The study finds that the self-consuming training loop produces correct outputs, but the output declines in its d
…[truncated 223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T08:27:16.770615+00:00_

Web search results for query: "Sadasivan "Can AI-Generated Text be Reliably Detected" published venue ICLR 2024"

Links: [{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2024"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"[2303.11156v3] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v3"},{"title":"[2303.11156v4] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v4"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"}]

Based on the search results, here's what I found about this paper:

The paper "Can AI-Generated Text be Reliably Detected?" was authored by Sadasivan, V. S., Kumar, A., Balasubramanian, S., Wang, W., & Feizi, S. in February 2024.

The paper appears on the OpenReview platform, which is the standard submission venue for ICLR. The paper shows that AI text detectors are not reliable in practical scenarios, and develops a recursive paraphrasing attack that can break a whole range of detectors, including watermarking schemes as well as neural network-based detectors, zero-shot classifiers, and retrieval-based detectors.

The paper provides a theoretical connection between the AUROC of the best possible detector and the Total Variation distance between human and AI text distributions that can be used to study the fundamental hardness
…[truncated 167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T08:27:16.770860+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T08:27:16.771008+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T08:27:16.771191+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat > /tmp/edit_refs.py << 'PYEOF'\n# 1. Update references.bib\nbib_path = '/root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib'\nwith open(bib_path, 'r') as f:\n    bib = f.read()\n\n# Add url to suresh2024rate (missing url field)\nold_suresh = '  journal={arXiv preprint arXiv:2412.17646},\\n  year={2024}\\n}'\nnew_suresh = '  journal={arXiv preprint arXiv:2412.17646},\\n  year={2024},\\n  url={https://arxiv.org/abs/2412.17646}\\n}'\nbib = bib.replace(old_suresh, new_suresh)\n\n# Append new entries\nnew_entries = \"\"\"\n% === New entries (added 2026-05-22, SF-2) ===\n\n@article{geng2026markovian,\n  title={Markovian Generation Chains in Large Language Models},\n  author={Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},\n  journal={arXiv preprint arXiv:2603.11228},\n  year={2026},\n  url={https://arxiv.org/abs/2603.11228}\n}\n\n@article{shahriar2025erosion,\n  title={The Erosion of {LLM} Signatures: Can We Still Distinguish Human and {LLM}-Generated Scientific Ideas After Iterative Paraphrasing?},\n  author={Shahriar, Sadat and Ayoobi, Navid and Mukherjee, Arjun},\n  journal={arXiv preprint arXiv:2512.05311},\n  year={2025},\n  url={https://arxiv.org/abs/2512.05311}\n}\n\"\"\"\nbib = bib.rstrip() + '\\n' + new_entries\nwith open(bib_path, 'w') as f:\n    f.write(bib)\nprint(\"references.bib: OK\")\n\n# 2. Update related_work.tex\nrw_path = '/root/autodl-tmp/gen-depth-contamination/docs/paper/related_work.tex'\nwith open(rw_path, 'r') as f:\n    rw = f.read()\n\n# Insert Geng after wang2025unveiling}.\nold1 = 'wang2025unveiling}.\\nSuresh et al.'\nnew1 = ('wang2025unveiling}.\\n'\n        'Geng et al.~\\\\cite{geng2026markovian} study the Markov chain convergence behavior of successive generation; '\n        'our work complements this by quantifying the empirical discrimination boundary.\\n'\n        'Suresh et al.')\nassert old1 in rw, f\"Pattern 1 not found in related_work.tex\"\nrw = rw.replace(old1, new1)\n\n# Insert Shahriar in beyond binary paragraph\nold2 = ('and cross-mode transfer~\\\\cite{hao2025rewrite}; '\n        'CoDeC~\\\\cite{zawalski2026codec} addresses contamination via membership inference.\\n'\n        'None estimates recursive generation depth.')\nnew2 = ('and cross-mode transfer~\\\\cite{hao2025rewrite}; '\n        'Shahriar et al.~\\\\cite{shahriar2025erosion} measure detection accuracy erosion '\n        '(${\\\\sim}25.4\\\\%$) across generation depths; '\n        'CoDeC~\\\\cite{zawalski2026codec} addresses contamination via membership inference.\\n'\n        'None estimates recursive generation depth; '\n        'we instead characterize the precise depth at which discrimination becomes impossible.')\nassert old2 in rw, f\"Pattern 2 not found in related_work.tex\"\nrw = rw.replace(old2, new2)\n\nwith open(rw_path, 'w') as f:\n    f.write(rw)\nprint(\"related_work.tex: OK\")\nPYEOF\npython3 /tmp/edit_refs.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat > /tmp/edit_refs.py << 'PYEOF'\n# 1. Update references.bib\nbib_path = '/root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib'\nwith open(bib_path, 'r') as f:\n    bib = f.read()\n\n# Add url to suresh2024rate (missing url field)\nold_suresh = '  journal={arXiv preprint arXiv:2412.17646},\\n  year={2024}\\n}'\nnew_suresh = '  journal={arXiv preprint arXiv:2412.17646},\\n  year={2024},\\n  url={https://arxiv.org/abs/2412.17646}\\n}'\nbib = bib.replace(old_suresh, new_suresh)\n\n# Append new entries\nnew_entries = \"\"\"\n% === New entries (added 2026-05-22, SF-2) ===\n\n@article{geng2026markovian,\n  title={Markovian Generation Chains in Large Language Models},\n  author={Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},\n  journal={arXiv preprint arXiv:2603.11228},\n  year={2026},\n  url={https://arxiv.org/abs/2603.11228}\n}\n\n@article{shahriar2025erosion,\n  title={The Erosion of {LLM} Signatures: Can We Still Distinguish Human and {LLM}-Generated Scientific Ideas After Iterative Paraphrasing?},\n  author={Shahriar, Sadat and Ayoobi, Navid and Mukherjee, Arjun},\n  journal={arXiv preprint arXiv:2512.05311},\n  year={2025},\n  url={https://arxiv.org/abs/2512.05311}\n}\n\"\"\"\nbib = bib.rstrip() + '\\n' + new_entries\nwith open(bib_path, 'w') as f:\n    f.write(bib)\nprint(\"references.bib: OK\")\n\n# 2. Update related_work.tex\nrw_path = '/root/autodl-tmp/gen-depth-contamination/docs/paper/related_work.tex'\nwith open(rw_path, 'r') as f:\n    rw = f.read()\n\n# Insert Geng after wang2025unveiling}.\nold1 = 'wang2025unveiling}.\\nSuresh et al.'\nnew1 = ('wang2025unveiling}.\\n'\n        'Geng et al.~\\\\cite{geng2026markovian} study the Markov chain convergence behavior of successive generation; '\n        'our work complements this by quantifying the empirical discrimination boundary.\\n'\n        'Suresh et al.')\nassert old1 in rw, f\"Pattern 1 not found in related_work.tex\"\nrw = rw.replace(old1, new1)\n\n# Insert Shahriar in beyond binary paragraph\nold2 = ('and cross-mode transfer~\\\\cite{hao2025rewrite}; '\n        'CoDeC~\\\\cite{zawalski2026codec} addresses contamination via membership inference.\\n'\n        'None estimates recursive generation depth.')\nnew2 = ('and cross-mode transfer~\\\\cite{hao2025rewrite}; '\n        'Shahriar et al.~\\\\cite{shahriar2025erosion} measure detection accuracy erosion '\n        '(${\\\\sim}25.4\\\\%$) across generation depths; '\n        'CoDeC~\\\\cite{zawalski2026codec} addresses contamination via membership inference.\\n'\n        'None estimates recursive generation depth; '\n        'we instead characterize the precise depth at which discrimination becomes impossible.')\nassert old2 in rw, f\"Pattern 2 not found in related_work.tex\"\nrw = rw.replace(old2, new2)\n\nwith open(rw_path, 'w') as f:\n    f.write(rw)\nprint(\"related_work.tex: OK\")\nPYEOF\npython3 /tmp/edit_refs.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T08:27:16.771352+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"references.bib: OK\\nrelated_work.tex: OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T08:27:16.771507+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/related_work.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/related_work.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T08:27:16.771666+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Related Work}\\n\\\\label{sec:related_work}\\n\\n\\\\paragraph{Model collapse and recursive degradation.}\\nIterative training on model outputs causes tail-distribution degradation~\\\\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong, fu2025theoretical}, diversity contraction~\\\\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\\\\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, wang2025unveiling}.\\nGeng et al.~\\\\cite{geng2026markovian} study the Markov chain convergence behavior of successive generation; our work complements this by quantifying the empirical discrimination boundary.\\nSuresh et al.~\\\\cite{suresh2024rate} derive precise collapse rates for discrete distributions under recursive MLE training, complementing the theoretical conditions established by Fu et al.~\\\\cite{fu2025theoretical}.\\nOur prompt-chain operates in the replace regime~\\\\cite{kazdan2025collapse}, making $\\\\Kempirical = 2$ a conservative lower bound.\\nThis literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.\\n\\n\\\\paragraph{Beyond binary detection.}\\nBinary detectors~\\\\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.\\nRecent work extends beyond binary labels to collaboration degree~\\\\cite{cheng2025beyond}, contamination hierarchies~\\\\cite{mehta2025beyond}, and multigenerator benchmarks~\\\\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\\\\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\\\\cite{hao2025rewrite}; Shahriar et al.~\\\\cite{shahriar2025erosion} measure detection accuracy erosion (${\\\\sim}25.4\\\\%$) across generation depths; CoDeC~\\\\cite{zawalski202
…[truncated 858 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T08:27:16.771841+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -30 /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -30 /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T08:27:16.771989+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  author={Fu, Shi and Wang, Yingjie and Chen, Yuzhu and Tian, Xinmei and Tao, Dacheng},\\n  booktitle={Proceedings of the 13th International Conference on Learning Representations},\\n  year={2025}\\n}\\n\\n@article{suresh2024rate,\\n  title={Rate of Model Collapse in Recursive Training},\\n  author={Suresh, Ananda Theertha and Thangaraj, Andrew and Khandavally, Aditya Nanda Kishore},\\n  journal={arXiv preprint arXiv:2412.17646},\\n  year={2024},\\n  url={https://arxiv.org/abs/2412.17646}\\n}\\n\\n% === New entries (added 2026-05-22, SF-2) ===\\n\\n@article{geng2026markovian,\\n  title={Markovian Generation Chains in Large Language Models},\\n  author={Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},\\n  journal={arXiv preprint arXiv:2603.11228},\\n  year={2026},\\n  url={https://arxiv.org/abs/2603.11228}\\n}\\n\\n@article{shahriar2025erosion,\\n  title={The Erosion of {LLM} Signatures: Can We Still Distinguish Human and {LLM}-Generated Scientific Ideas After Iterative Paraphrasing?},\\n  author={Shahriar, Sadat and Ayoobi, Navid and Mukherjee, Arjun},\\n  journal={arXiv preprint arXiv:2512.05311},\\n  year={2025},\\n  url={https://arxiv.org/abs/2512.05311}\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-22T08:27:16.772170+00:00_

全部修改已完成，验证通过。

---

## SF-2 结果

**references.bib** 追加两条：

```bibtex
@article{geng2026markovian,
  title={Markovian Generation Chains in Large Language Models},
  author={Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
  journal={arXiv preprint arXiv:2603.11228},
  year={2026},
  url={https://arxiv.org/abs/2603.11228}
}

@article{shahriar2025erosion,
  title={The Erosion of {LLM} Signatures: Can We Still Distinguish Human and {LLM}-Generated Scientific Ideas After Iterative Paraphrasing?},
  author={Shahriar, Sadat and Ayoobi, Navid and Mukherjee, Arjun},
  journal={arXiv preprint arXiv:2512.05311},
  year={2025},
  url={https://arxiv.org/abs/2512.05311}
}
```

**related_work.tex** 插入位置：

1. **Geng** → `\paragraph{Model collapse and recursive degradation.}` 段，`wang2025unveiling}.` 之后、`Suresh et al.` 之前：
   > Geng et al.~\cite{geng2026markovian} study the Markov chain convergence behavior of successive generation; our work complements this by quantifying the empirical discrimination boundary.

2. **Shahriar** → `\paragraph{Beyond binary detection.}` 段，`cross-mode transfer` 之后、`CoDeC` 之前，作为分号链的一环：
   > ...Shahriar et al.~\cite{shahriar2025erosion} measure detection accuracy erosion (${\sim}25.4\%$) across generation depths; CoDeC...
   
   末句扩展为：
   > None estimates recursive generation depth; we instead characterize the precise depth at which discrimination becomes impossible.

---

## m8 结果

**Preprint 格式审计**（5 条 `@article` 含 arXiv）：

| 条目 | 格式 | 状态 |
|------|------|------|
| `briesch2023selfconsuming` | `journal = {arXiv preprint arXiv:2311.16822}` | ✓ 一致 |
| `sadasivan2023detect` | `journal = {arXiv preprint arXiv:2303.11156}` | ✓ 一致 |
| `mehta2025beyond` | `journal = {arXiv preprint arXiv:2511.17602}` | ✓ 一致 |
| `spennemann2025quantifying` | `journal = {arXiv preprint arXiv:2504.08755}` | ✓ 一致 |
| `suresh2024rate` | `journal = {arXiv preprint arXiv:2412.17646}` | ✓ 一致 |

所有 preprint 均使用 `@article` + `journal = {arXiv preprint arXiv:XXXX.XXXXX}` 格式，**无不一致项**。新增两条也遵循此格式。

**修复的问题**：
- `suresh2024rate`：缺失 `url` 字段 → 已补充 `url={https://arxiv.org/abs/2412.17646}`

**已发表但仍标为 preprint？**：未发现。`sadasivan2023detect` 曾提交 OpenReview 但未确认被某会议正式接收，保持 preprint 状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_r26_sf2_m8_references_20260522T082246"
}
```

</details>

---
