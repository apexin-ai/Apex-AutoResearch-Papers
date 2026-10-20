# ops eval status check and fill

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_status_check_and_fill_20260515T225859_result.json`
- **Structured JSON:** [`af3cd30617b48c871478.json`](../../sessions/af/af3cd30617b48c871478.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

---

## 报告

### 1. nvidia-smi 实际状态

| GPU | 显存占用 | 总显存 | GPU 利用率 | 进程 PID | 进程显存 |
|-----|---------|--------|-----------|---------|---------|
| cuda:0 | 16921 MiB | 97887 MiB | 89% | 303530 | 16912 MiB |
| cuda:1 | 17343 MiB | 97887 MiB | 88% | 304011 | 17334 MiB |

**双卡满载运行中。**

### 2. 每个 eval 实验的实际情况

| exp_id | 状态 | PID | 运行时间 | 进度 | 备注 |
|--------|------|-----|---------|------|------|
| w5_llama_docred_lora_unconstrained_eval | **RUNNING** | 303525 | 3h01m | 721/998 (72%) | Registry 已从 PREPARING 修正为 RUNNING |
| w5_qwen_docred_lora_unconstrained_eval | **RUNNING** | 304006 | 2h55m | 487/998 (49%) | 状态正确 |
| w5_llama_docred_lora_constrained_eval | PREPARING | — | — | 等待 cuda:0 | 待 Llama unconstrained 完成后提交 |
| w5_qwen_docred_lora_constrained_eval | PREPARING | — | — | 等待 cuda:1 | 待 Qwen unconstrained 完成后提交 |

### 3. 已完成实验的 metrics

无新完成的实验。Llama ETA ~1.5h（剩余 277 样本），Qwen ETA ~3h（剩余 511 样本）。

### 4. 填 GPU 操作

**无法填充** — 双卡均被 unconstrained eval 占满。Constrained eval 需等各自 unconstrained 完成后提交。

### 5. 最终状态

双卡 89%/88% GPU 利用率，满负荷运行。Llama 预计先完成（~72% vs ~49%），届时 cuda:0 空出可立即提交 `w5_llama_docred_lora_constrained_eval`。

---
