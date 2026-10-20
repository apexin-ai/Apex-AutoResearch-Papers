# paper research bib completion

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 97
- **Recorded user turns:** 0
- **Tool calls:** 48
- **Original source:** `logs/chats/worker_paper_research_bib_completion_20260516T041312.jsonl`
- **Structured JSON:** [`ca0480ac04181fbff046.json`](../../sessions/ca/ca0480ac04181fbff046.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

97 recorded events

### Tool call

_source line 1 · 2026-05-16T04:19:57.932413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T04:19:57.932975+00:00_

1	---
2	name: reference-audit
3	description: 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。
4	scope: global
5	tags:
6	- workflow
7	- submission
8	- writing
9	- quality
10	priority: 6
11	version: 2
12	roles:
13	- agent
14	- paper_agent
15	- review_reviewer
16	- worker
17	---
18	
19	# 引用验证与审计（Reference Audit）
20	
21	## 核心原则
22	
23	**写时验证，而非写后检查。** 每添加一条引用，立即验证真实性。AI 生成的引用约 40% 存在错误——绝不信任记忆中的引用信息。
24	
25	## 触发条件
26	
27	- 写论文时添加引用
28	- Review Reviewer 审查论文引用质量
29	- 提交前最终检查
30	- 发现可疑引用（年份不对、作者不存在、找不到原文）
31	
32	## 验证流程
33	
34	### 1. 单条引用验证（写论文时）
35	
36	每次需要引用时：
37	
38	1. **WebSearch 查找**：搜索论文标题 + 第一作者
39	2. **Google Scholar 确认**：`site:scholar.google.com [论文标题] [作者]`
40	3. **核对关键信息**：标题、第一作者、年份（±1 年）、venue
41	4. **获取 BibTeX**：从 Google Scholar 或 DBLP 获取标准格式
42	5. **验证 claim**（如果引用了具体结论）：确认该 claim 确实出现在原文中
43	
44	### 2. 全文引用审计（批量检查）
45	
46	**Step 1：调用 `verify_references(paper_dir)`**
47	
48	这是首选方式。该工具自动完成：
49	- 解析所有 .bib 文件，提取结构化条目
50	- 解析所有 .tex 文件，提取 `\cite{}`/`\citep{}`/`\citet{}` 引用
51	- 交叉检查：找出 orphan（.bib 有但未引用）和 missing（引用了但 .bib 没有）
52	- 调 OpenAlex API 在线验证每条引用是否存在（返回 verified/not_found/mismatch）
53	
54	如果只需快速离线检查，传 `skip_online=True`。
55	
56	**Step 2：人工复核工具报告中的问题条目**
57	
58	重点关注：
59	- `status: not_found` — 可能是幻觉引用，用 WebSearch 二次验证
60	- `status: mismatch` — 年份等信息不一致，检查 preprint vs published 版本
61	- `missing_bib` — 正文引用了但 .bib 中不存在，编译会报错
62	- `orphan_bib` — .bib 中有但正文未引用，清理或补引用
63	
64	**Step 3：语义验证**（优先级排序）
65	1. 首先验证 Introduction 和 Related Work 中的高频引用
66	2. 然后验证 Method 中支撑技术 claim 的引用
67	3. 最后验证其余引用
68	
69	对于 OpenAlex 未找到的条目，用 WebSearch 补充验证（arXiv、DOI、DBLP）。
70	
71	### 3. 验证失败处理
72	
73	**找不到论文时**：
74	1. 检查拼写——标题或作者名是否有误？
75	2. 尝试不同查询组合（WebSearch + Google Scholar + DBLP）
76	3. 标记为 `[CITATION NEEDED]`
77	4. 明确告知——说明哪条引用无法验证
78	
79	**信息不匹配时**：
80	1. 确认是否找对了论文
81	2. 检查版本——preprint vs published 版本
82	3. 用最准确的版本更新信息
83	
84	**绝不做的事**：
85	- 从记忆生成 BibTeX——AI 生成引用 40% 错误率
86	- 跳过验证步骤
87	- 假设论文存在
88	- 对无法验证的引用不做标记
…[truncated 888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T04:19:57.933172+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T04:19:57.933349+00:00_

1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	% [VERIFY] Confirm venue and exact title. Likely "Prismatic VLMs" or OpenVLA architecture companion.
11	@article{karamcheti2024,
12	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
13	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
14	  journal   = {arXiv preprint arXiv:2402.07865},
15	  year      = {2024},
16	}
17	
18	@article{brohan2023_rt2,
19	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
20	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
21	  journal   = {arXiv preprint arXiv:2307.15818},
22	  year      = {2023},
23	}
24	
25	% === Benchmark ===
26	
27	@inproceedings{liu2023_libero,
28	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
29	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
30	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
31	  year      = {2023},
32	}
33	
34	% === Representation Analysis Methods ===
35	
36	@article{kriegeskorte2008,
37	  title     = {Representational Similarity Analysis -- Connecting 
…[truncated 2717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T04:19:57.933568+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA sparse autoencoder interpretability OpenVLA')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
  "description": "Search S2 for swann2026 - VLA sparse autoencoder"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA sparse autoencoder interpretability OpenVLA')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
    "description": "Search S2 for swann2026 - VLA sparse autoencoder"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T04:19:57.933722+00:00_

Title: Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models
Authors: ['Aiden Swann', 'Lachlain McGranahan', 'Hugo Buurmeijer', 'Monroe Kennedy', 'Mac Schwager']
Year: 2026
Venue: 
IDs: {'ArXiv': '2603.19183', 'CorpusId': 286673529}
---
Title: Mechanistic interpretability for steering vision-language-action models
Authors: ['Bear Häon', 'Kaylene C. Stocking', 'Ian Chuang', 'Claire J. Tomlin']
Year: 2025
Venue: arXiv.org
IDs: {'ArXiv': '2509.00328', 'DBLP': 'journals/corr/abs-2509-00328', 'DOI': '10.48550/arXiv.2509.00328', 'CorpusId': 281080756}
---
Title: Emergent World Representations in OpenVLA
Authors: ['Marco Molinari', 'Leonardo Nevali', 'Saharsha Navani', 'Omar G. Younis']
Year: 2025
Venue: arXiv.org
IDs: {'ArXiv': '2509.24559', 'DBLP': 'journals/corr/abs-2509-24559', 'DOI': '10.48550/arXiv.2509.24559', 'CorpusId': 281676036}
---
Title: SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation
Authors: ['Wei Li', 'Renshan Zhang', 'Rui Shao', 'Zhijian Fang', 'Kaiwen Zhou', 'Zhuotao Tian', 'Liqiang Nie']
Year: 2025
Venue: AAAI Conference on Artificial Intelligence
IDs: {'DBLP': 'journals/corr/abs-2511-10518', 'ArXiv': '2511.10518', 'DOI': '10.48550/arXiv.2511.10518', 'CorpusId': 282992074}
---
Title: Real-Time Vision-Language-Action Control for Open-Source Quadruped Robots
Authors: ['Sagar Manglani']
Year: None
Venue: 
IDs: {'CorpusId': 281105240}
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T04:19:57.933867+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA feature observability controllability steering')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
  "description": "Search S2 for rizzardo2026 - VLA feature observability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA feature observability controllability steering')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
    "description": "Search S2 for rizzardo2026 - VLA feature observability"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T04:19:57.934023+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    data = json.loads(urlopen(req, timeout=15).read())
                      ~~~~~~~^^^^^^^^^^^^^^^^^
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
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T04:19:57.934153+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('OpenVLA probing world model representations')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
  "description": "Search S2 for molinari2025 - OpenVLA probing world model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('OpenVLA probing world model representations')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
    "description": "Search S2 for molinari2025 - OpenVLA probing world model"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T04:19:57.934285+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
from urllib.request import …) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T04:19:57.934410+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('Belinkov probing classifiers promises shortcomings advances')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
  "description": "Search S2 for belinkov2022 - probing classifiers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('Belinkov probing classifiers promises shortcomings advances')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
    "description": "Search S2 for belinkov2022 - probing classifiers"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T04:19:57.934534+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
from urllib.request import …) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T04:19:57.934655+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('OpenVLA probing symbolic states layers')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
  "description": "Search S2 for lu2025 - OpenVLA probing symbolic states"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('OpenVLA probing symbolic states layers')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
    "description": "Search S2 for lu2025 - OpenVLA probing symbolic states"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T04:19:57.934775+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
from urllib.request import …) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T04:19:57.934901+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA semantic perturbation language instruction robustness')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
  "description": "Search S2 for hou2026 - VLA semantic perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA semantic perturbation language instruction robustness')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
    "description": "Search S2 for hou2026 - VLA semantic perturbation"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T04:19:57.935042+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
from urllib.request import …) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T04:19:57.935176+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA LIBERO robustness language instruction controlled test')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
  "description": "Search S2 for fei2025 - VLA LIBERO robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA LIBERO robustness language instruction controlled test')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
    "description": "Search S2 for fei2025 - VLA LIBERO robustness"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T04:19:57.935297+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
from urllib.request import …) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T04:19:57.935414+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA fine-tuning erodes VLM reasoning abilities')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
  "description": "Search S2 for fang2025 - VLA fine-tuning erodes VLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA fine-tuning erodes VLM reasoning abilities')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
    "description": "Search S2 for fang2025 - VLA fine-tuning erodes VLM"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T04:19:57.935532+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
from urllib.request import …) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T04:19:57.935648+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA visual dominance language instruction encoded not used')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
  "description": "Search S2 for grant2026 - VLA visual dominance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('VLA visual dominance language instruction encoded not used')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
    "description": "Search S2 for grant2026 - VLA visual dominance"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T04:19:57.935766+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
from urllib.request import …) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T04:19:57.935881+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('OpenVLA sparse semantic directions activation steering interpretability')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
  "description": "Search S2 for haon2025 - OpenVLA sparse semantic directions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('OpenVLA sparse semantic directions activation steering interpretability')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req, timeout=15).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n    print(f\\\"Year: {p.get('year')}\\\")\n    print(f\\\"Venue: {p.get('venue')}\\\")\n    print(f\\\"IDs: {p.get('externalIds')}\\\")\n    print('---')\n\"\n",
    "description": "Search S2 for haon2025 - OpenVLA sparse semantic directions"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T04:19:57.936032+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
from urllib.request import …) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T04:19:57.936192+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json, time\n\nqueries = [\n    ('belinkov2022', 'Belinkov probing classifiers promises shortcomings advances'),\n    ('lu2025', 'OpenVLA probing symbolic states layers'),\n    ('hou2026', 'VLA semantic perturbation language instruction robustness'),\n    ('fei2025', 'VLA LIBERO robustness language instruction controlled test'),\n    ('fang2025', 'VLA fine-tuning erodes VLM reasoning abilities'),\n    ('grant2026', 'VLA visual dominance language instruction encoded not used six architectures'),\n    ('rizzardo2026', 'VLA feature observability controllability steering'),\n]\n\nfor label, q in queries:\n    query = quote(q)\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\n    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\n    try:\n        data = json.loads(urlopen(req, timeout=15).read())\n        print(f'=== {label} ===')\n        for p in data.get('data', []):\n            print(f\\\"Title: {p['title']}\\\")\n            print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n            print(f\\\"Year: {p.get('year')}\\\")\n            print(f\\\"Venue: {p.get('venue')}\\\")\n            print(f\\\"IDs: {p.get('externalIds')}\\\")\n            print('---')\n    except Exception as e:\n        print(f'=== {label} === ERROR: {e}')\n    time.sleep(2)\n\" 2>&1\n",
  "description": "Sequential S2 API searches with rate limit delay",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json, time\n\nqueries = [\n    ('belinkov2022', 'Belinkov probing classifiers promises shortcomings advances'),\n    ('lu2025', 'OpenVLA probing symbolic states layers'),\n    ('hou2026', 'VLA semantic perturbation language instruction robustness'),\n    ('fei2025', 'VLA LIBERO robustness language instruction controlled test'),\n    ('fang2025', 'VLA fine-tuning erodes VLM reasoning abilities'),\n    ('grant2026', 'VLA visual dominance language instruction encoded not used six architectures'),\n    ('rizzardo2026', 'VLA feature observability controllability steering'),\n]\n\nfor label, q in queries:\n    query = quote(q)\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\n    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\n    try:\n        data = json.loads(urlopen(req, timeout=15).read())\n        print(f'=== {label} ===')\n        for p in data.get('data', []):\n            print(f\\\"Title: {p['title']}\\\")\n            print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n            print(f\\\"Year: {p.get('year')}\\\")\n            print(f\\\"Venue: {p.get('venue')}\\\")\n            print(f\\\"IDs: {p.get('externalIds')}\\\")\n            print('---')\n    except Exception as e:\n        print(f'=== {label} === ERROR: {e}')\n    time.sleep(2)\n\" 2>&1\n",
    "description": "Sequential S2 API searches with rate limit delay",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T04:19:57.936331+00:00_

=== belinkov2022 === ERROR: HTTP Error 429: 
=== lu2025 === ERROR: HTTP Error 429: 
=== hou2026 === ERROR: HTTP Error 429: 
=== fei2025 === ERROR: HTTP Error 429: 
=== fang2025 === ERROR: HTTP Error 429: 
=== grant2026 === ERROR: HTTP Error 429: 
=== rizzardo2026 === ERROR: HTTP Error 429:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T04:19:57.936470+00:00_

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
  "session": "worker_paper_research_bib_completion_20260516T041312",
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

_source line 28 · 2026-05-16T04:19:57.936587+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T04:19:57.936697+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Belinkov 2022 \"Probing Classifiers: Promises, Shortcomings, and Advances\" Computational Linguistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Belinkov 2022 \"Probing Classifiers: Promises, Shortcomings, and Advances\" Computational Linguistics"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T04:19:57.936814+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rizzardo 2026 VLA feature observability controllability steering arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rizzardo 2026 VLA feature observability controllability steering arXiv"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T04:19:57.936940+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lu 2025 OpenVLA probing symbolic states arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lu 2025 OpenVLA probing symbolic states arXiv"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T04:19:57.937056+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hou Zhao 2026 VLA semantic perturbation language instruction arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hou Zhao 2026 VLA semantic perturbation language instruction arXiv"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T04:19:57.937211+00:00_

Web search results for query: "Belinkov 2022 "Probing Classifiers: Promises, Shortcomings, and Advances" Computational Linguistics"

Links: [{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"(PDF) Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"@article{belinkov-2022-probing,","url":"https://aclanthology.org/2022.cl-1.7.bib"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://aclanthology.org/2022.cl-1.7.pdf"},{"title":"Probing Classifiers: Promises, Shortcomings, and Alternatives","url":"https://www.researchgate.net/publication/349583742_Probing_Classifiers_Promises_Shortcomings_and_Alternatives"}]

I found comprehensive information about this paper. Here are the search results:

## Paper Details

The paper "Probing Classifiers: Promises, Shortcomings, and Advances" was published in Computational Linguistics, volume 48, issue 1, pages 207-219 in 2022
…[truncated 908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T04:19:57.937380+00:00_

Web search results for query: "Hou Zhao 2026 VLA semantic perturbation language instruction arXiv"

Links: [{"title":"[2603.00592v1] LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.00592v1"},{"title":"[2603.00592] LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.00592"},{"title":"LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action ModelsCode and benchmark will be available at: https://github.com/YC11Hou/langgap","url":"https://arxiv.org/html/2603.00592"},{"title":"NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models","url":"https://arxiv.org/html/2603.09542v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System","url":"https://arxiv.org/html/2604.24921"},{"title":"[2603.09542] NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.09542"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://arxiv.org/html/2505.19789v4"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919v1"}]

Based on the web search results, I found a highly relevant paper matching your query:

The paper "LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models" was authored by Yuchen Hou and Lin Zhao and submitted on February 28, 2026 (arXiv:2603.00592).

The paper finds that current state-of-the-art VLA models largely ignore language instructions, and it addresses the lack of systematic semantic perturbation diagnostics, benchmarks that force language understanding by design, and linguistically diverse training data.

The paper constru
…[truncated 463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-16T04:19:57.937696+00:00_

Web search results for query: "Rizzardo 2026 VLA feature observability controllability steering arXiv"

Links: [{"title":"Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/html/2603.05487"},{"title":"[2603.05487] Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05487"},{"title":"(PDF) Observing and Controlling Features in Vision-Language-Action Models","url":"https://www.researchgate.net/publication/401601449_Observing_and_Controlling_Features_in_Vision-Language-Action_Models"},{"title":"[2603.19183] Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/abs/2603.19183"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/html/2603.19183v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots","url":"https://arxiv.org/html/2507.17049v2"},{"title":"PosePilot: Steering Camera Pose for Generative World Models with Self-supervised Depth","url":"https://arxiv.org/html/2505.01729"},{"title":"Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future","url":"https://arxiv.org/html/2512.16760v1"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"}]

Based on the search results, I found a relevant paper on arXiv. The search query matched a paper titled **"Observing and Controlling Features in Vision-Language-Action Models"** (arXiv:2603.05487), published on March 5, 2026.

The paper presents a combination of feature-observability and feature-controllability: a framework to observe and control robot behavior through accessing and modifying internal VLA representations. 

A linear observer extracts features fr
…[truncated 1044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T04:19:57.937875+00:00_

Web search results for query: "Lu 2025 OpenVLA probing symbolic states arXiv"

Links: [{"title":"[2502.04558] Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture","url":"https://arxiv.org/abs/2502.04558"},{"title":"Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture","url":"https://arxiv.org/html/2502.04558v1"},{"title":"[Literature Review] Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture","url":"https://www.themoonlight.io/en/review/probing-a-vision-language-action-model-for-symbolic-states-and-integration-into-a-cognitive-architecture"},{"title":"Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture | OpenReview","url":"https://openreview.net/forum?id=JktsyBGNrg"},{"title":"Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/probing-vision-language-action-model-symbolic-states"},{"title":"Week Ending 2.9.2025 — Eye On AI","url":"https://www.eye-on.ai/ai-articles/e6n7f8m6dc4a3aw-kysfw-p3bpn-gj8zp-p9mmz-b34zn"},{"title":"Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture","url":"https://paperreading.club/page?id=282643"},{"title":"HRILab Tufts - Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture","url":"https://hrilab.tufts.edu/publications/luetal25icad/"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Probing a Vision-Language-Action Model for Symbolic States ...","url":"https://hrilab.tufts.edu/publications/luetal25icad.pdf"}]

Based on the search results, here's information about the paper "Probing a Vision-Language-Action Model for Symbolic States and Integra
…[truncated 1676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T04:19:57.938074+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fei 2025 VLA LIBERO robustness language instruction ignore arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fei 2025 VLA LIBERO robustness language instruction ignore arXiv"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T04:19:57.938200+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fang 2025 VLA fine-tuning erodes VLM reasoning capabilities arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fang 2025 VLA fine-tuning erodes VLM reasoning capabilities arXiv"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T04:19:57.938317+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grant 2026 visual dominance VLA language instruction \"encoded but not used\" six architectures arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grant 2026 visual dominance VLA language instruction \"encoded but not used\" six architectures arXiv"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T04:19:57.938439+00:00_

Web search results for query: "Grant 2026 visual dominance VLA language instruction "encoded but not used" six architectures arXiv"

No links found.

The search didn't return any results. This could mean that either:

1. The exact phrase or combination of terms doesn't match any indexed papers on arXiv or other web sources
2. The paper may be very recent and not yet widely indexed
3. Some of the specific terms or phrasing might need adjustment

Would you like me to try:
- A shorter or simplified search query with the main keywords?
- Searching for specific terms like "visual dominance VLA" or "language instruction architectures"?
- Looking for variations of the terms?

Please let me know how you'd like to proceed, or if you have additional information about the paper you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T04:19:57.938590+00:00_

Web search results for query: "Fei 2025 VLA LIBERO robustness language instruction ignore arXiv"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Object: Lifelong Learning in Robotic Manipulation","url":"https://www.emergentmind.com/topics/libero-object"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"}]

Based on the search results, I found information about the research by Senyu Fei and colleagues on Vision-Language-Action (VLA) models, LIBERO benchmarking, and robustness analysis with respect to language instructions:

## LIBERO-Plus: In-depth Robustness Analysis

The research presents a systematic vulnerability analysis of Visual-Language-Action (VLA) models by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial
…[truncated 1085 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T04:19:57.938763+00:00_

Web search results for query: "Fang 2025 VLA fine-tuning erodes VLM reasoning capabilities arXiv"

Links: [{"title":"2026-01-21 Work in progress. TwinBrainVLA TwinBrainVLA","url":"https://arxiv.org/pdf/2601.14133"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Clutter-Robust Vision–Language–Action Models through Object-Centric and Geometry Grounding","url":"https://arxiv.org/html/2512.22519"},{"title":"[2512.12690] Reassessing the Role of Supervised Fine-Tuning: An Empirical Study in VLM Reasoning","url":"https://arxiv.org/abs/2512.12690"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/html/2509.22195v1"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v2"},{"title":"DriveVLA-W0: World Models Amplify Data Scaling Law in ...","url":"https://arxiv.org/pdf/2510.12796"},{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Reassessing the Role of Supervised Fine-Tuning: An Empirical Study in VLM Reasoning","url":"https://arxiv.org/html/2512.12690v1"}]

Based on the search results, I found several relevant research papers addressing the topic of how fine-tuning VLMs for robotic action generation affects their reasoning capabilities:

## Key Findings

Fine-tuning undermines the fundamental premise of the VLA paradigm, which aims to leverage general world understanding acquired during VLM pre-training to enable generalized robotic control. However, current fine-tuning methodologies paradoxically strip the VLM of this very capability.

As parameters are updated to minimize high-frequency spatial error in a
…[truncated 1280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T04:19:57.938961+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.13626 LIBERO-Plus authors Fei"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.13626 LIBERO-Plus authors Fei"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-16T04:19:57.939093+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fang 2025 \"VLA\" \"VLM\" reasoning erosion degradation fine-tuning action arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fang 2025 \"VLA\" \"VLM\" reasoning erosion degradation fine-tuning action arXiv"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T04:19:57.939211+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grant 2026 \"visual pathways dominate\" VLA action generation language arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grant 2026 \"visual pathways dominate\" VLA action generation language arXiv"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T04:19:57.939324+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.05487 Rizzardo \"Observing and Controlling Features\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.05487 Rizzardo \"Observing and Controlling Features\" authors"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-16T04:19:57.939442+00:00_

Web search results for query: "Grant 2026 "visual pathways dominate" VLA action generation language arXiv"

No links found.

The search didn't return any results for that exact query. This could mean:

1. The paper may not yet be indexed by search engines
2. The exact phrase or publication details may be slightly different
3. It might be a very recent submission to arXiv that hasn't been widely indexed yet

Since today is May 16, 2026, if this is a very recent paper from 2026, it's possible it hasn't been fully indexed yet. 

Would you like me to try a modified search? I could search for:
- Just the authors/key terms (like "Grant VLA action generation")
- The topic without quotes ("visual pathways dominate VLA")
- The paper on arXiv directly by browsing recent submissions

Let me know how you'd like to proceed, or if you have any additional information about where this paper might be published!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T04:19:57.939591+00:00_

Web search results for query: "arxiv 2510.13626 LIBERO-Plus authors Fei"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://bytez.com/docs/arxiv/2510.13626/paper"}]

Based on the search results, here's the information about arxiv paper 2510.13626:

## Paper: LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models

**Authors with "Fei":**
The paper has two authors with the surname "Fei": Senyu Fei (from Tongji University and Shanghai Innovation Institute) and Zhaoye Fei (from Fudan University).

**Full Author List:**
Senyu Fei, Siyin Wang, Junhao Shi, Zihao Dai, Jikun Cai, Pengfang Qian, Li J
…[truncated 781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T04:19:57.939767+00:00_

Web search results for query: "Fang 2025 "VLA" "VLM" reasoning erosion degradation fine-tuning action arXiv"

Links: [{"title":"TwinBrainVLA: Unleashing the Potential of Generalist VLMs for Embodied Tasks via Asymmetric Mixture-of-Transformers","url":"https://arxiv.org/html/2601.14133"},{"title":"2026-01-21 Work in progress. TwinBrainVLA TwinBrainVLA","url":"https://arxiv.org/pdf/2601.14133"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning","url":"https://arxiv.org/html/2510.11027v1"},{"title":"MolmoAct2 Action Reasoning Models for Real-World Deployment Haoquan Fang♥1,2∗","url":"https://arxiv.org/pdf/2605.02881"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/pdf/2509.22195"},{"title":"VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models","url":"https://arxiv.org/html/2601.03309v1"},{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"Reassessing the Role of Supervised Fine-Tuning: An Empirical Study in VLM Reasoning","url":"https://arxiv.org/html/2512.12690v1"}]

Based on the search results, I found relevant papers discussing the topics you're interested in. Here are the key findings:

## Main References Found

Fang et al. (2025) published "DualVLA: building a generalizable embodied agent via partial decoupling of reasoning and action" on arXiv (2511.22134).

## Key Research Area: Reasoning Erosion and Degradation in VLAs

Your search terms relate to an important problem in Vision-Language-Action models. Recent work has identified "catastrophic 
…[truncated 1153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T04:19:57.939942+00:00_

Web search results for query: "arxiv 2603.05487 Rizzardo "Observing and Controlling Features" authors"

Links: [{"title":"[2603.05487] Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05487"},{"title":"Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.05487"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=263&show=2000"},{"title":"[1503.01160] Spectrum of Controlling and Observing Complex Networks","url":"https://arxiv.org/abs/1503.01160"},{"title":"[1701.00830] A note on non-unique enhancements","url":"https://arxiv.org/abs/1701.00830"},{"title":"Contextual Preference Distribution Learning","url":"https://arxiv.org/html/2603.17139"},{"title":"[1801.06344] A k-linear triangulated category without a model","url":"https://arxiv.org/abs/1801.06344"},{"title":"GRVS: a Generalizable and Recurrent Approach to Monocular Dynamic View Synthesis","url":"https://arxiv.org/html/2603.29734"},{"title":"[2603.08947] Towards Reliable Simulation-based Inference","url":"https://arxiv.org/abs/2603.08947"},{"title":"Spectral sirens cosmology from binary black holes populations with sharper mass features","url":"https://arxiv.org/html/2603.06792v1"}]

Based on the search results, the authors of arxiv paper 2603.05487 "Observing and Controlling Features in Vision-Language-Action Models" are Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, and Marco Pavone.

Note: The search did not return results showing an author named "Rizzardo" for this paper. The results did show other papers by an Alice Rizzardo, but those were on different topics (mathematical category theory papers).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T04:19:57.940130+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rizzardo 2026 VLA robotics vision language action arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rizzardo 2026 VLA robotics vision language action arXiv"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T04:19:57.940256+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fang 2025 VLA fine-tuning \"catastrophic forgetting\" VLM reasoning arXiv 2509"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fang 2025 VLA fine-tuning \"catastrophic forgetting\" VLM reasoning arXiv 2509"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T04:19:57.940372+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grant 2026 VLA \"six architectures\" visual dominance language grounding robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grant 2026 VLA \"six architectures\" visual dominance language grounding robotics"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T04:19:57.940514+00:00_

Web search results for query: "Rizzardo 2026 VLA robotics vision language action arXiv"

Links: [{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"[2510.07077] Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications","url":"https://arxiv.org/abs/2510.07077"},{"title":"A Survey on Vision-Language-Action Models for Embodied ...","url":"https://arxiv.org/html/2405.14093v8"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919v1"},{"title":"A Vision-Language-Action-Critic Model for Robotic Real- ...","url":"https://arxiv.org/pdf/2509.15937"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"}]

I found several arXiv papers related to Vision-Language-Action (VLA) models and robotics from 2025-2026, but I didn't find a specific paper by an author named "Rizzardo" in the search results. 

The search returned multiple comprehensive reviews and surveys on VLA models published recently:

1. A foundational review covering over 80 VLA models published in the past three years, organized across five thematic pillars (arxiv.org/html/2505.04769v2)

2. A survey synthesizing insights from over three hundred recent studies on Pure Vision Language Action models (arxiv.org/html/2509.19012v1)

3. A systematic review analyzing 102 VLA models, 26 foundational dataset
…[truncated 658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-16T04:19:57.940685+00:00_

Web search results for query: "Fang 2025 VLA fine-tuning "catastrophic forgetting" VLM reasoning arXiv 2509"

Links: [{"title":"2026-01-21 Work in progress. TwinBrainVLA TwinBrainVLA","url":"https://arxiv.org/pdf/2601.14133"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://vlm2vla.github.io/"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/pdf/2509.22195"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.22195"},{"title":"TwinBrainVLA: Unleashing the Potential of Generalist VLMs for Embodied Tasks via Asymmetric Mixture-of-Transformers","url":"https://arxiv.org/html/2601.14133"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"[2509.22195] Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/abs/2509.22195"},{"title":"Fine-tuning VLMs Without Forgetting Is Easier Than You Think","url":"https://openreview.net/pdf/278c682d3fdae858e47cc6e1111e5d282dd787fa.pdf"},{"title":"Seeing to Act, Prompting to Specify: A Bayesian Factorization of...","url":"https://arxiv.org/abs/2512.11218"},{"title":"FINE-TUNING VLMS INTO VLAS WITHOUT CATASTROPHIC ...","url":"https://openreview.net/pdf/85f42c58962d316f5e438073b3fef845314336ce.pdf"}]

Based on the search results, I found highly relevant papers related to your query. Here are the key findings:

## VLM Fine-tuning and Catastrophic Forgetting

The catastrophic forgetting problem in VLA fine-tuning is due to a distribution mismatch between the VLM's internet-scale pretraining corpus and robotics fine-tuning data. One solution, VLM2VLA, resolves this mismatch at the data level by representing low-level actions with natural language, making it possible to train VLAs solely with Low-Rank Adapta
…[truncated 1260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T04:19:57.940855+00:00_

Web search results for query: "Grant 2026 VLA "six architectures" visual dominance language grounding robotics"

Links: [{"title":"Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications","url":"https://arxiv.org/html/2510.07077v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"LiteVLA-H: Dual-Rate Vision-Language-Action Inference for Onboard Aerial Guidance and Semantic Perception","url":"https://arxiv.org/html/2605.00884"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/html/2603.22760"},{"title":"12 Predictions for Embodied AI and Robotics in 2026 | Dylan Bourgeois","url":"https://dtsbourg.me/en/articles/predictions-embodied-ai"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"}]

I found search results related to Vision-Language-Action (VLA) models and robotics in 2026. While the results contain extensive information about VLA architectures, datasets, and applications, I did not find a specific document or grant with the exact phrase "six architectures" combined with "visual dominance language grounding" in these resu
…[truncated 1226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T04:19:57.941049+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Fang\" 2025 VLA VLM reasoning ability erosion degradation fine-tuning robotics arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Fang\" 2025 VLA VLM reasoning ability erosion degradation fine-tuning robotics arXiv"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-16T04:19:57.941176+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grant 2026 VLA language instruction visual modality dominance \"action generation\" arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grant 2026 VLA language instruction visual modality dominance \"action generation\" arXiv 2026"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-16T04:19:57.941326+00:00_

Web search results for query: ""Fang" 2025 VLA VLM reasoning ability erosion degradation fine-tuning robotics arXiv"

Links: [{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning","url":"https://arxiv.org/html/2510.11027v1"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178v1"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/html/2509.22195v1"},{"title":"Scalable Vision-Language-Action Model Pretraining for ​Robotic Manipulation with Real-Life Human Activity Videos","url":"https://arxiv.org/html/2510.21571v1"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models Angen Ye12∗","url":"https://arxiv.org/pdf/2510.01623"}]

I found relevant research results related to your query. The search returned several papers on Vision-Language-Action (VLA) models and Vision-Language Models (VLMs) for robotics from 2025 and related periods. Here are some key findings:

## Key Papers Found:

1. **LangForce** (arXiv:2601.15197) - This work addresses how fine-tuning VLMs for robotic action generation (VLA training) diminishes the model's foundational reasoning and multimodal understanding, potentially lea
…[truncated 1288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T04:19:57.941507+00:00_

Web search results for query: "Grant 2026 VLA language instruction visual modality dominance "action generation" arXiv 2026"

Links: [{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"Stable Language Guidance for Vision–Language–Action Models","url":"https://arxiv.org/html/2601.04052v2"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.28740"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"Unifying Language-Action Understanding and Generation for Autonomous Driving","url":"https://arxiv.org/html/2603.01441"},{"title":"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/html/2507.01925v1"}]

I found several highly relevant papers on Vision-Language-Action (VLA) models. Based on the search results, here are the most relevant findings:

A critical "modality collapse" phenomenon has been identified where strong visual priors overwhelm sparse linguistic signals, causing agents to overfit to specific instruction phrasings while ignoring the underlying semantic intent.

More specifically, analyses on benchmarks reveal a pervasive "instruction blindness," where models frequently ignore language inputs entirely, defaulting to the most probable action given the scen
…[truncated 1142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T04:19:57.941673+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Robix\" Fang 2025 VLA VLM reasoning fine-tuning arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Robix\" Fang 2025 VLA VLM reasoning fine-tuning arXiv"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-16T04:19:57.941795+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA \"visual dominance\" language instruction \"encoded but not used\" 2026 robotics arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA \"visual dominance\" language instruction \"encoded but not used\" 2026 robotics arXiv"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-16T04:19:57.941977+00:00_

Web search results for query: ""Robix" Fang 2025 VLA VLM reasoning fine-tuning arXiv"

Links: [{"title":"Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning","url":"https://arxiv.org/html/2510.11027v1"},{"title":"Robix: A Unified Model for Robot Interaction, Reasoning and Planning","url":"https://arxiv.org/pdf/2509.01106"},{"title":"ReFineVLA: Multimodal Reasoning-Aware Generalist Robotic Policies via Teacher-Guided Fine-Tuning","url":"https://arxiv.org/html/2604.17800v1"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"2026-01-21 Work in progress. TwinBrainVLA TwinBrainVLA","url":"https://arxiv.org/pdf/2601.14133"},{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://arxiv.org/html/2506.09930v1"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/html/2509.22195v1"},{"title":"DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models","url":"https://arxiv.org/html/2511.15669v1"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"}]

Based on the search results, I found relevant information about Robix and VLA/VLM reasoning fine-tuning research:

## Robix: A Unified Model for Robot Interaction, Reasoning and Planning

Robix is described as "A unified model for robot interaction, reasoning and planning" with arXiv preprint arXiv:2509.01106 (2025).

Robix (Fang et al., 2025) incorporates Reinforcement Fine-Tuning (RFT) and synthesizes spatio-t
…[truncated 991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T04:19:57.942184+00:00_

Web search results for query: "VLA "visual dominance" language instruction "encoded but not used" 2026 robotics arXiv"

Links: [{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models","url":"https://arxiv.org/html/2604.03956v2"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"Robotics arXiv Digest — 2026-03-30 - Kiru Park / Vision for Robotics","url":"https://www.visionforrobotics.com/robotics-digest/digest_2026-03-30.html"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/html/2603.22760"},{"title":"🤖 Robotics arXiv Digest — 2026-03-26","url":"https://www.visionforrobotics.com/robotics-digest/digest_2026-03-26.html"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"}]

I found relevant results for your search. The most directly relevant paper appears to be from the robotics arXiv digest. Here's what I found:

FocusVLA addresses visual representation utilization — how the policy network uses existing representations — finding this to be the dominant bottleneck. The empirical finding that VLA performance is primarily limited by visual utilization rather than visual quality challenges the prevailing scaling hypothesis, suggesting that better ar
…[truncated 1195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T04:19:57.942366+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2509.11417 \"Preserving Pretrained Representations\" VLA authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2509.11417 \"Preserving Pretrained Representations\" VLA authors"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-16T04:19:57.942491+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fang 2025 VLM VLA fine-tuning erodes reasoning \"original capabilities\" arXiv robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fang 2025 VLM VLA fine-tuning erodes reasoning \"original capabilities\" arXiv robotics"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-16T04:19:57.942765+00:00_

Web search results for query: "arxiv 2509.11417 "Preserving Pretrained Representations" VLA authors"

Links: [{"title":"[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/abs/2509.11417"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417"},{"title":"Enhancing Generalization in Vision–Language–Action Models by","url":"https://arxiv.org/pdf/2509.11417"},{"title":"[PDF] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Enhancing-Generalization-in-Vision-Language-Action-Grover-Gopalkrishnan/272525654b60ab7f4366e58244feadcfd2675aaf"},{"title":"Don’t Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/html/2510.25616v1"},{"title":"[2510.25616v1] Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/abs/2510.25616v1"},{"title":"PriorVLA: Prior-Preserving Adaptation for Vision-Language-Action Models","url":"https://arxiv.org/html/2605.10925v1"},{"title":"[2511.19878] MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization","url":"https://arxiv.org/abs/2511.19878"},{"title":": A Vision-Language-Action Model Bridging Understanding and Generation to Actions","url":"https://arxiv.org/html/2509.06951v1"},{"title":"[2510.25616] Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/abs/2510.25616"}]

Based on the search results, I found the paper you're looking for. 

The paper arXiv:2509.11417 titled "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" was submitted on September 14, 2025 and has the following authors: 
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T04:19:57.942999+00:00_

Web search results for query: "Fang 2025 VLM VLA fine-tuning erodes reasoning "original capabilities" arXiv robotics"

Links: [{"title":"[2509.22195] Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/abs/2509.22195"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/html/2509.22195v1"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation","url":"https://arxiv.org/html/2512.20188v1"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning","url":"https://arxiv.org/html/2510.11027v1"},{"title":"MolmoAct2 Action Reasoning Models for Real-World Deployment Haoquan Fang♥1,2∗","url":"https://arxiv.org/pdf/2605.02881"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"}]

I found relevant research on this topic. The search results contain information about the problem of fine-tuning vision-language models (VLMs) for vision-language-action (VLA) models in robotics.

Fine-tuning vision-language models on robot teleoperation data to create vision-language-action models suffers from a fundamental tradeoff: learning to produce actions often diminishes the VLM's foundational reas
…[truncated 908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-16T04:19:57.943179+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/related_work.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/related_work.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-16T04:19:57.943315+00:00_

docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-16T04:19:57.943432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-16T04:19:57.943572+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstration data to produce action-conditioned policies.
5	RT-2~\cite{brohan2023_rt2} pioneered this paradigm by co-fine-tuning PaLM-E on robotic trajectories; OpenVLA~\cite{kim2024_openvla} extended it with open-source weights and 970K demonstrations, built on the Prismatic VLM architecture~\cite{karamcheti2024} that chains frozen vision encoders with a Llama-2 backbone.
6	These architectures share a core design assumption---that LLM fine-tuning injects action-relevant knowledge---that our work tests at the representational level.
7	
8	\paragraph{Behavioral analysis of VLAs.}
9	A growing body of work reveals that VLAs rely disproportionately on visual input.
10	\cite{grant2026} showed across six architectures that visual pathways dominate action generation, with language instructions ``encoded but not used'' when visual context uniquely specifies the task.
11	Hou and Zhao~(2026) and Fei et al.~(2025) corroborated this through semantic perturbations and controlled robustness tests on LIBERO, finding that models largely ignore language instructions.
12	These studies establish the behavioral phenomenon; we provide a representational account showing that action-relevant geometric structure originates in the frozen vision encoder and is invariant to both LLM training and instruction content.
13	
14	\paragraph{Mechanistic interpretability of VLAs.}
15	Recent work has probed VLA internals from several angles.
16	\cite{haon2025} identified sparse semantic directions in OpenVLA causally linked to action selection, enabling activation steering without fine-tuning.
17	Swann et al.~(2026) applied sparse autoencoders, finding features dominated by memorized sequences with some interpretable motion primitives; Rizzardo et al.~(2026) introduced feature-observability and controllability concepts for VLA steering.
18	Lu et al.~(2025) and
…[truncated 2528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-16T04:19:57.943730+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fang 2025 VLA fine-tuning VLM reasoning abilities degradation erosion arxiv preprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fang 2025 VLA fine-tuning VLM reasoning abilities degradation erosion arxiv preprint"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-16T04:19:57.943848+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grant 2026 VLA visual pathways dominate action generation language \"six architectures\" preprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grant 2026 VLA visual pathways dominate action generation language \"six architectures\" preprint"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-16T04:19:57.944014+00:00_

Web search results for query: "Fang 2025 VLA fine-tuning VLM reasoning abilities degradation erosion arxiv preprint"

Links: [{"title":"TwinBrainVLA: Unleashing the Potential of Generalist VLMs for Embodied Tasks via Asymmetric Mixture-of-Transformers","url":"https://arxiv.org/html/2601.14133"},{"title":"2026-01-21 Work in progress. TwinBrainVLA TwinBrainVLA","url":"https://arxiv.org/pdf/2601.14133"},{"title":"Don’t Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/html/2510.25616v1"},{"title":"Knowledge Insulating Vision-Language-Action Models","url":"https://www.physicalintelligence.company/download/pi05_KI.pdf"},{"title":"Reassessing the Role of Supervised Fine-Tuning: An Empirical Study in VLM Reasoning","url":"https://arxiv.org/html/2512.12690v1"},{"title":"Unmasking the Illusion of Embodied Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2604.18000v1"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.22195"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v2"},{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178v1"}]

Based on the search results, I found relevant information about research on VLA (Vision-Language-Action) models and the degradation of reasoning abilities during fine-tuning. The search results include references to a work by Fang et al., 2025 that addresses this topic.

Fang et al. (2025) is cited as discussing "catastrophic forgetting" that occurs during standard robotic fine-tuning when the VLM backbone is aggressively update
…[truncated 1056 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-16T04:19:57.944193+00:00_

Web search results for query: "Grant 2026 VLA visual pathways dominate action generation language "six architectures" preprint"

Links: [{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"}]

Based on the search results, I found several comprehensive VLA (Vision-Language-Action) research papers and reviews from 2025-2026, though I didn't find a specific paper exactly matching your query with those precise keywords.

However, the search did return several highly relevant recent works on VLA architectures:

1. A unified taxonomy that organizes more than 100 VLA architectures published in a systematic review.

2. Early efforts such as
…[truncated 1086 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-16T04:19:57.944350+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2511.22134 DualVLA Fang authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2511.22134 DualVLA Fang authors"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-16T04:19:57.944475+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LangGap\" OR \"instruction blindness\" OR \"visual dominance\" VLA 2026 Grant author six architectures language \"encoded but not used\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LangGap\" OR \"instruction blindness\" OR \"visual dominance\" VLA 2026 Grant author six architectures language \"encoded but not used\""
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-16T04:19:57.944625+00:00_

Web search results for query: "arxiv 2511.22134 DualVLA Fang authors"

Links: [{"title":"[2511.22134] DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/abs/2511.22134"},{"title":"DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/html/2511.22134"},{"title":"[2602.22134] Secure Semantic Communications via AI Defenses: Fundamentals, Solutions, and Future Directions","url":"https://arxiv.org/abs/2602.22134"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=1593&show=1000"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/pastweek?skip=1527&show=1000"},{"title":"Mathematics","url":"https://www.arxiv.org/list/math/recent?skip=185&show=500"},{"title":"Shuai Bai on X: \"Excited to share the release of our Qwen3-VL paper! 🚀 Paper: https://t.co/8nWMoRfhWi https://t.co/tWbsSxq17a\" / X","url":"https://x.com/shuai_bai_/status/1993919195206307961"},{"title":"Computer Science Nov 2024","url":"https://arxiv.org/list/cs/2024-11?skip=2275&show=1000"},{"title":"Computer Vision and Pattern Recognition 2025","url":"https://arxiv.org/list/cs.CV/2025?skip=23125&show=25"},{"title":"Machine Learning","url":"https://web3.arxiv.org/list/cs.LG/recent?skip=542&show=2000"}]

Based on the search results, here's the information about arxiv paper 2511.22134:

The paper "DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action" was authored by Zhen Fang, Zhuoyang Liu, Jiaming Liu, Hao Chen, Yu Zeng, Shiting Huang, Zehui Chen, Lin Chen, Shanghang Zhang, and Feng Zhao.

The paper proposes DualVLA, which enhances action performance through carefully designed post-training while preserving reasoning capability, using a dual-layer data pruning method and a dual-teacher adaptive distillation strategy. Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEn
…[truncated 181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-16T04:19:57.944891+00:00_

Web search results for query: ""LangGap" OR "instruction blindness" OR "visual dominance" VLA 2026 Grant author six architectures language "encoded but not used""

Links: [{"title":"Stable Language Guidance for Vision–Language–Action Models","url":"https://arxiv.org/html/2601.04052v2"},{"title":"VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models","url":"https://arxiv.org/html/2604.03956v2"},{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"How Visual-Language-Action (VLA) Models Work | Towards Data Science","url":"https://towardsdatascience.com/how-visual-language-action-vla-models-work/"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"A systematic review of vision language models: Comprehensive analysis of architectures, applications, datasets and challenges towards robust multimodal intelligence - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2590005626000627"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"}]

Based on the search results, I found several relevant papers discussing instruction blindness and visual dominance in VLA (Vision-Language-Action) models in 2026:

## Key Findings:

VLA analyses on the Libero-Plus and RADAR benchmarks reveal a pervasive "instruction blindness," where models frequently ignore language inputs entirely,
…[truncated 1350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-16T04:19:57.945198+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json, time\n\nqueries = [\n    ('rizzardo2026', 'Rizzardo 2026 VLA feature observability controllability'),\n    ('grant2026', 'Grant 2026 visual dominance VLA action generation language instruction'),\n    ('fang2025_dualvla', 'DualVLA Fang 2025 generalizable embodied agent reasoning action'),\n]\n\nfor label, q in queries:\n    query = quote(q)\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\n    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\n    try:\n        data = json.loads(urlopen(req, timeout=15).read())\n        print(f'=== {label} ===')\n        for p in data.get('data', []):\n            print(f\\\"Title: {p['title']}\\\")\n            print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n            print(f\\\"Year: {p.get('year')}\\\")\n            print(f\\\"Venue: {p.get('venue')}\\\")\n            print(f\\\"IDs: {p.get('externalIds')}\\\")\n            print('---')\n    except Exception as e:\n        print(f'=== {label} === ERROR: {e}')\n    time.sleep(3)\n\" 2>&1\n",
  "description": "S2 API retry for remaining papers",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json, time\n\nqueries = [\n    ('rizzardo2026', 'Rizzardo 2026 VLA feature observability controllability'),\n    ('grant2026', 'Grant 2026 visual dominance VLA action generation language instruction'),\n    ('fang2025_dualvla', 'DualVLA Fang 2025 generalizable embodied agent reasoning action'),\n]\n\nfor label, q in queries:\n    query = quote(q)\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url'\n    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\n    try:\n        data = json.loads(urlopen(req, timeout=15).read())\n        print(f'=== {label} ===')\n        for p in data.get('data', []):\n            print(f\\\"Title: {p['title']}\\\")\n            print(f\\\"Authors: {[a['name'] for a in p.get('authors', [])]}\\\")\n            print(f\\\"Year: {p.get('year')}\\\")\n            print(f\\\"Venue: {p.get('venue')}\\\")\n            print(f\\\"IDs: {p.get('externalIds')}\\\")\n            print('---')\n    except Exception as e:\n        print(f'=== {label} === ERROR: {e}')\n    time.sleep(3)\n\" 2>&1\n",
    "description": "S2 API retry for remaining papers",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-16T04:19:57.945361+00:00_

=== rizzardo2026 === ERROR: HTTP Error 429: 
=== grant2026 === ERROR: HTTP Error 429: 
=== fang2025_dualvla === ERROR: HTTP Error 429:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-16T04:19:57.945578+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.05487 authors \"Observing and Controlling Features in Vision-Language-Action Models\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.05487 authors \"Observing and Controlling Features in Vision-Language-Action Models\""
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-16T04:19:57.945713+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2511.22134 DualVLA full author list Fang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2511.22134 DualVLA full author list Fang"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-16T04:19:57.945848+00:00_

Web search results for query: "arxiv 2511.22134 DualVLA full author list Fang"

Links: [{"title":"[2511.22134] DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/abs/2511.22134"},{"title":"DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/html/2511.22134"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=694&show=1000"},{"title":"Computation and Language","url":"https://www.arxiv.org/list/cs.CL/recent?skip=284&show=100"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=205&show=2000"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/recent?skip=70&show=2000"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=7575&show=2000"},{"title":"Computer Science Nov 2024","url":"https://arxiv.org/list/cs/2024-11?skip=2275&show=1000"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=325&show=2000"},{"title":"[2511.01183] QiMeng-NeuComBack: Self-Evolving Translation from IR to Assembly Code","url":"https://arxiv.org/abs/2511.01183"}]

Based on the search results, I found the full author list for the arXiv paper 2511.22134 titled "DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action":

The authors are: Zhen Fang, Zhuoyang Liu, Jiaming Liu, Hao Chen, Yu Zeng, Shiting Huang, Zehui Chen, Lin Chen, Shanghang Zhang, and Feng Zhao.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-16T04:19:57.946045+00:00_

Web search results for query: "arxiv 2603.05487 authors "Observing and Controlling Features in Vision-Language-Action Models""

Links: [{"title":"[2603.05487] Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05487"},{"title":"Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/html/2603.05487v1"},{"title":"(PDF) Observing and Controlling Features in Vision-Language-Action Models","url":"https://www.researchgate.net/publication/401601449_Observing_and_Controlling_Features_in_Vision-Language-Action_Models"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"A Survey on Vision-Language-Action Models for Autonomous Driving","url":"https://arxiv.org/html/2506.24044v1"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.15618v2"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"How Do Vision-Language Models Process Conflicting Information Across Modalities?","url":"https://arxiv.org/html/2507.01790v1"}]

Based on the web search results, here is the information about arxiv paper 2603.05487:

## Paper Details

**Title:** Observing and Controlling Features in Vision-Language-Action Models

**Authors:** Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann and Marco Pavone

**Submission Date:** 5 Mar 2026

## Summary

Vision-Language-Action Models (VLAs) have shown remarkable progress towards embodied intelligence. While their architecture partially resembles t
…[truncated 705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-16T04:19:57.946257+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "old_string": "% [VERIFY] Cannot confirm full bibliographic details. Cited for behavioral visual dominance in VLA policies.\n@article{grant2026,\n  title     = {[VERIFY] Behavioral Visual Dominance in Vision-Language-Action Policies},\n  author    = {Grant, [VERIFY]},\n  journal   = {[VERIFY]},\n  year      = {2026},\n}",
  "new_string": "% [UNVERIFIED] Could not find this paper via S2 or web search\n@article{grant2026,\n  title     = {[UNVERIFIED] Behavioral Visual Dominance in Vision-Language-Action Policies},\n  author    = {Grant, [UNVERIFIED]},\n  journal   = {[UNVERIFIED]},\n  year      = {2026},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "old_string": "% [VERIFY] Cannot confirm full bibliographic details. Cited for behavioral visual dominance in VLA policies.\n@article{grant2026,\n  title     = {[VERIFY] Behavioral Visual Dominance in Vision-Language-Action Policies},\n  author    = {Grant, [VERIFY]},\n  journal   = {[VERIFY]},\n  year      = {2026},\n}",
    "new_string": "% [UNVERIFIED] Could not find this paper via S2 or web search\n@article{grant2026,\n  title     = {[UNVERIFIED] Behavioral Visual Dominance in Vision-Language-Action Policies},\n  author    = {Grant, [UNVERIFIED]},\n  journal   = {[UNVERIFIED]},\n  year      = {2026},\n}"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-16T04:19:57.946418+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-16T04:19:57.946547+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "old_string": "% [VERIFY] Cannot confirm full bibliographic details. Cited for VLA interpretability.\n@article{haon2025,\n  title     = {[VERIFY] Interpretability of Vision-Language-Action Models},\n  author    = {Haon, [VERIFY]},\n  journal   = {[VERIFY]},\n  year      = {2025},\n}",
  "new_string": "@article{haon2025,\n  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},\n  author    = {H{\\\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},\n  journal   = {arXiv preprint arXiv:2509.00328},\n  year      = {2025},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "old_string": "% [VERIFY] Cannot confirm full bibliographic details. Cited for VLA interpretability.\n@article{haon2025,\n  title     = {[VERIFY] Interpretability of Vision-Language-Action Models},\n  author    = {Haon, [VERIFY]},\n  journal   = {[VERIFY]},\n  year      = {2025},\n}",
    "new_string": "@article{haon2025,\n  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},\n  author    = {H{\\\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},\n  journal   = {arXiv preprint arXiv:2509.00328},\n  year      = {2025},\n}"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-16T04:19:57.946688+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-16T04:19:57.946805+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-16T04:19:57.946981+00:00_

1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	% [VERIFY] Confirm venue and exact title. Likely "Prismatic VLMs" or OpenVLA architecture companion.
11	@article{karamcheti2024,
12	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
13	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
14	  journal   = {arXiv preprint arXiv:2402.07865},
15	  year      = {2024},
16	}
17	
18	@article{brohan2023_rt2,
19	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
20	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
21	  journal   = {arXiv preprint arXiv:2307.15818},
22	  year      = {2023},
23	}
24	
25	% === Benchmark ===
26	
27	@inproceedings{liu2023_libero,
28	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
29	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
30	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
31	  year      = {2023},
32	}
33	
34	% === Representation Analysis Methods ===
35	
36	@article{kriegeskorte2008,
37	  title     = {Representational Similarity Analysis -- Connecting 
…[truncated 2691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-16T04:19:57.947175+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "old_string": "@article{haon2025,\n  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},\n  author    = {H{\\\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},\n  journal   = {arXiv preprint arXiv:2509.00328},\n  year      = {2025},\n}",
  "new_string": "@article{haon2025,\n  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},\n  author    = {H{\\\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},\n  journal   = {arXiv preprint arXiv:2509.00328},\n  year      = {2025},\n}\n\n% === Behavioral Analysis of VLAs ===\n\n@article{hou2026,\n  title     = {{LangGap}: Diagnosing and Closing the Language Gap in Vision-Language-Action Models},\n  author    = {Hou, Yuchen and Zhao, Lin},\n  journal   = {arXiv preprint arXiv:2603.00592},\n  year      = {2026},\n}\n\n@article{fei2025,\n  title     = {{LIBERO-Plus}: In-depth Robustness Analysis of Vision-Language-Action Models},\n  author    = {Fei, Senyu and Wang, Siyin and Shi, Junhao and Dai, Zihao and Cai, Jikun and Qian, Pengfang and Ji, Li and He, Xinzhe and Zhang, Shiduo and Fei, Zhaoye and Fu, Jinlan and Gong, Jingjing and Qiu, Xipeng},\n  journal   = {arXiv preprint arXiv:2510.13626},\n  year      = {2025},\n}\n\n% === Mechanistic Interpretability of VLAs ===\n\n@article{swann2026,\n  title     = {Sparse Autoencoders Reveal Interpretable and Steerable Features in {VLA} Models},\n  author    = {Swann, Aiden and McGranahan, Lachlain and Buurmeijer, Hugo and Kennedy, Monroe and Schwager, Mac},\n  journal   = {arXiv preprint arXiv:2603.19183},\n  year      = {2026},\n}\n\n% NOTE: related_work.tex cites \"Rizzardo et al. (2026)\" but the matching paper is by Buurmeijer et al.\n@article{rizzardo2026,\n  title     = {Observing and Controlling Features in Vision-Language-Action Models},\n  author    = {Buurmeijer, Hugo and Amo Alonso, Carmen and Swann, Aiden and Pavone, Marco},\n  journal   = {arXiv preprint arXiv:2603.05487},\n  year      = {2026},\n}\n\n@article{lu2025,\n  title     = {Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture},\n  author    = {Lu, Hong and Li, Hengxu and Shahani, Prithviraj Singh and Herbers, Stephanie and Scheutz, Matthias},\n  journal   = {arXiv preprint arXiv:2502.04558},\n  year      = {2025},\n}\n\n@article{molinari2025,\n  title     = {Emergent World Representations in {OpenVLA}},\n  author    = {Molinari, Marco and Nevali, Leonardo and Navani, Saharsha and Younis, Omar G.},\n  journal   = {arXiv preprint arXiv:2509.24559},\n  year      = {2025},\n}\n\n% === Probing Methods ===\n\n@article{belinkov2022,\n  title     = {Probing Classifiers: Promises, Shortcomings, and Advances},\n  author    = {Belinkov, Yonatan},\n  journal   = {Computational Linguistics},\n  volume    = {48},\n  number    = {1},\n  pages     = {207--219},\n  year      = {2022},\n}\n\n% === VLA Fine-tuning and Reasoning ===\n\n@article{fang2025,\n  title     = {{DualVLA}: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action},\n  author    = {Fang, Zhen and Liu, Zhuoyang and Liu, Jiaming and Chen, Hao and Zeng, Yu and Huang, Shiting and Chen, Zehui and Chen, Lin and Zhang, Shanghang and Zhao, Feng},\n  journal   = {arXiv preprint arXiv:2511.22134},\n  year      = {2025},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "old_string": "@article{haon2025,\n  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},\n  author    = {H{\\\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},\n  journal   = {arXiv preprint arXiv:2509.00328},\n  year      = {2025},\n}",
    "new_string": "@article{haon2025,\n  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},\n  author    = {H{\\\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},\n  journal   = {arXiv preprint arXiv:2509.00328},\n  year      = {2025},\n}\n\n% === Behavioral Analysis of VLAs ===\n\n@article{hou2026,\n  title     = {{LangGap}: Diagnosing and Closing the Language Gap in Vision-Language-Action Models},\n  author    = {Hou, Yuchen and Zhao, Lin},\n  journal   = {arXiv preprint arXiv:2603.00592},\n  year      = {2026},\n}\n\n@article{fei2025,\n  title     = {{LIBERO-Plus}: In-depth Robustness Analysis of Vision-Language-Action Models},\n  author    = {Fei, Senyu and Wang, Siyin and Shi, Junhao and Dai, Zihao and Cai, Jikun and Qian, Pengfang and Ji, Li and He, Xinzhe and Zhang, Shiduo and Fei, Zhaoye and Fu, Jinlan and Gong, Jingjing and Qiu, Xipeng},\n  journal   = {arXiv preprint arXiv:2510.13626},\n  year      = {2025},\n}\n\n% === Mechanistic Interpretability of VLAs ===\n\n@article{swann2026,\n  title     = {Sparse Autoencoders Reveal Interpretable and Steerable Features in {VLA} Models},\n  author    = {Swann, Aiden and McGranahan, Lachlain and Buurmeijer, Hugo and Kennedy, Monroe and Schwager, Mac},\n  journal   = {arXiv preprint arXiv:2603.19183},\n  year      = {2026},\n}\n\n% NOTE: related_work.tex cites \"Rizzardo et al. (2026)\" but the matching paper is by Buurmeijer et al.\n@article{rizzardo2026,\n  title     = {Observing and Controlling Features in Vision-Language-Action Models},\n  author    = {Buurmeijer, Hugo and Amo Alonso, Carmen and Swann, Aiden and Pavone, Marco},\n  journal   = {arXiv preprint arXiv:2603.05487},\n  year      = {2026},\n}\n\n@article{lu2025,\n  title     = {Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture},\n  author    = {Lu, Hong and Li, Hengxu and Shahani, Prithviraj Singh and Herbers, Stephanie and Scheutz, Matthias},\n  journal   = {arXiv preprint arXiv:2502.04558},\n  year      = {2025},\n}\n\n@article{molinari2025,\n  title     = {Emergent World Representations in {OpenVLA}},\n  author    = {Molinari, Marco and Nevali, Leonardo and Navani, Saharsha and Younis, Omar G.},\n  journal   = {arXiv preprint arXiv:2509.24559},\n  year      = {2025},\n}\n\n% === Probing Methods ===\n\n@article{belinkov2022,\n  title     = {Probing Classifiers: Promises, Shortcomings, and Advances},\n  author    = {Belinkov, Yonatan},\n  journal   = {Computational Linguistics},\n  volume    = {48},\n  number    = {1},\n  pages     = {207--219},\n  year      = {2022},\n}\n\n% === VLA Fine-tuning and Reasoning ===\n\n@article{fang2025,\n  title     = {{DualVLA}: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action},\n  author    = {Fang, Zhen and Liu, Zhuoyang and Liu, Jiaming and Chen, Hao and Zeng, Yu and Huang, Shiting and Chen, Zehui and Chen, Lin and Zhang, Shanghang and Zhao, Feng},\n  journal   = {arXiv preprint arXiv:2511.22134},\n  year      = {2025},\n}"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-16T04:19:57.947361+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-16T04:19:57.947490+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c '@article\\|@inproceedings\\|@misc' /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c '@article\\|@inproceedings\\|@misc' /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "description": "Count bib entries"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-16T04:19:57.947608+00:00_

20

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_completion_20260516T041312",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 97 · 2026-05-16T04:19:57.947761+00:00_

原来 12 条，现在 20 条，增加了 8 条新条目。

**结果汇总：**

| 条目 | 状态 | 论文 | arXiv |
|------|------|------|-------|
| swann2026 | 已添加 | Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models | 2603.19183 |
| rizzardo2026 | 已添加 | Observing and Controlling Features in VLA Models | 2603.05487 |
| molinari2025 | 已添加 | Emergent World Representations in OpenVLA | 2509.24559 |
| belinkov2022 | 已添加 | Probing Classifiers: Promises, Shortcomings, and Advances | CL 48(1) |
| lu2025 | 已添加 | Probing a VLA Model for Symbolic States... | 2502.04558 |
| hou2026 | 已添加 | LangGap: Diagnosing and Closing the Language Gap in VLAs | 2603.00592 |
| fei2025 | 已添加 | LIBERO-Plus: In-depth Robustness Analysis of VLAs | 2510.13626 |
| fang2025 | 已添加 | DualVLA: Building a Generalizable Embodied Agent... | 2511.22134 |
| haon2025 | 已验证替换 | Mechanistic Interpretability for Steering VLAs (Bear Häon et al.) | 2509.00328 |
| grant2026 | 未找到 | 标记 [UNVERIFIED]，S2 和 web search 均无结果 | — |

**需注意两个问题：**

1. **rizzardo2026**：related_work.tex 写的是 "Rizzardo et al.~(2026)"，但实际论文作者是 Buurmeijer, Amo Alonso, Swann, Pavone——没有 Rizzardo 这个作者。tex 中的作者名需要修正。

2. **grant2026**：经过多轮搜索（S2 API + 多种关键词 WebSearch）均无法找到。\cite{grant2026} 在 tex 中出现两次（L10, L34），可能是虚构引用，建议核实或替换。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_bib_completion_20260516T041312"
}
```

</details>

---
