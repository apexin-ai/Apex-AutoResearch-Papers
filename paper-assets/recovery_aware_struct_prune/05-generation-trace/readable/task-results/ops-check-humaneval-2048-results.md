# ops check humaneval 2048 results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_humaneval_2048_results_20260517T133805_result.json`
- **Structured JSON:** [`0768f9623805cce01faf.json`](../../sessions/07/0768f9623805cce01faf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. eval_humaneval_sft_rasp_20_2048 — **已完成**
| 指标 | 值 |
|------|-----|
| Pass@1 | **10.37%** (17/164) |
| Stderr | 0.0238 |
| Median response length | 2048 (大量被截断) |

大量 SyntaxError 和推理文本泄漏到代码中，说明 sft_rasp_20 模型代码生成能力严重退化。

### 2. eval_humaneval_unpruned_2048 — **仍在运行**
- PID 23707 仍存活，当前进度 **140/164 (85%)**
- 最新 Pass@1: **46.43%** (at 140 problems)
- 预计约 10-12 分钟完成

### 3. GPU 状态 (westd-11672)
| GPU | 显存占用 | 利用率 | 状态 |
|-----|----------|--------|------|
| cuda:0 | 17667 MiB | 91% | unpruned eval 运行中 |
| cuda:1 | 31527 MiB | 99% | 占用中 |
| **cuda:2** | **0 MiB** | **0%** | **空闲** |
| cuda:3 | 31527 MiB | 99% | 占用中 |

空闲 GPU：**cuda:2**。unpruned 评估预计很快完成后 cuda:0 也将释放。

---
