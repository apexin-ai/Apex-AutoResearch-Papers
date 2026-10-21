# paper fig3 nve diagnostic d054 update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig3_nve_diagnostic_d054_update_20260515T181535_result.json`
- **Structured JSON:** [`9eb84f85759e998b54a8.json`](../../sessions/9e/9eb84f85759e998b54a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**输出文件**：
- 服务器：`/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/fig3_nve_diagnostic_d054.pdf` (+ .png)
- 本地：`artifacts/figures/paper/fig3_nve_diagnostic_d054.{pdf,png,py}`

**D054 修正内容**：
- 008e_v3_s2 标记为 FP（橙色菱形 + "FP (IRD, non-CIVO)" 标注），与 TP（红色圆形）和 TN（蓝色方形）视觉区分
- Stats box: AUROC=0.933, Accuracy=7/8 (87.5%), Task B2 threshold
- Threshold line at NVE=1.5x，左侧蓝色底色（Non-CIVO），右侧红色底色（CIVO-positive）

---
