# paper compile and verify

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_compile_and_verify_20260522T174753.jsonl`
- **Structured JSON:** [`33105bc543d1f96994df.json`](../../sessions/33/33105bc543d1f96994df.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-22T17:50:06.497538+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
  "description": "Compile LaTeX paper (3 passes + bibtex)",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
    "description": "Compile LaTeX paper (3 passes + bibtex)",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T17:50:06.497885+00:00_

/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (13 pages, 612729 bytes).
Transcript written on main.log.
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (13 pages, 612729 bytes).
Transcript written on main.log.
/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (13 pages, 612729 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T17:50:06.498058+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo \"Errors: $(grep -c '^!' main.log)\" && echo \"Undefined refs: $(grep -c 'LaTeX Warning.*undefined' main.log)\" && grep \"Output written\" main.log",
  "description": "Check compilation errors and page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "echo \"Errors: $(grep -c '^!' main.log)\" && echo \"Undefined refs: $(grep -c 'LaTeX Warning.*undefined' main.log)\" && grep \"Output written\" main.log",
    "description": "Check compilation errors and page count"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T17:50:06.498195+00:00_

Errors: 0
Undefined refs: 0
Output written on main.pdf (13 pages, 612729 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T17:50:06.498319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T17:50:06.498527+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split, a dataset of naturalistic dialogues across diverse topics. LoRA adapters (rank 16, $\alpha$=32) are applied to query and value projection layers (\texttt{q\_proj}, \texttt{v\_proj}). The combined loss $\mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\mathcal{L}_\text{GAR} + \lambda_\text{div}\mathcal{L}_\text{div}$ uses $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$ with MSE target $\tau = 0.5$ (\S\ref{sec:loss}). We train for 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are provided in Appendix~\ref{sec:appendix-hyper}.
7	
8	We evaluate five configurations that form a controlled comparison isolating four factors. \textbf{ThreadGate}: full system with 28 gate networks (Eq.~\ref{eq:gate}) and three-term loss. \textbf{+PCGrad}: ThreadGate with PCGrad \citep{yu2020pcgrad} projecting conflicting gradients (isolates gradient conflict). \textbf{Uniform Gate}: identical gate architecture with turn embedding replaced by a still-learnable constant vector (content-conditioned but turn-unaware; isolates turn conditioning). \textbf{LoRA-only}: gates fixed at 1.0, trained with $\mathcal{L}_\text{NTP} + \mathcal{L}_\text{GAR}$ only (isolates gating mechanism). \textbf{Base}: pretrained model (isolates fine-tuning). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours (last-token attention to goals, \S\ref{sec:background}), GAR-Dongre \citep{dongre2026attention} (all-token average
…[truncated 6787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T17:50:06.498698+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T17:50:06.498875+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Accessibility Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention point.
6	
7	If the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each
…[truncated 4692 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T17:50:06.499054+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\bibliography\\|\\\\\\\\section.*References\\|\\\\\\\\section.*Limitations\\|\\\\\\\\section.*Appendix\\|\\\\\\\\appendix\" main.tex",
  "description": "Find where references/appendix start in main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\bibliography\\|\\\\\\\\section.*References\\|\\\\\\\\section.*Limitations\\|\\\\\\\\section.*Appendix\\|\\\\\\\\appendix\" main.tex",
    "description": "Find where references/appendix start in main.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T17:50:06.499177+00:00_

37:\bibliography{references}
39:\appendix

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T17:50:06.499294+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\n# Use pdftotext to find page where References appears\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\nlines = result.stdout.split('\\n')\npage = 1\nfor line in lines:\n    if '\\x0c' in line:\n        page += 1\n    if 'References' in line and page > 3:\n        print(f'References starts on page {page}: {line.strip()}')\n        break\n    if 'Limitations' in line:\n        print(f'Limitations on page {page}: {line.strip()}')\n    if 'Appendix' in line or 'Hyperparameters' in line:\n        print(f'Appendix on page {page}: {line.strip()}')\n        break\n\" 2>/dev/null || echo \"pdftotext not available\"",
  "description": "Find which page References section starts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\n# Use pdftotext to find page where References appears\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\nlines = result.stdout.split('\\n')\npage = 1\nfor line in lines:\n    if '\\x0c' in line:\n        page += 1\n    if 'References' in line and page > 3:\n        print(f'References starts on page {page}: {line.strip()}')\n        break\n    if 'Limitations' in line:\n        print(f'Limitations on page {page}: {line.strip()}')\n    if 'Appendix' in line or 'Hyperparameters' in line:\n        print(f'Appendix on page {page}: {line.strip()}')\n        break\n\" 2>/dev/null || echo \"pdftotext not available\"",
    "description": "Find which page References section starts"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T17:50:06.499465+00:00_

Appendix on page 3: 147   tions across four families (Table 2; Appendix B), of         (Fan et al., 2020), Mixture-of-Depths (Raposo et al.,   197

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T17:50:06.499619+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\x0c')\nfor i, page in enumerate(pages, 1):\n    if 'References' in page:\n        # Check if it's a section header\n        for line in page.split('\\n'):\n            stripped = line.strip()\n            if stripped == 'References' or stripped.startswith('References'):\n                print(f'Page {i}: \\\"{stripped}\\\"')\n    if 'Limitations' in page:\n        for line in page.split('\\n'):\n            if 'Limitations' in line and ('imitation' in line.lower()):\n                print(f'Page {i}: \\\"{line.strip()}\\\"')\n    if i <= 2:\n        continue\n    # Look for Appendix as section header\n    for line in page.split('\\n'):\n        stripped = line.strip()\n        if stripped.startswith('A ') and ('Hyperparameters' in stripped or 'Loss' in stripped):\n            print(f'Page {i} appendix: \\\"{stripped}\\\"')\n        if stripped.startswith('B ') and ('Loss' in stripped or 'Iteration' in stripped):\n            print(f'Page {i} appendix: \\\"{stripped}\\\"')\n\"",
  "description": "Find References and Appendix page numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\x0c')\nfor i, page in enumerate(pages, 1):\n    if 'References' in page:\n        # Check if it's a section header\n        for line in page.split('\\n'):\n            stripped = line.strip()\n            if stripped == 'References' or stripped.startswith('References'):\n                print(f'Page {i}: \\\"{stripped}\\\"')\n    if 'Limitations' in page:\n        for line in page.split('\\n'):\n            if 'Limitations' in line and ('imitation' in line.lower()):\n                print(f'Page {i}: \\\"{line.strip()}\\\"')\n    if i <= 2:\n        continue\n    # Look for Appendix as section header\n    for line in page.split('\\n'):\n        stripped = line.strip()\n        if stripped.startswith('A ') and ('Hyperparameters' in stripped or 'Loss' in stripped):\n            print(f'Page {i} appendix: \\\"{stripped}\\\"')\n        if stripped.startswith('B ') and ('Loss' in stripped or 'Iteration' in stripped):\n            print(f'Page {i} appendix: \\\"{stripped}\\\"')\n\"",
    "description": "Find References and Appendix page numbers"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T17:50:06.499790+00:00_

Page 9: "634   8   Limitations                                                  Henry Mao, Gary Cottrell, and Julian McAuley. 2021.    684"
Page 10 appendix: "A     Training Hyperparameters                          803"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T17:50:06.499921+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor i, page in enumerate(pages, 1):\n    for line in page.split('\\n'):\n        s = line.strip()\n        if s == 'References':\n            print(f'References header on page {i}')\n        if 'Limitations' == s or s.startswith('8 ') and 'Limitation' in s:\n            print(f'Limitations header on page {i}: {s}')\n\"",
  "description": "Find exact page of References section header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor i, page in enumerate(pages, 1):\n    for line in page.split('\\n'):\n        s = line.strip()\n        if s == 'References':\n            print(f'References header on page {i}')\n        if 'Limitations' == s or s.startswith('8 ') and 'Limitation' in s:\n            print(f'Limitations header on page {i}: {s}')\n\"",
    "description": "Find exact page of References section header"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T17:50:06.500042+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T17:50:06.500157+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor i, page in enumerate(pages, 1):\n    lines = page.split('\\n')\n    for line in lines:\n        s = line.strip()\n        # Look for section-level headers\n        if any(w in s for w in ['Limitations', 'References', 'Ethical']):\n            if len(s) < 80:\n                print(f'Page {i}: [{s}]')\n\"",
  "description": "Find Limitations and References pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor i, page in enumerate(pages, 1):\n    lines = page.split('\\n')\n    for line in lines:\n        s = line.strip()\n        # Look for section-level headers\n        if any(w in s for w in ['Limitations', 'References', 'Ethical']):\n            if len(s) < 80:\n                print(f'Page {i}: [{s}]')\n\"",
    "description": "Find Limitations and References pages"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T17:50:06.500281+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T17:50:06.500396+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor i, page in enumerate(pages, 1):\n    lines = page.split('\\n')\n    for line in lines:\n        s = line.strip()\n        if 'imitation' in s.lower() and len(s) < 30:\n            print(f'Page {i}: [{s}]')\n        if s.lower() == 'references':\n            print(f'Page {i}: [{s}]')\n        if 'ppendix' in s and len(s) < 40:\n            print(f'Page {i}: [{s}]')\n\"",
  "description": "Find section boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor i, page in enumerate(pages, 1):\n    lines = page.split('\\n')\n    for line in lines:\n        s = line.strip()\n        if 'imitation' in s.lower() and len(s) < 30:\n            print(f'Page {i}: [{s}]')\n        if s.lower() == 'references':\n            print(f'Page {i}: [{s}]')\n        if 'ppendix' in s and len(s) < 40:\n            print(f'Page {i}: [{s}]')\n\"",
    "description": "Find section boundaries"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T17:50:06.500560+00:00_

Page 4: [converged during training (Appendix B).]
Page 9: [Limitations]
Page 9: [References]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T17:50:06.500674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T17:50:06.500796+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	
18	\graphicspath{{../figures/paper/}{../artifacts/}}
19	
20	\title{Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation:\\A Mechanistic Analysis}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T17:50:06.500934+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\n# Show last ~10 lines of page 8, first ~10 lines of page 9\nprint('=== END OF PAGE 8 ===')\nlines8 = [l for l in pages[7].split('\\n') if l.strip()]\nfor l in lines8[-10:]:\n    print(l)\nprint()\nprint('=== START OF PAGE 9 ===')\nlines9 = [l for l in pages[8].split('\\n') if l.strip()]\nfor l in lines9[:15]:\n    print(l)\n\"",
  "description": "Check content at page 8-9 boundary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\n# Show last ~10 lines of page 8, first ~10 lines of page 9\nprint('=== END OF PAGE 8 ===')\nlines8 = [l for l in pages[7].split('\\n') if l.strip()]\nfor l in lines8[-10:]:\n    print(l)\nprint()\nprint('=== START OF PAGE 9 ===')\nlines9 = [l for l in pages[8].split('\\n') if l.strip()]\nfor l in lines9[:15]:\n    print(l)\n\"",
    "description": "Check content at page 8-9 boundary"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T17:50:06.501064+00:00_

=== END OF PAGE 8 ===
624
625
626
627
628
629
630
631
632
633

=== START OF PAGE 9 ===
634
8
635
The five-way comparison uses seed = 42;
ThreadGate is additionally validated with
seed = 123 (TF/AR GAR-ours within ±0.001, gap
30.5–32.1×). The remaining three variants use a
single seed; cross-variant convergence provides
indirect robustness evidence but does not substitute
for multi-seed validation.
We test only one type of auxiliary attention loss
(GAR with MSE target τ = 0.5). Other attention steering objectives, such as head-specific or
layer-specific attention losses, may exhibit different sensitivity to exposure bias. Our negative result
applies to the GAR family; it does not rule out all
auxiliary attention interventions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T17:50:06.501200+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\n# Check end of page 7 and beginning of page 8\nprint('=== END OF PAGE 7 ===')\nlines7 = [l for l in pages[6].split('\\n') if l.strip()]\nfor l in lines7[-8:]:\n    print(l)\nprint()\nprint('=== START OF PAGE 8 ===')\nlines8 = [l for l in pages[7].split('\\n') if l.strip()]\nfor l in lines8[:15]:\n    print(l)\nprint()\nprint('=== END OF PAGE 8 (non-empty) ===')\nfor l in lines8[-15:]:\n    print(l)\n\"",
  "description": "Check page 7-8 boundary to understand main text extent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\n# Check end of page 7 and beginning of page 8\nprint('=== END OF PAGE 7 ===')\nlines7 = [l for l in pages[6].split('\\n') if l.strip()]\nfor l in lines7[-8:]:\n    print(l)\nprint()\nprint('=== START OF PAGE 8 ===')\nlines8 = [l for l in pages[7].split('\\n') if l.strip()]\nfor l in lines8[:15]:\n    print(l)\nprint()\nprint('=== END OF PAGE 8 (non-empty) ===')\nfor l in lines8[-15:]:\n    print(l)\n\"",
    "description": "Check page 7-8 boundary to understand main text extent"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T17:50:06.501330+00:00_

=== END OF PAGE 7 ===
528
529
530
531
532
533
534
535

=== START OF PAGE 8 ===
539
under autoregressive generation. Figure 2 confirms
teacher-forced GAR-ours remains near τ = 0.5
(7–8% decay, N = 45), yet autoregressive GAR collapses for all variants (Figure 4b).
540
5.4
541
560
§5.3 showed that exposure bias selectively destroys
GAR-ours while GAR-Dongre remains unaffected
under standard training. We test whether this selectivity extends beyond attention with Turn-level
Residual Coherence (TRC), the cosine similarity
between hidden states at the last-token position of
adjacent assistant turns. For ThreadGate, TF/AR
TRC is 0.334/0.332 (gap +0.002); for LoRA-only,

=== END OF PAGE 8 (non-empty) ===
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T17:50:06.501477+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nlines8 = pages[7].split('\\n')\n# Find sections on page 8\nfor l in lines8:\n    s = l.strip()\n    if s and not s.isdigit() and len(s) > 5:\n        print(s)\n\" | head -30",
  "description": "Show content on page 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nlines8 = pages[7].split('\\n')\n# Find sections on page 8\nfor l in lines8:\n    s = l.strip()\n    if s and not s.isdigit() and len(s) > 5:\n        print(s)\n\" | head -30",
    "description": "Show content on page 8"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T17:50:06.501613+00:00_

under autoregressive generation. Figure 2 confirms
teacher-forced GAR-ours remains near τ = 0.5
(7–8% decay, N = 45), yet autoregressive GAR collapses for all variants (Figure 4b).
§5.3 showed that exposure bias selectively destroys
GAR-ours while GAR-Dongre remains unaffected
under standard training. We test whether this selectivity extends beyond attention with Turn-level
Residual Coherence (TRC), the cosine similarity
between hidden states at the last-token position of
adjacent assistant turns. For ThreadGate, TF/AR
TRC is 0.334/0.332 (gap +0.002); for LoRA-only,
0.349/0.411 (gap −0.062, reversed). Neither shows
a gap comparable to the GAR collapse, confirming
that exposure bias disrupts a specific routing behavior (summary-position attention to goal tokens)
while leaving internal representations intact.
Cross-model evaluation extends this selectivity:
GAR-Dongre shows negligible distribution shift
on both Llama-3.1-8B (AR/TF ratio 1.002×) and
Qwen-2.5-7B (1.28×), compared to the order-ofmagnitude collapse in GAR-ours (the scheduled
sampling experiment in §6 breaks this pattern, with
GAR-Dongre rising to 0.353).
To test whether the failure generalizes, we replicate
on Llama-3.1-8B-Instruct (Grattafiori et al., 2024)
with Base, ThreadGate, and LoRA-only. Phase 1
diagnostics confirm goal attention decay (GAR:
0.026→0.003 over 10 turns). Teacher-forced GARours (N = 50) is 0.484 (TG) and 0.481 (LoRAonly); gating contributes zero benefit. We report median GAR-ours for autoregressive evaluation due to heavy-tailed distributions (5–8% of
turn-level measurements exhibit sporadic attention
spikes). Median GAR-ours (N = 20 mid-turn conversations, excluding the first two turns) is 0.018
for both TG and LoRA-only (Base: 0.009), yielding TF-AR gaps of 27× and 26×. The TF-AR
gap exceeds 25× on both architectures, consistent
with the exposure bias hypothesis. The gate profile

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T17:50:06.501775+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor l in pages[7].split('\\n'):\n    s = l.strip()\n    if 'Conclusion' in s or 'onclusion' in s:\n        print(f'Page 8: [{s}]')\nfor l in pages[8].split('\\n'):\n    s = l.strip()  \n    if 'Conclusion' in s or 'onclusion' in s:\n        print(f'Page 9: [{s}]')\n\"",
  "description": "Find Conclusion section page"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor l in pages[7].split('\\n'):\n    s = l.strip()\n    if 'Conclusion' in s or 'onclusion' in s:\n        print(f'Page 8: [{s}]')\nfor l in pages[8].split('\\n'):\n    s = l.strip()  \n    if 'Conclusion' in s or 'onclusion' in s:\n        print(f'Page 9: [{s}]')\n\"",
    "description": "Find Conclusion section page"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T17:50:06.501894+00:00_

Page 8: [Conclusion]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_compile_and_verify_20260522T174753",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-22T17:50:06.502045+00:00_

汇报：

| 项目 | 结果 |
|------|------|
| **Errors** | 0 |
| **Undefined refs** | 0 |
| **总页数** | 13 页 |
| **主文页数** | **8 页** (Conclusion 在第 8 页，Limitations 第 9 页开头 → 不计入 8 页限制，符合 EMNLP 2026) |
| **References** | 第 9 页（与 Limitations 同页），不计入页数限制 |
| **Appendix** | 第 10-13 页 |

**Table 1 (tab:four-way) 格式确认：**
- `\midrule` 分组：Base 单独一组，下面 ThreadGate / +PCGrad / Uniform Gate / LoRA-only 一组
- `\textbf{}` 标注 best values：GAR-O IID/Held-out 最高 0.51 (Uniform Gate)、GAR-D 最高 0.02 (ThreadGate)、AR GAR-O 最高 0.025 (LoRA-only)
- 表格结构完整，含 `\toprule`/`\midrule`/`\bottomrule`、`\cmidrule` 分列

**Intro 分段确认：**
- 5 个自然段落，合理分段（不是巨块）：(1) 问题引入+GAR量化 (2) residual stream 信息保留 (3) ThreadGate 动机 (4) 五方对比和主要发现 (5) 贡献列表

编译通过，格式和页数均符合要求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_compile_and_verify_20260522T174753"
}
```

</details>

---
