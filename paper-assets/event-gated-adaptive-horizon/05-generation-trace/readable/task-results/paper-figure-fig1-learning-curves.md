# paper figure fig1 learning curves

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_learning_curves_20260515T070014_result.json`
- **Structured JSON:** [`eadb6ccf91b660f3d739.json`](../../sessions/ea/eadb6ccf91b660f3d739.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成并注册。输出文件：

- **PDF**: `artifacts/figures/paper/fig1_learning_curves.pdf`
- **PNG**: `artifacts/figures/paper/fig1_learning_curves.png`

图中可见的关键信息：
- Baseline (dt=1) 稳步上升至 ~916，是最强配置
- 008e_v3 紧随其后达 ~870，验证了 trained dt_emb + dt=1 imagination 的有效性
- 008a 在 ~778 处收敛，波动较大
- Fixed dt=2 (006) 中期达峰后崩溃至 133
- Fixed dt=4 (007) 始终低位徘徊 ~150
- Learned gate (005) 中期冲高后回落
- 008d 标注了红色 ✗ collapse marker，从 167 跌至 83

---
