# analysis r11 q1 ner partial bcs

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r11-q1-ner-partial-bcs_20260517T091808_result.json`
- **Structured JSON:** [`92a055b78d6d27f3b911.json`](../../sessions/92/92a055b78d6d27f3b911.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## Few-NERD BCS-F1 Partial Correlation (n=450, 3 seeds × 150 batches)

| Metric | r | p |
|--------|---|---|
| Raw r(BCS, F1) | 0.004 | 0.937 |
| r(BCS, mean_freq) | -0.079 | 0.092 |
| r(F1, mean_freq) | **0.257** | **3.4e-08** |
| Partial r(BCS, F1 \| freq) | 0.025 | 0.597 |
| Partial r(BCS, F1 \| freq+count) | 0.022 | 0.635 |

### Within-count correlations (BCS vs F1):
| Count | n | r | p | Partial r\|freq | p |
|-------|---|---|---|------|---|
| 2 | 75 | 0.011 | 0.929 | 0.058 | 0.621 |
| 6 | 75 | 0.083 | 0.481 | 0.036 | 0.761 |
| 12 | 75 | 0.003 | 0.982 | -0.124 | 0.290 |
| 22 | 75 | **-0.297** | **0.010** | -0.217 | 0.061 |
| 44 | 75 | -0.063 | 0.592 | -0.114 | 0.331 |
| 66 | 75 | 0.049 | 0.676 | 0.049 | 0.676 |

### 解读

1. **Raw BCS-F1 相关在 NER 中接近零** (r=0.004)，频率控制后仍无显著效应
2. **Type frequency 确实预测 F1** (r=0.257, p<1e-7)：高频 types 更容易被提取
3. **但 BCS 与 frequency 正交** (r=-0.079, n.s.)：high-BCS batches 并不系统性地包含高频 types
4. **因此 frequency 不构成 BCS-F1 的混淆变量**：两者相互独立，不存在 confounding path
5. 唯一显著的 within-count 效应在 count_22（r=-0.30, p=0.01），方向是**负**的

对审稿人的回答框架：frequency 确实影响 NER extraction 难度，但它与 BCS 正交，不能解释 BCS-F1 的关系（本身就近乎为零）。

Figure 已保存：`/root/schema-dag-extraction/artifacts/paper/fig_q1_ner_partial_bcs.pdf`

---
