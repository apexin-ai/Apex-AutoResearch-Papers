# eval exp 028 qwen3 thinking

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_eval_exp-028-qwen3-thinking_20260518T140432.jsonl`
- **Structured JSON:** [`0b23edb24420d04ab195.json`](../../sessions/0b/0b23edb24420d04ab195.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-18T14:05:25.939705+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T14:05:25.940134+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T14:05:25.940319+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/.cache -name \"*Qwen3*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/.cache -name \"*Qwen3*\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T14:05:25.940455+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T14:05:25.940581+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/scripts/"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T14:05:25.940701+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "nvidia-smi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "nvidia-smi"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T14:05:25.940828+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"cross_model_extract.py\\npostprocess_case_study.py\\nrun_case_study_extract.sh\\nrun_cross_model_mistral.sh\\nrun_exp024_llama70b.sh\\nrun_exp025_qwen72b.sh\\nrun_folio_trace_regen.sh\\nrun_qwen3_14b_nonthinking.sh\\nrun_qwen3_14b_thinking.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T14:05:25.941011+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Mon May 18 22:04:52 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:16:00.0 Off |                  Off |\\n| N/A   54C    P0            334W /  600W |   88241MiB /  97887MiB |     97%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:49:00.0 Off |                  Off |\\n| N/A   26C    P8             33W /  600W |       3MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |\\n| N/A   26C    P8             33W /  600W |       3MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:B8:00.0 Off |                  Off |\\n| N/A   32C    P0            1
…[truncated 1017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T14:05:25.941190+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/scripts/run_qwen3_14b_thinking.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/scripts/run_qwen3_14b_thinking.sh"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T14:05:25.941316+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/scripts/run_qwen3_14b_nonthinking.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/scripts/run_qwen3_14b_nonthinking.sh"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T14:05:25.941522+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\n# exp-028: Qwen3-14B (thinking mode) SICA vs SC on FOLIO(204)\\n# Tests whether native reasoning (thinking mode) improves constraint quality\\n# Server: westd-25068, GPU 2, K=12, T=0.7, seed=42\\n#\\n# Qwen3 thinking mode: model generates &lt;think>...&lt;/think> before answering.\\n# vLLM reasoning-parser strips thinking from response content.\\n# max-model-len=16384 to accommodate thinking tokens.\\n# max-tokens=8192 to allow longer generation (thinking + answer).\\n\\nset -e\\ncd /root/symb_invariant_consensus\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\n\\n# ── Config ──────────────────────────────────────────────────────\\nMODEL=\\\"/root/autodl-tmp/models/Qwen3-14B\\\"\\nPORT=8002\\nGPU_ID=2\\nK=12\\nTEMPERATURE=0.7\\nMAX_TOKENS=8192\\nSEED=42\\nRESULTS_DIR=\\\"results/exp028_qwen3_14b_thinking\\\"\\nmkdir -p \\\"$RESULTS_DIR\\\"\\n\\necho \\\"=== [$(date)] exp-028: Qwen3-14B (thinking mode) SICA vs SC ===\\\"\\necho \\\"Model: $MODEL\\\"\\necho \\\"GPU: $GPU_ID, Port: $PORT\\\"\\necho \\\"K=$K, T=$TEMPERATURE, max_tokens=$MAX_TOKENS, seed=$SEED\\\"\\necho \\\"Data: folio_full.json (204 problems)\\\"\\necho \\\"Mode: THINKING enabled (native reasoning)\\\"\\n\\n# ── Pre-flight checks ──────────────────────────────────────────\\necho \\\"\\\"\\necho \\\"=== Pre-flight checks ===\\\"\\n\\nif [ ! -d \\\"$MODEL\\\" ]; then\\n    echo \\\"ERROR: Model not found: $MODEL\\\"\\n    exit 1\\nfi\\necho \\\"Model dir: OK\\\"\\n\\nSHARD_COUNT=$(ls \\\"$MODEL\\\"/model-*.safetensors 2>/dev/null | wc -l)\\necho \\\"Model shards: $SHARD_COUNT\\\"\\nif [ \\\"$SHARD_COUNT\\\" -lt 8 ]; then\\n    echo \\\"ERROR: Expected 8 safetensor shards, found $SHARD_COUNT. Download may be incomplete.\\\"\\n    exit 1\\nfi\\n\\nfor f in data/folio_full.json data/empty.json; do\\n    if [ ! -f \\\"$f\\\" ]; then\\n        echo \\\"ERROR: Data file not found: $f\\\"\\n        exit 1\\n    fi\\ndone\\n
…[truncated 3321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T14:05:25.941755+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\n# exp-027: Qwen3-14B (non-thinking) SICA vs SC on FOLIO(204)\\n# Generational comparison with exp-026 (Qwen2.5-14B)\\n# Server: westd-25068, GPU 1, K=12, T=0.7, T_ext=0.3, seed=42\\n#\\n# Purpose: Test whether capability trap persists on next-gen Qwen3-14B\\n# Non-thinking mode: disable Qwen3 native reasoning for fair comparison with Qwen2.5-14B\\n\\nset -e\\ncd /root/symb_invariant_consensus\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\n\\n# ── Config ──────────────────────────────────────────────────────\\nMODEL=\\\"/root/autodl-tmp/models/Qwen3-14B\\\"\\nPORT=8001\\nGPU_ID=1\\nK=12\\nTEMPERATURE=0.7\\nMAX_TOKENS=4096\\nSEED=42\\nRESULTS_DIR=\\\"results/exp027_qwen3_14b_nonthinking\\\"\\nmkdir -p \\\"$RESULTS_DIR\\\"\\n\\necho \\\"=== [$(date)] exp-027: Qwen3-14B (non-thinking) SICA vs SC ===\\\"\\necho \\\"Model: $MODEL\\\"\\necho \\\"GPU: $GPU_ID, Port: $PORT\\\"\\necho \\\"K=$K, T=$TEMPERATURE, max_tokens=$MAX_TOKENS, seed=$SEED\\\"\\necho \\\"Data: folio_full.json (204 problems)\\\"\\n\\n# ── Pre-flight checks ──────────────────────────────────────────\\necho \\\"\\\"\\necho \\\"=== Pre-flight checks ===\\\"\\n\\nif [ ! -d \\\"$MODEL\\\" ]; then\\n    echo \\\"ERROR: Model not found: $MODEL\\\"\\n    exit 1\\nfi\\necho \\\"Model dir: OK\\\"\\n\\nSHARD_COUNT=$(ls \\\"$MODEL\\\"/model-*.safetensors 2>/dev/null | wc -l)\\necho \\\"Model shards: $SHARD_COUNT\\\"\\nif [ \\\"$SHARD_COUNT\\\" -lt 8 ]; then\\n    echo \\\"ERROR: Expected 8 safetensor shards, found $SHARD_COUNT. Download may be incomplete.\\\"\\n    exit 1\\nfi\\n\\nfor f in data/folio_full.json data/empty.json; do\\n    if [ ! -f \\\"$f\\\" ]; then\\n        echo \\\"ERROR: Data file not found: $f\\\"\\n        exit 1\\n    fi\\ndone\\necho \\\"Data files: OK\\\"\\n\\nGPU_MEM=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits -i $GPU_ID 2>/dev/null | tr -d ' ')\\necho \\\"GPU $GPU_ID memor
…[truncated 2985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T14:05:25.941930+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/.cache/modelscope/hub/Qwen/Qwen3-14B/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/.cache/modelscope/hub/Qwen/Qwen3-14B/"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T14:05:25.942068+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/.cache/modelscope/hub/Qwen/Qwen3-14B/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T14:05:25.942510+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/autodl-tmp/models/Qwen3-14B/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/autodl-tmp/models/Qwen3-14B/"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T14:05:25.942769+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"LICENSE\\nREADME.md\\nconfig.json\\nconfiguration.json\\ngeneration_config.json\\nmerges.txt\\nmodel-00001-of-00008.safetensors\\nmodel-00002-of-00008.safetensors\\nmodel-00003-of-00008.safetensors\\nmodel-00004-of-00008.safetensors\\nmodel-00005-of-00008.safetensors\\nmodel-00006-of-00008.safetensors\\nmodel-00007-of-00008.safetensors\\nmodel-00008-of-00008.safetensors\\nmodel.safetensors.index.json\\ntokenizer.json\\ntokenizer_config.json\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T14:05:25.943025+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "westd-25068",
  "gpu_ids": "['cuda:2']",
  "exp_id": "exp-028-qwen3-14b-thinking",
  "command": "bash -c \"source /root/miniconda3/bin/activate && bash /root/symb_invariant_consensus/scripts/run_qwen3_14b_thinking.sh\"",
  "project": "symb_invariant_consensus",
  "timeout_hours": "24"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "westd-25068",
    "gpu_ids": "['cuda:2']",
    "exp_id": "exp-028-qwen3-14b-thinking",
    "command": "bash -c \"source /root/miniconda3/bin/activate && bash /root/symb_invariant_consensus/scripts/run_qwen3_14b_thinking.sh\"",
    "project": "symb_invariant_consensus",
    "timeout_hours": "24"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T14:05:25.943268+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"35447\", \"log_file\": \"~/runs/symb_invariant_consensus/exp-028-qwen3-14b-thinking.log\", \"gpu_ids\": [\"cuda:2\"], \"server\": \"westd-25068\", \"account\": \"root\", \"cuda_visible_devices\": \"2\", \"backend\": \"tmux\", \"tmux_session\": \"exp-028-qwen3-14b-thinking\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T14:05:25.943427+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "tail -30 /root/runs/symb_invariant_consensus/exp-028-qwen3-14b-thinking.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "tail -30 /root/runs/symb_invariant_consensus/exp-028-qwen3-14b-thinking.log"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T14:05:25.943566+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\nError while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n=== [Mon May 18 22:05:13 CST 2026] exp-028: Qwen3-14B (thinking mode) SICA vs SC ===\\nModel: /root/autodl-tmp/models/Qwen3-14B\\nGPU: 2, Port: 8002\\nK=12, T=0.7, max_tokens=8192, seed=42\\nData: folio_full.json (204 problems)\\nMode: THINKING enabled (native reasoning)\\n\\n=== Pre-flight checks ===\\nModel dir: OK\\nModel shards: 8\\nData files: OK\\nGPU 2 memory used: 3 MiB\\nPort 8002: free\\n\\n=== [Mon May 18 22:05:14 CST 2026] Starting vLLM on GPU 2, port 8002 (thinking mode) ===\\nNOTE: max-model-len=16384 for thinking token overhead\\nvLLM PID: 35471\\nWaiting for vLLM to be ready...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-18T14:05:25.943735+00:00_

Pre-flight 全部通过，vLLM 正在启动中。

**报告：**

| 项目 | 状态 |
|------|------|
| Qwen3-14B 模型 | `/root/autodl-tmp/models/Qwen3-14B`，8 分片完整 |
| Thinking mode 配置 | vLLM `--reasoning-parser qwen3`，默认启用 thinking，max-model-len=16384，max-tokens=8192 |
| 脚本路径 | `/root/symb_invariant_consensus/scripts/run_qwen3_14b_thinking.sh` |
| PID | 35447，tmux session: `exp-028-qwen3-14b-thinking` |
| GPU | cuda:2 (3 MiB used, clean)，端口 8002 |
| 状态 | vLLM 加载中，pre-flight checks 全部通过 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_exp-028-qwen3-thinking_20260518T140432"
}
```

</details>

---
