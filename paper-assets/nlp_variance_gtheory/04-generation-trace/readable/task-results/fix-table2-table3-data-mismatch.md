# fix table2 table3 data mismatch

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_table2_table3_data_mismatch_20260523T104345_result.json`
- **Structured JSON:** [`853ccc151fb33bec66ed.json`](../../sessions/85/853ccc151fb33bec66ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，无错误。只有正常的浮动体和交叉引用 warning。

## 修复总结

**Table 2 (tab:cross_model)** — 3 项修复：
1. `prompt×item`: 2.5% → **0.9%** (源: 0.9456%)
2. 新增 3 行被错误归入 "all others <0.1" 的组件：`temp.×item` **0.6%**, `seed×item` **0.5%**, `ordering×item` **0.3%**
3. "all others (each) <0.1" 现在准确（剩余组件最大为 model:temp 0.04%）

**Table 3 (tab:cross_benchmark)** — 10 个单元格修复：
| 单元格 | 旧值 | 新值 | 错误类型 |
|--------|------|------|----------|
| MMLU prompt† | 2.5 | **0.9** | 值过大 |
| ARC prompt† | 0.4 | **1.4** | 方向反了 |
| Hella prompt† | 2.3 | **2.1** | 小误差 |
| MATH prompt† | 1.0 | **0.8** | 小误差 |
| Hella m×p | 0.6 | **0.2** | 值过大 |
| MATH m×p | 2.0 | **1.7** | 小误差 |
| MMLU all others | <1.0 | **1.6** | 低估 |
| ARC all others | 1.5 | **0.5** | 高估 |
| Hella all others | <1.0 | **0.6** | 低估 |
| MATH all others | 3.3 | **3.8** | 低估 |

**§4.1 数值验证**: 所有 10 个数字与 `exp001_bf16_2temp_comparison.json` 一致，无需修改。

**GSM8K 列**: 所有值已正确，无需修改。

所有列总和 = 100.0%。修正对照表已注册为 `art_20260523_6b20ce`。

---
