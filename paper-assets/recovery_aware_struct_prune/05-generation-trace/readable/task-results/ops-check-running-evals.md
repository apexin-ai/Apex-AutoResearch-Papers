# ops check running evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-running-evals_20260516T051801_result.json`
- **Structured JSON:** [`1306981b0ed4f65d8da3.json`](../../sessions/13/1306981b0ed4f65d8da3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 实验 1: eval_grpo_rasp_v9_step10
- **状态**: STILL_RUNNING (PID 585618)
- **进度**: 249/1319 (18.9%)
- **当前 acc**: 0.6800 (@ 200 samples), eos_rate=99.50%, avg_len=167
- **速度**: ~2.0-2.5s/it
- **预计剩余**: ~40-45 分钟

### 实验 2: eval_grpo_unpruned_v2_step90
- **状态**: COMPLETED
- **accuracy**: **80.59%** (1063/1319)
- **stderr**: 0.0109
- **eos_rate**: 99.62%, avg_response_length: 213.4, truncated: 5

### 实验 3: eval_grpo_unpruned_v2_step100
- **状态**: COMPLETED
- **accuracy**: **81.27%** (1072/1319)
- **stderr**: 0.0107
- **eos_rate**: 99.70%, avg_response_length: 209.0, truncated: 4

### Unpruned v2 GRPO 趋势
| checkpoint | accuracy | eos_rate |
|---|---|---|
| step90 | 80.59% | 99.62% |
| step100 | 81.27% | 99.70% |

Step90→100 提升 +0.68pp，仍在缓慢上升。

---

### Prune 25% Checkpoints (westb-23072)

| 目录 | 存在 | 文件数 | 总大小 |
|---|---|---|---|
| `pruned_standard_25/` | Yes | 7 files | 11G |
| `pruned_rasp_25/` | Yes | 7 files | 11G |

两个目录结构一致：`model.safetensors`, `config.json`, `generation_config.json`, `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja`, `pruning_metadata.pt`。

---
