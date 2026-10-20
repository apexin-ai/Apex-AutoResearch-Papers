# code fix leakage truncation

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-leakage-truncation_20260514T215113_result.json`
- **Structured JSON:** [`e32d5eda6122eba628a5.json`](../../sessions/e3/e32d5eda6122eba628a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 修改文件

| 文件 | 修改内容 |
|------|---------|
| `src/vota.py` | 移除 3 处 `match=` 输出（Strategy 0/1/2），删除 `match` 变量赋值 |
| `data/format_training_data.py` | 1) `[No trace available - execution failed]` → `[No trace available]`；2) 新增 `_truncate_trace` 智能截断，保证 label 不被丢弃；3) tokenizer 前置加载；4) 截断统计输出 |
| `tests/test_vota.py` | 7 处 `assert "match=True/False" in result` → `assert "match=" not in result`；所有事件补充 `"source": "test"` 字段 |

## 截断率统计

| 条件 | 截断率 | 截断后 avg tokens | p50 | max |
|------|--------|-------------------|-----|-----|
| no_trace | 0.0% | 178 | 151 | 1260 |
| vota | 88.7% | 1922 | 2048 | 2048 |
| full_trace | 94.9% | 1957 | 2048 | 2048 |

## 数据样本数

- 总计 5910 样本（pass=3958, fail=1952）
- train: 4720, test: 1190
- 三组各 6 个文件（train+test）已输出到 `/root/autodl-tmp/trace-verdict-study-data/`

## 验证结果

- test_vota.py: **35/35 通过**
- match=True/False 泄漏: **0**（10 个 `total_match` 是 HumanEval/74 的函数名，非泄漏）
- label 超 2048 tokens: **0/5910（所有条件）**
- label 均为单 token（pass=[6385], fail=[18403]）

---
