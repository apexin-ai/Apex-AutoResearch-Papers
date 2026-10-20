# investigate v6 data check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_v6-data-check_20260514T071952_result.json`
- **Structured JSON:** [`3abfddda8ca35d3c0535.json`](../../sessions/3a/3abfddda8ca35d3c0535.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。

---

## 检查报告

### 1. 数据格式对比

| | `results/plan_c/` (plan-002 用) | `data/plan-004-implicit/` (ablation-b 用) | `results/plan_c_test_labels/` (plan-004 v2/v3/v4 用) |
|---|---|---|---|
| 结构 | 11个任务子目录，每个含 `labeled_steps.jsonl` | 单个 `implicit_sft.jsonl` | 单个 `implicit_sft.jsonl` + `sft_triples.jsonl` |
| 格式 | step-level: observation/action/label | chat messages: system/user/assistant | chat messages（同左） |
| 样本数 | **2040** | **2040** | **1814** |
| 任务覆盖 | 11 个任务 | 11 个任务 | **仅 4 个任务** |

### 2. 标签分布对比

| 数据集 | deterministic | internal | 来源 |
|---|---|---|---|
| `results/plan_c/` labeled_steps | ~1830 (det-preferred) | ~210 (internal-preferred) | 已过滤 no-preference |
| `data/plan-004-implicit/` | 1830 (89.7%) | 210 (10.3%) | 从 labeled_steps 转换 |
| `results/plan_c_test_labels/` | 600 (33%) | **1214 (67%)** | **1064 条 no-preference 被错误映射为 internal!** |

### 3. `data/plan-004-implicit/implicit_sft.jsonl`

存在，2040 行，标签干净。

### 4. 训练脚本数据加载差异

- **`router_sft_train.py`** (explicit, plan-002 用): `--data_dir` → 读 `{task}/labeled_steps.jsonl`，通过 `RAW_LABEL_MAP` 映射 `det-preferred→deterministic`, `internal-preferred→internal`。`AutoModelForSequenceClassification` 分类头。
- **`implicit_router_sft.py`** (implicit, plan-004 用): `--data_dir` → 读 `implicit_sft.jsonl`，chat format messages，`AutoModelForCausalLM` 生成式训练。

### 5. plan-002-formal-v6 的数据有没有问题？

**没有问题。** `results/plan_c/` 的 `labeled_steps.jsonl` 在生成时已过滤掉所有 no-preference 样本（逐个文件 grep 验证，结果均为 0）。2040 条数据全部是有效的 det-preferred 或 internal-preferred 标签，覆盖 11 个任务。

**问题只出在 `results/plan_c_test_labels/`**：这个目录是从原始 episode 数据生成的，1064 条 no-preference steps（59%）被错误映射为 internal，导致标签分布完全倒转（67% internal vs 正确的 10.3%），这就是 plan-004 v2/v3/v4 loss 异常的根因。

---
