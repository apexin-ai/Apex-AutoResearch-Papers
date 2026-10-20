# ops gpu probe and results

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-probe-and-results_20260516T182701_result.json`
- **Structured JSON:** [`1e57c4e2315d174f7296.json`](../../sessions/1e/1e57c4e2315d174f7296.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. GPU 状态

| GPU | 利用率 | 显存使用 | 进程 PID | 任务 |
|-----|--------|----------|----------|------|
| 0 | 100% | 94.5/97.9 GB | 294700 | `exception_only_nomarker_seed123` (step 230/444, **52%**) |
| 1 | 100% | 37.2/97.9 GB | 296972 | `exception_only_nomarker_seed456` (step 15/444, **3%**) |

### 2. 实验结果

| 实验 | 状态 | Accuracy | 备注 |
|------|------|----------|------|
| **codellama13b_vota_seed42** | 完成 | **98.57%** | eval_results.json 已生成，pass_f1=0.990, fail_f1=0.975 |
| **exception_only_nomarker_seed123** | 训练中 | — | 52% (230/444 steps), ~10s/it, 预计还需 ~35 min |
| **exception_only_nomarker_seed456** | 训练中 | — | 3% (15/444 steps), ~10s/it, 预计还需 ~70 min |

注意：seed123 的 output_dir 是 `/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker`（没有 `_seed123` 后缀），且目前没有 `final/` 目录。

### 3. CodeLlama-13B 模型路径

`/root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/` — 在 autodl-tmp 下，不在 `/root/trace-verdict-study/models/`。

### 4. GPU 可用性

**两张 GPU 都在忙，当前无空闲 GPU。** seed123 预计约 35 分钟后完成，之后 GPU 0 可释放用于 eval 或新实验。

---
