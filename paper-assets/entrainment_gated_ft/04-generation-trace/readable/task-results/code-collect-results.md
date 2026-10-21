# code collect results

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_collect-results_20260518T121745_result.json`
- **Structured JSON:** [`1752eaf78074201d966d.json`](../../sessions/17/1752eaf78074201d966d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整报告。

---

## Benchmark 结果汇总

### 服务器状态
- **GPU**: 空闲 (0% util, 3353 MiB used)
- **无正在运行的评测进程**

---

### 1. LM-Eval 标准 Benchmark（0-shot）

有两套结果：早期 `lm_eval/` 和后来的 `results_v5/` + `lm_eval_fixed/`。GatedDeltaNet 正确结果仅存在于早期 `lm_eval/` 目录中，后续 `lm_eval_fixed/` 对 GatedDeltaNet 和 RetNet 的结果均**异常**（lambada acc=0, ppl=数亿，其他任务接近随机水平），疑似模型加载 bug。

| Benchmark | Metric | Transformer 1.3B | GatedDeltaNet Hybrid | RetNet Pure |
|---|---|---|---|---|
| **lambada_openai** | acc | 0.4809 | **0.5077** | ~~0.0~~ (broken) |
| | ppl↓ | 11.46 | **9.97** | ~~14.5M~~ (broken) |
| **hellaswag** | acc_norm | 0.5923 | **0.6025** | ~~0.2605~~ (broken) |
| **arc_easy** | acc | 0.7075 | **0.7218** | ~~0.2576~~ (broken) |
| **arc_challenge** | acc_norm | 0.3916 | **0.3985** | ~~0.2876~~ (broken) |
| **winogrande** | acc | 0.6148 | **0.6148** | ~~0.4997~~ (broken) |
| **openbookqa** | acc_norm | 0.392 | — | — |
| **MMLU (5-shot)** | acc | 0.2698 | — | — |

**Transformer 来源**: `results_v5` 逐任务运行（正确），MMLU 来自 `lm_eval_fixed`
**GatedDeltaNet 来源**: `lm_eval/gated_deltanet_hybrid/results_2026-05-18T18-09-55`（正确）
**RetNet**: 所有运行均异常，模型加载有问题，结果不可用

---

### 2. GatedDeltaNet MMLU（5-shot, from lm_eval_fixed/18-56-16）

部分子任务已存，但**缺少 group-level 聚合分数**。已读到的子任务包括 abstract_algebra(0.23)、anatomy(0.25)、astronomy(0.20)、college_biology(0.23) 等，整体约 0.22-0.25 范围。

---

### 3. Function Composition 评测（func_comp, direct）

仅有 **Transformer 1.3B baseline** 的完整结果：

| Depth | Accuracy | Correct/Total |
|---|---|---|
| 1 | 0.094 | 47/500 |
| 2 | 0.094 | 47/500 |
| 3 | 0.124 | 62/500 |
| 4 | 0.128 | 64/500 |
| 5 | 0.118 | 59/500 |

Random chance = 0.10。GatedDeltaNet 和 RetNet 有 prediction 文件但**未包含在 summary 中**。

---

### 4. Logprob 评测（仅 Transformer）

| Depth | fraction_rank_1 | mean_correct_prob | mean_margin |
|---|---|---|---|
| 1 | 0.184 | 0.132 | -0.679 |
| 2 | 0.118 | 0.106 | -1.044 |
| 3 | 0.132 | 0.108 | -1.112 |
| 4 | 0.132 | 0.110 | -1.134 |
| 5 | 0.110 | 0.105 | -1.142 |

---

### 5. 失败的评测任务

| Log | 错误 |
|---|---|
| t7 (logiqa2) | `Dataset scripts are no longer supported` — datasets 库版本不兼容 |
| t9 | `httpx.ConnectTimeout` — 网络超时 |
| transformer_6tasks | SIGTERM (exit 143) — 被 kill，39% 进度 |
| transformer_7tasks | `Feature type 'List' not found` — datasets 库版本不兼容 |

---

### 关键问题
1. **RetNet 和 GatedDeltaNet 在 lm_eval_fixed 中模型加载异常**，导致近随机结果。GatedDeltaNet 仅早期的 5-task 一次运行是正确的；RetNet 无可用结果。
2. **GatedDeltaNet 缺少 openbookqa 和完整 MMLU**。
3. **func_comp/logprob 缺少 GatedDeltaNet 和 RetNet** 的汇总数据。
4. 模型存储: `/root/autodl-tmp/models_1.3b/` 共 26G。

---
