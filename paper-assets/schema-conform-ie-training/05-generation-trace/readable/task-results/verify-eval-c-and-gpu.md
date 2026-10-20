# verify eval c and gpu

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_eval_c_and_gpu_20260513T062358_result.json`
- **Structured JSON:** [`886c6478221281b7b30d.json`](../../sessions/88/886c6478221281b7b30d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 上跑的是 **formal_D1 GRPO 训练**（scierc, max_steps=500），不是残留进程。

汇总：

---

### 1. GPU 状态

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 0% | 0 / 97887 MiB | **空闲** |
| 1 | 100% | 65294 / 97887 MiB | **D1 GRPO 训练中** (PID 67223, 70714) |

### 2. eval_C_v2 — crossner_science **已完成**

完整三数据集结果：

| Metric | scierc_test | crossner_politics | crossner_science |
|--------|------------|-------------------|------------------|
| **entity_f1** | 0.3949 | 0.4158 | **0.5514** |
| **f1_correctness** | 0.2184 | 0.4116 | **0.5329** |
| **structural_validity** | 0.9964 | 1.0000 | **0.9982** |
| type_conformance | 0.9537 | 0.9997 | 0.9781 |
| structural_completeness | 0.9543 | 0.9932 | 0.9678 |
| relational_constraint | 0.7191 | 0.0000 | 0.0000 |

结果文件: `/root/autodl-tmp/output/base_zero_shot_v2/base_model_results.json`
预测文件: `/root/autodl-tmp/output/base_zero_shot_v2/predictions/base_crossner_science.jsonl`

### 3. A checkpoint-200 — **存在，完整**

路径: `/root/autodl-tmp/output/formal_A/checkpoint-200/`
包含 adapter_model.safetensors (465MB), optimizer.pt (931MB), scheduler.pt, trainer_state.json 等，可用于 D2 Phase 2 resume。

---
