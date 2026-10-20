# code full eval script

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_code_full-eval-script_20260515T022654.jsonl`
- **Structured JSON:** [`7d374f2babb0d3a120a6.json`](../../sessions/7d/7d374f2babb0d3a120a6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-15T02:28:11.594642+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_full-eval-script_20260515T022654",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T02:28:11.594971+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_full-eval-script_20260515T022654",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T02:28:11.595148+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/recovery_aware_struct_prune/src/eval_gsm8k.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_full-eval-script_20260515T022654",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat /root/recovery_aware_struct_prune/src/eval_gsm8k.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T02:28:11.595486+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nGSM8K Test Set Evaluation.\\n\\nEvaluates model accuracy on GSM8K test split by generating reasoning traces\\nand comparing extracted numeric answers against gold answers.\\n\\nInput:  model path\\nOutput: accuracy printed to stdout + saved to results JSON\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport math\\nimport logging\\nimport os\\nimport random\\nimport re\\n\\nimport numpy as np\\nimport torch\\nfrom datasets import load_dataset\\nfrom transformers import AutoTokenizer\\nfrom model_utils import load_pruned_model\\nfrom tqdm import tqdm\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef _extract_boxed(text: str) -> str | None:\\n    \\\"\\\"\\\"Extract content from \\\\\\\\boxed{...} with balanced brace matching.\\\"\\\"\\\"\\n    idx = text.rfind(\\\"\\\\\\\\boxed{\\\")\\n    if idx == -1:\\n        return None\\n    depth = 0\\n    start = idx + len(\\\"\\\\\\\\boxed{\\\")\\n    for i in range(start, len(text)):\\n        if text[i] == \\\"{\\\":\\n            depth += 1\\n        elif text[i] == \\\"}\\\":\\n            if depth == 0:\\n                return text[start:i]\\n            depth -= 1\\n    return None\\n\\n\\ndef _clean_latex_number(s: str) -> str:\\n    \\\"\\\"\\\"Strip LaTeX formatting to get a plain number.\\\"\\\"\\\"\\n    s = re.sub(r\\\"\\\\\\\\text\\\\{[^}]*\\\\}\\\", \\\"\\\", s)\\n    s = re.sub(r\\\"\\\\\\\\(mathrm|mathbf|textbf)\\\\{([^}]*)\\\\}\\\", r\\\"\\\\2\\\", s)\\n    s = s.replace(\\\"\\\\\\\\!\\\", \\\"\\\").replace(\\\"\\\\\\\\,\\\", \\\"\\\").replace(\\\"\\\\\\\\;\\\", \\\"\\\")\\n    s = s.replace(\\\"\\\\\\\\$\\\", \\\"\\\").replace(\\\"$\\\", \\\"\\\").replace(\\\"\\\\
…[truncated 7542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_full-eval-script_20260515T022654",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T02:28:11.595703+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-23072",
  "command": "cat > /root/recovery_aware_struct_prune/src/run_full_eval.sh << 'EOF'\n#!/bin/bash\n# =============================================================================\n# Full GSM8K Evaluation (N=1319, greedy)\n#\n# Usage:\n#   Phase 1 (baseline + pruned + SFT models):\n#     bash run_full_eval.sh phase1\n#\n#   Phase 2 (GRPO models, after training completes):\n#     bash run_full_eval.sh phase2\n#\n#   All phases:\n#     bash run_full_eval.sh all\n#\n# GPU allocation: GPU0 and GPU1 run in parallel.\n# Results: /root/autodl-tmp/recovery_aware_struct_prune/eval_results/full/\n# =============================================================================\n\nset -euo pipefail\n\n# === Environment ===\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\ncd /root/recovery_aware_struct_prune/src\n\nEVAL_DIR=\"/root/autodl-tmp/recovery_aware_struct_prune/eval_results/full\"\nmkdir -p \"$EVAL_DIR\"\n\n# === Model Paths ===\nBASELINE=\"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\"\nPRUNED_RASP_20=\"/root/autodl-tmp/pruned_rasp_20\"\nSFT_RASP_20=\"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\"\nSFT_STANDARD_20=\"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\"\n\n# Phase 2 paths (update after GRPO completes)\nGRPO_RASP_20=\"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20\"\nGRPO_STANDARD_20=\"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20\"\n\n# === Helper ===\nrun_eval() {\n    local gpu=$1\n    local model_path=$2\n    local model_name=$3\n\n    local output=\"${EVAL_DIR}/eval_full_${model_name}_greedy.json\"\n\n    if [ -f \"$output\" ]; then\n        echo \"[SKIP] $model_name already evaluated: $output\"\n        return 0\n    fi\n\n    echo \"[START] GPU${gpu} | ${model_name} | $(date '+%H:%M:%S')\"\n    CUDA_VISIBLE_DEVICES=$gpu python eval_gsm8k.py \\\n        --model_path \"$model_path\" \\\n        --output_path \"$output\" \\\n        --max_new_tokens 4096 \\\n        --dtype bfloat16 2>&1 | tail -5\n\n    echo \"[DONE] ${model_name} | $(date '+%H:%M:%S')\"\n    # Print summary\n    python -c \"\nimport json\nwith open('$output') as f:\n    d = json.load(f)\nprint(f\\\"  => {d['n_correct']}/{d['n_total']} = {d['accuracy']:.4f}, eos_rate={d['eos_stats']['eos_rate']:.2%}, avg_len={d['eos_stats']['avg_response_length']:.0f}\\\")\n\"\n}\n\n# === Phase 1: baseline + pruned + SFT ===\nrun_phase1() {\n    echo \"========== Phase 1: Baseline + Pruned + SFT ==========\"\n    echo \"Start: $(date)\"\n\n    # GPU0: baseline, then sft_rasp_20\n    (\n        run_eval 0 \"$BASELINE\" \"baseline_unpruned\"\n        run_eval 0 \"$SFT_RASP_20\" \"sft_rasp_20\"\n    ) &\n    local pid0=$!\n\n    # GPU1: pruned_rasp_20, then sft_standard_20\n    (\n        run_eval 1 \"$PRUNED_RASP_20\" \"pruned_rasp_20\"\n        run_eval 1 \"$SFT_STANDARD_20\" \"sft_standard_20\"\n    ) &\n    local pid1=$!\n\n    wait $pid0 $pid1\n    echo \"========== Phase 1 Complete: $(date) ==========\"\n}\n\n# === Phase 2: GRPO models ===\nrun_phase2() {\n    echo \"========== Phase 2: GRPO Models ==========\"\n    echo \"Start: $(date)\"\n\n    # Verify paths exist\n    for p in \"$GRPO_RASP_20\" \"$GRPO_STANDARD_20\"; do\n        if [ ! -d \"$p\" ]; then\n            echo \"[ERROR] Model not found: $p\"\n            echo \"  Update the path variable in this script after GRPO completes.\"\n            exit 1\n        fi\n    done\n\n    # GPU0: grpo_rasp_20\n    run_eval 0 \"$GRPO_RASP_20\" \"grpo_rasp_20\" &\n    local pid0=$!\n\n    # GPU1: grpo_standard_20\n    run_eval 1 \"$GRPO_STANDARD_20\" \"grpo_standard_20\" &\n    local pid1=$!\n\n    wait $pid0 $pid1\n    echo \"========== Phase 2 Complete: $(date) ==========\"\n}\n\n# === Main ===\nPHASE=\"${1:-all}\"\n\ncase \"$PHASE\" in\n    phase1) run_phase1 ;;\n    phase2) run_phase2 ;;\n    all)    run_phase1; run_phase2 ;;\n    *)      echo \"Usage: $0 {phase1|phase2|all}\"; exit 1 ;;\nesac\n\necho \"\"\necho \"=== All Results ===\"\nls -lh \"$EVAL_DIR\"/eval_full_*_greedy.json 2>/dev/null || echo \"No results yet.\"\nEOF\nchmod +x /root/recovery_aware_struct_prune/src/run_full_eval.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_full-eval-script_20260515T022654",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat > /root/recovery_aware_struct_prune/src/run_full_eval.sh << 'EOF'\n#!/bin/bash\n# =============================================================================\n# Full GSM8K Evaluation (N=1319, greedy)\n#\n# Usage:\n#   Phase 1 (baseline + pruned + SFT models):\n#     bash run_full_eval.sh phase1\n#\n#   Phase 2 (GRPO models, after training completes):\n#     bash run_full_eval.sh phase2\n#\n#   All phases:\n#     bash run_full_eval.sh all\n#\n# GPU allocation: GPU0 and GPU1 run in parallel.\n# Results: /root/autodl-tmp/recovery_aware_struct_prune/eval_results/full/\n# =============================================================================\n\nset -euo pipefail\n\n# === Environment ===\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\ncd /root/recovery_aware_struct_prune/src\n\nEVAL_DIR=\"/root/autodl-tmp/recovery_aware_struct_prune/eval_results/full\"\nmkdir -p \"$EVAL_DIR\"\n\n# === Model Paths ===\nBASELINE=\"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\"\nPRUNED_RASP_20=\"/root/autodl-tmp/pruned_rasp_20\"\nSFT_RASP_20=\"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\"\nSFT_STANDARD_20=\"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\"\n\n# Phase 2 paths (update after GRPO completes)\nGRPO_RASP_20=\"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20\"\nGRPO_STANDARD_20=\"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20\"\n\n# === Helper ===\nrun_eval() {\n    local gpu=$1\n    local model_path=$2\n    local model_name=$3\n\n    local output=\"${EVAL_DIR}/eval_full_${model_name}_greedy.json\"\n\n    if [ -f \"$output\" ]; then\n        echo \"[SKIP] $model_name already evaluated: $output\"\n        return 0\n    fi\n\n    echo \"[START] GPU${gpu} | ${model_name} | $(date '+%H:%M:%S')\"\n    CUDA_VISIBLE_DEVICES=$gpu python eval_gsm8k.py \\\n        --model_path \"$model_path\" \\\n        --output_path \"$output\" \\\n        --max_new_tokens 4096 \\\n        --dtype bfloat16 2>&1 | tail -5\n\n    echo \"[DONE] ${model_name} | $(date '+%H:%M:%S')\"\n    # Print summary\n    python -c \"\nimport json\nwith open('$output') as f:\n    d = json.load(f)\nprint(f\\\"  => {d['n_correct']}/{d['n_total']} = {d['accuracy']:.4f}, eos_rate={d['eos_stats']['eos_rate']:.2%}, avg_len={d['eos_stats']['avg_response_length']:.0f}\\\")\n\"\n}\n\n# === Phase 1: baseline + pruned + SFT ===\nrun_phase1() {\n    echo \"========== Phase 1: Baseline + Pruned + SFT ==========\"\n    echo \"Start: $(date)\"\n\n    # GPU0: baseline, then sft_rasp_20\n    (\n        run_eval 0 \"$BASELINE\" \"baseline_unpruned\"\n        run_eval 0 \"$SFT_RASP_20\" \"sft_rasp_20\"\n    ) &\n    local pid0=$!\n\n    # GPU1: pruned_rasp_20, then sft_standard_20\n    (\n        run_eval 1 \"$PRUNED_RASP_20\" \"pruned_rasp_20\"\n        run_eval 1 \"$SFT_STANDARD_20\" \"sft_standard_20\"\n    ) &\n    local pid1=$!\n\n    wait $pid0 $pid1\n    echo \"========== Phase 1 Complete: $(date) ==========\"\n}\n\n# === Phase 2: GRPO models ===\nrun_phase2() {\n    echo \"========== Phase 2: GRPO Models ==========\"\n    echo \"Start: $(date)\"\n\n    # Verify paths exist\n    for p in \"$GRPO_RASP_20\" \"$GRPO_STANDARD_20\"; do\n        if [ ! -d \"$p\" ]; then\n            echo \"[ERROR] Model not found: $p\"\n            echo \"  Update the path variable in this script after GRPO completes.\"\n            exit 1\n        fi\n    done\n\n    # GPU0: grpo_rasp_20\n    run_eval 0 \"$GRPO_RASP_20\" \"grpo_rasp_20\" &\n    local pid0=$!\n\n    # GPU1: grpo_standard_20\n    run_eval 1 \"$GRPO_STANDARD_20\" \"grpo_standard_20\" &\n    local pid1=$!\n\n    wait $pid0 $pid1\n    echo \"========== Phase 2 Complete: $(date) ==========\"\n}\n\n# === Main ===\nPHASE=\"${1:-all}\"\n\ncase \"$PHASE\" in\n    phase1) run_phase1 ;;\n    phase2) run_phase2 ;;\n    all)    run_phase1; run_phase2 ;;\n    *)      echo \"Usage: $0 {phase1|phase2|all}\"; exit 1 ;;\nesac\n\necho \"\"\necho \"=== All Results ===\"\nls -lh \"$EVAL_DIR\"/eval_full_*_greedy.json 2>/dev/null || echo \"No results yet.\"\nEOF\nchmod +x /root/recovery_aware_struct_prune/src/run_full_eval.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T02:28:11.595887+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_full-eval-script_20260515T022654",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T02:28:11.596019+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "bash -n /root/recovery_aware_struct_prune/src/run_full_eval.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_full-eval-script_20260515T022654",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "bash -n /root/recovery_aware_struct_prune/src/run_full_eval.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T02:28:11.596142+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'bash' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_full-eval-script_20260515T022654",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T02:28:11.596275+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-23072",
  "command": "bash -n /root/recovery_aware_struct_prune/src/run_full_eval.sh && echo \"SYNTAX_OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_full-eval-script_20260515T022654",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-23072",
    "command": "bash -n /root/recovery_aware_struct_prune/src/run_full_eval.sh && echo \"SYNTAX_OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T02:28:11.596406+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SYNTAX_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_full-eval-script_20260515T022654",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T02:28:11.596565+00:00_

语法验证通过。

**产出总结**：

**eval_gsm8k.py** — 无需修改，已支持 per-sample 输出（每个样本保存 question, gold, prediction, correct, response, response_length, hit_eos 到 JSON 的 `examples` 数组）。

**`/root/recovery_aware_struct_prune/src/run_full_eval.sh`** — 已创建，功能：

| 命令 | 作用 |
|------|------|
| `bash run_full_eval.sh phase1` | 跑 baseline + pruned_rasp_20 + sft_rasp_20 + sft_standard_20 |
| `bash run_full_eval.sh phase2` | 跑 grpo_rasp_20 + grpo_standard_20 |
| `bash run_full_eval.sh all` | 全部 |

**GPU 分配**：
- Phase 1: GPU0 → baseline + sft_rasp_20, GPU1 → pruned_rasp_20 + sft_standard_20（并行）
- Phase 2: GPU0 → grpo_rasp_20, GPU1 → grpo_standard_20（并行）

**跳重机制**：已评估的模型（输出文件已存在）自动跳过。

**预估运行时间**（7B 模型, 1319 样本, greedy, max_new_tokens=4096）：
- 每个模型约 40-60 分钟（取决于平均生成长度）
- Phase 1: ~60 分钟（两组并行，每组 2 个模型串行）
- Phase 2: ~40 分钟（两个模型并行）
- 总计: ~1.5-2 小时

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_full-eval-script_20260515T022654"
}
```

</details>

---
