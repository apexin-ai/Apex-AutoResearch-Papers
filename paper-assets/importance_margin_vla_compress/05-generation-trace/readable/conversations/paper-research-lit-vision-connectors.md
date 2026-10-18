# paper research lit vision connectors

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_research_lit_vision_connectors_20260518T013731.jsonl`
- **Structured JSON:** [`4ba9277f78663043c5e4.json`](../../sessions/4b/4ba9277f78663043c5e4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-18T01:40:44.920153+00:00_

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
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T01:40:44.920785+00:00_

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
…[truncated 11747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T01:40:44.921120+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport urllib.request, urllib.parse, json, time\n\nqueries = [\n    ('BLIP-2', 'BLIP-2 Bootstrapping Language-Image Pre-Training Generative Li 2023'),\n    ('Flamingo', 'Flamingo visual language model Alayrac 2022'),\n    ('LLaVA', 'LLaVA visual instruction tuning Liu 2024'),\n    ('PixelShuffle', 'Real-Time Single Image Video Super-Resolution Efficient Sub-Pixel Convolutional Neural Network Shi 2016'),\n    ('InternVL', 'InternVL scaling up vision foundation models Chen 2024'),\n    ('DINOv2', 'DINOv2 learning robust visual features without supervision Oquab 2024'),\n]\n\nresults = {}\nfor name, query in queries:\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit=3&fields=title,authors,year,venue,externalIds,abstract'\n    try:\n        req = urllib.request.Request(url)\n        with urllib.request.urlopen(req, timeout=15) as resp:\n            data = json.loads(resp.read())\n            results[name] = data.get('data', [])\n    except Exception as e:\n        results[name] = f'ERROR: {e}'\n    time.sleep(1.5)  # rate limit\n\nfor name, papers in results.items():\n    print(f'\\\\n=== {name} ===')\n    if isinstance(papers, str):\n        print(papers)\n        continue\n    for p in papers[:2]:\n        authors = ', '.join([a['name'] for a in (p.get('authors') or [])[:3]])\n        arxiv = (p.get('externalIds') or {}).get('ArXiv', 'N/A')\n        print(f\\\"  Title: {p.get('title')}\\\")\n        print(f\\\"  Authors: {authors}\\\")\n        print(f\\\"  Year: {p.get('year')}, Venue: {p.get('venue')}\\\")\n        print(f\\\"  ArXiv: {arxiv}\\\")\n        print(f\\\"  Abstract: {(p.get('abstract') or '')[:200]}\\\")\n        print()\n\"\n",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport urllib.request, urllib.parse, json, time\n\nqueries = [\n    ('BLIP-2', 'BLIP-2 Bootstrapping Language-Image Pre-Training Generative Li 2023'),\n    ('Flamingo', 'Flamingo visual language model Alayrac 2022'),\n    ('LLaVA', 'LLaVA visual instruction tuning Liu 2024'),\n    ('PixelShuffle', 'Real-Time Single Image Video Super-Resolution Efficient Sub-Pixel Convolutional Neural Network Shi 2016'),\n    ('InternVL', 'InternVL scaling up vision foundation models Chen 2024'),\n    ('DINOv2', 'DINOv2 learning robust visual features without supervision Oquab 2024'),\n]\n\nresults = {}\nfor name, query in queries:\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit=3&fields=title,authors,year,venue,externalIds,abstract'\n    try:\n        req = urllib.request.Request(url)\n        with urllib.request.urlopen(req, timeout=15) as resp:\n            data = json.loads(resp.read())\n            results[name] = data.get('data', [])\n    except Exception as e:\n        results[name] = f'ERROR: {e}'\n    time.sleep(1.5)  # rate limit\n\nfor name, papers in results.items():\n    print(f'\\\\n=== {name} ===')\n    if isinstance(papers, str):\n        print(papers)\n        continue\n    for p in papers[:2]:\n        authors = ', '.join([a['name'] for a in (p.get('authors') or [])[:3]])\n        arxiv = (p.get('externalIds') or {}).get('ArXiv', 'N/A')\n        print(f\\\"  Title: {p.get('title')}\\\")\n        print(f\\\"  Authors: {authors}\\\")\n        print(f\\\"  Year: {p.get('year')}, Venue: {p.get('venue')}\\\")\n        print(f\\\"  ArXiv: {arxiv}\\\")\n        print(f\\\"  Abstract: {(p.get('abstract') or '')[:200]}\\\")\n        print()\n\"\n",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T01:40:44.921491+00:00_

=== BLIP-2 ===
ERROR: HTTP Error 429: 

=== Flamingo ===
ERROR: HTTP Error 429: 

=== LLaVA ===
ERROR: HTTP Error 429: 

=== PixelShuffle ===
ERROR: HTTP Error 429: 

=== InternVL ===
  Title: Many-Shot In-Context Learning in Multimodal Foundation Models
  Authors: Yixing Jiang, Jeremy Irvin, Ji Wang
  Year: 2024, Venue: arXiv.org
  ArXiv: 2405.09798
  Abstract: Large language models are effective at few-shot in-context learning (ICL). Recent advancements in multimodal foundation models have enabled unprecedentedly long context windows, presenting an opportun

  Title: Yi: Open Foundation Models by 01.AI
  Authors: 01.AI Alex Young, Bei Chen, Chao Li
  Year: 2024, Venue: arXiv.org
  ArXiv: 2403.04652
  Abstract: We introduce the Yi model family, a series of language and multimodal models that demonstrate strong multi-dimensional capabilities. The Yi model family is based on 6B and 34B pretrained language mode


=== DINOv2 ===
ERROR: HTTP Error 429:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T01:40:44.921779+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport urllib.request, urllib.parse, json, time\n\nqueries = [\n    ('BLIP-2', 'BLIP-2 Bootstrapping Language-Image Pre-Training Generative Li 2023'),\n    ('Flamingo', 'Flamingo visual language model Alayrac 2022'),\n    ('LLaVA', 'LLaVA visual instruction tuning Liu 2024'),\n]\n\nresults = {}\nfor name, query in queries:\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit=3&fields=title,authors,year,venue,externalIds,abstract'\n    try:\n        req = urllib.request.Request(url)\n        with urllib.request.urlopen(req, timeout=15) as resp:\n            data = json.loads(resp.read())\n            results[name] = data.get('data', [])\n    except Exception as e:\n        results[name] = f'ERROR: {e}'\n    time.sleep(4)\n\nfor name, papers in results.items():\n    print(f'\\\\n=== {name} ===')\n    if isinstance(papers, str):\n        print(papers)\n        continue\n    for p in papers[:2]:\n        authors = ', '.join([a['name'] for a in (p.get('authors') or [])[:5]])\n        arxiv = (p.get('externalIds') or {}).get('ArXiv', 'N/A')\n        print(f\\\"  Title: {p.get('title')}\\\")\n        print(f\\\"  Authors: {authors}\\\")\n        print(f\\\"  Year: {p.get('year')}, Venue: {p.get('venue')}\\\")\n        print(f\\\"  ArXiv: {arxiv}\\\")\n        print(f\\\"  Abstract: {(p.get('abstract') or '')[:200]}\\\")\n        print()\n\" 2>&1\n",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport urllib.request, urllib.parse, json, time\n\nqueries = [\n    ('BLIP-2', 'BLIP-2 Bootstrapping Language-Image Pre-Training Generative Li 2023'),\n    ('Flamingo', 'Flamingo visual language model Alayrac 2022'),\n    ('LLaVA', 'LLaVA visual instruction tuning Liu 2024'),\n]\n\nresults = {}\nfor name, query in queries:\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit=3&fields=title,authors,year,venue,externalIds,abstract'\n    try:\n        req = urllib.request.Request(url)\n        with urllib.request.urlopen(req, timeout=15) as resp:\n            data = json.loads(resp.read())\n            results[name] = data.get('data', [])\n    except Exception as e:\n        results[name] = f'ERROR: {e}'\n    time.sleep(4)\n\nfor name, papers in results.items():\n    print(f'\\\\n=== {name} ===')\n    if isinstance(papers, str):\n        print(papers)\n        continue\n    for p in papers[:2]:\n        authors = ', '.join([a['name'] for a in (p.get('authors') or [])[:5]])\n        arxiv = (p.get('externalIds') or {}).get('ArXiv', 'N/A')\n        print(f\\\"  Title: {p.get('title')}\\\")\n        print(f\\\"  Authors: {authors}\\\")\n        print(f\\\"  Year: {p.get('year')}, Venue: {p.get('venue')}\\\")\n        print(f\\\"  ArXiv: {arxiv}\\\")\n        print(f\\\"  Abstract: {(p.get('abstract') or '')[:200]}\\\")\n        print()\n\" 2>&1\n",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T01:40:44.922053+00:00_

=== BLIP-2 ===
ERROR: HTTP Error 429: 

=== Flamingo ===
ERROR: HTTP Error 429: 

=== LLaVA ===
ERROR: HTTP Error 429:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T01:40:44.922334+00:00_

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
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
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

_source line 8 · 2026-05-18T01:40:44.922547+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T01:40:44.922783+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "BLIP-2 Bootstrapping Language-Image Pre-Training Generative arxiv Li Junnan 2023 ICML",
  "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "BLIP-2 Bootstrapping Language-Image Pre-Training Generative arxiv Li Junnan 2023 ICML",
    "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T01:40:44.922994+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Flamingo visual language model Alayrac 2022 NeurIPS Perceiver Resampler arxiv",
  "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Flamingo visual language model Alayrac 2022 NeurIPS Perceiver Resampler arxiv",
    "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T01:40:44.923218+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLaVA Visual Instruction Tuning Liu Haotian 2024 NeurIPS arxiv",
  "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLaVA Visual Instruction Tuning Liu Haotian 2024 NeurIPS arxiv",
    "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T01:40:44.923436+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Real-Time Single Image Video Super-Resolution Efficient Sub-Pixel Convolutional Neural Network Shi 2016 CVPR pixel shuffle arxiv",
  "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Real-Time Single Image Video Super-Resolution Efficient Sub-Pixel Convolutional Neural Network Shi 2016 CVPR pixel shuffle arxiv",
    "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T01:40:44.923650+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InternVL scaling vision foundation model pixel shuffle connector Chen Zhe 2024 arxiv",
  "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InternVL scaling vision foundation model pixel shuffle connector Chen Zhe 2024 arxiv",
    "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T01:40:44.923858+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DINOv2 Learning Robust Visual Features without Supervision Oquab 2024 TMLR arxiv",
  "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DINOv2 Learning Robust Visual Features without Supervision Oquab 2024 TMLR arxiv",
    "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T01:40:44.924117+00:00_

Web search results for query: "BLIP-2 Bootstrapping Language-Image Pre-Training Generative arxiv Li Junnan 2023 ICML"

Links: [{"title":"[2301.12597] BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models","url":"https://arxiv.org/abs/2301.12597"},{"title":"[PDF] BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BLIP-2:-Bootstrapping-Language-Image-Pre-training-Li-Li/3f5b31c4f7350dc88002c121aecbdc82f86eb5bb"},{"title":"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models","url":"https://arxiv.org/html/2301.12597"},{"title":"[2201.12086] BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation","url":"https://arxiv.org/abs/2201.12086"},{"title":"BLIP: Bootstrapping Language-Image Pre-training for ...","url":"https://arxiv.org/pdf/2201.12086"},{"title":"BLIP-2: Bootstrapping Language-Image Pre-training with ...","url":"https://arxiv.org/pdf/2301.12597"},{"title":"[PDF] BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BLIP:-Bootstrapping-Language-Image-Pre-training-for-Li-Li/a3b42a83669998f65df60d7c065a70d07ca95e99"},{"title":"[2301.12597v1] BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models","url":"https://arxiv.org/abs/2301.12597v1"},{"title":"[2301.12597v3] BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models","url":"https://arxiv.org/abs/2301.12597v3"},{"title":"[2201.12086v2] BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation","url":"https://arxiv.org/abs/2201.12086v2"}]

I've found information about BLIP-2. Here are the key findings
…[truncated 1376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T01:40:44.924444+00:00_

Web search results for query: "Flamingo visual language model Alayrac 2022 NeurIPS Perceiver Resampler arxiv"

Links: [{"title":"[2204.14198] Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://arxiv.org/abs/2204.14198"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2204.14198"},{"title":"Figure 5 from Flamingo: a Visual Language Model for Few-Shot Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Flamingo:-a-Visual-Language-Model-for-Few-Shot-Alayrac-Donahue/26218bdcc3945c7edae7aa2adbfba4cd820a2df3/figure/8"},{"title":"Visual Anchors Are Strong Information Aggregators For Multimodal Large Language Model","url":"https://arxiv.org/html/2405.17815"},{"title":"LLaVA-SP: Enhancing Visual Representation with Visual Spatial Tokens for MLLMs","url":"https://arxiv.org/html/2507.00505v3"},{"title":"Re-ViLM: Retrieval-Augmented Visual Language Model for","url":"https://arxiv.org/pdf/2302.04858"},{"title":"[2204.14198] Flamingo: a Visual Language Model for Few-Shot Learning","url":"http://export.arxiv.org/abs/2204.14198"},{"title":"Lost in Space: Probing Fine-grained Spatial Understanding in Vision and Language Resamplers","url":"https://arxiv.org/html/2404.13594"},{"title":"AlignVLM: Bridging Vision and Language Latent Spaces for Multimodal Understanding","url":"https://arxiv.org/html/2502.01341v1"},{"title":"[PDF] Flamingo: a Visual Language Model for Few-Shot Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Flamingo:-a-Visual-Language-Model-for-Few-Shot-Alayrac-Donahue/26218bdcc3945c7edae7aa2adbfba4cd820a2df3"}]

Perfect! I found comprehensive information about the Flamingo visual language model. Here's what the search results show:

## Flamingo: Visual Language Model for Few-Shot Learning

Flamingo, authored by Jean-Baptiste Alayrac and colleagues, is a family of Visual Language Models (VLM) designed for few-shot learning.

### Key Contributions

The model proposes key architectural innovations to: (i) br
…[truncated 1069 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T01:40:44.924717+00:00_

Web search results for query: "LLaVA Visual Instruction Tuning Liu Haotian 2024 NeurIPS arxiv"

Links: [{"title":"[2304.08485] Visual Instruction Tuning","url":"https://arxiv.org/abs/2304.08485"},{"title":"Visual Instruction Tuning","url":"https://arxiv.org/pdf/2304.08485"},{"title":"[2310.03744] Improved Baselines with Visual Instruction Tuning","url":"https://arxiv.org/abs/2310.03744"},{"title":"[PDF] Visual Instruction Tuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Visual-Instruction-Tuning-Liu-Li/a5036f31f0e629dc661f120b8c3b1f374d479ab8"},{"title":"Improved Baselines with Visual Instruction Tuning Haotian Liu1 Chunyuan Li2","url":"https://arxiv.org/pdf/2310.03744"},{"title":"[2310.03744v2] Improved Baselines with Visual Instruction Tuning","url":"https://arxiv.org/abs/2310.03744v2"},{"title":"[2310.03744v1] Improved Baselines with Visual Instruction Tuning","url":"https://arxiv.org/abs/2310.03744v1"},{"title":"[2304.08485v2] Visual Instruction Tuning","url":"https://arxiv.org/abs/2304.08485v2"},{"title":"Improved Baselines with Visual Instruction Tuning","url":"https://arxiv.org/html/2310.03744v2"},{"title":"Learning to Instruct for Visual Instruction Tuning","url":"https://arxiv.org/html/2503.22215v1"}]

Based on the search results, I found relevant information about the LLaVA Visual Instruction Tuning paper:

The paper "Visual Instruction Tuning" was authored by Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee and was published at NeurIPS in 2023.

The paper is available on arxiv as paper 2304.08485. The original version was submitted on April 17, 2023, with updates through December 11, 2023.

The paper presents LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an LLM for general-purpose visual and language understanding, using the first attempt to leverage language-only GPT-4 to generate multimodal language-image instruction-following data.


REMINDER: Yo
…[truncated 88 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T01:40:44.925017+00:00_

Web search results for query: "Real-Time Single Image Video Super-Resolution Efficient Sub-Pixel Convolutional Neural Network Shi 2016 CVPR pixel shuffle arxiv"

Links: [{"title":"[1609.05158] Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network","url":"https://arxiv.org/abs/1609.05158"},{"title":"[PDF] Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Real-Time-Single-Image-and-Video-Super-Resolution-Shi-Caballero/03a5b2aac53443e6078f0f63b35d4f95d6d54c5d"},{"title":"Figure 1 from Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Real-Time-Single-Image-and-Video-Super-Resolution-Shi-Caballero/03a5b2aac53443e6078f0f63b35d4f95d6d54c5d/figure/0"},{"title":"Real-Time Single Image and Video Super-Resolution Using an Efﬁcient","url":"https://arxiv.org/pdf/1609.05158"},{"title":"Figure 2 from Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Real-Time-Single-Image-and-Video-Super-Resolution-Shi-Caballero/03a5b2aac53443e6078f0f63b35d4f95d6d54c5d/figure/2"},{"title":"[1609.05158v2] Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network","url":"https://arxiv.org/abs/1609.05158v2"},{"title":"Real-Time Super-Resolution System of 4K-Video Based on Deep Learning","url":"https://arxiv.org/pdf/2107.05307"},{"title":"WaveMixSR-V2: Enhancing Super-resolution with Higher Efficiency","url":"https://arxiv.org/html/2409.10582"},{"title":"[1806.02658] SUPER-RESOLUTION USING CONVOLUTIONAL NEURAL NETWORKS WITHOUT ANY CHECKERBOARD ARTIFACTS","url":"https://ar5iv.labs.arxiv.org/html/1806.02658"},{"title":"Single Image Super-
…[truncated 1583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T01:40:44.925337+00:00_

Web search results for query: "InternVL scaling vision foundation model pixel shuffle connector Chen Zhe 2024 arxiv"

Links: [{"title":"[2312.14238] InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks","url":"https://arxiv.org/abs/2312.14238"},{"title":"InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks","url":"https://arxiv.org/html/2312.14238v3"},{"title":"InternVL: Scaling up Vision Foundation Models and Aligning","url":"https://arxiv.org/pdf/2312.14238"},{"title":"[2312.14238v3] InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks","url":"https://arxiv.org/abs/2312.14238v3"},{"title":"[2312.14238] InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks","url":"https://ar5iv.labs.arxiv.org/html/2312.14238"},{"title":"[PDF] Intern VL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/6a33e58ef961a3a0a5657518b2be86395eb7c8d0"},{"title":"Mini-InternVL: A Flexible-Transfer Pocket Multimodal Model with 5% Parameters and 90% Performance","url":"https://arxiv.org/html/2410.16261v2"},{"title":"Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling","url":"https://arxiv.org/html/2412.05271v1"},{"title":"[2412.05271] Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling","url":"https://arxiv.org/abs/2412.05271"},{"title":"InternVideo2: Scaling Foundation Models for Multimodal Video Understanding","url":"https://arxiv.org/html/2403.15377v4"}]

Based on the search results, I found information about the InternVL research by Zhe Chen and colleagues. Here are the key findings:

## InternVL: Scaling Vision Foundation Models

InternVL is a large-scale vision-language foundation model that scales up the vision founda
…[truncated 1314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T01:40:44.925624+00:00_

Web search results for query: "DINOv2 Learning Robust Visual Features without Supervision Oquab 2024 TMLR arxiv"

Links: [{"title":"[2304.07193] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193"},{"title":"DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/html/2304.07193v2"},{"title":"[PDF] DINOv2: Learning Robust Visual Features without Supervision | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DINOv2:-Learning-Robust-Visual-Features-without-Oquab-Darcet/5a9cb1b3dc4655218b3deeaf4a2417a9a8cd0891"},{"title":"[2304.07193v2] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193v2"},{"title":"[2304.07193v1] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193v1"},{"title":"DINOv2 Meets Text: A Unified Framework for Image- and Pixel-Level Vision-Language Alignment","url":"https://arxiv.org/html/2412.16334v1"},{"title":"Published in Transactions on Machine Learning Research (01/2024)","url":"https://arxiv.org/pdf/2304.07193"},{"title":"Upsampling DINOv2 features for unsupervised vision tasks and weakly supervised materials segmentation","url":"https://arxiv.org/html/2410.19836v1"},{"title":"FastDINOv2: Frequency Based Curriculum Learning Improves Robustness and Training Speed","url":"https://arxiv.org/html/2507.03779v1"},{"title":"LUDVIG: Learning-free Uplifting of 2D Visual features to Gaussian Splatting scenes","url":"https://arxiv.org/html/2410.14462v3"}]

I found the paper you're looking for! Here's what I discovered:

The paper "DINOv2: Learning Robust Visual Features without Supervision" was authored by Maxime Oquab, Timothée Darcet, and 24 other researchers, and it's available on arXiv with the identifier 2304.07193.

The paper was published in TMLR (Transactions on Machine Learning Research) in 2024. The work addresses breakthroughs in computer vision model pretraini
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T01:40:44.925906+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InternVL 1.5 pixel shuffle dynamic resolution token compression Chen 2024 arxiv",
  "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InternVL 1.5 pixel shuffle dynamic resolution token compression Chen 2024 arxiv",
    "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T01:40:44.926123+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLaVA 1.5 improved baselines visual instruction tuning MLP projector Liu 2024 arxiv 2310.03744",
  "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLaVA 1.5 improved baselines visual instruction tuning MLP projector Liu 2024 arxiv 2310.03744",
    "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T01:40:44.926411+00:00_

Web search results for query: "InternVL 1.5 pixel shuffle dynamic resolution token compression Chen 2024 arxiv"

Links: [{"title":"A Survey of Token Compression for Efficient Multimodal Large Language Models","url":"https://arxiv.org/html/2507.20198v5"},{"title":"InternVL-X: Advancing and Accelerating InternVL Series with Efficient Visual Token Compression","url":"https://arxiv.org/html/2503.21307v1"},{"title":"SmolVLM: Redefining small and efficient multimodal models","url":"https://arxiv.org/html/2504.05299v1"},{"title":"When Tokens Talk Too Much: A Survey of Multimodal Long-Context Token Compression across Images, Videos, and Audios","url":"https://arxiv.org/html/2507.20198v1"},{"title":"InternVL3.5: Advancing Open-Source Multimodal Models in Versatility, Reasoning, and Efficiency","url":"https://arxiv.org/html/2508.18265v1"},{"title":"Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors","url":"https://arxiv.org/html/2509.00969"},{"title":"TokenFLEX: Unified VLM Training for Flexible Visual Tokens Inference","url":"https://arxiv.org/html/2504.03154v1"},{"title":"LaCo: Efficient Layer-wise Compression of Visual Tokens ...","url":"https://arxiv.org/pdf/2507.02279"},{"title":"Token-Shuffle: Towards High-Resolution Image Generation with Autoregressive Models","url":"https://arxiv.org/html/2504.17789v2"},{"title":"A Glimpse to Compress: Dynamic Visual Token Pruning for Large Vision-Language Models","url":"https://arxiv.org/html/2508.01548v1"}]

Based on the search results, I found relevant information about InternVL 1.5 and its token compression techniques:

InternVL v1.5 uses 2×2 pixel-shuffle, reducing token counts fourfold while maintaining OCR capability. The Dynamic High Resolution strategy introduced in InternVL1.5 is retained in subsequent design iterations.

Pixel unshuffle is the inverse operation of pixel shuffle and transforms a feature map from a high spatial resolution with a small number of channels into a lower-res
…[truncated 755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T01:40:44.926694+00:00_

Web search results for query: "LLaVA 1.5 improved baselines visual instruction tuning MLP projector Liu 2024 arxiv 2310.03744"

Links: [{"title":"[2310.03744] Improved Baselines with Visual Instruction Tuning","url":"https://arxiv.org/abs/2310.03744"},{"title":"Improved Baselines with Visual Instruction Tuning","url":"https://arxiv.org/html/2310.03744v2"},{"title":"Improved Baselines with Visual Instruction Tuning Haotian Liu1 Chunyuan Li2","url":"https://arxiv.org/pdf/2310.03744"},{"title":"[2310.03744v1] Improved Baselines with Visual Instruction Tuning","url":"https://arxiv.org/abs/2310.03744v1"},{"title":"[2310.03744v2] Improved Baselines with Visual Instruction Tuning","url":"https://arxiv.org/abs/2310.03744v2"},{"title":"LLaVA-SP: Enhancing Visual Representation with Visual Spatial Tokens for MLLMs","url":"https://arxiv.org/html/2507.00505v3"},{"title":"[2304.08485] Visual Instruction Tuning","url":"https://arxiv.org/abs/2304.08485"},{"title":"1 Introduction","url":"https://arxiv.org/html/2601.03100"},{"title":"TG-LLaVA: Text Guided LLaVA via Learnable Latent EmbeddingsWork was done when D. Yan was an intern at Alibaba","url":"https://arxiv.org/html/2409.09564v2"},{"title":"LLaVA-UHD: an LMM Perceiving Any Aspect Ratio and High-Resolution Images","url":"https://arxiv.org/html/2403.11703v1"}]

I found the paper you're looking for. Here are the key details about the arxiv 2310.03744 paper:

The paper is titled "Improved Baselines with Visual Instruction Tuning" by Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee from the University of Wisconsin–Madison and Microsoft Research.

**Main Contributions:**

The paper demonstrates that the fully-connected vision-language cross-modal connector in LLaVA is surprisingly powerful and data-efficient.

The authors establish stronger baselines by using CLIP-ViT-L-336px with an MLP projection and adding academic-task-oriented VQA data with response formatting prompts, achieving state-of-the-art results across 11 benchmark
…[truncated 591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T01:40:44.926993+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InternVL 1.5 \"How Far Are We to GPT-4V\" Chen 2024 arxiv pixel unshuffle",
  "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InternVL 1.5 \"How Far Are We to GPT-4V\" Chen 2024 arxiv pixel unshuffle",
    "allowed_domains": "['arxiv.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T01:40:44.927286+00:00_

Web search results for query: "InternVL 1.5 "How Far Are We to GPT-4V" Chen 2024 arxiv pixel unshuffle"

Links: [{"title":"[2404.16821] How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites","url":"https://arxiv.org/abs/2404.16821"},{"title":"[2404.16821v1] How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites","url":"https://arxiv.org/abs/2404.16821v1"},{"title":"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites","url":"https://arxiv.org/html/2404.16821v1"},{"title":"How Far Are We to GPT-4V?","url":"https://arxiv.org/pdf/2404.16821"},{"title":"[PDF] How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Far-Are-We-to-GPT-4V-Closing-the-Gap-to-Models-Chen-Wang/887306ee7ebd9eebd7faea24106ec8e8f1a50987"},{"title":"Mini-InternVL: A Flexible-Transfer Pocket Multimodal Model with 5% Parameters and 90% Performance","url":"https://arxiv.org/html/2410.16261v3"},{"title":"InternVL-X: Advancing and Accelerating InternVL Series with Efficient Visual Token Compression","url":"https://arxiv.org/html/2503.21307v1"},{"title":"Mono-InternVL: Pushing the Boundaries of Monolithic Multimodal Large Language Models with Endogenous Visual Pre-training","url":"https://arxiv.org/html/2410.08202v1"},{"title":"V2PE: Improving Multimodal Long-Context Capability of Vision-Language Models with Variable Visual Position Encoding","url":"https://arxiv.org/html/2412.09616v2"},{"title":"CapArena: Benchmarking and Analyzing Detailed Image Captioning in the LLM Era","url":"https://arxiv.org/html/2503.12329v1"}]

I found the paper! Here are the search results for "InternVL 1.5: How Far Are We to GPT-4V" by Chen et al. (2024):

## Paper Overview

InternVL 1.5 is an open-source multimodal large language model (MLLM) designed to bridge the capability gap betwee
…[truncated 1430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T01:40:44.927629+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
  "old_string": "  - bibtex_key: lipman2023flow\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv_id: \"2210.02747\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling.\"\n    notes: \"Action generation mechanism in SmolVLA and pi0.\"",
  "new_string": "  - bibtex_key: lipman2023flow\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv_id: \"2210.02747\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling.\"\n    notes: \"Action generation mechanism in SmolVLA and pi0.\"\n\n  # ============================================================\n  # Cluster: Vision Connectors & Token Compression (target: 6)\n  # ============================================================\n  - bibtex_key: li2023blip2\n    title: \"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\"\n    authors: \"Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven\"\n    year: 2023\n    venue: \"ICML 2023\"\n    arxiv_id: \"2301.12597\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Querying Transformer (Q-Former) compresses visual tokens into fixed number of query tokens; outperforms Flamingo80B on zero-shot VQAv2 with 54x fewer trainable parameters.\"\n    notes: \"Exemplar of learned cross-attention compression for vision-language bridging. Our proposed cross-attention compression draws on this principle.\"\n\n  - bibtex_key: alayrac2022flamingo\n    title: \"Flamingo: a Visual Language Model for Few-Shot Learning\"\n    authors: \"Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others\"\n    year: 2022\n    venue: \"NeurIPS 2022\"\n    arxiv_id: \"2204.14198\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Perceiver Resampler maps variable-size spatio-temporal visual features to fixed number of output tokens via cross-attention with learnable queries.\"\n    notes: \"Another learned cross-attention connector. Together with BLIP-2, establishes the cross-attention connector paradigm that contrasts with MLP/pixel_shuffle approaches.\"\n\n  - bibtex_key: liu2023llava\n    title: \"Visual Instruction Tuning\"\n    authors: \"Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2304.08485\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear/MLP projection connects vision encoder to LLM; LLaVA-1.5 shows two-layer MLP projector is surprisingly effective and data-efficient.\"\n    notes: \"Key reference for the MLP projector approach used in OpenVLA. Our finding that MLP projector enables graceful degradation under token pruning connects to this design choice.\"\n\n  - bibtex_key: shi2016subpixel\n    title: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\"\n    authors: \"Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan\"\n    year: 2016\n    venue: \"CVPR 2016\"\n    arxiv_id: \"1609.05158\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"Introduces sub-pixel convolution (pixel shuffle) that rearranges spatial resolution and channel dimensions; enables real-time 1080p super-resolution.\"\n    notes: \"Origin of the pixel_shuffle operation adopted by SmolVLA and InternVL as vision connector. Central to our cliff-edge failure analysis.\"\n\n  - bibtex_key: chen2024internvl\n    title: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\"\n    authors: \"Chen, Zhe and Wang, Weiyun and Tian, Hao and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2404.16821\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"InternVL 1.5 uses 2x2 pixel unshuffle to compress 1024 visual tokens to 256 per tile; supports dynamic high-resolution up to 4K with up to 40 tiles.\"\n    notes: \"Another VLM using pixel_shuffle connector, confirming its adoption beyond SmolVLA. Strengthens generality of our cliff-edge finding.\"\n\n  - bibtex_key: oquab2024dinov2\n    title: \"DINOv2: Learning Robust Visual Features without Supervision\"\n    authors: \"Oquab, Maxime and Darcet, Timothee and Moutakanni, Theo and others\"\n    year: 2024\n    venue: \"TMLR 2024\"\n    arxiv_id: \"2304.07193\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Self-supervised ViT producing all-purpose visual features; scaled to ViT-g with curated LVD-142M dataset; strong transfer across tasks without finetuning.\"\n    notes: \"Vision encoder used in OpenVLA (DinoSigLIP). Its feature structure interacts with the MLP projector to determine token-level importance distribution.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
    "old_string": "  - bibtex_key: lipman2023flow\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv_id: \"2210.02747\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling.\"\n    notes: \"Action generation mechanism in SmolVLA and pi0.\"",
    "new_string": "  - bibtex_key: lipman2023flow\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv_id: \"2210.02747\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling.\"\n    notes: \"Action generation mechanism in SmolVLA and pi0.\"\n\n  # ============================================================\n  # Cluster: Vision Connectors & Token Compression (target: 6)\n  # ============================================================\n  - bibtex_key: li2023blip2\n    title: \"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\"\n    authors: \"Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven\"\n    year: 2023\n    venue: \"ICML 2023\"\n    arxiv_id: \"2301.12597\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Querying Transformer (Q-Former) compresses visual tokens into fixed number of query tokens; outperforms Flamingo80B on zero-shot VQAv2 with 54x fewer trainable parameters.\"\n    notes: \"Exemplar of learned cross-attention compression for vision-language bridging. Our proposed cross-attention compression draws on this principle.\"\n\n  - bibtex_key: alayrac2022flamingo\n    title: \"Flamingo: a Visual Language Model for Few-Shot Learning\"\n    authors: \"Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others\"\n    year: 2022\n    venue: \"NeurIPS 2022\"\n    arxiv_id: \"2204.14198\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Perceiver Resampler maps variable-size spatio-temporal visual features to fixed number of output tokens via cross-attention with learnable queries.\"\n    notes: \"Another learned cross-attention connector. Together with BLIP-2, establishes the cross-attention connector paradigm that contrasts with MLP/pixel_shuffle approaches.\"\n\n  - bibtex_key: liu2023llava\n    title: \"Visual Instruction Tuning\"\n    authors: \"Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2304.08485\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear/MLP projection connects vision encoder to LLM; LLaVA-1.5 shows two-layer MLP projector is surprisingly effective and data-efficient.\"\n    notes: \"Key reference for the MLP projector approach used in OpenVLA. Our finding that MLP projector enables graceful degradation under token pruning connects to this design choice.\"\n\n  - bibtex_key: shi2016subpixel\n    title: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\"\n    authors: \"Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan\"\n    year: 2016\n    venue: \"CVPR 2016\"\n    arxiv_id: \"1609.05158\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"Introduces sub-pixel convolution (pixel shuffle) that rearranges spatial resolution and channel dimensions; enables real-time 1080p super-resolution.\"\n    notes: \"Origin of the pixel_shuffle operation adopted by SmolVLA and InternVL as vision connector. Central to our cliff-edge failure analysis.\"\n\n  - bibtex_key: chen2024internvl\n    title: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\"\n    authors: \"Chen, Zhe and Wang, Weiyun and Tian, Hao and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2404.16821\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"InternVL 1.5 uses 2x2 pixel unshuffle to compress 1024 visual tokens to 256 per tile; supports dynamic high-resolution up to 4K with up to 40 tiles.\"\n    notes: \"Another VLM using pixel_shuffle connector, confirming its adoption beyond SmolVLA. Strengthens generality of our cliff-edge finding.\"\n\n  - bibtex_key: oquab2024dinov2\n    title: \"DINOv2: Learning Robust Visual Features without Supervision\"\n    authors: \"Oquab, Maxime and Darcet, Timothee and Moutakanni, Theo and others\"\n    year: 2024\n    venue: \"TMLR 2024\"\n    arxiv_id: \"2304.07193\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Self-supervised ViT producing all-purpose visual features; scaled to ViT-g with curated LVD-142M dataset; strong transfer across tasks without finetuning.\"\n    notes: \"Vision encoder used in OpenVLA (DinoSigLIP). Its feature structure interacts with the MLP projector to determine token-level importance distribution.\""
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T01:40:44.928079+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T01:40:44.928356+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"bibtex_key:\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml && echo \"---\" && grep \"bibtex_key:\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml | tail -6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"bibtex_key:\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml && echo \"---\" && grep \"bibtex_key:\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml | tail -6"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T01:40:44.928572+00:00_

28
---
  - bibtex_key: li2023blip2
  - bibtex_key: alayrac2022flamingo
  - bibtex_key: liu2023llava
  - bibtex_key: shi2016subpixel
  - bibtex_key: chen2024internvl
  - bibtex_key: oquab2024dinov2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-18T01:40:44.928820+00:00_

6 papers added (total now 28). The "Vision Connectors & Token Compression" cluster contains:

| bibtex_key | Paper | Year | Venue | Role |
|---|---|---|---|---|
| `li2023blip2` | BLIP-2 (Q-Former) | 2023 | ICML | foundation |
| `alayrac2022flamingo` | Flamingo (Perceiver Resampler) | 2022 | NeurIPS | foundation |
| `liu2023llava` | LLaVA (MLP projector) | 2023 | NeurIPS | foundation |
| `shi2016subpixel` | Sub-Pixel CNN (pixel shuffle origin) | 2016 | CVPR | background |
| `chen2024internvl` | InternVL 1.5 (pixel unshuffle connector) | 2024 | arXiv | background |
| `oquab2024dinov2` | DINOv2 (vision encoder in OpenVLA) | 2024 | TMLR | foundation |

All verified via WebSearch against arxiv.org/semanticscholar.org.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_lit_vision_connectors_20260518T013731"
}
```

</details>

---
