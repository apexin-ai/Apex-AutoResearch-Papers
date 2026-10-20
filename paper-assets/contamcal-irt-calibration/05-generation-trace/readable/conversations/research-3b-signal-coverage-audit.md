# research 3B signal coverage audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 0
- **Tool calls:** 32
- **Original source:** `logs/chats/worker_research_3B_signal_coverage_audit_20260516T101702.jsonl`
- **Structured JSON:** [`4608cab3b52e4f1784be.json`](../../sessions/46/4608cab3b52e4f1784be.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

65 recorded events

### Tool call

_source line 1 · 2026-05-16T10:22:35.444629+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__ssh_read_only",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__ssh_read_only",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T10:22:35.445131+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T10:22:35.445408+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T10:22:35.445643+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T10:22:35.447065+00:00_

Error: result (336,093 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T10:22:35.447404+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight (D039 pivot — Dream 三档验证)\\nBenchmark contamination effects are far more complex than \\\"scores go up.\\\" Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects are benchmark-dependent (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\n\\n## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)\\n\\n1. **Characterization Claim (PRIMARY)**: Contamination effects are benchmark-dependent and scale-dependent. IRT γ_k captures bidirectional effects: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at
…[truncated 10510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T10:22:35.447597+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration/exp003 -type f -name \"*.py\" -o -name \"*.yaml\" -o -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration/exp003 -type f -name \"*.py\" -o -name \"*.yaml\" -o -name \"*.json\""
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T10:22:35.447742+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/exp003/rrf_aggregation.py\\n/root/contamcal-irt-calibration/exp003/ablations.py\\n/root/contamcal-irt-calibration/exp003/evaluate_rrf.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T10:22:35.447892+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Parse 3B registry entries",
  "prompt": "I need you to analyze a large JSON registry file and extract all 3B-related experiments. The file is at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\n\nThe file format is JSON with schema: {result: string} — the \"result\" field contains a JSON string that needs to be parsed again.\n\nI need you to:\n1. First probe the structure (jq type, length, keys)\n2. Extract ALL experiments that contain \"3B\" in their exp_id, title, notes, or config\n3. For each, report: exp_id, status (RUNNING/DONE/FAILED/PENDING), dosage (d000/d005/d025/d100), seed, what type it is (eval/signals/training), and any output paths or metrics\n\nAlso extract all 0.5B and 1.5B signal experiments to check their completion status.\n\nReport in a structured format I can use to build a coverage matrix. Be exhaustive — don't skip any entries.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Agent",
  "tool_args": {
    "description": "Parse 3B registry entries",
    "prompt": "I need you to analyze a large JSON registry file and extract all 3B-related experiments. The file is at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\n\nThe file format is JSON with schema: {result: string} — the \"result\" field contains a JSON string that needs to be parsed again.\n\nI need you to:\n1. First probe the structure (jq type, length, keys)\n2. Extract ALL experiments that contain \"3B\" in their exp_id, title, notes, or config\n3. For each, report: exp_id, status (RUNNING/DONE/FAILED/PENDING), dosage (d000/d005/d025/d100), seed, what type it is (eval/signals/training), and any output paths or metrics\n\nAlso extract all 0.5B and 1.5B signal experiments to check their completion status.\n\nReport in a structured format I can use to build a coverage matrix. Be exhaustive — don't skip any entries.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T10:22:35.448055+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp003/rrf_aggregation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp003/rrf_aggregation.py"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T10:22:35.448180+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "ROADMAP.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "ROADMAP.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T10:22:35.448345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T10:22:35.448535+00:00_

File content (148169 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T10:22:35.448666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T10:22:35.448784+00:00_

File content (148169 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T10:22:35.448906+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 2000 \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"",
  "description": "Peek at first 2000 bytes to understand structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 2000 \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"",
    "description": "Peek at first 2000 bytes to understand structure"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T10:22:35.449039+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_002_signals_3B_d005_a32_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:51:39.086Z\", \"updated_at\": \"2026-05-16T10:11:52.002Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python compute_signals.py --signal all --benchmark {mmlu,gsm8k,arc_challenge}\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"gpu_id\": \"cuda:2\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42\", \"data_count\": 12, \"hypothesis\": \"3B d005 s42 alpha=32 signals (s1_embedding + s2_minkpp + s3 + s4_selfcritique) x (mmlu + gsm8k + arc_challenge). Prerequisite for RRF aggregation. Uses D076-retrained checkpoint.\", \"pid\": 719534, \"log_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/run.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:09:15.071Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:09:17.583Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:09:20.769563+00:00\"}]}, \"notes\": \"Cron false positive: signals pipeline不用W&B, cron检测不到metrics误判为failed. 实际已全部完成: s1+s2+s4 × mmlu+gsm8k+arc_challenge, 输出merged json在 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/. GPU cuda:2 已释放.\"}, \"exp_002_signals_15B_d100_s123_cuda2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:07:31.281Z\", \"updated_at\": \"2026-05-16T10:07:38.375Z\", \"spec\": {\"command\": \"bash run_15B_d100_s123_cuda2.sh (CUDA_VISIBLE_DEVICES=2, 3 benchmarks × 3 signals)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": \"746777\", \"data_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d100_s123/\", \"data_count\": 9, \"model_name\": \"Qwen2.5-1.5B_d100_s

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T10:22:35.449192+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\n# Extract the inner JSON and get experiment keys\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint('---ALL KEYS---')\nfor k in sorted(exps.keys()):\n    print(k)\n\"",
  "description": "Parse JSON structure and list all experiment keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\n# Extract the inner JSON and get experiment keys\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint('---ALL KEYS---')\nfor k in sorted(exps.keys()):\n    print(k)\n\"",
    "description": "Parse JSON structure and list all experiment keys"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T10:22:35.449355+00:00_

Total experiments: 214
---ALL KEYS---
exp002-signal-d025-05B
exp002-signals-1p5B
exp006-gsm8k-d024-delta
exp006-oracle-arc-2pl
exp006-oracle-arc-4pl-pooled
exp006-oracle-gsm8k-extended
exp006-oracle-gsm8k-extended-v2
exp006-pooled-05B-15B-arc-v2
exp006-pooled-05B-15B-gsm8k-v2
exp006-pooled-05B-15B-mmlu-v2
exp006-pooled-s1only-arc
exp006-pooled-s1only-gsm8k
exp006-pooled-s1only-gsm8k-v2
exp006-s1only-gsm8k-2pl
exp006_pooled_rrf_irt_05b_15b
exp006_pooled_rrf_irt_05b_15b_v2
exp_001_eval_05B_aligned_batch
exp_001_eval_05B_d000_s123
exp_001_eval_05B_d000_s123_aligned
exp_001_eval_05B_d000_s42
exp_001_eval_05B_d000_s42_v2
exp_001_eval_05B_d000_s42_v3
exp_001_eval_05B_d000_s42_v4
exp_001_eval_05B_d000_s42_v5
exp_001_eval_05B_d000_s42_v6
exp_001_eval_05B_d000_s42_v7
exp_001_eval_05B_d005
exp_001_eval_05B_d005_aligned
exp_001_eval_05B_d005_para_aligned
exp_001_eval_05B_d005_s123_aligned
exp_001_eval_05B_d005_s123_para_aligned
exp_001_eval_05B_d025_aligned
exp_001_eval_05B_d025_aligned_v2
exp_001_eval_05B_d025_s123_aligned
exp_001_eval_05B_d100
exp_001_eval_05B_d100_aligned
exp_001_eval_05B_d100_aligned_v2
exp_001_eval_05B_d100_aligned_v3
exp_001_eval_05B_d100_aligned_v4
exp_001_eval_05B_d100_s123_aligned
exp_001_eval_05B_d100_v2
exp_001_eval_05B_d100_v3
exp_001_eval_05B_d100_v4
exp_001_eval_05B_d100_v5
exp_001_eval_05B_d100_v6
exp_001_eval_05B_raw
exp_001_eval_15B_aligned_batch
exp_001_eval_15B_d000_s123
exp_001_eval_15B_d000_s123_aligned
exp_001_eval_15B_d000_s42
exp_001_eval_15B_d000_s42_v2
exp_001_eval_15B_d005_aligned_v2
exp_001_eval_15B_d005_s123
exp_001_eval_15B_d005_s123_v2
exp_001_eval_15B_d025_aligned
exp_001_eval_15B_d025_para_aligned
exp_001_eval_15B_d025_s123
exp_001_eval_15B_d025_s123_v2
exp_001_eval_15B_d100_aligned
exp_001_eval_15B_d100_s123_aligned
exp_001_eval_15B_d100_s42
exp_001_eval_15B_s123_para_aligned_batch
exp_001_eval_3B_d000_aligned
exp_001_eval_3B_d000_s123
exp_001_eval_3B_d000_s123_aligned
exp_001_eval_3B_d000_s42
exp_001_eval_3B_d000_s42_a32_alig
…[truncated 4046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T10:22:35.449514+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Extract all 3B experiments\nkeys_3b = [k for k in exps.keys() if '3B' in k or '3b' in k]\nprint(f'=== 3B EXPERIMENTS ({len(keys_3b)} total) ===')\nprint()\n\nfor k in sorted(keys_3b):\n    e = exps[k]\n    status = e.get('status', 'UNKNOWN')\n    spec = e.get('spec', {})\n    notes = e.get('notes', '')\n    conclusion = e.get('conclusion', '')\n    failure = e.get('failure_reason', '')\n    \n    # Determine type\n    if 'sft' in k or 'train' in k.lower():\n        etype = 'training'\n    elif 'signal' in k.lower():\n        etype = 'signals'\n    elif 'eval' in k:\n        etype = 'eval'\n    elif 'irt' in k or 'rrf' in k or 'pooled' in k:\n        etype = 'analysis'\n    else:\n        etype = 'other'\n    \n    # Determine dosage\n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(spec):\n            dosage = d\n            break\n    \n    # Determine seed\n    seed = 'unknown'\n    if 's42' in k:\n        seed = '42'\n    elif 's123' in k:\n        seed = '123'\n    elif spec.get('seed'):\n        seed = str(spec['seed'])\n    \n    # Output paths\n    data_path = spec.get('data_path', '')\n    log_path = spec.get('log_path', '')\n    \n    print(f'--- {k} ---')\n    print(f'  status: {status} | type: {etype} | dosage: {dosage} | seed: {seed}')\n    print(f'  conclusion: {conclusion}')\n    if failure:\n        print(f'  failure_reason: {failure}')\n    if data_path:\n        print(f'  data_path: {data_path}')\n    if log_path:\n        print(f'  log_path: {log_path}')\n    if notes:\n        print(f'  notes: {notes[:200]}')\n    print()\n\" 2>&1 | head -500",
  "description": "Extract all 3B experiments with details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Extract all 3B experiments\nkeys_3b = [k for k in exps.keys() if '3B' in k or '3b' in k]\nprint(f'=== 3B EXPERIMENTS ({len(keys_3b)} total) ===')\nprint()\n\nfor k in sorted(keys_3b):\n    e = exps[k]\n    status = e.get('status', 'UNKNOWN')\n    spec = e.get('spec', {})\n    notes = e.get('notes', '')\n    conclusion = e.get('conclusion', '')\n    failure = e.get('failure_reason', '')\n    \n    # Determine type\n    if 'sft' in k or 'train' in k.lower():\n        etype = 'training'\n    elif 'signal' in k.lower():\n        etype = 'signals'\n    elif 'eval' in k:\n        etype = 'eval'\n    elif 'irt' in k or 'rrf' in k or 'pooled' in k:\n        etype = 'analysis'\n    else:\n        etype = 'other'\n    \n    # Determine dosage\n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(spec):\n            dosage = d\n            break\n    \n    # Determine seed\n    seed = 'unknown'\n    if 's42' in k:\n        seed = '42'\n    elif 's123' in k:\n        seed = '123'\n    elif spec.get('seed'):\n        seed = str(spec['seed'])\n    \n    # Output paths\n    data_path = spec.get('data_path', '')\n    log_path = spec.get('log_path', '')\n    \n    print(f'--- {k} ---')\n    print(f'  status: {status} | type: {etype} | dosage: {dosage} | seed: {seed}')\n    print(f'  conclusion: {conclusion}')\n    if failure:\n        print(f'  failure_reason: {failure}')\n    if data_path:\n        print(f'  data_path: {data_path}')\n    if log_path:\n        print(f'  log_path: {log_path}')\n    if notes:\n        print(f'  notes: {notes[:200]}')\n    print()\n\" 2>&1 | head -500",
    "description": "Extract all 3B experiments with details"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T10:22:35.449718+00:00_

=== 3B EXPERIMENTS (86 total) ===

--- exp_001_eval_3B_d000_aligned ---
  status: DONE | type: eval | dosage: d000 | seed: unknown
  conclusion: success
  log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_aligned.log
  notes: D018 决策：3B GSM8K 标记为 "SFT-degraded, excluded from dose-response"。3B MMLU/ARC 仍可用。不重训 LoRA 配置。诊断根因：LoRA SFT (r=16, alpha=32, lr=2e-4, 7 proj) 导致 CoT 灾难性遗忘。

--- exp_001_eval_3B_d000_s123 ---
  status: DONE | type: eval | dosage: d000 | seed: 123
  conclusion: success
  data_path: mmlu,gsm8k,arc_challenge,humaneval
  log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s123.log

--- exp_001_eval_3B_d000_s123_aligned ---
  status: DONE | type: eval | dosage: d000 | seed: 123
  conclusion: success
  data_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter
  log_path: /tmp/eval_3B_d000_s123_aligned.log
  notes: Cron false positive: process exited normally after completing all 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval). Sentinel .done written. Cron missed sentinel because eval experiments don't log 

--- exp_001_eval_3B_d000_s42 ---
  status: DONE | type: eval | dosage: d000 | seed: 42
  conclusion: success
  failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
  data_path: mmlu,gsm8k,arc_challenge,humaneval
  log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42.log
  notes: v1 failed (--gpu bug), v2 resubmitted with CUDA_VISIBLE_DEVICES. PID 249294 confirmed running on GPU 1 (cron monitored).

--- exp_001_eval_3B_d000_s42_a32_aligned ---
  status: PREPARING | type: eval | dosage: d000 | seed: 42
  conclusion: 

--- exp_001_eval_3B_d000_s42_a32_batch ---
  status: DONE | type: eval | dosage: d000 | seed: 42
  conclusion: success
  data_path: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_a32_aligned
  log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_a32_batch.log

--- exp_001_eval_3B_d000_s42_a32_para_aligned ---
  status: 
…[truncated 23674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T10:22:35.449888+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Continue 3B signals\nkeys_3b_signals_cont = [k for k in sorted(exps.keys()) if '3B' in k and k >= 'exp_002_signals_3B_v5']\nfor k in keys_3b_signals_cont:\n    e = exps[k]\n    status = e.get('status', 'UNKNOWN')\n    spec = e.get('spec', {})\n    notes = e.get('notes', '')\n    conclusion = e.get('conclusion', '')\n    failure = e.get('failure_reason', '')\n    \n    # Determine type\n    if 'sft' in k or 'train' in k.lower():\n        etype = 'training'\n    elif 'signal' in k.lower():\n        etype = 'signals'\n    elif 'eval' in k:\n        etype = 'eval'\n    elif 'irt' in k or 'rrf' in k or 'pooled' in k:\n        etype = 'analysis'\n    else:\n        etype = 'other'\n    \n    # Determine dosage\n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(spec):\n            dosage = d\n            break\n    \n    # Determine seed\n    seed = 'unknown'\n    if 's42' in k:\n        seed = '42'\n    elif 's123' in k:\n        seed = '123'\n    elif spec.get('seed'):\n        seed = str(spec['seed'])\n    \n    # Output paths\n    data_path = spec.get('data_path', '')\n    log_path = spec.get('log_path', '')\n    \n    print(f'--- {k} ---')\n    print(f'  status: {status} | type: {etype} | dosage: {dosage} | seed: {seed}')\n    print(f'  conclusion: {conclusion}')\n    if failure:\n        print(f'  failure_reason: {failure}')\n    if data_path:\n        print(f'  data_path: {data_path}')\n    if log_path:\n        print(f'  log_path: {log_path}')\n    if notes:\n        print(f'  notes: {notes[:200]}')\n    print()\n\" 2>&1",
  "description": "Get remaining 3B signal experiments (v5+)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Continue 3B signals\nkeys_3b_signals_cont = [k for k in sorted(exps.keys()) if '3B' in k and k >= 'exp_002_signals_3B_v5']\nfor k in keys_3b_signals_cont:\n    e = exps[k]\n    status = e.get('status', 'UNKNOWN')\n    spec = e.get('spec', {})\n    notes = e.get('notes', '')\n    conclusion = e.get('conclusion', '')\n    failure = e.get('failure_reason', '')\n    \n    # Determine type\n    if 'sft' in k or 'train' in k.lower():\n        etype = 'training'\n    elif 'signal' in k.lower():\n        etype = 'signals'\n    elif 'eval' in k:\n        etype = 'eval'\n    elif 'irt' in k or 'rrf' in k or 'pooled' in k:\n        etype = 'analysis'\n    else:\n        etype = 'other'\n    \n    # Determine dosage\n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(spec):\n            dosage = d\n            break\n    \n    # Determine seed\n    seed = 'unknown'\n    if 's42' in k:\n        seed = '42'\n    elif 's123' in k:\n        seed = '123'\n    elif spec.get('seed'):\n        seed = str(spec['seed'])\n    \n    # Output paths\n    data_path = spec.get('data_path', '')\n    log_path = spec.get('log_path', '')\n    \n    print(f'--- {k} ---')\n    print(f'  status: {status} | type: {etype} | dosage: {dosage} | seed: {seed}')\n    print(f'  conclusion: {conclusion}')\n    if failure:\n        print(f'  failure_reason: {failure}')\n    if data_path:\n        print(f'  data_path: {data_path}')\n    if log_path:\n        print(f'  log_path: {log_path}')\n    if notes:\n        print(f'  notes: {notes[:200]}')\n    print()\n\" 2>&1",
    "description": "Get remaining 3B signal experiments (v5+)"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T10:22:35.450036+00:00_

--- exp_002_signals_3B_v5 ---
  status: DONE | type: signals | dosage: d025 | seed: unknown
  conclusion: failed
  failure_reason: EXIT_CODE=129 (non-zero)
  data_path: /root/autodl-tmp/exp002/signals/
  log_path: ~/runs/contamcal-irt-calibration/exp_002_signals_3B_v5.log
  notes: 失败原因: EXIT_CODE=129 (SIGHUP), 实际是 d100_s42/mmlu selfcritique 在 22% 处被 SIGTERM (D078/D079 orphan 清理). 3/4 batch tasks 完成 (d025_s42/mmlu PASS, d100_s42/gsm8k PASS, d100_s42/arc_challenge PASS). 已有成果: d0

--- exp_002_signals_3B_v6 ---
  status: DONE | type: signals | dosage: d000 | seed: 42
  conclusion: failed
  data_path: mmlu/gsm8k/arc_challenge benchmarks
  log_path: /root/runs/contamcal-irt-calibration/exp_002_signals_3B_v6.log
  notes: s1_embedding and s2_minkpp completed for all 3 benchmarks (mmlu: 14042, gsm8k: 1319, arc_challenge: 1172). s3_constat crashed on all benchmarks with ValueError: Item count mismatch (expected 1172, got

--- exp_002_signals_3B_v7 ---
  status: DONE | type: signals | dosage: d000 | seed: unknown
  conclusion: success
  log_path: ~/runs/contamcal-irt-calibration/exp_002_signals_3B_v7.log

--- exp_002_signals_3B_v8 ---
  status: DONE | type: signals | dosage: d000 | seed: [123]
  conclusion: failed
  failure_reason: OOM Killed during s4_selfcritique mmlu (7021 items, ~1.3s/it). selfcritique on mmlu too memory-intensive when combined with model inference.
  data_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_{d025_s123,d100_a32_s123}/lora_adapter
  log_path: ~/runs/contamcal-irt-calibration/exp_002_signals_3B_v8.log
  notes: Process Killed (OOM) during s4_selfcritique mmlu. Partial completion: d025_s123 gsm8k+arc_challenge complete (s1,s2,s4,merged); d025_s123 mmlu has s1+s2 only (s4 killed at 388/7021); d100_a32_s123 mml

--- exp_002_signals_3B_v8_recovery ---
  status: DONE | type: signals | dosage: d000 | seed: 123
  conclusion: failed
  data_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter
  log_path: /root/autodl-tmp/ex
…[truncated 650 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T10:22:35.450193+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Extract 0.5B and 1.5B signal experiments\nkeys_signal = [k for k in sorted(exps.keys()) if ('signal' in k.lower() or 'Signal' in k) and ('05B' in k or '15B' in k or '0.5B' in k or '1.5B' in k or '1p5B' in k)]\nprint(f'=== 0.5B/1.5B SIGNAL EXPERIMENTS ({len(keys_signal)} total) ===')\nprint()\n\nfor k in sorted(keys_signal):\n    e = exps[k]\n    status = e.get('status', 'UNKNOWN')\n    spec = e.get('spec', {})\n    notes = e.get('notes', '')\n    conclusion = e.get('conclusion', '')\n    failure = e.get('failure_reason', '')\n    \n    # Determine model size\n    if '05B' in k or '0.5B' in k:\n        model = '0.5B'\n    elif '15B' in k or '1.5B' in k or '1p5B' in k:\n        model = '1.5B'\n    else:\n        model = 'unknown'\n    \n    # Determine dosage\n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(spec):\n            dosage = d\n            break\n    \n    # Determine seed\n    seed = 'unknown'\n    if 's42' in k:\n        seed = '42'\n    elif 's123' in k:\n        seed = '123'\n    elif spec.get('seed'):\n        seed = str(spec['seed'])\n    \n    # Output paths\n    data_path = spec.get('data_path', '')\n    log_path = spec.get('log_path', '')\n    \n    print(f'--- {k} ---')\n    print(f'  model: {model} | status: {status} | dosage: {dosage} | seed: {seed}')\n    print(f'  conclusion: {conclusion}')\n    if failure:\n        print(f'  failure_reason: {failure[:150]}')\n    if data_path:\n        print(f'  data_path: {data_path}')\n    if log_path:\n        print(f'  log_path: {log_path}')\n    if notes:\n        print(f'  notes: {notes[:250]}')\n    print()\n\"",
  "description": "Extract 0.5B and 1.5B signal experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Extract 0.5B and 1.5B signal experiments\nkeys_signal = [k for k in sorted(exps.keys()) if ('signal' in k.lower() or 'Signal' in k) and ('05B' in k or '15B' in k or '0.5B' in k or '1.5B' in k or '1p5B' in k)]\nprint(f'=== 0.5B/1.5B SIGNAL EXPERIMENTS ({len(keys_signal)} total) ===')\nprint()\n\nfor k in sorted(keys_signal):\n    e = exps[k]\n    status = e.get('status', 'UNKNOWN')\n    spec = e.get('spec', {})\n    notes = e.get('notes', '')\n    conclusion = e.get('conclusion', '')\n    failure = e.get('failure_reason', '')\n    \n    # Determine model size\n    if '05B' in k or '0.5B' in k:\n        model = '0.5B'\n    elif '15B' in k or '1.5B' in k or '1p5B' in k:\n        model = '1.5B'\n    else:\n        model = 'unknown'\n    \n    # Determine dosage\n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(spec):\n            dosage = d\n            break\n    \n    # Determine seed\n    seed = 'unknown'\n    if 's42' in k:\n        seed = '42'\n    elif 's123' in k:\n        seed = '123'\n    elif spec.get('seed'):\n        seed = str(spec['seed'])\n    \n    # Output paths\n    data_path = spec.get('data_path', '')\n    log_path = spec.get('log_path', '')\n    \n    print(f'--- {k} ---')\n    print(f'  model: {model} | status: {status} | dosage: {dosage} | seed: {seed}')\n    print(f'  conclusion: {conclusion}')\n    if failure:\n        print(f'  failure_reason: {failure[:150]}')\n    if data_path:\n        print(f'  data_path: {data_path}')\n    if log_path:\n        print(f'  log_path: {log_path}')\n    if notes:\n        print(f'  notes: {notes[:250]}')\n    print()\n\"",
    "description": "Extract 0.5B and 1.5B signal experiments"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T10:22:35.450360+00:00_

=== 0.5B/1.5B SIGNAL EXPERIMENTS (7 total) ===

--- exp002-signal-d025-05B ---
  model: 0.5B | status: DONE | dosage: d025 | seed: 42
  conclusion: success
  data_path: /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl
  log_path: ~/runs/contamcal-irt-calibration/exp002-signal-d025-05B.log
  notes: 0.5B d025 signals 3/3 passed (embedding, minkpp, selfcritique × mmlu, gsm8k, arc_challenge). 13 files total including merged signals.

--- exp002-signals-1p5B ---
  model: 1.5B | status: DONE | dosage: unknown | seed: unknown
  conclusion: success
  notes: 1.5B signals 12/12 complete (d000/d005/d025/d100 × s1_embedding/s2_minkpp/s4_selfcritique). All PASS. GPU 0 released.

--- exp_002_signals_05B ---
  model: 0.5B | status: DONE | dosage: unknown | seed: 42
  conclusion: success
  data_path: /root/autodl-tmp/exp001/eval_results/ + /root/autodl-tmp/exp001/checkpoints/
  log_path: ~/runs/contamcal-irt-calibration/exp_002_signals_05B.log
  notes: v5 完成 9/9 PASS。d000/d005/d100 × mmlu/gsm8k/arc_challenge 全部完成。9 个 signals_merged 文件已产出。三项修复奏效: timeout 4h, per-signal cache, max_tokens 64。GPU 0 已释放。

--- exp_002_signals_05B_s123_batch ---
  model: 0.5B | status: DONE | dosage: unknown | seed: 123
  conclusion: failed
  failure_reason: 脚本 /root/contamcal-irt-calibration/exp002/run_05B_s123_signals.sh 不存在（EXIT_CODE=127, command not found）。目录下只有 run_signals_05B.sh，无 run_05B_s123_signal
  data_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d{000,005,025,100}_s123
  log_path: ~/runs/contamcal-irt-calibration/exp_002_signals_05B_s123_batch.log

--- exp_002_signals_05B_s123_v2 ---
  model: 0.5B | status: RUNNING | dosage: d000 | seed: 123
  conclusion: 
  data_path: /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s123
  log_path: /root/autodl-tmp/exp002/signals/signals_05B_s123_v2.log

--- exp_002_signals_15B_d100_s123_cuda2 ---
  model: 1.5B | status: RUNNING | dosage: d100 | seed: 123
  conclusion: 
  data_path: /root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d100_s123/
  lo
…[truncated 336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T10:22:35.450527+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Find entries NOT containing 3B in key but containing 3B in spec/notes\nkeys_3b_in_name = set(k for k in exps.keys() if '3B' in k or '3b' in k)\nextra_3b = []\nfor k, e in exps.items():\n    if k in keys_3b_in_name:\n        continue\n    full_text = json.dumps(e)\n    if '3B' in full_text or 'Qwen2.5-3B' in full_text:\n        extra_3b.append(k)\n\nif extra_3b:\n    print(f'=== Entries referencing 3B but not in key name ({len(extra_3b)}) ===')\n    for k in sorted(extra_3b):\n        e = exps[k]\n        status = e.get('status','?')\n        conclusion = e.get('conclusion','')\n        notes = e.get('notes','')[:150]\n        print(f'  {k}: status={status}, conclusion={conclusion}')\n        if notes:\n            print(f'    notes: {notes}')\nelse:\n    print('No additional 3B references found outside named keys.')\n\"",
  "description": "Find 3B references in experiments not named with 3B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Find entries NOT containing 3B in key but containing 3B in spec/notes\nkeys_3b_in_name = set(k for k in exps.keys() if '3B' in k or '3b' in k)\nextra_3b = []\nfor k, e in exps.items():\n    if k in keys_3b_in_name:\n        continue\n    full_text = json.dumps(e)\n    if '3B' in full_text or 'Qwen2.5-3B' in full_text:\n        extra_3b.append(k)\n\nif extra_3b:\n    print(f'=== Entries referencing 3B but not in key name ({len(extra_3b)}) ===')\n    for k in sorted(extra_3b):\n        e = exps[k]\n        status = e.get('status','?')\n        conclusion = e.get('conclusion','')\n        notes = e.get('notes','')[:150]\n        print(f'  {k}: status={status}, conclusion={conclusion}')\n        if notes:\n            print(f'    notes: {notes}')\nelse:\n    print('No additional 3B references found outside named keys.')\n\"",
    "description": "Find 3B references in experiments not named with 3B"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T10:22:35.450664+00:00_

=== Entries referencing 3B but not in key name (10) ===
  exp006-pooled-05B-15B-arc-v2: status=DONE, conclusion=success
  exp006-pooled-05B-15B-gsm8k-v2: status=DONE, conclusion=negative
    notes: INCONCLUSIVE (Reviewer WARNING): MCMC convergence failed — rhat=1.015, ess=330, gamma CI crosses zero. 等待 exp006-oracle-gsm8k-extended / exp006-pooled
  exp006-pooled-05B-15B-mmlu-v2: status=DONE, conclusion=failed
  exp_001_sft_0pct: status=DONE, conclusion=success
    notes: Parent entry for 3 sub-experiments (05B/15B/3B). All confirmed running.
  exp_001_sft_d005_05B: status=DONE, conclusion=killed
    notes: v1 OOM at step 8/3177 — GPU 5 有残留进程 PID 234755 占 6.8GB。PID 236994 (submit_training_job 重提交) 也使用了 --gpu 0，实际跑到 GPU 0 而非 GPU 5，同样 OOM。根因：--gpu 0 导致 CUDA
  exp_001_sft_d005_15B: status=DONE, conclusion=success
    notes: 训练实际已完成。3177/3177 steps, train_loss=1.2637, mean_token_accuracy=0.7308, epoch=1.0。LoRA adapter 已保存。EXIT_CODE=129 (SIGHUP) 发生在 Training complete 之后，属于 
  exp_001_sft_injection: status=DONE, conclusion=success
    notes: MMLU paraphrase 3-attempt QC 重试流程: Attempt 1 ✅ (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 进行中 (v2重启, 439 batches total, 进度~22%). Attem
  exp_003_mmlu_item_aligned_gap: status=DONE, conclusion=success
    notes: (a) para > aligned is a systematic artifact (paraphrase versions are inherently easier), not a contamination signal — mean gap is -2.24pp across all 2
  exp_006_irt_05B: status=DONE, conclusion=killed
    notes: KILLED by Director 指令: 混合 scale (0.5B+1.5B+3B) + legacy 格式 + 多余 seed 的错误数据在拟合。Stan NUTS 4 chains (PID 386298-386301) 运行 ~30min 后终止。代码修复中: 正则改为 _d(\d+)
  exp_006_pooled_gsm8k_v1: status=DONE, conclusion=failed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T10:22:35.450830+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Now let's build the structured summary for 3B\n# First: categorize the definitive/latest successful experiments by type x dosage x seed\n\nprint('=' * 80)\nprint('3B COVERAGE MATRIX — TRAINING (SFT)')\nprint('=' * 80)\nprint()\nprint('Key: [OK]=DONE+success, [FAIL]=DONE+failed, [RUN]=RUNNING, [PREP]=PREPARING, [KILL]=killed')\nprint()\n\n# Training matrix\ntrain_3b = {}\nfor k in sorted(exps.keys()):\n    if '3B' not in k:\n        continue\n    if 'sft' not in k and 'train' not in k.lower():\n        continue\n    e = exps[k]\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    \n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(e.get('spec',{})):\n            dosage = d\n            break\n    \n    seed = 'unknown'\n    if 's42' in k: seed = '42'\n    elif 's123' in k: seed = '123'\n    elif e.get('spec',{}).get('seed'): seed = str(e['spec']['seed'])\n    \n    # mark status\n    if conclusion == 'success':\n        mark = 'OK'\n    elif conclusion == 'failed':\n        mark = 'FAIL'\n    elif conclusion == 'killed':\n        mark = 'KILL'\n    elif status == 'RUNNING':\n        mark = 'RUN'\n    elif status == 'PREPARING':\n        mark = 'PREP'\n    else:\n        mark = f'{status}/{conclusion}'\n    \n    key = (dosage, seed)\n    if key not in train_3b:\n        train_3b[key] = []\n    train_3b[key].append((k, mark))\n\nfor (dosage, seed), entries in sorted(train_3b.items()):\n    print(f'  {dosage} / seed={seed}:')\n    for name, mark in entries:\n        print(f'    [{mark}] {name}')\n    print()\n\nprint()\nprint('=' * 80)\nprint('3B COVERAGE MATRIX — EVAL')\nprint('=' * 80)\nprint()\n\neval_3b = {}\nfor k in sorted(exps.keys()):\n    if '3B' not in k:\n        continue\n    if 'eval' not in k:\n        continue\n    e = exps[k]\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    \n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(e.get('spec',{})):\n            dosage = d\n            break\n    \n    seed = 'unknown'\n    if 's42' in k: seed = '42'\n    elif 's123' in k: seed = '123'\n    elif e.get('spec',{}).get('seed'): seed = str(e['spec']['seed'])\n    \n    if conclusion == 'success': mark = 'OK'\n    elif conclusion == 'failed': mark = 'FAIL'\n    elif conclusion == 'killed': mark = 'KILL'\n    elif status == 'RUNNING': mark = 'RUN'\n    elif status == 'PREPARING': mark = 'PREP'\n    else: mark = f'{status}/{conclusion}'\n    \n    key = (dosage, seed)\n    if key not in eval_3b:\n        eval_3b[key] = []\n    eval_3b[key].append((k, mark))\n\nfor (dosage, seed), entries in sorted(eval_3b.items()):\n    print(f'  {dosage} / seed={seed}:')\n    for name, mark in entries:\n        print(f'    [{mark}] {name}')\n    print()\n\nprint()\nprint('=' * 80)\nprint('3B COVERAGE MATRIX — SIGNALS')\nprint('=' * 80)\nprint()\n\nsig_3b = {}\nfor k in sorted(exps.keys()):\n    if '3B' not in k:\n        continue\n    if 'signal' not in k.lower():\n        continue\n    e = exps[k]\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    \n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(e.get('spec',{})):\n            dosage = d\n            break\n    \n    seed = 'unknown'\n    if 's42' in k: seed = '42'\n    elif 's123' in k: seed = '123'\n    elif e.get('spec',{}).get('seed'): seed = str(e['spec']['seed'])\n    \n    if conclusion == 'success': mark = 'OK'\n    elif conclusion == 'failed': mark = 'FAIL'\n    elif conclusion == 'killed': mark = 'KILL'\n    elif status == 'RUNNING': mark = 'RUN'\n    elif status == 'PREPARING': mark = 'PREP'\n    else: mark = f'{status}/{conclusion}'\n    \n    key = (dosage, seed)\n    if key not in sig_3b:\n        sig_3b[key] = []\n    sig_3b[key].append((k, mark))\n\nfor (dosage, seed), entries in sorted(sig_3b.items()):\n    print(f'  {dosage} / seed={seed}:')\n    for name, mark in entries:\n        print(f'    [{mark}] {name}')\n    print()\n\"",
  "description": "Build structured coverage matrix for 3B experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Now let's build the structured summary for 3B\n# First: categorize the definitive/latest successful experiments by type x dosage x seed\n\nprint('=' * 80)\nprint('3B COVERAGE MATRIX — TRAINING (SFT)')\nprint('=' * 80)\nprint()\nprint('Key: [OK]=DONE+success, [FAIL]=DONE+failed, [RUN]=RUNNING, [PREP]=PREPARING, [KILL]=killed')\nprint()\n\n# Training matrix\ntrain_3b = {}\nfor k in sorted(exps.keys()):\n    if '3B' not in k:\n        continue\n    if 'sft' not in k and 'train' not in k.lower():\n        continue\n    e = exps[k]\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    \n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(e.get('spec',{})):\n            dosage = d\n            break\n    \n    seed = 'unknown'\n    if 's42' in k: seed = '42'\n    elif 's123' in k: seed = '123'\n    elif e.get('spec',{}).get('seed'): seed = str(e['spec']['seed'])\n    \n    # mark status\n    if conclusion == 'success':\n        mark = 'OK'\n    elif conclusion == 'failed':\n        mark = 'FAIL'\n    elif conclusion == 'killed':\n        mark = 'KILL'\n    elif status == 'RUNNING':\n        mark = 'RUN'\n    elif status == 'PREPARING':\n        mark = 'PREP'\n    else:\n        mark = f'{status}/{conclusion}'\n    \n    key = (dosage, seed)\n    if key not in train_3b:\n        train_3b[key] = []\n    train_3b[key].append((k, mark))\n\nfor (dosage, seed), entries in sorted(train_3b.items()):\n    print(f'  {dosage} / seed={seed}:')\n    for name, mark in entries:\n        print(f'    [{mark}] {name}')\n    print()\n\nprint()\nprint('=' * 80)\nprint('3B COVERAGE MATRIX — EVAL')\nprint('=' * 80)\nprint()\n\neval_3b = {}\nfor k in sorted(exps.keys()):\n    if '3B' not in k:\n        continue\n    if 'eval' not in k:\n        continue\n    e = exps[k]\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    \n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(e.get('spec',{})):\n            dosage = d\n            break\n    \n    seed = 'unknown'\n    if 's42' in k: seed = '42'\n    elif 's123' in k: seed = '123'\n    elif e.get('spec',{}).get('seed'): seed = str(e['spec']['seed'])\n    \n    if conclusion == 'success': mark = 'OK'\n    elif conclusion == 'failed': mark = 'FAIL'\n    elif conclusion == 'killed': mark = 'KILL'\n    elif status == 'RUNNING': mark = 'RUN'\n    elif status == 'PREPARING': mark = 'PREP'\n    else: mark = f'{status}/{conclusion}'\n    \n    key = (dosage, seed)\n    if key not in eval_3b:\n        eval_3b[key] = []\n    eval_3b[key].append((k, mark))\n\nfor (dosage, seed), entries in sorted(eval_3b.items()):\n    print(f'  {dosage} / seed={seed}:')\n    for name, mark in entries:\n        print(f'    [{mark}] {name}')\n    print()\n\nprint()\nprint('=' * 80)\nprint('3B COVERAGE MATRIX — SIGNALS')\nprint('=' * 80)\nprint()\n\nsig_3b = {}\nfor k in sorted(exps.keys()):\n    if '3B' not in k:\n        continue\n    if 'signal' not in k.lower():\n        continue\n    e = exps[k]\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    \n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(e.get('spec',{})):\n            dosage = d\n            break\n    \n    seed = 'unknown'\n    if 's42' in k: seed = '42'\n    elif 's123' in k: seed = '123'\n    elif e.get('spec',{}).get('seed'): seed = str(e['spec']['seed'])\n    \n    if conclusion == 'success': mark = 'OK'\n    elif conclusion == 'failed': mark = 'FAIL'\n    elif conclusion == 'killed': mark = 'KILL'\n    elif status == 'RUNNING': mark = 'RUN'\n    elif status == 'PREPARING': mark = 'PREP'\n    else: mark = f'{status}/{conclusion}'\n    \n    key = (dosage, seed)\n    if key not in sig_3b:\n        sig_3b[key] = []\n    sig_3b[key].append((k, mark))\n\nfor (dosage, seed), entries in sorted(sig_3b.items()):\n    print(f'  {dosage} / seed={seed}:')\n    for name, mark in entries:\n        print(f'    [{mark}] {name}')\n    print()\n\"",
    "description": "Build structured coverage matrix for 3B experiments"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T10:22:35.451020+00:00_

================================================================================
3B COVERAGE MATRIX — TRAINING (SFT)
================================================================================

Key: [OK]=DONE+success, [FAIL]=DONE+failed, [RUN]=RUNNING, [PREP]=PREPARING, [KILL]=killed

  d000 / seed=123:
    [OK] exp_001_sft_0pct_3B_s123
    [OK] exp_001_sft_3B_d000_s123

  d000 / seed=42:
    [PREP] exp_001_sft_3B_d000_s42
    [OK] exp_001_sft_3B_d000_s42_a32
    [OK] exp_001_sft_3B_d000_v2
    [FAIL] exp_001_sft_3B_d000_v3

  d000 / seed=unknown:
    [OK] exp_001_sft_0pct_3B
    [PREP] exp_001_sft_3B_d000_v4

  d005 / seed=123:
    [OK] exp_001_sft_3B_d005_s123

  d005 / seed=42:
    [OK] exp_001_sft_3B_d005_s42_a32
    [OK] exp_001_sft_d005_3B

  d025 / seed=123:
    [OK] exp_001_sft_3B_d025_s123
    [KILL] exp_001_sft_3B_d100_s123_a32

  d025 / seed=42:
    [KILL] exp_001_sft_3B_d025_s42_a32
    [FAIL] exp_001_sft_3B_d025_s42_a32_v2
    [KILL] exp_001_sft_3B_d025_s42_a32_v3
    [FAIL] exp_001_sft_d025_3B
    [OK] exp_001_sft_d025_3B_v2
    [OK] exp_001_sft_d025_3B_v3

  d100 / seed=123:
    [OK] exp_001_sft_3B_d100_s123
    [OK] exp_001_sft_3B_d100_s123_a32_v2

  d100 / seed=42:
    [KILL] exp_001_sft_3B_d100_s42_a32
    [FAIL] exp_001_sft_3B_d100_s42_a32_v2
    [OK] exp_001_sft_3B_d100_s42_a32_v3
    [OK] exp_001_sft_d100_3B_v2

  d100 / seed=unknown:
    [OK] exp_001_sft_d100_3B


================================================================================
3B COVERAGE MATRIX — EVAL
================================================================================

  d000 / seed=123:
    [OK] exp_001_eval_3B_d000_s123
    [OK] exp_001_eval_3B_d000_s123_aligned
    [OK] exp_001_eval_3B_d000_v2_s123_aligned
    [OK] exp_001_eval_3B_d000_v2_s123_para_aligned

  d000 / seed=42:
    [OK] exp_001_eval_3B_d000_s42
    [PREP] exp_001_eval_3B_d000_s42_a32_aligned
    [OK] exp_001_eval_3B_d000_s42_a32_batch
    [OK] exp_001_eval_3B_d000_s42_a32_para_aligned
    [OK
…[truncated 2804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T10:22:35.451176+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Get detailed info on the RUNNING 3B experiments\nrunning_keys = [\n    'exp_002_signals_3B_d000_a32_s42',\n    'exp_002_signals_3B_d100_a32_s42', \n    'exp_001_eval_3B_instruct_aligned_para'\n]\n\nprint('=== CURRENTLY RUNNING 3B EXPERIMENTS ===')\nprint()\nfor k in running_keys:\n    e = exps[k]\n    print(f'--- {k} ---')\n    print(json.dumps(e, indent=2, default=str)[:800])\n    print()\n\n# Now summarize 0.5B/1.5B signal completion\nprint()\nprint('=' * 80)\nprint('0.5B / 1.5B SIGNAL COMPLETION STATUS')\nprint('=' * 80)\nprint()\n\n# Also check for experiments named with 'exp002-signal' prefix\nfor k in sorted(exps.keys()):\n    if not (('05B' in k or '15B' in k or '0.5B' in k or '1.5B' in k or '1p5B' in k) and ('signal' in k.lower())):\n        continue\n    e = exps[k]\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    notes = e.get('notes','')\n    spec = e.get('spec',{})\n    \n    model = '0.5B' if ('05B' in k) else '1.5B'\n    \n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(spec):\n            dosage = d\n            break\n    # check notes for dosage info\n    if dosage == 'unknown' and notes:\n        if 'd000' in notes and 'd005' in notes:\n            dosage = 'ALL'\n    \n    seed = 'unknown'\n    if 's42' in k: seed = '42'\n    elif 's123' in k: seed = '123'\n    elif spec.get('seed'): seed = str(spec['seed'])\n    \n    mark = 'OK' if conclusion=='success' else ('FAIL' if conclusion=='failed' else ('RUN' if status=='RUNNING' else status))\n    \n    print(f'  [{mark}] {k}')\n    print(f'       model={model} dosage={dosage} seed={seed}')\n    if notes:\n        print(f'       notes: {notes[:200]}')\n    print()\n\"",
  "description": "Get running 3B experiments and 0.5B/1.5B signal detail"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Get detailed info on the RUNNING 3B experiments\nrunning_keys = [\n    'exp_002_signals_3B_d000_a32_s42',\n    'exp_002_signals_3B_d100_a32_s42', \n    'exp_001_eval_3B_instruct_aligned_para'\n]\n\nprint('=== CURRENTLY RUNNING 3B EXPERIMENTS ===')\nprint()\nfor k in running_keys:\n    e = exps[k]\n    print(f'--- {k} ---')\n    print(json.dumps(e, indent=2, default=str)[:800])\n    print()\n\n# Now summarize 0.5B/1.5B signal completion\nprint()\nprint('=' * 80)\nprint('0.5B / 1.5B SIGNAL COMPLETION STATUS')\nprint('=' * 80)\nprint()\n\n# Also check for experiments named with 'exp002-signal' prefix\nfor k in sorted(exps.keys()):\n    if not (('05B' in k or '15B' in k or '0.5B' in k or '1.5B' in k or '1p5B' in k) and ('signal' in k.lower())):\n        continue\n    e = exps[k]\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    notes = e.get('notes','')\n    spec = e.get('spec',{})\n    \n    model = '0.5B' if ('05B' in k) else '1.5B'\n    \n    dosage = 'unknown'\n    for d in ['d000', 'd005', 'd025', 'd100']:\n        if d in k or d in str(spec):\n            dosage = d\n            break\n    # check notes for dosage info\n    if dosage == 'unknown' and notes:\n        if 'd000' in notes and 'd005' in notes:\n            dosage = 'ALL'\n    \n    seed = 'unknown'\n    if 's42' in k: seed = '42'\n    elif 's123' in k: seed = '123'\n    elif spec.get('seed'): seed = str(spec['seed'])\n    \n    mark = 'OK' if conclusion=='success' else ('FAIL' if conclusion=='failed' else ('RUN' if status=='RUNNING' else status))\n    \n    print(f'  [{mark}] {k}')\n    print(f'       model={model} dosage={dosage} seed={seed}')\n    if notes:\n        print(f'       notes: {notes[:200]}')\n    print()\n\"",
    "description": "Get running 3B experiments and 0.5B/1.5B signal detail"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T10:22:35.451366+00:00_

=== CURRENTLY RUNNING 3B EXPERIMENTS ===

--- exp_002_signals_3B_d000_a32_s42 ---
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-16T07:09:17.976Z",
  "updated_at": "2026-05-16T07:09:43.025Z",
  "spec": {
    "command": "bash /root/contamcal-irt-calibration/exp002/run_3B_d000_a32_s42_signals.sh",
    "server": "cqa1-21977",
    "gpu": "cuda:4",
    "pid": "721519",
    "log_path": "~/runs/contamcal-irt-calibration/exp_002_signals_3B_d000_a32_s42.log",
    "submitted_at": "2026-05-16T07:09:17.497Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42",
    "model_name": "Qwen2.5-3B_d000_s42 (alpha=32)",
    "seed": 42,
    "hypothesis": "Compute contamination signals (s1_embedding, s2_minkpp, s4_selfcritique) for d000 baseline across mmlu/

--- exp_002_signals_3B_d100_a32_s42 ---
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-16T07:29:33.942Z",
  "updated_at": "2026-05-16T07:30:09.869Z",
  "spec": {
    "command": "bash /root/contamcal-irt-calibration/exp002/run_signals_3B_d100_a32_s42.sh",
    "server": "cqa1-21977",
    "gpu": "cuda:1",
    "pid": "724022",
    "log_path": "~/runs/contamcal-irt-calibration/exp_002_signals_3B_d100_a32_s42.log",
    "submitted_at": "2026-05-16T07:29:33.473Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl",
    "data_count": 9,
    "model_name": "Qwen2.5-3B_d100_a32_s42_v3",
    "seed": 42,
    "hypothesis": "3B d100 s42 alpha=32 signals. Completes 3B s42 RRF coverage (last missing dosage). Uses 

--- exp_001_eval_3B_instruct_aligned_para ---
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-16T07:54:58.792Z",
  "updated_at": "2026-05-16T07:55:55.970Z",
  "spec": {
    "command": "bash /root/contamcal-irt-calibration/scripts/run_instruct_3b_eval.s
…[truncated 1746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T10:22:35.451536+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Get full details on the running 0.5B/1.5B signal exps\nfor k in ['exp_002_signals_05B_s123_v2', 'exp_002_signals_15B_d100_s123_cuda2', 'exp_002_signals_15B_s123_batch']:\n    e = exps[k]\n    print(f'--- {k} ---')\n    print(json.dumps(e, indent=2, default=str)[:600])\n    print()\n\n# Also check if there are any 3B entries in the 'exp006' range (IRT/analysis)\nprint()\nprint('=== exp006 entries referencing 3B ===')\nfor k in sorted(exps.keys()):\n    if not k.startswith('exp006'):\n        continue\n    e = exps[k]\n    full = json.dumps(e)\n    if '3B' in full:\n        notes = e.get('notes','')[:200]\n        status = e.get('status','?')\n        conclusion = e.get('conclusion','')\n        print(f'  {k}: status={status}, conclusion={conclusion}')\n        if notes:\n            print(f'    {notes}')\n        print()\n\"",
  "description": "Get details on running 0.5B/1.5B signals and exp006 3B references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/4084f923-c726-4ccc-869a-0251787ffacb/tool-results/mcp-agent-ml-research-read_registry-1778926643978.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Get full details on the running 0.5B/1.5B signal exps\nfor k in ['exp_002_signals_05B_s123_v2', 'exp_002_signals_15B_d100_s123_cuda2', 'exp_002_signals_15B_s123_batch']:\n    e = exps[k]\n    print(f'--- {k} ---')\n    print(json.dumps(e, indent=2, default=str)[:600])\n    print()\n\n# Also check if there are any 3B entries in the 'exp006' range (IRT/analysis)\nprint()\nprint('=== exp006 entries referencing 3B ===')\nfor k in sorted(exps.keys()):\n    if not k.startswith('exp006'):\n        continue\n    e = exps[k]\n    full = json.dumps(e)\n    if '3B' in full:\n        notes = e.get('notes','')[:200]\n        status = e.get('status','?')\n        conclusion = e.get('conclusion','')\n        print(f'  {k}: status={status}, conclusion={conclusion}')\n        if notes:\n            print(f'    {notes}')\n        print()\n\"",
    "description": "Get details on running 0.5B/1.5B signals and exp006 3B references"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T10:22:35.451691+00:00_

--- exp_002_signals_05B_s123_v2 ---
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-16T03:03:30.869Z",
  "updated_at": "2026-05-16T04:09:04.152Z",
  "spec": {
    "hypothesis": "0.5B d000 s123 signals computation. D099/D101 priority for IRT pool N expansion.",
    "model_name": "Qwen2.5-0.5B",
    "seed": 123,
    "server": "cqa1-21977",
    "gpu": "cuda:5",
    "data_path": "/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s123",
    "data_count": 1,
    "command": "compute_signals.py 0.5B d000_s123 mmlu signals (s1+s2+s4)",
    "log_path": "/root/autodl-tmp/exp002/signals/signals_05B_s123_v2.log",
    "t

--- exp_002_signals_15B_d100_s123_cuda2 ---
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-16T10:07:31.281Z",
  "updated_at": "2026-05-16T10:07:38.375Z",
  "spec": {
    "command": "bash run_15B_d100_s123_cuda2.sh (CUDA_VISIBLE_DEVICES=2, 3 benchmarks \u00d7 3 signals)",
    "server": "cqa1-21977",
    "gpu": "cuda:2",
    "pid": "746777",
    "data_path": "/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d100_s123/",
    "data_count": 9,
    "model_name": "Qwen2.5-1.5B_d100_s123",
    "seed": 123,
    "hypothesis": "1.5B d100 s123 signals (s1_embedding + s2_minkpp + s4_selfcritique \u00d7 mmlu + gsm8k + arc_challenge

--- exp_002_signals_15B_s123_batch ---
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-16T03:44:39.543Z",
  "updated_at": "2026-05-16T03:45:59.000Z",
  "spec": {
    "command": "bash run_15B_s123_signals.sh",
    "server": "cqa1-21977",
    "gpu": [
      "cuda:0"
    ],
    "pid": "691872",
    "log_path": "~/runs/contamcal-irt-calibration/exp_002_signals_15B_s123_batch.log",
    "submitted_at": "2026-05-16T03:44:35.931Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_*_s123",
    "data_count": 12,
    "


=== exp006 entries referencing 3B ===
  exp006-pooled-05B-15B-arc-v2: stat
…[truncated 365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T10:22:35.451898+00:00_

Here is the exhaustive structured report:

---

## 3B EXPERIMENTS — FULL REGISTRY EXTRACT (86 entries)

### TRAINING (SFT) — Definitive Status by Dosage x Seed

| Dosage | Seed 42 (a32) | Seed 123 |
|--------|---------------|----------|
| **d000** | `exp_001_sft_3B_d000_s42_a32` — **OK** | `exp_001_sft_3B_d000_s123` — **OK** |
| **d005** | `exp_001_sft_3B_d005_s42_a32` — **OK** | `exp_001_sft_3B_d005_s123` — **OK** |
| **d025** | `exp_001_sft_d025_3B_v3` — **OK** (alpha=32 confirmed D086) | `exp_001_sft_3B_d025_s123` — **OK** |
| **d100** | `exp_001_sft_3B_d100_s42_a32_v3` — **OK** | `exp_001_sft_3B_d100_s123_a32_v2` — **OK** |

All 8 cells covered. Deprecated entries (lr=2e-4/alpha=16 per D076): `exp_001_sft_d005_3B`, `exp_001_sft_d025_3B_v2`, `exp_001_sft_d100_3B_v2`.

---

### EVAL — Definitive Status by Dosage x Seed x Type

**Format: aligned / para_aligned**

| Dosage | Seed 42 (a32) aligned | Seed 42 (a32) para | Seed 123 aligned | Seed 123 para |
|--------|----------------------|-------------------|-----------------|--------------|
| **d000** | `_d000_s42_a32_batch` **OK** | `_d000_s42_a32_para_aligned` **OK** | `_d000_v2_s123_aligned` **OK** | `_d000_v2_s123_para_aligned` **OK** |
| **d005** | `_d005_s42_a32_batch` **OK** | `_d005_s42_para_aligned` **OK** | `_d005_s123_aligned` **OK** | `_d005_s123_para_aligned` **OK** |
| **d025** | `_d025_v2_aligned` **OK** | `_d025_s42_a32_para` **OK** | `_d025_s123_aligned` **OK** | `_d025_s123_para_aligned` **OK** |
| **d100** | `_d100_v2_aligned_v2` **OK** | `_d100_s42_para_aligned` **OK** | `_d100_v2_s123_aligned` **OK** | `_d100_s123_para_aligned_v2` **OK** |

All 16 cells covered. Additional: `exp_001_eval_3B_instruct_aligned_para` — **RUNNING** (Instruct baseline, no SFT).

---

### SIGNALS — Status by Dosage x Seed

| Dosage | Seed 42 | Seed 123 |
|--------|---------|----------|
| **d000** | `exp_002_signals_3B_d000_a32_s42` — **RUNNING** (cuda:4, PID 721519) | `exp_002_signals_3B_v7` — **OK** (notes say d000) |
|
…[truncated 2766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-16T10:22:35.452186+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-003: RRF Aggregation of Contamination Detection Signals.\\n\\nFuses per-item signal scores from exp-002 into composite exposure scores\\nusing Reciprocal Rank Fusion (Cormack et al., 2009).\\n\\nInput:  Signal JSONs from /root/autodl-tmp/exp002/signals/{model}_{dosage}_{seed}/\\nOutput: Per-item exposure scores in [0,1] for downstream IRT calibration (exp-006)\\n\\nCSV output columns: item_id, benchmark, model_id, model_size, dose, seed,\\n                    rrf_score, rrf_raw, s1_embedding, s2_minkpp,\\n                    s4_selfcritique, rank_s1_embedding, ...\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport logging\\nimport re\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nlogger = logging.getLogger(__name__)\\n\\nSIGNAL_KEYS = [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s4_selfcritique\\\"]\\nSIGNAL_NAMES = {\\n    \\\"s1_embedding\\\": \\\"Embedding\\\",\\n    \\\"s2_minkpp\\\": \\\"Min-K++\\\",\\n    \\\"s4_selfcritique\\\": \\\"Self-Critique\\\",\\n}\\nDEFAULT_K = 60\\n\\nSIGNAL_ROOT = \\\"/root/autodl-tmp/exp002/signals\\\"\\nLABELS_ROOT = \\\"/root/autodl-tmp/exp001/sft_data\\\"\\nBENCHMARKS = [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\"]\\nDOSAGES = [\\\"d000\\\", \\\"d005\\\", \\\"d025\\\", \\\"d100\\\"]\\nDOSAGE_NUM = {\\\"d000\\\": 0, \\\"d005\\\": 5, \\\"d025\\\": 25, \\\"d100\\\": 100}\\n\\nSKIP_PATTERNS = [\\\"DEPRECATED\\\"]\\n\\n# D076: alpha=16 / lr=2e-4 checkpoints — all downstream signals invalidated\\nALPHA16_BLOCKLIST = {\\n    \\\"Qwen2.5-3B_d000_s42\\\",\\n    \\\"Qwen2.5-3B_d000_v2_s42\\\",\\n    \\\"Qwen2.5-3B_d005_s42\\\",\\n    \\\"Qwen2.5-3B_d025_s42\\\",\\n    \\\"Qwen2.5-3B_d100_s42\\\",\\n}\\n\\n_DIR_RE = re.compile(r'Qwen2\\\\.5-(\\\\d+\\\\.?\\\\d*B)_(d\\\\d+)(?:_[va]\\\\d+)*_(s\\\\d+)')\\n\\n\\ndef parse_model_dir(dirname: str) -> dict:\\n    \\\"\\\"\\\"Parse signal directory name into model_size, dose, seed.\\\"\\
…[truncated 7347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T10:22:35.452433+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-16 00:58 UTC | 更新原因: D090 sim_sweep_v7完成 + D091 s4降级P1 + Reviewer校正(cuda:4实际运行/Claim3间接支撑/s4非critical) + Agent Session#14状态同步\\n\\n## 核心方向\\nContamCal：post-hoc statistical calibration via contamination-augmented 4PL IRT。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（距今 9 天）\\n\\n## 当前进展\\n- **阶段**: Research (MVP 2026-05-13 通过) + 审稿进行中\\n- **Plan coverage**: Claim 1 ↑ (exp-004 sim_sweep_v7 完成 9/12, D090) | Claim 2=60% (3/5) | Claim 3 有 exp-004 间接支撑 (also_supports) | Overall ↑\\n- **IRT Pool**: N=23 (1.5B+3B), N=35 含 0.5B。1.5B 双种子矩阵全就绪 (16/16)。3B 是瓶颈 (7/16 cells)\\n- **sim_sweep_v7 ✅**: gamma_bias [-0.025,+0.056], CI95 coverage [0.8,1.0], theta_corr [0.947,0.972]。Claim 1 identifiability 充分支撑\\n\\n## GPU 实时占用 (6× RTX 4090D, cqa1-21977, 100% 饱和)\\n| GPU | 任务 | 进度 | 备注 |\\n|-----|------|------|------|\\n| cuda:0 | ⚠️ SFT d005_s42_a32 + eval d100_s123_a32 GSM8K | SFT ~79%, eval ~75% | 双进程，等完成不干预 |\\n| cuda:1 | SFT d100_s42_a32_v3 | ~94%→完成中 | 释放后分配下一任务 |\\n| cuda:2 | signals d005_s123 mmlu | 运行中 | — |\\n| cuda:3 | eval d025_v3_s42 aligned | 运行中 | — |\\n| cuda:4 | d000_s42_a32 batch eval (aligned+para) | 刚提交 | v8_recovery 已标 FAILED |\\n| cuda:5 | signals d025_v3_s42 mmlu | 运行中 | — |\\n| CPU | sim_sweep_v7 ✅ 完成 (9/12) | — | auc0.65×3 CmdStan TMPDIR 竞态，不重试 |\\n\\n## Signal Pipeline (exp-002)\\n- 0.5B ✅ | 1.5B ✅ (12/12 PASS)\\n- **3B 🟡**: d000_s42 旧 checkpoint signals 不可用(D076); d025+d100 signals 运行中; d005 待 GPU\\n- **s4_selfcritique MMLU OOM → P1 (D091)**：不阻塞 critical path (D034 S1-only pipeline)。论文可用 0.5B/1.5B 完整 s4 + 3B S1/S2/S3。修复仍需做但不急\\n\\n## Critical Path (EMNLP T-9)\\n```\\n[Now]     cuda:0 双进程完成 → d005_s42 eval\\n          cuda:1 完成 → 下一 SFT/eval\\n          cuda:4 d000_s42_a32 eval 运行中\\n[Day 1-2] 3B s42 eval+signals 全
…[truncated 2353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T10:22:35.452648+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -d /root/autodl-tmp/exp002/signals/Qwen2.5-3B*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -d /root/autodl-tmp/exp002/signals/Qwen2.5-3B*"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T10:22:35.452779+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp003/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp003/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-16T10:22:35.452919+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s42_DEPRECATED_alpha16\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T10:22:35.453045+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T10:22:35.453205+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -d /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B* /root/autodl-tmp/exp002/signals/Qwen2.5-1.5B*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -d /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B* /root/autodl-tmp/exp002/signals/Qwen2.5-1.5B*"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T10:22:35.453429+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s123\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s123\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d025_s123\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d025_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s123\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d000_s123\\n/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d000_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d005_s123\\n/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d005_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d025_s123\\n/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d025_s42\\n/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d100_s123\\n/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d100_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T10:22:35.453600+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42 -name \"signals_merged_*.json\" -o -name \"signal_*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42 -name \"signals_merged_*.json\" -o -name \"signal_*.json\""
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T10:22:35.453759+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signal_s1_embedding_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signal_s2_minkpp_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signal_s4_selfcritique_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signals_merged_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signal_s1_embedding_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signal_s2_minkpp_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signal_s4_selfcritique_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signals_merged_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signal_s1_embedding_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signal_s2_minkpp_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signal_s4_selfcritique_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/signals_merged_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/signal_s1_embedding_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/signal_s1_embedding_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/signal_s1_embedding_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/signal_s2_minkpp_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/signal_s2_minkpp_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/signal_s2_minkpp_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/signal_s4_selfcritique_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/signal_s4_selfcritique_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/signal_s4_selfcritique_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a3
…[truncated 1049 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T10:22:35.453900+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123 -name \"signals_merged_*.json\" -o -name \"signal_*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123 -name \"signals_merged_*.json\" -o -name \"signal_*.json\""
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T10:22:35.454023+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp003 -type f -name \"*.json\" -o -name \"*.csv\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp003 -type f -name \"*.json\" -o -name \"*.csv\""
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-16T10:22:35.454169+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signal_s1_embedding_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signal_s2_minkpp_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signal_s4_selfcritique_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signals_merged_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signal_s1_embedding_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signal_s2_minkpp_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signal_s4_selfcritique_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signals_merged_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signal_s1_embedding_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signal_s2_minkpp_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signal_s4_selfcritique_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/signals_merged_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s1_embedding_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s2_minkpp_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s1_embedding_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s2_minkpp_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s4_selfcritique_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signals_merged_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s1_embedding_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s2_minkpp_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s4_selfcritique_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signals_merged_arc_challenge.json\\n/root/autodl-tmp/exp00
…[truncated 1263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T10:22:35.454349+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp003/exposure_scores.json\\n/root/autodl-tmp/exp003/exposure_aggregated.json\\n/root/autodl-tmp/exp003/exp003_flagged_items.json\\n/root/autodl-tmp/exp003/exp003_results.json\\n/root/autodl-tmp/exp003/exp003_mock/mock_metrics.json\\n/root/autodl-tmp/exp003/exp003_real_test/rrf_scores_Qwen2.5-0.5B_d005_s42_mmlu.json\\n/root/autodl-tmp/exp003/test_exp003/exposure_scores.json\\n/root/autodl-tmp/exp003/rrf_05B_15B/exposure_scores.json\\n/root/autodl-tmp/exp003/rrf_05B_15B/exposure_aggregated.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T10:22:35.454526+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42 -name \"signal_*.json\" -o -name \"signals_merged_*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42 -name \"signal_*.json\" -o -name \"signals_merged_*.json\""
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T10:22:35.454657+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42/signal_s1_embedding_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42/signal_s2_minkpp_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T10:22:35.454776+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp003/rrf_05B_15B/exposure_aggregated.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp003/rrf_05B_15B/exposure_aggregated.json"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T10:22:35.454893+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123 -name \"signals_merged_mmlu.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123 -name \"signals_merged_mmlu.json\""
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-16T10:22:35.455122+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"arc_challenge\\\": [\\n    0.16803934060418566,\\n    0.10902494243633097,\\n    0.38666665842655273,\\n    0.15154102638550063,\\n    0.173740764773006,\\n    0.1108768722178274,\\n    0.22808563394390324,\\n    0.13209892102683285,\\n    0.2362946023053938,\\n    0.302509018260125,\\n    0.2057612733079911,\\n    0.08187784436168134,\\n    0.1426720808069294,\\n    0.18658265065968116,\\n    0.281025962497638,\\n    0.19352920341434388,\\n    0.17350938167145394,\\n    0.10818388818475132,\\n    0.10230001684024574,\\n    0.13926261448137361,\\n    0.08148430661805672,\\n    0.2939936363072783,\\n    0.17093749111474282,\\n    0.20120286016299122,\\n    0.1712703990809365,\\n    0.19812763611924858,\\n    0.23186170626029962,\\n    0.16482637824803167,\\n    0.22147052318209234,\\n    0.2042631428452629,\\n    0.1935744583655632,\\n    0.08761897468074788,\\n    0.19332001625541093,\\n    0.1006175740850947,\\n    0.11006806755190789,\\n    0.32820976209273084,\\n    0.29657207381040346,\\n    0.18820684216162623,\\n    0.1600636692292106,\\n    0.13473584994568027,\\n    0.14024352467554033,\\n    0.21629305093562545,\\n    0.1320226809620246,\\n    0.26119048274832823,\\n    0.294783080968134,\\n    0.19210620303986214,\\n    0.09321607215395745,\\n    0.11359511669348334,\\n    0.11192912488727762,\\n    0.20157356294855663,\\n    0.1871404062593828,\\n    0.1449584312826067,\\n    0.19402795657388314,\\n    0.17259216994880025,\\n    0.1008429329100787,\\n    0.535945842015378,\\n    0.09828595125117484,\\n    0.13918674681730492,\\n    0.13277622074702403,\\n    0.26751739187107737,\\n    0.2762701827574659,\\n    0.26428353570026203,\\n    0.11844091689299825,\\n    0.14777235227917673,\\n    0.14734809171144028,\\n    0.2221685231205818,\\n    0.21709285670020959,\\n    0.17235539176197437,\\n    0.24867469517102825,\\n    0.09523616608183806,\\n    0.23758484413916137,\\n    0.20509489566426
…[truncated 6851 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T10:22:35.455276+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T10:22:35.455522+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -c /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42/signal_s1_embedding_mmlu.json /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42/signal_s4_selfcritique_arc_challenge.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -c /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42/signal_s1_embedding_mmlu.json /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42/signal_s4_selfcritique_arc_challenge.json"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T10:22:35.455665+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"7865462 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42/signal_s1_embedding_mmlu.json\\n 290589 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42/signal_s4_selfcritique_arc_challenge.json\\n8156051 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T10:22:35.455789+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -c /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s1_embedding_mmlu.json /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s4_selfcritique_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -c /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s1_embedding_mmlu.json /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s4_selfcritique_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T10:22:35.455920+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \" 7843126 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s1_embedding_mmlu.json\\n 3336149 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s123/signal_s4_selfcritique_mmlu.json\\n11179275 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T10:22:35.456041+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T10:22:35.456160+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"739125, GPU-52bfebf5-3ba8-8f6e-ae36-56511cce901f, 4112 MiB\\n727334, GPU-466bc8fe-796f-8068-9660-0fb52de3681b, 6620 MiB\\n750036, GPU-b8bea42c-5b6e-4ba4-3618-e9b2095c6e54, 4166 MiB\\n746500, GPU-c30258a6-4c47-f7a8-7b0c-4c5cbdc3c1c3, 9062 MiB\\n745695, GPU-f1a0b9ee-87a0-41a4-a300-b3cb3c870263, 1898 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T10:22:35.456288+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi --query-gpu=index,uuid,memory.used,memory.total --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi --query-gpu=index,uuid,memory.used,memory.total --format=csv,noheader"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T10:22:35.456435+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, GPU-52bfebf5-3ba8-8f6e-ae36-56511cce901f, 4121 MiB, 24564 MiB\\n1, GPU-466bc8fe-796f-8068-9660-0fb52de3681b, 6629 MiB, 24564 MiB\\n2, GPU-b8bea42c-5b6e-4ba4-3618-e9b2095c6e54, 4175 MiB, 24564 MiB\\n3, GPU-c30258a6-4c47-f7a8-7b0c-4c5cbdc3c1c3, 9071 MiB, 24564 MiB\\n4, GPU-ec1378f2-6e00-01ce-6bf6-c5e8081f887b, 0 MiB, 24564 MiB\\n5, GPU-f1a0b9ee-87a0-41a4-a300-b3cb3c870263, 1907 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T10:22:35.456564+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp002/signals -maxdepth 1 -name \"Qwen2.5-3B_d000*s123*\" -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp002/signals -maxdepth 1 -name \"Qwen2.5-3B_d000*s123*\" -type d"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T10:22:35.456682+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-16T10:22:35.456883+00:00_

数据收集完毕。以下是完整审计报告。

---

## 1. 3B s42 覆盖矩阵

### Eval (exp-001): ✅ 16/16 COMPLETE

| Dosage | aligned | para_aligned |
|--------|---------|--------------|
| d000 s42 | ✅ | ✅ |
| d005 s42 | ✅ | ✅ |
| d025 s42 | ✅ | ✅ |
| d100 s42 | ✅ | ✅ |
| d000 s123 | ✅ | ✅ |
| d005 s123 | ✅ | ✅ |
| d025 s123 | ✅ | ✅ |
| d100 s123 | ✅ | ✅ |

+1 RUNNING: 3B-Instruct baseline eval (cuda:3)

### Signals (exp-002): 6/8 complete

| Dosage | s42 | s123 |
|--------|-----|------|
| **d000** | ✅ 9/9 files (7.8MB s1 mmlu confirmed) | ❌ **MISSING** — no directory on disk |
| **d005** | ✅ complete + merged | ✅ complete + merged |
| **d025** | ✅ 9/9 (v3 alpha=32) | ✅ 9/9 (individual files + merged gsm8k/arc) |
| **d100** | 🔄 **RUNNING** cuda:1 (2/9: s1+s2 mmlu only) | ✅ complete + merged |

---

## 2. GPU 实时状态

| GPU | 显存 | 状态 |
|-----|------|------|
| cuda:0 | 4.1/24.6 GB | busy |
| cuda:1 | 6.6/24.6 GB | busy — d100_s42 signals |
| cuda:2 | 4.2/24.6 GB | busy |
| cuda:3 | 9.1/24.6 GB | busy — Instruct eval |
| cuda:4 | **0/24.6 GB** | **FREE** |
| cuda:5 | 1.9/24.6 GB | busy |

---

## 3. RRF 聚合 (exp-003) 前置条件

**RRF 输入要求** (`rrf_aggregation.py --generate-exposure`):
- 扫描 `/root/autodl-tmp/exp002/signals/` 下所有 `Qwen2.5-*` 目录
- 每个目录需要 `signal_{s1/s2/s4}_{mmlu/gsm8k/arc_challenge}.json`（9 files）或 merged
- 自动跳过 ALPHA16_BLOCKLIST
- 可以处理部分信号（graceful degradation）

**0.5B + 1.5B RRF: ✅ 已完成**
- 产出: `/root/autodl-tmp/exp003/rrf_05B_15B/exposure_scores.json`
- 覆盖: 0.5B × 4 dosages × 2 seeds + 1.5B × 4 dosages × 2 seeds = 16 respondents

**3B RRF: 阻塞中**
| 阻塞项 | 状态 | 预估剩余时间 |
|---------|------|------------|
| d100_s42 signals | RUNNING cuda:1, 2/9 done | ~3-5h |
| d000_s123 signals | **未开始** | ~2-3h (可立即在 cuda:4 启动) |

**最小可行 RRF**: 可先用 6/8 跑 partial RRF（缺 d100_s42 和 d000_s123），但会损失 2 个 respondents（N=35→33 含 0.5B/1.5B，或 N=21→19 仅 1.5B+3B）。

---

## 4. GPU 释放后任务优先级队列

按 C007 约束 + paper critical path:

| 优先级 | 任务 | GPU 需求 | 预估耗时 | 阻塞什么 |
|--------|------|----------|----------|----------|
| **P0** ⚡ | 3B d000_s123 signals (全部 s1/s2/s4 × 3 benchmarks) | 1 GPU (~6GB) | 2-3h | 3B RRF 完整性 |
| P1 | 等 d100_s42 完成 (cuda:1) | 已占用 | 3-5h | 3B RRF 完整性 |
| P2 | 3B RRF 聚合 | CPU only | 5-10min | IRT fitting |
| P3 | pooled IRT fitting (per-benchmark γ_k, Stan NUTS) | CPU only | 1-2h | paper results |

**cuda:4 现在空闲 → 应立即提交 3B d000_s123 signals**

---

## 5. Paper Timeline 影响评估

```
May 16 (今天, T-9):
  - 立即提交 d000_s123 signals → cuda:4 [2-3h]
  - d100_s42 继续在 cuda:1 [3-5h]
  
May 16 晚 / May 17 (T-8):
  - 两个 signals 任务完成 → 3B 矩阵 8/8 ✅
  - RRF 聚合 (CPU, 10min) → exposure_scores for 3B
  
May 17 (T-8):
  - pooled IRT fitting: N=35 (0.5B+1.5B+3B, 全 dosage × 双 seed)
  - 7 baselines 对比 + ablation
  
May 18-19 (T-7~T-6):
  - Results table 定稿, paper writing
  
May 20-24 (T-5~T-1):
  - Review 迭代 + 提交
```

**结论: 3B pipeline 可在 T-8 (May 17) 前全部完成，不阻塞 EMNLP deadline。**

唯一风险：d100_s42 如果 cuda:1 有 OOM 或进程中断需要重启，可能滑到 May 17 下午。建议几小时后检查 cuda:1 进度。

---

## 6. 立即行动项

**cuda:4 空闲 → 提交 3B d000_s123 signals**

需要确认：
1. d000_s123 的 SFT checkpoint 路径（应为 `Qwen2.5-3B_d000_s123` 或类似）
2. `cat adapter_config.json | grep lora_alpha` 验证 alpha=32（C006）
3. CUDA_VISIBLE_DEVICES=4 显式设置（C004）

是否要我现在查找 checkpoint 路径并准备提交命令？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_3B_signal_coverage_audit_20260516T101702"
}
```

</details>

---
