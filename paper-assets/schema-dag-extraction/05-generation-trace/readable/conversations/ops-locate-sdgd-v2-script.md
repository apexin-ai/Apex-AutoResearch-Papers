# ops locate sdgd v2 script

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_ops_locate_sdgd_v2_script_20260515T134131.jsonl`
- **Structured JSON:** [`f70141871cb2579a22f2.json`](../../sessions/f7/f70141871cb2579a22f2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-15T13:42:15.598335+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T13:42:15.598660+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T13:42:15.598827+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "account": "root",
  "command": "find /root/schema-dag-extraction -name \"*sdgd*v2*\" -o -name \"*run_sdgd_v2*\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "account": "root",
    "command": "find /root/schema-dag-extraction -name \"*sdgd*v2*\" -o -name \"*run_sdgd_v2*\" -type f 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T13:42:15.598999+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T13:42:15.599138+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "account": "root",
  "command": "find /root/schema-dag-extraction -name \"*exp012*\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "account": "root",
    "command": "find /root/schema-dag-extraction -name \"*exp012*\" -type f 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T13:42:15.599265+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T13:42:15.599386+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "account": "root",
  "command": "nvidia-smi --query-gpu=name,memory.used,memory.total,utilization.gpu --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "account": "root",
    "command": "nvidia-smi --query-gpu=name,memory.used,memory.total,utilization.gpu --format=csv,noheader"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T13:42:15.599513+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 MiB, 97887 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.25}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T13:42:15.599651+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "account": "root",
  "command": "find /root/schema-dag-extraction -name \"*sdgd*v2*\" -o -name \"*run_sdgd_v2*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "account": "root",
    "command": "find /root/schema-dag-extraction -name \"*sdgd*v2*\" -o -name \"*run_sdgd_v2*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T13:42:15.599775+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema-dag-extraction/scripts/run_sdgd_v2_fewnerd.sh\\n/root/schema-dag-extraction/scripts/run_sdgd_v2_maven_minilm.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T13:42:15.599915+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "account": "root",
  "command": "find /root/schema-dag-extraction -name \"*exp012*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "account": "root",
    "command": "find /root/schema-dag-extraction -name \"*exp012*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T13:42:15.600052+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema-dag-extraction/scripts/run_exp012_llama.sh\\n/root/schema-dag-extraction/scripts/submit_exp012.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T13:42:15.600189+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "account": "root",
  "command": "cat /root/schema-dag-extraction/scripts/run_sdgd_v2_fewnerd.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "account": "root",
    "command": "cat /root/schema-dag-extraction/scripts/run_sdgd_v2_fewnerd.sh"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T13:42:15.600357+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e\\nsource /root/miniconda3/etc/profile.d/conda.sh\\nconda activate base\\ncd /root/schema-dag-extraction\\n\\nTYPES_FILE=configs/few_nerd_types.json\\nSIM_MATRIX=artifacts/sim_matrix.pt\\nMODEL_PATH=/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\nOUTPUT_DIR=artifacts/exp008_v2\\nMAX_SAMPLES=1000\\nTASK=ner\\nMIN_BATCH_SIZE=8\\nMERGE_STRATEGY=confidence\\nCONFIDENCE_THRESHOLD=-1.0\\n\\nmkdir -p ${OUTPUT_DIR}\\n\\necho \\\"===== [$(date)] SDGD-zero v2 — FewNERD =====\\\"\\necho \\\"  min_batch_size=${MIN_BATCH_SIZE}, merge=${MERGE_STRATEGY}, threshold=${CONFIDENCE_THRESHOLD}\\\"\\n\\n# ========== Stage 1: CPU Decomposition ==========\\necho \\\"===== [$(date)] Stage 1: CPU Decomposition =====\\\"\\n\\nfor MODE in sdgd_zero single_pass random_batch per_type; do\\n  EXTRA_ARGS=\\\"\\\"\\n  if [ \\\"${MODE}\\\" = \\\"sdgd_zero\\\" ]; then\\n    EXTRA_ARGS=\\\"--min_batch_size ${MIN_BATCH_SIZE}\\\"\\n  fi\\n  echo \\\"  Decomposing: ${MODE} ${EXTRA_ARGS}\\\"\\n  python3 src/sdgd_decompose_cpu.py \\\\\\n    --mode ${MODE} \\\\\\n    --types_file ${TYPES_FILE} \\\\\\n    --sim_matrix_path ${SIM_MATRIX} \\\\\\n    --output ${OUTPUT_DIR}/decomposition_${MODE}.json \\\\\\n    ${EXTRA_ARGS}\\ndone\\n\\n# ========== Stage 2: GPU Extraction ==========\\necho \\\"===== [$(date)] Stage 2: GPU Extraction (confidence merge) =====\\\"\\n\\npython3 src/sdgd_extract_gpu.py \\\\\\n  --decompositions \\\\\\n    ${OUTPUT_DIR}/decomposition_sdgd_zero.json \\\\\\n    ${OUTPUT_DIR}/decomposition_single_pass.json \\\\\\n    ${OUTPUT_DIR}/decomposition_random_batch.json \\\\\\n    ${OUTPUT_DIR}/decomposition_per_type.json \\\\\\n  --model_path ${MODEL_PATH} \\\\\\n  --types_file ${TYPES_FILE} \\\\\\n  --dataset fewnerd \\\\\\n  --prompt_version v2 \\\\\\n  --max_samples ${MAX_SAMPLES} \\\\\\n  --output_dir ${OUTPUT_DIR} \\\\\\n  --max_model_len 4096 \\\\\\n  --task ${TASK} \\\\\\n  --merge_strategy ${MERGE_STRATEGY} \\\\\\n
…[truncated 204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T13:42:15.600503+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "account": "root",
  "command": "cat /root/schema-dag-extraction/scripts/run_sdgd_v2_maven_minilm.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "account": "root",
    "command": "cat /root/schema-dag-extraction/scripts/run_sdgd_v2_maven_minilm.sh"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:42:15.600663+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e\\nsource /root/miniconda3/etc/profile.d/conda.sh\\nconda activate base\\ncd /root/schema-dag-extraction\\n\\nTYPES_FILE=configs/maven_event_types.json\\nSIM_MATRIX=artifacts/maven_minilm_sim_matrix.pt\\nMODEL_PATH=/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\nOUTPUT_DIR=artifacts/exp008_v2_maven_minilm\\nMAX_SAMPLES=1000\\nTASK=event\\nMIN_BATCH_SIZE=8\\nMERGE_STRATEGY=confidence\\nCONFIDENCE_THRESHOLD=-1.0\\n\\nmkdir -p ${OUTPUT_DIR}\\n\\necho \\\"===== [$(date)] SDGD-zero v2 — MAVEN (MiniLM) =====\\\"\\necho \\\"  min_batch_size=${MIN_BATCH_SIZE}, merge=${MERGE_STRATEGY}, threshold=${CONFIDENCE_THRESHOLD}\\\"\\n\\n# ========== Stage 1: CPU Decomposition ==========\\necho \\\"===== [$(date)] Stage 1: CPU Decomposition =====\\\"\\n\\nfor MODE in sdgd_zero single_pass random_batch per_type; do\\n  EXTRA_ARGS=\\\"\\\"\\n  if [ \\\"${MODE}\\\" = \\\"sdgd_zero\\\" ]; then\\n    EXTRA_ARGS=\\\"--min_batch_size ${MIN_BATCH_SIZE}\\\"\\n  fi\\n  echo \\\"  Decomposing: ${MODE} ${EXTRA_ARGS}\\\"\\n  python3 src/sdgd_decompose_cpu.py \\\\\\n    --mode ${MODE} \\\\\\n    --types_file ${TYPES_FILE} \\\\\\n    --sim_matrix_path ${SIM_MATRIX} \\\\\\n    --output ${OUTPUT_DIR}/decomposition_${MODE}.json \\\\\\n    ${EXTRA_ARGS}\\ndone\\n\\n# ========== Stage 2: GPU Extraction ==========\\necho \\\"===== [$(date)] Stage 2: GPU Extraction (confidence merge) =====\\\"\\n\\npython3 src/sdgd_extract_gpu.py \\\\\\n  --decompositions \\\\\\n    ${OUTPUT_DIR}/decomposition_sdgd_zero.json \\\\\\n    ${OUTPUT_DIR}/decomposition_single_pass.json \\\\\\n    ${OUTPUT_DIR}/decomposition_random_batch.json \\\\\\n    ${OUTPUT_DIR}/decomposition_per_type.json \\\\\\n  --model_path ${MODEL_PATH} \\\\\\n  --types_file ${TYPES_FILE} \\\\\\n  --dataset maven \\\\\\n  --prompt_version v2 \\\\\\n  --max_samples ${MAX_SAMPLES} \\\\\\n  --output_dir ${OUTPUT_DIR} \\\\\\n  --max_model_len 4096 \\\\\\n  --task ${TASK} \\\\\\n  --merg
…[truncated 240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T13:42:15.600861+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "account": "root",
  "command": "cat /root/schema-dag-extraction/scripts/run_exp012_llama.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "account": "root",
    "command": "cat /root/schema-dag-extraction/scripts/run_exp012_llama.sh"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T13:42:15.601034+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "account": "root",
  "command": "cat /root/schema-dag-extraction/scripts/submit_exp012.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "account": "root",
    "command": "cat /root/schema-dag-extraction/scripts/submit_exp012.sh"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T13:42:15.601172+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e\\nsource /root/miniconda3/etc/profile.d/conda.sh\\nconda activate base\\ncd /root/schema-dag-extraction\\n\\nMODEL=/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/\\nMODEL_NAME=llama-3.3-70b-fp8\\nCOMMON=\\\"--dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json --embeddings_path artifacts/type_embeddings.pt --sim_matrix_path artifacts/sim_matrix.pt --model_path $MODEL --model_name $MODEL_NAME --max_samples 1000 --max_model_len 4096 --gpu_memory_utilization 0.90 --output_dir artifacts/exp012\\\"\\n\\nmkdir -p artifacts/exp012\\n\\necho \\\"===== [$(date)] exp-012 exp1: Count Baseline ($MODEL_NAME) =====\\\"\\npython3 src/run_experiment.py --mode exp1 $COMMON\\n\\necho \\\"===== [$(date)] exp-012 exp2: Confusability Controlled ($MODEL_NAME) =====\\\"\\npython3 src/run_experiment.py --mode exp2 $COMMON\\n\\necho \\\"===== [$(date)] exp-012 DONE =====\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T13:42:15.601311+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\n# One-liner for submit_training_job\\nnohup bash /root/schema-dag-extraction/scripts/run_exp012_llama.sh > /root/schema-dag-extraction/logs/exp012_llama.log 2>&1 &\\necho \\\"exp-012 launched, PID=$!\\\"\\necho \\\"Log: /root/schema-dag-extraction/logs/exp012_llama.log\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-15T13:42:15.601492+00:00_

## 结果

### GPU 状态
| GPU | 显存占用 | 总显存 | 利用率 |
|-----|---------|--------|--------|
| NVIDIA RTX PRO 6000 Blackwell Server Edition | 0 MiB | 97887 MiB | 0% |

GPU 空闲，无任务运行。

---

### `scripts/run_sdgd_v2_fewnerd.sh`

```bash
#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/schema-dag-extraction

TYPES_FILE=configs/few_nerd_types.json
SIM_MATRIX=artifacts/sim_matrix.pt
MODEL_PATH=/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/
OUTPUT_DIR=artifacts/exp008_v2
MAX_SAMPLES=1000
TASK=ner
MIN_BATCH_SIZE=8
MERGE_STRATEGY=confidence
CONFIDENCE_THRESHOLD=-1.0

mkdir -p ${OUTPUT_DIR}

# Stage 1: CPU Decomposition — 4 modes: sdgd_zero, single_pass, random_batch, per_type
for MODE in sdgd_zero single_pass random_batch per_type; do
  EXTRA_ARGS=""
  if [ "${MODE}" = "sdgd_zero" ]; then
    EXTRA_ARGS="--min_batch_size ${MIN_BATCH_SIZE}"
  fi
  python3 src/sdgd_decompose_cpu.py \
    --mode ${MODE} \
    --types_file ${TYPES_FILE} \
    --sim_matrix_path ${SIM_MATRIX} \
    --output ${OUTPUT_DIR}/decomposition_${MODE}.json \
    ${EXTRA_ARGS}
done

# Stage 2: GPU Extraction (confidence merge) — 所有 decomposition 一起送入
python3 src/sdgd_extract_gpu.py \
  --decompositions \
    ${OUTPUT_DIR}/decomposition_sdgd_zero.json \
    ${OUTPUT_DIR}/decomposition_single_pass.json \
    ${OUTPUT_DIR}/decomposition_random_batch.json \
    ${OUTPUT_DIR}/decomposition_per_type.json \
  --model_path ${MODEL_PATH} \
  --types_file ${TYPES_FILE} \
  --dataset fewnerd \
  --prompt_version v2 \
  --max_samples ${MAX_SAMPLES} \
  --output_dir ${OUTPUT_DIR} \
  --max_model_len 4096 \
  --task ${TASK} \
  --merge_strategy ${MERGE_STRATEGY} \
  --confidence_threshold ${CONFIDENCE_THRESHOLD}
```

---

### `scripts/run_sdgd_v2_maven_minilm.sh`

同结构，差异点：
- `TYPES_FILE=configs/maven_event_types.json`
- `SIM_MATRIX=artifacts/maven_minilm_sim_matrix.pt`
- `OUTPUT_DIR=artifacts/exp008_v2_maven_minilm`
- `TASK=event`
- `--dataset maven`

---

### `scripts/run_exp012_llama.sh`

```bash
#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/schema-dag-extraction

MODEL=/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/
MODEL_NAME=llama-3.3-70b-fp8
COMMON="--dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json \
  --embeddings_path artifacts/type_embeddings.pt --sim_matrix_path artifacts/sim_matrix.pt \
  --model_path $MODEL --model_name $MODEL_NAME --max_samples 1000 --max_model_len 4096 \
  --gpu_memory_utilization 0.90 --output_dir artifacts/exp012"

mkdir -p artifacts/exp012

# exp1: Count Baseline
python3 src/run_experiment.py --mode exp1 $COMMON

# exp2: Confusability Controlled
python3 src/run_experiment.py --mode exp2 $COMMON
```

### `scripts/submit_exp012.sh`（启动器）

```bash
#!/bin/bash
nohup bash /root/schema-dag-extraction/scripts/run_exp012_llama.sh \
  > /root/schema-dag-extraction/logs/exp012_llama.log 2>&1 &
echo "exp-012 launched, PID=$!"
```

---

**关键对比**：
- SDGD v2 用 **Qwen3-32B-FP8**，两阶段（CPU decompose → GPU extract），4 种 decomposition mode 对比
- exp-012 用 **LLaMA-3.3-70B-FP8**，统一 `run_experiment.py` 入口，跑 exp1 (count baseline) 和 exp2 (confusability controlled)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_locate_sdgd_v2_script_20260515T134131"
}
```

</details>

---
