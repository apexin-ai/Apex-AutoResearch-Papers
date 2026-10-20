# audit exp016 data source

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_exp016_data_source_20260514T231243_result.json`
- **Structured JSON:** [`9fd854415df2a1bc2c92.json`](../../sessions/9f/9fd854415df2a1bc2c92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结论如下：

---

## 审计结论

### 1. 数据来源

**exp_016_signal_ensemble 的全部分析数据来自 exp_012_logprob（max_tokens=512），NOT pilot_004。**

`analyze_exp016_ensemble.py` 第 643-648 行是 if/else 逻辑：当 `exp_012_logprob/samples_with_logprobs.jsonl` 存在且包含 logprob 字段时，**直接使用该文件作为唯一数据源**，pilot_004 完全未被加载。Registry 中 `spec.eval_data = "pilot_004"` 具有误导性。

### 2. max_tokens 确认

| 实验 | 脚本 | max_tokens |
|------|------|-----------|
| pilot_004 | `run_mvp_pilot.py` (default) | **1024** |
| exp_012_logprob | `extract_logprobs.py` 第 56/67 行 | **512** |

### 3. 截断情况

exp_012_logprob 存在实质性截断：

- **239/4959 个样本 (4.8%)** 命中 512 token 上限
- **46/551 个 instance (8.3%)** 至少有一个样本被截断
- 受影响 instance 中平均 5.2/9 个样本被截断（截断比例高）

### 4. 论文数值是否可信

**不完全可信。** 三个论文数值全部基于 exp_012（512）而非 pilot_004（1024）数据：

| 指标 | 值 | 风险 |
|------|------|------|
| Ensemble AUROC | 0.735 (NER) | 截断样本→entities/relations 不完整→一致性信号被低估→AUROC 可能被低估 |
| Selection F1 table | greedy=0.6094, oracle=0.7692 等 | 截断使 sample 质量下降，F1 和 oracle headroom 可能被压低 |
| ECE | 同上 | 基于同一批截断数据计算 |

**建议**：用 pilot_004 数据（max_tokens=1024，无截断）重跑 exp_016 分析，或用 max_tokens=1024 重新提取 logprob，以获得无截断数值用于论文。

---
