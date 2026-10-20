# analysis round10 data compilation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_round10_data_compilation_20260516T002532.jsonl`
- **Structured JSON:** [`665ed3166049d3b82cab.json`](../../sessions/66/665ed3166049d3b82cab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-16T00:34:21.359026+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T00:34:21.359427+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T00:34:21.359666+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T00:34:21.359827+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T00:34:21.360879+00:00_

Error: result (206,204 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T00:34:21.361139+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/memory.md\", \"content\": \"# Project Memory\\n\\n## 2026-05-15: C10 GSM8K — random masking confirms compound interaction is intrinsic\\n- gsm8k_qw_rand_s025_v2 (PASS) + gsm8k_qw_rand_s030_v2 (PASS): random masking 在 s=0.25 和 s=0.30 均产生显著 compound interaction\\n- II dose-response: s=0.30 > s=0.25（所有 phase），median CI lower bound 均 > 0\\n- 关键论文 claim: compound interaction 是 sparsity 的固有属性，不依赖 masking strategy（importance vs random）\\n- 对比 spark-aaai2026: 他们只报告 importance-based compound 是 super-additive，我们证明 random 也如此 → 更强 generalization\\n\\n## 2026-05-15: DS 8k truncation — 即使 8192 tokens 仍不够\\n- acc_ds_s020_8k_v2: truncation 从 4k 版 64% 仅降至 8k 版 58%（目标 <20% 远未达到）\\n- DS 在 sparsity 下生成极长输出，8k tokens 仍不足 → accuracy 数据为下界\\n- 论文处理：DS accuracy 标注为 \\\"lower bound under token budget constraint\\\"，呼应 D086（降为定性观察）\\n\\n## 2026-05-15: QW n=100 accuracy dose curve — v2 fix 影响极小\\n- acc_qw_s020_n100_b2_fix 完成：v2 rescore 未改变 s020 batch1（均为 13/50=0.26），8k batch2 仅 +1 correct（22→23）\\n- 当前 dose curve: dense=0.40, s015=0.36, s020=0.36(v2✓), s025=0.33(fix running), s030=0.19\\n- **s015=s020 平台期**：低 sparsity 区间（≤20%）accuracy 损失几乎相同（-4pp），断崖在 s025→s030（-14pp）\\n- ⚠️ s015/s030/dense 的 batch1 尚未走 v2 rescore；s020 的 v2 与 pre-v2 相同，但不能假设其他条件也如此\\n- 推翻早期结论\\\"QW s015 完全无损(0pp)\\\"——n=100 显示 -4pp（早期结论可能基于更小样本）\\n\\n## 2026-05-15: Qwen n=475 reanalysis complete\\n- Reviewer flagged Qwen using n=274 (complete-case requiring all 3 phases). Corrected to n=475 (low+high valid only).\\n- Created `analyze_n500_v2.py` on server. Outputs: `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\\n- v2 adds: cross-model Mann-Whitney U, imp/rand effect size ratio, proper paired filtering via `extract_diffs_paired`\\n- Bonferroni correction across 48 tests total (16 conditions + 8 within-imp d_z + 8 rand-within + 8 imp-vs-rand + 8 cross-model)\\n- DS rand s025/s
…[truncated 1291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T00:34:21.361334+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T00:34:21.361646+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-15 (D080v3 GSM8K median-based 数据更新: DS 0.241→4.682, QW 0.039→2.092, imp/rand ratio 2.3-3.8×) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 3-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\\\"反转\\\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phas
…[truncated 11080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T00:34:21.361862+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract PPL dose curve data",
  "prompt": "Extract PPL dose curve experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need ALL experiments related to PPL (perplexity) dose curves. These include experiments with IDs matching patterns like:\n- v6_* series (DeepSeek PPL)\n- bf16_* series (bf16 PPL)\n- Any experiment with \"ppl\" or \"PPL\" in the ID or description\n- n500 unified analysis experiments\n\nFor each experiment found, extract:\n1. exp_id\n2. status\n3. conclusion (if any)\n4. metrics (ALL metrics, especially: median_diff, median II, Wilcoxon p-value, effect_size/Cohen's d, sparsity level)\n5. Any notes about the experiment\n\nUse jq or python to parse. First probe the structure, then extract. Report ALL found experiments with their full metrics verbatim. Be thorough - don't miss any PPL-related experiment.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract PPL dose curve data",
    "prompt": "Extract PPL dose curve experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need ALL experiments related to PPL (perplexity) dose curves. These include experiments with IDs matching patterns like:\n- v6_* series (DeepSeek PPL)\n- bf16_* series (bf16 PPL)\n- Any experiment with \"ppl\" or \"PPL\" in the ID or description\n- n500 unified analysis experiments\n\nFor each experiment found, extract:\n1. exp_id\n2. status\n3. conclusion (if any)\n4. metrics (ALL metrics, especially: median_diff, median II, Wilcoxon p-value, effect_size/Cohen's d, sparsity level)\n5. Any notes about the experiment\n\nUse jq or python to parse. First probe the structure, then extract. Report ALL found experiments with their full metrics verbatim. Be thorough - don't miss any PPL-related experiment.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T00:34:21.362032+00:00_

Async agent launched successfully.
agentId: a7fba12d105bf979c (internal ID - do not mention to user. Use SendMessage with to: 'a7fba12d105bf979c' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a7fba12d105bf979c.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T00:34:21.362251+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract QW accuracy data",
  "prompt": "Extract QW (Qwen) accuracy dose curve experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need experiments with IDs matching:\n- acc_qw_dense_n100\n- acc_qw_s015_n100\n- acc_qw_s020_n100 (and _b2_fix variant)\n- acc_qw_s025_n100 (and _b2_fix variant)\n- acc_qw_s030_n100\n- Any other acc_qw_* experiments\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL - especially combined_accuracy, truncation_rate, correct counts, batch details)\n5. notes\n6. Any other relevant fields\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim - don't summarize away any metrics.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract QW accuracy data",
    "prompt": "Extract QW (Qwen) accuracy dose curve experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need experiments with IDs matching:\n- acc_qw_dense_n100\n- acc_qw_s015_n100\n- acc_qw_s020_n100 (and _b2_fix variant)\n- acc_qw_s025_n100 (and _b2_fix variant)\n- acc_qw_s030_n100\n- Any other acc_qw_* experiments\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL - especially combined_accuracy, truncation_rate, correct counts, batch details)\n5. notes\n6. Any other relevant fields\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim - don't summarize away any metrics.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T00:34:21.362513+00:00_

Async agent launched successfully.
agentId: a3e0a592254fabea7 (internal ID - do not mention to user. Use SendMessage with to: 'a3e0a592254fabea7' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a3e0a592254fabea7.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T00:34:21.362705+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract DS accuracy + GSM8K data",
  "prompt": "Extract DS (DeepSeek) accuracy and GSM8K experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need TWO sets of experiments:\n\n**SET 1: DS Accuracy (8k v2)**\n- acc_ds_dense_8k_v2\n- acc_ds_s015_8k_v2\n- acc_ds_s020_8k_v2\n- acc_ds_s025_8k_v2\n- acc_ds_s030_8k_v2\n- Any other acc_ds_* experiments\n\n**SET 2: GSM8K Compound Interaction**\n- gsm8k_qw_rand_s025_v2\n- gsm8k_qw_rand_s030_v2\n- Any other gsm8k_* experiments\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL metrics)\n5. notes\n6. Any other relevant fields\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract DS accuracy + GSM8K data",
    "prompt": "Extract DS (DeepSeek) accuracy and GSM8K experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need TWO sets of experiments:\n\n**SET 1: DS Accuracy (8k v2)**\n- acc_ds_dense_8k_v2\n- acc_ds_s015_8k_v2\n- acc_ds_s020_8k_v2\n- acc_ds_s025_8k_v2\n- acc_ds_s030_8k_v2\n- Any other acc_ds_* experiments\n\n**SET 2: GSM8K Compound Interaction**\n- gsm8k_qw_rand_s025_v2\n- gsm8k_qw_rand_s030_v2\n- Any other gsm8k_* experiments\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL metrics)\n5. notes\n6. Any other relevant fields\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T00:34:21.362863+00:00_

Async agent launched successfully.
agentId: a09137f4d041cbaa5 (internal ID - do not mention to user. Use SendMessage with to: 'a09137f4d041cbaa5' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a09137f4d041cbaa5.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T00:34:21.363027+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract sf5 + misc evidence",
  "prompt": "Extract supplementary evidence experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need experiments related to:\n\n1. **sf5 asymmetric sparsity** - any experiment with \"sf5\" or \"asymmetric\" in the ID\n2. **Appendix B G× correction** - any experiment with \"gx\" or \"G×\" or \"appendix\" in the ID or notes\n3. **Cross-model Mann-Whitney U** - any experiment with \"mann_whitney\" or \"n475\" or \"n500_v2\" or \"reanalysis\" in the ID\n4. **n500 unified analysis** - experiments with \"n500\" in the ID\n5. **c4_entropy** experiments (discrimination collapse mechanism)\n6. **c3_llama** experiments (cross-architecture)\n7. **c5b_pilot** experiments (phase-gated controller)\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL metrics)\n5. notes\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim - this is for a data compilation so completeness matters.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract sf5 + misc evidence",
    "prompt": "Extract supplementary evidence experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need experiments related to:\n\n1. **sf5 asymmetric sparsity** - any experiment with \"sf5\" or \"asymmetric\" in the ID\n2. **Appendix B G× correction** - any experiment with \"gx\" or \"G×\" or \"appendix\" in the ID or notes\n3. **Cross-model Mann-Whitney U** - any experiment with \"mann_whitney\" or \"n475\" or \"n500_v2\" or \"reanalysis\" in the ID\n4. **n500 unified analysis** - experiments with \"n500\" in the ID\n5. **c4_entropy** experiments (discrimination collapse mechanism)\n6. **c3_llama** experiments (cross-architecture)\n7. **c5b_pilot** experiments (phase-gated controller)\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL metrics)\n5. notes\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim - this is for a data compilation so completeness matters.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T00:34:21.363197+00:00_

Async agent launched successfully.
agentId: a692d7d4f3f7a841e (internal ID - do not mention to user. Use SendMessage with to: 'a692d7d4f3f7a841e' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a692d7d4f3f7a841e.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T00:34:21.363878+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "round10_data_summary.md",
  "content": "# Round 10 Data Summary — All Experimental Evidence\n\n> Compiled: 2026-05-16 | EMNLP 2026 ARR deadline: 2026-05-25\n\n---\n\n## 1. PPL Dose Curve\n\n### 1a. n=500 Unified Analysis (canonical)\n\n**DeepSeek (c2_n500_deepseek, n=496)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Rand median II | Rand p (Bonf k=4) |\n|----------|--------------|--------|------------|---------------|-------------------|\n| s015 | 0.3907 | [0.350, 0.443] | 1.27e-70 | 0.0139 | 0.863 (NS) |\n| s020 | 1.2149 | [1.107, 1.337] | 3.98e-75 | 0.0315 | 0.280 (NS) |\n| s025 | 3.9857 | [3.527, 4.359] | 1.99e-78 | 0.2574 | 0.0058 ** |\n| s030 | 8.4813 | [7.754, 9.692] | 1.09e-79 | 0.5096 | 0.0059 ** |\n\n- Imp/rand ratio: 15.5–38.6×\n- Adjacent d_z: s015→s020 = −0.925, s020→s025 = −0.824, s025→s030 = −0.773\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n\n**Qwen (c2_qw_n500_r3, n=475, low+high valid filter)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Bonf p | Rand median II | Rand Bonf p |\n|----------|--------------|--------|------------|--------|---------------|------------|\n| s015 | 0.0659 | [0.049, 0.093] | 8.66e-15 | 3.46e-14 | −0.0111 | 0.687 (NS) |\n| s020 | 0.3073 | [0.261, 0.356] | 6.84e-42 | 2.74e-41 | 0.0153 | 0.800 (NS) |\n| s025 | 1.0745 | [0.977, 1.179] | 1.06e-68 | 4.25e-68 | 0.3931 | 6.37e-11 *** |\n| s030 | 3.1550 | [2.783, 3.558] | 9.21e-74 | 3.69e-73 | 0.9127 | 1.17e-14 *** |\n\n- Imp/rand ratio: 2.7–20.1×\n- Adjacent d_z: s015→s020 = −0.629, s020→s025 = −0.865, s025→s030 = −0.767\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n- Mid-null rate: 45.2% (filter: low+high valid only)\n\n### 1b. bf16 Paired Statistics (n≈50, per-problem)\n\n**DeepSeek importance (bf16_ds_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|------------|----------|\n| s015 | 0.3236 | 0 | 0.607 | 0 | 49 |\n| s020 | 1.1520 | 0 | 0.725 | 0 | 49 |\n| s025 | 3.9686 | 0 | 0.953 | 0 | 49 |\n| s030 | 9.9436 | 0 | 1.126 | 0 | 49 |\n\n**Qwen importance (bf16_qw_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Bootstrap CI | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|-------------|------------|----------|\n| s015 | 0.0476 | 0.0001 | 0.371 | [−0.005, 0.110] | 0.030 | 46 |\n| s020 | 0.2075 | 0 | 0.722 | [0.067, 0.402] | 3.4e-5 | 46 |\n| s025 | 1.1087 | 0 | 1.233 | [0.609, 1.469] | 0 | 46 |\n| s030 | 2.6194 | 0 | 1.439 | [1.722, 3.651] | 0 | 46 |\n\n⚠️ QW s015 n=50 CI crosses zero [−0.005, 0.110]; resolved at n=475 (CI [0.049, 0.093], p=3.5e-14).\n\n**Random controls (bf16, both models):** All 8 conditions FAIL — no structured phase gradient. DS rand median II range 0.09–4.04; QW rand median II range 0.14–8.07. All permutation p > 0.01 or CI overlapping.\n\n### 1c. Boundary Sparsity (s010, s035)\n\n| Condition | II_low median | II_mid median | II_high median | Verdict |\n|-----------|--------------|--------------|----------------|---------|\n| DS imp s010 | 0.0151 | 0.0061 | 0.0027 | FAIL (near-zero II) |\n| DS imp s035 | 28.76 | 4.95 | 0.11 | PASS (extends monotonic) |\n| QW imp s010 | −0.0444 | −0.0359 | 0.0001 | FAIL (near-zero II) |\n| QW imp s035 | 8.24 | 0.96 | 0.02 | PASS (extends monotonic) |\n\n---\n\n## 2. QW Accuracy Dose Curve (MATH-500, n=100)\n\nSource: acc_qw_dense_n100, acc_qw_s015_n100, acc_qw_s020_n100_b2_fix, acc_qw_s025_n100_b2_fix, acc_qw_s030_n100\n\n| Sparsity | Accuracy | Correct/100 | Δ vs dense | Note |\n|----------|----------|-------------|-----------|------|\n| dense | 0.40 | 40 | — | |\n| s015 | 0.36 | 36 | −0.04 | |\n| s020 | 0.36 | 36 | −0.04 | b2_fix: +1 vs original (35→36) |\n| s025 | 0.33 | 33 | −0.07 | b2_fix: unchanged (33→33) |\n| s030 | 0.19 | 19 | −0.21 | steep cliff from s025 |\n\n- s015 ≈ s020 plateau (−4pp); cliff at s025→s030 (−14pp)\n- b2_fix used max_new_tokens=8192 for batch2; batch1 used 2048 (mismatch noted)\n- ⚠️ s015/s030/dense batch1 未走 v2 rescore; s020 v2 rescore confirmed no change\n\n---\n\n## 3. DS Accuracy (8k v2, n=50, 定性观察)\n\nSource: acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2 + pending\n\n| Sparsity | Accuracy | Truncation Rate | Avg Tokens | Status |\n|----------|----------|-----------------|-----------|--------|\n| dense | 0.74 | 0.16 | 3126 | DONE |\n| s015 | — | — | — | **RUNNING** |\n| s020 | 0.30 | 0.58 | — | DONE |\n| s025 | 0.08 | 0.76 | 6344 | DONE |\n| s030 | — | — | — | **RUNNING** |\n\n**Caveat (D086):** Truncation rate 58–76% even at 8k tokens. DS under sparsity generates extremely long outputs; accuracy = lower bound under token budget constraint. 降为定性观察，不纳入统计检验。\n\n4k baseline for reference: ds_dense_acc=0.52 (truncation 56%), ds_s015_acc=0.36, ds_s030_acc=0.10.\n\n---\n\n## 4. GSM8K Cross-Benchmark (C10)\n\n### 4a. Importance Masking Phase Gradient\n\nSource: gsm8k_profiling_ds, gsm8k_profiling_qw\n\n| Model | s015 | s020 | s025 | s030 | Monotonic |\n|-------|------|------|------|------|-----------|\n| DS median gradient | 0.241 | 0.740 | 1.992 | 4.682 | ✓ |\n| DS CI | [0.077, 0.478] | [0.314, 1.119] | [0.933, 2.820] | [2.121, 10.557] | |\n| DS Wilcoxon p | 0.0003 | 0.0001 | 0.0001 | 0.0001 | |\n| QW median gradient | 0.039 | 0.158 | 1.100 | 2.092 | ✓ |\n\n### 4b. Strategy Specificity (imp/rand ratio)\n\n| Sparsity | Ratio (GSM8K) | Ratio (MATH-500) |\n|----------|--------------|-----------------|\n| s015 | 2.3× | 28.1× (DS) / 5.9× (QW) |\n| s020 | 2.5× | 38.6× (DS) / 20.1× (QW) |\n| s025 | 3.8× | 15.5× (DS) / 2.7× (QW) |\n| s030 | 2.8× | 16.6× (DS) / 3.5× (QW) |\n\nStrategy specificity ratio 从 MATH-500 的 15–36× 衰减至 GSM8K 的 2.3–3.8×（task-dependent）。\n\n### 4c. QW Random GSM8K (补全数据)\n\nSource: gsm8k_qw_rand_s025_v2, gsm8k_qw_rand_s030_v2\n\n| Condition | II_high median | II_mid median | II_low median | Verdict |\n|-----------|---------------|--------------|--------------|---------|\n| QW rand s025 | 0.718 | 1.127 | 1.459 | PASS |\n| QW rand s030 | 2.310 | 2.700 | 5.200 | PASS |\n\nRandom masking 在 GSM8K s025+s030 也产生 positive compound interaction（与 MATH-500 random FAIL 不同）。\n\n---\n\n## 5. Additional Evidence\n\n### 5a. sf5 Asymmetric Sparsity (sf5_asymmetric_spot)\n\n| Config | Head% | KV% | II_low | II_mid | II_high | D (low−high) |\n|--------|-------|-----|--------|--------|---------|-------------|\n| A | 0.20 | 0.30 | 19.51 | 6.05 | 0.38 | 19.13 |\n| B | 0.30 | 0.20 | 18.77 | 3.97 | 0.52 | 18.25 |\n\n- Phase gradient direction 完全稳健（D > 0 both configs）\n- KV sparsity 较高时 mid-phase II 更大（6.05 vs 3.97）\n- Head sparsity 较高时 high-phase II 略升（0.52 vs 0.38）\n- Pre-registered criterion: PASS\n\n### 5b. Appendix B G× Correction\n\n- 旧值: 58–241×\n- 修正值: **21–64×**（per-problem additive II + aggregate PPL 修正）\n- 计算脚本: `/root/autodl-tmp/pacs/compute_gx_final.py`\n- 来源: memory.md（未注册为独立实验）\n\n### 5c. Cross-Model Mann-Whitney U (n=475 reanalysis)\n\n- Qwen 从 n=274 (complete-case) 修正为 n=475 (low+high valid only)\n- 分析脚本: `analyze_n500_v2.py` → `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\n- Bonferroni 修订 (D066): k=4 family-wise（原 k=48）\n- DS rand s025/s030: Bonf p ≈ 0.006（恢复为显著）\n- BH-FDR (48 tests): rand s025/s030 fdr_p = 0.0019\n- 所有 imp 条件 *** 在 n=475 下保持显著\n\n### 5d. c4_entropy — Discrimination Collapse Mechanism\n\n**DeepSeek (c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.040 | −0.047 | −0.045 | −0.044 |\n| Rand entropy Δ | +0.128 | +0.136 | +0.217 | +0.233 |\n| Imp Gini Δ | −0.030 | −0.040 | −0.065 | −0.081 |\n| Imp CV Δ | −0.564 | −0.774 | −1.287 | −1.665 |\n\n**Qwen (qwen_c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.073 | −0.076 | **+0.045** | −0.007 |\n| Rand entropy Δ | +0.084 | +0.090 | +0.217 | +0.197 |\n| Imp Gini Δ | −0.010 | −0.012 | −0.010 | −0.020 |\n| Imp CV Δ | −0.045 | −0.208 | −1.491 | −1.142 |\n\n**结论:** Gini/CV 下降跨模型一致（discrimination collapse confirmed）。Entropy redistribution DS 一致但 QW s025 方向反转（+0.045）— model-dependent，不作为主线机制。\n\n### 5e. c3_llama — Cross-Architecture Validation\n\n- Model: DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\n- 8/8 conditions complete (imp + rand × 4 sparsity)\n- Within-importance phase gradient: d_z ≈ 1.0 across all sparsity levels ✓\n- imp_vs_rand d_z: 0.19→0.26→0.29→0.34（仅 s030 Bonferroni p=0.029 显著）\n- Random also shows significant phase gradient (d_z 0.35→0.44, CI excludes zero)\n- Qualitative direction consistent; strategy×phase interaction weaker + architecture-dependent\n\n### 5f. c5b_pilot — Phase-Gated Controller\n\n| Metric | s025 |\n|--------|------|\n| Uniform median II | 1.0435 |\n| Oracle median II | 0.856 |\n| Oracle recovery | 18% (CI [−39, 45.8], p=0.002) |\n| Heuristic median II | 0.713 |\n| Heuristic recovery | 31.7% (CI [−22.8, 66], p=0.024) |\n| Gate criterion | oracle > 30% |\n| Gate result | **FAIL** |\n\nDirection correct (Wilcoxon significant) but effect size insufficient. → §8 Future Work.\n\n---\n\n## 6. Claim–Evidence Mapping\n\n| Claim | Status | Primary Evidence (exp_id) |\n|-------|--------|--------------------------|\n| C1: Strategy- & task-modulated severity | confirmed | c2_n500_deepseek, c2_qw_n500_r3 (imp/rand ratio 15–39× DS, 2.7–20× QW); gsm8k_profiling_ds/qw (ratio 衰减至 2.3–3.8×) |\n| C2: Phase-modulated (low > high) | confirmed | bf16_ds_imp_s015–s030 (0.32→9.94); bf16_qw_imp_s015–s030 (0.048→2.619); n500 confirms all p < 1e-14 |\n| C3: Phase-strategy crossover | confirmed | bf16_importance_s025 (imp low=7.196 > rand low=1.363; imp high=0.032 < rand high=0.818) |\n| C4: Discrimination collapse | partially | c4_entropy (DS: Gini/CV ✓, entropy ✓); qwen_c4_entropy (Gini/CV ✓, entropy ✗ at s025) |\n| C5: Cross-model generalization | confirmed | c2_n500_deepseek + c2_qw_n500_r3: ρ=1.0 both, QW magnitude ~1/4 DS |\n| C5b: Phase-aware mitigation | gate_failed | c5b_pilot: oracle 18% < 30% gate → future work |\n| C6: Sub-exponential growth | confirmed | Δ growth factors: 3.8×→4.8×→2.0× (递减) |\n| C7: n=500 dose-response | confirmed | c2_n500_deepseek (n=496) + c2_qw_n500_r3 (n=475): monotonic, ρ=1.0 |\n| C8: Cross-architecture (LLaMA) | partially | c3_llama: within-imp d_z≈1.0 ✓; imp_vs_rand weak (d_z 0.19–0.34); rand also shows gradient |\n| C10: Cross-benchmark (GSM8K) | confirmed | gsm8k_profiling_ds/qw: monotonic ✓; gsm8k_qw_rand_s025/s030_v2: random也显著 |\n| S3→C: Model-dependent onset | confirmed | QW s015 n=50 CI crosses zero; n=475 resolves (p=3.5e-14). DS significant from s015+ |\n| S7→C: Dose-response monotonicity | confirmed | Spearman ρ=1.0 both models (n=500), perm p=0.0417 |\n\n---\n\n## 7. Known Caveats\n\n1. **DS accuracy truncation-dominated**: 58–76% truncation even at 8k tokens. All DS accuracy = lower bound (D086).\n2. **QW batch mismatch**: b2_fix experiments used max_new_tokens=8192 vs batch1's 2048. Impact minimal (s020: +1, s025: 0).\n3. **QW s015 n=50 marginal**: bf16 CI [−0.005, 0.110] crosses zero. Resolved at n=475.\n4. **Entropy mechanism model-dependent**: Qwen s025 entropy reversed (+0.045). Paper uses discrimination collapse (Gini/CV) as primary mechanism.\n5. **LLaMA strategy×phase interaction weak**: d_z 0.19–0.34; random also shows phase gradient. Use \"suggests\"/\"partial support\" language.\n6. **GSM8K strategy specificity 衰减**: 2.3–3.8× vs MATH-500 15–36×. Phase gradient robust, magnitude ratio task-dependent.\n7. **c5b pilot gate failed**: Oracle 18% < 30%. CI crosses zero for both oracle and heuristic.\n8. **Bonferroni revision (D066)**: k=4 family-wise (revised from k=48). DS rand s025/s030 restored to significant.\n9. **G× correction**: Paper must update from 58–241× to 21–64×.\n\n---\n\n## 8. Missing / Pending Data\n\n| Item | Status | Impact |\n|------|--------|--------|\n| acc_ds_s015_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| acc_ds_s030_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| QW batch1 v2 rescore (s015/s030/dense) | Not started | Low priority: s020 v2 showed zero change |\n| G× values not in registry | Post-hoc computation | Reference compute_gx_final.py; values in memory.md |\n| GSM8K QW importance full metrics | In gsm8k_profiling_qw | Only summary values (0.039/0.158/1.1/2.092) without CI |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "round10_data_summary.md",
    "content": "# Round 10 Data Summary — All Experimental Evidence\n\n> Compiled: 2026-05-16 | EMNLP 2026 ARR deadline: 2026-05-25\n\n---\n\n## 1. PPL Dose Curve\n\n### 1a. n=500 Unified Analysis (canonical)\n\n**DeepSeek (c2_n500_deepseek, n=496)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Rand median II | Rand p (Bonf k=4) |\n|----------|--------------|--------|------------|---------------|-------------------|\n| s015 | 0.3907 | [0.350, 0.443] | 1.27e-70 | 0.0139 | 0.863 (NS) |\n| s020 | 1.2149 | [1.107, 1.337] | 3.98e-75 | 0.0315 | 0.280 (NS) |\n| s025 | 3.9857 | [3.527, 4.359] | 1.99e-78 | 0.2574 | 0.0058 ** |\n| s030 | 8.4813 | [7.754, 9.692] | 1.09e-79 | 0.5096 | 0.0059 ** |\n\n- Imp/rand ratio: 15.5–38.6×\n- Adjacent d_z: s015→s020 = −0.925, s020→s025 = −0.824, s025→s030 = −0.773\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n\n**Qwen (c2_qw_n500_r3, n=475, low+high valid filter)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Bonf p | Rand median II | Rand Bonf p |\n|----------|--------------|--------|------------|--------|---------------|------------|\n| s015 | 0.0659 | [0.049, 0.093] | 8.66e-15 | 3.46e-14 | −0.0111 | 0.687 (NS) |\n| s020 | 0.3073 | [0.261, 0.356] | 6.84e-42 | 2.74e-41 | 0.0153 | 0.800 (NS) |\n| s025 | 1.0745 | [0.977, 1.179] | 1.06e-68 | 4.25e-68 | 0.3931 | 6.37e-11 *** |\n| s030 | 3.1550 | [2.783, 3.558] | 9.21e-74 | 3.69e-73 | 0.9127 | 1.17e-14 *** |\n\n- Imp/rand ratio: 2.7–20.1×\n- Adjacent d_z: s015→s020 = −0.629, s020→s025 = −0.865, s025→s030 = −0.767\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n- Mid-null rate: 45.2% (filter: low+high valid only)\n\n### 1b. bf16 Paired Statistics (n≈50, per-problem)\n\n**DeepSeek importance (bf16_ds_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|------------|----------|\n| s015 | 0.3236 | 0 | 0.607 | 0 | 49 |\n| s020 | 1.1520 | 0 | 0.725 | 0 | 49 |\n| s025 | 3.9686 | 0 | 0.953 | 0 | 49 |\n| s030 | 9.9436 | 0 | 1.126 | 0 | 49 |\n\n**Qwen importance (bf16_qw_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Bootstrap CI | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|-------------|------------|----------|\n| s015 | 0.0476 | 0.0001 | 0.371 | [−0.005, 0.110] | 0.030 | 46 |\n| s020 | 0.2075 | 0 | 0.722 | [0.067, 0.402] | 3.4e-5 | 46 |\n| s025 | 1.1087 | 0 | 1.233 | [0.609, 1.469] | 0 | 46 |\n| s030 | 2.6194 | 0 | 1.439 | [1.722, 3.651] | 0 | 46 |\n\n⚠️ QW s015 n=50 CI crosses zero [−0.005, 0.110]; resolved at n=475 (CI [0.049, 0.093], p=3.5e-14).\n\n**Random controls (bf16, both models):** All 8 conditions FAIL — no structured phase gradient. DS rand median II range 0.09–4.04; QW rand median II range 0.14–8.07. All permutation p > 0.01 or CI overlapping.\n\n### 1c. Boundary Sparsity (s010, s035)\n\n| Condition | II_low median | II_mid median | II_high median | Verdict |\n|-----------|--------------|--------------|----------------|---------|\n| DS imp s010 | 0.0151 | 0.0061 | 0.0027 | FAIL (near-zero II) |\n| DS imp s035 | 28.76 | 4.95 | 0.11 | PASS (extends monotonic) |\n| QW imp s010 | −0.0444 | −0.0359 | 0.0001 | FAIL (near-zero II) |\n| QW imp s035 | 8.24 | 0.96 | 0.02 | PASS (extends monotonic) |\n\n---\n\n## 2. QW Accuracy Dose Curve (MATH-500, n=100)\n\nSource: acc_qw_dense_n100, acc_qw_s015_n100, acc_qw_s020_n100_b2_fix, acc_qw_s025_n100_b2_fix, acc_qw_s030_n100\n\n| Sparsity | Accuracy | Correct/100 | Δ vs dense | Note |\n|----------|----------|-------------|-----------|------|\n| dense | 0.40 | 40 | — | |\n| s015 | 0.36 | 36 | −0.04 | |\n| s020 | 0.36 | 36 | −0.04 | b2_fix: +1 vs original (35→36) |\n| s025 | 0.33 | 33 | −0.07 | b2_fix: unchanged (33→33) |\n| s030 | 0.19 | 19 | −0.21 | steep cliff from s025 |\n\n- s015 ≈ s020 plateau (−4pp); cliff at s025→s030 (−14pp)\n- b2_fix used max_new_tokens=8192 for batch2; batch1 used 2048 (mismatch noted)\n- ⚠️ s015/s030/dense batch1 未走 v2 rescore; s020 v2 rescore confirmed no change\n\n---\n\n## 3. DS Accuracy (8k v2, n=50, 定性观察)\n\nSource: acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2 + pending\n\n| Sparsity | Accuracy | Truncation Rate | Avg Tokens | Status |\n|----------|----------|-----------------|-----------|--------|\n| dense | 0.74 | 0.16 | 3126 | DONE |\n| s015 | — | — | — | **RUNNING** |\n| s020 | 0.30 | 0.58 | — | DONE |\n| s025 | 0.08 | 0.76 | 6344 | DONE |\n| s030 | — | — | — | **RUNNING** |\n\n**Caveat (D086):** Truncation rate 58–76% even at 8k tokens. DS under sparsity generates extremely long outputs; accuracy = lower bound under token budget constraint. 降为定性观察，不纳入统计检验。\n\n4k baseline for reference: ds_dense_acc=0.52 (truncation 56%), ds_s015_acc=0.36, ds_s030_acc=0.10.\n\n---\n\n## 4. GSM8K Cross-Benchmark (C10)\n\n### 4a. Importance Masking Phase Gradient\n\nSource: gsm8k_profiling_ds, gsm8k_profiling_qw\n\n| Model | s015 | s020 | s025 | s030 | Monotonic |\n|-------|------|------|------|------|-----------|\n| DS median gradient | 0.241 | 0.740 | 1.992 | 4.682 | ✓ |\n| DS CI | [0.077, 0.478] | [0.314, 1.119] | [0.933, 2.820] | [2.121, 10.557] | |\n| DS Wilcoxon p | 0.0003 | 0.0001 | 0.0001 | 0.0001 | |\n| QW median gradient | 0.039 | 0.158 | 1.100 | 2.092 | ✓ |\n\n### 4b. Strategy Specificity (imp/rand ratio)\n\n| Sparsity | Ratio (GSM8K) | Ratio (MATH-500) |\n|----------|--------------|-----------------|\n| s015 | 2.3× | 28.1× (DS) / 5.9× (QW) |\n| s020 | 2.5× | 38.6× (DS) / 20.1× (QW) |\n| s025 | 3.8× | 15.5× (DS) / 2.7× (QW) |\n| s030 | 2.8× | 16.6× (DS) / 3.5× (QW) |\n\nStrategy specificity ratio 从 MATH-500 的 15–36× 衰减至 GSM8K 的 2.3–3.8×（task-dependent）。\n\n### 4c. QW Random GSM8K (补全数据)\n\nSource: gsm8k_qw_rand_s025_v2, gsm8k_qw_rand_s030_v2\n\n| Condition | II_high median | II_mid median | II_low median | Verdict |\n|-----------|---------------|--------------|--------------|---------|\n| QW rand s025 | 0.718 | 1.127 | 1.459 | PASS |\n| QW rand s030 | 2.310 | 2.700 | 5.200 | PASS |\n\nRandom masking 在 GSM8K s025+s030 也产生 positive compound interaction（与 MATH-500 random FAIL 不同）。\n\n---\n\n## 5. Additional Evidence\n\n### 5a. sf5 Asymmetric Sparsity (sf5_asymmetric_spot)\n\n| Config | Head% | KV% | II_low | II_mid | II_high | D (low−high) |\n|--------|-------|-----|--------|--------|---------|-------------|\n| A | 0.20 | 0.30 | 19.51 | 6.05 | 0.38 | 19.13 |\n| B | 0.30 | 0.20 | 18.77 | 3.97 | 0.52 | 18.25 |\n\n- Phase gradient direction 完全稳健（D > 0 both configs）\n- KV sparsity 较高时 mid-phase II 更大（6.05 vs 3.97）\n- Head sparsity 较高时 high-phase II 略升（0.52 vs 0.38）\n- Pre-registered criterion: PASS\n\n### 5b. Appendix B G× Correction\n\n- 旧值: 58–241×\n- 修正值: **21–64×**（per-problem additive II + aggregate PPL 修正）\n- 计算脚本: `/root/autodl-tmp/pacs/compute_gx_final.py`\n- 来源: memory.md（未注册为独立实验）\n\n### 5c. Cross-Model Mann-Whitney U (n=475 reanalysis)\n\n- Qwen 从 n=274 (complete-case) 修正为 n=475 (low+high valid only)\n- 分析脚本: `analyze_n500_v2.py` → `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\n- Bonferroni 修订 (D066): k=4 family-wise（原 k=48）\n- DS rand s025/s030: Bonf p ≈ 0.006（恢复为显著）\n- BH-FDR (48 tests): rand s025/s030 fdr_p = 0.0019\n- 所有 imp 条件 *** 在 n=475 下保持显著\n\n### 5d. c4_entropy — Discrimination Collapse Mechanism\n\n**DeepSeek (c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.040 | −0.047 | −0.045 | −0.044 |\n| Rand entropy Δ | +0.128 | +0.136 | +0.217 | +0.233 |\n| Imp Gini Δ | −0.030 | −0.040 | −0.065 | −0.081 |\n| Imp CV Δ | −0.564 | −0.774 | −1.287 | −1.665 |\n\n**Qwen (qwen_c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.073 | −0.076 | **+0.045** | −0.007 |\n| Rand entropy Δ | +0.084 | +0.090 | +0.217 | +0.197 |\n| Imp Gini Δ | −0.010 | −0.012 | −0.010 | −0.020 |\n| Imp CV Δ | −0.045 | −0.208 | −1.491 | −1.142 |\n\n**结论:** Gini/CV 下降跨模型一致（discrimination collapse confirmed）。Entropy redistribution DS 一致但 QW s025 方向反转（+0.045）— model-dependent，不作为主线机制。\n\n### 5e. c3_llama — Cross-Architecture Validation\n\n- Model: DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\n- 8/8 conditions complete (imp + rand × 4 sparsity)\n- Within-importance phase gradient: d_z ≈ 1.0 across all sparsity levels ✓\n- imp_vs_rand d_z: 0.19→0.26→0.29→0.34（仅 s030 Bonferroni p=0.029 显著）\n- Random also shows significant phase gradient (d_z 0.35→0.44, CI excludes zero)\n- Qualitative direction consistent; strategy×phase interaction weaker + architecture-dependent\n\n### 5f. c5b_pilot — Phase-Gated Controller\n\n| Metric | s025 |\n|--------|------|\n| Uniform median II | 1.0435 |\n| Oracle median II | 0.856 |\n| Oracle recovery | 18% (CI [−39, 45.8], p=0.002) |\n| Heuristic median II | 0.713 |\n| Heuristic recovery | 31.7% (CI [−22.8, 66], p=0.024) |\n| Gate criterion | oracle > 30% |\n| Gate result | **FAIL** |\n\nDirection correct (Wilcoxon significant) but effect size insufficient. → §8 Future Work.\n\n---\n\n## 6. Claim–Evidence Mapping\n\n| Claim | Status | Primary Evidence (exp_id) |\n|-------|--------|--------------------------|\n| C1: Strategy- & task-modulated severity | confirmed | c2_n500_deepseek, c2_qw_n500_r3 (imp/rand ratio 15–39× DS, 2.7–20× QW); gsm8k_profiling_ds/qw (ratio 衰减至 2.3–3.8×) |\n| C2: Phase-modulated (low > high) | confirmed | bf16_ds_imp_s015–s030 (0.32→9.94); bf16_qw_imp_s015–s030 (0.048→2.619); n500 confirms all p < 1e-14 |\n| C3: Phase-strategy crossover | confirmed | bf16_importance_s025 (imp low=7.196 > rand low=1.363; imp high=0.032 < rand high=0.818) |\n| C4: Discrimination collapse | partially | c4_entropy (DS: Gini/CV ✓, entropy ✓); qwen_c4_entropy (Gini/CV ✓, entropy ✗ at s025) |\n| C5: Cross-model generalization | confirmed | c2_n500_deepseek + c2_qw_n500_r3: ρ=1.0 both, QW magnitude ~1/4 DS |\n| C5b: Phase-aware mitigation | gate_failed | c5b_pilot: oracle 18% < 30% gate → future work |\n| C6: Sub-exponential growth | confirmed | Δ growth factors: 3.8×→4.8×→2.0× (递减) |\n| C7: n=500 dose-response | confirmed | c2_n500_deepseek (n=496) + c2_qw_n500_r3 (n=475): monotonic, ρ=1.0 |\n| C8: Cross-architecture (LLaMA) | partially | c3_llama: within-imp d_z≈1.0 ✓; imp_vs_rand weak (d_z 0.19–0.34); rand also shows gradient |\n| C10: Cross-benchmark (GSM8K) | confirmed | gsm8k_profiling_ds/qw: monotonic ✓; gsm8k_qw_rand_s025/s030_v2: random也显著 |\n| S3→C: Model-dependent onset | confirmed | QW s015 n=50 CI crosses zero; n=475 resolves (p=3.5e-14). DS significant from s015+ |\n| S7→C: Dose-response monotonicity | confirmed | Spearman ρ=1.0 both models (n=500), perm p=0.0417 |\n\n---\n\n## 7. Known Caveats\n\n1. **DS accuracy truncation-dominated**: 58–76% truncation even at 8k tokens. All DS accuracy = lower bound (D086).\n2. **QW batch mismatch**: b2_fix experiments used max_new_tokens=8192 vs batch1's 2048. Impact minimal (s020: +1, s025: 0).\n3. **QW s015 n=50 marginal**: bf16 CI [−0.005, 0.110] crosses zero. Resolved at n=475.\n4. **Entropy mechanism model-dependent**: Qwen s025 entropy reversed (+0.045). Paper uses discrimination collapse (Gini/CV) as primary mechanism.\n5. **LLaMA strategy×phase interaction weak**: d_z 0.19–0.34; random also shows phase gradient. Use \"suggests\"/\"partial support\" language.\n6. **GSM8K strategy specificity 衰减**: 2.3–3.8× vs MATH-500 15–36×. Phase gradient robust, magnitude ratio task-dependent.\n7. **c5b pilot gate failed**: Oracle 18% < 30%. CI crosses zero for both oracle and heuristic.\n8. **Bonferroni revision (D066)**: k=4 family-wise (revised from k=48). DS rand s025/s030 restored to significant.\n9. **G× correction**: Paper must update from 58–241× to 21–64×.\n\n---\n\n## 8. Missing / Pending Data\n\n| Item | Status | Impact |\n|------|--------|--------|\n| acc_ds_s015_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| acc_ds_s030_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| QW batch1 v2 rescore (s015/s030/dense) | Not started | Low priority: s020 v2 showed zero change |\n| G× values not in registry | Post-hoc computation | Reference compute_gx_final.py; values in memory.md |\n| GSM8K QW importance full metrics | In gsm8k_profiling_qw | Only summary values (0.039/0.158/1.1/2.092) without CI |\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T00:34:21.364204+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'round10_data_summary.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T00:34:21.364370+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T00:34:21.364583+00:00_

R9-C2
_project
analysis_pipeline_audit.md
analysis_pipeline_readiness.md
analysis_pipeline_verification.md
analyze_c2_n500.py
appendix_b_precise_gx
bf16_qw_imp_failures_diagnosis.md
bf16_qw_rand_s015
bf16_qw_rand_s020
bf16_qw_rand_s025
bf16_qw_rand_s030
bootstrap_phase_gradient.py
c2_n500_deepseek
c2_n500_paper_update_checklist.md
c2_progress_report.md
c2_progress_snapshot.json
c2_qw_n500_investigation.md
c3_llama
c3_llama_results.json
c5b_framing_proposal.md
c5b_pilot
c5b_pilot_design.md
c5b_pilot_diagnosis.md
compute_multiplicative_null.py
consistency_audit_final.md
consistency_audit_report.md
consistency_report.md
crossover_n500.csv
crossover_n500.md
dream_reports
exp_progress_check_20260516.md
gpu_check_loop7.md
gsm8k_diagnosis
gsm8k_importance_bug
gsm8k_profiling
gsm8k_profiling_ds
gsm8k_profiling_ds_diagnosis.md
gsm8k_token_length
literature_scan_20260515.md
literature_scan_phase_adaptive.md
m1_phase_segmentation_analysis.md
m2_figure1_n500
m2_m4_code_readiness.md
magnitude_crossover_novelty_check.md
main.pdf
main_r6_revised.pdf
main_r7_revised.pdf
manifest.yaml
math500_token_length
mechanistic_explanation.md
mid_sparsity_gap_analysis.md
mvp_ii_analysis.md
mvp_ii_profiling_v2
mvp_ii_profiling_v3
mvp_ii_v3_analysis.md
mvp_interaction_index_profiling
n1a_answer_region
n1a_boxed_validation
n500_analysis
n500_analysis_pipeline_ready.md
n500_analysis_readiness.md
n500_paper_patch_plan.md
n500_paper_update_FINAL.md
n500_paper_update_checklist.md
n500_paper_update_plan.md
n500_pipeline_check.md
n500_progress_20260515_0632.md
n500_progress_check.md
n500_update_checklist.md
novelty_evidence_summary.md
number_consistency_audit_v2.md
p1_appendix_b_null
p3_figure1
pacs
paper_n500_update_checklist.md
paper_n500_update_plan.md
paper_placeholder_audit.md
paper_update_checklist.md
qwen_kill_investigation.md
qwen_status_check.md
r8_citations
reference_audit.md
reference_audit_report.md
report_analysis_pipeline_ready.md
report_process_check.md
review_issues.yaml
review_reports

…[truncated 150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T00:34:21.364753+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T00:34:21.364877+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T00:34:21.365035+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "round10_data_summary",
  "type": "report",
  "description": "Round 10 完整数据编译：PPL dose curve (n=500), QW/DS accuracy, GSM8K cross-benchmark, sf5/entropy/LLaMA/pilot 补充证据，claim-evidence mapping，caveats 和 pending items",
  "project": "phase-gated-compound-sparse",
  "content_filename": "round10_data_summary.md",
  "tags": "['round10', 'data-compilation', 'emnlp2026']",
  "content": "# Round 10 Data Summary — All Experimental Evidence\n\n> Compiled: 2026-05-16 | EMNLP 2026 ARR deadline: 2026-05-25\n\n---\n\n## 1. PPL Dose Curve\n\n### 1a. n=500 Unified Analysis (canonical)\n\n**DeepSeek (c2_n500_deepseek, n=496)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Rand median II | Rand p (Bonf k=4) |\n|----------|--------------|--------|------------|---------------|-------------------|\n| s015 | 0.3907 | [0.350, 0.443] | 1.27e-70 | 0.0139 | 0.863 (NS) |\n| s020 | 1.2149 | [1.107, 1.337] | 3.98e-75 | 0.0315 | 0.280 (NS) |\n| s025 | 3.9857 | [3.527, 4.359] | 1.99e-78 | 0.2574 | 0.0058 ** |\n| s030 | 8.4813 | [7.754, 9.692] | 1.09e-79 | 0.5096 | 0.0059 ** |\n\n- Imp/rand ratio: 15.5–38.6×\n- Adjacent d_z: s015→s020 = −0.925, s020→s025 = −0.824, s025→s030 = −0.773\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n\n**Qwen (c2_qw_n500_r3, n=475, low+high valid filter)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Bonf p | Rand median II | Rand Bonf p |\n|----------|--------------|--------|------------|--------|---------------|------------|\n| s015 | 0.0659 | [0.049, 0.093] | 8.66e-15 | 3.46e-14 | −0.0111 | 0.687 (NS) |\n| s020 | 0.3073 | [0.261, 0.356] | 6.84e-42 | 2.74e-41 | 0.0153 | 0.800 (NS) |\n| s025 | 1.0745 | [0.977, 1.179] | 1.06e-68 | 4.25e-68 | 0.3931 | 6.37e-11 *** |\n| s030 | 3.1550 | [2.783, 3.558] | 9.21e-74 | 3.69e-73 | 0.9127 | 1.17e-14 *** |\n\n- Imp/rand ratio: 2.7–20.1×\n- Adjacent d_z: s015→s020 = −0.629, s020→s025 = −0.865, s025→s030 = −0.767\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n- Mid-null rate: 45.2% (filter: low+high valid only)\n\n### 1b. bf16 Paired Statistics (n≈50, per-problem)\n\n**DeepSeek importance (bf16_ds_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|------------|----------|\n| s015 | 0.3236 | 0 | 0.607 | 0 | 49 |\n| s020 | 1.1520 | 0 | 0.725 | 0 | 49 |\n| s025 | 3.9686 | 0 | 0.953 | 0 | 49 |\n| s030 | 9.9436 | 0 | 1.126 | 0 | 49 |\n\n**Qwen importance (bf16_qw_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Bootstrap CI | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|-------------|------------|----------|\n| s015 | 0.0476 | 0.0001 | 0.371 | [−0.005, 0.110] | 0.030 | 46 |\n| s020 | 0.2075 | 0 | 0.722 | [0.067, 0.402] | 3.4e-5 | 46 |\n| s025 | 1.1087 | 0 | 1.233 | [0.609, 1.469] | 0 | 46 |\n| s030 | 2.6194 | 0 | 1.439 | [1.722, 3.651] | 0 | 46 |\n\n⚠️ QW s015 n=50 CI crosses zero [−0.005, 0.110]; resolved at n=475 (CI [0.049, 0.093], p=3.5e-14).\n\n**Random controls (bf16, both models):** All 8 conditions FAIL — no structured phase gradient. DS rand median II range 0.09–4.04; QW rand median II range 0.14–8.07. All permutation p > 0.01 or CI overlapping.\n\n### 1c. Boundary Sparsity (s010, s035)\n\n| Condition | II_low median | II_mid median | II_high median | Verdict |\n|-----------|--------------|--------------|----------------|---------|\n| DS imp s010 | 0.0151 | 0.0061 | 0.0027 | FAIL (near-zero II) |\n| DS imp s035 | 28.76 | 4.95 | 0.11 | PASS (extends monotonic) |\n| QW imp s010 | −0.0444 | −0.0359 | 0.0001 | FAIL (near-zero II) |\n| QW imp s035 | 8.24 | 0.96 | 0.02 | PASS (extends monotonic) |\n\n---\n\n## 2. QW Accuracy Dose Curve (MATH-500, n=100)\n\nSource: acc_qw_dense_n100, acc_qw_s015_n100, acc_qw_s020_n100_b2_fix, acc_qw_s025_n100_b2_fix, acc_qw_s030_n100\n\n| Sparsity | Accuracy | Correct/100 | Δ vs dense | Note |\n|----------|----------|-------------|-----------|------|\n| dense | 0.40 | 40 | — | |\n| s015 | 0.36 | 36 | −0.04 | |\n| s020 | 0.36 | 36 | −0.04 | b2_fix: +1 vs original (35→36) |\n| s025 | 0.33 | 33 | −0.07 | b2_fix: unchanged (33→33) |\n| s030 | 0.19 | 19 | −0.21 | steep cliff from s025 |\n\n- s015 ≈ s020 plateau (−4pp); cliff at s025→s030 (−14pp)\n- b2_fix used max_new_tokens=8192 for batch2; batch1 used 2048 (mismatch noted)\n- ⚠️ s015/s030/dense batch1 未走 v2 rescore; s020 v2 rescore confirmed no change\n\n---\n\n## 3. DS Accuracy (8k v2, n=50, 定性观察)\n\nSource: acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2 + pending\n\n| Sparsity | Accuracy | Truncation Rate | Avg Tokens | Status |\n|----------|----------|-----------------|-----------|--------|\n| dense | 0.74 | 0.16 | 3126 | DONE |\n| s015 | — | — | — | **RUNNING** |\n| s020 | 0.30 | 0.58 | — | DONE |\n| s025 | 0.08 | 0.76 | 6344 | DONE |\n| s030 | — | — | — | **RUNNING** |\n\n**Caveat (D086):** Truncation rate 58–76% even at 8k tokens. DS under sparsity generates extremely long outputs; accuracy = lower bound under token budget constraint. 降为定性观察，不纳入统计检验。\n\n4k baseline for reference: ds_dense_acc=0.52 (truncation 56%), ds_s015_acc=0.36, ds_s030_acc=0.10.\n\n---\n\n## 4. GSM8K Cross-Benchmark (C10)\n\n### 4a. Importance Masking Phase Gradient\n\nSource: gsm8k_profiling_ds, gsm8k_profiling_qw\n\n| Model | s015 | s020 | s025 | s030 | Monotonic |\n|-------|------|------|------|------|-----------|\n| DS median gradient | 0.241 | 0.740 | 1.992 | 4.682 | ✓ |\n| DS CI | [0.077, 0.478] | [0.314, 1.119] | [0.933, 2.820] | [2.121, 10.557] | |\n| DS Wilcoxon p | 0.0003 | 0.0001 | 0.0001 | 0.0001 | |\n| QW median gradient | 0.039 | 0.158 | 1.100 | 2.092 | ✓ |\n\n### 4b. Strategy Specificity (imp/rand ratio)\n\n| Sparsity | Ratio (GSM8K) | Ratio (MATH-500 DS) | Ratio (MATH-500 QW) |\n|----------|--------------|--------------------|--------------------|\n| s015 | 2.3× | 28.1× | 5.9× |\n| s020 | 2.5× | 38.6× | 20.1× |\n| s025 | 3.8× | 15.5× | 2.7× |\n| s030 | 2.8× | 16.6× | 3.5× |\n\nStrategy specificity ratio 从 MATH-500 的 15–36× 衰减至 GSM8K 的 2.3–3.8×（task-dependent）。\n\n### 4c. QW Random GSM8K (补全数据)\n\nSource: gsm8k_qw_rand_s025_v2, gsm8k_qw_rand_s030_v2\n\n| Condition | II_high median | II_mid median | II_low median | Verdict |\n|-----------|---------------|--------------|--------------|---------|\n| QW rand s025 | 0.718 | 1.127 | 1.459 | PASS |\n| QW rand s030 | 2.310 | 2.700 | 5.200 | PASS |\n\nRandom masking 在 GSM8K s025+s030 也产生 positive compound interaction（与 MATH-500 random FAIL 不同）。\n\n---\n\n## 5. Additional Evidence\n\n### 5a. sf5 Asymmetric Sparsity (sf5_asymmetric_spot)\n\n| Config | Head% | KV% | II_low | II_mid | II_high | D (low−high) |\n|--------|-------|-----|--------|--------|---------|-------------|\n| A | 0.20 | 0.30 | 19.51 | 6.05 | 0.38 | 19.13 |\n| B | 0.30 | 0.20 | 18.77 | 3.97 | 0.52 | 18.25 |\n\n- Phase gradient direction 完全稳健（D > 0 both configs）\n- KV sparsity 较高时 mid-phase II 更大（6.05 vs 3.97）\n- Head sparsity 较高时 high-phase II 略升（0.52 vs 0.38）\n- Pre-registered criterion: PASS\n\n### 5b. Appendix B G× Correction\n\n- 旧值: 58–241×\n- 修正值: **21–64×**（per-problem additive II + aggregate PPL 修正）\n- 计算脚本: `/root/autodl-tmp/pacs/compute_gx_final.py`\n- 来源: memory.md（未注册为独立实验）\n\n### 5c. Cross-Model Mann-Whitney U (n=475 reanalysis)\n\n- Qwen 从 n=274 (complete-case) 修正为 n=475 (low+high valid only)\n- 分析脚本: `analyze_n500_v2.py` → `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\n- Bonferroni 修订 (D066): k=4 family-wise（原 k=48）\n- DS rand s025/s030: Bonf p ≈ 0.006（恢复为显著）\n- BH-FDR (48 tests): rand s025/s030 fdr_p = 0.0019\n- 所有 imp 条件 *** 在 n=475 下保持显著\n\n### 5d. c4_entropy — Discrimination Collapse Mechanism\n\n**DeepSeek (c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.040 | −0.047 | −0.045 | −0.044 |\n| Rand entropy Δ | +0.128 | +0.136 | +0.217 | +0.233 |\n| Imp Gini Δ | −0.030 | −0.040 | −0.065 | −0.081 |\n| Imp CV Δ | −0.564 | −0.774 | −1.287 | −1.665 |\n\n**Qwen (qwen_c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.073 | −0.076 | **+0.045** | −0.007 |\n| Rand entropy Δ | +0.084 | +0.090 | +0.217 | +0.197 |\n| Imp Gini Δ | −0.010 | −0.012 | −0.010 | −0.020 |\n| Imp CV Δ | −0.045 | −0.208 | −1.491 | −1.142 |\n\n**结论:** Gini/CV 下降跨模型一致（discrimination collapse confirmed）。Entropy redistribution DS 一致但 QW s025 方向反转（+0.045）— model-dependent，不作为主线机制。\n\n### 5e. c3_llama — Cross-Architecture Validation\n\n- Model: DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\n- 8/8 conditions complete (imp + rand × 4 sparsity)\n- Within-importance phase gradient: d_z ≈ 1.0 across all sparsity levels ✓\n- imp_vs_rand d_z: 0.19→0.26→0.29→0.34（仅 s030 Bonferroni p=0.029 显著）\n- Random also shows significant phase gradient (d_z 0.35→0.44, CI excludes zero)\n- Qualitative direction consistent; strategy×phase interaction weaker + architecture-dependent\n\n### 5f. c5b_pilot — Phase-Gated Controller\n\n| Metric | s025 |\n|--------|------|\n| Uniform median II | 1.0435 |\n| Oracle median II | 0.856 |\n| Oracle recovery | 18% (CI [−39, 45.8], p=0.002) |\n| Heuristic median II | 0.713 |\n| Heuristic recovery | 31.7% (CI [−22.8, 66], p=0.024) |\n| Gate criterion | oracle > 30% |\n| Gate result | **FAIL** |\n\nDirection correct (Wilcoxon significant) but effect size insufficient. → §8 Future Work.\n\n---\n\n## 6. Claim–Evidence Mapping\n\n| Claim | Status | Primary Evidence (exp_id) |\n|-------|--------|--------------------------|\n| C1: Strategy- and task-modulated severity | confirmed | c2_n500_deepseek, c2_qw_n500_r3 (imp/rand ratio 15–39× DS, 2.7–20× QW); gsm8k_profiling_ds/qw (ratio 衰减至 2.3–3.8×) |\n| C2: Phase-modulated (low > high) | confirmed | bf16_ds_imp_s015–s030 (0.32→9.94); bf16_qw_imp_s015–s030 (0.048→2.619); n500 confirms all p < 1e-14 |\n| C3: Phase-strategy crossover | confirmed | bf16_importance_s025 (imp low=7.196 > rand low=1.363; imp high=0.032 < rand high=0.818) |\n| C4: Discrimination collapse | partially | c4_entropy (DS: Gini/CV ✓, entropy ✓); qwen_c4_entropy (Gini/CV ✓, entropy ✗ at s025) |\n| C5: Cross-model generalization | confirmed | c2_n500_deepseek + c2_qw_n500_r3: ρ=1.0 both, QW magnitude ~1/4 DS |\n| C5b: Phase-aware mitigation | gate_failed | c5b_pilot: oracle 18% < 30% gate → future work |\n| C6: Sub-exponential growth | confirmed | Δ growth factors: 3.8×→4.8×→2.0× (递减) |\n| C7: n=500 dose-response | confirmed | c2_n500_deepseek (n=496) + c2_qw_n500_r3 (n=475): monotonic, ρ=1.0 |\n| C8: Cross-architecture (LLaMA) | partially | c3_llama: within-imp d_z≈1.0 ✓; imp_vs_rand weak (d_z 0.19–0.34); rand also shows gradient |\n| C10: Cross-benchmark (GSM8K) | confirmed | gsm8k_profiling_ds/qw: monotonic ✓; gsm8k_qw_rand_s025/s030_v2: random 也显著 |\n| S3→C: Model-dependent onset | confirmed | QW s015 n=50 CI crosses zero; n=475 resolves (p=3.5e-14). DS significant from s015+ |\n| S7→C: Dose-response monotonicity | confirmed | Spearman ρ=1.0 both models (n=500), perm p=0.0417 |\n\n---\n\n## 7. Known Caveats\n\n1. **DS accuracy truncation-dominated**: 58–76% truncation even at 8k tokens. All DS accuracy = lower bound (D086).\n2. **QW batch mismatch**: b2_fix experiments used max_new_tokens=8192 vs batch1's 2048. Impact minimal (s020: +1, s025: 0).\n3. **QW s015 n=50 marginal**: bf16 CI [−0.005, 0.110] crosses zero. Resolved at n=475.\n4. **Entropy mechanism model-dependent**: Qwen s025 entropy reversed (+0.045). Paper uses discrimination collapse (Gini/CV) as primary mechanism.\n5. **LLaMA strategy×phase interaction weak**: d_z 0.19–0.34; random also shows phase gradient. Use \"suggests\"/\"partial support\" language.\n6. **GSM8K strategy specificity 衰减**: 2.3–3.8× vs MATH-500 15–36×. Phase gradient robust, magnitude ratio task-dependent.\n7. **c5b pilot gate failed**: Oracle 18% < 30%. CI crosses zero for both oracle and heuristic.\n8. **Bonferroni revision (D066)**: k=4 family-wise (revised from k=48). DS rand s025/s030 restored to significant.\n9. **G× correction**: Paper must update from 58–241× to 21–64×.\n\n---\n\n## 8. Missing / Pending Data\n\n| Item | Status | Impact |\n|------|--------|--------|\n| acc_ds_s015_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| acc_ds_s030_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| QW batch1 v2 rescore (s015/s030/dense) | Not started | Low priority: s020 v2 showed zero change |\n| G× values not in registry | Post-hoc computation | Reference compute_gx_final.py; values in memory.md |\n| GSM8K QW importance full metrics | In gsm8k_profiling_qw | Only summary values (0.039/0.158/1.1/2.092) without CI |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "round10_data_summary",
    "type": "report",
    "description": "Round 10 完整数据编译：PPL dose curve (n=500), QW/DS accuracy, GSM8K cross-benchmark, sf5/entropy/LLaMA/pilot 补充证据，claim-evidence mapping，caveats 和 pending items",
    "project": "phase-gated-compound-sparse",
    "content_filename": "round10_data_summary.md",
    "tags": "['round10', 'data-compilation', 'emnlp2026']",
    "content": "# Round 10 Data Summary — All Experimental Evidence\n\n> Compiled: 2026-05-16 | EMNLP 2026 ARR deadline: 2026-05-25\n\n---\n\n## 1. PPL Dose Curve\n\n### 1a. n=500 Unified Analysis (canonical)\n\n**DeepSeek (c2_n500_deepseek, n=496)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Rand median II | Rand p (Bonf k=4) |\n|----------|--------------|--------|------------|---------------|-------------------|\n| s015 | 0.3907 | [0.350, 0.443] | 1.27e-70 | 0.0139 | 0.863 (NS) |\n| s020 | 1.2149 | [1.107, 1.337] | 3.98e-75 | 0.0315 | 0.280 (NS) |\n| s025 | 3.9857 | [3.527, 4.359] | 1.99e-78 | 0.2574 | 0.0058 ** |\n| s030 | 8.4813 | [7.754, 9.692] | 1.09e-79 | 0.5096 | 0.0059 ** |\n\n- Imp/rand ratio: 15.5–38.6×\n- Adjacent d_z: s015→s020 = −0.925, s020→s025 = −0.824, s025→s030 = −0.773\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n\n**Qwen (c2_qw_n500_r3, n=475, low+high valid filter)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Bonf p | Rand median II | Rand Bonf p |\n|----------|--------------|--------|------------|--------|---------------|------------|\n| s015 | 0.0659 | [0.049, 0.093] | 8.66e-15 | 3.46e-14 | −0.0111 | 0.687 (NS) |\n| s020 | 0.3073 | [0.261, 0.356] | 6.84e-42 | 2.74e-41 | 0.0153 | 0.800 (NS) |\n| s025 | 1.0745 | [0.977, 1.179] | 1.06e-68 | 4.25e-68 | 0.3931 | 6.37e-11 *** |\n| s030 | 3.1550 | [2.783, 3.558] | 9.21e-74 | 3.69e-73 | 0.9127 | 1.17e-14 *** |\n\n- Imp/rand ratio: 2.7–20.1×\n- Adjacent d_z: s015→s020 = −0.629, s020→s025 = −0.865, s025→s030 = −0.767\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n- Mid-null rate: 45.2% (filter: low+high valid only)\n\n### 1b. bf16 Paired Statistics (n≈50, per-problem)\n\n**DeepSeek importance (bf16_ds_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|------------|----------|\n| s015 | 0.3236 | 0 | 0.607 | 0 | 49 |\n| s020 | 1.1520 | 0 | 0.725 | 0 | 49 |\n| s025 | 3.9686 | 0 | 0.953 | 0 | 49 |\n| s030 | 9.9436 | 0 | 1.126 | 0 | 49 |\n\n**Qwen importance (bf16_qw_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Bootstrap CI | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|-------------|------------|----------|\n| s015 | 0.0476 | 0.0001 | 0.371 | [−0.005, 0.110] | 0.030 | 46 |\n| s020 | 0.2075 | 0 | 0.722 | [0.067, 0.402] | 3.4e-5 | 46 |\n| s025 | 1.1087 | 0 | 1.233 | [0.609, 1.469] | 0 | 46 |\n| s030 | 2.6194 | 0 | 1.439 | [1.722, 3.651] | 0 | 46 |\n\n⚠️ QW s015 n=50 CI crosses zero [−0.005, 0.110]; resolved at n=475 (CI [0.049, 0.093], p=3.5e-14).\n\n**Random controls (bf16, both models):** All 8 conditions FAIL — no structured phase gradient. DS rand median II range 0.09–4.04; QW rand median II range 0.14–8.07. All permutation p > 0.01 or CI overlapping.\n\n### 1c. Boundary Sparsity (s010, s035)\n\n| Condition | II_low median | II_mid median | II_high median | Verdict |\n|-----------|--------------|--------------|----------------|---------|\n| DS imp s010 | 0.0151 | 0.0061 | 0.0027 | FAIL (near-zero II) |\n| DS imp s035 | 28.76 | 4.95 | 0.11 | PASS (extends monotonic) |\n| QW imp s010 | −0.0444 | −0.0359 | 0.0001 | FAIL (near-zero II) |\n| QW imp s035 | 8.24 | 0.96 | 0.02 | PASS (extends monotonic) |\n\n---\n\n## 2. QW Accuracy Dose Curve (MATH-500, n=100)\n\nSource: acc_qw_dense_n100, acc_qw_s015_n100, acc_qw_s020_n100_b2_fix, acc_qw_s025_n100_b2_fix, acc_qw_s030_n100\n\n| Sparsity | Accuracy | Correct/100 | Δ vs dense | Note |\n|----------|----------|-------------|-----------|------|\n| dense | 0.40 | 40 | — | |\n| s015 | 0.36 | 36 | −0.04 | |\n| s020 | 0.36 | 36 | −0.04 | b2_fix: +1 vs original (35→36) |\n| s025 | 0.33 | 33 | −0.07 | b2_fix: unchanged (33→33) |\n| s030 | 0.19 | 19 | −0.21 | steep cliff from s025 |\n\n- s015 ≈ s020 plateau (−4pp); cliff at s025→s030 (−14pp)\n- b2_fix used max_new_tokens=8192 for batch2; batch1 used 2048 (mismatch noted)\n- ⚠️ s015/s030/dense batch1 未走 v2 rescore; s020 v2 rescore confirmed no change\n\n---\n\n## 3. DS Accuracy (8k v2, n=50, 定性观察)\n\nSource: acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2 + pending\n\n| Sparsity | Accuracy | Truncation Rate | Avg Tokens | Status |\n|----------|----------|-----------------|-----------|--------|\n| dense | 0.74 | 0.16 | 3126 | DONE |\n| s015 | — | — | — | **RUNNING** |\n| s020 | 0.30 | 0.58 | — | DONE |\n| s025 | 0.08 | 0.76 | 6344 | DONE |\n| s030 | — | — | — | **RUNNING** |\n\n**Caveat (D086):** Truncation rate 58–76% even at 8k tokens. DS under sparsity generates extremely long outputs; accuracy = lower bound under token budget constraint. 降为定性观察，不纳入统计检验。\n\n4k baseline for reference: ds_dense_acc=0.52 (truncation 56%), ds_s015_acc=0.36, ds_s030_acc=0.10.\n\n---\n\n## 4. GSM8K Cross-Benchmark (C10)\n\n### 4a. Importance Masking Phase Gradient\n\nSource: gsm8k_profiling_ds, gsm8k_profiling_qw\n\n| Model | s015 | s020 | s025 | s030 | Monotonic |\n|-------|------|------|------|------|-----------|\n| DS median gradient | 0.241 | 0.740 | 1.992 | 4.682 | ✓ |\n| DS CI | [0.077, 0.478] | [0.314, 1.119] | [0.933, 2.820] | [2.121, 10.557] | |\n| DS Wilcoxon p | 0.0003 | 0.0001 | 0.0001 | 0.0001 | |\n| QW median gradient | 0.039 | 0.158 | 1.100 | 2.092 | ✓ |\n\n### 4b. Strategy Specificity (imp/rand ratio)\n\n| Sparsity | Ratio (GSM8K) | Ratio (MATH-500 DS) | Ratio (MATH-500 QW) |\n|----------|--------------|--------------------|--------------------|\n| s015 | 2.3× | 28.1× | 5.9× |\n| s020 | 2.5× | 38.6× | 20.1× |\n| s025 | 3.8× | 15.5× | 2.7× |\n| s030 | 2.8× | 16.6× | 3.5× |\n\nStrategy specificity ratio 从 MATH-500 的 15–36× 衰减至 GSM8K 的 2.3–3.8×（task-dependent）。\n\n### 4c. QW Random GSM8K (补全数据)\n\nSource: gsm8k_qw_rand_s025_v2, gsm8k_qw_rand_s030_v2\n\n| Condition | II_high median | II_mid median | II_low median | Verdict |\n|-----------|---------------|--------------|--------------|---------|\n| QW rand s025 | 0.718 | 1.127 | 1.459 | PASS |\n| QW rand s030 | 2.310 | 2.700 | 5.200 | PASS |\n\nRandom masking 在 GSM8K s025+s030 也产生 positive compound interaction（与 MATH-500 random FAIL 不同）。\n\n---\n\n## 5. Additional Evidence\n\n### 5a. sf5 Asymmetric Sparsity (sf5_asymmetric_spot)\n\n| Config | Head% | KV% | II_low | II_mid | II_high | D (low−high) |\n|--------|-------|-----|--------|--------|---------|-------------|\n| A | 0.20 | 0.30 | 19.51 | 6.05 | 0.38 | 19.13 |\n| B | 0.30 | 0.20 | 18.77 | 3.97 | 0.52 | 18.25 |\n\n- Phase gradient direction 完全稳健（D > 0 both configs）\n- KV sparsity 较高时 mid-phase II 更大（6.05 vs 3.97）\n- Head sparsity 较高时 high-phase II 略升（0.52 vs 0.38）\n- Pre-registered criterion: PASS\n\n### 5b. Appendix B G× Correction\n\n- 旧值: 58–241×\n- 修正值: **21–64×**（per-problem additive II + aggregate PPL 修正）\n- 计算脚本: `/root/autodl-tmp/pacs/compute_gx_final.py`\n- 来源: memory.md（未注册为独立实验）\n\n### 5c. Cross-Model Mann-Whitney U (n=475 reanalysis)\n\n- Qwen 从 n=274 (complete-case) 修正为 n=475 (low+high valid only)\n- 分析脚本: `analyze_n500_v2.py` → `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\n- Bonferroni 修订 (D066): k=4 family-wise（原 k=48）\n- DS rand s025/s030: Bonf p ≈ 0.006（恢复为显著）\n- BH-FDR (48 tests): rand s025/s030 fdr_p = 0.0019\n- 所有 imp 条件 *** 在 n=475 下保持显著\n\n### 5d. c4_entropy — Discrimination Collapse Mechanism\n\n**DeepSeek (c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.040 | −0.047 | −0.045 | −0.044 |\n| Rand entropy Δ | +0.128 | +0.136 | +0.217 | +0.233 |\n| Imp Gini Δ | −0.030 | −0.040 | −0.065 | −0.081 |\n| Imp CV Δ | −0.564 | −0.774 | −1.287 | −1.665 |\n\n**Qwen (qwen_c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.073 | −0.076 | **+0.045** | −0.007 |\n| Rand entropy Δ | +0.084 | +0.090 | +0.217 | +0.197 |\n| Imp Gini Δ | −0.010 | −0.012 | −0.010 | −0.020 |\n| Imp CV Δ | −0.045 | −0.208 | −1.491 | −1.142 |\n\n**结论:** Gini/CV 下降跨模型一致（discrimination collapse confirmed）。Entropy redistribution DS 一致但 QW s025 方向反转（+0.045）— model-dependent，不作为主线机制。\n\n### 5e. c3_llama — Cross-Architecture Validation\n\n- Model: DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\n- 8/8 conditions complete (imp + rand × 4 sparsity)\n- Within-importance phase gradient: d_z ≈ 1.0 across all sparsity levels ✓\n- imp_vs_rand d_z: 0.19→0.26→0.29→0.34（仅 s030 Bonferroni p=0.029 显著）\n- Random also shows significant phase gradient (d_z 0.35→0.44, CI excludes zero)\n- Qualitative direction consistent; strategy×phase interaction weaker + architecture-dependent\n\n### 5f. c5b_pilot — Phase-Gated Controller\n\n| Metric | s025 |\n|--------|------|\n| Uniform median II | 1.0435 |\n| Oracle median II | 0.856 |\n| Oracle recovery | 18% (CI [−39, 45.8], p=0.002) |\n| Heuristic median II | 0.713 |\n| Heuristic recovery | 31.7% (CI [−22.8, 66], p=0.024) |\n| Gate criterion | oracle > 30% |\n| Gate result | **FAIL** |\n\nDirection correct (Wilcoxon significant) but effect size insufficient. → §8 Future Work.\n\n---\n\n## 6. Claim–Evidence Mapping\n\n| Claim | Status | Primary Evidence (exp_id) |\n|-------|--------|--------------------------|\n| C1: Strategy- and task-modulated severity | confirmed | c2_n500_deepseek, c2_qw_n500_r3 (imp/rand ratio 15–39× DS, 2.7–20× QW); gsm8k_profiling_ds/qw (ratio 衰减至 2.3–3.8×) |\n| C2: Phase-modulated (low > high) | confirmed | bf16_ds_imp_s015–s030 (0.32→9.94); bf16_qw_imp_s015–s030 (0.048→2.619); n500 confirms all p < 1e-14 |\n| C3: Phase-strategy crossover | confirmed | bf16_importance_s025 (imp low=7.196 > rand low=1.363; imp high=0.032 < rand high=0.818) |\n| C4: Discrimination collapse | partially | c4_entropy (DS: Gini/CV ✓, entropy ✓); qwen_c4_entropy (Gini/CV ✓, entropy ✗ at s025) |\n| C5: Cross-model generalization | confirmed | c2_n500_deepseek + c2_qw_n500_r3: ρ=1.0 both, QW magnitude ~1/4 DS |\n| C5b: Phase-aware mitigation | gate_failed | c5b_pilot: oracle 18% < 30% gate → future work |\n| C6: Sub-exponential growth | confirmed | Δ growth factors: 3.8×→4.8×→2.0× (递减) |\n| C7: n=500 dose-response | confirmed | c2_n500_deepseek (n=496) + c2_qw_n500_r3 (n=475): monotonic, ρ=1.0 |\n| C8: Cross-architecture (LLaMA) | partially | c3_llama: within-imp d_z≈1.0 ✓; imp_vs_rand weak (d_z 0.19–0.34); rand also shows gradient |\n| C10: Cross-benchmark (GSM8K) | confirmed | gsm8k_profiling_ds/qw: monotonic ✓; gsm8k_qw_rand_s025/s030_v2: random 也显著 |\n| S3→C: Model-dependent onset | confirmed | QW s015 n=50 CI crosses zero; n=475 resolves (p=3.5e-14). DS significant from s015+ |\n| S7→C: Dose-response monotonicity | confirmed | Spearman ρ=1.0 both models (n=500), perm p=0.0417 |\n\n---\n\n## 7. Known Caveats\n\n1. **DS accuracy truncation-dominated**: 58–76% truncation even at 8k tokens. All DS accuracy = lower bound (D086).\n2. **QW batch mismatch**: b2_fix experiments used max_new_tokens=8192 vs batch1's 2048. Impact minimal (s020: +1, s025: 0).\n3. **QW s015 n=50 marginal**: bf16 CI [−0.005, 0.110] crosses zero. Resolved at n=475.\n4. **Entropy mechanism model-dependent**: Qwen s025 entropy reversed (+0.045). Paper uses discrimination collapse (Gini/CV) as primary mechanism.\n5. **LLaMA strategy×phase interaction weak**: d_z 0.19–0.34; random also shows phase gradient. Use \"suggests\"/\"partial support\" language.\n6. **GSM8K strategy specificity 衰减**: 2.3–3.8× vs MATH-500 15–36×. Phase gradient robust, magnitude ratio task-dependent.\n7. **c5b pilot gate failed**: Oracle 18% < 30%. CI crosses zero for both oracle and heuristic.\n8. **Bonferroni revision (D066)**: k=4 family-wise (revised from k=48). DS rand s025/s030 restored to significant.\n9. **G× correction**: Paper must update from 58–241× to 21–64×.\n\n---\n\n## 8. Missing / Pending Data\n\n| Item | Status | Impact |\n|------|--------|--------|\n| acc_ds_s015_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| acc_ds_s030_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| QW batch1 v2 rescore (s015/s030/dense) | Not started | Low priority: s020 v2 showed zero change |\n| G× values not in registry | Post-hoc computation | Reference compute_gx_final.py; values in memory.md |\n| GSM8K QW importance full metrics | In gsm8k_profiling_qw | Only summary values (0.039/0.158/1.1/2.092) without CI |"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T00:34:21.365323+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_c8f9bc\", \"name\": \"round10_data_summary\", \"type\": \"report\", \"description\": \"Round 10 完整数据编译：PPL dose curve (n=500), QW/DS accuracy, GSM8K cross-benchmark, sf5/entropy/LLaMA/pilot 补充证据，claim-evidence mapping，caveats 和 pending items\", \"path\": \"projects/phase-gated-compound-sparse/artifacts/_project/report/round10_data_summary.md\", \"url\": null, \"project\": \"phase-gated-compound-sparse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T00:34:10.408266+00:00\", \"tags\": [\"round10\", \"data-compilation\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_round10_data_compilation_20260516T002532",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-16T00:34:21.365530+00:00_

已注册为 artifact `art_20260516_c8f9bc`。

编译完成。核心结论：

**12 claims 中 8 confirmed, 2 partially confirmed, 1 gate_failed (future work), 1 confirmed (running 补充数据)**

关键数字：
- PPL dose curve (n=500): DS 0.39→1.21→3.99→8.48, QW 0.07→0.31→1.07→3.16, 两模型 Spearman ρ=1.0, 全部 imp p<1e-14
- QW accuracy: 0.40→0.36→0.36→0.33→0.19, 断崖在 s025→s030 (−14pp)
- GSM8K: phase gradient 跨 benchmark 复现, 但 strategy specificity 从 15–36× 衰减至 2.3–3.8×

待补：acc_ds_s015_8k_v2 和 acc_ds_s030_8k_v2 仍在运行（DS accuracy 5-point curve 缺 2 点，但已降为定性观察，不阻塞论文）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_round10_data_compilation_20260516T002532"
}
```

</details>

---
