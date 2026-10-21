# research topk ablation lit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 0
- **Tool calls:** 35
- **Original source:** `logs/chats/worker_research_topk_ablation_lit_20260516T002831.jsonl`
- **Structured JSON:** [`9235f50c85a816076e05.json`](../../sessions/92/9235f50c85a816076e05.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

71 recorded events

### Tool call

_source line 1 · 2026-05-16T00:32:34.976144+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T00:32:34.976607+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T00:32:34.976850+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T00:32:34.977196+00:00_

Error: result (68,498 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/mcp-agent-ml-research-read_project_file-1778891323627.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/mcp-agent-ml-research-read_project_file-1778891323627.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T00:32:34.977461+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/mcp-agent-ml-research-read_project_file-1778891323627.txt | python3 -c \"\nimport sys, json\ndata = json.load(sys.stdin)\ntext = data['result']\n# Search for relevant keywords\nkeywords = ['rejection sampling', 'best-of', 'top.k', 'top_k', 'rerank', 'RLHF', 'RLAIF', 'reward model', 'selection noise', 'data quality', 'k sensitivity', 'ablation.*k', 'candidate', 'best.of.N', 'sample selection']\nimport re\nlines = text.split('\\n')\nfor i, line in enumerate(lines):\n    for kw in keywords:\n        if re.search(kw, line, re.IGNORECASE):\n            # Print context: 3 lines before and 5 after\n            start = max(0, i-3)\n            end = min(len(lines), i+6)\n            print(f'--- Match [{kw}] at line {i} ---')\n            for j in range(start, end):\n                print(f'{j}: {lines[j]}')\n            print()\n            break\n\" 2>&1 | head -500",
  "description": "Search literature map for rejection sampling, top-k, reranking keywords"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/mcp-agent-ml-research-read_project_file-1778891323627.txt | python3 -c \"\nimport sys, json\ndata = json.load(sys.stdin)\ntext = data['result']\n# Search for relevant keywords\nkeywords = ['rejection sampling', 'best-of', 'top.k', 'top_k', 'rerank', 'RLHF', 'RLAIF', 'reward model', 'selection noise', 'data quality', 'k sensitivity', 'ablation.*k', 'candidate', 'best.of.N', 'sample selection']\nimport re\nlines = text.split('\\n')\nfor i, line in enumerate(lines):\n    for kw in keywords:\n        if re.search(kw, line, re.IGNORECASE):\n            # Print context: 3 lines before and 5 after\n            start = max(0, i-3)\n            end = min(len(lines), i+6)\n            print(f'--- Match [{kw}] at line {i} ---')\n            for j in range(start, end):\n                print(f'{j}: {lines[j]}')\n            print()\n            break\n\" 2>&1 | head -500",
    "description": "Search literature map for rejection sampling, top-k, reranking keywords"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T00:32:34.977698+00:00_

&lt;persisted-output>
Output too large (82.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/b3xluxyob.txt

Preview (first 2KB):
--- Match [rejection sampling] at line 0 ---
0: {"success": true, "data": {"path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml", "content": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion)\n\npapers:\n\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\n\n  - title: \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"\n    authors: NVIDIA Labs\n    year: 2025\n    venue: ICML 2026\n    url: https://arxiv.org/abs/2601.05242\n    category: reward_diversity\n    role: closest_prior_work\n    key_finding: >\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\n      保留多 reward 的相对差异，显著提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\n\n  - title: \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\"\n    authors: Xiwen Chen et al.\n    year: 2025\n    venue: arXiv 2505.09655\n    url: https://arxiv.org/abs/2505.09655\n    category: reward_diversity\n    role: related_method\n    key_finding: >\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\
…[truncated 293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T00:32:34.977870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/b3xluxyob.txt",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/b3xluxyob.txt",
    "limit": "300"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T00:32:34.978003+00:00_

File content (30621 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T00:32:34.978123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/b3xluxyob.txt",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/b3xluxyob.txt",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T00:32:34.978260+00:00_

File content (30621 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T00:32:34.978385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/b3xluxyob.txt",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/b3xluxyob.txt",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T00:32:34.978501+00:00_

File content (30621 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T00:32:34.978621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/b3xluxyob.txt",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/b3xluxyob.txt",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T00:32:34.978735+00:00_

File content (30621 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T00:32:34.978864+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/b3xluxyob.txt | python3 -c \"\nimport sys, json, re\ndata = sys.stdin.read()\nlines = data.split('\\n')\n\n# Find all match blocks and deduplicate\nseen = set()\nresults = []\ni = 0\nwhile i < len(lines):\n    if lines[i].startswith('--- Match ['):\n        block_lines = [lines[i]]\n        i += 1\n        while i < len(lines) and not lines[i].startswith('--- Match [') and lines[i].strip() != '':\n            block_lines.append(lines[i])\n            i += 1\n        # Use the line range as dedup key\n        key = block_lines[0]\n        if key not in seen:\n            seen.add(key)\n            results.append('\\n'.join(block_lines))\n    else:\n        i += 1\n\nfor r in results:\n    print(r)\n    print()\n\" 2>&1 | head -300",
  "description": "Deduplicate and list all matched sections from literature map"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/b3xluxyob.txt | python3 -c \"\nimport sys, json, re\ndata = sys.stdin.read()\nlines = data.split('\\n')\n\n# Find all match blocks and deduplicate\nseen = set()\nresults = []\ni = 0\nwhile i < len(lines):\n    if lines[i].startswith('--- Match ['):\n        block_lines = [lines[i]]\n        i += 1\n        while i < len(lines) and not lines[i].startswith('--- Match [') and lines[i].strip() != '':\n            block_lines.append(lines[i])\n            i += 1\n        # Use the line range as dedup key\n        key = block_lines[0]\n        if key not in seen:\n            seen.add(key)\n            results.append('\\n'.join(block_lines))\n    else:\n        i += 1\n\nfor r in results:\n    print(r)\n    print()\n\" 2>&1 | head -300",
    "description": "Deduplicate and list all matched sections from literature map"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T00:32:34.979072+00:00_

&lt;persisted-output>
Output too large (82.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/bif3y4ek9.txt

Preview (first 2KB):
--- Match [rejection sampling] at line 0 ---
0: {"success": true, "data": {"path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml", "content": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion)\n\npapers:\n\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\n\n  - title: \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"\n    authors: NVIDIA Labs\n    year: 2025\n    venue: ICML 2026\n    url: https://arxiv.org/abs/2601.05242\n    category: reward_diversity\n    role: closest_prior_work\n    key_finding: >\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\n      保留多 reward 的相对差异，显著提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\n\n  - title: \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\"\n    authors: Xiwen Chen et al.\n    year: 2025\n    venue: arXiv 2505.09655\n    url: https://arxiv.org/abs/2505.09655\n    category: reward_diversity\n    role: related_method\n    key_finding: >\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\
…[truncated 293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T00:32:34.979269+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/mcp-agent-ml-research-read_project_file-1778891323627.txt | python3 -c \"\nimport sys, json, re, yaml\n\ndata = json.load(sys.stdin)\ntext = data['result']\n\n# Extract YAML content from the result\nyaml_start = text.find('papers:')\nif yaml_start < 0:\n    print('No papers section found')\n    sys.exit()\n\nyaml_text = text[yaml_start:]\n# Parse as YAML\nparsed = yaml.safe_load(yaml_text)\npapers = parsed.get('papers', [])\n\n# Search for papers mentioning rejection sampling, top-k, best-of-N, data selection, reranking\nrelevant_keywords = ['rejection.sampl', 'best.of.n', 'top.k', 'top_k', 'rerank', 'data.selection', 'data.quality', 'sample.selection', 'candidate.select', 'noise.*train', 'train.*noise', 'k.sensit']\n\nrelevant_papers = []\nfor p in papers:\n    if not isinstance(p, dict):\n        continue\n    text_to_search = json.dumps(p, ensure_ascii=False).lower()\n    for kw in relevant_keywords:\n        if re.search(kw, text_to_search):\n            relevant_papers.append((kw, p.get('title', 'Unknown'), p.get('category', ''), p.get('key_finding', ''), p.get('relevance_to_ced_stabilizer', p.get('relevance_to_freige', ''))))\n            break\n\nprint(f'Found {len(relevant_papers)} relevant papers:')\nfor kw, title, cat, finding, rel in relevant_papers:\n    print(f'\\n=== {title} ===')\n    print(f'  Category: {cat}')\n    print(f'  Matched: {kw}')\n    print(f'  Key finding: {str(finding)[:500]}')\n    print(f'  Relevance: {str(rel)[:500]}')\n\" 2>&1",
  "description": "Parse YAML and find papers related to rejection sampling, top-k, data selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/mcp-agent-ml-research-read_project_file-1778891323627.txt | python3 -c \"\nimport sys, json, re, yaml\n\ndata = json.load(sys.stdin)\ntext = data['result']\n\n# Extract YAML content from the result\nyaml_start = text.find('papers:')\nif yaml_start < 0:\n    print('No papers section found')\n    sys.exit()\n\nyaml_text = text[yaml_start:]\n# Parse as YAML\nparsed = yaml.safe_load(yaml_text)\npapers = parsed.get('papers', [])\n\n# Search for papers mentioning rejection sampling, top-k, best-of-N, data selection, reranking\nrelevant_keywords = ['rejection.sampl', 'best.of.n', 'top.k', 'top_k', 'rerank', 'data.selection', 'data.quality', 'sample.selection', 'candidate.select', 'noise.*train', 'train.*noise', 'k.sensit']\n\nrelevant_papers = []\nfor p in papers:\n    if not isinstance(p, dict):\n        continue\n    text_to_search = json.dumps(p, ensure_ascii=False).lower()\n    for kw in relevant_keywords:\n        if re.search(kw, text_to_search):\n            relevant_papers.append((kw, p.get('title', 'Unknown'), p.get('category', ''), p.get('key_finding', ''), p.get('relevance_to_ced_stabilizer', p.get('relevance_to_freige', ''))))\n            break\n\nprint(f'Found {len(relevant_papers)} relevant papers:')\nfor kw, title, cat, finding, rel in relevant_papers:\n    print(f'\\n=== {title} ===')\n    print(f'  Category: {cat}')\n    print(f'  Matched: {kw}')\n    print(f'  Key finding: {str(finding)[:500]}')\n    print(f'  Relevance: {str(rel)[:500]}')\n\" 2>&1",
    "description": "Parse YAML and find papers related to rejection sampling, top-k, data selection"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T00:32:34.979419+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 16, in &lt;module>
    papers = parsed.get('papers', [])
             ^^^^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T00:32:34.979546+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/mcp-agent-ml-research-read_project_file-1778891323627.txt | python3 -c \"\nimport sys, json, re\n\ndata = json.load(sys.stdin)\ntext = data['result']\n\n# Split into paper entries by looking for '  - title:' pattern\nentries = re.split(r'\\n  - title:', text)\n\nrelevant_keywords = ['rejection.sampl', 'best.of.n', 'top.k', 'top_k', 'rerank', 'data.selection', 'data.quality', 'sample.selection', 'candidate.select', 'noise.*train', 'train.*noise', 'k.sensit', 'best-of', 'sampling.*quality', 'quality.*sampling']\n\nprint(f'Total entries: {len(entries)}')\n\nfor i, entry in enumerate(entries):\n    if i == 0:\n        continue  # header\n    entry_lower = entry.lower()\n    for kw in relevant_keywords:\n        if re.search(kw, entry_lower):\n            # Get title\n            title_line = entry.split('\\n')[0].strip().strip('\\\"')\n            print(f'\\n===== [{kw}] {title_line} =====')\n            # Print first 800 chars\n            print(entry[:800])\n            print('...')\n            break\n\" 2>&1",
  "description": "Find papers in literature map related to rejection sampling and top-k selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/mcp-agent-ml-research-read_project_file-1778891323627.txt | python3 -c \"\nimport sys, json, re\n\ndata = json.load(sys.stdin)\ntext = data['result']\n\n# Split into paper entries by looking for '  - title:' pattern\nentries = re.split(r'\\n  - title:', text)\n\nrelevant_keywords = ['rejection.sampl', 'best.of.n', 'top.k', 'top_k', 'rerank', 'data.selection', 'data.quality', 'sample.selection', 'candidate.select', 'noise.*train', 'train.*noise', 'k.sensit', 'best-of', 'sampling.*quality', 'quality.*sampling']\n\nprint(f'Total entries: {len(entries)}')\n\nfor i, entry in enumerate(entries):\n    if i == 0:\n        continue  # header\n    entry_lower = entry.lower()\n    for kw in relevant_keywords:\n        if re.search(kw, entry_lower):\n            # Get title\n            title_line = entry.split('\\n')[0].strip().strip('\\\"')\n            print(f'\\n===== [{kw}] {title_line} =====')\n            # Print first 800 chars\n            print(entry[:800])\n            print('...')\n            break\n\" 2>&1",
    "description": "Find papers in literature map related to rejection sampling and top-k selection"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T00:32:34.979679+00:00_

Total entries: 1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T00:32:34.979799+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/mcp-agent-ml-research-read_project_file-1778891323627.txt | python3 -c \"\nimport sys, json, re\n\ndata = json.load(sys.stdin)\ntext = data['result']\n\n# The YAML is inside the JSON result field. Let's search directly with context\nkeywords = ['rejection.sampl', 'best.of.n', 'best-of-n', 'top.k', 'top_k', 'rerank', 'data.selection', 'data.quality', 'sample.selection', 'noise.*train', 'k.sensit', 'rsft', 'RSFT']\n\nlines = text.split('\\n')\nmatched_regions = set()\n\nfor kw in keywords:\n    for i, line in enumerate(lines):\n        if re.search(kw, line, re.IGNORECASE):\n            # Find the paper title above this line\n            region_start = i\n            for j in range(i, max(i-30, 0), -1):\n                if '- title:' in lines[j] or 'title:' in lines[j]:\n                    region_start = j\n                    break\n            region_end = min(i + 10, len(lines))\n            region_key = region_start\n            if region_key not in matched_regions:\n                matched_regions.add(region_key)\n                print(f'--- [{kw}] lines {region_start}-{region_end} ---')\n                for k in range(region_start, region_end):\n                    print(lines[k])\n                print()\n\" 2>&1 | head -400",
  "description": "Search literature map with context around matched keywords"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/mcp-agent-ml-research-read_project_file-1778891323627.txt | python3 -c \"\nimport sys, json, re\n\ndata = json.load(sys.stdin)\ntext = data['result']\n\n# The YAML is inside the JSON result field. Let's search directly with context\nkeywords = ['rejection.sampl', 'best.of.n', 'best-of-n', 'top.k', 'top_k', 'rerank', 'data.selection', 'data.quality', 'sample.selection', 'noise.*train', 'k.sensit', 'rsft', 'RSFT']\n\nlines = text.split('\\n')\nmatched_regions = set()\n\nfor kw in keywords:\n    for i, line in enumerate(lines):\n        if re.search(kw, line, re.IGNORECASE):\n            # Find the paper title above this line\n            region_start = i\n            for j in range(i, max(i-30, 0), -1):\n                if '- title:' in lines[j] or 'title:' in lines[j]:\n                    region_start = j\n                    break\n            region_end = min(i + 10, len(lines))\n            region_key = region_start\n            if region_key not in matched_regions:\n                matched_regions.add(region_key)\n                print(f'--- [{kw}] lines {region_start}-{region_end} ---')\n                for k in range(region_start, region_end):\n                    print(lines[k])\n                print()\n\" 2>&1 | head -400",
    "description": "Search literature map with context around matched keywords"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T00:32:34.980013+00:00_

&lt;persisted-output>
Output too large (82.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/bgpuijbud.txt

Preview (first 2KB):
--- [rejection.sampl] lines 0-1 ---
{"success": true, "data": {"path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml", "content": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion)\n\npapers:\n\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\n\n  - title: \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"\n    authors: NVIDIA Labs\n    year: 2025\n    venue: ICML 2026\n    url: https://arxiv.org/abs/2601.05242\n    category: reward_diversity\n    role: closest_prior_work\n    key_finding: >\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\n      保留多 reward 的相对差异，显著提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\n\n  - title: \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\"\n    authors: Xiwen Chen et al.\n    year: 2025\n    venue: arXiv 2505.09655\n    url: https://arxiv.org/abs/2505.09655\n    category: reward_diversity\n    role: related_method\n    key_finding: >\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\n      等价于 I
…[truncated 293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T00:32:34.980197+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n -i -E \"rejection.sampl|best.of.n|top.k|top_k|rerank|data.quality|sample.select|k.sensit|rsft|RSFT\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml 2>/dev/null | head -80",
  "description": "Search YAML file directly for relevant keywords"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n -i -E \"rejection.sampl|best.of.n|top.k|top_k|rerank|data.quality|sample.select|k.sensit|rsft|RSFT\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml 2>/dev/null | head -80",
    "description": "Search YAML file directly for relevant keywords"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T00:32:34.980385+00:00_

2:# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE
283:  # === Category 6: RSFT Methodology & Theory ===
285:  - title: "A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce"
290:    category: rsft_methodology
293:      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。
297:      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。
298:    relevance_to_rsft_docre: >
299:      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，
300:      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；
301:      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；
303:      强化了 offline RSFT 的合理性。
305:  - title: "Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)"
310:    category: rsft_methodology
313:      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，
315:    relevance_to_rsft_docre: >
316:      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。
320:  - title: "Rejection Sampling Based Fine Tuning Secretly Performs PPO"
325:    category: rsft_methodology
328:      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning
330:    relevance_to_rsft_docre: >
331:      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为
357:    relevance_to_rsft_docre: >
359:      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。
376:    relevance_to_rsft_docre: >
378:      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。
390:    relevance_to_rsft_docre: >
392:      且使用 offline RSFT 而非 online RL。
404:    relevance_to_rsft_docre: >
406:      与我们 RSFT 直接微调 LLM 的方法路径不同。
418:    relevance_to_rsft_docre: >
442:    relevance_to_rsft_docre: >
444:      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。
445:      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。
467:    relevance_to_rsft_docre: >
470:      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。
487:    relevance_to_rsft_docre: >
512:    relevance_to_rsft_docre: >
538:    relevance_to_rsft_docre: >
541:      RSFT 在此基
…[truncated 2927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T00:32:34.980550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": "1218",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "offset": "1218",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T00:32:34.980791+00:00_

1218	    venue: TMLR 2024
1219	    url: https://arxiv.org/abs/2304.06767
1220	    category: rsft_offline_rl
1221	    role: background
1222	    key_finding: >
1223	      RAFT 是 rejection sampling fine-tuning 的标准化框架：迭代式 generate → rank → filter → SFT。
1224	      每轮生成 n 个 response，用 reward model 排序，取 top-k 做 SFT。
1225	      在文本生成和对话上验证有效性，提供了 RSFT 的 canonical 实现。
1226	    relevance_to_freige: >
1227	      我们的 RSFT pipeline 直接基于 RAFT 框架。差异在于：
1228	      (1) 我们用 verifiable reward（F1 score）替代 learned reward model；
1229	      (2) 我们的 filtering 基于 extraction F1 threshold 而非 top-k ranking；
1230	      (3) 我们额外引入 CED reward 维度用于 inference-time reranking。
1231	
1232	  # === Category 7: Evidence-based DocRE (Expanded) ===
1233	
1234	  - title: "EAAGRE: Evidence and Axial Attention Guided Document-level Relation Extraction"
1235	    authors: Unknown (Computer Speech and Language)
1236	    year: 2024
1237	    venue: Computer Speech and Language 2024
1238	    url: https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116
1239	    category: evidence_docre
1240	    role: related_method
1241	    key_finding: >
1242	      联合考虑 evidence information 和 relation triple 的全局交互。
1243	      直接引导 PLM encoder 最后一层的 top-k token attention 到 evidence sentences，
1244	      不引入额外可训练参数。Axial attention 建模 relation triple 之间的全局相互依赖。
1245	    relevance_to_freige: >
1246	      与 DREEAM 属于同一 evidence-guided attention 范式。
1247	      EAAGRE 的无参数 evidence attention 与我们 CED reranker 的 post-hoc 方式形成对比——
1248	      前者在 encoder 内部注入 evidence signal，后者在 generation 后验证。
1249	      证明 evidence 信号无论注入位置都能提升 DocRE 性能。
1250	
1251	  - title: "GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction"
1252	    authors: Yanxu Mao et al.
1253	    year: 2024
1254	    venue: arXiv 2407.21384
1255	    url: https://arxiv.org/abs/2407.21384
1256	    category: evidence_docre
1257	    role: related_method

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T00:32:34.981031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": "1197",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "offset": "1197",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T00:32:34.981177+00:00_

1197	      "structured output 任务中 offline 方法优于 online GRPO"的普遍性论述。
1198	
1199	  - title: "RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models"
1200	    authors: Anonymous
1201	    year: 2024
1202	    venue: NAACL 2024 Findings
1203	    url: https://arxiv.org/abs/2402.10038
1204	    category: rsft_offline_rl
1205	    role: method-component
1206	    key_finding: >
1207	      系统性结合 rejection sampling 和 DPO。从 SFT 模型采样 k 个 response per prompt，
1208	      根据 reward 分布识别 contrastive pairs，用 DPO 对齐。
1209	      在有限资源环境下有效微调 LLM，超越独立的 RS、PPO 和 DPO。
1210	    relevance_to_freige: >
1211	      RS-DPO 提供了 rejection sampling 和 preference optimization 的桥梁方法。
1212	      我们的 RSFT 只用正样本训练（SFT loss），RS-DPO 进一步利用负样本构造 preference pair。
1213	      Future work 方向：可考虑用 RS-DPO 方式利用 RSFT rejected 样本做 DPO。
1214	
1215	  - title: "RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment"
1216	    authors: Anonymous
1217	    year: 2024
1218	    venue: TMLR 2024
1219	    url: https://arxiv.org/abs/2304.06767
1220	    category: rsft_offline_rl
1221	    role: background

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T00:32:34.981344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": "283",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "offset": "283",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T00:32:34.981496+00:00_

283	  # === Category 6: RSFT Methodology & Theory ===
284	
285	  - title: "A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce"
286	    authors: Xiao et al.
287	    year: 2025
288	    venue: arXiv 2504.11343
289	    url: https://arxiv.org/abs/2504.11343
290	    category: rsft_methodology
291	    role: key_theoretical_support
292	    key_finding: >
293	      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。
294	      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。
295	      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。
296	      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，
297	      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。
298	    relevance_to_rsft_docre: >
299	      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，
300	      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；
301	      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；
302	      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，
303	      强化了 offline RSFT 的合理性。
304	
305	  - title: "Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)"
306	    authors: Jie Deng et al.
307	    year: 2026
308	    venue: arXiv 2602.04391
309	    url: https://arxiv.org/abs/2602.04391
310	    category: rsft_methodology
311	    role: method_component
312	    key_finding: >
313	      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，
314	      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。
315	    relevance_to_rsft_docre: >
316	      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。
317	      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，
318	      融合方式需要重新设计。
319	
320	  - title: "Rejection Sampling Based Fine Tuning Secretly Performs PPO"
321	    authors: Anonymous
322	    year: 2025
323	    venue: ICML 2025
324	    url: https://openreview.net/forum?id=yQ2UivKlir
325	    category: rsft_methodology
326	    role: theoretical_support
327	    key_finding: >
328	      建立 RSFT 与 PPO 之间的理论联系：rejection sampling
…[truncated 195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T00:32:34.981643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": "1155",
  "limit": "45"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "offset": "1155",
    "limit": "45"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T00:32:34.981795+00:00_

1155	      通过将 reward 条件化于最终正确性，对齐内部推理与代码正确性。
1156	    relevance_to_freige: >
1157	      P-GRPO 的"仅对成功输出奖励推理过程"与我们 RSFT 的 rejection sampling 理念一致——
1158	      都是只从高质量输出中学习。P-GRPO 的 conditional reward 思路可启发 CED 改进：
1159	      只在 RE 正确时奖励 evidence quality，避免"evidence 好但 RE 错"的情况。
1160	
1161	  # === Category 25: Rejection Sampling Fine-Tuning / Offline RL (Direction 5) ===
1162	
1163	  - title: "OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning"
1164	    authors: Anonymous
1165	    year: 2024
1166	    venue: arXiv 2412.16145
1167	    url: https://arxiv.org/abs/2412.16145
1168	    category: rsft_offline_rl
1169	    role: direct-competitor
1170	    key_finding: >
1171	      基于 maximum entropy RL 的 offline 方法，联合学习 policy model 和 value function，
1172	      优化 soft Bellman Equation。无需 paired preference data，
1173	      实现更好的 credit assignment。学到的 value function 可免费引导 test-time tree search。
1174	      在 GSM8K、MATH、ALFWorld 上超越现有 offline 方法。
1175	    relevance_to_freige: >
1176	      OREO 提供了比简单 RSFT 更理论化的 offline RL 框架。
1177	      我们的 RSFT 可视为 OREO 的特例（无 value function，简单 threshold filtering）。
1178	      Future work 方向：用 OREO 替代简单 RSFT 可能进一步提升 DocRE 性能。
1179	
1180	  - title: "PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning"
1181	    authors: Yao Lu, Dengdong Fan, Jianzheng Nie, Fan Xu, Jie Chen, Bin Zhou, Yonghong Tian
1182	    year: 2026
1183	    venue: arXiv 2601.14716
1184	    url: https://arxiv.org/abs/2601.14716
1185	    category: rsft_offline_rl
1186	    role: key_evidence
1187	    key_finding: >
1188	      基于 Qwen2.5-32B 的数学推理模型。核心创新是 offline RL 方法，
1189	      在训练稳定性和效率上优于 GRPO 等 online RL。
1190	      AIME 2024 平均 90.9%，AIME 2025 平均 85.6%，
1191	      在 Qwen2.5-32B post-training 中达 SOTA。
1192	    relevance_to_freige: >
1193	      强有力证据支持 offline RL > online RL 的论点。
1194	      PCL-Reasoner 在数学推理上用 offline RL 超越 GRPO，
1195	      与我们在 DocRE 上 RSFT 超越 GRPO 的发现一致。
1196	      两个独立领域的 converging evidence 增强了
1197	      "structur
…[truncated 187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T00:32:34.981969+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n -i -E \"best.of|bon|sample.size|k.ablat|quality.*noise|noise.*quality|number.*candidates|候选|噪声.*训练|训练.*噪声|top-k.*ablat|k.*选\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml 2>/dev/null | head -40",
  "description": "Search for more keywords: best-of-N, sample size, noise quality"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n -i -E \"best.of|bon|sample.size|k.ablat|quality.*noise|noise.*quality|number.*candidates|候选|噪声.*训练|训练.*噪声|top-k.*ablat|k.*选\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml 2>/dev/null | head -40",
    "description": "Search for more keywords: best-of-N, sample size, noise quality"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T00:32:34.982118+00:00_

440:      backbone: LLaMA3-8B
456:      再用 LLM 在精简候选空间中做多分类（RC）。
465:      backbone: BERT classifier + LLM
510:      backbone: "dual-encoder (few hundred M params)"
536:      backbone: "Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)"
578:      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。
1097:      标准量化引入静态确定性噪声，对 RL 后期训练不利。但精确控制的量化噪声
1435:      为我们的 QLoRA rank 选择提供实证指导。
1506:      但 sparse training 的 proactive conflict mitigation 需要 task-aware 的参数选择，
1529:  # === Category 13: Inference-Time Reranking / Best-of-N (New from 2025-05-16 scan) ===
1531:  - title: "Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment"
1539:      Best-of-N sampling provably suffers from reward hacking when N is large.
1542:      强调 pre-trained policy 对高质量 response 的 coverage 是 BoN 成功的关键。
1544:      直接对应 CED reranker 的理论基础。CED 作为 inference-time reward model 选择最佳候选，
1556:      证明 BoN 中 true reward 先升后降的 hacking pattern 是所有 inference-time 机制的固有属性。
1557:      提出 Best-of-Poisson (BoP) 高效近似最优 reward-KL tradeoff policy，
1564:  - title: "Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models"
1572:      提出 inference-aware fine-tuning 范式：训练时直接优化 BoN inference 策略的性能。
1573:      设计 imitation learning 和 RL 方法克服 BoN 中不可微的 argmax 操作。
1574:      BoN-aware 模型隐式学习 exploration-exploitation meta-strategy，
1579:      使模型生成 BoN-aware 的多样输出而非事后选择。
1581:  - title: "Evaluation of Best-of-N Sampling Strategies for Language Model Alignment"
1589:      系统评估 BoN 采样的 reward hacking 问题。
1590:      提出 Stochastic Regularized BoN (SRBoN) 有理论保证的方法。
1591:      发现简单的 Sentence Length Regularized BoN 也能获得 comparable 性能。
1595:      可借鉴 SRBoN 的正则化思路防止 CED reranker over-optimize evidence 而牺牲 extraction quality。
1597:  - title: "Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment"
1605:      MBR-BoN：用 Minimum Bayes Risk 目标作为 proximity regularizer 缓解 reward hacking。
1607:      在 AlpacaFarm 和 hh-rlhf 上优于 vanilla BoN 和 MBR decoding。
1609:     
…[truncated 117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T00:32:34.982311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": "1529",
  "limit": "85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "offset": "1529",
    "limit": "85"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T00:32:34.982549+00:00_

1529	  # === Category 13: Inference-Time Reranking / Best-of-N (New from 2025-05-16 scan) ===
1530	
1531	  - title: "Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment"
1532	    authors: Audrey Huang et al.
1533	    year: 2025
1534	    venue: ICML 2025
1535	    url: https://arxiv.org/abs/2503.21878
1536	    category: inference_time_reranking
1537	    role: key_baseline
1538	    key_finding: >
1539	      Best-of-N sampling provably suffers from reward hacking when N is large.
1540	      提出 InferenceTimePessimism 算法，通过 pessimism in the face of uncertainty
1541	      实现 scaling-monotonic 性能（性能不随 N 增大而退化）。
1542	      强调 pre-trained policy 对高质量 response 的 coverage 是 BoN 成功的关键。
1543	    relevance_to_freige: >
1544	      直接对应 CED reranker 的理论基础。CED 作为 inference-time reward model 选择最佳候选，
1545	      该论文的 pessimism 原则可指导 CED reranker 的 threshold 设计——
1546	      避免过度信任 CED score 导致 reward hacking。
1547	
1548	  - title: "Inference-Time Reward Hacking in Large Language Models"
1549	    authors: Yiwei Chen et al.
1550	    year: 2025
1551	    venue: NeurIPS 2025 Spotlight
1552	    url: https://arxiv.org/abs/2506.19248
1553	    category: inference_time_reranking
1554	    role: related_analysis
1555	    key_finding: >
1556	      证明 BoN 中 true reward 先升后降的 hacking pattern 是所有 inference-time 机制的固有属性。
1557	      提出 Best-of-Poisson (BoP) 高效近似最优 reward-KL tradeoff policy，
1558	      以及 HedgeTune 自动寻找最优 inference-time 参数。
1559	    relevance_to_freige: >
1560	      CED reranker 本质上是 inference-time 对齐。此论文警示：
1561	      即使 CED score 是高质量 reward，过度优化（选 N 过大）仍可能退化。
1562	      HedgeTune 的思路可用于自动选择 CED reranker 的最优 N。
1563	
1564	  - title: "Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models"
1565	    authors: Yinlam Chow et al.
1566	    year: 2024
1567	    venue: ICLR 2025
1568	    url: https://arxiv.org/abs/2412.15287
1569	    category: inference_time_reranking
1570	    role: method_component
1571	    key_finding: >
1572	      提
…[truncated 1946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T00:32:34.982803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": "1612",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "offset": "1612",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T00:32:34.983072+00:00_

1612	  # === Category 14: RSFT Methodology Advances (New from 2025-05-16 scan) ===
1613	
1614	  - title: "AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners"
1615	    authors: Hyung Won Chung et al.
1616	    year: 2025
1617	    venue: NeurIPS 2025
1618	    url: https://arxiv.org/abs/2505.16322
1619	    category: rsft_methodology
1620	    role: related_method
1621	    key_finding: >
1622	      RFT/RSFT 的随机数据采样导致训练不均衡——已解决的样本被过度训练，困难样本训练不足。
1623	      AdaSTaR 引入两个自适应采样原则：(1) diversity sampling 促进均衡，
1624	      (2) curriculum sampling 根据模型能力动态调整数据难度。
1625	      在 6 个 benchmark 全部取得最优，训练 FLOPs 平均减少 58.6%。
1626	    relevance_to_freige: >
1627	      直接适用于 FREIGE 的 RSFT 阶段。当前 RSFT 随机采样 CED-filtered 数据，
1628	      AdaSTaR 的 curriculum 策略可优化采样——先训简单 relation pair，再逐步引入困难的多跳关系。
1629	      其 diversity sampling 也可缓解 RSFT 数据中 relation type 分布不均的问题。
1630	
1631	  - title: "RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning"
1632	    authors: Unknown
1633	    year: 2026
1634	    venue: arXiv 2601.09253
1635	    url: https://arxiv.org/abs/2601.09253
1636	    category: rsft_methodology
1637	    role: direct_competitor
1638	    key_finding: >
1639	      RSFT 的 hard rejection 丢弃大量计算昂贵的负样本。
1640	      RIFT 保留所有轨迹，用标量 reward 重新加权 loss，
1641	      正 reward 样本鼓励正确行为，负 reward 样本提供反向梯度。
1642	      引入 stabilized loss 解决 naive reward integration 的训练坍塌问题。
1643	    relevance_to_freige: >
1644	      FREIGE 的 RSFT 同样面临 hard rejection 的效率问题——大量生成但 CED 不达标的样本被丢弃。
1645	      RIFT 的 soft reweighting 可替代 binary CED 筛选：
1646	      用 CED score 作为连续 reward 加权 SFT loss，充分利用所有生成样本。
1647	
1648	  # === Category 15: NLI for Evidence Scoring / Faithfulness (New from 2025-05-16 scan) ===
1649	
1650	  - title: "FaithLens: Detecting and Explaining Faithfulness Hallucination"
1651	    authors: Unknown
1652	    year: 2025
1653	    venue: arXiv 2512.20182
1654	    url: https://arxiv.org/abs/2512.20182
1655	    category: faithfulness_nli
1656	    role: method_component
1657	    key_find
…[truncated 1600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T00:32:34.983471+00:00_

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
  "session": "worker_research_topk_ablation_lit_20260516T002831",
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

_source line 40 · 2026-05-16T00:32:34.983644+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T00:32:34.983773+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "rejection sampling top-k training data quality degradation noise LLM fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebSearch",
  "tool_args": {
    "query": "rejection sampling top-k training data quality degradation noise LLM fine-tuning"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T00:32:34.983899+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "best-of-N selection N sensitivity reward hacking training data RLHF 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebSearch",
  "tool_args": {
    "query": "best-of-N selection N sensitivity reward hacking training data RLHF 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T00:32:34.984031+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RAFT reward ranked fine-tuning top-k ablation data quality noise"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RAFT reward ranked fine-tuning top-k ablation data quality noise"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T00:32:34.984192+00:00_

Web search results for query: "RAFT reward ranked fine-tuning top-k ablation data quality noise"

Links: [{"title":"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment","url":"https://arxiv.org/html/2304.06767v4"},{"title":"[PDF] RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RAFT:-Reward-rAnked-FineTuning-for-Generative-Model-Dong-Xiong/3ab661db57d924f4ff1706e05ac807873ca00e0a"},{"title":"Reward-Ranked Fine-Tuning (RAFT)","url":"https://www.emergentmind.com/topics/reward-ranked-fine-tuning-raft"},{"title":"Reward rAnked FineTuning (RAFT)","url":"https://www.emergentmind.com/topics/reward-ranked-finetuning-raft"},{"title":"Papers Explained 303: Reward rAnked FineTuning (RAFT) | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-303-reward-ranked-finetuning-raft-791154585908"},{"title":"[2304.06767] RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment","url":"https://arxiv.org/abs/2304.06767"},{"title":"RAFT — LMFlow documentation","url":"https://optimalscale.github.io/LMFlow/examples/raft.html"},{"title":"GitHub - RLHFlow/RAFT: This is an official implementation of the Reward rAnked Fine-Tuning Algorithm (RAFT), also known as iterative best-of-n fine-tuning or rejection sampling fine-tuning. · GitHub","url":"https://github.com/RLHFlow/RAFT"},{"title":"(PDF) RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment","url":"https://www.researchgate.net/publication/370058357_RAFT_Reward_rAnked_FineTuning_for_Generative_Foundation_Model_Alignment"},{"title":"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment | OpenReview","url":"https://openreview.net/forum?id=m7p5O7zblY"}]

I found comprehensive information about RAFT (Reward rAnked FineTuning). Here are the key findings:

## Overview
RAFT is a new framework designed to align generative models effectively, serving as an alte
…[truncated 1544 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-16T00:32:34.984413+00:00_

Web search results for query: "best-of-N selection N sensitivity reward hacking training data RLHF 2024 2025"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Inference-Time Reward Hacking in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=hSX7Dd8dxy"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/pdf/2502.18770"},{"title":"Avoiding Reward Hacking","url":"https://www.emergentmind.com/topics/avoiding-reward-hacking"},{"title":"Reward Modeling in LLM Alignment","url":"https://www.emergentmind.com/topics/reward-modeling-in-llm-alignment"},{"title":"Mitigating Reward Hacking in RLHF via Information- ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f25d75fc760aec0a6174f9f5d9da59b8-Paper-Conference.pdf"},{"title":"REWARD MODEL BOOSTING FOR RLHF","url":"https://openreview.net/pdf/2fd4b1609b392151e6692f73c18ac0a8fe54ae94.pdf"},{"title":"Pessimistic Reward Modeling in RLHF against Reward Hacking","url":"https://openreview.net/pdf?id=HWOAZUPA0C"},{"title":"Inference-Time Reward Hacking in Large Language Models Hadi Khalaf","url":"https://openreview.net/pdf?id=hSX7Dd8dxy"},{"title":"Reward Hacking Mitigation using Verifiable Composite Rewards","url":"https://arxiv.org/html/2509.15557v1"}]

I found comprehensive research on reward hacking and RLHF. Here are the key findings related to best-of-N selection, N sensitivity, reward hacking, and training data in RLHF from 2024-2025:

## Best-of-N Sampling and Reward Hacking

Best-of-N sampling (BoN) is a technique used in RLHF frameworks, and recent research has explored its sensitivity to reward hacking. Inference-time hacking occurs when overselecting based on noisy or adversarial proxy rewards at decode time leads to a collapse of alignment performance as selection pressure increases.

Research published in 2025 asks "Is best-of-n the best of
…[truncated 1184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T00:32:34.984614+00:00_

Web search results for query: "rejection sampling top-k training data quality degradation noise LLM fine-tuning"

Links: [{"title":"When Fine-Tuning Fails and when it Generalises: Role of Data Diversity and Mixed Training in LLM-based TTS","url":"https://arxiv.org/html/2603.10904"},{"title":"Rejection Sampling | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/09-rejection-sampling"},{"title":"1Cademy - Rejection Sampling for LLM Fine-Tuning","url":"https://1cademy.com/node/rejection-sampling-for-llm-fine-tuning/KccgwQodLPzOTmqGzDOH"},{"title":"Rejection Fine-Tuning (RFT)","url":"https://www.emergentmind.com/topics/rejection-fine-tuning-rft"},{"title":"Rejection Sampling & SFT in LLM Alignment","url":"https://www.emergentmind.com/topics/rejection-sampling-and-supervised-fine-tuning-sft"},{"title":"RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models","url":"https://arxiv.org/html/2402.10038v1"},{"title":"LLM Training: RLHF and Its Alternatives - Ahead of AI","url":"https://magazine.sebastianraschka.com/p/llm-training-rlhf-and-its-alternatives"},{"title":"The Ultimate Guide to Rejection Sampling in LLMs: Making AI Sound Human, One Sample at a Time | by KoshurAI | 𝐀𝐈 𝐦𝐨𝐧𝐤𝐬.𝐢𝐨 | Medium","url":"https://medium.com/aimonks/the-ultimate-guide-to-rejection-sampling-in-llms-making-ai-sound-human-one-sample-at-a-time-9e9e8c193359"},{"title":"Rejection-sampling Fine-Tuning (RFT)","url":"https://www.emergentmind.com/topics/rejection-sampling-fine-tuning-rft-ad4c417c-416b-40b6-bf9a-4653b83ddcfb"},{"title":"DeepSeek-R1: RL for LLMs Rethought | by Anna Alexandra Grigoryan | Medium","url":"https://thegrigorian.medium.com/deepseek-r1-rl-for-llms-rethought-e148445d4381"}]

I've completed the web search for your query. Here are the key findings related to rejection sampling, top-k sampling, training data quality degradation, noise, and LLM fine-tuning:

## Key Results:

**Rejection Sampling & Top-k Sampling:**
C
…[truncated 1643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T00:32:34.984838+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"rejection sampling\" \"top-k\" OR \"top k\" ablation training quality \"k=1\" OR \"k=3\" OR \"k=5\" fine-tuning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"rejection sampling\" \"top-k\" OR \"top k\" ablation training quality \"k=1\" OR \"k=3\" OR \"k=5\" fine-tuning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-16T00:32:34.985000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "best-of-N training data selection increasing N degrades quality noise accumulation reward model imperfect proxy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebSearch",
  "tool_args": {
    "query": "best-of-N training data selection increasing N degrades quality noise accumulation reward model imperfect proxy"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T00:32:34.985151+00:00_

Web search results for query: ""rejection sampling" "top-k" OR "top k" ablation training quality "k=1" OR "k=3" OR "k=5" fine-tuning 2024 2025"

Links: [{"title":"Rejection Sampling | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/09-rejection-sampling"},{"title":"Rejection Sampling & SFT in LLM Alignment","url":"https://www.emergentmind.com/topics/rejection-sampling-and-supervised-fine-tuning-sft"},{"title":"Rejection Sampling Fine-Tuning (RSFT)","url":"https://www.emergentmind.com/topics/rejection-sampling-fine-tuning-rsft"},{"title":"Rejection Sampling Based Fine Tuning Secretly Performs PPO | OpenReview","url":"https://openreview.net/forum?id=yQ2UivKlir"},{"title":"Rejection Fine-Tuning (RFT)","url":"https://www.emergentmind.com/topics/rejection-fine-tuning-rft"},{"title":"Rejection-sampling Fine-Tuning (RFT)","url":"https://www.emergentmind.com/topics/rejection-sampling-fine-tuning-rft-ad4c417c-416b-40b6-bf9a-4653b83ddcfb"},{"title":"DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving","url":"https://tongyx361.github.io/assets/dart-math/paper-dart-math.pdf"},{"title":"ICML Rejection Sampling Based Fine Tuning Secretly Performs PPO","url":"https://icml.cc/virtual/2025/48054"},{"title":"DART-Math: Difficulty-Aware Rejection Tuning for ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf"},{"title":"from Rejection Sampling to Reinforce","url":"https://openreview.net/pdf?id=eK3yDPtwIK"}]

I've completed the web search for your query about rejection sampling with top-k ablation studies related to training quality and fine-tuning from 2024-2025. Here are the key findings:

## Main Research Areas Found

**Rejection Sampling Fine-Tuning (RSFT/RFT) - Core Technique:**
RSFT has become the prevailing baseline for self-improvement in mathematical reasoning and chain-of-thought LLMs. On Qwen-2.5-Math-1.5B, RSFT achieved mean@8 accuracy 25.6% on MATH.

**Top-K Ablati
…[truncated 1091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T00:32:34.985372+00:00_

Web search results for query: "best-of-N training data selection increasing N degrades quality noise accumulation reward model imperfect proxy"

Links: [{"title":"Diffusion Model as a Noise-Aware Latent Reward Model for Step-Level Preference Optimization","url":"https://arxiv.org/html/2502.01051v5"},{"title":"Overcoming Reward Model Noise in Instruction-Guided Reinforcement Learning","url":"https://arxiv.org/html/2409.15922v1"},{"title":"Understanding the Effect of Noise in LLM Training Data with Algorithmic Chains of Thought","url":"https://arxiv.org/html/2402.04004v2"},{"title":"Dual-Stage Clean-Sample Selection for Incremental Noisy Label Learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12292581/"},{"title":"Noise injection for training artificial neural networks - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC2771718/"},{"title":"Review–A Survey of Learning from Noisy Labels - IOPscience","url":"https://iopscience.iop.org/article/10.1149/2754-2726/ac75f5"},{"title":"Deep learning with noisy labels: exploring techniques and ...","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7484266/"},{"title":"Selecting optimal training data for learning to rank | Request PDF","url":"https://www.researchgate.net/publication/220230355_Selecting_optimal_training_data_for_learning_to_rank"},{"title":"Understanding and Mitigating the Bias in Sample Selection for Learning with Noisy Labels","url":"https://arxiv.org/html/2401.13360v3"},{"title":"A probabilistic approach to training machine learning models using noisy data - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1364815224001944"}]

Based on the search results, I found several relevant papers addressing aspects of your query about best-of-N training data selection and quality degradation issues:

## Key Findings:

**Best-of-N and Quality Degradation:**
The best-of-N approach can be extended to a step-level version, enabling exploration and selection at each step of image genera
…[truncated 1462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T00:32:34.985549+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T00:32:34.985674+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T00:32:34.985792+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://rlhfbook.com/c/09-rejection-sampling",
  "prompt": "Extract all content about: (1) how the number of samples N or top-k selection affects training data quality, (2) any ablation studies on k or N, (3) any discussion of noise introduced by selecting more candidates, (4) the trade-off between data quantity and quality when varying k. Include specific numbers and findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://rlhfbook.com/c/09-rejection-sampling",
    "prompt": "Extract all content about: (1) how the number of samples N or top-k selection affects training data quality, (2) any ablation studies on k or N, (3) any discussion of noise introduced by selecting more candidates, (4) the trade-off between data quantity and quality when varying k. Include specific numbers and findings."
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-16T00:32:34.985912+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf",
  "prompt": "This is the DART-Math paper. Extract: (1) any ablation on the number of samples k used for rejection tuning, (2) any findings on how increasing the number of selected samples affects training quality, (3) any discussion of noise from including lower-ranked samples, (4) the relationship between selection threshold/quantity and downstream performance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf",
    "prompt": "This is the DART-Math paper. Extract: (1) any ablation on the number of samples k used for rejection tuning, (2) any findings on how increasing the number of selected samples affects training quality, (3) any discussion of noise from including lower-ranked samples, (4) the relationship between selection threshold/quantity and downstream performance."
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-16T00:32:34.986041+00:00_

# Analysis of Sample Size and Selection Effects in Rejection Sampling

Based on the provided content, there is **limited empirical data** on the specific effects you requested:

## What the Document States

**On completion quantity:**
The text notes that "successful implementations of rejection sampling have included 10 to 30 or more completions for each prompt. Using too few completions will make training biased and/or noisy."

This is the only quantitative guidance provided, though it lacks specific ablation results comparing these ranges.

**On selection trade-offs:**
The document acknowledges that "more completions can improve the best available sample, but only if the reward model can separate good and bad answers," suggesting a potential quality-quantity trade-off. However, no empirical findings demonstrate this trade-off.

## What's Missing

The content explicitly states that "the actual details on which prompts to use, how to select a reward model, how to sequence rejection sampling, etc. are not well documented in the literature." 

Notably, the document contains **no ablation studies comparing different N or k values**, no quantified noise analysis, and no empirical measurements of data quality degradation at different sample sizes.

The suggested experiments section recommends practitioners "vary how much choice the reward model gets" and "change num_completions_per_prompt," but provides no baseline results from such experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T00:32:34.986180+00:00_

# DART-Math: Ablation Studies on Sample Selection

Based on the provided PDF content, I can identify the following relevant findings:

## Key Ablation Studies

**Sample Size Analysis:**
The paper investigates how the number of selected samples (k) impacts rejection tuning effectiveness. The research examines performance across different selection quantities to determine optimal training configurations.

**Quality vs. Quantity Tradeoff:**
The authors document findings showing that including lower-ranked samples introduces noise that can degrade training quality. This suggests a meaningful relationship between selection threshold stringency and final model performance.

**Threshold Effects:**
The work establishes that downstream performance correlates with the selection threshold used during sample filtering. More restrictive thresholds (fewer samples) appear to produce cleaner training signals, though potentially with reduced data volume.

**Training Stability:**
The ablation reveals that increasing selected sample count beyond optimal levels does not monotonically improve outcomes, indicating diminishing returns and potential negative effects from noisy lower-quality examples.

The paper demonstrates these findings through systematic experimental variation, establishing empirical guidelines for practitioners selecting rejection tuning hyperparameters.

[Binary content (application/pdf, 558.4KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/b69ab9a8-8e92-45c4-8283-0113da64e7fa/tool-results/webfetch-1778891463718-ld0o0y.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T00:32:34.986348+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2304.06767v4",
  "prompt": "Extract from the RAFT paper: (1) Any ablation on the number of top-k samples selected per prompt for fine-tuning, (2) How the paper defines the filtering threshold or top-k ratio, (3) Any discussion of how increasing k (selecting more samples) affects training quality, (4) Any analysis of the trade-off between data quantity and noise when selecting top-ranked samples. Include specific numbers and experimental results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2304.06767v4",
    "prompt": "Extract from the RAFT paper: (1) Any ablation on the number of top-k samples selected per prompt for fine-tuning, (2) How the paper defines the filtering threshold or top-k ratio, (3) Any discussion of how increasing k (selecting more samples) affects training quality, (4) Any analysis of the trade-off between data quantity and noise when selecting top-ranked samples. Include specific numbers and experimental results."
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T00:32:34.986490+00:00_

# RAFT Paper: Top-K Selection Analysis

## 1. Ablation on Number of Top-K Samples

The paper conducts experiments with **K ∈ {8, 16, 32}** to evaluate how sample count affects performance:

- **K=8**: Achieves reward of 2.180
- **K=16**: Achieves reward of 2.251
- **K=32**: Achieves reward of 2.329 (best performance)

Results show "as K increases, the obtained model tends to achieve a higher test reward" with consistent diversity metrics across all settings.

## 2. Filtering Threshold Definition

The paper employs **local ranking per prompt** rather than absolute thresholds. For each prompt, the method "sample[s] K responses from the model and take[s] the response with the highest reward." This means selecting the **top-1 sample** from K candidates per prompt, establishing an implicit 1/K acceptance ratio.

## 3. Impact of Increasing K on Training Quality

The theoretical justification shows that reward improvement follows: "larger K leads to better performance" with marginal benefits following "log K" scaling. Practically:

- Larger K requires more inference time (5-7 hours for K ∈ {8,32})
- K=16 and K=32 converge in 10-12 iterations versus 15-18 for K=8
- Trade-off: "balance the training cost and model performance"

## 4. Data Quality vs. Quantity Trade-Off

The paper doesn't explicitly analyze noise accumulation but notes that diversity metrics remain "never worse" with higher K values, suggesting quality preservation despite increased sampling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T00:32:34.986683+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T00:32:34.986821+00:00_

_project
ced_stabilizer_literature_survey.md
cuda3_diagnostic.md
d024_literature_survey.md
diag_mvp2_grpo_flatnli_r3.md
diagnose_plan_001.md
diversity_probe.py
diversity_probe_results.md
dream_reports
edcr_analysis.md
edcr_analysis_r2b.md
edcr_diagnostic_table.md
eval_progress_check_0515.md
eval_script_audit.md
eval_status_check.md
freige
gap_analysis_w3.md
grpo_forgetting_dynamics.pdf
grpo_forgetting_dynamics.png
kl_analysis_report.md
literature_quantization_rl.md
literature_survey_evidence_overhead.md
manifest.yaml
metrics_summary.csv
metrics_summary_table.md
mvp2_eval_rsft_r2b_maxtok1536_r2
plan_001_flat_nli_seed45
plan_003
plan_003_edcr_cross_method_table.md
plan_003_edcr_diagnostic
plan_003_edcr_diagnostic.md
plan_009
plan_009_dynamics_data.json
plan_009_dynamics_figure
plan_009_forgetting_data.csv
plan_009_forgetting_data_v5.csv
plan_009_forgetting_figure
plan_009_grpo_forgetting
plan_012_dpo_ced
plan_012_dpo_ced_1ep_analysis.md
process_check_report.md
related_work_gap_analysis.md
related_work_survey
rsft_gen_progress_check.md
rsft_pipeline_commands.md
status_check_loop4.md
training_health_check.md
training_trajectory_loop4.md
trl_grpo_stability_research.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T00:32:34.986949+00:00_

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
  "session": "worker_research_topk_ablation_lit_20260516T002831",
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

_source line 62 · 2026-05-16T00:32:34.987067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T00:32:34.987195+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/topk_ablation_lit_review.md",
  "content": "# Top-k Ablation Negative Result: Literature Context\n\n## 实验背景\n\nCED RSFT top_k ablation 结果为 negative：\n- top_k=3: rel_f1=0.4454, ign_f1=0.4364\n- top_k=1: rel_f1≈0.46\n- 增加 k 引入更多噪声训练样本，降低关系抽取精度\n\n## 文献中的共识\n\n### 1. RAFT 框架的关键设计：top-1 selection from K candidates\n\nRAFT (Dong et al., TMLR 2024) 定义了 RSFT 的标准框架：每轮生成 K 个 response，用 reward model 排序，**始终只取 top-1** 做 SFT。论文的 ablation 显示 K∈{8,16,32} 时性能随 K 增加而提升（K=8→2.180, K=16→2.251, K=32→2.329），但这是因为更大的候选池提供了更好的 top-1 样本——而非保留更多样本训练。\n\n这恰好与我们的实验形成对照：\n- **RAFT 的 K**：候选池大小，增大→更好的 top-1→性能提升\n- **我们的 top_k**：保留样本数，增大→引入次优样本→性能下降\n\nRAFT 隐式地做出了 \"只用最好的 1 个\" 的设计选择，我们的 ablation 从实验角度验证了这个选择的合理性。\n\n### 2. Best-of-N 文献：N 增大导致 reward hacking\n\nliterature_map.yaml 中 Category 13 收录了 4 篇直接相关论文：\n\n- **Huang et al. (ICML 2025)** \"Is Best-of-N the Best of Them?\"：证明 BoN 在 N 增大时 provably suffers from reward hacking——proxy reward 持续改善但 true reward 先升后降。根本原因是 reward model 作为不完美代理，选择压力越大，over-optimization 越严重。\n- **Chen et al. (NeurIPS 2025 Spotlight)** \"Inference-Time Reward Hacking\"：true reward 的先升后降是所有 inference-time 选择机制的固有属性，提出 BoP 和 HedgeTune 缓解。\n- **Ichihara et al. (TMLR 2025)**：系统评估 BoN reward hacking，提出 SRBoN 正则化方法。\n- **Jinnai et al. (NAACL 2025)**：MBR-BoN 用 proximity regularizer 约束选择偏离度。\n\n虽然这些论文讨论的是 inference-time reranking，但核心机制完全适用于 training-time data selection：**当 reward model（此处为 CED score）不完美时，选择更多样本放大了 proxy-true reward 的 misalignment**。\n\n### 3. 训练数据噪声的放大效应\n\n- **DART-Math (NeurIPS 2024)**：在数学推理 rejection tuning 中发现，放宽选择阈值（保留更多样本）增加数据量但引入噪声，downstream 性能非单调——存在 sweet spot。\n- **AdaSTaR (NeurIPS 2025)**：指出 RFT 的随机采样导致已解决样本被过度训练、困难样本训练不足，进一步论证了 naive top-k 扩大选择集的问题。\n- **RLHF Book (Nathan Lambert)**：指出 rejection sampling 中 \"more completions can improve the best available sample, but only if the reward model can separate good and bad answers\"——隐含条件是 reward model 必须足够准确，否则扩大选择集只是放大噪声。\n\n### 4. 对 CED top_k=3 negative result 的解释\n\n综合文献，我们的 negative result 可归因于两个交互因素：\n\n1. **CED score 作为不完美 proxy**：CED 用 NLI entailment 评估 evidence quality，但 evidence quality 与 relation extraction correctness 并非完全对齐。top_k=1 时只取 CED 最高分的样本，proxy 偏差影响小；top_k=3 时第 2、3 名样本的 CED score 更可能 reward-hack——evidence 看起来好但 RE triple 有误。\n\n2. **噪声稀释训练信号**：即使第 2、3 名样本不是 reward hacking，它们客观上也是次优样本。将它们与最优样本混合训练，稀释了每个 prompt 的训练信号强度，等价于在 SFT loss 中引入 label noise。\n\n## 建议\n\n### 不需要加入 literature_map.yaml 的论文\n上述关键论文（Huang et al., Chen et al., Ichihara et al., Jinnai et al., DART-Math, AdaSTaR）**已全部收录**在 literature_map.yaml 中。\n\n### 可考虑补充的论文\n- Nathan Lambert, *RLHF Book*, Chapter 9: Rejection Sampling (https://rlhfbook.com/c/09-rejection-sampling) — 作为 practitioner guide 补充，讨论了 completion 数量与 reward model 分辨力的交互，但无实验数据，优先级低。\n\n### 写作建议\n在论文 ablation section 中报告 top_k 结果时，可引用 Huang et al. (2025) 的 BoN reward hacking 理论和 RAFT 的 top-1 design choice 作为文献支撑，论证 \"CED scoring 的最优 k=1 与 BoN 文献中 reward over-optimization 的发现一致\"。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/topk_ablation_lit_review.md",
    "content": "# Top-k Ablation Negative Result: Literature Context\n\n## 实验背景\n\nCED RSFT top_k ablation 结果为 negative：\n- top_k=3: rel_f1=0.4454, ign_f1=0.4364\n- top_k=1: rel_f1≈0.46\n- 增加 k 引入更多噪声训练样本，降低关系抽取精度\n\n## 文献中的共识\n\n### 1. RAFT 框架的关键设计：top-1 selection from K candidates\n\nRAFT (Dong et al., TMLR 2024) 定义了 RSFT 的标准框架：每轮生成 K 个 response，用 reward model 排序，**始终只取 top-1** 做 SFT。论文的 ablation 显示 K∈{8,16,32} 时性能随 K 增加而提升（K=8→2.180, K=16→2.251, K=32→2.329），但这是因为更大的候选池提供了更好的 top-1 样本——而非保留更多样本训练。\n\n这恰好与我们的实验形成对照：\n- **RAFT 的 K**：候选池大小，增大→更好的 top-1→性能提升\n- **我们的 top_k**：保留样本数，增大→引入次优样本→性能下降\n\nRAFT 隐式地做出了 \"只用最好的 1 个\" 的设计选择，我们的 ablation 从实验角度验证了这个选择的合理性。\n\n### 2. Best-of-N 文献：N 增大导致 reward hacking\n\nliterature_map.yaml 中 Category 13 收录了 4 篇直接相关论文：\n\n- **Huang et al. (ICML 2025)** \"Is Best-of-N the Best of Them?\"：证明 BoN 在 N 增大时 provably suffers from reward hacking——proxy reward 持续改善但 true reward 先升后降。根本原因是 reward model 作为不完美代理，选择压力越大，over-optimization 越严重。\n- **Chen et al. (NeurIPS 2025 Spotlight)** \"Inference-Time Reward Hacking\"：true reward 的先升后降是所有 inference-time 选择机制的固有属性，提出 BoP 和 HedgeTune 缓解。\n- **Ichihara et al. (TMLR 2025)**：系统评估 BoN reward hacking，提出 SRBoN 正则化方法。\n- **Jinnai et al. (NAACL 2025)**：MBR-BoN 用 proximity regularizer 约束选择偏离度。\n\n虽然这些论文讨论的是 inference-time reranking，但核心机制完全适用于 training-time data selection：**当 reward model（此处为 CED score）不完美时，选择更多样本放大了 proxy-true reward 的 misalignment**。\n\n### 3. 训练数据噪声的放大效应\n\n- **DART-Math (NeurIPS 2024)**：在数学推理 rejection tuning 中发现，放宽选择阈值（保留更多样本）增加数据量但引入噪声，downstream 性能非单调——存在 sweet spot。\n- **AdaSTaR (NeurIPS 2025)**：指出 RFT 的随机采样导致已解决样本被过度训练、困难样本训练不足，进一步论证了 naive top-k 扩大选择集的问题。\n- **RLHF Book (Nathan Lambert)**：指出 rejection sampling 中 \"more completions can improve the best available sample, but only if the reward model can separate good and bad answers\"——隐含条件是 reward model 必须足够准确，否则扩大选择集只是放大噪声。\n\n### 4. 对 CED top_k=3 negative result 的解释\n\n综合文献，我们的 negative result 可归因于两个交互因素：\n\n1. **CED score 作为不完美 proxy**：CED 用 NLI entailment 评估 evidence quality，但 evidence quality 与 relation extraction correctness 并非完全对齐。top_k=1 时只取 CED 最高分的样本，proxy 偏差影响小；top_k=3 时第 2、3 名样本的 CED score 更可能 reward-hack——evidence 看起来好但 RE triple 有误。\n\n2. **噪声稀释训练信号**：即使第 2、3 名样本不是 reward hacking，它们客观上也是次优样本。将它们与最优样本混合训练，稀释了每个 prompt 的训练信号强度，等价于在 SFT loss 中引入 label noise。\n\n## 建议\n\n### 不需要加入 literature_map.yaml 的论文\n上述关键论文（Huang et al., Chen et al., Ichihara et al., Jinnai et al., DART-Math, AdaSTaR）**已全部收录**在 literature_map.yaml 中。\n\n### 可考虑补充的论文\n- Nathan Lambert, *RLHF Book*, Chapter 9: Rejection Sampling (https://rlhfbook.com/c/09-rejection-sampling) — 作为 practitioner guide 补充，讨论了 completion 数量与 reward model 分辨力的交互，但无实验数据，优先级低。\n\n### 写作建议\n在论文 ablation section 中报告 top_k 结果时，可引用 Huang et al. (2025) 的 BoN reward hacking 理论和 RAFT 的 top-1 design choice 作为文献支撑，论证 \"CED scoring 的最优 k=1 与 BoN 文献中 reward over-optimization 的发现一致\"。\n"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T00:32:34.987448+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/topk_ablation_lit_review.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T00:32:34.987595+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-16T00:32:34.987719+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-16T00:32:34.987836+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T00:32:34.987946+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-16T00:32:34.988056+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-16T00:32:34.988165+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_topk_ablation_lit_20260516T002831",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-16T00:32:34.988336+00:00_

产出文件已写入 `artifacts/topk_ablation_lit_review.md`。

核心发现：

1. **literature_map.yaml 已有充分覆盖**——Category 13（BoN/Reranking）的 4 篇论文 + Category 14（RSFT Methodology）的 AdaSTaR/RIFT 直接解释了 top_k=3 的 negative result。

2. **文献共识**：RAFT 框架始终只取 top-1（不是 top-k），我们的 ablation 从反面验证了这个设计。BoN 文献（Huang et al. ICML 2025）证明 proxy reward 不完美时，扩大选择集导致 reward hacking——CED score 与 RE correctness 的 misalignment 在 top_k=3 时被放大。

3. **不需要新增论文到 literature_map.yaml**，已有收录足够支撑。写论文时可引用 Huang et al. (2025) 和 RAFT 的 top-1 设计作为文献锚点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_topk_ablation_lit_20260516T002831"
}
```

</details>

---
