# eval qwen deberta ft combo

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_eval_qwen-deberta-ft-combo_20260522T185637.jsonl`
- **Structured JSON:** [`e9feabf40b1dd92caf1c.json`](../../sessions/e9/e9feabf40b1dd92caf1c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

63 recorded events

### Tool call

_source line 1 · 2026-05-22T18:59:41.556491+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T18:59:41.556837+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T18:59:41.557051+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -n \"CLASSES\\|sorted\\|most_common\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -n \"CLASSES\\|sorted\\|most_common\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T18:59:41.557198+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T18:59:41.557325+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results/ -path \"*qwen*\" -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results/ -path \"*qwen*\" -name \"*.json\""
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T18:59:41.557538+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-1041_Q1.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNeg-OWA-D5-81_Q11.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-1284_Q8.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-585_Q19.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNoneg-OWA-D5-949_Q8.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNeg-OWA-D5-508_Q2.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-270_Q8.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNoneg-OWA-D5-487_Q19.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-971_Q5.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-804_Q16.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-572_Q18.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-285_Q16.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNoneg-OWA-D5-686_Q18.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-735_Q9.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNeg-OWA-D5-966_Q7.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-145_Q9.json\\n/root/symb_invariant_consensus/results/exp032_
…[truncated 6335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T18:59:41.557727+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -n \"CLASSES\\|sorted\\|most_common\\|tiebreak\\|alphabetical\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -n \"CLASSES\\|sorted\\|most_common\\|tiebreak\\|alphabetical\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T18:59:41.557870+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T18:59:41.558020+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls -d /root/symb_invariant_consensus/results/*qwen*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls -d /root/symb_invariant_consensus/results/*qwen*"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T18:59:41.558155+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large\\n/root/symb_invariant_consensus/results/dir_k_nli_qwen3_proofwriter\\n/root/symb_invariant_consensus/results/exp028b_qwen3_thinking_folio204\\n/root/symb_invariant_consensus/results/exp032_qwen14b_pw_oracle\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600\\n/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking\\n/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204\\n/root/symb_invariant_consensus/results/exp038_qwen25_14b_logiqa200\\n/root/symb_invariant_consensus/results/exp064_deepseek_r1_qwen3_8b_folio204\\n/root/symb_invariant_consensus/results/exp068_qwen3_logiqa200\\n/root/symb_invariant_consensus/results/exp_folio_2x2_qwen3\\n/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T18:59:41.558279+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results/ -maxdepth 2 -name \"results.json\" -path \"*qwen*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results/ -maxdepth 2 -name \"results.json\" -path \"*qwen*\""
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T18:59:41.558408+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\\n/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json\\n/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json\\n/root/symb_invariant_consensus/results/exp038_qwen25_14b_logiqa200/results.json\\n/root/symb_invariant_consensus/results/exp064_deepseek_r1_qwen3_8b_folio204/results.json\\n/root/symb_invariant_consensus/results/dir_k_nli_qwen3_proofwriter/results.json\\n/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json\\n/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json\\n/root/symb_invariant_consensus/results/exp032_qwen14b_pw_oracle/results.json\\n/root/symb_invariant_consensus/results/exp_folio_2x2_qwen3/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T18:59:41.558558+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -nE \"CLASSES|sorted|most_common|tiebreak|alphabetical\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -nE \"CLASSES|sorted|most_common|tiebreak|alphabetical\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T18:59:41.558688+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T18:59:41.558806+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "head -5 /root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "head -5 /root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T18:59:41.558951+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"Qwen2.5-14B ProofWriter NLI Combo (DeBERTa-large reused from D116)\\\",\\n  \\\"verifier_model\\\": \\\"microsoft/deberta-large-mnli\\\",\\n  \\\"generator_model\\\": \\\"Qwen2.5-14B-Instruct\\\",\\n  \\\"dataset\\\": \\\"ProofWriter-D5-600\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T18:59:41.559073+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "head -5 /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "head -5 /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T18:59:41.559197+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"D116: Qwen3-14B ProofWriter combo with DeBERTa-large-mnli\\\",\\n  \\\"verifier_model\\\": \\\"microsoft/deberta-large-mnli\\\",\\n  \\\"generator_model\\\": \\\"Qwen3-14B (non-thinking mode)\\\",\\n  \\\"dataset\\\": \\\"ProofWriter-D5-600\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T18:59:41.559329+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -n \"most_common\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -n \"most_common\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T18:59:41.559448+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T18:59:41.559561+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -n \"sorted\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -n \"sorted\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T18:59:41.559687+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"30:CLASSES = sorted([\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"])\\n68:    return sorted(tied)[0]\\n247:                combo_answers.append(sorted(tied_c)[0])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T18:59:41.559803+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -n \"CLASSES\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -n \"CLASSES\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T18:59:41.559944+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"30:CLASSES = sorted([\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"])\\n66:    max_v = max(votes.get(c, 0) for c in CLASSES)\\n67:    tied = [c for c in CLASSES if votes.get(c, 0) == max_v]\\n182:    for cls in CLASSES:\\n198:    for cls in CLASSES:\\n243:                combo_v = {c: sv.get(c, 0) for c in CLASSES}\\n245:                max_cv = max(combo_v.get(c, 0) for c in CLASSES)\\n246:                tied_c = [c for c in CLASSES if combo_v.get(c, 0) == max_cv]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T18:59:41.560066+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -n \"tiebreak\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -n \"tiebreak\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T18:59:41.560182+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T18:59:41.560337+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls /root/autodl-tmp/symb_invariant_consensus/models/deberta-large-pw-owa/best/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls /root/autodl-tmp/symb_invariant_consensus/models/deberta-large-pw-owa/best/"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T18:59:41.560462+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"config.json\\nmodel.safetensors\\ntokenizer.json\\ntokenizer_config.json\\ntraining_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T18:59:41.560576+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls /root/symb_invariant_consensus/data/proofwriter_full.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls /root/symb_invariant_consensus/data/proofwriter_full.json"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T18:59:41.560690+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "wc -l /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "wc -l /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-22T18:59:41.560810+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/data/proofwriter_full.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T18:59:41.560959+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"327 /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T18:59:41.561109+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -n \"add_argument\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -n \"add_argument\" /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T18:59:41.561241+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"99:    parser.add_argument(\\\"--model-path\\\", required=True, help=\\\"Path to fine-tuned checkpoint\\\")\\n100:    parser.add_argument(\\\"--sc-sources\\\", nargs=\\\"+\\\", default=[\\\"llama8b\\\", \\\"qwen14b\\\"],\\n102:    parser.add_argument(\\\"--weights\\\", nargs=\\\"+\\\", type=int, default=WEIGHTS)\\n103:    parser.add_argument(\\\"--max-length\\\", type=int, default=512)\\n104:    parser.add_argument(\\\"--batch-size\\\", type=int, default=32)\\n105:    parser.add_argument(\\\"--device\\\", default=\\\"cuda:0\\\")\\n106:    parser.add_argument(\\\"--output-dir\\\", default=None)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T18:59:41.561361+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results/ -maxdepth 2 -name \"results.json\" -path \"*qwen3*think*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results/ -maxdepth 2 -name \"results.json\" -path \"*qwen3*think*\""
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T18:59:41.561480+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T18:59:41.561630+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T18:59:41.561935+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Evaluate fine-tuned DeBERTa on ProofWriter depth-5 test set.\\nStandalone accuracy + combo with LLM SC votes.\\n\\nUsage:\\n    python scripts/eval_finetuned_nli.py \\\\\\n        --model-path checkpoints/deberta-large-pw-finetuned/best\\n    python scripts/eval_finetuned_nli.py \\\\\\n        --model-path /root/autodl-tmp/models/deberta-large-mnli \\\\\\n        --sc-sources llama8b qwen14b mistral\\n\\\"\\\"\\\"\\n\\n# Environment setup for westd-16639:\\n#   export CUDA_VISIBLE_DEVICES=&lt;free_gpu_id>\\n#   export LD_LIBRARY_PATH=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib:$LD_LIBRARY_PATH\\n\\n\\nimport argparse\\nimport json\\nimport os\\nimport time\\nfrom collections import Counter\\nimport numpy as np\\nimport torch\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom scipy.stats import binomtest\\n\\nPW_DATA_PATH = \\\"/root/symb_invariant_consensus/data/proofwriter_full.json\\\"\\nRESULTS_DIR = \\\"/root/symb_invariant_consensus/results\\\"\\nCLASSES = sorted([\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"])\\nWEIGHTS = [1, 3, 5]\\n\\nSC_SOURCES = {\\n    \\\"llama8b\\\": {\\n        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp048_llama8b_pw600/exp048_results.json\\\"),\\n        \\\"name\\\": \\\"LLaMA-3.1-8B-Instruct\\\",\\n        \\\"format\\\": \\\"results_list\\\",\\n    },\\n    \\\"qwen14b\\\": {\\n        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp032_qwen25_14b_pw600/results.json\\\"),\\n        \\\"name\\\": \\\"Qwen2.5-14B-Instruct\\\",\\n        \\\"format\\\": \\\"results_list\\\",\\n    },\\n    \\\"mistral\\\": {\\n        \\\"path\\\": \\\"/root/symb_invariant_consensus/data/mistral_pw600_sc_votes.json\\\",\\n        \\\"name\\\": \\\"Mistral-7B-Instruct-v0.3\\\",\\n        \\\"format\\\": \\\"vote_dict\\\",\\n    },\\n}\\n\\n\\ndef parse_pw_problem(text):\\n    for m in [\\n        \\\"Determine 
…[truncated 7356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T18:59:41.562154+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "head -30 /root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "head -30 /root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T18:59:41.562313+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 600,\\n    \\\"sica_accuracy\\\": 0.8566666666666667,\\n    \\\"sc_accuracy\\\": 0.85,\\n    \\\"sica_correct\\\": 514,\\n    \\\"sc_correct\\\": 510,\\n    \\\"extraction_rate\\\": 0.9966666666666667,\\n    \\\"total_constraints_extracted\\\": 146636,\\n    \\\"total_unique_constraints\\\": 22738,\\n    \\\"contradiction_rate\\\": 0.0042659864543935265,\\n    \\\"problems_with_contradictions\\\": 72,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"OWA-D5\\\": {\\n        \\\"sica\\\": 0.8566666666666667,\\n        \\\"sc\\\": 0.85,\\n        \\\"n\\\": 600\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"proofwriter\\\": {\\n        \\\"sica\\\": 0.8566666666666667,\\n        \\\"sc\\\": 0.85,\\n        \\\"n\\\": 600\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 61932.1\\n  },\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T18:59:41.562453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -c \"sc_vote_distribution\" /root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -c \"sc_vote_distribution\" /root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T18:59:41.562581+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"600\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T18:59:41.562735+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && cat -n scripts/eval_finetuned_nli.py | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cd /root/symb_invariant_consensus && cat -n scripts/eval_finetuned_nli.py | head -50"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T18:59:41.562917+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t#!/usr/bin/env python3\\n     2\\t\\\"\\\"\\\"Evaluate fine-tuned DeBERTa on ProofWriter depth-5 test set.\\n     3\\tStandalone accuracy + combo with LLM SC votes.\\n     4\\t\\n     5\\tUsage:\\n     6\\t    python scripts/eval_finetuned_nli.py \\\\\\n     7\\t        --model-path checkpoints/deberta-large-pw-finetuned/best\\n     8\\t    python scripts/eval_finetuned_nli.py \\\\\\n     9\\t        --model-path /root/autodl-tmp/models/deberta-large-mnli \\\\\\n    10\\t        --sc-sources llama8b qwen14b mistral\\n    11\\t\\\"\\\"\\\"\\n    12\\t\\n    13\\t# Environment setup for westd-16639:\\n    14\\t#   export CUDA_VISIBLE_DEVICES=&lt;free_gpu_id>\\n    15\\t#   export LD_LIBRARY_PATH=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib:$LD_LIBRARY_PATH\\n    16\\t\\n    17\\t\\n    18\\timport argparse\\n    19\\timport json\\n    20\\timport os\\n    21\\timport time\\n    22\\tfrom collections import Counter\\n    23\\timport numpy as np\\n    24\\timport torch\\n    25\\tfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\n    26\\tfrom scipy.stats import binomtest\\n    27\\t\\n    28\\tPW_DATA_PATH = \\\"/root/symb_invariant_consensus/data/proofwriter_full.json\\\"\\n    29\\tRESULTS_DIR = \\\"/root/symb_invariant_consensus/results\\\"\\n    30\\tCLASSES = sorted([\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"])\\n    31\\tWEIGHTS = [1, 3, 5]\\n    32\\t\\n    33\\tSC_SOURCES = {\\n    34\\t    \\\"llama8b\\\": {\\n    35\\t        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp048_llama8b_pw600/exp048_results.json\\\"),\\n    36\\t        \\\"name\\\": \\\"LLaMA-3.1-8B-Instruct\\\",\\n    37\\t        \\\"format\\\": \\\"results_list\\\",\\n    38\\t    },\\n    39\\t    \\\"qwen14b\\\": {\\n    40\\t        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp032_qwen25_14b_pw600/results.json\\\"),\\n    41\\t        \\\"name\\\": \\\"Qwen2.5-14B-Instruct\\\",\\n 
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T18:59:41.563081+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && sed -i '48a\\    },\\n    \"qwen3_14b\": {\\n        \"path\": os.path.join(RESULTS_DIR, \"exp033_qwen3_14b_pw600_nonthinking/results.json\"),\\n        \"name\": \"Qwen3-14B (non-thinking)\",\\n        \"format\": \"results_list\",' scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cd /root/symb_invariant_consensus && sed -i '48a\\    },\\n    \"qwen3_14b\": {\\n        \"path\": os.path.join(RESULTS_DIR, \"exp033_qwen3_14b_pw600_nonthinking/results.json\"),\\n        \"name\": \"Qwen3-14B (non-thinking)\",\\n        \"format\": \"results_list\",' scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T18:59:41.563211+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T18:59:41.563328+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat -n /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat -n /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-22T18:59:41.563623+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t#!/usr/bin/env python3\\n     2\\t\\\"\\\"\\\"Evaluate fine-tuned DeBERTa on ProofWriter depth-5 test set.\\n     3\\tStandalone accuracy + combo with LLM SC votes.\\n     4\\t\\n     5\\tUsage:\\n     6\\t    python scripts/eval_finetuned_nli.py \\\\\\n     7\\t        --model-path checkpoints/deberta-large-pw-finetuned/best\\n     8\\t    python scripts/eval_finetuned_nli.py \\\\\\n     9\\t        --model-path /root/autodl-tmp/models/deberta-large-mnli \\\\\\n    10\\t        --sc-sources llama8b qwen14b mistral\\n    11\\t\\\"\\\"\\\"\\n    12\\t\\n    13\\t# Environment setup for westd-16639:\\n    14\\t#   export CUDA_VISIBLE_DEVICES=&lt;free_gpu_id>\\n    15\\t#   export LD_LIBRARY_PATH=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib:$LD_LIBRARY_PATH\\n    16\\t\\n    17\\t\\n    18\\timport argparse\\n    19\\timport json\\n    20\\timport os\\n    21\\timport time\\n    22\\tfrom collections import Counter\\n    23\\timport numpy as np\\n    24\\timport torch\\n    25\\tfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\n    26\\tfrom scipy.stats import binomtest\\n    27\\t\\n    28\\tPW_DATA_PATH = \\\"/root/symb_invariant_consensus/data/proofwriter_full.json\\\"\\n    29\\tRESULTS_DIR = \\\"/root/symb_invariant_consensus/results\\\"\\n    30\\tCLASSES = sorted([\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"])\\n    31\\tWEIGHTS = [1, 3, 5]\\n    32\\t\\n    33\\tSC_SOURCES = {\\n    34\\t    \\\"llama8b\\\": {\\n    35\\t        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp048_llama8b_pw600/exp048_results.json\\\"),\\n    36\\t        \\\"name\\\": \\\"LLaMA-3.1-8B-Instruct\\\",\\n    37\\t        \\\"format\\\": \\\"results_list\\\",\\n    38\\t    },\\n    39\\t    \\\"qwen14b\\\": {\\n    40\\t        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp032_qwen25_14b_pw600/results.json\\\"),\\n    41\\t        \\\"name\\\": \\\"Qwen2.5-14B-Instruct\\\",\\n 
…[truncated 7596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-22T18:59:41.563831+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && python3 -c \"\nlines = open('scripts/eval_finetuned_nli.py').readlines()\n# Find and replace the SC_SOURCES block (lines 33-54, 0-indexed 32-53)\nnew_block = '''SC_SOURCES = {\n    \\\"llama8b\\\": {\n        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp048_llama8b_pw600/exp048_results.json\\\"),\n        \\\"name\\\": \\\"LLaMA-3.1-8B-Instruct\\\",\n        \\\"format\\\": \\\"results_list\\\",\n    },\n    \\\"qwen14b\\\": {\n        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp032_qwen25_14b_pw600/results.json\\\"),\n        \\\"name\\\": \\\"Qwen2.5-14B-Instruct\\\",\n        \\\"format\\\": \\\"results_list\\\",\n    },\n    \\\"mistral\\\": {\n        \\\"path\\\": \\\"/root/symb_invariant_consensus/data/mistral_pw600_sc_votes.json\\\",\n        \\\"name\\\": \\\"Mistral-7B-Instruct-v0.3\\\",\n        \\\"format\\\": \\\"vote_dict\\\",\n    },\n    \\\"qwen3_14b\\\": {\n        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp033_qwen3_14b_pw600_nonthinking/results.json\\\"),\n        \\\"name\\\": \\\"Qwen3-14B (non-thinking)\\\",\n        \\\"format\\\": \\\"results_list\\\",\n    },\n}\n'''\n# Find start (SC_SOURCES = {) and end of the block\nstart = None\nend = None\nbrace_count = 0\nfor i, line in enumerate(lines):\n    if 'SC_SOURCES = {' in line:\n        start = i\n        brace_count = 1\n        continue\n    if start is not None:\n        brace_count += line.count('{') - line.count('}')\n        if brace_count <= 0:\n            end = i\n            break\nlines[start:end+1] = [new_block]\nopen('scripts/eval_finetuned_nli.py', 'w').writelines(lines)\nprint('Done')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cd /root/symb_invariant_consensus && python3 -c \"\nlines = open('scripts/eval_finetuned_nli.py').readlines()\n# Find and replace the SC_SOURCES block (lines 33-54, 0-indexed 32-53)\nnew_block = '''SC_SOURCES = {\n    \\\"llama8b\\\": {\n        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp048_llama8b_pw600/exp048_results.json\\\"),\n        \\\"name\\\": \\\"LLaMA-3.1-8B-Instruct\\\",\n        \\\"format\\\": \\\"results_list\\\",\n    },\n    \\\"qwen14b\\\": {\n        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp032_qwen25_14b_pw600/results.json\\\"),\n        \\\"name\\\": \\\"Qwen2.5-14B-Instruct\\\",\n        \\\"format\\\": \\\"results_list\\\",\n    },\n    \\\"mistral\\\": {\n        \\\"path\\\": \\\"/root/symb_invariant_consensus/data/mistral_pw600_sc_votes.json\\\",\n        \\\"name\\\": \\\"Mistral-7B-Instruct-v0.3\\\",\n        \\\"format\\\": \\\"vote_dict\\\",\n    },\n    \\\"qwen3_14b\\\": {\n        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp033_qwen3_14b_pw600_nonthinking/results.json\\\"),\n        \\\"name\\\": \\\"Qwen3-14B (non-thinking)\\\",\n        \\\"format\\\": \\\"results_list\\\",\n    },\n}\n'''\n# Find start (SC_SOURCES = {) and end of the block\nstart = None\nend = None\nbrace_count = 0\nfor i, line in enumerate(lines):\n    if 'SC_SOURCES = {' in line:\n        start = i\n        brace_count = 1\n        continue\n    if start is not None:\n        brace_count += line.count('{') - line.count('}')\n        if brace_count <= 0:\n            end = i\n            break\nlines[start:end+1] = [new_block]\nopen('scripts/eval_finetuned_nli.py', 'w').writelines(lines)\nprint('Done')\n\""
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-22T18:59:41.564015+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Done\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T18:59:41.564143+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat -n /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat -n /root/symb_invariant_consensus/scripts/eval_finetuned_nli.py"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-22T18:59:41.564439+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t#!/usr/bin/env python3\\n     2\\t\\\"\\\"\\\"Evaluate fine-tuned DeBERTa on ProofWriter depth-5 test set.\\n     3\\tStandalone accuracy + combo with LLM SC votes.\\n     4\\t\\n     5\\tUsage:\\n     6\\t    python scripts/eval_finetuned_nli.py \\\\\\n     7\\t        --model-path checkpoints/deberta-large-pw-finetuned/best\\n     8\\t    python scripts/eval_finetuned_nli.py \\\\\\n     9\\t        --model-path /root/autodl-tmp/models/deberta-large-mnli \\\\\\n    10\\t        --sc-sources llama8b qwen14b mistral\\n    11\\t\\\"\\\"\\\"\\n    12\\t\\n    13\\t# Environment setup for westd-16639:\\n    14\\t#   export CUDA_VISIBLE_DEVICES=&lt;free_gpu_id>\\n    15\\t#   export LD_LIBRARY_PATH=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib:$LD_LIBRARY_PATH\\n    16\\t\\n    17\\t\\n    18\\timport argparse\\n    19\\timport json\\n    20\\timport os\\n    21\\timport time\\n    22\\tfrom collections import Counter\\n    23\\timport numpy as np\\n    24\\timport torch\\n    25\\tfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\n    26\\tfrom scipy.stats import binomtest\\n    27\\t\\n    28\\tPW_DATA_PATH = \\\"/root/symb_invariant_consensus/data/proofwriter_full.json\\\"\\n    29\\tRESULTS_DIR = \\\"/root/symb_invariant_consensus/results\\\"\\n    30\\tCLASSES = sorted([\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"])\\n    31\\tWEIGHTS = [1, 3, 5]\\n    32\\t\\n    33\\tSC_SOURCES = {\\n    34\\t    \\\"llama8b\\\": {\\n    35\\t        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp048_llama8b_pw600/exp048_results.json\\\"),\\n    36\\t        \\\"name\\\": \\\"LLaMA-3.1-8B-Instruct\\\",\\n    37\\t        \\\"format\\\": \\\"results_list\\\",\\n    38\\t    },\\n    39\\t    \\\"qwen14b\\\": {\\n    40\\t        \\\"path\\\": os.path.join(RESULTS_DIR, \\\"exp032_qwen25_14b_pw600/results.json\\\"),\\n    41\\t        \\\"name\\\": \\\"Qwen2.5-14B-Instruct\\\",\\n 
…[truncated 7615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-22T18:59:41.564638+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && python3 -c \"\nlines = open('scripts/eval_finetuned_nli.py').readlines()\n# Remove lines 55-59 (0-indexed 54-58)\ndel lines[54:59]\nopen('scripts/eval_finetuned_nli.py', 'w').writelines(lines)\nprint('Done')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cd /root/symb_invariant_consensus && python3 -c \"\nlines = open('scripts/eval_finetuned_nli.py').readlines()\n# Remove lines 55-59 (0-indexed 54-58)\ndel lines[54:59]\nopen('scripts/eval_finetuned_nli.py', 'w').writelines(lines)\nprint('Done')\n\""
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T18:59:41.564774+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Done\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-22T18:59:41.564946+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && python3 -c \"import ast; ast.parse(open('scripts/eval_finetuned_nli.py').read()); print('Syntax OK')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cd /root/symb_invariant_consensus && python3 -c \"import ast; ast.parse(open('scripts/eval_finetuned_nli.py').read()); print('Syntax OK')\""
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-22T18:59:41.565077+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Syntax OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-22T18:59:41.565197+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport scripts.eval_finetuned_nli as m\nfor k, v in m.SC_SOURCES.items():\n    import os\n    exists = os.path.exists(v['path'])\n    print(f'{k}: {v[\\\"name\\\"]} -> exists={exists}')\nprint('CLASSES:', m.CLASSES)\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport scripts.eval_finetuned_nli as m\nfor k, v in m.SC_SOURCES.items():\n    import os\n    exists = os.path.exists(v['path'])\n    print(f'{k}: {v[\\\"name\\\"]} -> exists={exists}')\nprint('CLASSES:', m.CLASSES)\n\""
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-22T18:59:41.565322+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"llama8b: LLaMA-3.1-8B-Instruct -> exists=True\\nqwen14b: Qwen2.5-14B-Instruct -> exists=True\\nmistral: Mistral-7B-Instruct-v0.3 -> exists=True\\nqwen3_14b: Qwen3-14B (non-thinking) -> exists=True\\nCLASSES: ['False', 'True', 'Unknown']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.05}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-22T18:59:41.565477+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total --format=csv,noheader"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-22T18:59:41.565604+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 MiB, 97887 MiB\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 88263 MiB, 97887 MiB\\n2, NVIDIA RTX PRO 6000 Blackwell Server Edition, 90213 MiB, 97887 MiB\\n3, NVIDIA RTX PRO 6000 Blackwell Server Edition, 88263 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-22T18:59:41.565740+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_LIBRARY_PATH=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib:$LD_LIBRARY_PATH && export CUDA_VISIBLE_DEVICES=0 && python scripts/eval_finetuned_nli.py --model-path /root/autodl-tmp/symb_invariant_consensus/models/deberta-large-pw-owa/best --sc-sources qwen14b qwen3_14b --weights 1 3 5 --output-dir results/eval_finetuned_qwen_combo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_LIBRARY_PATH=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib:$LD_LIBRARY_PATH && export CUDA_VISIBLE_DEVICES=0 && python scripts/eval_finetuned_nli.py --model-path /root/autodl-tmp/symb_invariant_consensus/models/deberta-large-pw-owa/best --sc-sources qwen14b qwen3_14b --weights 1 3 5 --output-dir results/eval_finetuned_qwen_combo"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-22T18:59:41.565908+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading model: /root/autodl-tmp/symb_invariant_consensus/models/deberta-large-pw-owa/best\\nDevice: cuda:0, id2label: {0: 'CONTRADICTION', 1: 'NEUTRAL', 2: 'ENTAILMENT'}\\nNLI->PW: {0: 'False', 1: 'Unknown', 2: 'True'}\\nLoaded 600 problems\\n\\nRunning NLI inference...\\n  600/600\\nInference: 3.6s (164.8 samples/s)\\n\\n=== Standalone: 0.9967 (598/600) ===\\n  False: 200/200 = 1.0000 (P=0.9901 R=1.0000 F1=0.9950)\\n  True: 200/200 = 1.0000 (P=1.0000 R=1.0000 F1=1.0000)\\n  Unknown: 198/200 = 0.9900 (P=1.0000 R=0.9900 F1=0.9950)\\n  Pred dist: {'True': 200, 'False': 202, 'Unknown': 198}\\n\\n=== Combo: Qwen2.5-14B-Instruct (SC=0.7400) ===\\n  NLI↑SC↓=155, SC↑NLI↓=1, both↑=443, both↓=1\\n  w=1: 0.7500 (450/600), delta=+1.00pp, p=0.0312 *\\n  w=3: 0.7850 (471/600), delta=+4.50pp, p=0.0000 ***\\n  w=5: 0.8300 (498/600), delta=+9.00pp, p=0.0000 ***\\n  Agree: 443/600 (0.7383), acc when agree=1.0000\\n  Disagree: 157, NLI right=155, SC right=1\\n\\n=== Combo: Qwen3-14B (non-thinking) (SC=0.8583) ===\\n  NLI↑SC↓=85, SC↑NLI↓=2, both↑=513, both↓=0\\n  w=1: 0.8650 (519/600), delta=+0.67pp, p=0.1250 \\n  w=3: 0.8800 (528/600), delta=+2.17pp, p=0.0002 ***\\n  w=5: 0.9000 (540/600), delta=+4.17pp, p=0.0000 ***\\n  Agree: 513/600 (0.8550), acc when agree=1.0000\\n  Disagree: 87, NLI right=85, SC right=2\\n\\nSaved: results/eval_finetuned_qwen_combo/results.json\\n\", \"stderr\": \"\\rLoading weights:   0%|          | 0/392 [00:00<?, ?it/s]\\rLoading weights: 100%|██████████| 392/392 [00:00<00:00, 12155.43it/s]\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.23}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-22T18:59:41.566097+00:00_

实验完成。结果汇总：

### DeBERTa-large-FT Standalone: **99.67%** (598/600)

---

### Qwen2.5-14B-Instruct
- **SC baseline**: 74.00% (444/600)
- **Combo w=1**: 75.00% (+1.00pp, p=0.0312 \*)
- **Combo w=3**: 78.50% (+4.50pp, p<0.0001 \*\*\*)
- **Combo w=5**: 83.00% (+9.00pp, p<0.0001 \*\*\*)
- **互补性**: NLI↑SC↓=155, SC↑NLI↓=1, both↑=443, both↓=1
- Agreement 时 acc=100%

### Qwen3-14B (non-thinking)
- **SC baseline**: 85.83% (515/600)
- **Combo w=1**: 86.50% (+0.67pp, p=0.1250 n.s.)
- **Combo w=3**: 88.00% (+2.17pp, p=0.0002 \*\*\*)
- **Combo w=5**: 90.00% (+4.17pp, p<0.0001 \*\*\*)
- **互补性**: NLI↑SC↓=85, SC↑NLI↓=2, both↑=513, both↓=0
- Agreement 时 acc=100%

Qwen3 thinking mode 在 ProofWriter 上无 traces，仅有 FOLIO 的 (`exp028b_qwen3_thinking_folio204`)。

结果已保存至 `results/eval_finetuned_qwen_combo/results.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_qwen-deberta-ft-combo_20260522T185637"
}
```

</details>

---
