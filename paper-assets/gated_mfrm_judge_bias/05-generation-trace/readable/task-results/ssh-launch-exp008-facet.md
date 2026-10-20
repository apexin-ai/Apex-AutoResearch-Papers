# ssh launch exp008 facet

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_launch_exp008_facet_20260522T212739_result.json`
- **Structured JSON:** [`45d9e3c7f66e8c305e36.json`](../../sessions/45/45d9e3c7f66e8c305e36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果汇报：

---

## exp-008 Facet Fit Diagnostics 结果

### 1. 代码状态
新创建 `/root/gated_mfrm_judge_bias/exp008/run_exp008.py`

### 2. 全局拟合
| 指标 | 值 | 评估 |
|------|-----|------|
| Global infit MNSQ | 0.870 | 略低于1.0，模型整体偏 overfit（预测过于确定） |
| Global outfit MNSQ | 0.795 | 同上 |

### 3. Model facet — 无异常
全部 8 个模型 infit/outfit 在 [0.63, 1.07]，无 flagged。gpt-4-0613 拟合最好（infit=0.993, outfit=1.068），qwen2.5-72b outfit 最低（0.628）。

### 4. Judge facet — 无异常
全部 9 个 judge 在可接受范围内。gpt-5.5-proxy 拟合最佳（infit=1.006, outfit=1.001，几乎完美）。claude-sonnet-4.6-proxy 和 mistral-large-2 outfit 偏低（~0.6），判分模式比模型预期更规律。

### 5. Item facet — 92/176 flagged
- **5 items overfit（MNSQ > 1.5）**：响应模式与模型预期不一致，最严重的是 `20c9d951` (outfit=3.170) 和 `6b31320632` (outfit=3.010)
- **87 items underfit（MNSQ < 0.5）**：响应过于可预测。这些大多是低观测量（4-6 obs）、低 exposure（e_i≈0）的 items，模型对它们的预测已经很确定

### 6. 整体评估
G-MFRM 模型对 model 和 judge facet 拟合良好，主要问题在 item 层面：
- 大量低观测量 items 的 underfit 是稀疏数据的自然结果（非模型缺陷）
- 少数 overfit items 值得检查——可能包含异常判分模式（如不同 judge 对同一 item 评价高度矛盾）

---
