# audit toxicchat wiki mlm verify

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_toxicchat_wiki_mlm_verify_20260524T044757_result.json`
- **Structured JSON:** [`7f997b72ab3db8ac6a49.json`](../../sessions/7f/7f997b72ab3db8ac6a49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。以下是结论：

---

## 结论

### 1. corrected 文件修正了什么 bug？

原始 `exp8_mhj_evaluation.json` 只计算了 **binary F1**（正类 F1），字段名为 `f1`。论文需要 **macro F1**（两类 F1 的平均）。`exp8_recalc_macro_f1.py` 用相同模型 checkpoint 重新推理，同时计算了 binary_f1 和 macro_f1。不是数据 bug，是指标缺失。

### 2. Wiki-MLM：**论文 .791±.093 正确**

corrected 文件中有**三个**评测集。你看到的 .742±.161 来自 `verazuo_test_only_benign` 部分，不是 `toxicchat` 部分：

| 评测集 | seed 42 | seed 123 | seed 456 | Mean | Std |
|--------|---------|----------|----------|------|-----|
| **toxicchat** (论文用) | .661 | .872 | .840 | **.791** | **.093** |
| verazuo_test_only_benign | .514 | .845 | .867 | .742 | .161 |

论文 ToxicChat 表用的是 `toxicchat` 部分（204 jb + 204 benign），值为 **.7913±.0930**，与论文完全吻合。

### 3. Topic：**论文 .496±.042 正确**

同理：

| 评测集 | seed 42 | seed 123 | seed 456 | Mean | Std |
|--------|---------|----------|----------|------|-----|
| **toxicchat** (论文用) | .493 | .548 | .445 | **.496** | **.042** |
| verazuo_test_only_benign | .554 | .550 | .406 | .503 | .069 |

论文值 **.4955±.0418** 来自 `toxicchat` 部分，正确。

### 4. 错误来源

**你对比了不同评测集的数值。** corrected 文件有 `toxicchat`、`verazuo`、`verazuo_test_only_benign` 三个顶层 key。论文 ToxicChat 表取的是 `toxicchat` key 下的数据，而 .742/.503 来自 `verazuo_test_only_benign` key。7 个变体全部一致，无需修改论文。

---
