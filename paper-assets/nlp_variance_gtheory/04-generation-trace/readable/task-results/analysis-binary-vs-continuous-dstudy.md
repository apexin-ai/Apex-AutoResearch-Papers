# analysis binary vs continuous dstudy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_binary_vs_continuous_dstudy_20260523T030219_result.json`
- **Structured JSON:** [`71ed4f27186058099291.json`](../../sessions/71/71ed4f27186058099291.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果总结：

**D-study budget (n_items for G≥0.80)**

| Case | G at 200 items | n_min G≥0.80 | δ/τ ratio |
|------|---------------|-------------|-----------|
| Continuous (TRUE_VC) | 0.890 | **99** | 0.124 |
| Binary observed (real data) | 0.936 | **55** | 0.068 |
| Binary oracle (simulation p=0.7) | 0.856 | **135** | 0.168 |

**两组对比：**

1. **公平对比（同一模拟内）**：continuous 99 vs binary oracle 135 → 二值化增加 36% 的 item budget。方向符合预期：Bernoulli 噪声将 residual 从 16%→41%，压缩 item_id 从 50%→32%，恶化 δ/τ 比。

2. **跨源对比（模拟 vs 实际数据）**：continuous 99 vs observed binary 55 → continuous 反而多需 80% items。原因是 TRUE_VC 的 facet×item 交互项相对于 item_id 比实际数据更大（δ/τ=0.124 vs 0.068），这是模拟设计与实际方差结构不匹配导致的，不代表连续数据天然劣于二值数据。

输出已保存并注册：`exp004/data/binary_vs_continuous_dstudy.json`

---
