# research drayson b value

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_drayson-b-value_20260514T084551_result.json`
- **Structured JSON:** [`1df11f761b3611839882.json`](../../sessions/1d/1df11f761b3611839882.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认了原文参数。情况与预期不同：

## 结果

| 来源 | b 值 |
|------|------|
| **Drayson 原文** (Table S1, SmolLM2-1.7B) | **b=1** |
| **我们的代码** (`exp006_filtering_strategies.py:88`) | b=1.5 |
| **我们的论文** (`experiments_c3.tex:18`) | b=1.5 |

**Drayson 原文确认**：Table S1 中 SmolLM2-1.7B 对应 b=1, k=1.5, rmax=3。小模型用 b=10，1.7B 用 b=1。

**实际情况与你的描述不同**：代码中 `BinaryDrayson.__init__` 的默认值是 `b=1.5`（不是 b=1），和论文一致。代码中也没有你提到的 "Table S1: b=1, k=1.5, rmax=3 for SmolLM-1.7B" 注释。

**结论**：代码和论文一致（都是 b=1.5），但**都与 Drayson 原文不符**（原文是 b=1）。exp-006 正在用 b=1.5 跑。

这是个需要你判断的决策：
- 如果目标是忠实复现 Drayson baseline → 应改为 b=1（代码和论文都要改）
- 如果 b=1.5 是有意的选择（比如经过调参）→ 论文中应注明与原文参数不同

请确认方向，我再改。

Sources:
- [Drayson et al. 2025 - Machine-generated text detection prevents language model collapse](https://arxiv.org/abs/2502.15654)
- [Full paper HTML](https://arxiv.org/html/2502.15654)

---
