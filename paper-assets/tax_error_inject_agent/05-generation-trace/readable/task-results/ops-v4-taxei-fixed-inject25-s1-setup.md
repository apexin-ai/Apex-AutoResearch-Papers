# ops v4 taxei fixed inject25 s1 setup

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v4-taxei-fixed-inject25-s1-setup_20260515T212829_result.json`
- **Structured JSON:** [`402657bfc3709e6706da.json`](../../sessions/40/402657bfc3709e6706da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已在 cuda:2 上运行，GPU 利用率 96%，显存占用 18.2GB/32GB。

**汇报：**

| 项目 | 值 |
|------|-----|
| 数据路径 | `data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl` (4,358行) |
| 训练命令 | `swift sft --model Qwen3-8B --seed 1 --data_seed 1 --lora_rank 16 --num_train_epochs 3 ...` |
| GPU | cuda:2，利用率 96%，显存 18.2GB |
| PID | 199599 |
| tmux session | `v4-taxei-fixed-inject25-s1` |
| Registry | RUNNING，hypothesis 已设置 |

---
