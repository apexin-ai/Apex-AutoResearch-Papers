# paper research lit vla efficiency

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_paper_research_lit_vla_efficiency_20260518T015546.jsonl`
- **Structured JSON:** [`33e81bc60362901d76c1.json`](../../sessions/33/33e81bc60362901d76c1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-18T01:57:33.278450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T01:57:33.278905+00:00_

1	# Literature Map — importance_margin_vla_compress
2	# Generated: 2026-05-17
3	# Citation budget: 35
4	
5	papers:
6	
7	  # ============================================================
8	  # Cluster: VLA Models (target: 6)
9	  # ============================================================
10	  - bibtex_key: shukor2025smolvla
11	    title: "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics"
12	    authors: "Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others"
13	    year: 2025
14	    venue: "arXiv preprint"
15	    arxiv_id: "2506.01844"
16	    category: "VLA Models"
17	    role: foundation
18	    verified: true
19	    key_finding: "450M-param VLA combining compact VLM (SigLIP+Qwen2) with flow matching action expert; 87.3% SR on LIBERO with batch size 64."
20	    pruning_stats: null
21	    notes: "Our experimental platform. SigLIP encoder produces 128 vision tokens."
22	
23	  - bibtex_key: kim2024openvla
24	    title: "OpenVLA: An Open-Source Vision-Language-Action Model"
25	    authors: "Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others"
26	    year: 2024
27	    venue: "CoRL 2024"
28	    arxiv_id: "2406.09246"
29	    category: "VLA Models"
30	    role: foundation
31	    verified: true
32	    key_finding: "7B-param open-source VLA trained on 970K episodes from Open X-Embodiment; supports parameter-efficient fine-tuning."
33	
34	  - bibtex_key: zitkovich2023rt2
35	    title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
36	    authors: "Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others"
37	    year: 2023
38	    venue: "CoRL 2023"
39	    arxiv_id: "2307.15818"
40	    category: "VLA Models"
41	    role: foundation
42	    verified: true
43	    key_finding: "Co-fine-tunes VLM on robotic trajectory data; actions expressed as text tokens; emergent semantic reasoning via chain of thought."
44	
45	  - bibtex_key: ghosh2024octo
46	    title: "Octo: An Open-Source Generalist R
…[truncated 16496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T01:57:33.279153+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport urllib.request, urllib.parse, json\n\ndef search_s2(query, limit=5):\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit={limit}&fields=title,authors,year,venue,externalIds,abstract'\n    req = urllib.request.Request(url)\n    with urllib.request.urlopen(req, timeout=15) as resp:\n        return json.loads(resp.read())\n\n# Search 1: EfficientVLA\nresults = search_s2('EfficientVLA efficient vision language action model', 5)\nprint('=== EfficientVLA ===')\nfor p in results.get('data', []):\n    print(json.dumps({'title': p['title'], 'year': p.get('year'), 'venue': p.get('venue'), 'arxiv': p.get('externalIds', {}).get('ArXiv'), 'authors': [a['name'] for a in p.get('authors', [])[:3]]}, indent=2))\n    print()\n\"\n",
  "description": "Search Semantic Scholar for EfficientVLA",
  "timeout": "20000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport urllib.request, urllib.parse, json\n\ndef search_s2(query, limit=5):\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit={limit}&fields=title,authors,year,venue,externalIds,abstract'\n    req = urllib.request.Request(url)\n    with urllib.request.urlopen(req, timeout=15) as resp:\n        return json.loads(resp.read())\n\n# Search 1: EfficientVLA\nresults = search_s2('EfficientVLA efficient vision language action model', 5)\nprint('=== EfficientVLA ===')\nfor p in results.get('data', []):\n    print(json.dumps({'title': p['title'], 'year': p.get('year'), 'venue': p.get('venue'), 'arxiv': p.get('externalIds', {}).get('ArXiv'), 'authors': [a['name'] for a in p.get('authors', [])[:3]]}, indent=2))\n    print()\n\"\n",
    "description": "Search Semantic Scholar for EfficientVLA",
    "timeout": "20000"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T01:57:33.279339+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 11, in &lt;module>
    results = search_s2('EfficientVLA efficient vision language action model', 5)
  File "&lt;string>", line 7, in search_s2
    with urllib.request.urlopen(req, timeout=15) as resp:
         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/urllib/request.py", line 187, in urlopen
    return opener.open(url, data, timeout)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/urllib/request.py", line 493, in open
    response = meth(req, response)
  File "/usr/lib/python3.14/urllib/request.py", line 602, in http_response
    response = self.parent.error(
        'http', request, response, code, msg, hdrs)
  File "/usr/lib/python3.14/urllib/request.py", line 531, in error
    return self._call_chain(*args)
           ~~~~~~~~~~~~~~~~^^^^^^^
  File "/usr/lib/python3.14/urllib/request.py", line 464, in _call_chain
    result = func(*args)
  File "/usr/lib/python3.14/urllib/request.py", line 611, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 429:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T01:57:33.279491+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport urllib.request, urllib.parse, json\n\ndef search_s2(query, limit=5):\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit={limit}&fields=title,authors,year,venue,externalIds,abstract'\n    req = urllib.request.Request(url)\n    with urllib.request.urlopen(req, timeout=15) as resp:\n        return json.loads(resp.read())\n\n# Search 2: VLA-Pruner\nresults = search_s2('VLA-Pruner temporal aware pruning vision language action', 5)\nprint('=== VLA-Pruner ===')\nfor p in results.get('data', []):\n    print(json.dumps({'title': p['title'], 'year': p.get('year'), 'venue': p.get('venue'), 'arxiv': p.get('externalIds', {}).get('ArXiv'), 'authors': [a['name'] for a in p.get('authors', [])[:3]]}, indent=2))\n    print()\n\"\n",
  "description": "Search Semantic Scholar for VLA-Pruner",
  "timeout": "20000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport urllib.request, urllib.parse, json\n\ndef search_s2(query, limit=5):\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit={limit}&fields=title,authors,year,venue,externalIds,abstract'\n    req = urllib.request.Request(url)\n    with urllib.request.urlopen(req, timeout=15) as resp:\n        return json.loads(resp.read())\n\n# Search 2: VLA-Pruner\nresults = search_s2('VLA-Pruner temporal aware pruning vision language action', 5)\nprint('=== VLA-Pruner ===')\nfor p in results.get('data', []):\n    print(json.dumps({'title': p['title'], 'year': p.get('year'), 'venue': p.get('venue'), 'arxiv': p.get('externalIds', {}).get('ArXiv'), 'authors': [a['name'] for a in p.get('authors', [])[:3]]}, indent=2))\n    print()\n\"\n",
    "description": "Search Semantic Scholar for VLA-Pruner",
    "timeout": "20000"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T01:57:33.279627+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
import urllib.request, urll…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T01:57:33.279754+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport urllib.request, urllib.parse, json\n\ndef search_s2(query, limit=5):\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit={limit}&fields=title,authors,year,venue,externalIds,abstract'\n    req = urllib.request.Request(url)\n    with urllib.request.urlopen(req, timeout=15) as resp:\n        return json.loads(resp.read())\n\n# Search 3: LLaVA-PruMerge or VLM token pruning merging\nresults = search_s2('LLaVA-PruMerge visual token pruning merging', 5)\nprint('=== LLaVA-PruMerge ===')\nfor p in results.get('data', []):\n    print(json.dumps({'title': p['title'], 'year': p.get('year'), 'venue': p.get('venue'), 'arxiv': p.get('externalIds', {}).get('ArXiv'), 'authors': [a['name'] for a in p.get('authors', [])[:3]]}, indent=2))\n    print()\n\"\n",
  "description": "Search Semantic Scholar for LLaVA-PruMerge",
  "timeout": "20000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport urllib.request, urllib.parse, json\n\ndef search_s2(query, limit=5):\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit={limit}&fields=title,authors,year,venue,externalIds,abstract'\n    req = urllib.request.Request(url)\n    with urllib.request.urlopen(req, timeout=15) as resp:\n        return json.loads(resp.read())\n\n# Search 3: LLaVA-PruMerge or VLM token pruning merging\nresults = search_s2('LLaVA-PruMerge visual token pruning merging', 5)\nprint('=== LLaVA-PruMerge ===')\nfor p in results.get('data', []):\n    print(json.dumps({'title': p['title'], 'year': p.get('year'), 'venue': p.get('venue'), 'arxiv': p.get('externalIds', {}).get('ArXiv'), 'authors': [a['name'] for a in p.get('authors', [])[:3]]}, indent=2))\n    print()\n\"\n",
    "description": "Search Semantic Scholar for LLaVA-PruMerge",
    "timeout": "20000"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T01:57:33.279882+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
import urllib.request, urll…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T01:57:33.280012+00:00_

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
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
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

_source line 10 · 2026-05-18T01:57:33.280128+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T01:57:33.280288+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EfficientVLA vision language action model pruning caching 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EfficientVLA vision language action model pruning caching 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T01:57:33.280404+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA-Pruner temporal aware dual level pruning vision language action 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA-Pruner temporal aware dual level pruning vision language action 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T01:57:33.280515+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLaVA-PruMerge adaptive token reduction large multimodal models arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLaVA-PruMerge adaptive token reduction large multimodal models arxiv"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T01:57:33.280654+00:00_

Web search results for query: "VLA-Pruner temporal aware dual level pruning vision language action 2025 arxiv"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449v1"},{"title":"[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/abs/2509.05614"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614v1"},{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/html/2509.22093v1"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"}]

Based on the search results, I found the paper you're looking for. Here's the information about VLA-Pruner:

## VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning

VLA-Pruner is a paper titled "Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference", published on arXiv with ID 2511.16449.

### Key Asp
…[truncated 1132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T01:57:33.280815+00:00_

Web search results for query: "LLaVA-PruMerge adaptive token reduction large multimodal models arxiv"

Links: [{"title":"[2403.15388] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/pdf/2403.15388"},{"title":"[2403.15388v5] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v5"},{"title":"[2403.15388v4] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v4"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/llava-prumerge-adaptive-token-reduction-efficient-large"},{"title":"Rethinking Token Reduction in MLLMs: Towards a Unified Paradigm for Training-Free Acceleration","url":"https://arxiv.org/html/2411.17686v1"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models - Paper Detail","url":"https://deeplearn.org/arxiv/472288/llava-prumerge:-adaptive-token-reduction-for-efficient-large-multimodal-models"},{"title":"PAR: Prompt-Aware Token Reduction Method for Efficient Large Multimodal Models","url":"https://arxiv.org/html/2410.07278v2"},{"title":"Towards Adaptive Visual Token Pruning for Large Multimodal Models","url":"https://arxiv.org/html/2509.00320v1"},{"title":"AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning","url":"https://arxiv.org/html/2412.03248v1"}]

I found the research paper you're looking for. Here's a summary of the search results:

## LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models

Large Multimodal Models (LMMs) have shown significant visual reasoning capabilities by connecting a visual encoder and a large language model, and typical
…[truncated 980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T01:57:33.280979+00:00_

Web search results for query: "EfficientVLA vision language action model pruning caching 2025 arxiv"

Links: [{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614v1"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v2"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/html/2511.18960v1"}]

I found comprehensive information about EfficientVLA and related research on Vision-Language-Action (VLA) model optimization. Here are the key findings:

## EfficientVLA Overview

EfficientVLA is a novel training-free, structured inference acceleration framework that synergistically prunes redundant layers from the language module based on their informational impact and strategically selects a compact, task-focused subset o
…[truncated 1580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T01:57:33.281129+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2506.10100 EfficientVLA authors CogACT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2506.10100 EfficientVLA authors CogACT"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T01:57:33.281308+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2403.15388 LLaVA-PruMerge authors Yuzhang Shang venue 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2403.15388 LLaVA-PruMerge authors Yuzhang Shang venue 2024"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T01:57:33.281469+00:00_

Web search results for query: "arxiv 2506.10100 EfficientVLA authors CogACT"

Links: [{"title":"[2506.10100] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100"},{"title":"Paper page - EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/html/2411.19650v1"},{"title":"[PDF] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CogACT:-A-Foundational-Vision-Language-Action-Model-Li-Liang/54caf5927a6d656bb84d2a16e16fa2b0c5d6f522"},{"title":"README.md · CogACT/CogACT-Small at 8afbf8b0b3ab13fe6bb08d17c6f5956218d45e8d","url":"https://huggingface.co/CogACT/CogACT-Small/blob/8afbf8b0b3ab13fe6bb08d17c6f5956218d45e8d/README.md"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://vla-cache.github.io/"},{"title":"[2411.19650] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650"},{"title":"RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.17811"}]

Based on the search results, I found the paper arxiv 2506.10100 with information about EfficientVLA and CogACT:

## Paper: EfficientVLA (arxiv 2506.10100)

The authors are: Yantai Yang, Yuhao Wang, Zichen 
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T01:57:33.281632+00:00_

Web search results for query: "arxiv 2403.15388 LLaVA-PruMerge authors Yuzhang Shang venue 2024"

Links: [{"title":"[2403.15388] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/pdf/2403.15388"},{"title":"[Paper Review] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://velog.io/@euisuk-chung/LLaVA-PruMerge-Adaptive-Token-Reduction-for-Efficient-Large-Multimodal-Models"},{"title":"Figure 2 from LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLaVA-PruMerge:-Adaptive-Token-Reduction-for-Large-Shang-Cai/c0ef72d02b93065e77c506e23ce9acbbcd945893/figure/2"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient ...","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2403.15388"},{"title":"dblp: LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models.","url":"https://dblp.org/rec/journals/corr/abs-2403-15388.html"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Shang_LLaVA-PruMerge_Adaptive_Token_Reduction_for_Efficient_Large_Multimodal_Models_ICCV_2025_paper.html"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/llava-prumerge-adaptive-token-reduction-efficient-large"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient ...","url":"https://arxiv.org/pdf/2403.15388v4"},{"title":"arXiv:2409.10994v3 [cs.CL] 17 Dec 2024","url":"https://arxiv.org/pdf/2409.10994"}]

Based on the search results, here's the information about arxiv paper 2403.15388:

**Paper Title:** LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models

**A
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T01:57:33.281799+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2511.16449 VLA-Pruner authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2511.16449 VLA-Pruner authors"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T01:57:33.281932+00:00_

Web search results for query: "arxiv 2511.16449 VLA-Pruner authors"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"Computer Vision and Pattern Recognition 2025","url":"https://www.arxiv.org/list/cs.CV/2025?skip=24300&show=50"},{"title":"Computer Science Nov 2025","url":"https://arxiv.org/list/cs/2025-11?skip=7900"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"[2511.09516] MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation","url":"https://arxiv.org/abs/2511.09516"},{"title":"[2511.10518] SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.10518"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.14148v1"},{"title":"[2512.02700] VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm","url":"https://arxiv.org/abs/2512.02700"},{"title":"[2511.05397v1] EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation","url":"https://arxiv.org/abs/2511.05397v1"}]

Based on the search results, the authors of arXiv paper 2511.16449 "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference" are: Ziyan Liu, Yeqiu Chen, Hongyi Cai, Tao Lin, Shuo Yang, Zheng Liu, and Bo Zhao.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T01:57:33.282085+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
  "old_string": "  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"",
  "new_string": "  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"\n\n  - bibtex_key: yang2025efficientvla\n    title: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\"\n    authors: \"Yang, Yantai and Wang, Yuhao and Wen, Zichen and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.10100\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Synergistic layer pruning + task-aware visual token selection + temporal caching on CogACT (7B); 1.93x speedup with 0.6% SR drop on SIMPLER.\"\n    notes: \"Combines three orthogonal efficiency strategies. Uses CogACT not SmolVLA. Layer pruning and temporal caching are complementary to our token-level analysis.\"\n\n  - bibtex_key: liu2025vlapruner\n    title: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\"\n    authors: \"Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2511.16449\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Dual-level importance criterion combining prefill attention (semantic) and temporally-smoothed action decode attention for VLA token pruning.\"\n    notes: \"VLA-specific pruning exploiting temporal continuity. Directly relevant as it separates semantic vs action-level token importance.\"\n\n  - bibtex_key: shang2024prumerge\n    title: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\"\n    authors: \"Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan\"\n    year: 2024\n    venue: \"ICCV 2025\"\n    arxiv_id: \"2403.15388\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Adaptive visual token pruning + merging for LMMs; reduces tokens by 4x (to 5.5% with PruMerge) with comparable performance on VQA/reasoning tasks.\"\n    notes: \"VLM token reduction via CLS attention importance + similarity-based merging. Establishes prune-then-merge paradigm for visual tokens in VLMs.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
    "old_string": "  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"",
    "new_string": "  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"\n\n  - bibtex_key: yang2025efficientvla\n    title: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\"\n    authors: \"Yang, Yantai and Wang, Yuhao and Wen, Zichen and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.10100\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Synergistic layer pruning + task-aware visual token selection + temporal caching on CogACT (7B); 1.93x speedup with 0.6% SR drop on SIMPLER.\"\n    notes: \"Combines three orthogonal efficiency strategies. Uses CogACT not SmolVLA. Layer pruning and temporal caching are complementary to our token-level analysis.\"\n\n  - bibtex_key: liu2025vlapruner\n    title: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\"\n    authors: \"Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2511.16449\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Dual-level importance criterion combining prefill attention (semantic) and temporally-smoothed action decode attention for VLA token pruning.\"\n    notes: \"VLA-specific pruning exploiting temporal continuity. Directly relevant as it separates semantic vs action-level token importance.\"\n\n  - bibtex_key: shang2024prumerge\n    title: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\"\n    authors: \"Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan\"\n    year: 2024\n    venue: \"ICCV 2025\"\n    arxiv_id: \"2403.15388\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Adaptive visual token pruning + merging for LMMs; reduces tokens by 4x (to 5.5% with PruMerge) with comparable performance on VQA/reasoning tasks.\"\n    notes: \"VLM token reduction via CLS attention importance + similarity-based merging. Establishes prune-then-merge paradigm for visual tokens in VLMs.\""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T01:57:33.282352+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-18T01:57:33.282519+00:00_

已完成。在 `wang2026vlaiap` 后追加了 3 篇论文：

1. **yang2025efficientvla** — EfficientVLA (arXiv 2506.10100): 层剪枝 + token 选择 + 时序缓存，CogACT 上 1.93x 加速
2. **liu2025vlapruner** — VLA-Pruner (arXiv 2511.16449): 双层级 (语义 + 动作注意力) 时序感知 token 剪枝
3. **shang2024prumerge** — LLaVA-PruMerge (arXiv 2403.15388, ICCV 2025): 自适应视觉 token 剪枝 + 合并，4x token 压缩

"VLM/LLM Token Efficiency" cluster 现有 8 篇 (原 5 + 新增 3)，达到 target。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_lit_vla_efficiency_20260518T015546"
}
```

</details>

---
