# research diveye citation verify

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_research_diveye_citation_verify_20260514T195449.jsonl`
- **Structured JSON:** [`2089ae4b2ae0dab6d07c.json`](../../sessions/20/2089ae4b2ae0dab6d07c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-14T19:56:10.238045+00:00_

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
  "session": "worker_research_diveye_citation_verify_20260514T195449",
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

_source line 2 · 2026-05-14T19:56:10.238359+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T19:56:10.238550+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Basani Chen DivEye Diversity Boosts AI-Generated Text Detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Basani Chen DivEye Diversity Boosts AI-Generated Text Detection"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T19:56:10.238681+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DivEye TMLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DivEye TMLR 2026"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T19:56:10.238800+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "IBM diveye text detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "WebSearch",
  "tool_args": {
    "query": "IBM diveye text detection"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T19:56:10.238967+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/IBM/diveye",
  "prompt": "Does this GitHub repository exist? What is it about? List the README content, authors, and description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/IBM/diveye",
    "prompt": "Does this GitHub repository exist? What is it about? List the README content, authors, and description."
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T19:56:10.239149+00:00_

Web search results for query: "Basani Chen DivEye Diversity Boosts AI-Generated Text Detection"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"DivEye","url":"https://diveye.vercel.app/"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection","url":"https://ceur-ws.org/Vol-4038/paper_282.pdf"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"}]

Based on the search results, here's what I found about "Diversity Boosts AI-Generated Text Detection":

## Overview

DivEye is a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-based features. The research was authored by Advik Raj Basani and Pin-Yu Chen.

## Key Innovation

The framework is motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs, and DivEye captures th
…[truncated 892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T19:56:10.239324+00:00_

Web search results for query: "IBM diveye text detection"

Links: [{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880"},{"title":"DivEye","url":"https://diveye.vercel.app/"},{"title":"DivEye - Diversity Boosts AI-generated Text Detection - a Hugging Face Space by pinyuchen","url":"https://huggingface.co/spaces/pinyuchen/Diveye_AI_text_detector"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"DivEye: Diversity-Driven AI Text Detector - a TrustSafeAI Collection","url":"https://huggingface.co/collections/TrustSafeAI/diveye-diversity-driven-ai-text-detector"},{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"},{"title":"DivEye - Diversity Boosts AI-generated Text Detection - a Hugging Face Space by edusocial","url":"https://huggingface.co/spaces/edusocial/Diveye_AI_text_detector"}]

Based on the search results, here's what I found about IBM DivEye text detection:

## Overview

DivEye is an official implementation from IBM for the paper "Diversity Boosts AI-Generated Text Detection" (accepted at TMLR '26 and ICML, Data in Generative Models).

## What It Does

DivEye is a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-based features. More specifically, human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs, and DivEye captures this signal through a set of interpretable statistical features.

## Key Features

DivEye 
…[truncated 746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T19:56:10.239500+00:00_

Web search results for query: "DivEye TMLR 2026"

Links: [{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"tmlr-2026 · GitHub Topics · GitHub","url":"https://github.com/topics/tmlr-2026"},{"title":"ICLR 2026 on X: \"Following a successful pilot, ICLR has decided to continue its partnership with TMLR. Look forward to seeing more exciting TMLR publications featured at ICLR for the foreseeable future!\" / X","url":"https://x.com/iclr_conf/status/1919852504658989088"},{"title":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/"},{"title":"TMLR - Transactions on Machine Learning Research","url":"https://openreview.net/group?id=TMLR"},{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"Daily TMLR digest for Jan 27, 2026","url":"https://groups.google.com/g/tmlr-announce-daily/c/15WAmvi5idM"},{"title":"GriDiT-TMLR-2026","url":"https://snehalstomar.github.io/projects/gridit_project/index.html"},{"title":"The NeurIPS/ICLR/ICML Journal-to-Conference Track","url":"https://icml.cc/public/JournalToConference"},{"title":"Announcing MLRC 2025, our first in-person conference | MLRC 2025","url":"https://reproml.org/blog/announcing_mlrc2025/"}]

Based on the search results, here's what I found about DivEye TMLR 2026:

DivEye is an official implementation for the paper "Diversity Boosts AI-Generated Text Detection" which was accepted at TMLR '26 and also presented at ICML's Data in Generative Models (DIG-BUG) workshop in 2025.

The method is motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs, and DivEye captures this signal through a set of interpretable statistical features.

**Key Performance Results:**
- The method outperforms existing zero-shot detectors by up to 33.2% and achieves competitive perf
…[truncated 739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T19:56:10.239656+00:00_

# DivEye GitHub Repository

**Repository Status:** Yes, this repository exists.

## Description

DivEye is an AI-generated text detection framework published at TMLR '26 and ICML's Data in Generative Models workshop (2025). The project proposes a novel method using "surprisal-based features" to identify synthetic text by analyzing how unpredictability fluctuates throughout documents.

## Key Focus

The framework addresses detection challenges by capturing "richer variability in lexical and structural unpredictability" that distinguishes human writing from LLM outputs, achieving significant performance improvements over existing zero-shot detectors.

## Authors

- Advik Raj Basani
- Pin-Yu Chen

## README Content Summary

**Installation:** Setup requires Python 3.11, conda, and dependencies including transformers, scikit-learn, and xgboost.

**Execution:** Run via command line with required arguments for model selection and train/test datasets in CSV format.

**License:** CC BY-NC-SA 4.0

**Additional Resources:**
- Official website: https://diveye.vercel.app/
- HuggingFace Space (ZeroGPU): Available for live demonstrations

The repository contains core implementation files and is written entirely in Python.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T19:56:10.239819+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__append_idea",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__append_idea",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T19:56:10.239968+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T19:56:10.240086+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T19:56:10.240221+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/memory.md\", \"content\": \"# Memory — recursive_gen_depth_est\\n\\n## 经验教训\\n\\n### [2026-05-14] Cron false failure 根因\\nWorker 绕过 `submit_training_job`（ToolSearch 找不到该工具），用 raw ssh_execute 创建 tmux session，导致无 sentinel 文件。Cron handler 连续检测 \\\"process dead, no sentinel, no W&B\\\" → 误标 failed。\\n**修复**：所有 pipeline 脚本已添加 EXIT trap（通过 `AML_EXP_ID` 环境变量写 sentinel 到 `/tmp/agent-ml-exit/{exp_id}.exit`）。spawn_worker 时确保 tool_groups 包含 submit_training_job 所需工具，或在 tools 中显式传入。\\n\\n### [2026-05-14] GPT-2 XL 表现最强的可能原因\\nGPT-2 XL nucleus 83.3% >> Pythia 78.2% / OLMo 78.8%。Worker 分析：跨模型 surprisal（Pythia 参考模型评估 GPT-2 XL 文本）放大了递归退化信号 + GPT-2 XL 代码污染极低（<1.5%）。这对 paper framing 有影响——需要讨论 cross-model evaluation 是否引入了 bias。\\n\\n### [2026-05-14] DivEye 引用修正\\nbaselines.py 中 \\\"Basani & Chen, ICLR 2026\\\" 实际为 TMLR 2026。已修正。\\n\\n### [2026-05-14] 3×3 矩阵排队优化\\n同模型不同 decoding strategy 的 pipeline 可复用 depth-0 LoRA adapter（Step 1 与 decoding 无关）。通过 symlink nucleus adapter 跳过重复训练，节省 ~4.5min/run。\\n\", \"total_chars\": 917, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T19:56:10.240391+00:00_

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
  "session": "worker_research_diveye_citation_verify_20260514T195449",
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

_source line 16 · 2026-05-14T19:56:10.240510+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T19:56:10.240630+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "memory.md",
  "content": "# Memory — recursive_gen_depth_est\n\n## 经验教训\n\n### [2026-05-14] Cron false failure 根因\nWorker 绕过 `submit_training_job`（ToolSearch 找不到该工具），用 raw ssh_execute 创建 tmux session，导致无 sentinel 文件。Cron handler 连续检测 \"process dead, no sentinel, no W&B\" → 误标 failed。\n**修复**：所有 pipeline 脚本已添加 EXIT trap（通过 `AML_EXP_ID` 环境变量写 sentinel 到 `/tmp/agent-ml-exit/{exp_id}.exit`）。spawn_worker 时确保 tool_groups 包含 submit_training_job 所需工具，或在 tools 中显式传入。\n\n### [2026-05-14] GPT-2 XL 表现最强的可能原因\nGPT-2 XL nucleus 83.3% >> Pythia 78.2% / OLMo 78.8%。Worker 分析：跨模型 surprisal（Pythia 参考模型评估 GPT-2 XL 文本）放大了递归退化信号 + GPT-2 XL 代码污染极低（<1.5%）。这对 paper framing 有影响——需要讨论 cross-model evaluation 是否引入了 bias。\n\n### [2026-05-14] DivEye 引用验证 (Reviewer 引用审计)\n- **结论: 真实论文 ✓**\n- 论文: \"Diversity Boosts AI-Generated Text Detection\", Advik Raj Basani & Pin-Yu Chen\n- 发表: TMLR 2026 (confirmed via OpenReview + GitHub tag)\n- arXiv: https://arxiv.org/abs/2509.18880\n- OpenReview: https://openreview.net/forum?id=DNgsOhGZBI\n- GitHub: https://github.com/IBM/diveye (存在，CC BY-NC-SA 4.0，Python 实现)\n- HuggingFace Space: https://huggingface.co/spaces/pinyuchen/Diveye_AI_text_detector\n- 官网: https://diveye.vercel.app/\n- 也在 ICML 2025 DIG-BUG workshop 发表 (CEUR-WS Vol-4038)\n- **注意**: baselines.py 中曾误写为 \"ICLR 2026\"，已修正为 \"TMLR 2026\"\n- **行动: 保留引用，无需替换**\n\n### [2026-05-14] 3×3 矩阵排队优化\n同模型不同 decoding strategy 的 pipeline 可复用 depth-0 LoRA adapter（Step 1 与 decoding 无关）。通过 symlink nucleus adapter 跳过重复训练，节省 ~4.5min/run。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "memory.md",
    "content": "# Memory — recursive_gen_depth_est\n\n## 经验教训\n\n### [2026-05-14] Cron false failure 根因\nWorker 绕过 `submit_training_job`（ToolSearch 找不到该工具），用 raw ssh_execute 创建 tmux session，导致无 sentinel 文件。Cron handler 连续检测 \"process dead, no sentinel, no W&B\" → 误标 failed。\n**修复**：所有 pipeline 脚本已添加 EXIT trap（通过 `AML_EXP_ID` 环境变量写 sentinel 到 `/tmp/agent-ml-exit/{exp_id}.exit`）。spawn_worker 时确保 tool_groups 包含 submit_training_job 所需工具，或在 tools 中显式传入。\n\n### [2026-05-14] GPT-2 XL 表现最强的可能原因\nGPT-2 XL nucleus 83.3% >> Pythia 78.2% / OLMo 78.8%。Worker 分析：跨模型 surprisal（Pythia 参考模型评估 GPT-2 XL 文本）放大了递归退化信号 + GPT-2 XL 代码污染极低（<1.5%）。这对 paper framing 有影响——需要讨论 cross-model evaluation 是否引入了 bias。\n\n### [2026-05-14] DivEye 引用验证 (Reviewer 引用审计)\n- **结论: 真实论文 ✓**\n- 论文: \"Diversity Boosts AI-Generated Text Detection\", Advik Raj Basani & Pin-Yu Chen\n- 发表: TMLR 2026 (confirmed via OpenReview + GitHub tag)\n- arXiv: https://arxiv.org/abs/2509.18880\n- OpenReview: https://openreview.net/forum?id=DNgsOhGZBI\n- GitHub: https://github.com/IBM/diveye (存在，CC BY-NC-SA 4.0，Python 实现)\n- HuggingFace Space: https://huggingface.co/spaces/pinyuchen/Diveye_AI_text_detector\n- 官网: https://diveye.vercel.app/\n- 也在 ICML 2025 DIG-BUG workshop 发表 (CEUR-WS Vol-4038)\n- **注意**: baselines.py 中曾误写为 \"ICLR 2026\"，已修正为 \"TMLR 2026\"\n- **行动: 保留引用，无需替换**\n\n### [2026-05-14] 3×3 矩阵排队优化\n同模型不同 decoding strategy 的 pipeline 可复用 depth-0 LoRA adapter（Step 1 与 decoding 无关）。通过 symlink nucleus adapter 跳过重复训练，节省 ~4.5min/run。\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T19:56:10.240766+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_diveye_citation_verify_20260514T195449",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T19:56:10.240939+00:00_

## DivEye 引用审计结论: **真实论文 ✓**

| 字段 | 声称 | 验证结果 |
|------|------|----------|
| 作者 | Basani & Chen | ✓ Advik Raj Basani & Pin-Yu Chen |
| 标题 | "Diversity Boosts AI-Generated Text Detection" | ✓ 完全匹配 |
| 发表 | TMLR 2026 | ✓ 确认 (OpenReview + GitHub tag) |
| GitHub | github.com/IBM/diveye | ✓ 存在，有完整代码 |

额外发现：该工作也在 ICML 2025 DIG-BUG workshop 发表（CEUR-WS Vol-4038），有 HuggingFace Space demo 和官网 diveye.vercel.app。

**行动：保留引用，无需替换。**

Sources:
- [arXiv: 2509.18880](https://arxiv.org/abs/2509.18880)
- [OpenReview](https://openreview.net/forum?id=DNgsOhGZBI)
- [GitHub - IBM/diveye](https://github.com/IBM/diveye)
- [HuggingFace Space](https://huggingface.co/spaces/pinyuchen/Diveye_AI_text_detector)
- [ICML 2025 Workshop](https://icml.cc/virtual/2025/51028)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_diveye_citation_verify_20260514T195449"
}
```

</details>

---
