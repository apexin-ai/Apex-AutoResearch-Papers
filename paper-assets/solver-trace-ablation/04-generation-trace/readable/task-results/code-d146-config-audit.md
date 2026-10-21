# code d146 config audit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-config-audit_20260519T155056_result.json`
- **Structured JSON:** [`b409e464cb0174669c74.json`](../../sessions/b4/b409e464cb0174669c74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### train_grpo.py 默认值
`num_generations` 默认 **4**（line 491: `args.num_generations = 4`）

### 各 config 文件 num_generations 值

| 值 | config 文件 |
|---|---|
| **16** | `grpo_prolog_exec_only_k16_warmup.yaml` |
| **8** | `grpo_exec_retrain.yaml`, `grpo_exec_retrain_v3.yaml`, `grpo_isr_gated.yaml`, `grpo_isr_gated_curriculum.yaml`, `grpo_isr_gated_warmstart.yaml`, `grpo_isr_gated_warmstart_v2.yaml`, `grpo_isr_warmstart_t015.yaml`, `grpo_isr_warmstart_v3.yaml` |
| **4** | 其余 29 个 config（含所有 sweep_*, plan018_*, additive_bonus/random 系列, exec_only, exec_sta, prolog, prooffol, llama, d142_gated_isr 等） |
| **2** | `grpo_additive_bonus_b01_8b.yaml`, `grpo_exec_only_8b.yaml`（8B 模型显存限制） |

总计 40 个 config：2 个=16，8 个=8，28 个=4，2 个=2。

---
