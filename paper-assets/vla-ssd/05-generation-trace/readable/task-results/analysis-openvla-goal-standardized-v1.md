# analysis openvla goal standardized v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_openvla_goal_standardized_v1_20260522T041113_result.json`
- **Structured JSON:** [`34b38f990a788e7bb952.json`](../../sessions/34/34b38f990a788e7bb952.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入并注册 (`art_20260522_df83d8`)。

核心发现：

1. **R2 exit collapse: 未确认**（与 Object/Long/Spatial 不同）。Trained R2 从 L8 到 L31 保持平坦（0.853-0.869），peak-to-exit delta 仅 -0.016。Untrained 反而在 exit 层下降更多（-0.056）。

2. **L1 attention**: Finetuning 将 3 个头从 instruction-dominant 转为 mixed（26→23 instr-dom, 6→9 mixed）。h3/h6/h9/h13/h21/h24 是两个条件共有的 mixed heads。

3. **Cross-instruction**: 两个条件从 L1 起 last_preaction 分类准确率均为 1.0。

4. **RSA**: 两个条件均在 L16_last_preaction 达到峰值（trained 0.607, untrained 0.605），几乎一致。

5. **Counterfactual**: Trained ordering = wrong > empty > shuffled > para; untrained = empty > shuffled > wrong > para。与预期 (empty > wrong > shuffled > para) 有微小排序偏差（top-2 差值 <0.013d），但整体梯度成立。Finetuning 将所有 effect sizes 均匀放大约 +0.3d。

---
