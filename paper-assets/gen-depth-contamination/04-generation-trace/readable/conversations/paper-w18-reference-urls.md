# paper w18 reference urls

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_paper_w18_reference_urls_20260522T061745.jsonl`
- **Structured JSON:** [`bf934ed2019ed39d67cd.json`](../../sessions/bf/bf934ed2019ed39d67cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-22T06:21:14.717880+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T06:21:14.718292+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T06:21:14.718487+00:00_

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
  "session": "worker_paper_w18_reference_urls_20260522T061745",
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

### Tool result

_source line 4 · 2026-05-22T06:21:14.718737+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"% === References for gen-depth-contamination ===\\n% Source: literature_map.yaml — verified 2026-05-15\\n\\n% === Must-Cite ===\\n\\n@inproceedings{drayson2025,\\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\\n  booktitle={Proceedings of EMNLP},\\n  year={2025},\\n  url={https://arxiv.org/abs/2502.15654}\\n}\\n\\n@inproceedings{schaeffer2025position,\\n  title={Position: Model Collapse Does Not Mean What You Think},\\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\\n  booktitle={Proceedings of ICML},\\n  year={2025},\\n  url={https://arxiv.org/abs/2503.03150}\\n}\\n\\n@inproceedings{kazdan2025collapse,\\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\\n  booktitle={Proceedings of ICML},\\n  year={2025},\\n  url={https://arxiv.org/abs/2410.16713}\\n}\\n\\n@inproceedings{mitchell2023detectgpt,\\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\\n  booktitle={Proceedings of ICML},\\n  year={2023}\\n}\\n\\n% === Should-Cite ===\\n\\n@article{basani2026diveye,\\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\\n  author={Basani, Advik Raj and Chen, Pin-Yu},\\n  journal={Transactions on Machine Learning Research},\\n  issn={2835-8856},\\n  year={2026},\\n  url={https://arxiv.org/abs/2509.18880}\\n}\\n\\n@inproceedings{zawalski2026codec,\\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\\n  author={Zawalski, Micha{\\\\l} and Boubdir, Meriem and Ba{\\\\l}azy, Klaudia an
…[truncated 6618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T06:21:14.719069+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -c \"@\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -c \"@\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T06:21:14.719243+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"31\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T06:21:14.719377+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -c \"url = \" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -c \"url = \" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T06:21:14.719519+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"0\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T06:21:14.719799+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -c \"url=\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -c \"url=\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T06:21:14.719992+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"17\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T06:21:14.720158+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"^@\\|url=\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -n \"^@\\|url=\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T06:21:14.720293+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T06:21:14.720414+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -nE \"^@|url=\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -nE \"^@|url=\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T06:21:14.720535+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T06:21:14.720664+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"^@\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -n \"^@\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T06:21:14.720808+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"url=\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -n \"url=\" /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-22T06:21:14.720994+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"6:@inproceedings{drayson2025,\\n14:@inproceedings{schaeffer2025position,\\n22:@inproceedings{kazdan2025collapse,\\n30:@inproceedings{mitchell2023detectgpt,\\n39:@article{basani2026diveye,\\n48:@inproceedings{zawalski2026codec,\\n56:@inproceedings{zhang2024minkpp,\\n63:@article{shumailov2024collapse,\\n72:@inproceedings{alemohammad2024selfconsuming,\\n79:@inproceedings{dohmatob2024model,\\n86:@inproceedings{xie2023dsir,\\n93:@inproceedings{tirumala2023d4,\\n100:@inproceedings{xie2023doremi,\\n107:@inproceedings{hans2024binoculars,\\n116:@inproceedings{alain2017understanding,\\n123:@article{belinkov2022probing,\\n135:@inproceedings{bao2024fast,\\n143:@inproceedings{frank2001ordinal,\\n153:@inproceedings{cheng2025beyond,\\n161:@article{mehta2025beyond,\\n171:@inproceedings{sun2025aigt,\\n179:@article{spennemann2025quantifying,\\n189:@inproceedings{dohmatob2025strong,\\n197:@inproceedings{wang2024semeval,\\n205:@inproceedings{gerstgrasser2024model,\\n213:@inproceedings{guo2024curious,\\n221:@article{briesch2023selfconsuming,\\n229:@inproceedings{padmakumar2024writing,\\n239:@inproceedings{krishna2023paraphrasing,\\n246:@article{sadasivan2023detect,\\n254:@inproceedings{hao2025rewrite,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T06:21:14.721148+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"11:  url={https://arxiv.org/abs/2502.15654}\\n19:  url={https://arxiv.org/abs/2503.03150}\\n27:  url={https://arxiv.org/abs/2410.16713}\\n45:  url={https://arxiv.org/abs/2509.18880}\\n53:  url={https://arxiv.org/abs/2510.27055}\\n140:  url={https://arxiv.org/abs/2310.05130}\\n158:  url={https://arxiv.org/abs/2410.14259}\\n166:  url={https://arxiv.org/abs/2511.17602}\\n176:  url={https://arxiv.org/abs/2412.18148}\\n184:  url={https://arxiv.org/abs/2504.08755}\\n194:  url={https://arxiv.org/abs/2410.04840}\\n202:  url={https://arxiv.org/abs/2404.14183}\\n210:  url={https://arxiv.org/abs/2404.01413}\\n218:  url={https://arxiv.org/abs/2311.09807}\\n226:  url={https://arxiv.org/abs/2311.16822}\\n234:  url={https://arxiv.org/abs/2309.05196}\\n251:  url={https://arxiv.org/abs/2303.11156}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T06:21:14.721317+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -170 /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -170 /root/autodl-tmp/gen-depth-contamination/docs/paper/references.bib",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T06:21:14.721514+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"% === References for gen-depth-contamination ===\\n% Source: literature_map.yaml — verified 2026-05-15\\n\\n% === Must-Cite ===\\n\\n@inproceedings{drayson2025,\\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\\n  booktitle={Proceedings of EMNLP},\\n  year={2025},\\n  url={https://arxiv.org/abs/2502.15654}\\n}\\n\\n@inproceedings{schaeffer2025position,\\n  title={Position: Model Collapse Does Not Mean What You Think},\\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\\n  booktitle={Proceedings of ICML},\\n  year={2025},\\n  url={https://arxiv.org/abs/2503.03150}\\n}\\n\\n@inproceedings{kazdan2025collapse,\\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\\n  booktitle={Proceedings of ICML},\\n  year={2025},\\n  url={https://arxiv.org/abs/2410.16713}\\n}\\n\\n@inproceedings{mitchell2023detectgpt,\\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\\n  booktitle={Proceedings of ICML},\\n  year={2023}\\n}\\n\\n% === Should-Cite ===\\n\\n@article{basani2026diveye,\\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\\n  author={Basani, Advik Raj and Chen, Pin-Yu},\\n  journal={Transactions on Machine Learning Research},\\n  issn={2835-8856},\\n  year={2026},\\n  url={https://arxiv.org/abs/2509.18880}\\n}\\n\\n@inproceedings{zawalski2026codec,\\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\\n  author={Zawalski, Micha{\\\\l} and Boubdir, Meriem and Ba{\\\\l}azy, Klaudia an
…[truncated 4587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T06:21:14.721719+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature Mitchell ICML 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature Mitchell ICML 2023 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T06:21:14.721948+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Min-K%++ Improved Baseline Detecting Pre-Training Data Large Language Models Zhang EMNLP 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Min-K%++ Improved Baseline Detecting Pre-Training Data Large Language Models Zhang EMNLP 2024 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T06:21:14.722102+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shumailov \"AI Models Collapse When Trained on Recursively Generated Data\" Nature 2024 DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shumailov \"AI Models Collapse When Trained on Recursively Generated Data\" Nature 2024 DOI"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T06:21:14.722224+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Self-Consuming Generative Models Go MAD Alemohammad ICLR 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Self-Consuming Generative Models Go MAD Alemohammad ICLR 2024 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T06:21:14.722343+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Tale of Tails Model Collapse as a Change of Scaling Laws\" Dohmatob ICML 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Tale of Tails Model Collapse as a Change of Scaling Laws\" Dohmatob ICML 2024 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T06:21:14.722458+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DSIR \"Data Selection with Importance Resampling\" Xie ICML 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DSIR \"Data Selection with Importance Resampling\" Xie ICML 2023 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T06:21:14.722572+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "D4 Improving LLM Pretraining Document De-Duplication Diversification Tirumala NeurIPS 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "D4 Improving LLM Pretraining Document De-Duplication Diversification Tirumala NeurIPS 2023 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T06:21:14.722724+00:00_

Web search results for query: "Shumailov "AI Models Collapse When Trained on Recursively Generated Data" Nature 2024 DOI"

Links: [{"title":"A note on “AI models collapse when trained on recursively generated data” | by Ali Borji | Medium","url":"https://medium.com/@aliborji/a-note-on-ai-models-collapse-when-trained-on-recursively-generated-data-5bee1de1ab87"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"A Note on Shumailov et al. (2024): ‘AI Models Collapse When Trained on Recursively Generated Data’","url":"https://arxiv.org/html/2410.12954v2"},{"title":"AI models collapse when trained on recursively generated data","url":"https://ideas.repec.org/a/nat/nature/v631y2024i8022d10.1038_s41586-024-07566-y.html"},{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/pdf/2410.12954"},{"title":"AI models collapse when trained on recursively generated data","url":"https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf"},{"title":"[PDF] AI models collapse when trained on recursively generated data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AI-models-collapse-when-trained-on-recursively-data-Shumailov-Shumaylov/603d3f90fc40f79ff51258f0295de3ec5107f73e"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'","url":"https://arxiv.org/abs/2410.12954"},{"title":"Author Correction: AI models collapse when trained on recursively generated data","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11981929/"}]

I found the paper you're looking for. Here are the key details:

**Publication Information:**
The paper was published in Nature, volume 631, pages 755–759 (2024
…[truncated 912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T06:21:14.722996+00:00_

Web search results for query: "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature Mitchell ICML 2023 arxiv"

Links: [{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230111305M/abstract"},{"title":"[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3698"},{"title":"dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.","url":"https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability   Curvature","url":"https://arxiv.org/pdf/2301.11305"},{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"GitHub - eric-mitchell/detect-gpt: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature · GitHub","url":"https://github.com/eric-mitchell/detect-gpt"},{"title":"ICML 2023 DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature Oral","url":"https://icml.cc/virtual/2023/oral/25525"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://proceedings.mlr.press/v202/mitchell23a.html"},{"title":"FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature

**Authors:** Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn

**Publication:** Proceedings of the 40th Internation
…[truncated 1141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T06:21:14.723334+00:00_

Web search results for query: "Min-K%++ Improved Baseline Detecting Pre-Training Data Large Language Models Zhang EMNLP 2024 arxiv"

Links: [{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/min-kpercent-improved-baseline-detecting-pre-training"},{"title":"Paper page - Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://huggingface.co/papers/2404.02936"},{"title":"(PDF) Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models (2024) | Jingyang Zhang | 16 Citations","url":"https://scispace.com/papers/min-k-improved-baseline-for-detecting-pre-training-data-from-1r3llgg58h"},{"title":"(PDF) Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://www.researchgate.net/publication/379541659_Min-K_Improved_Baseline_for_Detecting_Pre-Training_Data_from_Large_Language_Models"},{"title":"[2404.02936] Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/abs/2404.02936"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models - 专知论文","url":"https://sl.zhuanzhi.ai/paper/e31511b756378dfdbb98e08410253633"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/html/2404.02936v1"}]

I found the paper you're looking for! Here's what I found:

**Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models**

The paper proposes a novel and theoretically motivated methodology for pre-training data detection, named Min-K%++. The problem of pre-training data detection for large language models (LLMs) has received growing attention due to its implications in critical issues like copyright violation and test data contamination.

**Key Contributions:**

T
…[truncated 1053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-22T06:21:14.723521+00:00_

Web search results for query: "DSIR "Data Selection with Importance Resampling" Xie ICML 2023 arxiv"

Links: [{"title":"Data Selection for Language Models via Importance Resampling","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/6b9aa8f418bde2840d5f4ab7a02f663b-Abstract-Conference.html"},{"title":"[2302.03169v3] Data Selection for Language Models via Importance Resampling","url":"http://arxiv.org/abs/2302.03169v3"},{"title":"[2302.03169] Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/abs/2302.03169"},{"title":"NeurIPS Poster Data Selection for Language Models via Importance Resampling","url":"https://neurips.cc/virtual/2023/poster/70154"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://www.researchgate.net/publication/368333487_Data_Selection_for_Language_Models_via_Importance_Resampling"},{"title":"[PDF] Data Selection for Language Models via Importance Resampling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Selection-for-Language-Models-via-Importance-Xie-Santurkar/74013b7cfa0fc524803350fca51341004565eb22"},{"title":"Paper page - Data Selection for Language Models via Importance Resampling","url":"https://huggingface.co/papers/2302.03169"},{"title":"[Quick Review] Data Selection for Language Models via Importance Resampling","url":"https://liner.com/review/data-selection-for-language-models-via-importance-resampling"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/pdf/2302.03169"}]

Based on the search results, I found the paper you're looking for:

**Paper Title:** Data Selection with Importance Resampling (DSIR)

**Authors:** Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang

**Publication:** Advances in Neural Information Processing Systems 36 (NeurIPS 2023) Main Conference Track

**arXiv:** The paper is available at arxiv.org/abs/2302.03169

**Summary:** DSIR is an efficient and 
…[truncated 633 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T06:21:14.723710+00:00_

Web search results for query: "Self-Consuming Generative Models Go MAD Alemohammad ICLR 2024 arxiv"

Links: [{"title":"Two Papers at ICLR 2024","url":"https://dsp.rice.edu/2024/03/16/two-papers-at-iclr/"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD - Houston Methodist Scholars","url":"https://scholars.houstonmethodist.org/en/publications/self-consuming-generative-models-go-mad/"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://richb.rice.edu/2023/07/12/self-consuming-generative-models-go-mad/"},{"title":"Self-Consuming Generative Models Go MAD | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10570494"},{"title":"ICLR Poster Self-Consuming Generative Models Go MAD","url":"https://iclr.cc/virtual/2024/poster/18592"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"}]

I found the paper you're looking for! Here's what I found:

**Paper Details:**

"Self-Consuming Generative Models Go MAD" is by S. Alemohammad, J. Casco-Rodriguez, L. Luzi, A. I. Humayun, H. Babaei, D. LeJeune, A. Siahkoohi, and R. G. Baraniuk, and it was presented at the International Conference on Learning Representations (ICLR) on 16 January 2024.

**Overview:**

The paper addresses how advances in generative AI have led to using AI-synthesized data to train next-generation models, creating a self-consuming loop whose pro
…[truncated 882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-22T06:21:14.723971+00:00_

Web search results for query: ""A Tale of Tails Model Collapse as a Change of Scaling Laws" Dohmatob ICML 2024 arxiv"

Links: [{"title":"A tale of tails: model collapse as a change of scaling laws","url":"https://dl.acm.org/doi/10.5555/3692070.3692515"},{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tale-tails-model-collapse-as-change-scaling"},{"title":"1 Introduction","url":"https://arxiv.org/html/2503.03150v2"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://openreview.net/pdf/c028ead5595978096e7ba1f2c41cc3bb709058f9.pdf"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/html/2402.07043v2"},{"title":"ICML Poster A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://icml.cc/virtual/2024/poster/34339"},{"title":"Paper page - A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://huggingface.co/papers/2402.07043"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/pdf/2402.07043"},{"title":"arxiv preprint - A Tale of Tails: Model Collapse as a Change of Scaling Laws - Welcome","url":"https://aibreakdown.org/arxiv-preprint-a-tale-of-tails-model-collapse-as-a-change-of-scaling-laws/"}]

I found the paper you're looking for! Here's what I found:

## Paper Details

"A Tale of Tails: Model Collapse as a Change of Scaling Laws" is authored by Elvis Dohmatob, Yunzhen Feng, Pu Yang, François Charton, and Julia Kempe.

The paper is available on arxiv (arxiv:2402.07043), and it was presented as a 2024 poster at ICML.

## Main Research Question

The paper asks: How will the scaling laws change in the inevitable regime where synthetic data makes its way into the training corpus?

## Key Fi
…[truncated 580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T06:21:14.724325+00:00_

Web search results for query: "D4 Improving LLM Pretraining Document De-Duplication Diversification Tirumala NeurIPS 2023 arxiv"

Links: [{"title":"Kushal Tirumala, Daniel Simig, Armen Aghajanyan, Ari S. Morcos · D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://slideslive.com/39010897/d4-improving-llm-pretraining-via-document-deduplication-and-diversification"},{"title":"[PDF] D4: Improving LLM Pretraining via Document De-Duplication and Diversification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/D4:-Improving-LLM-Pretraining-via-Document-and-Tirumala-Simig/11cf88dce827bd67cbfa60400306318022e736d5"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://papers.nips.cc/paper_files/paper/2023/hash/a8f8cbd7f7a5fb2c837e578c75e5b615-Abstract-Datasets_and_Benchmarks.html"},{"title":"NeurIPS Poster D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://neurips.cc/virtual/2023/poster/73662"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversiﬁcation","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/a8f8cbd7f7a5fb2c837e578c75e5b615-Paper-Datasets_and_Benchmarks.pdf"},{"title":"[2308.12284] D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://arxiv.org/abs/2308.12284"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification | OpenReview","url":"https://openreview.net/forum?id=CG0L2PFrb1&noteId=CG0L2PFrb1"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification - Paper Detail","url":"https://deeplearn.org/arxiv/405850/d4:-improving-llm-pretraining-via-document-de-duplication-and-diversification"},{"title":"D4: Improving LLM Pretraining via Document De-Duplication and Diversification","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/a8f8cbd7f7a5fb2c837e578c75e5b
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T06:21:14.724891+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining Xie NeurIPS 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining Xie NeurIPS 2023 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-22T06:21:14.725191+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Spotting LLMs With Binoculars\" Hans ICML 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Spotting LLMs With Binoculars\" Hans ICML 2024 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T06:21:14.725417+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Alain Bengio \"Understanding Intermediate Layers Using Linear Classifier Probes\" 2017 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alain Bengio \"Understanding Intermediate Layers Using Linear Classifier Probes\" 2017 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T06:21:14.725636+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Belinkov \"Probing Classifiers Promises Shortcomings and Advances\" Computational Linguistics 2022 DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Belinkov \"Probing Classifiers Promises Shortcomings and Advances\" Computational Linguistics 2022 DOI"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T06:21:14.725999+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Frank Hall \"A Simple Approach to Ordinal Classification\" ECML 2001 DOI Springer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Frank Hall \"A Simple Approach to Ordinal Classification\" ECML 2001 DOI Springer"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-22T06:21:14.726152+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Krishna \"Paraphrasing Evades Detectors of AI-Generated Text but Retrieval is an Effective Defense\" NeurIPS 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Krishna \"Paraphrasing Evades Detectors of AI-Generated Text but Retrieval is an Effective Defense\" NeurIPS 2023 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-22T06:21:14.726313+00:00_

Web search results for query: "DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining Xie NeurIPS 2023 arxiv"

Links: [{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | OpenReview","url":"https://openreview.net/forum?id=lXuByUeHhd"},{"title":"NeurIPS Poster DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://neurips.cc/virtual/2023/poster/70588"},{"title":"[2305.10429] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/abs/2305.10429"},{"title":"Paper page - DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://huggingface.co/papers/2305.10429"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://dmlr.ai/assets/accepted-papers/15/CameraReady/ICML_workshop_DoReMi%20(5)%20(1).pdf"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Request PDF","url":"https://www.researchgate.net/publication/401463528_DoReMi_Optimizing_Data_Mixtures_Speeds_Up_Language_Model_Pretraining"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/dcba6be91359358c2355cd920da3fcbd-Paper-Conference.pdf"}]

I found the paper! Here are the search results for "DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining":

## Overview

DoReMi (Domain Reweighting with Minimax Optimization) first trains a small proxy model using group distributionally robust optimization (Group DRO) over domains to produce domain weights, then resamples a dataset with these domain weights and trains a larger, full-sized model.

## Key Results

The researchers use DoReMi on a 280M-parameter proxy model to set the domain weights for training an 8B-parameter model (30x larger) more efficiently.

DoReMi improves average few-shot downstream accuracy by 6.5% points over a baseline model traine
…[truncated 610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-22T06:21:14.726473+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hao \"Learning to Rewrite Generalized LLM-Generated Text Detection\" ACL 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hao \"Learning to Rewrite Generalized LLM-Generated Text Detection\" ACL 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-22T06:21:14.726631+00:00_

Web search results for query: ""Spotting LLMs With Binoculars" Hans ICML 2024 arxiv"

Links: [{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/spotting-llms-binoculars-zero-shot-detection-machine"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated   Text","url":"https://arxiv.org/pdf/2401.12070"},{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"[2401.12070v2] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v2"},{"title":"Spotting LLMs with binoculars | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692768"},{"title":"Under review as a conference paper at ICLR 2024 SPOTTING LLMS WITH BINOCULARS:","url":"https://openreview.net/pdf?id=iARAKITHTH"},{"title":"[2401.12070v1] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v1"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | OpenReview","url":"https://openreview.net/forum?id=iARAKITHTH"}]

I found comprehensive information about the paper "Spotting LLMs With Binoculars" by Hans and colleagues. Here are the key details:

## Paper Overview

The paper is titled "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" by Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein, with arXiv ID 2401.12070.

## Conference Publication

The paper was presented at the Proceedings of the 4
…[truncated 809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T06:21:14.726865+00:00_

Web search results for query: "Alain Bengio "Understanding Intermediate Layers Using Linear Classifier Probes" 2017 arxiv"

Links: [{"title":"Understanding intermediate layers using linear classifier ...","url":"https://www.summarizepaper.com/en/arxiv-id/1610.01644v1/"},{"title":"Understanding intermediate layers using linear classiﬁer probes Guillaume Alain","url":"https://arxiv.org/pdf/1610.01644"},{"title":"[1610.01644v1] Understanding intermediate layers using linear classifier probes","url":"https://www.arxiv.org/abs/1610.01644v1"},{"title":"[1610.01644v3] Understanding intermediate layers using linear classifier probes","url":"https://arxiv.org/abs/1610.01644v3"},{"title":"[1610.01644] Understanding intermediate layers using linear classifier probes","url":"https://arxiv.org/abs/1610.01644"},{"title":"[1610.01644v4] Understanding intermediate layers using linear classifier probes","url":"https://arxiv.org/abs/1610.01644v4"},{"title":"[PDF] Understanding intermediate layers using linear classifier probes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Understanding-intermediate-layers-using-linear-Alain-Bengio/5e23a28063b395bdaf784dc548a046885cb90cf2"},{"title":"(PDF) Understanding intermediate layers using linear classifier probes","url":"https://www.researchgate.net/publication/308913017_Understanding_intermediate_layers_using_linear_classifier_probes"},{"title":"Workshop track - ICLR 2017 UNDERSTANDING INTERMEDIATE LAYERS","url":"https://openreview.net/pdf?id=HJ4-rAVtl"}]

I found the paper you're looking for. The paper "Understanding intermediate layers using linear classifier probes" was authored by Guillaume Alain and Yoshua Bengio (note: the authors are Guillaume Alain and Yoshua Bengio, not Alain Bengio).

The paper was published in 2016, and it's available on arXiv with the ID 1610.01644. 

The method uses linear classifiers called "probes" that can only use the hidden units of a given intermediate layer as discriminating features. The
…[truncated 492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-22T06:21:14.727101+00:00_

Web search results for query: "Frank Hall "A Simple Approach to Ordinal Classification" ECML 2001 DOI Springer"

Links: [{"title":"A Theoretical Approach to Ordinal Classification: Feature Space-Based Definition and Classifier-Independent Detection of Ordinal Class Structures","url":"https://www.mdpi.com/2076-3417/12/4/1815"},{"title":"[PDF] A Simple Approach to Ordinal Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Simple-Approach-to-Ordinal-Classification-Frank-Hall/76fc26939d73c565431e1f38107a4245e739284e"},{"title":"A Simple Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/3-540-44795-4_13"},{"title":"Ordinal Classification with Decision Rules | Springer Nature Link","url":"https://link.springer.com/content/pdf/10.1007/978-3-540-68416-9_14.pdf"},{"title":"(PDF) A Simple Approach to Ordinal Classification","url":"https://www.researchgate.net/publication/226877154_A_Simple_Approach_to_Ordinal_Classification"},{"title":"An Improved Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-662-45652-1_4"},{"title":"A simple approach to ordinal classification | Proceedings of the 12th European Conference on Machine Learning","url":"https://dl.acm.org/doi/10.1007/3-540-44795-4_13"},{"title":"(PDF) A Simple Approach to Ordinal Classification (2001) | Eibe Frank | 655 Citations","url":"https://scispace.com/papers/a-simple-approach-to-ordinal-classification-2mjbzk39ox"}]

Based on the search results, I found the paper you're looking for. Here are the details:

**Paper:** "A Simple Approach to Ordinal Classification" by Frank, E. and Hall, M.A.

**Publication Details:**
- Published in ECML 2001, Lecture Notes in Computer Science, Volume 2167, Springer, Berlin, Heidelberg
- Pages 145–156
- DOI: 10.1007/3-540-44795-4_13

**Summary:** The paper presents a simple method that enables standard classification algorithms to make use
…[truncated 293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T06:21:14.727353+00:00_

Web search results for query: "Hao "Learning to Rewrite Generalized LLM-Generated Text Detection" ACL 2025 arxiv"

Links: [{"title":"Learning to Rewrite: Generalized LLM-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.322/"},{"title":"Distance Learning for Detecting LLM-Generated Text","url":"https://arxiv.org/pdf/2601.21895"},{"title":"Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://arxiv.org/pdf/2408.04237"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Learning to Rewrite: Generalized LLM-Generated Text ...","url":"https://www.cs.columbia.edu/~junfeng/papers/learn2rewrite-acl25.pdf"},{"title":"[2408.04237] Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://arxiv.org/abs/2408.04237"},{"title":"Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://arxiv.org/html/2408.04237"},{"title":"Paper page - Learning to Rewrite: Generalized LLM-Generated Text Detection","url":"https://huggingface.co/papers/2408.04237"}]

I found the paper you're looking for! Here's the information:

**Learning to Rewrite: Generalized LLM-Generated Text Detection** is authored by Wei Hao, Ran Li, Weiliang Zhao, Junfeng Yang, and Chengzhi Mao and was published at ACL 2025. The paper appears in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 6421–6434, Vienna, Austria.

The paper is available on:
- **ACL Anthology**: https://aclanthology.org/2025.acl-long.322/
- **arXiv**: https://arxiv.org/abs/2408.04237

The paper introduces Learning2Rewrite, a novel framework for detecting AI-generated text with exceptional generalization to unseen domains, leveraging the insight that LLMs inherently modify AI-generated content less than human-written text when tasked with rewriting. Extensive experiments on data from 21 independent domains and f
…[truncated 362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-22T06:21:14.727557+00:00_

Web search results for query: "Belinkov "Probing Classifiers Promises Shortcomings and Advances" Computational Linguistics 2022 DOI"

Links: [{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"(PDF) Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/pdf/2102.12452"},{"title":"[PDF] Probing Classifiers: Promises, Shortcomings, and Advances | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Probing-Classifiers:-Promises,-Shortcomings,-and-Belinkov/3dcfa05a1c162e6cab927c5b08d0444f7b6691f4"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://aclanthology.org/2022.cl-1.7.pdf"}]

I found the paper you're looking for. Here are the key details:

**Citation Information:**
Yonatan Belinkov's "Probing Classifiers: Promises, Shortcomings, and Advances" was published in C
…[truncated 907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-22T06:21:14.727745+00:00_

Web search results for query: "Krishna "Paraphrasing Evades Detectors of AI-Generated Text but Retrieval is an Effective Defense" NeurIPS 2023 arxiv"

Links: [{"title":"GitHub - martiansideofthemoon/ai-detection-paraphrases: Official repository for our NeurIPS 2023 paper \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\" (https://arxiv.org/abs/2303.13408). · GitHub","url":"https://github.com/martiansideofthemoon/ai-detection-paraphrases"},{"title":"[2303.13408v1] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://arxiv.org/abs/2303.13408v1"},{"title":"[2303.13408] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://arxiv.org/abs/2303.13408"},{"title":"[PDF] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Paraphrasing-evades-detectors-of-AI-generated-text,-Krishna-Song/1c13af186d1e177b85ef1ec3fc7b8d33ec314cfd"},{"title":"NeurIPS Poster Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://neurips.cc/virtual/2023/poster/71402"},{"title":"Paper page - Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://huggingface.co/papers/2303.13408"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://arxiv.org/pdf/2303.13408"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Request PDF","url":"https://www.researchgate.net/publication/369477232_Paraphrasing_evades_detectors_of_AI-generated_text_but_retrieval_is_an_effective_defense"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://openreview.net/pdf?id=WbFhFvjjKj"}]

Based on the search results, I found the paper you're looking for:

## Paper Details

…[truncated 1631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-22T06:21:14.728066+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && python3 -c \"\nimport re\n\nwith open('references.bib', 'r') as f:\n    content = f.read()\n\nurls = {\n    'mitchell2023detectgpt': 'https://arxiv.org/abs/2301.11305',\n    'zhang2024minkpp': 'https://arxiv.org/abs/2404.02936',\n    'shumailov2024collapse': 'https://doi.org/10.1038/s41586-024-07566-y',\n    'alemohammad2024selfconsuming': 'https://arxiv.org/abs/2307.01850',\n    'dohmatob2024model': 'https://arxiv.org/abs/2402.07043',\n    'xie2023dsir': 'https://arxiv.org/abs/2302.03169',\n    'tirumala2023d4': 'https://arxiv.org/abs/2308.12284',\n    'xie2023doremi': 'https://arxiv.org/abs/2305.10429',\n    'hans2024binoculars': 'https://arxiv.org/abs/2401.12070',\n    'alain2017understanding': 'https://arxiv.org/abs/1610.01644',\n    'belinkov2022probing': 'https://doi.org/10.1162/coli_a_00422',\n    'frank2001ordinal': 'https://doi.org/10.1007/3-540-44795-4_13',\n    'krishna2023paraphrasing': 'https://arxiv.org/abs/2303.13408',\n    'hao2025rewrite': 'https://arxiv.org/abs/2408.04237',\n}\n\nfor key, url in urls.items():\n    pattern = r'(@\\w+\\{' + re.escape(key) + r',.*?year=\\{[^}]+\\})\\s*\\n(\\})'\n    replacement = r'\\1,\\n  url={' + url + r'}\\n\\2'\n    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)\n    if new_content == content:\n        print(f'WARNING: No match for {key}')\n    else:\n        print(f'OK: {key} -> {url}')\n    content = new_content\n\nwith open('references.bib', 'w') as f:\n    f.write(content)\n\nprint('Done. Verifying...')\n# Count entries and URLs\nentry_count = len(re.findall(r'^@', content, re.MULTILINE))\nurl_count = len(re.findall(r'url=', content))\nprint(f'Entries: {entry_count}, URLs: {url_count}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && python3 -c \"\nimport re\n\nwith open('references.bib', 'r') as f:\n    content = f.read()\n\nurls = {\n    'mitchell2023detectgpt': 'https://arxiv.org/abs/2301.11305',\n    'zhang2024minkpp': 'https://arxiv.org/abs/2404.02936',\n    'shumailov2024collapse': 'https://doi.org/10.1038/s41586-024-07566-y',\n    'alemohammad2024selfconsuming': 'https://arxiv.org/abs/2307.01850',\n    'dohmatob2024model': 'https://arxiv.org/abs/2402.07043',\n    'xie2023dsir': 'https://arxiv.org/abs/2302.03169',\n    'tirumala2023d4': 'https://arxiv.org/abs/2308.12284',\n    'xie2023doremi': 'https://arxiv.org/abs/2305.10429',\n    'hans2024binoculars': 'https://arxiv.org/abs/2401.12070',\n    'alain2017understanding': 'https://arxiv.org/abs/1610.01644',\n    'belinkov2022probing': 'https://doi.org/10.1162/coli_a_00422',\n    'frank2001ordinal': 'https://doi.org/10.1007/3-540-44795-4_13',\n    'krishna2023paraphrasing': 'https://arxiv.org/abs/2303.13408',\n    'hao2025rewrite': 'https://arxiv.org/abs/2408.04237',\n}\n\nfor key, url in urls.items():\n    pattern = r'(@\\w+\\{' + re.escape(key) + r',.*?year=\\{[^}]+\\})\\s*\\n(\\})'\n    replacement = r'\\1,\\n  url={' + url + r'}\\n\\2'\n    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)\n    if new_content == content:\n        print(f'WARNING: No match for {key}')\n    else:\n        print(f'OK: {key} -> {url}')\n    content = new_content\n\nwith open('references.bib', 'w') as f:\n    f.write(content)\n\nprint('Done. Verifying...')\n# Count entries and URLs\nentry_count = len(re.findall(r'^@', content, re.MULTILINE))\nurl_count = len(re.findall(r'url=', content))\nprint(f'Entries: {entry_count}, URLs: {url_count}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-22T06:21:14.728249+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"OK: mitchell2023detectgpt -> https://arxiv.org/abs/2301.11305\\nOK: zhang2024minkpp -> https://arxiv.org/abs/2404.02936\\nOK: shumailov2024collapse -> https://doi.org/10.1038/s41586-024-07566-y\\nOK: alemohammad2024selfconsuming -> https://arxiv.org/abs/2307.01850\\nOK: dohmatob2024model -> https://arxiv.org/abs/2402.07043\\nOK: xie2023dsir -> https://arxiv.org/abs/2302.03169\\nOK: tirumala2023d4 -> https://arxiv.org/abs/2308.12284\\nOK: xie2023doremi -> https://arxiv.org/abs/2305.10429\\nOK: hans2024binoculars -> https://arxiv.org/abs/2401.12070\\nOK: alain2017understanding -> https://arxiv.org/abs/1610.01644\\nOK: belinkov2022probing -> https://doi.org/10.1162/coli_a_00422\\nOK: frank2001ordinal -> https://doi.org/10.1007/3-540-44795-4_13\\nOK: krishna2023paraphrasing -> https://arxiv.org/abs/2303.13408\\nOK: hao2025rewrite -> https://arxiv.org/abs/2408.04237\\nDone. Verifying...\\nEntries: 31, URLs: 31\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_w18_reference_urls_20260522T061745",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-22T06:21:14.728461+00:00_

全部 14 条 URL 添加成功。31 个条目现在都有 URL。

## 结果汇总

**缺 URL 的 14 个条目（非 8 个）及补全的 URL：**

| # | cite key | URL |
|---|----------|-----|
| 1 | `mitchell2023detectgpt` | `https://arxiv.org/abs/2301.11305` |
| 2 | `zhang2024minkpp` | `https://arxiv.org/abs/2404.02936` |
| 3 | `shumailov2024collapse` | `https://doi.org/10.1038/s41586-024-07566-y` |
| 4 | `alemohammad2024selfconsuming` | `https://arxiv.org/abs/2307.01850` |
| 5 | `dohmatob2024model` | `https://arxiv.org/abs/2402.07043` |
| 6 | `xie2023dsir` | `https://arxiv.org/abs/2302.03169` |
| 7 | `tirumala2023d4` | `https://arxiv.org/abs/2308.12284` |
| 8 | `xie2023doremi` | `https://arxiv.org/abs/2305.10429` |
| 9 | `hans2024binoculars` | `https://arxiv.org/abs/2401.12070` |
| 10 | `alain2017understanding` | `https://arxiv.org/abs/1610.01644` |
| 11 | `belinkov2022probing` | `https://doi.org/10.1162/coli_a_00422` |
| 12 | `frank2001ordinal` | `https://doi.org/10.1007/3-540-44795-4_13` |
| 13 | `krishna2023paraphrasing` | `https://arxiv.org/abs/2303.13408` |
| 14 | `hao2025rewrite` | `https://arxiv.org/abs/2408.04237` |

**URL 类型选择：**
- Nature 文章（shumailov2024collapse）用 DOI URL
- Computational Linguistics 文章（belinkov2022probing）用 DOI URL
- Springer 会议论文（frank2001ordinal）用 DOI URL
- 其余全部用 arXiv 链接

**未找到 URL 的条目：** 无，全部补全。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_w18_reference_urls_20260522T061745"
}
```

</details>

---
