# analysis held out prediction

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_held_out_prediction_20260523T074112_result.json`
- **Structured JSON:** [`0a86e41dd75c0d132f85.json`](../../sessions/0a/0a86e41dd75c0d132f85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。结果保存到 `artifacts/exp004/data/held_out_prediction.json`，已注册为 `art_20260523_1fc7c0`。

核心发现：

- **数学恒等式**：比例转移后 `predicted_G(target) = G(source)`，因为 total variance 在 G_item 比值中约掉了。预测误差本质上就是 `|G_source - G_target|`。
- **绝对误差低**：5 个 benchmark 的 G_item 落在窄区间 0.863–0.896（CV=1.4%），因此 MAPE 都很小：
  - Within-MC: 1.85%
  - Within-FF: 2.88%
  - Cross-format: 1.88%
  - LOO: 1.62%
- **排名反转**：LOO rank correlation rho = −0.90（p=0.037）。这是数学必然——hold out G 最高的 benchmark 后，剩余 4 个平均 G 最低，反之亦然。
- **关键洞察**：item 测量信度 G_item ≈ 0.88 是跨 benchmark 的稳健属性，但这一相似性来自不同的方差组成（如 MMLU 的 model×item 占 30%、ARC 的 model×prompt 占 8.8%），而非共享的方差结构。

---
