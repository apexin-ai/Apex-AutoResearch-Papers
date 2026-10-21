# diagnose hellaswag metric check

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_hellaswag-metric-check_20260521T095449_result.json`
- **Structured JSON:** [`91a235a02ce6ed0aa349.json`](../../sessions/91/91a235a02ce6ed0aa349.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论明确了。

## 结果

**HellaSwag per-example correct/incorrect 基于 `acc`（非 `acc_norm`）。**

### 证据

1. **`analyze_boolq_hellaswag.py` 第 32 行**（生成 `hellaswag_per_example.json` 的脚本）：
   ```python
   accs.append((d["doc_id"], int(d["acc"])))
   ```
   用的是 `d["acc"]` 字段，不是 `d["acc_norm"]`。

2. **per-example jsonl 样本**（`hellaswag.jsonl` 第一行）同时包含 `"acc": 0.0` 和 `"acc_norm": 0.0` 两个字段，但分析代码只读取了 `"acc"`。

3. **Aggregate 指标**（GatedDeltaNet-pure）：
   - **`acc` = 0.4641**
   - **`acc_norm` = 0.6076**
   
   差异很大（~14pp），`acc_norm` 做了 length normalization 后显著更高。

4. **注意**：`task_specificity_analysis.py` 的 aggregate 汇报用的是 `acc_norm,none`（即报告时引用 0.6076），但 per-example helped/hurt 分类用的是 `acc`（即基于 0.4641 水平的逐样本对错判断）。

### 含义

per-example 分析中一个样本被判"正确"意味着模型选了 raw log-likelihood 最高的选项恰好是 gold answer（无 length normalization）。这比 `acc_norm` 标准更严格，对应的 pure baseline 正确率只有 ~46%。

---
