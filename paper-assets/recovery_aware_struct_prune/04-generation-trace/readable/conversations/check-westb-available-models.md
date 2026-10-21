# check westb available models

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_check_westb_available_models_20260518T094750.jsonl`
- **Structured JSON:** [`5dc6ad651eaaca35dc2d.json`](../../sessions/5d/5dc6ad651eaaca35dc2d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-18T09:48:30.558958+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_westb_available_models_20260518T094750",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T09:48:30.559287+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_westb_available_models_20260518T094750",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T09:48:30.559508+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-23072",
  "command": "echo \"=== /root/autodl-tmp/recovery_aware_struct_prune/ ===\"\nls -d /root/autodl-tmp/recovery_aware_struct_prune/*/ 2>/dev/null\n\necho \"=== checkpoints 目录 ===\"\nls -d /root/autodl-tmp/recovery_aware_struct_prune/checkpoints/*/ 2>/dev/null\n\necho \"=== 所有含 grpo 或 sft 的目录 ===\"\nfind /root/autodl-tmp/recovery_aware_struct_prune/ -maxdepth 2 -type d \\( -name \"*grpo*\" -o -name \"*sft*\" -o -name \"*standard*\" -o -name \"*rasp*\" \\) 2>/dev/null\n\necho \"=== Dense model ===\"\nls -d /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B 2>/dev/null && echo \"EXISTS\" || echo \"NOT FOUND\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_westb_available_models_20260518T094750",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-23072",
    "command": "echo \"=== /root/autodl-tmp/recovery_aware_struct_prune/ ===\"\nls -d /root/autodl-tmp/recovery_aware_struct_prune/*/ 2>/dev/null\n\necho \"=== checkpoints 目录 ===\"\nls -d /root/autodl-tmp/recovery_aware_struct_prune/checkpoints/*/ 2>/dev/null\n\necho \"=== 所有含 grpo 或 sft 的目录 ===\"\nfind /root/autodl-tmp/recovery_aware_struct_prune/ -maxdepth 2 -type d \\( -name \"*grpo*\" -o -name \"*sft*\" -o -name \"*standard*\" -o -name \"*rasp*\" \\) 2>/dev/null\n\necho \"=== Dense model ===\"\nls -d /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B 2>/dev/null && echo \"EXISTS\" || echo \"NOT FOUND\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T09:48:30.559736+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== /root/autodl-tmp/recovery_aware_struct_prune/ ===\\n/root/autodl-tmp/recovery_aware_struct_prune/artifacts/\\n/root/autodl-tmp/recovery_aware_struct_prune/eval_results/\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/logs/\\n/root/autodl-tmp/recovery_aware_struct_prune/models/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_gradient_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_magnitude_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30/\\n/root/autodl-tmp/recovery_aware_struct_prune/results/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/\\n=== checkpoints 目录 ===\\n=== 所有含 grpo 或 sft 的目录 ===\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30\\n/root/auto
…[truncated 676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_westb_available_models_20260518T094750",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-18T09:48:30.559960+00:00_

westb-23072 上的模型清单：

**Dense model**
- `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B` ✅

**Pruned models (未训练)**
| 路径 | 说明 |
|------|------|
| `pruned_cka_only_20/` | CKA-only 剪枝 20% |
| `pruned_gradient_20/` | Gradient 剪枝 20% |
| `pruned_magnitude_20/` | Magnitude 剪枝 20% |
| `pruned_random_20/` | Random 剪枝 20% |
| `pruned_rasp_25/` | RASP 剪枝 25% |
| `pruned_rasp_30/` | RASP 剪枝 30% |
| `pruned_rasp_rlvr_20/` | RASP-RLVR 剪枝 20% |
| `pruned_standard_25/` | Standard 剪枝 25% |
| `pruned_standard_30/` | Standard 剪枝 30% |

**SFT checkpoints**
| 路径 | 说明 |
|------|------|
| `sft_cka_only_20/` | CKA-only 20% SFT |
| `sft_gradient_20/` | Gradient 20% SFT |
| `sft_random_20/` | Random 20% SFT |
| `sft_rasp_25/` | RASP 25% SFT |
| `sft_rasp_rlvr_20/` | RASP-RLVR 20% SFT |
| `sft_standard_25/` | Standard 25% SFT |

**GRPO checkpoints**
| 路径 | 说明 |
|------|------|
| `grpo_cka_only_20/` | CKA-only 20% GRPO |
| `grpo_random_20/` | Random 20% GRPO |
| `grpo_rasp_25/` | RASP 25% GRPO |

所有路径前缀均为 `/root/autodl-tmp/recovery_aware_struct_prune/`。

---

**你要找的 5 个模型全部不在 westb 上：**

| 需要的模型 | westb 状态 |
|-----------|-----------|
| `grpo_standard_20` / `grpo_standard_20_fair` | ❌ 没有（只有 25% 的 `grpo` 没有 standard 20%） |
| `grpo_rasp_20` / `grpo_stage2_rasp_20_v9` | ❌ 没有（只有 `grpo_rasp_25`） |
| `sft_standard_20` | ❌ 没有（只有 `sft_standard_25`） |
| `sft_rasp_20` | ❌ 没有（只有 `sft_rasp_25`） |
| `grpo_unpruned_v2` | ❌ 没有 |

westb 上有的是另一批实验（25%/30% sparsity 以及 cka_only/gradient/random/rasp_rlvr 等 ablation 变体），核心的 20% standard/rasp GRPO/SFT checkpoint 都只在 westd-11672 上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_westb_available_models_20260518T094750"
}
```

</details>

---
