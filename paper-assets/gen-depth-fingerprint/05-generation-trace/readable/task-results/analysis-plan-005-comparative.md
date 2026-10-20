# analysis plan 005 comparative

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-005-comparative_20260515T060035_result.json`
- **Structured JSON:** [`41574051ea2ea231c039.json`](../../sessions/41/41574051ea2ea231c039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan-005 分析全部完成。以下是完整结果：

---

## 1. Per-Prompt-Type 5-Fold CV (XGBoost, 3-class macro-F1)

| Prompt Type | F1 mean | F1 std |
|---|---|---|
| continuation | **0.7806** | ±0.0120 |
| inspired_rewriting | 0.7368 | ±0.0114 |
| elaboration | 0.7300 | ±0.0112 |

Continuation 最易区分 depth（F1 最高），因为它的特征漂移最剧烈。

## 2. Leave-One-Prompt-Type-Out (LOPTO)

| Held-out | F1 |
|---|---|
| continuation | 0.7620 |
| elaboration | 0.7622 |
| inspired_rewriting | 0.7334 |
| **Average** | **0.7525** |

跨 prompt type 泛化良好。Rewriting 作为 held-out 时 F1 略低，说明其 depth signal 模式与另外两种有微小差异。

## 3. Depth Decay (d4 / d0 retention)

| Prompt Type | d0 | d4 | Retention |
|---|---|---|---|
| continuation | 995 | 827 | **83.1%** |
| inspired_rewriting | 995 | 934 | 93.9% |
| elaboration | 995 | 981 | **98.6%** |

Continuation 衰减最严重（16.9% 样本在 depth 4 丢失），elaboration 几乎无衰减。

## 4. Feature Drift Rate (relative change d0→d4)

| Feature | continuation | elaboration | rewriting |
|---|---|---|---|
| entropy_mean | -55.7% | -47.1% | -47.7% |
| entropy_std | -4.6% | -0.5% | -1.5% |
| entropy_max | -0.3% | +6.9% | +7.1% |
| entropy_min | **+291.2%** | -46.9% | +79.9% |
| tail_decay | +3.1% | -1.3% | -0.5% |
| ttr | -60.7% | -64.1% | -61.8% |
| hapax_ratio | -74.0% | **-82.8%** | -80.0% |

关键发现：
- **hapax_ratio** 是三种 type 中最一致的 depth 判别特征（drift -74%~-83%）
- **ttr** 同样稳健（drift -61%~-64%）
- **entropy_min** 在 continuation 中异常飙升 +291%，而 elaboration 反而下降 -47%，这是造成 continuation CV F1 最高的主要原因
- **entropy_max / entropy_std / tail_decay** 跨 depth 几乎不变，判别能力弱

Registry 已更新 (`plan-005`, conclusion=success)，结果 JSON 保存在服务器 `data/prompt_type_results.json`。

---
