# ops prepare qwen14b d050 eval scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618.jsonl`
- **Structured JSON:** [`a8a28835f16d6ac0b65b.json`](../../sessions/a8/a8a28835f16d6ac0b65b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-21T03:37:00.450833+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T03:37:00.451393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T03:37:00.451782+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "mkdir -p /root/contamcal-irt-calibration/scripts/seed0 && cat > /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_mmlu.sh << 'SCRIPT_EOF'\n#!/bin/bash\nset -euo pipefail\nexport HF_DATASETS_OFFLINE=1\nexport HF_HOME=/root/autodl-tmp/.hf_cache\n\nsource /root/miniconda3/bin/activate base\ncd /root/contamcal-irt-calibration\n\n# Adapter path detection\nADAPTER_BASE=\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s0\"\nif [ -f \"${ADAPTER_BASE}/lora_adapter/adapter_model.safetensors\" ]; then\n    ADAPTER=\"${ADAPTER_BASE}/lora_adapter\"\nelif [ -f \"${ADAPTER_BASE}/adapter_model.safetensors\" ]; then\n    ADAPTER=\"${ADAPTER_BASE}\"\nelse\n    echo \"ERROR: adapter not found at ${ADAPTER_BASE}\"; exit 1\nfi\n\n# C006 verify\nALPHA=$(python3 -c \"import json; c=json.load(open('${ADAPTER}/adapter_config.json')); print(c.get('lora_alpha', 'MISSING'))\")\necho \"lora_alpha=${ALPHA}\"\nif [ \"$ALPHA\" != \"32\" ]; then echo \"ERROR: lora_alpha != 32\"; exit 1; fi\n\npython evaluate.py \\\n    --model Qwen/Qwen2.5-14B \\\n    --adapter-path \"${ADAPTER}\" \\\n    --benchmark mmlu \\\n    --shots 5 \\\n    --output-dir results/qwen14b_d050_s0_mmlu \\\n    --batch-size 2\n\necho \"DONE: Qwen-14B d050 s0 MMLU eval\"\nSCRIPT_EOF\nchmod +x /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_mmlu.sh\necho \"MMLU script created\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "mkdir -p /root/contamcal-irt-calibration/scripts/seed0 && cat > /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_mmlu.sh << 'SCRIPT_EOF'\n#!/bin/bash\nset -euo pipefail\nexport HF_DATASETS_OFFLINE=1\nexport HF_HOME=/root/autodl-tmp/.hf_cache\n\nsource /root/miniconda3/bin/activate base\ncd /root/contamcal-irt-calibration\n\n# Adapter path detection\nADAPTER_BASE=\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s0\"\nif [ -f \"${ADAPTER_BASE}/lora_adapter/adapter_model.safetensors\" ]; then\n    ADAPTER=\"${ADAPTER_BASE}/lora_adapter\"\nelif [ -f \"${ADAPTER_BASE}/adapter_model.safetensors\" ]; then\n    ADAPTER=\"${ADAPTER_BASE}\"\nelse\n    echo \"ERROR: adapter not found at ${ADAPTER_BASE}\"; exit 1\nfi\n\n# C006 verify\nALPHA=$(python3 -c \"import json; c=json.load(open('${ADAPTER}/adapter_config.json')); print(c.get('lora_alpha', 'MISSING'))\")\necho \"lora_alpha=${ALPHA}\"\nif [ \"$ALPHA\" != \"32\" ]; then echo \"ERROR: lora_alpha != 32\"; exit 1; fi\n\npython evaluate.py \\\n    --model Qwen/Qwen2.5-14B \\\n    --adapter-path \"${ADAPTER}\" \\\n    --benchmark mmlu \\\n    --shots 5 \\\n    --output-dir results/qwen14b_d050_s0_mmlu \\\n    --batch-size 2\n\necho \"DONE: Qwen-14B d050 s0 MMLU eval\"\nSCRIPT_EOF\nchmod +x /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_mmlu.sh\necho \"MMLU script created\""
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T03:37:00.452064+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"MMLU script created\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T03:37:00.452352+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "cat > /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_arc.sh << 'SCRIPT_EOF'\n#!/bin/bash\nset -euo pipefail\nexport HF_DATASETS_OFFLINE=1\nexport HF_HOME=/root/autodl-tmp/.hf_cache\n\nsource /root/miniconda3/bin/activate base\ncd /root/contamcal-irt-calibration\n\n# Adapter path detection\nADAPTER_BASE=\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s0\"\nif [ -f \"${ADAPTER_BASE}/lora_adapter/adapter_model.safetensors\" ]; then\n    ADAPTER=\"${ADAPTER_BASE}/lora_adapter\"\nelif [ -f \"${ADAPTER_BASE}/adapter_model.safetensors\" ]; then\n    ADAPTER=\"${ADAPTER_BASE}\"\nelse\n    echo \"ERROR: adapter not found at ${ADAPTER_BASE}\"; exit 1\nfi\n\n# C006 verify\nALPHA=$(python3 -c \"import json; c=json.load(open('${ADAPTER}/adapter_config.json')); print(c.get('lora_alpha', 'MISSING'))\")\necho \"lora_alpha=${ALPHA}\"\nif [ \"$ALPHA\" != \"32\" ]; then echo \"ERROR: lora_alpha != 32\"; exit 1; fi\n\npython evaluate.py \\\n    --model Qwen/Qwen2.5-14B \\\n    --adapter-path \"${ADAPTER}\" \\\n    --benchmark arc_challenge \\\n    --shots 25 \\\n    --output-dir results/qwen14b_d050_s0_arc \\\n    --batch-size 2\n\necho \"DONE: Qwen-14B d050 s0 ARC eval\"\nSCRIPT_EOF\nchmod +x /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_arc.sh\necho \"ARC script created\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat > /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_arc.sh << 'SCRIPT_EOF'\n#!/bin/bash\nset -euo pipefail\nexport HF_DATASETS_OFFLINE=1\nexport HF_HOME=/root/autodl-tmp/.hf_cache\n\nsource /root/miniconda3/bin/activate base\ncd /root/contamcal-irt-calibration\n\n# Adapter path detection\nADAPTER_BASE=\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s0\"\nif [ -f \"${ADAPTER_BASE}/lora_adapter/adapter_model.safetensors\" ]; then\n    ADAPTER=\"${ADAPTER_BASE}/lora_adapter\"\nelif [ -f \"${ADAPTER_BASE}/adapter_model.safetensors\" ]; then\n    ADAPTER=\"${ADAPTER_BASE}\"\nelse\n    echo \"ERROR: adapter not found at ${ADAPTER_BASE}\"; exit 1\nfi\n\n# C006 verify\nALPHA=$(python3 -c \"import json; c=json.load(open('${ADAPTER}/adapter_config.json')); print(c.get('lora_alpha', 'MISSING'))\")\necho \"lora_alpha=${ALPHA}\"\nif [ \"$ALPHA\" != \"32\" ]; then echo \"ERROR: lora_alpha != 32\"; exit 1; fi\n\npython evaluate.py \\\n    --model Qwen/Qwen2.5-14B \\\n    --adapter-path \"${ADAPTER}\" \\\n    --benchmark arc_challenge \\\n    --shots 25 \\\n    --output-dir results/qwen14b_d050_s0_arc \\\n    --batch-size 2\n\necho \"DONE: Qwen-14B d050 s0 ARC eval\"\nSCRIPT_EOF\nchmod +x /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_arc.sh\necho \"ARC script created\""
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T03:37:00.459130+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "tail -10 /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "tail -10 /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T03:37:00.459425+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ARC script created\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 7
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T03:37:00.459738+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': '0.8423', 'grad_norm': '0.3033', 'learning_rate': '1.619e-05', 'entropy': '0.9717', 'num_tokens': '1.313e+07', 'mean_token_accuracy': '0.7777', 'epoch': '0.6343'}\\n{'loss': '1.014', 'grad_norm': '0.2759', 'learning_rate': '1.598e-05', 'entropy': '1.022', 'num_tokens': '1.318e+07', 'mean_token_accuracy': '0.7736', 'epoch': '0.6371'}\\n{'loss': '0.861', 'grad_norm': '0.3043', 'learning_rate': '1.577e-05', 'entropy': '0.9767', 'num_tokens': '1.323e+07', 'mean_token_accuracy': '0.778', 'epoch': '0.6398'}\\n{'loss': '0.9411', 'grad_norm': '0.3674', 'learning_rate': '1.556e-05', 'entropy': '1.005', 'num_tokens': '1.329e+07', 'mean_token_accuracy': '0.768', 'epoch': '0.6426'}\\n{'loss': '0.9423', 'grad_norm': '0.3127', 'learning_rate': '1.535e-05', 'entropy': '0.9841', 'num_tokens': '1.335e+07', 'mean_token_accuracy': '0.7725', 'epoch': '0.6453'}\\n{'loss': '0.8847', 'grad_norm': '1.492', 'learning_rate': '1.514e-05', 'entropy': '0.968', 'num_tokens': '1.341e+07', 'mean_token_accuracy': '0.783', 'epoch': '0.6481'}\\n{'loss': '1.016', 'grad_norm': '0.2985', 'learning_rate': '1.493e-05', 'entropy': '1.093', 'num_tokens': '1.346e+07', 'mean_token_accuracy': '0.7563', 'epoch': '0.6508'}\\n{'loss': '0.9124', 'grad_norm': '0.2525', 'learning_rate': '1.472e-05', 'entropy': '1.005', 'num_tokens': '1.352e+07', 'mean_token_accuracy': '0.7733', 'epoch': '0.6536'}\\n{'loss': '0.9576', 'grad_norm': '0.3808', 'learning_rate': '1.452e-05', 'entropy': '1.015', 'num_tokens': '1.357e+07', 'mean_token_accuracy': '0.7713', 'epoch': '0.6563'}\\n\\r 66%|██████▌   | 2400/3642 [3:18:04<1:37:42,  4.72s/it]\\r 66%|██████▌   | 2401/3642 [3:18:09<1:38:03,  4.74s/it]\\r 66%|██████▌   | 2402/3642 [3:18:15<1:41:46,  4.92s/it]\\r 66%|██████▌   | 2403/3642 [3:18:20<1:44:59,  5.08s/it]\\r 66%|██████▌   | 2404/3642 [3:18:25<1:42:44,  4.98s/it]\\r 66%|██████▌   | 2405/3642 [3:18:30<1:41:57,  4.95s/it]\\r 66%|██████▌   | 2406/3642 [3:18:35<1:45
…[truncated 4375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T03:37:00.460034+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls -la /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_mmlu.sh /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_arc.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls -la /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_mmlu.sh /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_arc.sh"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T03:37:00.460273+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rwxr-xr-x 1 root root 1038 May 21 11:36 /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_arc.sh\\n-rwxr-xr-x 1 root root 1030 May 21 11:36 /root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_mmlu.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T03:37:00.507056+00:00_

产出：

**脚本路径：**
- MMLU: `/root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_mmlu.sh`
- ARC: `/root/contamcal-irt-calibration/scripts/seed0/eval_qwen14b_d050_s0_arc.sh`

两个脚本均已 `chmod +x`，包含 adapter 路径自动检测和 C006 lora_alpha=32 校验。

**Retrain 进度：**
- 2467/3642 steps（67.7%）
- 速度 ~4.9s/step
- 剩余 1175 steps，预计 **~1h36min** 后完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_prepare-qwen14b-d050-eval-scripts_20260521T033618"
}
```

</details>

---
