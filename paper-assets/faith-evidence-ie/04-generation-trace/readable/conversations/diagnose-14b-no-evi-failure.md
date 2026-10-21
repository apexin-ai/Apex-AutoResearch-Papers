# diagnose 14b no evi failure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_diagnose_14b-no-evi-failure_20260521T004242.jsonl`
- **Structured JSON:** [`a3bf1020e6482724feba.json`](../../sessions/a3/a3bf1020e6482724feba.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-21T00:43:15.421562+00:00_

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
  "session": "worker_diagnose_14b-no-evi-failure_20260521T004242",
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

_source line 2 · 2026-05-21T00:43:15.421911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_14b-no-evi-failure_20260521T004242",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T00:43:15.422081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_no_evidence_eval.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_14b-no-evi-failure_20260521T004242",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_no_evidence_eval.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T00:43:15.422216+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/scripts/plan017/step4b_eval_14b_rsft_no_evidence.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_14b-no-evi-failure_20260521T004242",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/scripts/plan017/step4b_eval_14b_rsft_no_evidence.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T00:43:15.422476+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Step 4b: Eval 14B RSFT (no-evidence) ===\\nBase:    /root/autodl-tmp/models/Qwen/Qwen3-14B\\nSFT:     /root/autodl-tmp/sft_output_14b\\nRSFT:    /root/autodl-tmp/rsft_output_14b\\nOutput:  /root/autodl-tmp/eval_results/plan017_14b_rsft_no_evidence_eval\\nGPUs:    2\\n2026-05-21 05:19:04,134 INFO Detected adapter at /root/autodl-tmp/rsft_output_14b, base: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n2026-05-21 05:19:04,134 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n2026-05-21 05:19:04,511 INFO Loading model: /root/autodl-tmp/models/Qwen/Qwen3-14B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/443 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/443 [00:00<01:22,  5.34it/s]\\rLoading weights:   0%|          | 2/443 [00:00<01:32,  4.77it/s]\\rLoading weights:   3%|▎         | 14/443 [00:00<00:12, 35.30it/s]\\rLoading weights:   6%|▌         | 27/443 [00:00<00:07, 57.60it/s]\\rLoading weights:   9%|▊         | 38/443 [00:00<00:05, 70.66it/s]\\rLoading weights:  11%|█         | 49/443 [00:00<00:04, 79.60it/s]\\rLoading weights:  14%|█▎        | 60/443 [00:00<00:04, 87.64it/s]\\rLoading weights:  16%|█▌        | 71/443 [00:01<00:03, 93.88it/s]\\rLoading weights:  19%|█▊        | 82/443 [00:01<00:03, 98.29it/s]\\rLoading weights:  21%|██        | 94/443 [00:01<00:03, 98.00it/s]\\rLoading weights:  24%|██▍       | 108/443 [00:01<00:03, 109.01it/s]\\rLoading weights:  27%|██▋       | 120/443 [00:01<00:03, 90.24it/s] \\rLoading weights:  31%|███       | 136/443 [00:01<00:03, 96.54it/s]\\rLoading weights:  36%|███▌      | 158/443 [00:01<00:02, 111.46it/s]\\rLoading weights:  38%|███▊      | 170/443 [00:01<00:02, 111.88it/s]\\rLoading weights:  42%|████▏     | 186/443 [00:02<00:02, 121.56it/s]\\rLoading weights:  45%|████▍     | 199/443 [00:02<00:02, 120.61it/s]\\rLoading weights:  48%|████▊     | 213/443 [00:02<00:01, 119.48it/s]\\rLo
…[truncated 6461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_14b-no-evi-failure_20260521T004242",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T00:43:15.422699+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\n# Step 4b: D076 eval for 14B RSFT (no-evidence variant — evidence tax measurement)\\n# Must pass --no_evidence to use NO_EVIDENCE_SYSTEM_PROMPT (C005)\\nset -euo pipefail\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\ncd /root/autodl-tmp/freige\\n\\nexport CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-2,3}}\\nexport HF_HOME=/root/autodl-tmp/.hf_cache\\nexport HF_HUB_OFFLINE=1\\nexport TRANSFORMERS_OFFLINE=1\\n\\nRSFT_ADAPTER=\\\"/root/autodl-tmp/rsft_output_14b\\\"\\nSFT_ADAPTER=\\\"/root/autodl-tmp/sft_output_14b\\\"\\nBASE_MODEL=\\\"/root/autodl-tmp/models/Qwen/Qwen3-14B\\\"\\nOUTPUT_DIR=\\\"/root/autodl-tmp/eval_results/plan017_14b_rsft_no_evidence_eval\\\"\\n\\n# --- Pre-flight checks ---\\nif [ ! -f \\\"${RSFT_ADAPTER}/adapter_config.json\\\" ]; then\\n    echo \\\"ERROR: RSFT adapter not found at ${RSFT_ADAPTER}/adapter_config.json\\\"\\n    echo \\\"Training may not have completed yet. Latest checkpoints:\\\"\\n    ls -d \\\"${RSFT_ADAPTER}\\\"/checkpoint-* 2>/dev/null || echo \\\"  (none)\\\"\\n    exit 1\\nfi\\n\\nif [ ! -f \\\"${SFT_ADAPTER}/adapter_config.json\\\" ]; then\\n    echo \\\"ERROR: SFT adapter not found at ${SFT_ADAPTER}/adapter_config.json\\\"\\n    exit 1\\nfi\\n\\necho \\\"=== Step 4b: Eval 14B RSFT (no-evidence) ===\\\"\\necho \\\"Base:    $BASE_MODEL\\\"\\necho \\\"SFT:     $SFT_ADAPTER\\\"\\necho \\\"RSFT:    $RSFT_ADAPTER\\\"\\necho \\\"Output:  $OUTPUT_DIR\\\"\\necho \\\"GPUs:    $CUDA_VISIBLE_DEVICES\\\"\\n\\npython -m freige.eval.inference \\\\\\n    --model_path \\\"${RSFT_ADAPTER}\\\" \\\\\\n    --base_model \\\"${BASE_MODEL}\\\" \\\\\\n    --sft_adapter \\\"${SFT_ADAPTER}\\\" \\\\\\n    --data_path /root/autodl-tmp/data/docred \\\\\\n    --split dev \\\\\\n    --output_dir \\\"${OUTPUT_DIR}\\\" \\\\\\n    --batch_size 4 \\\\\\n    --max_new_tokens 1024 \\\\\\n    --no-quantize \\\\\\n    --no_evidence \\\\\\n    --seed 42\\n\\nec
…[truncated 139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_14b-no-evi-failure_20260521T004242",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-21T00:43:15.422911+00:00_

**Eval 没有失败——它已成功完成。**

日志显示推理跑完了全部 247 batch（耗时 2h37m），结果已写入：

```
/root/autodl-tmp/eval_results/plan017_14b_rsft_no_evidence_eval/metrics.json
/root/autodl-tmp/eval_results/plan017_14b_rsft_no_evidence_eval/predictions.json
```

## 结果

| 指标 | 值 |
|------|-----|
| F1 | 0.5536 |
| Ign-F1 | 0.5432 |
| Evi-F1 | 0.0000 (预期，no-evidence 不输出 evidence) |
| Format OK | 953/985 (96.8%) |
| Truncated | 106/985 |

## 为什么看起来"失败"

输出目录路径不匹配：
- 你检查的路径：`/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_no_evidence_eval/`
- 实际输出路径：`/root/autodl-tmp/eval_results/plan017_14b_rsft_no_evidence_eval/`

脚本用的是 `eval_results/` 而非 `eval_outputs/`。PID 55039 正常退出（进程完成后自然消失），cuda:2 空闲也符合预期。

**结论：eval 成功完成，无需重跑。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_diagnose_14b-no-evi-failure_20260521T004242"
}
```

</details>

---
