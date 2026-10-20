# ops full gpu check and collect

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-gpu-check-and-collect_20260515T235320_result.json`
- **Structured JSON:** [`04260acf2cbd7287252f.json`](../../sessions/04/04260acf2cbd7287252f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被之前的 session 清理）。全部 registry 更新完毕。

## GPU 状态汇总

| GPU | 任务 | 状态 | 结果 |
|-----|------|------|------|
| cuda:0 | v4-random-fixed-inject50-s1 (训练) | **FAILED** | OOM at step 5/1635 — `Tried to allocate 4.25 GiB`，batch_size=8 + max_length=4096 对 50% 数据集太大 |
| cuda:1 | v4-taxei-fixed-inject50-s1 (训练) | **FAILED** | ModelScope 报错 `Invalid repo_id: model`——swift sft 的 `--model Qwen3-8B` 缺少完整路径，应为 `/root/autodl-tmp/models/Qwen/Qwen3-8B` |
| cuda:2 | v4-taxei-fixed-inject25-s7-eval-r2 | **DONE** | **success_rate = 57.4%** (27/47) |
| cuda:3 | v4-random-fixed-inject25-s7-eval | **DONE** | **success_rate = 59.6%** (28/47) |

### 25% s7 Eval 详细对比

| task_type | TaxEI (s7) | Random (s7) |
|-----------|-----------|-------------|
| look_at_obj_in_light | 5/6 (83.3%) | 4/6 (66.7%) |
| pick_and_place_simple | 3/8 (37.5%) | 5/8 (62.5%) |
| pick_clean_then_place | 5/11 (45.5%) | 6/11 (54.5%) |
| pick_cool_then_place | 3/7 (42.9%) | 3/7 (42.9%) |
| pick_heat_then_place | 6/8 (75.0%) | 6/8 (75.0%) |
| pick_two_obj_and_place | 5/7 (71.4%) | 4/7 (57.1%) |

### 50% 训练失败原因

- **cuda:0 (random)**: CUDA OOM — `per_device_train_batch_size=8` 配合 50% 数据集（4358条）溢出。需降到 batch_size=4 或加 gradient_checkpointing
- **cuda:1 (taxei)**: `--model Qwen3-8B` 被 ModelScope 解析为 repo_id 失败。命令中缺少完整模型路径 `/root/autodl-tmp/models/Qwen/Qwen3-8B`

4 块 GPU 全部空闲，可重新调度 50% 训练。

---
