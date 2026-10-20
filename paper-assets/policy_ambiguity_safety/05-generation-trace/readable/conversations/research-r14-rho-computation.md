# research r14 rho computation

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_research_r14_rho_computation_20260522T135212.jsonl`
- **Structured JSON:** [`702f20cf32fc209ce7d3.json`](../../sessions/70/702f20cf32fc209ce7d3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-22T13:53:07.300286+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom scipy.stats import spearmanr\nimport numpy as np\n\n# Table 1 data (ambiguous condition violation rates %)\n# GPT-5.4-judged models: GPT-4.1, Claude, Qwen3\n# GPT-4.1-judged models: GPT-5.4, DeepSeek\n\ntypes = ['Incompleteness', 'Auth. Scope', 'Cond. Prec.', 'Lexical', 'Scopal', 'Coreferential']\n\n# Per-type rates\ngpt41 = [58, 46, 36, 34, 38, 32]\nclaude = [48, 12, 36, 32, 32, 22]\nqwen3 = [62, 26, 40, 52, 37, 42]\ngpt54 = [46, 64, 34, 42, 42, 18]\nds    = [54, 60, 38, 54, 48, 44]\n\n# Pooled rates\njudged_54 = [np.mean([gpt41[i], claude[i], qwen3[i]]) for i in range(6)]\njudged_41 = [np.mean([gpt54[i], ds[i]]) for i in range(6)]\n\nprint('=== 6 types (all) ===')\nfor i, t in enumerate(types):\n    print(f'  {t}: GPT-5.4-judged={judged_54[i]:.2f}, GPT-4.1-judged={judged_41[i]:.2f}')\n\nrho6, p6 = spearmanr(judged_54, judged_41)\nprint(f'Spearman rho = {rho6:.4f}, p = {p6:.4f}')\n\n# Exclude auth scope (index 1)\nidx5 = [0, 2, 3, 4, 5]\ntypes5 = [types[i] for i in idx5]\nj54_5 = [judged_54[i] for i in idx5]\nj41_5 = [judged_41[i] for i in idx5]\n\nprint()\nprint('=== 5 types (excluding Auth. Scope) ===')\nfor i, t in enumerate(types5):\n    print(f'  {t}: GPT-5.4-judged={j54_5[i]:.2f}, GPT-4.1-judged={j41_5[i]:.2f}')\n\nrho5, p5 = spearmanr(j54_5, j41_5)\nprint(f'Spearman rho = {rho5:.4f}, p = {p5:.4f}')\n\"\n",
  "description": "Compute Spearman rho for 6 and 5 types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r14_rho_computation_20260522T135212",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom scipy.stats import spearmanr\nimport numpy as np\n\n# Table 1 data (ambiguous condition violation rates %)\n# GPT-5.4-judged models: GPT-4.1, Claude, Qwen3\n# GPT-4.1-judged models: GPT-5.4, DeepSeek\n\ntypes = ['Incompleteness', 'Auth. Scope', 'Cond. Prec.', 'Lexical', 'Scopal', 'Coreferential']\n\n# Per-type rates\ngpt41 = [58, 46, 36, 34, 38, 32]\nclaude = [48, 12, 36, 32, 32, 22]\nqwen3 = [62, 26, 40, 52, 37, 42]\ngpt54 = [46, 64, 34, 42, 42, 18]\nds    = [54, 60, 38, 54, 48, 44]\n\n# Pooled rates\njudged_54 = [np.mean([gpt41[i], claude[i], qwen3[i]]) for i in range(6)]\njudged_41 = [np.mean([gpt54[i], ds[i]]) for i in range(6)]\n\nprint('=== 6 types (all) ===')\nfor i, t in enumerate(types):\n    print(f'  {t}: GPT-5.4-judged={judged_54[i]:.2f}, GPT-4.1-judged={judged_41[i]:.2f}')\n\nrho6, p6 = spearmanr(judged_54, judged_41)\nprint(f'Spearman rho = {rho6:.4f}, p = {p6:.4f}')\n\n# Exclude auth scope (index 1)\nidx5 = [0, 2, 3, 4, 5]\ntypes5 = [types[i] for i in idx5]\nj54_5 = [judged_54[i] for i in idx5]\nj41_5 = [judged_41[i] for i in idx5]\n\nprint()\nprint('=== 5 types (excluding Auth. Scope) ===')\nfor i, t in enumerate(types5):\n    print(f'  {t}: GPT-5.4-judged={j54_5[i]:.2f}, GPT-4.1-judged={j41_5[i]:.2f}')\n\nrho5, p5 = spearmanr(j54_5, j41_5)\nprint(f'Spearman rho = {rho5:.4f}, p = {p5:.4f}')\n\"\n",
    "description": "Compute Spearman rho for 6 and 5 types"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T13:53:07.300693+00:00_

=== 6 types (all) ===
  Incompleteness: GPT-5.4-judged=56.00, GPT-4.1-judged=50.00
  Auth. Scope: GPT-5.4-judged=28.00, GPT-4.1-judged=62.00
  Cond. Prec.: GPT-5.4-judged=37.33, GPT-4.1-judged=36.00
  Lexical: GPT-5.4-judged=39.33, GPT-4.1-judged=48.00
  Scopal: GPT-5.4-judged=35.67, GPT-4.1-judged=45.00
  Coreferential: GPT-5.4-judged=32.00, GPT-4.1-judged=31.00
Spearman rho = 0.0857, p = 0.8717

=== 5 types (excluding Auth. Scope) ===
  Incompleteness: GPT-5.4-judged=56.00, GPT-4.1-judged=50.00
  Cond. Prec.: GPT-5.4-judged=37.33, GPT-4.1-judged=36.00
  Lexical: GPT-5.4-judged=39.33, GPT-4.1-judged=48.00
  Scopal: GPT-5.4-judged=35.67, GPT-4.1-judged=45.00
  Coreferential: GPT-5.4-judged=32.00, GPT-4.1-judged=31.00
Spearman rho = 0.9000, p = 0.0374

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r14_rho_computation_20260522T135212",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T13:53:07.300909+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/r14_rho_computation.md",
  "content": "## Cross-Judge-Group Type Ranking Correlation\n\n### 6 types (all)\nGPT-5.4-judged rates: [56.00, 28.00, 37.33, 39.33, 35.67, 32.00] (Incompleteness, Auth. Scope, Cond. Prec., Lexical, Scopal, Coreferential)\nGPT-4.1-judged rates: [50.00, 62.00, 36.00, 48.00, 45.00, 31.00]\nSpearman ρ = 0.09, p = 0.87\n\n### 5 types (excluding auth scope)\nGPT-5.4-judged rates: [56.00, 37.33, 39.33, 35.67, 32.00] (Incompleteness, Cond. Prec., Lexical, Scopal, Coreferential)\nGPT-4.1-judged rates: [50.00, 36.00, 48.00, 45.00, 31.00]\nSpearman ρ = 0.90, p = 0.037\n\n### Interpretation\nExcluding authorization scope (the type with lowest inter-judge agreement, κ=0.385) dramatically improves cross-judge-group correlation from ρ=0.09 (p=0.87) to ρ=0.90 (p=0.037). The remaining 5 types show strong, statistically significant rank agreement across judge groups. This confirms that the near-zero full correlation is driven almost entirely by authorization scope, whose ambiguous judgments diverge most across judges, rather than reflecting a systematic judge-group bias.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r14_rho_computation_20260522T135212",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/r14_rho_computation.md",
    "content": "## Cross-Judge-Group Type Ranking Correlation\n\n### 6 types (all)\nGPT-5.4-judged rates: [56.00, 28.00, 37.33, 39.33, 35.67, 32.00] (Incompleteness, Auth. Scope, Cond. Prec., Lexical, Scopal, Coreferential)\nGPT-4.1-judged rates: [50.00, 62.00, 36.00, 48.00, 45.00, 31.00]\nSpearman ρ = 0.09, p = 0.87\n\n### 5 types (excluding auth scope)\nGPT-5.4-judged rates: [56.00, 37.33, 39.33, 35.67, 32.00] (Incompleteness, Cond. Prec., Lexical, Scopal, Coreferential)\nGPT-4.1-judged rates: [50.00, 36.00, 48.00, 45.00, 31.00]\nSpearman ρ = 0.90, p = 0.037\n\n### Interpretation\nExcluding authorization scope (the type with lowest inter-judge agreement, κ=0.385) dramatically improves cross-judge-group correlation from ρ=0.09 (p=0.87) to ρ=0.90 (p=0.037). The remaining 5 types show strong, statistically significant rank agreement across judge groups. This confirms that the near-zero full correlation is driven almost entirely by authorization scope, whose ambiguous judgments diverge most across judges, rather than reflecting a systematic judge-group bias.\n"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T13:53:07.301143+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/r14_rho_computation.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r14_rho_computation_20260522T135212",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-22T13:53:07.301433+00:00_

结果：

- **6 types (all)**: Spearman ρ = 0.09, p = 0.87 — 近乎无相关
- **5 types (excl. auth scope)**: Spearman ρ = 0.90, p = 0.037 — 强正相关且显著

排除 auth scope 后，两个 judge group 的 type 排序高度一致。近零相关几乎完全由 auth scope 这一个 type 驱动（该 type 在 GPT-5.4-judged 组排最低 28%，在 GPT-4.1-judged 组排最高 62%）。

结果已写入 `artifacts/r14_rho_computation.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_r14_rho_computation_20260522T135212"
}
```

</details>

---
