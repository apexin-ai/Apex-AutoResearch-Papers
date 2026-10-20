# paper bib first author audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bib-first-author-audit_20260515T223048_result.json`
- **Structured JSON:** [`ef027a9d62705530514f.json`](../../sessions/ef/ef027a9d62705530514f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审核结果

| # | Citation Key | Title | 当前 First Author | 正确 First Author | 需修复? |
|---|---|---|---|---|---|
| 1 | `maimon2026selfexecution` | Self-Execution Simulation... | Maimon, Gallil | Maimon, Gallil | -- |
| 2 | `meta2025cwm` | CWM: An Open-Weights LLM... | ~~Meta AI~~ | FAIR CodeGen team + Copet, Jade | **已修复** |
| 3 | `liu2024codemind` | CodeMind... | Liu, Changshu | Liu, Changshu | -- |
| 4 | `abdollahi2025demystifying` | Demystifying Errors... | Abdollahi, Mohammad | Abdollahi, Mohammad | -- |
| 5 | `lee2026solidcoder` | SolidCoder... | Lee, Woojin | Lee, Woojin | -- |
| 6 | `shum2025swerm` | SWE-RM... | Shum, KaShun | Shum, KaShun | -- |
| 7 | `xu2025patchreasoner` | Patch Reasoner... | Xu, Junjielong | Xu, Junjielong | -- |
| 8 | `chen2025vgsearch` | Rethinking Optimal Verification... | Chen, Hao Mark | Chen, Hao Mark | -- |
| 9 | `snell2024scaling` | Scaling LLM Test-Time... | Snell, Charlie | Snell, Charlie | -- (title 已修复) |
| 10 | `li2025sstar` | S*: Test Time Scaling... | Li, Dacheng | Li, Dacheng | -- |
| 11 | `jimenez2024swebench` | SWE-bench... | Jimenez, Carlos E | Jimenez, Carlos E | -- |
| 12 | `chowdhury2024swebenchverified` | SWE-bench Verified | Chowdhury, Neil | Chowdhury, Neil | -- |
| 13 | `yang2024sweagent` | SWE-agent... | Yang, John | Yang, John | -- |
| 14 | `xia2024agentless` | Agentless... | Xia, Chunqiu Steven | Xia, Chunqiu Steven | -- |
| 15 | `yang2025aprsurvey` | A Survey of LLM-based APR... | Yang, Boyang | Yang, Boyang | -- |
| 16 | `qwen2025qwen3` | Qwen3 Technical Report | Yang, An (alphabetical) | Yang, An (alphabetical) | -- |
| 17 | `chen2021humaneval` | Evaluating LLMs Trained on Code | Chen, Mark | Chen, Mark | -- |
| 18 | `austin2021mbpp` | Program Synthesis with LLMs | Austin, Jacob | Austin, Jacob | -- |
| 19 | `hu2022lora` | LoRA... | Hu, Edward J | Hu, Edward J | -- |
| 20 | `dettmers2024qlora` | QLoRA... | Dettmers, Tim | Dettmers, Tim | -- |
| 21 | `ni2023lever` | LEVER... | Ni, Ansong | Ni, Ansong | -- |
| 22 | `chen2023codet` | CodeT... | Chen, Bei | Chen, Bei | -- |
| 23 | `rajpurkar2016squad` | SQuAD... | Rajpurkar, Pranav | Rajpurkar, Pranav | -- |
| 24 | `lewis2020bart` | BART... | Lewis, Mike | Lewis, Mike | -- |
| 25 | `raffel2020t5` | T5... | Raffel, Colin | Raffel, Colin | -- |
| 26 | `schuirmann1987tost` | Two One-Sided Tests... | Schuirmann, Donald J | Schuirmann, Donald J | -- |
| 27 | `davison1997bootstrap` | Bootstrap Methods... | Davison, Anthony C | Davison, Anthony C | -- |
| 28 | `shrout1979icc` | Intraclass Correlations... | Shrout, Patrick E | Shrout, Patrick E | -- |

### 修复内容

1. **`meta2025cwm`** — author 字段从 `{Meta AI}` 改为 `{FAIR CodeGen team} and Copet, Jade and ... and others`，匹配 arXiv 实际作者列表
2. **`snell2024scaling`** — title 补上缺失的 "Model"：`...Scaling Model Parameters`

### 附加检查

- **缺失字段**：所有条目的 year、title、author 均完整。会议论文均有 booktitle，期刊论文均有 journal。
- **格式一致性**：会议名称使用简写（ICLR, NeurIPS, EMNLP, ACL, ICML, FSE），风格统一。
- **无其他 first author 错误**：26/28 条目原本就正确，2 条已修复。

---
